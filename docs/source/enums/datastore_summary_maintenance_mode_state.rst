
==================================================================================================
DatastoreSummaryMaintenanceModeState
==================================================================================================

.. describe:: DatastoreSummaryMaintenanceModeState

    Defines the current maintenance mode state of the datastore. NOTE: This data object type and all of its methods are experimental and subject to change in future releases.

    
    .. py:data:: DatastoreSummaryMaintenanceModeState.enteringMaintenance

        Started entering maintenance mode, but not finished. This could happen when waiting for user input or for long-running vmotions to complete.

    
    .. py:data:: DatastoreSummaryMaintenanceModeState.inMaintenance

        Successfully entered maintenance mode.

    
    .. py:data:: DatastoreSummaryMaintenanceModeState.normal

        Default state.

    