
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasVmSettings(vim, *args, **kwargs):
    '''The ClusterDasVmSettings data object contains the HA configuration settings
    specified for a single virtual machine (identified by
    ClusterDasVmConfigInfo.key) or as cluster-wide defaults
    (ClusterDasConfigInfo.defaultVmSettings).All fields are optional. If you set
    the parameter to when you call ReconfigureComputeResource_Task, an unset
    property has no effect on the existing property value in the cluster
    configuration on the Server. If you set the parameter to when you reconfigure a
    cluster, the cluster configuration is reverted to the default values, then the
    new configuration values are applied.'''
    
    obj = vim.client.factory.create('{urn:vim25}ClusterDasVmSettings')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'isolationResponse', 'restartPriority', 'vmToolsMonitoringSettings',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    