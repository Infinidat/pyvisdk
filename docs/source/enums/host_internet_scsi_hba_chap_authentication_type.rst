
==================================================================================================
HostInternetScsiHbaChapAuthenticationType
==================================================================================================

.. describe:: HostInternetScsiHbaChapAuthenticationType

    The type of CHAP authentication setting to use. prohibited : do not use CHAP. preferred : use CHAP if successfully negotiated, but allow non-CHAP connections as fallback discouraged : use non-CHAP, but allow CHAP connectsion as fallback required : use CHAP for connection strictly, and fail if CHAP negotiation fails. Defaults to preferred on first configuration if unspecified.

    
    .. py:data:: HostInternetScsiHbaChapAuthenticationType.chapDiscouraged

        

    
    .. py:data:: HostInternetScsiHbaChapAuthenticationType.chapPreferred

        

    
    .. py:data:: HostInternetScsiHbaChapAuthenticationType.chapProhibited

        

    
    .. py:data:: HostInternetScsiHbaChapAuthenticationType.chapRequired

        

    