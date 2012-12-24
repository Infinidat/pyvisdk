
==================================================================================================
VmwareDistributedVirtualSwitchPvlanPortType
==================================================================================================

.. describe:: VmwareDistributedVirtualSwitchPvlanPortType

    The PVLAN port types.

    
    .. py:data:: VmwareDistributedVirtualSwitchPvlanPortType.community

        The ports communicates with other community ports and with promiscuous ports within the same PVLAN. any other traffics are blocked.

    
    .. py:data:: VmwareDistributedVirtualSwitchPvlanPortType.isolated

        The port can only communicate with the promiscuous ports within the same PVLAN, any other traffics are blocked.

    
    .. py:data:: VmwareDistributedVirtualSwitchPvlanPortType.promiscuous

        The port can communicate with all other ports within the same PVLAN, including the isolated and community ports .

    