
==================================================================================================
ClusterDasAamNodeStateDasState
==================================================================================================

.. describe:: ClusterDasAamNodeStateDasState

    The ClusterDasAamNodeStateDasState enumerated type defines values for host HA configuration and runtime state properties (configState and runtimeState).

    
    .. py:data:: ClusterDasAamNodeStateDasState.agentShutdown

        The HA agent has been shut down.

    
    .. py:data:: ClusterDasAamNodeStateDasState.configuring

        HA configuration is in progress.

    
    .. py:data:: ClusterDasAamNodeStateDasState.error

        There is an error condition. This can represent a configuration error or a host agent runtime error.

    
    .. py:data:: ClusterDasAamNodeStateDasState.initialized

        HA agents have been installed but are not running on the the host.

    
    .. py:data:: ClusterDasAamNodeStateDasState.nodeFailed

        The host is not reachable. This can represent a host failure or an isolated host.

    
    .. py:data:: ClusterDasAamNodeStateDasState.running

        HA agent is running on this host.

    
    .. py:data:: ClusterDasAamNodeStateDasState.unconfiguring

        HA configuration is being removed.

    
    .. py:data:: ClusterDasAamNodeStateDasState.uninitialized

        HA has never been enabled on the the host.

    