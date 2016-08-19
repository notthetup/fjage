"""Shell: Support for interactive shell and command scripts.

Copyright (c) 2016, Manu Ignatius

This file is part of fjage which is released under Simplified BSD License.
See file LICENSE.txt or go to http://www.opensource.org/licenses/BSD-3-Clause
for full license details.

"""
from fjage import Message
from fjage import Performative

class ShellExecReq(Message):
    """Request to execute shell command/script.

    Attributes:
        cmd
        script
        args

    Guidelines for directly operating on the attributes are as follows:
    1. IMPORTANT: ShellExecReq can either have a command or script, but not both
    2. cmd can be any command (str) supported by the shell
    3. script is a dictionary which contains the path to the script file. E.g. "script":{"path":"samples/01_hello.groovy"}
    4. script has to be accompanied with arguments.
    5. args is a list containing arguments to the script. E.g. []

    """

    def __init__(self, **kwargs):

        super(ShellExecReq, self).__init__()
        self.perf = Performative.REQUEST
        self.cmd = None
        self.script = None
        self.args = None
        self.__dict__.update(kwargs)
