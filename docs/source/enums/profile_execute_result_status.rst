
==================================================================================================
ProfileExecuteResultStatus
==================================================================================================

.. describe:: ProfileExecuteResultStatus

    Defines the result status values for a HostProfile.ExecuteHostProfile operation. The result data is contained in the ProfileExecuteResult data object.

    
    .. py:data:: ProfileExecuteResultStatus.error

        Profile execution generated an error. See ProfileExecuteResult.error.

    
    .. py:data:: ProfileExecuteResultStatus.needInput

        Additional data is required to complete the operation. The data requirements are defined in the list of policy options for the profile (ApplyProfile.policy[]).

    
    .. py:data:: ProfileExecuteResultStatus.success

        Profile execution was successful. You can use the output configuration data to apply the profile to a host.

    