
==================================================================================================
RecommendationReasonCode
==================================================================================================

.. describe:: RecommendationReasonCode

    List of defined migration reason codes:

    
    .. py:data:: RecommendationReasonCode.antiAffin

        Fulfill anti-affinity rule.

    
    .. py:data:: RecommendationReasonCode.balanceDatastoreIOLoad

        Balance datastore I/O workload. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.balanceDatastoreSpaceUsage

        Balance datastore space usage. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.checkResource

        Sanity-check resource pool hierarchy vSphere API 4.0

    
    .. py:data:: RecommendationReasonCode.datastoreMaint

        Datastore entering maintenance mode. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.datastoreSpaceOutage

        Fix the issue that a datastore run out of space. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.enterStandby

        Host entering standby mode.

    
    .. py:data:: RecommendationReasonCode.fairnessCpuAvg

        Balance average CPU utilization.

    
    .. py:data:: RecommendationReasonCode.fairnessMemAvg

        Balance average memory utilization.

    
    .. py:data:: RecommendationReasonCode.hostMaint

        Host entering maintenance mode.

    
    .. py:data:: RecommendationReasonCode.increaseCapacity

        Power on host to increase cluster capacity

    
    .. py:data:: RecommendationReasonCode.iolbDisabledInternal

        IO load balancing was disabled internally. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.jointAffin

        Fulfill affinity rule.

    
    .. py:data:: RecommendationReasonCode.powerOnVm

        Power on virtual machine

    
    .. py:data:: RecommendationReasonCode.powerSaving

        Power off host for power savings

    
    .. py:data:: RecommendationReasonCode.reservationCpu

        balance CPU reservations

    
    .. py:data:: RecommendationReasonCode.reservationMem

        balance memory reservations

    
    .. py:data:: RecommendationReasonCode.storagePlacement

        Satisfy storage initial placement requests. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.unreservedCapacity

        Maintain unreserved capacity vSphere API 4.0

    
    .. py:data:: RecommendationReasonCode.virtualDiskAntiAffin

        Fix virtual disk anti-affinity rule violation. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.virtualDiskJointAffin

        Fix virtual disk affinity rule violation. vSphere API 5.0

    
    .. py:data:: RecommendationReasonCode.vmHostHardAffinity

        Fix hard VM/host affinity rule violation vSphere API 4.1

    
    .. py:data:: RecommendationReasonCode.vmHostSoftAffinity

        Fix soft VM/host affinity rule violation vSphere API 4.1

    