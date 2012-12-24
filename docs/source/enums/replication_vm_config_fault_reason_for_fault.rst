
==================================================================================================
ReplicationVmConfigFaultReasonForFault
==================================================================================================

.. describe:: ReplicationVmConfigFaultReasonForFault

    

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.cannotRetrieveVmReplicationConfiguration

        Could not retrieve the VM configuration

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.incompatibleHwVersion

        Incompatible VM hardware version

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidDestinationIpAddress

        Invalid destination IP address

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidDestinationPort

        Invalid destination port

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidExtraVmOptions

        Malformed extra options list

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidGenerationNumber

        Invalid generation number in VM's configuration

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidPriorConfiguration

        The existing replication configuration of the VM is broken (applicable to re-configuration only).

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.invalidVmReplicationId

        Invalid VM Replication ID string

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.outOfBoundsRpoValue

        Invalid RPO value (out of bounds)

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.reconfigureVmReplicationIdNotAllowed

        Attempting to re-configure the VM replication ID

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.replicationAlreadyEnabled

        Attempting to re-enable replication for the VM

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.replicationConfigurationFailed

        Failed to commit the new replication properties for the VM.

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.replicationNotEnabled

        Attempting to re-configure or disable replication for a VM for which replication has not been enabled.

    
    .. py:data:: ReplicationVmConfigFaultReasonForFault.staleGenerationNumber

        Mis-matching generation number (stale)

    