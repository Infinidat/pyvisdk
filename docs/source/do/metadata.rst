
================================================================================
Metadata
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.query_result.QueryResult`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.metadata.Metadata
    
    .. py:attribute:: lastUpdateTime

        Time at which the returned data was last updated in the service cache.

    
    .. py:attribute:: numRows

        Number of rows in the result set.

    
    .. py:attribute:: propertyName

        List of names of the properties (column names) returned in the result set.

    
    .. py:attribute:: totalRows

        Total number of rows that matched the query. This can be different from numRows if the offset/maxCount values were specified in the QuerySpec.

    