
==================================================================================================
ScsiLunVStorageSupportStatus
==================================================================================================

.. describe:: ScsiLunVStorageSupportStatus

    Storage array hardware acceleration support status. When a host boots, the support status is unknown. As a host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the vStorageSupport property accordingly.
    
    
    .. py:data:: ScsiLunVStorageSupportStatus.vStorageSupported
    
        Storage device supports hardware acceleration. The ESX host will use the feature to offload certain storage-related operations to the device.
        
    
    .. py:data:: ScsiLunVStorageSupportStatus.vStorageUnknown
    
        Initial support status value.
        
    
    .. py:data:: ScsiLunVStorageSupportStatus.vStorageUnsupported
    
        Storage device does not support hardware acceleration. The ESX host will handle all storage-related operations.
        
    