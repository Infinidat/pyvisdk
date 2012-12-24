
================================================================================
SmsTaskInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`,
    :py:class:`~pyvisdk.do.sms_task.SmsTask`
    
.. describe:: Since
    
    SMS API 2.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_sms_task_info.QuerySmsTaskInfo`
    
.. class:: pyvisdk.do.sms_task_info.SmsTaskInfo
    
    .. py:attribute:: completionTime

        Time stamp when the task was completed (whether success or failure).

    
    .. py:attribute:: error

        If the task state is "error", then this property contains the fault code.

    
    .. py:attribute:: key

        The unique key for the task.

    
    .. py:attribute:: object

        Managed Object to which the operation applies.

    
    .. py:attribute:: progress

        If the task state is "running", then this property contains a progress measurement, expressed as percentage completed, from 0 to 100.

    
    .. py:attribute:: result

        If the task state is "success", then this property may be used to hold a return value.

    
    .. py:attribute:: startTime

        Time stamp when the task started running.

    
    .. py:attribute:: state

        Runtime status of the task. Possible values are SmsTaskState

    
    .. py:attribute:: task

        The managed object that represents this task.

    