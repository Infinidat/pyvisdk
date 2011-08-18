# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ObjectUpdate(vim, *args, **kwargs):
    '''The ObjectUpdate data object type contains information about changes to a
    particular managed object. We distinguish updates when an object is created,
    destroyed, or modified, as well as when the object enters or leaves the set of
    objects dynamically associated with a filter.'''
    
    obj = vim.client.factory.create('ns0:ObjectUpdate')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'changeSet', 'kind', 'missingSet', 'obj' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    