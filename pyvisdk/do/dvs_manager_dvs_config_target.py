
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSManagerDvsConfigTarget(vim, *args, **kwargs):
    '''Configuration specification for a DistributedVirtualSwitch or
    DistributedVirtualPortgroup.'''

    obj = vim.client.factory.create('{urn:vim25}DVSManagerDvsConfigTarget')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'distributedVirtualPortgroup', 'distributedVirtualSwitch', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
