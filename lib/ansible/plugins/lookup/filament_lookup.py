from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
    import subprocess
    from ansible.module_utils._text import to_text
    import epdb
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        display.vvv("got your argument "+str(terms))
        
        command = None
        # if no argument passed, show process table
        if len(terms)is 0:
            command = "ps aux"
        elif len(terms) is 1:
            command = "ps aux|grep " + str(terms[0])
        else:
            raise AnsibleError("Argument Fault: 1 string argument expect, {0} got.".format(len(terms))) 

        display.vvv(command)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        epdb.st()
        result = p.stdout.read()
        result = to_text(result)
        display.vvv(result)
        return to_text(result)
