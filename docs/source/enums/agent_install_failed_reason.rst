
==================================================================================================
AgentInstallFailedReason
==================================================================================================

.. describe:: AgentInstallFailedReason

    

    
    .. py:data:: AgentInstallFailedReason.AgentNotReachable

        The agent was installed but did not respond to requests.

    
    .. py:data:: AgentInstallFailedReason.AgentNotRunning

        The agent was installed but is not running.

    
    .. py:data:: AgentInstallFailedReason.AgentUploadFailed

        Failed to upload the agent installer.

    
    .. py:data:: AgentInstallFailedReason.AgentUploadTimedout

        The agent upload took too long.

    
    .. py:data:: AgentInstallFailedReason.InstallTimedout

        The agent install took too long.

    
    .. py:data:: AgentInstallFailedReason.NotEnoughSpaceOnDevice

        There is not enough storage space on the host to install the agent.

    
    .. py:data:: AgentInstallFailedReason.PrepareToUpgradeFailed

        Failed to initialize the upgrade directory on the host.

    
    .. py:data:: AgentInstallFailedReason.SignatureVerificationFailed

        The signature verification for the installer failed.

    
    .. py:data:: AgentInstallFailedReason.UnknownInstallerError

        The agent installer failed for an unknown reason.

    