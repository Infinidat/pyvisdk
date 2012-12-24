
==================================================================================================
OvfCreateImportSpecParamsDiskProvisioningType
==================================================================================================

.. describe:: OvfCreateImportSpecParamsDiskProvisioningType

    Types of disk provisioning that can be set for the disk in the deployed OVF package.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.eagerZeroedThick

        An eager zeroed thick disk has all space allocated and wiped clean of any previous contents on the physical media at creation time. Such disks may take longer time during creation compared to other disk formats. vSphere API 5.0

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.flat

        Depending on the host type, Flat is mapped to either MonolithicFlat or Thick.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.monolithicFlat

        A preallocated monolithic disk. Disks in this format can be used with other VMware products.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.monolithicSparse

        A sparse (allocate on demand) monolithic disk. Disks in this format can be used with other VMware products.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.sparse

        Depending on the host type, Sparse is mapped to either MonolithicSparse or Thin.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.thick

        A thick disk has all space allocated at creation time and the space is zeroed on demand as the space is used.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.thin

        Space required for thin-provisioned virtual disk is allocated and zeroed on demand as the space is used.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.twoGbMaxExtentFlat

        A preallocated disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files.

    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.twoGbMaxExtentSparse

        A sparse (allocate on demand) disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files.

    