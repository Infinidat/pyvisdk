
==================================================================================================
DistributedVirtualSwitchProductSpecOperationType
==================================================================================================

.. describe:: DistributedVirtualSwitchProductSpecOperationType

    The product spec operation types.

    
    .. py:data:: DistributedVirtualSwitchProductSpecOperationType.notifyAvailableUpgrade

        Set the product information for an available switch upgrade that would be done by the switch implementation. This operation will post a config issue on the switch to signal the availability of an upgrade. This operation is applicable only in the case when switch policy autoUpgradeAllowed is set to false.

    
    .. py:data:: DistributedVirtualSwitchProductSpecOperationType.preInstall

        Push the switch's host component of the specified product info to the host members of the switch at a fixed location known by the host.

    
    .. py:data:: DistributedVirtualSwitchProductSpecOperationType.proceedWithUpgrade

        If productSpec is set to be same as that in the DvsUpgradeAvailableEvent configIssue, the switch implementation will proceed with the upgrade. To reject or stop the upgrade, leave the productSpec unset. If productSpec is set but does not match that in DvsUpgradeAvailableEvent configIssue, a fault will be raised. This operation is applicable only in the case when switch policy autoUpgradeAllowed is set to false.

    
    .. py:data:: DistributedVirtualSwitchProductSpecOperationType.updateBundleInfo

        Update the bundle URL and ID information. If other properties in the specified product info differ from the corresponding properties of the switch's product info, a fault will be thrown. Updating the bundle ID will result in installing the new host component identified by the bundle ID.

    
    .. py:data:: DistributedVirtualSwitchProductSpecOperationType.upgrade

        Change the switch implementation to use the specified one. If the property values in the specified product info are different from those of the corresponding properties in the switch's product info, a host component preinstall and switch upgrade will be performed.

    