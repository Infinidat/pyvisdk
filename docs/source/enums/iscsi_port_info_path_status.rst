
==================================================================================================
IscsiPortInfoPathStatus
==================================================================================================

.. describe:: IscsiPortInfoPathStatus

    

    
    .. py:data:: IscsiPortInfoPathStatus.active

        All paths on this Virtual NIC are standby paths from SCSI stack perspective.

    
    .. py:data:: IscsiPortInfoPathStatus.lastActive

        One or more paths on the Virtual NIC is the last active path to a particular storage device.

    
    .. py:data:: IscsiPortInfoPathStatus.notUsed

        There are no paths on this Virtual NIC

    
    .. py:data:: IscsiPortInfoPathStatus.standBy

        One or more paths on the Virtual NIC are active paths to storage. Unbinding this Virtual NIC will cause storage path transitions.

    