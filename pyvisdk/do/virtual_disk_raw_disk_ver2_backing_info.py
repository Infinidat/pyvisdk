# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskVer2BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk by
    using a host device, as used by VMware Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskVer2BackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'deviceName' ]
    inherited = [ 'useAutoDetect', 'changeId', 'descriptorFileName', 'uuid' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    