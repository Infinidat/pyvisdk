
==================================================================================================
ClusterDasConfigInfoHBDatastoreCandidate
==================================================================================================

.. describe:: ClusterDasConfigInfoHBDatastoreCandidate

    The policy to determine the candidates from which vCenter Server can choose heartbeat datastores.

    
    .. py:data:: ClusterDasConfigInfoHBDatastoreCandidate.allFeasibleDs

        vCenter Server chooses heartbeat datastores from all the feasible ones, i.e., the datastores that are accessible to more than one host in the cluster. The choice will be made without giving preference to those specified by the user (see heartbeatDatastore).

    
    .. py:data:: ClusterDasConfigInfoHBDatastoreCandidate.allFeasibleDsWithUserPreference

        vCenter Server chooses heartbeat datastores from all the feasible ones while giving preference to those specified by the user (see heartbeatDatastore). More specifically, the datastores not included in heartbeatDatastore will be chosen if and only if the specified ones are not sufficient.

    
    .. py:data:: ClusterDasConfigInfoHBDatastoreCandidate.userSelectedDs

        vCenter Server chooses heartbeat datastores from the set specified by the user (see heartbeatDatastore). More specifically, datastores not included in the set will not be chosen. Note that if heartbeatDatastore is empty, datastore heartbeating will be disabled for HA.

    