
==================================================================================================
VirtualAppVAppState
==================================================================================================

.. describe:: VirtualAppVAppState

    The VAppState type defines the set of states a vApp can be in. The transitory states between started and stopped is modeled explicitly, since the starting or stopping of a vApp is typically a time-consuming process that might take minutes to complete.

    
    .. py:data:: VirtualAppVAppState.started

        The vApp is currently powered on .

    
    .. py:data:: VirtualAppVAppState.starting

        The vApp is in the process of starting.

    
    .. py:data:: VirtualAppVAppState.stopped

        The vApp is currently powered off or suspended.

    
    .. py:data:: VirtualAppVAppState.stopping

        The vApp is in the process of stopping.

    