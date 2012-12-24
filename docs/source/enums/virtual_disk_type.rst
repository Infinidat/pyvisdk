
==================================================================================================
VirtualDiskType
==================================================================================================

.. describe:: VirtualDiskType

    The types of virtual disks that can be created or cloned.

    
    .. py:data:: VirtualDiskType.eagerZeroedThick

        An eager zeroed thick disk has all space allocated and wiped clean of any previous contents on the physical media at creation time. Such disks may take longer time during creation compared to other disk formats.

    
    .. py:data:: VirtualDiskType.flatMonolithic

        A preallocated monolithic disk. Disks in this format can be used with other VMware products. This format is only applicable as a destination format in a clone operation, and not usable for disk creation. vSphere API 4.0

    
    .. py:data:: VirtualDiskType.preallocated

        A preallocated disk has all space allocated at creation time and the space is zeroed on demand as the space is used.

    
    .. py:data:: VirtualDiskType.raw

        Raw device.

    
    .. py:data:: VirtualDiskType.rdm

        Virtual compatibility mode raw disk mapping. An rdm virtual disk grants access to the entire raw disk and the virtual disk can participate in snapshots.

    
    .. py:data:: VirtualDiskType.rdmp

        Physical compatibility mode (pass-through) raw disk mapping. An rdmp virtual disk passes SCSI commands directly to the hardware, but the virtual disk cannot participate in snapshots.

    
    .. py:data:: VirtualDiskType.sparse2Gb

        A sparse disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

    
    .. py:data:: VirtualDiskType.sparseMonolithic

        A sparse monolithic disk. Disks in this format can be used with other VMware products. This format is only applicable as a destination format in a clone operation, and not usable for disk creation. vSphere API 4.0

    
    .. py:data:: VirtualDiskType.thick

        A thick disk has all space allocated at creation time. This space may contain stale data on the physical media. Thick disks are primarily used for virtual machine clustering, but they are generally insecure and should not be used. Due to better performance and security properties, the use of the 'preallocated' format is preferred over this format.

    
    .. py:data:: VirtualDiskType.thick2Gb

        A thick disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

    
    .. py:data:: VirtualDiskType.thin

        Space required for thin-provisioned virtual disk is allocated and zeroed on demand as the space is used.

    