
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsFaultsFaultsByVirtualDisk(vim, *args, **kwargs):
    '''The faults generated by storage DRS when it tries to move a virtual disk.NOTE:
    This data object type and all of its fields are experimental and subject to
    change in future releases.'''

    obj = vim.client.factory.create('{urn:vim25}ClusterDrsFaultsFaultsByVirtualDisk')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'fault' ]
    optional = [ 'disk', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
