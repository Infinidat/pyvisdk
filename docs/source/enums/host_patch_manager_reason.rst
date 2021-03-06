
==================================================================================================
HostPatchManagerReason
==================================================================================================

.. describe:: HostPatchManagerReason

    Reasons why an update is not applicable to the ESX host.

    
    .. py:data:: HostPatchManagerReason.conflictLib

        The update conflicts with RPMs or libraries installed on the host.

    
    .. py:data:: HostPatchManagerReason.conflictPatch

        The update conflicts with certain updates that are already installed on the host.

    
    .. py:data:: HostPatchManagerReason.hasDependentPatch

        The update depends on an update that is not installed but is in the scanned list of updates.

    
    .. py:data:: HostPatchManagerReason.missingLib

        The update depends on certain libraries or RPMs that are not available.

    
    .. py:data:: HostPatchManagerReason.missingPatch

        The update depends on another update that is neither installed nor in the scanned list of updates.

    
    .. py:data:: HostPatchManagerReason.obsoleted

        The update is made obsolete by other patches installed on the host.

    