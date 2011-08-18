# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EnteringMaintenanceModeEvent(vim, *args, **kwargs):
    '''This event records that a host has begun the process of entering maintenance
    mode. All virtual machine operations are blocked, except the following:'''
    
    obj = vim.client.factory.create('ns0:EnteringMaintenanceModeEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'chainId' ]
    inherited = [ 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    