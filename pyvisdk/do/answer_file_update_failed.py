
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AnswerFileUpdateFailed(vim, *args, **kwargs):
    '''Could not update the answer file as it has invalid inputs.'''

    obj = vim.client.factory.create('{urn:vim25}AnswerFileUpdateFailed')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'failure', 'dynamicProperty', 'dynamicType', 'faultCause', 'faultMessage' ]
    optional = [  ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj