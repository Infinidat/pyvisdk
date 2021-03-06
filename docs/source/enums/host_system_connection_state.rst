
==================================================================================================
HostSystemConnectionState
==================================================================================================

.. describe:: HostSystemConnectionState

    Defines a host's connection state.

    
    .. py:data:: HostSystemConnectionState.connected

        Connected to the server. For ESX Server, this is always the setting.

    
    .. py:data:: HostSystemConnectionState.disconnected

        The user has explicitly taken the host down. VirtualCenter does not expect to receive heartbeats from the host. The next time a heartbeat is received, the host is moved to the connected state again and an event is logged.

    
    .. py:data:: HostSystemConnectionState.notResponding

        VirtualCenter is not receiving heartbeats from the server. The state automatically changes to connected once heartbeats are received again. This state is typically used to trigger an alarm on the host.

    