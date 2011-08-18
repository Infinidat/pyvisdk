# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGuiUnattended(vim, *args, **kwargs):
    '''The GuiUnattended type maps to the GuiUnattended key in the answer file. These
    values are plugged directly into the file that VirtualCenter stores on the
    target virtual disk. For more detailed information, see the document'''
    
    obj = vim.client.factory.create('ns0:CustomizationGuiUnattended')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'autoLogon', 'autoLogonCount' ]
    inherited = [ 'password', 'timeZone' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    