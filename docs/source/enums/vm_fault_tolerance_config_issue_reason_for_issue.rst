
==================================================================================================
VmFaultToleranceConfigIssueReasonForIssue
==================================================================================================

.. describe:: VmFaultToleranceConfigIssueReasonForIssue

    

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.esxAgentVm

        The virtual machine is an ESX agent VM vSphere API 5.0

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.ftSecondaryVm

        The virtual machine is a fault tolerance secondary virtual machine

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.ftUnsupportedHardware

        The host ftSupported flag is not set because of hardware issues

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.ftUnsupportedProduct

        The host ftSupported flag is not set because of it is a VMware Server 2.0

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.haNotEnabled

        HA is not enabled on the cluster

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.hasLocalDisk

        The virtual machine has one or more disks on local datastore

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.hasSnapshots

        The virtual machine has one or more snapshots

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.hostInactive

        The host is not active

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.missingFTLoggingNic

        FT logging nic is not configured on the host

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.missingVMotionNic

        No VMotion license or VMotion nic is not configured on the host

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.moreThanOneSecondary

        There is already a secondary virtual machine for the primary virtual machine

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.multipleVCPU

        The virtual machine has more than one virtual CPU

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.noConfig

        No configuration information is available for the virtual machine

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.recordReplayNotSupported

        The virtual machine does not support record/replay. Vm::Capability.RecordReplaySupported is false.

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.replayNotSupported

        It is not possible to turn on Fault Tolerance on this powered-on VM. The support for record/replay should be enabled or Fault Tolerance turned on, when this VM is powered off.

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.templateVm

        The virtual machine is a template

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.thinDisk

        The virtual machine has thin provisioned disks

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.verifySSLCertificateFlagNotSet

        The "check host certificate" flag is not set

    
    .. py:data:: VmFaultToleranceConfigIssueReasonForIssue.video3dEnabled

        The virtual machine video device has 3D enabled vSphere API 5.0

    