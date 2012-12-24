
==================================================================================================
HostProfileManagerAnswerFileStatus
==================================================================================================

.. describe:: HostProfileManagerAnswerFileStatus

    The HostProfileManagerAnswerFileStatus enum defines possible values for answer file status.

    
    .. py:data:: HostProfileManagerAnswerFileStatus.invalid

        Answer file is not valid. The file is either missing or incomplete.
          
            * To produce an answer file, pass host-specific data (user input) to the HostProfileManager.ApplyHostConfig_Task method.

    
    .. py:data:: HostProfileManagerAnswerFileStatus.unknown

        Answer file status is not known.

    
    .. py:data:: HostProfileManagerAnswerFileStatus.valid

        Answer file is valid.

    