# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortgroupPolicy(vim, *args, **kwargs):
    '''The DistributedVirtualPortgroup policies. This field is not applicable when
    queried directly against an ESX host.'''
    
    obj = vim.client.factory.create('ns0:DVPortgroupPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'blockOverrideAllowed', 'livePortMovingAllowed', 'portConfigResetAtDisconnect',
        'shapingOverrideAllowed', 'vendorConfigOverrideAllowed' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    