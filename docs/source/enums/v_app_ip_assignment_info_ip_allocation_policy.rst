
==================================================================================================
VAppIPAssignmentInfoIpAllocationPolicy
==================================================================================================

.. describe:: VAppIPAssignmentInfoIpAllocationPolicy

    IP allocation policy for a deployment.

    
    .. py:data:: VAppIPAssignmentInfoIpAllocationPolicy.dhcpPolicy

        Specifies that DHCP must be used to allocate IP addresses to the vApp

    
    .. py:data:: VAppIPAssignmentInfoIpAllocationPolicy.fixedPolicy

        Specifies that IP allocation is done through the range managed by the VI platform. The IP addresses are allocated when the vApp is deployed and will be kept with the server as long as it is deployed. This will ensure that a vApp will get a consistent IP for the life-time of the deployment.

    
    .. py:data:: VAppIPAssignmentInfoIpAllocationPolicy.transientPolicy

        Specifies that IP allocation is done through the range managed by the VI platform. The IP addresses are allocated when needed, typically at power-on, and deallocated during power-off. There is no guantee that a vApp will get the same IP address when restarted.

    