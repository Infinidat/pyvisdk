
==================================================================================================
VirtualMachineToolsVersionStatus
==================================================================================================

.. describe:: VirtualMachineToolsVersionStatus

    Current version status of VMware Tools installed in the guest operating system.

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsBlacklisted

        VMware Tools is installed, but the installed version is known to have a grave bug and should be immediately upgraded. vSphere API 5.0

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsCurrent

        VMware Tools is installed, and the version is current.

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsNeedUpgrade

        VMware Tools is installed, but the version is not current.

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsNotInstalled

        VMware Tools has never been installed.

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsSupportedNew

        VMware Tools is installed, supported, and newer than the version available on the host. vSphere API 5.0

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsSupportedOld

        VMware Tools is installed, supported, but a newer version is available. vSphere API 5.0

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsTooNew

        VMware Tools is installed, and the version is known to be too new to work correctly with this virtual machine. vSphere API 5.0

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsTooOld

        VMware Tools is installed, but the version is too old. vSphere API 5.0

    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsUnmanaged

        VMware Tools is installed, but it is not managed by VMWare.

    