
==================================================================================================
DistributedVirtualPortgroupPortgroupType
==================================================================================================

.. describe:: DistributedVirtualPortgroupPortgroupType

    The DistributedVirtualPortgroup types.

    
    .. py:data:: DistributedVirtualPortgroupPortgroupType.earlyBinding

        A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is reconfigured to connect to the portgroup.

    
    .. py:data:: DistributedVirtualPortgroupPortgroupType.ephemeral

        A DistributedVirtualPort will be created and assigned to a Virtual Machine when the Virtual Machine is powered on, and will be deleted when the Virtual Machine is powered off. An ephemeral portgroup has no limit on the number of ports that can be a part of this portgroup. In cases where the vCenter Server is unavailable the host can create conflict ports in this portgroup to be used by a Virtual Machine at power on.

    
    .. py:data:: DistributedVirtualPortgroupPortgroupType.lateBinding

        deprecated as of vSphere API 5.0 A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is powered on.

    