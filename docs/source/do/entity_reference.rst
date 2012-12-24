
================================================================================
EntityReference
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.query_list.QueryList`,
    :py:meth:`~pyvisdk.do.query_topology.QueryTopology`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.edge.Edge`,
    :py:class:`~pyvisdk.do.entity_not_found.EntityNotFound`,
    :py:class:`~pyvisdk.do.node.Node`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.entity_reference_entity_type.EntityReferenceEntityType`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.entity_reference.EntityReference
    
    .. py:attribute:: id

        Unique identifier for the entity of a given type in the system. A VirtualCenter managed object ID can be supplied here, in which case the type may be unset. Otherwise, the type must be set.

    
    .. py:attribute:: type

        Type of the entity.

    