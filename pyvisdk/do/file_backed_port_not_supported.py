
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileBackedPortNotSupported(vim, *args, **kwargs):
    '''The virtual machine has a port (either a SerialPort or a ParallelPort) which is
    backed by a file. This is an error when migrating a virtual machine with the
    device connected, and can be returned as a subfault of
    DisallowedMigrationDeviceAttached.'''

    obj = vim.client.factory.create('{urn:vim25}FileBackedPortNotSupported')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'device', 'reason', 'dynamicProperty', 'dynamicType', 'faultCause',
        'faultMessage' ]
    optional = [  ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
