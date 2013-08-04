
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SoftRuleVioCorrectionImpact(vim, *args, **kwargs):
    '''DRS has determined that correcting the soft VM/Host affinity rules constraint
    violation for the VM impacts respecting cluster constraints or performance
    goals so the violation will not be corrected.'''

    obj = vim.client.factory.create('{urn:vim25}SoftRuleVioCorrectionImpact')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'vmName', 'dynamicProperty', 'dynamicType', 'faultCause', 'faultMessage' ]
    optional = [  ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
