
==================================================================================================
SlpDiscoveryMethod
==================================================================================================

.. describe:: SlpDiscoveryMethod

    The available SLP discovery methods.

    
    .. py:data:: SlpDiscoveryMethod.slpAutoMulticast

        Use the well known multicast address to find DAs.

    
    .. py:data:: SlpDiscoveryMethod.slpAutoUnicast

        Use broadcasting to find SLP DAs. Only DAs on the current subnet will be found.

    
    .. py:data:: SlpDiscoveryMethod.slpDhcp

        Use DHCP to find the SLP DAs.

    
    .. py:data:: SlpDiscoveryMethod.slpManual

        User specified address for a DA.

    