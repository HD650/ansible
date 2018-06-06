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

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    
    def __init__(self):
        super(CallbackModule, self).__init__()

    def runner_on_ok(self, host, result):
        self._display.display(str(result))
        self._display.banner("[OK] " + str(host))
