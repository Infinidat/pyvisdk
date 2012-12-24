
==================================================================================================
VirtualMachineConfigInfoSwapPlacementType
==================================================================================================

.. describe:: VirtualMachineConfigInfoSwapPlacementType

    Available choices for virtual machine swapfile placement policy. This is the set of legal values for the virtual machine configuration's swapPlacement property. All values except for "inherit" and "vmConfigured" are also valid values for a compute resource configuration's vmSwapPlacement property.

    
    .. py:data:: VirtualMachineConfigInfoSwapPlacementType.hostLocal

        Store the swapfile in the datastore specified by the localSwapDatastore property of the virtual machine's host, if that property is set and indicates a datastore with sufficient free space. Otherwise store the swapfile in the same directory as the virtual machine.

    
    .. py:data:: VirtualMachineConfigInfoSwapPlacementType.inherit

        Honor the virtual machine swapfile placement policy of the compute resource that contains this virtual machine.

    
    .. py:data:: VirtualMachineConfigInfoSwapPlacementType.vmDirectory

        Store the swapfile in the same directory as the virtual machine.

    