
==================================================================================================
HostPatchManagerIntegrityStatus
==================================================================================================

.. describe:: HostPatchManagerIntegrityStatus

    The integrity validation status.

    
    .. py:data:: HostPatchManagerIntegrityStatus.digestMismatch

        A digital signature of the update does not match.

    
    .. py:data:: HostPatchManagerIntegrityStatus.keyExpired

        A public key to verify the update is expired.

    
    .. py:data:: HostPatchManagerIntegrityStatus.keyNotFound

        The integrity can not be verified since a public key to verify the update cannot be found.

    
    .. py:data:: HostPatchManagerIntegrityStatus.keyRevoked

        A public key to verify the update has been revoked.

    
    .. py:data:: HostPatchManagerIntegrityStatus.notEnoughSignatures

        Not enough signed signatures on the update.

    
    .. py:data:: HostPatchManagerIntegrityStatus.validated

        The update is successfully validated.

    
    .. py:data:: HostPatchManagerIntegrityStatus.validationError

        The integrity validation failed.

    