# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AuthorizationRole(vim, *args, **kwargs):
    '''This data object type specifies a collection of privileges used to grant access
    to users on managed entities.'''
    
    obj = vim.client.factory.create('ns0:AuthorizationRole')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'info', 'name' ]
    inherited = [ 'privilege', 'roleId', 'system' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    