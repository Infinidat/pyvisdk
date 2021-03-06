
==================================================================================================
VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm
==================================================================================================

.. describe:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm

    

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptConflictingIOChainConfigured

        Some networking feature has placed a conflicting IOChain on the network adapter, which prevents VMDirectPath Gen 2. Examples include DVFilter.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptConflictingOperationInProgress

        VMDirectPath Gen 2 is temporarily suspended while the virtual machine executes an operation such as suspend.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptDisabledOrDisconnectedAdapter

        The virtual machine's network adapter is disabled or disconnected, and thus is not participating in VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptFaultToleranceOrRecordReplayConfigured

        The virtual machine is configured for Fault Tolerance or Record & Replay, which prevents VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptIncompatibleAdapterFeatures

        The virtual machine's network adapter has features enabled which preclude it participating in VMDirectPath Gen 2 such as INT-x or PXE booting.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptIncompatibleAdapterType

        The device type does not support VMDirectPath Gen 2.See vmDirectPathGen2Supported

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptIncompatibleBackingType

        The device backing is not a DistributedVirtualPortBacking.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptIncompatibleGuest

        The virtual machine's guest OS does not support VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptIncompatibleGuestDriver

        The virtual machine's guest network driver does not support VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptInsufficientMemoryReservation

        The virtual machine does not have full memory reservation required to activate VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptMonitorBlocks

        The virtual machine monitor is exercising functionality which which prevents VMDirectPath Gen 2.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptOutOfIntrVector

        VMDirectPath Gen 2 is unavailable due to host run out of intr vector in host. Guest can configure the vNIC to use less rx/tx queues or use MSI instead of MSIX.

    
    .. py:data:: VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVm.vmNptRuntimeError

        VMDirectPath Gen 2 is unavailable due to an unforeseen runtime error in the virtualization platform (typically resource constraints.)

    