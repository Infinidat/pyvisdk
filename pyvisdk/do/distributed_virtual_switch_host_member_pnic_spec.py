
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchHostMemberPnicSpec(vim, *args, **kwargs):
    '''Specification to select individual physical NICs. In this case, a proxy switch
    will be created on the host from scratch with the pNICs as the uplinks.'''

    obj = vim.client.factory.create('{urn:vim25}DistributedVirtualSwitchHostMemberPnicSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'pnicDevice' ]
    optional = [ 'connectionCookie', 'uplinkPortgroupKey', 'uplinkPortKey', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
