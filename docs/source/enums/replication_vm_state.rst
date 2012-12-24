
==================================================================================================
ReplicationVmState
==================================================================================================

.. describe:: ReplicationVmState

    Describes the current state of a replicated VirtualMachine

    
    .. py:data:: ReplicationVmState.active

        The VirtualMachine is in the process of having a consistent instance created.

    
    .. py:data:: ReplicationVmState.error

        The VirtualMachine is unable to replicate due to errors.

    
    .. py:data:: ReplicationVmState.idle

        The VirtualMachine is being replicated but is not currently in the process of having a consistent instance created.

    
    .. py:data:: ReplicationVmState.none

        The VirtualMachine has no current replication state. This is a virtual machine that is configured for replication, but is powered off and not undergoing offline replication.

    
    .. py:data:: ReplicationVmState.paused

        The VirtualMachine replication is paused.

    
    .. py:data:: ReplicationVmState.syncing

        One or more of the VirtualMachine disks is in the process of an initial synchronization with the remote site.

    