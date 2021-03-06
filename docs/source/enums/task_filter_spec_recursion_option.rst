
==================================================================================================
TaskFilterSpecRecursionOption
==================================================================================================

.. describe:: TaskFilterSpecRecursionOption

    This option specifies how to select tasks based on child relationships in the inventory hierarchy. If a managed entity has children, their tasks can be retrieved with this filter option.

    
    .. py:data:: TaskFilterSpecRecursionOption.all

        Returns tasks pertaining either to the specified managed entity or to its child entities.

    
    .. py:data:: TaskFilterSpecRecursionOption.children

        Returns tasks pertaining to child entities only. Excludes tasks pertaining to the specified managed entity itself.

    
    .. py:data:: TaskFilterSpecRecursionOption.self

        Returns tasks that pertain only to the specified managed entity, and not its children.

    