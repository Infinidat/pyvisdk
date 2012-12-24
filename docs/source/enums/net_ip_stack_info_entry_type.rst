
==================================================================================================
NetIpStackInfoEntryType
==================================================================================================

.. describe:: NetIpStackInfoEntryType

    IP Stack keeps state on entries in IpNetToMedia table to perform physical address lookups for IP addresses. Here are the standard states perSee RFC

    
    .. py:data:: NetIpStackInfoEntryType.dynamic

        This entry has been learned using ARP or NDP.

    
    .. py:data:: NetIpStackInfoEntryType.invalid

        The IP Stack has marked this entry as not useable.

    
    .. py:data:: NetIpStackInfoEntryType.manual

        This entry was set manually.

    
    .. py:data:: NetIpStackInfoEntryType.other

        This implementation is reporting something other than what states are listed below.

    