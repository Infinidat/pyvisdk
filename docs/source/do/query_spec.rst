
================================================================================
QuerySpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.query_list.QueryList`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.filter_spec.FilterSpec`,
    :py:class:`~pyvisdk.do.sort_spec.SortSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.query_spec.QuerySpec
    
    .. py:attribute:: filterSpec

        Specification of filter constraints on the results.

    
    .. py:attribute:: maxCount

        Maximum number of rows to return.

    
    .. py:attribute:: offset

        Offset from which rows should be included in the result set.

    
    .. py:attribute:: sortSpec

        List of criteria on which to sort the results. Currently, only a single sort spec is supported.

    