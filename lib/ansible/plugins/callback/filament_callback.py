# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: filament
    type: stdout
    short_description: a filament display
    description:
      - a filament display, do the normal output logic
    version_added: "2.4"
    requirements:
      - set as stdout in configuration
'''

from ansible import constants as C
from ansible.playbook.task_include import TaskInclude
from ansible.plugins.callback import CallbackBase
import epdb

class CallbackModule(CallbackBase):
    
    def __init__(self):
        super(CallbackModule, self).__init__()

    def v2_runner_on_failed(self, result, ignore_errors=False):
        # if we met error, print the error
        self._display.display("fatal: [%s]: FAILED! => %s " % (result._host.get_name(), self._dump_result(result._result)), color=C.COLOR_ERROR)

    def v2_runner_on_ok(self, result):
        epdb.st()
        if isinstance(result._task, TaskInclude):
            return
        if result._result.get('changed', False):
            msg = "changed: [%s]" % result._host.get_name()
        else:
            msg = "ok: [%s]" % result._host.get_name()

        msg += " => %s" % self._dump_results(result._result)
        self._display.display(msg, color=C.COLOR_OK)

    def v2_runner_on_skipped(self, result):
        msg = "skipping: [%s]" % result._host.get_name()
        msg += " => %s" % self._dump_results(result._result)
        self._display.display(msg, color=C.COLOR_SKIP)
