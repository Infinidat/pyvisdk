
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UserGroupProfile(vim, *args, **kwargs):
    '''The UserGroupProfile data object represents a user group. Use the policy list
    for access to configuration data for the user group profile. Use the property
    list for access to subprofile configuration data, if any.'''

    obj = vim.client.factory.create('{urn:vim25}UserGroupProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'key', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
