
==================================================================================================
VmFailedStartingSecondaryEventFailureReason
==================================================================================================

.. describe:: VmFailedStartingSecondaryEventFailureReason

    The reason for the failure.

    
    .. py:data:: VmFailedStartingSecondaryEventFailureReason.incompatibleHost

        Remote host is incompatible for secondary virtual machine. For instance, the host doesn't have access to the virtual machine's network or datastore.

    
    .. py:data:: VmFailedStartingSecondaryEventFailureReason.loginFailed

        Login to remote host failed.

    
    .. py:data:: VmFailedStartingSecondaryEventFailureReason.migrateFailed

        Migration failed.

    
    .. py:data:: VmFailedStartingSecondaryEventFailureReason.registerVmFailed

        Registration of the secondary virtual machine on the remote host failed.

    