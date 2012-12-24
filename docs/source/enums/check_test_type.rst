
==================================================================================================
CheckTestType
==================================================================================================

.. describe:: CheckTestType

    The types of tests which can requested by any of the methods in either VirtualMachineCompatibilityChecker or VirtualMachineProvisioningChecker.

    
    .. py:data:: CheckTestType.datastoreTests

        Tests that check that the destination host or cluster can see the datastores where the virtual machine's virtual disks are goint to be located. The destination resource pool is irrelevant.

    
    .. py:data:: CheckTestType.hostTests

        Tests that examine both the virtual machine and the destination host or cluster; the destination resource pool is irrelevant. This set excludes tests that fall into the datastoreTests group.

    
    .. py:data:: CheckTestType.resourcePoolTests

        Tests that check that the destination resource pool can support the virtual machine if it is powered on. The destination host or cluster is relevant because it will affect the amount of overhead memory required to run the virtual machine.

    
    .. py:data:: CheckTestType.sourceTests

        Tests that examine only the configuration of the virtual machine and its current host; the destination resource pool and host or cluster are irrelevant.

    