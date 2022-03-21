
# Simple Jupyter kernel for Crystal
# Forked from https://github.com/takluyver/bash_kernel

from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF
import pexpect

from subprocess import check_output
import os.path

import re
import signal

__version__ = '0.0.2'

version_pat = re.compile(r'version (\d+(\.\d+)+)')


class IREPLWrapper(replwrap.REPLWrapper):
    def __init__(self, cmd_or_spawn, orig_prompt, prompt_change,
                 extra_init_cmd=None, line_output_callback=None):
        self.line_output_callback = line_output_callback
        replwrap.REPLWrapper.__init__(
            self,
            cmd_or_spawn,
            orig_prompt,
            prompt_change,
            extra_init_cmd=extra_init_cmd)

    def _expect_prompt(self, timeout=-1):
        if timeout is None:
            # "None" means we are executing code from a Jupyter cell by way of the run_command
            # in the do_execute() code below, so do incremental output.
            while True:
                # Use expect(pattern) instead of expect_expect(string)
                # because the crystal interpreter prompt includes line numbers.
                pos = self.child.expect([self.prompt, r'\r\n'],
                                        timeout=None)
                if pos == 1:
                    # End of line received
                    self.line_output_callback(self.child.before + '\n')
                else:
                    if len(self.child.before) != 0:
                        # prompt received, but partial line precedes it
                        self.line_output_callback(self.child.before)
                    break
        else:
            # Otherwise, use existing non-incremental code
            # Use expect(pattern) instead of expect_expect(string)
            # because the crystal interpreter prompt includes line numbers.
            pos = self.child.expect([self.prompt], timeout=timeout)

        # Prompt received, so return normally
        return pos


class CrystalKernel(Kernel):
    implementation = 'crystal_kernel'
    implementation_version = __version__

    @property
    def language_version(self):
        m = version_pat.search(self.banner)
        return m.group(1)

    _banner = None

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output(
                ['crystal', '--version']).decode('utf-8')
        return self._banner

    language_info = {'name': 'crystal',
                     'codemirror_mode': 'shell',
                     'mimetype': 'text/x-crystal',
                     'file_extension': '.cr'}

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self._start_crystal()

    def _start_crystal(self):
        # Signal handlers are inherited by forked processes, and we can't easily
        # reset it from the subprocess. Since kernelapp ignores SIGINT except in
        # message handlers, we need to temporarily reset the SIGINT handler here
        # so that crystal and its children are interruptible.
        sig = signal.signal(signal.SIGINT, signal.SIG_DFL)
        try:
            child = pexpect.spawn(
                "crystal",
                ['i'],
                echo=False,
                encoding='utf-8',
                codec_errors='replace')
            # Pattern should be used to avoid line numbers.
            # See (#1) for [>\*].
            prompt_regexp = r'^icr:\d+:\d+[>\*] '
            # Using IREPLWrapper to get incremental output
            self.crystalwrapper = IREPLWrapper(
                child, prompt_regexp, None, line_output_callback=self.process_output)
        finally:
            signal.signal(signal.SIGINT, sig)

    def process_output(self, output):
        if not self.silent:
            # Send standard output
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        self.silent = silent
        if not code.strip():
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

        interrupted = False
        try:
            # Note: timeout=None tells IREPLWrapper to do incremental
            # output.  Also note that the return value from
            # run_command is not needed, because the output was
            # already sent by IREPLWrapper.
            self.crystalwrapper.run_command(code.rstrip(), timeout=None)
        except KeyboardInterrupt:
            self.crystalwrapper.child.sendintr()
            interrupted = True
            self.crystalwrapper._expect_prompt()
            output = self.crystalwrapper.child.before
            self.process_output(output)
        except EOF:
            output = self.crystalwrapper.child.before
            self.process_output(output)

        if interrupted:
            return {'status': 'abort', 'execution_count': self.execution_count}

        return {'status': 'ok', 'execution_count': self.execution_count,
                'payload': [], 'user_expressions': {}}
