
==================================================================================================
ClusterDasConfigInfoVmMonitoringState
==================================================================================================

.. describe:: ClusterDasConfigInfoVmMonitoringState

    The ClusterDasConfigInfoVmMonitoringState enum defines values that indicate the state of Virtual Machine Health Monitoring. Health Monitoring uses the vmTools (guest) and application agent heartbeat modules. You can configure HA to respond to heartbeat failures of either one or both modules. You can also disable the HA response to heartbeat failures.

    
    .. py:data:: ClusterDasConfigInfoVmMonitoringState.vmAndAppMonitoring

        HA response to both guest and application heartbeat failure is enabled.
          
            * To retrieve the guest heartbeat status, use the VirtualMachine.guestHeartbeatStatus property.
            
            * To retrieve the application heartbeat status, use the GuestInfo.appHeartbeatStatus property.

    
    .. py:data:: ClusterDasConfigInfoVmMonitoringState.vmMonitoringDisabled

        Virtual machine health monitoring is disabled. In this state, HA response to guest and application heartbeat failures are disabled.

    
    .. py:data:: ClusterDasConfigInfoVmMonitoringState.vmMonitoringOnly

        HA response to guest heartbeat failure is enabled. To retrieve the guest heartbeat status, use the VirtualMachine.guestHeartbeatStatus property.

    