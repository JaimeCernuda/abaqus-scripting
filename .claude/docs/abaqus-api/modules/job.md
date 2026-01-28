# Abaqus JOB Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/job.html](https://hailin.wang/abqpy/en/2025/reference/mdb/job.html)
> Downloaded for offline use by Claude Code skills.

---

# Job[¶](#job "Permalink to this heading")

The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.

## Create jobs[¶](#create-jobs "Permalink to this heading")

JobMdb.Job(*[name](#abaqus.Job.JobMdb.JobMdb.Job.name "abaqus.Job.JobMdb.JobMdb.Job.name (Python parameter) — A String specifying the name of the new job.")*, *[model](#abaqus.Job.JobMdb.JobMdb.Job.model "abaqus.Job.JobMdb.JobMdb.Job.model (Python parameter) — A String specifying the name of the model to be analyzed or a Model object specifying the model to be analyzed.")*, *[description](#abaqus.Job.JobMdb.JobMdb.Job.description "abaqus.Job.JobMdb.JobMdb.Job.description (Python parameter) — A String specifying a description of the job.")=`''`*, *[type](#abaqus.Job.JobMdb.JobMdb.Job.type "abaqus.Job.JobMdb.JobMdb.Job.type (Python parameter) — A SymbolicConstant specifying the type of job.")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.JobMdb.JobMdb.Job.queue "abaqus.Job.JobMdb.JobMdb.Job.queue (Python parameter) — A String specifying the name of the queue to which to submit the job.")=`''`*, *[waitHours](#abaqus.Job.JobMdb.JobMdb.Job.waitHours "abaqus.Job.JobMdb.JobMdb.Job.waitHours (Python parameter) — An Int specifying the number of hours to wait before submitting the job.")=`0`*, *[waitMinutes](#abaqus.Job.JobMdb.JobMdb.Job.waitMinutes "abaqus.Job.JobMdb.JobMdb.Job.waitMinutes (Python parameter) — An Int specifying the number of minutes to wait before submitting the job.")=`0`*, *[atTime](#abaqus.Job.JobMdb.JobMdb.Job.atTime "abaqus.Job.JobMdb.JobMdb.Job.atTime (Python parameter) — A String specifying the time at which to submit the job.")=`''`*, *[echoPrint](#abaqus.Job.JobMdb.JobMdb.Job.echoPrint "abaqus.Job.JobMdb.JobMdb.Job.echoPrint (Python parameter) — A Boolean specifying whether an echo of the input data is printed.")=`0`*, *[contactPrint](#abaqus.Job.JobMdb.JobMdb.Job.contactPrint "abaqus.Job.JobMdb.JobMdb.Job.contactPrint (Python parameter) — A Boolean specifying whether contact constraint data are printed.")=`0`*, *[modelPrint](#abaqus.Job.JobMdb.JobMdb.Job.modelPrint "abaqus.Job.JobMdb.JobMdb.Job.modelPrint (Python parameter) — A Boolean specifying whether model definition data are printed.")=`0`*, *[historyPrint](#abaqus.Job.JobMdb.JobMdb.Job.historyPrint "abaqus.Job.JobMdb.JobMdb.Job.historyPrint (Python parameter) — A Boolean specifying whether history data are printed.")=`0`*, *[scratch](#abaqus.Job.JobMdb.JobMdb.Job.scratch "abaqus.Job.JobMdb.JobMdb.Job.scratch (Python parameter) — A String specifying the location of the scratch directory.")=`''`*, *[userSubroutine](#abaqus.Job.JobMdb.JobMdb.Job.userSubroutine "abaqus.Job.JobMdb.JobMdb.Job.userSubroutine (Python parameter) — A String specifying the file containing the user's subroutine definitions.")=`''`*, *[numCpus](#abaqus.Job.JobMdb.JobMdb.Job.numCpus "abaqus.Job.JobMdb.JobMdb.Job.numCpus (Python parameter) — An Int specifying the number of CPUs to use for this analysis if parallel processing is available.")=`1`*, *[memory](#abaqus.Job.JobMdb.JobMdb.Job.memory "abaqus.Job.JobMdb.JobMdb.Job.memory (Python parameter) — An Int specifying the amount of memory available to Abaqus analysis.")=`90`*, *[memoryUnits](#abaqus.Job.JobMdb.JobMdb.Job.memoryUnits "abaqus.Job.JobMdb.JobMdb.Job.memoryUnits (Python parameter) — A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis.")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.JobMdb.JobMdb.Job.explicitPrecision "abaqus.Job.JobMdb.JobMdb.Job.explicitPrecision (Python parameter) — A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit.")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.JobMdb.JobMdb.Job.nodalOutputPrecision "abaqus.Job.JobMdb.JobMdb.Job.nodalOutputPrecision (Python parameter) — A SymbolicConstant specifying the precision of the nodal output written to the output database.")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.JobMdb.JobMdb.Job.numDomains "abaqus.Job.JobMdb.JobMdb.Job.numDomains (Python parameter) — An Int specifying the number of domains for parallel execution in Abaqus/Explicit.")=`1`*, *[activateLoadBalancing](#abaqus.Job.JobMdb.JobMdb.Job.activateLoadBalancing "abaqus.Job.JobMdb.JobMdb.Job.activateLoadBalancing (Python parameter) — A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit.")=`0`*, *[multiprocessingMode](#abaqus.Job.JobMdb.JobMdb.Job.multiprocessingMode "abaqus.Job.JobMdb.JobMdb.Job.multiprocessingMode (Python parameter) — A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message passing interface (MPI).")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.JobMdb.JobMdb.Job.licenseType "abaqus.Job.JobMdb.JobMdb.Job.licenseType (Python parameter) — A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model.")=`abaqusConstants.DEFAULT`*, *\*[args](#abaqus.Job.JobMdb.JobMdb.Job "abaqus.Job.JobMdb.JobMdb.Job.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Job.JobMdb.JobMdb.Job "abaqus.Job.JobMdb.JobMdb.Job.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L36-L204)
:   This method creates an analysis job using a model on a model database (MDB) for the model definition.

    Note

    This function can be accessed by:

    ```python
    mdb.Job
    ```

    Changed in version 2023: The `parallelizationMethodExplicit` argument was removed.

    Note

    Check [Job on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?contextscope=all).

    Parameters:[¶](#parameters "Permalink to this headline")
    :   name
        :   A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
            name.

        model
        :   A String specifying the name of the model to be analyzed or a Model object specifying
            the model to be analyzed.

        description=`''`
        :   A String specifying a description of the job.

        type=`abaqusConstants.ANALYSIS`
        :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
            SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the
            type JobFromInputFile, **type** = RESTART is not available.

        queue=`''`
        :   A String specifying the name of the queue to which to submit the job. The default value
            is an empty string. Note: You can use the **queue** argument when creating a Job object on a
            Windows workstation; however, remote queues are available only on Linux platforms.

        waitHours=`0`
        :   An Int specifying the number of hours to wait before submitting the job. This argument
            is ignored if **queue** is set. The default value is 0.This argument works in conjunction
            with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

        waitMinutes=`0`
        :   An Int specifying the number of minutes to wait before submitting the job. This argument
            is ignored if **queue** is set. The default value is 0.This argument works in conjunction
            with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

        atTime=`''`
        :   A String specifying the time at which to submit the job. If **queue** is empty, the string
            syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
            valid according to the system administrator. The default value is an empty
            string. Note: You can use the **atTime** argument when creating a Job object on a Windows
            workstation; however, the `at` command is available only on Linux platforms.

        echoPrint=`0`
        :   A Boolean specifying whether an echo of the input data is printed. The default value is
            OFF.

        contactPrint=`0`
        :   A Boolean specifying whether contact constraint data are printed. The default value is
            OFF.

        modelPrint=`0`
        :   A Boolean specifying whether model definition data are printed. The default value is
            OFF.

        historyPrint=`0`
        :   A Boolean specifying whether history data are printed. The default value is OFF.

        scratch=`''`
        :   A String specifying the location of the scratch directory. The default value is an empty
            string.

        userSubroutine=`''`
        :   A String specifying the file containing the user’s subroutine definitions. The default
            value is an empty string.

        numCpus=`1`
        :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
            available. Possible values are **numCpus** > 0. The default value is 1.

        memory=`90`
        :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
            expressed in the units supplied in **memoryUnits**. The default value is 90.

        memoryUnits=`abaqusConstants.PERCENTAGE`
        :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
            analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
            is PERCENTAGE.

        explicitPrecision=`abaqusConstants.SINGLE`
        :   A SymbolicConstant specifying whether to use the double precision version of
            Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
            DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

        nodalOutputPrecision=`abaqusConstants.SINGLE`
        :   A SymbolicConstant specifying the precision of the nodal output written to the output
            database. Possible values are SINGLE and FULL. The default value is SINGLE.

        numDomains=`1`
        :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
            using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

            Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
            argument was removed in 2023.

        activateLoadBalancing=`0`
        :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
            multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

        multiprocessingMode=`abaqusConstants.DEFAULT`
        :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
            multiple processes that communicate through a message passing interface (MPI). Possible
            values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

        licenseType=`abaqusConstants.DEFAULT`
        :   A SymbolicConstant specifying the type of license type being used in the case of the
            DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
            value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
            available.

            Changed in version 2022: The `licenseType` argument was added.

    Returns:[¶](#returns "Permalink to this headline")
    :   A ModelJob object.

    Return type:[¶](#return-type "Permalink to this headline")
    :   `ModelJob`

    Raises:[¶](#raises "Permalink to this headline")
    :   [**AbaqusException**](../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

## Create queues in Session[¶](#create-queues-in-session "Permalink to this heading")

JobSession.Queue(*[name](#abaqus.Job.JobSession.JobSession.Queue.name "abaqus.Job.JobSession.JobSession.Queue.name (Python parameter) — A String specifying the name of the new Queue object.")*, *[queueName](#abaqus.Job.JobSession.JobSession.Queue.queueName "abaqus.Job.JobSession.JobSession.Queue.queueName (Python parameter) — A String specifying the name of the remote analysis queue.")*, *[hostName](#abaqus.Job.JobSession.JobSession.Queue.hostName "abaqus.Job.JobSession.JobSession.Queue.hostName (Python parameter) — A String specifying the name of the remote host.")=`''`*, *[fileCopy](#abaqus.Job.JobSession.JobSession.Queue.fileCopy "abaqus.Job.JobSession.JobSession.Queue.fileCopy (Python parameter) — A Boolean specifying if the results files are to be copied from the remote machine to the local machine.")=`1`*, *[directory](#abaqus.Job.JobSession.JobSession.Queue.directory "abaqus.Job.JobSession.JobSession.Queue.directory (Python parameter) — A String specifying the remote location for the execution of the simulation.")=`''`*, *[driver](#abaqus.Job.JobSession.JobSession.Queue.driver "abaqus.Job.JobSession.JobSession.Queue.driver (Python parameter) — A String specifying the designation of the remote driver.")=`''`*, *[remotePlatform](#abaqus.Job.JobSession.JobSession.Queue.remotePlatform "abaqus.Job.JobSession.JobSession.Queue.remotePlatform (Python parameter) — A SymbolicConstant specifying the type of operating system on the remote machine.")=`abaqusConstants.LINUX`*, *[filesToCopy](#abaqus.Job.JobSession.JobSession.Queue.filesToCopy "abaqus.Job.JobSession.JobSession.Queue.filesToCopy (Python parameter) — A list of Strings specifying the files to be copied from the remote location to the local machine, or ALL.")=`abaqusConstants.ALL`*, *[deleteAfterCopy](#abaqus.Job.JobSession.JobSession.Queue.deleteAfterCopy "abaqus.Job.JobSession.JobSession.Queue.deleteAfterCopy (Python parameter) — A Boolean specifying whether remote files are to be deleted after they are copied to the local machine.")=`0`*, *[description](#abaqus.Job.JobSession.JobSession.Queue.description "abaqus.Job.JobSession.JobSession.Queue.description (Python parameter) — A String specifying a description of the queue.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobSession.py#L15-L89)
:   This method creates a Queue object. Note:Remote queues are available only on Linux platforms.

    Note

    This function can be accessed by:

    ```python
    session.Queue
    ```

    Note

    Check [Queue on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-queuepyc.htm?contextscope=all).

    Parameters:[¶](#parameters "Permalink to this headline")
    :   name
        :   A String specifying the name of the new Queue object.

        queueName
        :   A String specifying the name of the remote analysis queue.

        hostName=`''`
        :   A String specifying the name of the remote host. The default value is an empty string.

        fileCopy=`1`
        :   A Boolean specifying if the results files are to be copied from the remote machine to
            the local machine. The default value is ON.

        directory=`''`
        :   A String specifying the remote location for the execution of the simulation. The default
            value is an empty string.

        driver=`''`
        :   A String specifying the designation of the remote driver. The default value is “abaqus”.

        remotePlatform=`abaqusConstants.LINUX`
        :   A SymbolicConstant specifying the type of operating system on the remote machine. The
            default value is Linux.

        filesToCopy=`abaqusConstants.ALL`
        :   A list of Strings specifying the files to be copied from the remote location to the
            local machine, or ALL. Strings specified in a list are the extensions of the job files
            that will be copied, such as (‘log’, ‘dat’, ‘msg’, ‘sta’, ‘odb’). The default value is
            ALL.

        deleteAfterCopy=`0`
        :   A Boolean specifying whether remote files are to be deleted after they are copied to the
            local machine. The default value is OFF.

        description=`''`
        :   A String specifying a description of the queue. The default value is an empty string.

    Returns:[¶](#returns "Permalink to this headline")
    :   A Queue object.

    Return type:[¶](#return-type "Permalink to this headline")
    :   [`Queue`](#abaqus.Job.JobSession.JobSession.Queue "abaqus.Job.JobSession.JobSession.Queue (Python method) — This method creates a Queue object. Note:Remote queues are available only on Linux platforms.")

    Raises:[¶](#raises "Permalink to this headline")
    :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – Remote queue host name is not set, If **fileCopy** = ON and **hostName** is empty.
        Directory in which to run the job on the remote computer is not set, If **fileCopy** = ON and **directory** is empty.

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* Coexecution[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L16-L161)[¶](#abaqus.Job.Coexecution.Coexecution "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Coexecution object contains a set of jobs as associated parameters to define a co-simulation
    analysis.

    Note

    This object can be accessed by:

    ```python
    import job
    mdb.coexecutions[name]
    ```

    The corresponding analysis keywords are:

    * HEADING
    * PREPRINT

    Note

    Check [Coexecution on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coexecutionpyc.htm?contextscope=all).

    Member Details:

    atTime : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L71-L77)[¶](#abaqus.Job.Coexecution.Coexecution.atTime "Permalink to this definition")
    :   A String specifying the time at which to submit the co-execution. If **queue** is empty,
        the string syntax must be valid for the Linux `at` command. If **queue** is set, the
        syntax must be valid according to the system administrator. The default value is an
        empty string. Note: You can use the **atTime** argument when creating a Coexecution object
        on a Windows workstation; however, the `at` command is available only on Linux
        platforms.

    jobs : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Job.Job.Job`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L79-L80)[¶](#abaqus.Job.Coexecution.Coexecution.jobs "Permalink to this definition")
    :   A repository of Job objects specifying the jobs that comprise this co-execution.

    kill()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L110-L113)[¶](#abaqus.Job.Coexecution.Coexecution.kill "Permalink to this definition")
    :   This method kills the analysis of a co-execution.

    licenseType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L106-L108)[¶](#abaqus.Job.Coexecution.Coexecution.licenseType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of license type being used in case of DSLS
        SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value
        is DEFAULT.If the license model is not DSLS SimUnit then the licenseType is not
        available.

        New in version 2022: The `licenseType` attribute was added.

    mainAnalysisProduct : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ABAQUS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L45-L47)[¶](#abaqus.Job.Coexecution.Coexecution.mainAnalysisProduct "Permalink to this definition")
    :   A SymbolicConstant specifying the analysis product type of the main model for the
        co-execution. The default value is ABAQUS.

        Changed in version 2022: The `masterAnalysisProduct` attribute was changed to `mainAnalysisProduct`.

    mainModel : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L45-L47)[¶](#abaqus.Job.Coexecution.Coexecution.mainModel "Permalink to this definition")
    :   A String specifying the name of the main model for the co-execution.

        Changed in version 2022: The `masterModel` attribute was changed to `mainModel`.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L33-L35)[¶](#abaqus.Job.Coexecution.Coexecution.name "Permalink to this definition")
    :   A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
        name.

    queue : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L65-L69)[¶](#abaqus.Job.Coexecution.Coexecution.queue "Permalink to this definition")
    :   A String specifying the name of the queue to which to submit the co-execution. The
        default value is an empty string. Note: You can use the **queue** argument when creating a
        Coexecution object on a Windows workstation; however, remote queues are available only
        on Linux platforms.

    secondaryAnalysisProducts : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py)[¶](#abaqus.Job.Coexecution.Coexecution.secondaryAnalysisProducts "Permalink to this definition")
    :   A tuple of SymbolicConstants specifying the analysis product types of the secondary
        models for the co-execution. The default value is an empty sequence.

        Changed in version 2022: The `slaveAnalysisProducts` attribute was changed to `secondaryAnalysisProducts`.

    secondaryModels : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L45-L47)[¶](#abaqus.Job.Coexecution.Coexecution.secondaryModels "Permalink to this definition")
    :   A tuple of Strings specifying the names of the secondary models for the co-execution.

        Changed in version 2022: The `slaveModels` attribute was changed to `secondaryModels`.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py)[¶](#abaqus.Job.Coexecution.Coexecution.status "Permalink to this definition")
    :   A SymbolicConstant specifying the status of the co-execution. Possible values are
        SUBMITTED, RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK\_SUBMITTED, CHECK\_RUNNING, and
        CHECK\_COMPLETED.If the **message** member of all the jobs are empty, **status** is set to
        NONE.

    submit(*[consistencyChecking](#abaqus.Job.Coexecution.Coexecution.submit.consistencyChecking "abaqus.Job.Coexecution.Coexecution.submit.consistencyChecking (Python parameter) — A Boolean specifying whether to perform consistency checking for the individual jobs. The default value is ON.")=`1`*, *[datacheckJob](#abaqus.Job.Coexecution.Coexecution.submit.datacheckJob "abaqus.Job.Coexecution.Coexecution.submit.datacheckJob (Python parameter) — A Boolean specifying whether to run the co-execution as a datacheck analysis.")=`False`*, *[continueJob](#abaqus.Job.Coexecution.Coexecution.submit.continueJob "abaqus.Job.Coexecution.Coexecution.submit.continueJob (Python parameter) — A Boolean specifying whether to run the co-execution as a continuation analysis.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L115-L139)[¶](#abaqus.Job.Coexecution.Coexecution.submit "Permalink to this definition")
    :   This method submits a co-execution for analysis.

        Note

        Check [Coexecution.submit on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coexecutionpyc.htm?contextscope=all#simaker-coexecutionsubmitpyc).

        Parameters:[¶](#abaqus.Job.Coexecution.Coexecution.submit-parameters "Permalink to this headline")
        :   consistencyChecking=`1`[¶](#abaqus.Job.Coexecution.Coexecution.submit.consistencyChecking "Permalink to this definition")
            :   A Boolean specifying whether to perform consistency checking for the individual jobs.
                The default value is ON. It is not recommended to turn the consistency checking off
                unless you are absolutely sure the models are all consistent.

            datacheckJob=`False`[¶](#abaqus.Job.Coexecution.Coexecution.submit.datacheckJob "Permalink to this definition")
            :   A Boolean specifying whether to run the co-execution as a datacheck analysis. The
                default value is False. The **datacheckJob** and **continueJob** arguments cannot both be
                True.

            continueJob=`False`[¶](#abaqus.Job.Coexecution.Coexecution.submit.continueJob "Permalink to this definition")
            :   A Boolean specifying whether to run the co-execution as a continuation analysis. The
                default value is False. The **datacheckJob** and **continueJob** arguments cannot both be
                True.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ANALYSIS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L37-L40)[¶](#abaqus.Job.Coexecution.Coexecution.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of analysis to execute for the co-execution.
        Possible values are ANALYSIS, SYNTAXCHECK, RECOVER, and RESTART. The default value is
        ANALYSIS.

    waitForCompletion()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L154-L161)[¶](#abaqus.Job.Coexecution.Coexecution.waitForCompletion "Permalink to this definition")
    :   This method interrupts the execution of the script until the end of all the analyses.

        If you call the waitForCompletion method and the **status** member is neither SUBMITTED nor RUNNING,
        Abaqus assumes the analysis has either completed or aborted and returns immediately.

    waitHours : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L49-L52)[¶](#abaqus.Job.Coexecution.Coexecution.waitHours "Permalink to this definition")
    :   An Int specifying the number of hours to wait before submitting the co-execution. This
        argument is ignored if **queue** is set. The default value is 0.This argument works in
        conjunction with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

    waitMinutes : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L54-L57)[¶](#abaqus.Job.Coexecution.Coexecution.waitMinutes "Permalink to this definition")
    :   An Int specifying the number of minutes to wait before submitting the job. This argument
        is ignored if **queue** is set. The default value is 0.This argument works in conjunction
        with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

    writeInput(*[consistencyChecking](#abaqus.Job.Coexecution.Coexecution.writeInput.consistencyChecking "abaqus.Job.Coexecution.Coexecution.writeInput.consistencyChecking (Python parameter) — A Boolean specifying whether to perform consistency checking for the individual jobs. The default value is ON.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Coexecution.py#L141-L152)[¶](#abaqus.Job.Coexecution.Coexecution.writeInput "Permalink to this definition")
    :   This method writes an input file for each analysis in the co-execution.

        Note

        Check [Coexecution.writeInput on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coexecutionpyc.htm?contextscope=all#simaker-coexecutionwriteinputpyc).

        Parameters:[¶](#abaqus.Job.Coexecution.Coexecution.writeInput-parameters "Permalink to this headline")
        :   consistencyChecking=`1`[¶](#abaqus.Job.Coexecution.Coexecution.writeInput.consistencyChecking "Permalink to this definition")
            :   A Boolean specifying whether to perform consistency checking for the individual jobs.
                The default value is ON. It is not recommended to turn the consistency checking off
                unless you are absolutely sure the models are all consistent.

*class* JobFromInputFile(*[name](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.name (Python parameter)")*, *[inputFileName](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.inputFileName (Python parameter)")*, *[type](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.type (Python parameter)")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.queue (Python parameter)")=`''`*, *[waitHours](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.waitHours (Python parameter)")=`0`*, *[waitMinutes](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.waitMinutes (Python parameter)")=`0`*, *[atTime](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.atTime (Python parameter)")=`''`*, *[scratch](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.scratch (Python parameter)")=`''`*, *[userSubroutine](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.userSubroutine (Python parameter)")=`''`*, *[numCpus](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.numCpus (Python parameter)")=`1`*, *[memory](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.memory (Python parameter)")=`90`*, *[memoryUnits](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.memoryUnits (Python parameter)")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.explicitPrecision (Python parameter)")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.nodalOutputPrecision (Python parameter)")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.numDomains (Python parameter)")=`1`*, *[activateLoadBalancing](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.activateLoadBalancing (Python parameter)")=`0`*, *[multiprocessingMode](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.multiprocessingMode (Python parameter)")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.licenseType (Python parameter)")=`abaqusConstants.DEFAULT`*, *[getMemoryFromAnalysis](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.getMemoryFromAnalysis (Python parameter)")=`1`*, *[numGPUs](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.numGPUs (Python parameter)")=`0`*, *[resultsFormat](#abaqus.Job.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobFromInputFile.__init__.resultsFormat (Python parameter)")=`abaqusConstants.ODB`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L22-L389)[¶](#abaqus.Job.JobMdb.JobFromInputFile "Permalink to this definition")
:   Bases: `Job`

    The JobFromInputFile object defines a Job object which analyzes a model contained in an input file. The
    JobFromInputFile object is derived from the Job object.

    Note

    This object can be accessed by:

    ```python
    import job
    mdb.jobs[name]
    ```

    Changed in version 2023: The `parallelizationMethodExplicit` attribute was removed.

    Note

    Check [JobFromInputFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobfrominputfilepyc.htm?contextscope=all).

    Member Details:

    activateLoadBalancing : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L136-L138)[¶](#abaqus.Job.JobMdb.JobFromInputFile.activateLoadBalancing "Permalink to this definition")
    :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
        multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

    analysis : --is-rst--:py:data:`~typing.Literal`\[``STANDARD``, ``EXPLICIT``, ``UNKNOWN``][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py)[¶](#abaqus.Job.JobMdb.JobFromInputFile.analysis "Permalink to this definition")
    :   A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or
        Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has
        the type JobFromInputFile, **analysis** = UNKNOWN.

    atTime : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L88-L93)[¶](#abaqus.Job.JobMdb.JobFromInputFile.atTime "Permalink to this definition")
    :   A String specifying the time at which to submit the job. If **queue** is empty, the string
        syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
        valid according to the system administrator. The default value is an empty string. Note:
        You can use the **atTime** argument when creating a Job object on a Windows workstation;
        however, the `at` command is available only on Linux platforms.

    environment : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L56-L57)[¶](#abaqus.Job.JobMdb.JobFromInputFile.environment "Permalink to this definition")
    :   A tuple of Strings specifying the environment variables and their values.

    explicitPrecision : --is-rst--:py:data:`~typing.Literal`\[``SINGLE``, ``FORCE\_SINGLE``, ``DOUBLE``, ``DOUBLE\_CONSTRAINT\_ONLY``, ``DOUBLE\_PLUS\_PACK``] = `'SINGLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L116-L119)[¶](#abaqus.Job.JobMdb.JobFromInputFile.explicitPrecision "Permalink to this definition")
    :   A SymbolicConstant specifying whether to use the double precision version of
        Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
        DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

    getMemoryFromAnalysis : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L38-L41)[¶](#abaqus.Job.JobMdb.JobFromInputFile.getMemoryFromAnalysis "Permalink to this definition")
    :   A Boolean specifying whether to retrieve the recommended memory settings from the last
        datacheck or analysis run and use those values in subsequent submissions. The default
        value is ON.

    inputFileName : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py)[¶](#abaqus.Job.JobMdb.JobFromInputFile.inputFileName "Permalink to this definition")
    :   A String specifying the input file to read. Possible values are any valid file name. If
        the .inp extension is not included in the value of the argument, the system will append
        it for the user.

    licenseType : --is-rst--:py:data:`~typing.Literal`\[``DEFAULT``, ``TOKEN``, ``CREDIT``] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L150-L152)[¶](#abaqus.Job.JobMdb.JobFromInputFile.licenseType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of license type being used in the case of the
        DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
        value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
        available.

        New in version 2022: The `licenseType` attribute was added.

    memory : --is-rst--:py:class:`int` = `90`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L107-L109)[¶](#abaqus.Job.JobMdb.JobFromInputFile.memory "Permalink to this definition")
    :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
        expressed in the units supplied in **memoryUnits**. The default value is 90.

    memoryUnits : --is-rst--:py:data:`~typing.Literal`\[``PERCENTAGE``, ``MEGA\_BYTES``, ``GIGA\_BYTES``] = `'PERCENTAGE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L111-L114)[¶](#abaqus.Job.JobMdb.JobFromInputFile.memoryUnits "Permalink to this definition")
    :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
        analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
        is PERCENTAGE.

    messages : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Job.Message.Message`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L53-L54)[¶](#abaqus.Job.JobMdb.JobFromInputFile.messages "Permalink to this definition")
    :   A MessageArray object specifying the messages received during an analysis.

    multiprocessingMode : --is-rst--:py:data:`~typing.Literal`\[``DEFAULT``, ``THREADS``, ``MPI``] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L140-L143)[¶](#abaqus.Job.JobMdb.JobFromInputFile.multiprocessingMode "Permalink to this definition")
    :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
        multiple processes that communicate through a message passing interface (MPI). Possible
        values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

    nodalOutputPrecision : --is-rst--:py:data:`~typing.Literal`\[``SINGLE``, ``FULL``] = `'SINGLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L123-L125)[¶](#abaqus.Job.JobMdb.JobFromInputFile.nodalOutputPrecision "Permalink to this definition")
    :   A SymbolicConstant specifying the precision of the nodal output written to the output
        database. Possible values are SINGLE and FULL. The default value is SINGLE.

    numCpus : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L103-L105)[¶](#abaqus.Job.JobMdb.JobFromInputFile.numCpus "Permalink to this definition")
    :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
        available. Possible values are **numCpus** > 0. The default value is 1.

    numDomains : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L132-L134)[¶](#abaqus.Job.JobMdb.JobFromInputFile.numDomains "Permalink to this definition")
    :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
        using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

        Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
        argument was removed in 2023.

    queue : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L73-L76)[¶](#abaqus.Job.JobMdb.JobFromInputFile.queue "Permalink to this definition")
    :   A String specifying the name of the queue to which to submit the job. The default value
        is an empty string. Note: You can use the **queue** argument when creating a Job object on
        a Windows workstation; however, remote queues are available only on Linux platforms.

    scratch : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L95-L97)[¶](#abaqus.Job.JobMdb.JobFromInputFile.scratch "Permalink to this definition")
    :   A String specifying the location of the scratch directory. The default value is an empty
        string.

    setValues(*[type](#abaqus.Job.JobMdb.JobFromInputFile.setValues.type "abaqus.Job.JobMdb.JobFromInputFile.setValues.type (Python parameter) — A SymbolicConstant specifying the type of job.")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.JobMdb.JobFromInputFile.setValues.queue "abaqus.Job.JobMdb.JobFromInputFile.setValues.queue (Python parameter) — A String specifying the name of the queue to which to submit the job.")=`''`*, *[waitHours](#abaqus.Job.JobMdb.JobFromInputFile.setValues.waitHours "abaqus.Job.JobMdb.JobFromInputFile.setValues.waitHours (Python parameter) — An Int specifying the number of hours to wait before submitting the job.")=`0`*, *[waitMinutes](#abaqus.Job.JobMdb.JobFromInputFile.setValues.waitMinutes "abaqus.Job.JobMdb.JobFromInputFile.setValues.waitMinutes (Python parameter) — An Int specifying the number of minutes to wait before submitting the job.")=`0`*, *[atTime](#abaqus.Job.JobMdb.JobFromInputFile.setValues.atTime "abaqus.Job.JobMdb.JobFromInputFile.setValues.atTime (Python parameter) — A String specifying the time at which to submit the job.")=`''`*, *[scratch](#abaqus.Job.JobMdb.JobFromInputFile.setValues.scratch "abaqus.Job.JobMdb.JobFromInputFile.setValues.scratch (Python parameter) — A String specifying the location of the scratch directory.")=`''`*, *[userSubroutine](#abaqus.Job.JobMdb.JobFromInputFile.setValues.userSubroutine "abaqus.Job.JobMdb.JobFromInputFile.setValues.userSubroutine (Python parameter) — A String specifying the file containing the user's subroutine definitions.")=`''`*, *[numCpus](#abaqus.Job.JobMdb.JobFromInputFile.setValues.numCpus "abaqus.Job.JobMdb.JobFromInputFile.setValues.numCpus (Python parameter) — An Int specifying the number of CPUs to use for this analysis if parallel processing is available.")=`1`*, *[memory](#abaqus.Job.JobMdb.JobFromInputFile.setValues.memory "abaqus.Job.JobMdb.JobFromInputFile.setValues.memory (Python parameter) — An Int specifying the amount of memory available to Abaqus analysis.")=`90`*, *[memoryUnits](#abaqus.Job.JobMdb.JobFromInputFile.setValues.memoryUnits "abaqus.Job.JobMdb.JobFromInputFile.setValues.memoryUnits (Python parameter) — A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis.")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.JobMdb.JobFromInputFile.setValues.explicitPrecision "abaqus.Job.JobMdb.JobFromInputFile.setValues.explicitPrecision (Python parameter) — A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit.")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.JobMdb.JobFromInputFile.setValues.nodalOutputPrecision "abaqus.Job.JobMdb.JobFromInputFile.setValues.nodalOutputPrecision (Python parameter) — A SymbolicConstant specifying the precision of the nodal output written to the output database.")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.JobMdb.JobFromInputFile.setValues.numDomains "abaqus.Job.JobMdb.JobFromInputFile.setValues.numDomains (Python parameter) — An Int specifying the number of domains for parallel execution in Abaqus/Explicit.")=`1`*, *[activateLoadBalancing](#abaqus.Job.JobMdb.JobFromInputFile.setValues.activateLoadBalancing "abaqus.Job.JobMdb.JobFromInputFile.setValues.activateLoadBalancing (Python parameter) — A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit.")=`0`*, *[multiprocessingMode](#abaqus.Job.JobMdb.JobFromInputFile.setValues.multiprocessingMode "abaqus.Job.JobMdb.JobFromInputFile.setValues.multiprocessingMode (Python parameter) — A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message passing interface (MPI).")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.JobMdb.JobFromInputFile.setValues.licenseType "abaqus.Job.JobMdb.JobFromInputFile.setValues.licenseType (Python parameter) — A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model.")=`abaqusConstants.DEFAULT`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L293-L389)[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues "Permalink to this definition")
    :   This method modifies the JobFromInputFile object.

        Changed in version 2023: The `parallelizationMethodExplicit` argument was removed.

        Note

        Check [JobFromInputFile.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobfrominputfilepyc.htm?contextscope=all#simaker-jobfrominputfilesetvaluespyc).

        Parameters:[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues-parameters "Permalink to this headline")
        :   type=`abaqusConstants.ANALYSIS`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
                SYNTAXCHECK, and RECOVER. The default value is ANALYSIS.For theJobFromInputFile object,
                **type** = RESTART is not currently supported.

            queue=`''`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.queue "Permalink to this definition")
            :   A String specifying the name of the queue to which to submit the job. The default value
                is an empty string. Note: You can use the **queue** argument when creating a Job object on
                a Windows workstation; however, remote queues are available only on Linux platforms.

            waitHours=`0`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.waitHours "Permalink to this definition")
            :   An Int specifying the number of hours to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

            waitMinutes=`0`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.waitMinutes "Permalink to this definition")
            :   An Int specifying the number of minutes to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

            atTime=`''`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.atTime "Permalink to this definition")
            :   A String specifying the time at which to submit the job. If **queue** is empty, the string
                syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
                valid according to the system administrator. The default value is an empty string. Note:
                You can use the **atTime** argument when creating a Job object on a Windows workstation;
                however, the `at` command is available only on Linux platforms.

            scratch=`''`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.scratch "Permalink to this definition")
            :   A String specifying the location of the scratch directory. The default value is an empty
                string.

            userSubroutine=`''`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.userSubroutine "Permalink to this definition")
            :   A String specifying the file containing the user’s subroutine definitions. The default
                value is an empty string.

            numCpus=`1`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.numCpus "Permalink to this definition")
            :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
                available. Possible values are **numCpus** > 0. The default value is 1.

            memory=`90`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.memory "Permalink to this definition")
            :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
                expressed in the units supplied in **memoryUnits**. The default value is 90.

            memoryUnits=`abaqusConstants.PERCENTAGE`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.memoryUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
                analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
                is PERCENTAGE.

            explicitPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.explicitPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the double precision version of
                Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
                DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

            nodalOutputPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.nodalOutputPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying the precision of the nodal output written to the output
                database. Possible values are SINGLE and FULL. The default value is SINGLE.

            numDomains=`1`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.numDomains "Permalink to this definition")
            :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
                using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

                Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
                argument was removed in 2023.

            activateLoadBalancing=`0`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.activateLoadBalancing "Permalink to this definition")
            :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
                multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

            multiprocessingMode=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.multiprocessingMode "Permalink to this definition")
            :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
                multiple processes that communicate through a message passing interface (MPI). Possible
                values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

            licenseType=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobFromInputFile.setValues.licenseType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of license type being used in the case of the
                DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
                value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
                available.

    status : --is-rst--:py:data:`~typing.Literal`\[``SUBMITTED``, ``RUNNING``, ``ABORTED``, ``TERMINATED``, ``COMPLETED``, ``CHECK\_RUNNING``, ``CHECK\_COMPLETED``][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py)[¶](#abaqus.Job.JobMdb.JobFromInputFile.status "Permalink to this definition")
    :   A SymbolicConstant specifying the status of the analysis. Possible values are SUBMITTED,
        RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK\_RUNNING, and CHECK\_COMPLETED.If the
        **message** member is empty, **status** is set to NONE.

    type : --is-rst--:py:data:`~typing.Literal`\[``ANALYSIS``, ``SYNTAXCHECK``, ``RECOVER``] = `'ANALYSIS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L68-L71)[¶](#abaqus.Job.JobMdb.JobFromInputFile.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
        SYNTAXCHECK, and RECOVER. The default value is ANALYSIS.For theJobFromInputFile object,
        **type** = RESTART is not currently supported.

    userSubroutine : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L99-L101)[¶](#abaqus.Job.JobMdb.JobFromInputFile.userSubroutine "Permalink to this definition")
    :   A String specifying the file containing the user’s subroutine definitions. The default
        value is an empty string.

    waitHours : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L78-L81)[¶](#abaqus.Job.JobMdb.JobFromInputFile.waitHours "Permalink to this definition")
    :   An Int specifying the number of hours to wait before submitting the job. This argument
        is ignored if **queue** is set. The default value is 0.This argument works in conjunction
        with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

    waitMinutes : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L83-L86)[¶](#abaqus.Job.JobMdb.JobFromInputFile.waitMinutes "Permalink to this definition")
    :   An Int specifying the number of minutes to wait before submitting the job. This argument
        is ignored if **queue** is set. The default value is 0.This argument works in conjunction
        with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

*class* JobMdb(*[pathName](#abaqus.Job.JobMdb.JobMdb "abaqus.Job.JobMdb.JobMdb.__init__.pathName (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L25-L443)[¶](#abaqus.Job.JobMdb.JobMdb "Permalink to this definition")
:   Bases: [`MdbBase`](index.html#abaqus.Mdb.MdbBase.MdbBase "abaqus.Mdb.MdbBase.MdbBase (Python class) — Bases: object")

    The Mdb object is the high-level Abaqus model database. A model database stores models and analysis
    controls.

    Note

    This object can be accessed by:

    ```python
    mdb
    ```

    Note

    Check [JobMdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all).

    Member Details:

    Job(*[name](#abaqus.Job.JobMdb.JobMdb.Job.name "abaqus.Job.JobMdb.JobMdb.Job.name (Python parameter) — A String specifying the name of the new job.")*, *[model](#abaqus.Job.JobMdb.JobMdb.Job.model "abaqus.Job.JobMdb.JobMdb.Job.model (Python parameter) — A String specifying the name of the model to be analyzed or a Model object specifying the model to be analyzed.")*, *[description](#abaqus.Job.JobMdb.JobMdb.Job.description "abaqus.Job.JobMdb.JobMdb.Job.description (Python parameter) — A String specifying a description of the job.")=`''`*, *[type](#abaqus.Job.JobMdb.JobMdb.Job.type "abaqus.Job.JobMdb.JobMdb.Job.type (Python parameter) — A SymbolicConstant specifying the type of job.")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.JobMdb.JobMdb.Job.queue "abaqus.Job.JobMdb.JobMdb.Job.queue (Python parameter) — A String specifying the name of the queue to which to submit the job.")=`''`*, *[waitHours](#abaqus.Job.JobMdb.JobMdb.Job.waitHours "abaqus.Job.JobMdb.JobMdb.Job.waitHours (Python parameter) — An Int specifying the number of hours to wait before submitting the job.")=`0`*, *[waitMinutes](#abaqus.Job.JobMdb.JobMdb.Job.waitMinutes "abaqus.Job.JobMdb.JobMdb.Job.waitMinutes (Python parameter) — An Int specifying the number of minutes to wait before submitting the job.")=`0`*, *[atTime](#abaqus.Job.JobMdb.JobMdb.Job.atTime "abaqus.Job.JobMdb.JobMdb.Job.atTime (Python parameter) — A String specifying the time at which to submit the job.")=`''`*, *[echoPrint](#abaqus.Job.JobMdb.JobMdb.Job.echoPrint "abaqus.Job.JobMdb.JobMdb.Job.echoPrint (Python parameter) — A Boolean specifying whether an echo of the input data is printed.")=`0`*, *[contactPrint](#abaqus.Job.JobMdb.JobMdb.Job.contactPrint "abaqus.Job.JobMdb.JobMdb.Job.contactPrint (Python parameter) — A Boolean specifying whether contact constraint data are printed.")=`0`*, *[modelPrint](#abaqus.Job.JobMdb.JobMdb.Job.modelPrint "abaqus.Job.JobMdb.JobMdb.Job.modelPrint (Python parameter) — A Boolean specifying whether model definition data are printed.")=`0`*, *[historyPrint](#abaqus.Job.JobMdb.JobMdb.Job.historyPrint "abaqus.Job.JobMdb.JobMdb.Job.historyPrint (Python parameter) — A Boolean specifying whether history data are printed.")=`0`*, *[scratch](#abaqus.Job.JobMdb.JobMdb.Job.scratch "abaqus.Job.JobMdb.JobMdb.Job.scratch (Python parameter) — A String specifying the location of the scratch directory.")=`''`*, *[userSubroutine](#abaqus.Job.JobMdb.JobMdb.Job.userSubroutine "abaqus.Job.JobMdb.JobMdb.Job.userSubroutine (Python parameter) — A String specifying the file containing the user's subroutine definitions.")=`''`*, *[numCpus](#abaqus.Job.JobMdb.JobMdb.Job.numCpus "abaqus.Job.JobMdb.JobMdb.Job.numCpus (Python parameter) — An Int specifying the number of CPUs to use for this analysis if parallel processing is available.")=`1`*, *[memory](#abaqus.Job.JobMdb.JobMdb.Job.memory "abaqus.Job.JobMdb.JobMdb.Job.memory (Python parameter) — An Int specifying the amount of memory available to Abaqus analysis.")=`90`*, *[memoryUnits](#abaqus.Job.JobMdb.JobMdb.Job.memoryUnits "abaqus.Job.JobMdb.JobMdb.Job.memoryUnits (Python parameter) — A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis.")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.JobMdb.JobMdb.Job.explicitPrecision "abaqus.Job.JobMdb.JobMdb.Job.explicitPrecision (Python parameter) — A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit.")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.JobMdb.JobMdb.Job.nodalOutputPrecision "abaqus.Job.JobMdb.JobMdb.Job.nodalOutputPrecision (Python parameter) — A SymbolicConstant specifying the precision of the nodal output written to the output database.")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.JobMdb.JobMdb.Job.numDomains "abaqus.Job.JobMdb.JobMdb.Job.numDomains (Python parameter) — An Int specifying the number of domains for parallel execution in Abaqus/Explicit.")=`1`*, *[activateLoadBalancing](#abaqus.Job.JobMdb.JobMdb.Job.activateLoadBalancing "abaqus.Job.JobMdb.JobMdb.Job.activateLoadBalancing (Python parameter) — A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit.")=`0`*, *[multiprocessingMode](#abaqus.Job.JobMdb.JobMdb.Job.multiprocessingMode "abaqus.Job.JobMdb.JobMdb.Job.multiprocessingMode (Python parameter) — A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message passing interface (MPI).")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.JobMdb.JobMdb.Job.licenseType "abaqus.Job.JobMdb.JobMdb.Job.licenseType (Python parameter) — A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model.")=`abaqusConstants.DEFAULT`*, *\*[args](#abaqus.Job.JobMdb.JobMdb.Job "abaqus.Job.JobMdb.JobMdb.Job.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Job.JobMdb.JobMdb.Job "abaqus.Job.JobMdb.JobMdb.Job.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L36-L204)[¶](#abaqus.Job.JobMdb.JobMdb.Job "Permalink to this definition")
    :   This method creates an analysis job using a model on a model database (MDB) for the model definition.

        Note

        This function can be accessed by:

        ```python
        mdb.Job
        ```

        Changed in version 2023: The `parallelizationMethodExplicit` argument was removed.

        Note

        Check [Job on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Job.JobMdb.JobMdb.Job-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Job.JobMdb.JobMdb.Job.name "Permalink to this definition")
            :   A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
                name.

            model[¶](#abaqus.Job.JobMdb.JobMdb.Job.model "Permalink to this definition")
            :   A String specifying the name of the model to be analyzed or a Model object specifying
                the model to be analyzed.

            description=`''`[¶](#abaqus.Job.JobMdb.JobMdb.Job.description "Permalink to this definition")
            :   A String specifying a description of the job.

            type=`abaqusConstants.ANALYSIS`[¶](#abaqus.Job.JobMdb.JobMdb.Job.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
                SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the
                type JobFromInputFile, **type** = RESTART is not available.

            queue=`''`[¶](#abaqus.Job.JobMdb.JobMdb.Job.queue "Permalink to this definition")
            :   A String specifying the name of the queue to which to submit the job. The default value
                is an empty string. Note: You can use the **queue** argument when creating a Job object on a
                Windows workstation; however, remote queues are available only on Linux platforms.

            waitHours=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.waitHours "Permalink to this definition")
            :   An Int specifying the number of hours to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

            waitMinutes=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.waitMinutes "Permalink to this definition")
            :   An Int specifying the number of minutes to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

            atTime=`''`[¶](#abaqus.Job.JobMdb.JobMdb.Job.atTime "Permalink to this definition")
            :   A String specifying the time at which to submit the job. If **queue** is empty, the string
                syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
                valid according to the system administrator. The default value is an empty
                string. Note: You can use the **atTime** argument when creating a Job object on a Windows
                workstation; however, the `at` command is available only on Linux platforms.

            echoPrint=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.echoPrint "Permalink to this definition")
            :   A Boolean specifying whether an echo of the input data is printed. The default value is
                OFF.

            contactPrint=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.contactPrint "Permalink to this definition")
            :   A Boolean specifying whether contact constraint data are printed. The default value is
                OFF.

            modelPrint=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.modelPrint "Permalink to this definition")
            :   A Boolean specifying whether model definition data are printed. The default value is
                OFF.

            historyPrint=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.historyPrint "Permalink to this definition")
            :   A Boolean specifying whether history data are printed. The default value is OFF.

            scratch=`''`[¶](#abaqus.Job.JobMdb.JobMdb.Job.scratch "Permalink to this definition")
            :   A String specifying the location of the scratch directory. The default value is an empty
                string.

            userSubroutine=`''`[¶](#abaqus.Job.JobMdb.JobMdb.Job.userSubroutine "Permalink to this definition")
            :   A String specifying the file containing the user’s subroutine definitions. The default
                value is an empty string.

            numCpus=`1`[¶](#abaqus.Job.JobMdb.JobMdb.Job.numCpus "Permalink to this definition")
            :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
                available. Possible values are **numCpus** > 0. The default value is 1.

            memory=`90`[¶](#abaqus.Job.JobMdb.JobMdb.Job.memory "Permalink to this definition")
            :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
                expressed in the units supplied in **memoryUnits**. The default value is 90.

            memoryUnits=`abaqusConstants.PERCENTAGE`[¶](#abaqus.Job.JobMdb.JobMdb.Job.memoryUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
                analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
                is PERCENTAGE.

            explicitPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobMdb.Job.explicitPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the double precision version of
                Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
                DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

            nodalOutputPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobMdb.Job.nodalOutputPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying the precision of the nodal output written to the output
                database. Possible values are SINGLE and FULL. The default value is SINGLE.

            numDomains=`1`[¶](#abaqus.Job.JobMdb.JobMdb.Job.numDomains "Permalink to this definition")
            :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
                using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

                Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
                argument was removed in 2023.

            activateLoadBalancing=`0`[¶](#abaqus.Job.JobMdb.JobMdb.Job.activateLoadBalancing "Permalink to this definition")
            :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
                multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

            multiprocessingMode=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobMdb.Job.multiprocessingMode "Permalink to this definition")
            :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
                multiple processes that communicate through a message passing interface (MPI). Possible
                values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

            licenseType=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobMdb.Job.licenseType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of license type being used in the case of the
                DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
                value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
                available.

                Changed in version 2022: The `licenseType` argument was added.

        Returns:[¶](#abaqus.Job.JobMdb.JobMdb.Job-returns "Permalink to this headline")
        :   A ModelJob object.

        Return type:[¶](#abaqus.Job.JobMdb.JobMdb.Job-return-type "Permalink to this headline")
        :   `ModelJob`

        Raises:[¶](#abaqus.Job.JobMdb.JobMdb.Job-raises "Permalink to this headline")
        :   [**AbaqusException**](../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    JobFromInputFile(*[name](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.name "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.name (Python parameter) — A String specifying the name of the new job.")*, *[inputFileName](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.inputFileName "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.inputFileName (Python parameter) — A String specifying the input file to read.")*, *[type](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.type "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.type (Python parameter) — A SymbolicConstant specifying the type of job.")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.queue "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.queue (Python parameter) — A String specifying the name of the queue to which to submit the job.")=`''`*, *[waitHours](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitHours "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitHours (Python parameter) — An Int specifying the number of hours to wait before submitting the job.")=`0`*, *[waitMinutes](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitMinutes "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitMinutes (Python parameter) — An Int specifying the number of minutes to wait before submitting the job.")=`0`*, *[atTime](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.atTime "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.atTime (Python parameter) — A String specifying the time at which to submit the job.")=`''`*, *[scratch](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.scratch "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.scratch (Python parameter) — A String specifying the location of the scratch directory.")=`''`*, *[userSubroutine](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.userSubroutine "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.userSubroutine (Python parameter) — A String specifying the file containing the user's subroutine definitions.")=`''`*, *[numCpus](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numCpus "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numCpus (Python parameter) — An Int specifying the number of CPUs to use for this analysis if parallel processing is available.")=`1`*, *[memory](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memory "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memory (Python parameter) — An Int specifying the amount of memory available to Abaqus analysis.")=`90`*, *[memoryUnits](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memoryUnits "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memoryUnits (Python parameter) — A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis.")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.explicitPrecision "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.explicitPrecision (Python parameter) — A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit.")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.nodalOutputPrecision "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.nodalOutputPrecision (Python parameter) — A SymbolicConstant specifying the precision of the nodal output written to the output database.")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numDomains "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numDomains (Python parameter) — An Int specifying the number of domains for parallel execution in Abaqus/Explicit.")=`1`*, *[activateLoadBalancing](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.activateLoadBalancing "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.activateLoadBalancing (Python parameter) — A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit.")=`0`*, *[multiprocessingMode](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.multiprocessingMode "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.multiprocessingMode (Python parameter) — A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.licenseType "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.licenseType (Python parameter) — A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model.")=`abaqusConstants.DEFAULT`*, *[getMemoryFromAnalysis](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.getMemoryFromAnalysis "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.getMemoryFromAnalysis (Python parameter) — A Boolean specifying whether to retrieve the recommended memory settings from the last datacheck or analysis run and use those values in subsequent submissions.")=`1`*, *[numGPUs](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numGPUs "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numGPUs (Python parameter) — An Int specifying the number of GPUs to use for this analysis if parallel processing is available.")=`0`*, *[resultsFormat](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.resultsFormat "abaqus.Job.JobMdb.JobMdb.JobFromInputFile.resultsFormat (Python parameter) — This option specifies the results output format: ODB, SIM, or BOTH.")=`abaqusConstants.ODB`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L206-L348)[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile "Permalink to this definition")
    :   This method creates an analysis job using an input file for the model definition.

        Note

        This function can be accessed by:

        ```python
        mdb.JobFromInputFile
        ```

        Changed in version 2023: The `parallelizationMethodExplicit` argument was removed.

        Note

        Check [JobFromInputFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobfrominputfilepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.name "Permalink to this definition")
            :   A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
                name.

            inputFileName[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.inputFileName "Permalink to this definition")
            :   A String specifying the input file to read. Possible values are any valid file name. If
                the .inp extension is not included in the value of the argument, the system will append
                it for the user.

            type=`abaqusConstants.ANALYSIS`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
                SYNTAXCHECK, and RECOVER. The default value is ANALYSIS.For theJobFromInputFile object,
                **type** = RESTART is not currently supported.

            queue=`''`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.queue "Permalink to this definition")
            :   A String specifying the name of the queue to which to submit the job. The default value
                is an empty string. Note: You can use the **queue** argument when creating a Job object on
                a Windows workstation; however, remote queues are available only on Linux platforms.

            waitHours=`0`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitHours "Permalink to this definition")
            :   An Int specifying the number of hours to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

            waitMinutes=`0`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.waitMinutes "Permalink to this definition")
            :   An Int specifying the number of minutes to wait before submitting the job. This argument
                is ignored if **queue** is set. The default value is 0.This argument works in conjunction
                with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

            atTime=`''`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.atTime "Permalink to this definition")
            :   A String specifying the time at which to submit the job. If **queue** is empty, the string
                syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
                valid according to the system administrator. The default value is an empty string. Note:
                You can use the **atTime** argument when creating a Job object on a Windows workstation;
                however, the `at` command is available only on Linux platforms.

            scratch=`''`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.scratch "Permalink to this definition")
            :   A String specifying the location of the scratch directory. The default value is an empty
                string.

            userSubroutine=`''`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.userSubroutine "Permalink to this definition")
            :   A String specifying the file containing the user’s subroutine definitions. The default
                value is an empty string.

            numCpus=`1`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numCpus "Permalink to this definition")
            :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
                available. Possible values are **numCpus** > 0. The default value is 1.

            memory=`90`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memory "Permalink to this definition")
            :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
                expressed in the units supplied in **memoryUnits**. The default value is 90.

            memoryUnits=`abaqusConstants.PERCENTAGE`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.memoryUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
                analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
                is PERCENTAGE.

            explicitPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.explicitPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the double precision version of
                Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
                DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

            nodalOutputPrecision=`abaqusConstants.SINGLE`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.nodalOutputPrecision "Permalink to this definition")
            :   A SymbolicConstant specifying the precision of the nodal output written to the output
                database. Possible values are SINGLE and FULL. The default value is SINGLE.

            numDomains=`1`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numDomains "Permalink to this definition")
            :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
                using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

                Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
                argument was removed in 2023.

            activateLoadBalancing=`0`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.activateLoadBalancing "Permalink to this definition")
            :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
                multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

            multiprocessingMode=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.multiprocessingMode "Permalink to this definition")
            :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
                multiple processes that communicate through a message

            licenseType=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.licenseType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of license type being used in the case of the
                DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
                value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
                available.

            getMemoryFromAnalysis=`1`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.getMemoryFromAnalysis "Permalink to this definition")
            :   A Boolean specifying whether to retrieve the recommended memory settings from the last
                datacheck or analysis run and use those values in subsequent submissions. The default
                value is ON.

            numGPUs=`0`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.numGPUs "Permalink to this definition")
            :   An Int specifying the number of GPUs to use for this analysis if parallel processing is
                available. Possible values are **numCpus** >= 0. The default value is 0.

            resultsFormat=`abaqusConstants.ODB`[¶](#abaqus.Job.JobMdb.JobMdb.JobFromInputFile.resultsFormat "Permalink to this definition")
            :   This option specifies the results output format: ODB, SIM, or BOTH. The default value is ODB.

    OptimizationProcess(*[name](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.name "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.name (Python parameter) — A String specifying name of the optimization process.")*, *[model](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.model "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.model (Python parameter) — A String specifying name of the model to be used for the optimization process.")*, *[task](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.task "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.task (Python parameter) — A String specifying name of the optimization task to be used for the optimization process.")*, *[prototypeJob](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.prototypeJob "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.prototypeJob (Python parameter) — A String specifying name of the job to be used as the prototype for all analysis jobs run by the optimization process.")*, *[description](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.description "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.description (Python parameter) — A String specifying a description of the optimization process.")=`''`*, *[maxDesignCycle](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.maxDesignCycle "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.maxDesignCycle (Python parameter) — An Int specifying the maximum number of allowed design cycles for the optimization process.")=`15`*, *[dataSaveFrequency](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.dataSaveFrequency "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.dataSaveFrequency (Python parameter) — An Enum specifying whether Abaqus should save every iteration file in the optimization process or a selection of iteration files saved at a user-specified frequency.")=`abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE`*, *[saveInitial](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveInitial "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveInitial (Python parameter) — A Boolean specifying whether the initial cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveFirst](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveFirst "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveFirst (Python parameter) — A Boolean specifying whether the first cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveLast](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveLast "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveLast (Python parameter) — A Boolean specifying whether the last cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveEvery](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveEvery "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveEvery (Python parameter) — An Int specifying every nth cycle iterations to be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`None`*, *[licenseType](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.licenseType "abaqus.Job.JobMdb.JobMdb.OptimizationProcess.licenseType (Python parameter) — A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model.")=`abaqusConstants.DEFAULT`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobMdb.py#L350-L443)[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess "Permalink to this definition")
    :   This method creates an OptimizationProcess object.

        Note

        This function can be accessed by:

        ```python
        mdb.OptimizationProcess
        ```

        Note

        Check [OptimizationProcess on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.name "Permalink to this definition")
            :   A String specifying name of the optimization process.

            model[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.model "Permalink to this definition")
            :   A String specifying name of the model to be used for the optimization process.

            task[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.task "Permalink to this definition")
            :   A String specifying name of the optimization task to be used for the optimization
                process.

            prototypeJob[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.prototypeJob "Permalink to this definition")
            :   A String specifying name of the job to be used as the prototype for all analysis jobs
                run by the optimization process.

            description=`''`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.description "Permalink to this definition")
            :   A String specifying a description of the optimization process.

            maxDesignCycle=`15`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.maxDesignCycle "Permalink to this definition")
            :   An Int specifying the maximum number of allowed design cycles for the optimization
                process. The default value is 15.

            dataSaveFrequency=`abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.dataSaveFrequency "Permalink to this definition")
            :   An Enum specifying whether Abaqus should save every iteration file in the optimization
                process or a selection of iteration files saved at a user-specified frequency. If you
                set **dataSaveFrequency** = OPT\_DATASAVE\_EVERY\_CYCLE, Abaqus saves every iteration file; if
                you set **dataSaveFrequency** = OPT\_DATASAVE\_SPECIFY\_CYCLE, Abaqus saves iteration files
                according to the frequency defined by the **saveEvery** parameter. The default value is
                OPT\_DATASAVE\_SPECIFY\_CYCLE.

            saveInitial=`True`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveInitial "Permalink to this definition")
            :   A Boolean specifying whether the initial cycle should be saved when **dataSaveFrequency**
                is OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveFirst=`True`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveFirst "Permalink to this definition")
            :   A Boolean specifying whether the first cycle should be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveLast=`True`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveLast "Permalink to this definition")
            :   A Boolean specifying whether the last cycle should be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveEvery=`None`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.saveEvery "Permalink to this definition")
            :   An Int specifying every nth cycle iterations to be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. Abaqus saves file iterations for every nth iteration after
                iteration 1; if you set **saveEvery** = 3, Abaqus saves file iterations for cycles 1, 4, 7,
                and so on. The default value is None.

            licenseType=`abaqusConstants.DEFAULT`[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess.licenseType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license
                model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value is DEFAULT.
                For optimization job submission, the licenseType options are available regardless of the license model.

                New in version 2024: The argument `licenseType` was added.

        Returns:[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess-returns "Permalink to this headline")
        :   An OptimizationProcess object.

        Return type:[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess-return-type "Permalink to this headline")
        :   [`OptimizationProcess`](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess "abaqus.Job.JobMdb.JobMdb.OptimizationProcess (Python method) — This method creates an OptimizationProcess object.")

        Raises:[¶](#abaqus.Job.JobMdb.JobMdb.OptimizationProcess-raises "Permalink to this headline")
        :   [**AbaqusException**](../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

*class* ModelJob(*[name](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.name (Python parameter)")*, *[model](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.model (Python parameter)")*, *[description](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.description (Python parameter)")=`''`*, *[type](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.type (Python parameter)")=`abaqusConstants.ANALYSIS`*, *[queue](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.queue (Python parameter)")=`''`*, *[waitHours](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.waitHours (Python parameter)")=`0`*, *[waitMinutes](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.waitMinutes (Python parameter)")=`0`*, *[atTime](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.atTime (Python parameter)")=`''`*, *[echoPrint](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.echoPrint (Python parameter)")=`0`*, *[contactPrint](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.contactPrint (Python parameter)")=`0`*, *[modelPrint](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.modelPrint (Python parameter)")=`0`*, *[historyPrint](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.historyPrint (Python parameter)")=`0`*, *[scratch](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.scratch (Python parameter)")=`''`*, *[userSubroutine](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.userSubroutine (Python parameter)")=`''`*, *[numCpus](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.numCpus (Python parameter)")=`1`*, *[memory](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.memory (Python parameter)")=`90`*, *[memoryUnits](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.memoryUnits (Python parameter)")=`abaqusConstants.PERCENTAGE`*, *[explicitPrecision](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.explicitPrecision (Python parameter)")=`abaqusConstants.SINGLE`*, *[nodalOutputPrecision](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.nodalOutputPrecision (Python parameter)")=`abaqusConstants.SINGLE`*, *[numDomains](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.numDomains (Python parameter)")=`1`*, *[activateLoadBalancing](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.activateLoadBalancing (Python parameter)")=`0`*, *[multiprocessingMode](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.multiprocessingMode (Python parameter)")=`abaqusConstants.DEFAULT`*, *[licenseType](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.licenseType (Python parameter)")=`abaqusConstants.DEFAULT`*, *\*[args](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Job.ModelJob.ModelJob "abaqus.Job.ModelJob.ModelJob.__init__.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L21-L310)[¶](#abaqus.Job.ModelJob.ModelJob "Permalink to this definition")
:   Bases: `Job`

    The ModelJob object defines a Job object which analyzes a model on a model database (MDB). The ModelJob
    object is derived from the Job object.

    Note

    This object can be accessed by:

    ```python
    import job
    mdb.adaptivityProcesses[name].job
    mdb.jobs[name]
    ```

    Changed in version 2023: The `parallelizationMethodExplicit` attribute was removed.

    Note

    Check [ModelJob on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeljobpyc.htm?contextscope=all).

    Member Details:

    activateLoadBalancing : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L117-L119)[¶](#abaqus.Job.ModelJob.ModelJob.activateLoadBalancing "Permalink to this definition")
    :   A Boolean specifying whether to activate dyanmic load balancing for jobs running on
        multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

    analysis : --is-rst--Literal[C.STANDARD, C.EXPLICIT, C.UNKNOWN][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py)[¶](#abaqus.Job.ModelJob.ModelJob.analysis "Permalink to this definition")
    :   A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or
        Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has
        the type JobFromInputFile, **analysis** = UNKNOWN.

    atTime : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L141-L146)[¶](#abaqus.Job.ModelJob.ModelJob.atTime "Permalink to this definition")
    :   A String specifying the time at which to submit the job. If **queue** is empty, the string
        syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
        valid according to the system administrator. The default value is an empty
        string. Note: You can use the **atTime** argument when creating a Job object on a Windows
        workstation; however, the `at` command is available only on Linux platforms.

    contactPrint : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L46-L48)[¶](#abaqus.Job.ModelJob.ModelJob.contactPrint "Permalink to this definition")
    :   A Boolean specifying whether contact constraint data are printed. The default value is
        OFF.

    description : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L61-L62)[¶](#abaqus.Job.ModelJob.ModelJob.description "Permalink to this definition")
    :   A String specifying a description of the job.

    echoPrint : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L42-L44)[¶](#abaqus.Job.ModelJob.ModelJob.echoPrint "Permalink to this definition")
    :   A Boolean specifying whether an echo of the input data is printed. The default value is
        OFF.

    environment : --is-rst--tuple[str, ...] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L159-L160)[¶](#abaqus.Job.ModelJob.ModelJob.environment "Permalink to this definition")
    :   A tuple of Strings specifying the environment variables and their values.

    explicitPrecision : --is-rst--Literal[C.SINGLE, C.FORCE\_SINGLE, C.DOUBLE, C.DOUBLE\_CONSTRAINT\_ONLY, C.DOUBLE\_PLUS\_PACK] = `'SINGLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L97-L100)[¶](#abaqus.Job.ModelJob.ModelJob.explicitPrecision "Permalink to this definition")
    :   A SymbolicConstant specifying whether to use the double precision version of
        Abaqus/Explicit. Possible values are SINGLE, FORCE\_SINGLE, DOUBLE,
        DOUBLE\_CONSTRAINT\_ONLY, and DOUBLE\_PLUS\_PACK. The default value is SINGLE.

    getMemoryFromAnalysis : --is-rst--Boolean = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L92-L95)[¶](#abaqus.Job.ModelJob.ModelJob.getMemoryFromAnalysis "Permalink to this definition")
    :   A Boolean specifying whether to retrieve the recommended memory settings from the last
        datacheck or analysis run and use those values in subsequent submissions. The default
        value is ON.

    historyPrint : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L54-L55)[¶](#abaqus.Job.ModelJob.ModelJob.historyPrint "Permalink to this definition")
    :   A Boolean specifying whether history data are printed. The default value is OFF.

    memory : --is-rst--int = `90`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L83-L85)[¶](#abaqus.Job.ModelJob.ModelJob.memory "Permalink to this definition")
    :   An Int specifying the amount of memory available to Abaqus analysis. The value should be
        expressed in the units supplied in **memoryUnits**. The default value is 90.

    memoryUnits : --is-rst--Literal[C.PERCENTAGE, C.MEGA\_BYTES, C.GIGA\_BYTES] = `'PERCENTAGE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L87-L90)[¶](#abaqus.Job.ModelJob.ModelJob.memoryUnits "Permalink to this definition")
    :   A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
        analysis. Possible values are PERCENTAGE, MEGA\_BYTES, and GIGA\_BYTES. The default value
        is PERCENTAGE.

    messages : --is-rst--MessageArray = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L156-L157)[¶](#abaqus.Job.ModelJob.ModelJob.messages "Permalink to this definition")
    :   A MessageArray object specifying the messages received during an analysis.

    model : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L57-L59)[¶](#abaqus.Job.ModelJob.ModelJob.model "Permalink to this definition")
    :   A String specifying the name of the model to be analyzed or a Model object specifying
        the model to be analyzed.

    modelPrint : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L50-L52)[¶](#abaqus.Job.ModelJob.ModelJob.modelPrint "Permalink to this definition")
    :   A Boolean specifying whether model definition data are printed. The default value is
        OFF.

    multiprocessingMode : --is-rst--Literal[C.DEFAULT, C.THREADS, C.MPI] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L121-L124)[¶](#abaqus.Job.ModelJob.ModelJob.multiprocessingMode "Permalink to this definition")
    :   A SymbolicConstant specifying whether an analysis is decomposed into threads or into
        multiple processes that communicate through a message passing interface (MPI). Possible
        values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

    name : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L38-L40)[¶](#abaqus.Job.ModelJob.ModelJob.name "Permalink to this definition")
    :   A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
        name.

    nodalOutputPrecision : --is-rst--Literal[C.SINGLE, C.FULL] = `'SINGLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L104-L106)[¶](#abaqus.Job.ModelJob.ModelJob.nodalOutputPrecision "Permalink to this definition")
    :   A SymbolicConstant specifying the precision of the nodal output written to the output
        database. Possible values are SINGLE and FULL. The default value is SINGLE.

    numCpus : --is-rst--int = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L79-L81)[¶](#abaqus.Job.ModelJob.ModelJob.numCpus "Permalink to this definition")
    :   An Int specifying the number of CPUs to use for this analysis if parallel processing is
        available. Possible values are **numCpus** > 0. The default value is 1.

    numDomains : --is-rst--int = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L113-L115)[¶](#abaqus.Job.ModelJob.ModelJob.numDomains "Permalink to this definition")
    :   An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
        using more than 1 numCpus, numDomains must be a multiple of numCpus. The default value is 1.

        Changed in version 2023: The docs for this argument were updated to reflect that the `parallelizationMethodExplicit`
        argument was removed in 2023.

    queue : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L136-L139)[¶](#abaqus.Job.ModelJob.ModelJob.queue "Permalink to this definition")
    :   A String specifying the name of the queue to which to submit the job. The default value
        is an empty string. Note: You can use the **queue** argument when creating a Job object on a
        Windows workstation; however, remote queues are available only on Linux platforms.

    scratch : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L148-L150)[¶](#abaqus.Job.ModelJob.ModelJob.scratch "Permalink to this definition")
    :   A String specifying the location of the scratch directory. The default value is an empty
        string.

    setValues(*\*[args](#abaqus.Job.ModelJob.ModelJob.setValues "abaqus.Job.ModelJob.ModelJob.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Job.ModelJob.ModelJob.setValues "abaqus.Job.ModelJob.ModelJob.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L307-L310)[¶](#abaqus.Job.ModelJob.ModelJob.setValues "Permalink to this definition")
    :   This method modifies the ModelJob object.

    status : --is-rst--Literal[C.SUBMITTED, C.RUNNING, C.ABORTED, C.TERMINATED, C.COMPLETED, C.CHECK\_RUNNING, C.CHECK\_COMPLETED][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py)[¶](#abaqus.Job.ModelJob.ModelJob.status "Permalink to this definition")
    :   A SymbolicConstant specifying the status of the analysis. Possible values are SUBMITTED,
        RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK\_RUNNING, and CHECK\_COMPLETED.If the
        **message** member is empty, **status** is set to NONE.

    type : --is-rst--Literal[C.ANALYSIS, C.SYNTAXCHECK, C.RECOVER, C.RESTART] = `'ANALYSIS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L64-L67)[¶](#abaqus.Job.ModelJob.ModelJob.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
        SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS. If the object has the
        type JobFromInputFile, **type** = RESTART is not available.

    userSubroutine : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L152-L154)[¶](#abaqus.Job.ModelJob.ModelJob.userSubroutine "Permalink to this definition")
    :   A String specifying the file containing the user’s subroutine definitions. The default
        value is an empty string.

    waitHours : --is-rst--int = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L69-L72)[¶](#abaqus.Job.ModelJob.ModelJob.waitHours "Permalink to this definition")
    :   An Int specifying the number of hours to wait before submitting the job. This argument
        is ignored if **queue** is set. The default value is 0.This argument works in conjunction
        with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.

    waitMinutes : --is-rst--int = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L74-L77)[¶](#abaqus.Job.ModelJob.ModelJob.waitMinutes "Permalink to this definition")
    :   An Int specifying the number of minutes to wait before submitting the job. This argument
        is ignored if **queue** is set. The default value is 0.This argument works in conjunction
        with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.

    writeInput(*[consistencyChecking](#abaqus.Job.ModelJob.ModelJob.writeInput.consistencyChecking "abaqus.Job.ModelJob.ModelJob.writeInput.consistencyChecking (Python parameter) — A Boolean specifying whether to perform consistency checking for the job.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/ModelJob.py#L294-L305)[¶](#abaqus.Job.ModelJob.ModelJob.writeInput "Permalink to this definition")
    :   This method writes an input file.

        Note

        Check [ModelJob.writeInput on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeljobpyc.htm?contextscope=all#simaker-modeljobwriteinputpyc).

        Parameters:[¶](#abaqus.Job.ModelJob.ModelJob.writeInput-parameters "Permalink to this headline")
        :   consistencyChecking=`1`[¶](#abaqus.Job.ModelJob.ModelJob.writeInput.consistencyChecking "Permalink to this definition")
            :   A Boolean specifying whether to perform consistency checking for the job. The default
                value is ON.It is not recommended to turn the consistency checking off unless you are
                absolutely sure the model is consistent.

*class* OptimizationProcess(*[name](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.name (Python parameter)")*, *[model](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.model (Python parameter)")*, *[task](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.task (Python parameter)")*, *[prototypeJob](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.prototypeJob (Python parameter)")*, *[description](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.description (Python parameter)")=`''`*, *[maxDesignCycle](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.maxDesignCycle (Python parameter)")=`15`*, *[dataSaveFrequency](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.dataSaveFrequency (Python parameter)")=`abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE`*, *[saveInitial](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.saveInitial (Python parameter)")=`True`*, *[saveFirst](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.saveFirst (Python parameter)")=`True`*, *[saveLast](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.saveLast (Python parameter)")=`True`*, *[saveEvery](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.saveEvery (Python parameter)")=`None`*, *[licenseType](#abaqus.Job.OptimizationProcess.OptimizationProcess "abaqus.Job.OptimizationProcess.OptimizationProcess.__init__.licenseType (Python parameter)")=`abaqusConstants.DEFAULT`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L16-L287)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OptimizationProcess object defines a process to perform an optimization of a model defined using an
    optimization task.

    Note

    This object can be accessed by:

    ```python
    import job
    mdb.optimizationProcesses[name]
    ```

    Note

    Check [OptimizationProcess on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?contextscope=all).

    Member Details:

    dataSaveFrequency : --is-rst--:py:class:`str` = `'OPT_DATASAVE_SPECIFY_CYCLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L49-L55)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.dataSaveFrequency "Permalink to this definition")
    :   An Enum specifying whether Abaqus should save every iteration file in the optimization
        process or a selection of iteration files saved at a user-specified frequency. If you
        set **dataSaveFrequency** = OPT\_DATASAVE\_EVERY\_CYCLE, Abaqus saves every iteration file; if
        you set **dataSaveFrequency** = OPT\_DATASAVE\_SPECIFY\_CYCLE, Abaqus saves iteration files
        according to the frequency defined by the **saveEvery** parameter. The default value is
        OPT\_DATASAVE\_SPECIFY\_CYCLE.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L42-L43)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.description "Permalink to this definition")
    :   A String specifying a description of the optimization process.

    extract(*[outputFileName](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.outputFileName "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.outputFileName (Python parameter) — Name of the output file for the extracted surface mesh.")*, *[designCycle](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.designCycle "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.designCycle (Python parameter) — The design cycle number for which the surface mesh should be extracted.")*, *[isoValue](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.isoValue "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.isoValue (Python parameter) — Value used to determine the positions on the element edges where the new nodes are created.")=`0`*, *[smoothCycles](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.smoothCycles "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.smoothCycles (Python parameter) — Number of smoothing cycles; if set to 0, no smoothing is performed.")=`5`*, *[reductionPercent](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionPercent "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionPercent (Python parameter) — Defines the percent of faces that should be removed during the data reduction.")=`0`*, *[reductionAngle](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionAngle "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionAngle (Python parameter) — Defines the maximal angle between adjacent faces at a node such that the node may be removed during the data reduction.")=`''`*, *[targetVolume](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.targetVolume "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.targetVolume (Python parameter) — Defines the target volume that is to be achieved iteratively by varying the isovalue. Value between 0 and 1.")=`0`*, *[extractFormat](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.extractFormat "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.extractFormat (Python parameter) — Tuple for the types of format of the output.")=`abaqusConstants.OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE`*, *[resultFiltering](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.resultFiltering "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.resultFiltering (Python parameter) — Possible string values are OFF or MODERATE or FULL.")=`0`*, *[instances](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.instances "abaqus.Job.OptimizationProcess.OptimizationProcess.extract.instances (Python parameter) — Defines a list of names of part instances to be used for surface extraction.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L191-L243)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract "Permalink to this definition")
    :   This method extracts a surface mesh from the optimized model.

        Note

        Check [OptimizationProcess.extract on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?contextscope=all#simaker-optimizationprocessextractpyc).

        Parameters:[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract-parameters "Permalink to this headline")
        :   outputFileName[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.outputFileName "Permalink to this definition")
            :   Name of the output file for the extracted surface mesh.

            designCycle[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.designCycle "Permalink to this definition")
            :   The design cycle number for which the surface mesh should be extracted.

            isoValue=`0`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.isoValue "Permalink to this definition")
            :   Value used to determine the positions on the element edges where the new nodes are
                created. Value between 0 and 1. The default value is 0.3.

            smoothCycles=`5`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.smoothCycles "Permalink to this definition")
            :   Number of smoothing cycles; if set to 0, no smoothing is performed. The default value is
                5.

            reductionPercent=`0`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionPercent "Permalink to this definition")
            :   Defines the percent of faces that should be removed during the data reduction. If set to
                0, no data reduction occurs. If set to 100, the data reduction stops when no faces can
                be removed (that is checked using reductionAngle parameter). Value between 0 and 100.
                The default value is 0.

            reductionAngle=`''`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.reductionAngle "Permalink to this definition")
            :   Defines the maximal angle between adjacent faces at a node such that the node may be
                removed during the data reduction. Value in degrees between 0 and 90. The default value
                is15.

            targetVolume=`0`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.targetVolume "Permalink to this definition")
            :   Defines the target volume that is to be achieved iteratively by varying the isovalue.
                Value between 0 and 1. The default value is 0.

            extractFormat=`abaqusConstants.OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.extractFormat "Permalink to this definition")
            :   Tuple for the types of format of the output. Values are (OPT\_EXTRACT\_SMOOTH\_ABAQUS\_INPUT\_FILE,
                OPT\_EXTRACT\_SMOOTH\_STL). Default: OPT\_EXTRACT\_SMOOTH\_ABAQUS\_INPUT\_FILE

            resultFiltering=`0`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.resultFiltering "Permalink to this definition")
            :   Possible string values are OFF or MODERATE or FULL. Defines if the element material
                values are to be filtered (averaged locally) before the isocut, and to what extent. The
                default value is OFF.

            instances=`''`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.extract.instances "Permalink to this definition")
            :   Defines a list of names of part instances to be used for surface extraction. One file
                (according to extractFormat) is created for each part instance. If the argument is not
                specified, no part instance is selected and surface is generated for the whole model.

    licenseType : --is-rst--:py:data:`~typing.Literal`\[``DEFAULT``, ``TOKEN``, ``CREDIT``] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L81-L82)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.licenseType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license
        model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value is DEFAULT.
        For optimization job submission, the licenseType options are available regardless of the license model.

        New in version 2024: The argument `licenseType` was added.

    maxDesignCycle : --is-rst--:py:class:`int` = `15`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L45-L47)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.maxDesignCycle "Permalink to this definition")
    :   An Int specifying the maximum number of allowed design cycles for the optimization
        process. The default value is 15.

    model : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.model "Permalink to this definition")
    :   A String specifying name of the model to be used for the optimization process.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.name "Permalink to this definition")
    :   A String specifying name of the optimization process.

    prototypeJob : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.prototypeJob "Permalink to this definition")
    :   A String specifying name of the job to be used as the prototype for all analysis jobs
        run by the optimization process.

    saveEvery : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L69-L73)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.saveEvery "Permalink to this definition")
    :   An Int specifying every nth cycle iterations to be saved when **dataSaveFrequency** is
        OPT\_DATASAVE\_SPECIFY\_CYCLE. Abaqus saves file iterations for every nth iteration after
        iteration 1; if you set **saveEvery** = 3, Abaqus saves file iterations for cycles 1, 4, 7,
        and so on. The default value is None.

    saveFirst : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `True`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L61-L63)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.saveFirst "Permalink to this definition")
    :   A Boolean specifying whether the first cycle should be saved when **dataSaveFrequency** is
        OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

    saveInitial : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `True`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L57-L59)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.saveInitial "Permalink to this definition")
    :   A Boolean specifying whether the initial cycle should be saved when **dataSaveFrequency**
        is OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

    saveLast : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `True`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L65-L67)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.saveLast "Permalink to this definition")
    :   A Boolean specifying whether the last cycle should be saved when **dataSaveFrequency** is
        OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

    setValues(*[description](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.description "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.description (Python parameter) — A String specifying a description of the optimization process.")=`''`*, *[maxDesignCycle](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.maxDesignCycle "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.maxDesignCycle (Python parameter) — An Int specifying the maximum number of allowed design cycles for the optimization process.")=`15`*, *[dataSaveFrequency](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.dataSaveFrequency "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.dataSaveFrequency (Python parameter) — An Enum specifying whether Abaqus should save every iteration file in the optimization process or a selection of iteration files saved at a user-specified frequency.")=`abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE`*, *[saveInitial](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveInitial "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveInitial (Python parameter) — A Boolean specifying whether the initial cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveFirst](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveFirst "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveFirst (Python parameter) — A Boolean specifying whether the first cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveLast](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveLast "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveLast (Python parameter) — A Boolean specifying whether the last cycle should be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`True`*, *[saveEvery](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveEvery "abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveEvery (Python parameter) — An Int specifying every nth cycle iterations to be saved when dataSaveFrequency is OPT_DATASAVE_SPECIFY_CYCLE.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L245-L287)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues "Permalink to this definition")
    :   This method modifies the OptimizationProcess object.

        Note

        Check [OptimizationProcess.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?contextscope=all#simaker-optimizationprocesssetvaluespyc).

        Parameters:[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues-parameters "Permalink to this headline")
        :   description=`''`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.description "Permalink to this definition")
            :   A String specifying a description of the optimization process.

            maxDesignCycle=`15`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.maxDesignCycle "Permalink to this definition")
            :   An Int specifying the maximum number of allowed design cycles for the optimization
                process. The default value is 15.

            dataSaveFrequency=`abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.dataSaveFrequency "Permalink to this definition")
            :   An Enum specifying whether Abaqus should save every iteration file in the optimization
                process or a selection of iteration files saved at a user-specified frequency. If you
                set **dataSaveFrequency** = OPT\_DATASAVE\_EVERY\_CYCLE, Abaqus saves every iteration file; if
                you set **dataSaveFrequency** = OPT\_DATASAVE\_SPECIFY\_CYCLE, Abaqus saves iteration files
                according to the frequency defined by the **saveEvery** parameter. The default value is
                OPT\_DATASAVE\_SPECIFY\_CYCLE.

            saveInitial=`True`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveInitial "Permalink to this definition")
            :   A Boolean specifying whether the initial cycle should be saved when **dataSaveFrequency**
                is OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveFirst=`True`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveFirst "Permalink to this definition")
            :   A Boolean specifying whether the first cycle should be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveLast=`True`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveLast "Permalink to this definition")
            :   A Boolean specifying whether the last cycle should be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. The default value is True.

            saveEvery=`None`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.setValues.saveEvery "Permalink to this definition")
            :   An Int specifying every nth cycle iterations to be saved when **dataSaveFrequency** is
                OPT\_DATASAVE\_SPECIFY\_CYCLE. Abaqus saves file iterations for every nth iteration after
                iteration 1; if you set **saveEvery** = 3, Abaqus saves file iterations for cycles 1, 4, 7,
                and so on. The default value is None.

    submit(*[validate](#abaqus.Job.OptimizationProcess.OptimizationProcess.submit.validate "abaqus.Job.OptimizationProcess.OptimizationProcess.submit.validate (Python parameter) — A Boolean specifying whether Abaqus should perform the validation of the optimization process only.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L170-L180)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.submit "Permalink to this definition")
    :   This method submits an optimization process.

        Note

        Check [OptimizationProcess.submit on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?contextscope=all#simaker-optimizationprocesssubmitpyc).

        Parameters:[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.submit-parameters "Permalink to this headline")
        :   validate=`False`[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.submit.validate "Permalink to this definition")
            :   A Boolean specifying whether Abaqus should perform the validation of the optimization
                process only. The default value is False.

    task : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.task "Permalink to this definition")
    :   A String specifying name of the optimization task to be used for the optimization
        process.

    waitForCompletion()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L182-L189)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.waitForCompletion "Permalink to this definition")
    :   This method interrupts the execution of the script until the end of all the analyses.

        If you call the waitForCompletion method and the **status** member is neither SUBMITTED nor RUNNING,
        Abaqus assumes the analysis has either completed or aborted and returns immediately.

    writeParAndInputFiles()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/OptimizationProcess.py#L165-L168)[¶](#abaqus.Job.OptimizationProcess.OptimizationProcess.writeParAndInputFiles "Permalink to this definition")
    :   This method allows you to write par and input files for an optimization task.

*class* JobSession[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobSession.py#L13-L89)[¶](#abaqus.Job.JobSession.JobSession "Permalink to this definition")
:   Bases: [`SessionBase`](../session/index.html#abaqus.Session.SessionBase.SessionBase "abaqus.Session.SessionBase.SessionBase (Python class) — Bases: object")

    Member Details:

    Queue(*[name](#abaqus.Job.JobSession.JobSession.Queue.name "abaqus.Job.JobSession.JobSession.Queue.name (Python parameter) — A String specifying the name of the new Queue object.")*, *[queueName](#abaqus.Job.JobSession.JobSession.Queue.queueName "abaqus.Job.JobSession.JobSession.Queue.queueName (Python parameter) — A String specifying the name of the remote analysis queue.")*, *[hostName](#abaqus.Job.JobSession.JobSession.Queue.hostName "abaqus.Job.JobSession.JobSession.Queue.hostName (Python parameter) — A String specifying the name of the remote host.")=`''`*, *[fileCopy](#abaqus.Job.JobSession.JobSession.Queue.fileCopy "abaqus.Job.JobSession.JobSession.Queue.fileCopy (Python parameter) — A Boolean specifying if the results files are to be copied from the remote machine to the local machine.")=`1`*, *[directory](#abaqus.Job.JobSession.JobSession.Queue.directory "abaqus.Job.JobSession.JobSession.Queue.directory (Python parameter) — A String specifying the remote location for the execution of the simulation.")=`''`*, *[driver](#abaqus.Job.JobSession.JobSession.Queue.driver "abaqus.Job.JobSession.JobSession.Queue.driver (Python parameter) — A String specifying the designation of the remote driver.")=`''`*, *[remotePlatform](#abaqus.Job.JobSession.JobSession.Queue.remotePlatform "abaqus.Job.JobSession.JobSession.Queue.remotePlatform (Python parameter) — A SymbolicConstant specifying the type of operating system on the remote machine.")=`abaqusConstants.LINUX`*, *[filesToCopy](#abaqus.Job.JobSession.JobSession.Queue.filesToCopy "abaqus.Job.JobSession.JobSession.Queue.filesToCopy (Python parameter) — A list of Strings specifying the files to be copied from the remote location to the local machine, or ALL.")=`abaqusConstants.ALL`*, *[deleteAfterCopy](#abaqus.Job.JobSession.JobSession.Queue.deleteAfterCopy "abaqus.Job.JobSession.JobSession.Queue.deleteAfterCopy (Python parameter) — A Boolean specifying whether remote files are to be deleted after they are copied to the local machine.")=`0`*, *[description](#abaqus.Job.JobSession.JobSession.Queue.description "abaqus.Job.JobSession.JobSession.Queue.description (Python parameter) — A String specifying a description of the queue.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/JobSession.py#L15-L89)[¶](#abaqus.Job.JobSession.JobSession.Queue "Permalink to this definition")
    :   This method creates a Queue object. Note:Remote queues are available only on Linux platforms.

        Note

        This function can be accessed by:

        ```python
        session.Queue
        ```

        Note

        Check [Queue on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-queuepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Job.JobSession.JobSession.Queue-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Job.JobSession.JobSession.Queue.name "Permalink to this definition")
            :   A String specifying the name of the new Queue object.

            queueName[¶](#abaqus.Job.JobSession.JobSession.Queue.queueName "Permalink to this definition")
            :   A String specifying the name of the remote analysis queue.

            hostName=`''`[¶](#abaqus.Job.JobSession.JobSession.Queue.hostName "Permalink to this definition")
            :   A String specifying the name of the remote host. The default value is an empty string.

            fileCopy=`1`[¶](#abaqus.Job.JobSession.JobSession.Queue.fileCopy "Permalink to this definition")
            :   A Boolean specifying if the results files are to be copied from the remote machine to
                the local machine. The default value is ON.

            directory=`''`[¶](#abaqus.Job.JobSession.JobSession.Queue.directory "Permalink to this definition")
            :   A String specifying the remote location for the execution of the simulation. The default
                value is an empty string.

            driver=`''`[¶](#abaqus.Job.JobSession.JobSession.Queue.driver "Permalink to this definition")
            :   A String specifying the designation of the remote driver. The default value is “abaqus”.

            remotePlatform=`abaqusConstants.LINUX`[¶](#abaqus.Job.JobSession.JobSession.Queue.remotePlatform "Permalink to this definition")
            :   A SymbolicConstant specifying the type of operating system on the remote machine. The
                default value is Linux.

            filesToCopy=`abaqusConstants.ALL`[¶](#abaqus.Job.JobSession.JobSession.Queue.filesToCopy "Permalink to this definition")
            :   A list of Strings specifying the files to be copied from the remote location to the
                local machine, or ALL. Strings specified in a list are the extensions of the job files
                that will be copied, such as (‘log’, ‘dat’, ‘msg’, ‘sta’, ‘odb’). The default value is
                ALL.

            deleteAfterCopy=`0`[¶](#abaqus.Job.JobSession.JobSession.Queue.deleteAfterCopy "Permalink to this definition")
            :   A Boolean specifying whether remote files are to be deleted after they are copied to the
                local machine. The default value is OFF.

            description=`''`[¶](#abaqus.Job.JobSession.JobSession.Queue.description "Permalink to this definition")
            :   A String specifying a description of the queue. The default value is an empty string.

        Returns:[¶](#abaqus.Job.JobSession.JobSession.Queue-returns "Permalink to this headline")
        :   A Queue object.

        Return type:[¶](#abaqus.Job.JobSession.JobSession.Queue-return-type "Permalink to this headline")
        :   [`Queue`](#abaqus.Job.JobSession.JobSession.Queue "abaqus.Job.JobSession.JobSession.Queue (Python method) — This method creates a Queue object. Note:Remote queues are available only on Linux platforms.")

        Raises:[¶](#abaqus.Job.JobSession.JobSession.Queue-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – Remote queue host name is not set, If **fileCopy** = ON and **hostName** is empty.
            Directory in which to run the job on the remote computer is not set, If **fileCopy** = ON and **directory** is empty.

*class* Queue(*[name](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.name (Python parameter)")*, *[queueName](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.queueName (Python parameter)")*, *[hostName](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.hostName (Python parameter)")=`''`*, *[fileCopy](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.fileCopy (Python parameter)")=`1`*, *[directory](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.directory (Python parameter)")=`''`*, *[driver](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.driver (Python parameter)")=`''`*, *[remotePlatform](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.remotePlatform (Python parameter)")=`abaqusConstants.LINUX`*, *[filesToCopy](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.filesToCopy (Python parameter)")=`abaqusConstants.ALL`*, *[deleteAfterCopy](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.deleteAfterCopy (Python parameter)")=`0`*, *[description](#abaqus.Job.Queue.Queue "abaqus.Job.Queue.Queue.__init__.description (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L15-L129)[¶](#abaqus.Job.Queue.Queue "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A Queue object tells the job where and how to submit a job remotely. A Queue object can be used as the
    **queue** argument to the Job method.

    Note

    This object can be accessed by:

    ```python
    import job
    session.queues[name]
    ```

    Note

    Check [Queue on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-queuepyc.htm?contextscope=all).

    Member Details:

    deleteAfterCopy : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L57-L59)[¶](#abaqus.Job.Queue.Queue.deleteAfterCopy "Permalink to this definition")
    :   A Boolean specifying whether remote files are to be deleted after they are copied to the
        local machine. The default value is OFF.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L61-L62)[¶](#abaqus.Job.Queue.Queue.description "Permalink to this definition")
    :   A String specifying a description of the queue. The default value is an empty string.

    directory : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L40-L42)[¶](#abaqus.Job.Queue.Queue.directory "Permalink to this definition")
    :   A String specifying the remote location for the execution of the simulation. The default
        value is an empty string.

    driver : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L44-L45)[¶](#abaqus.Job.Queue.Queue.driver "Permalink to this definition")
    :   A String specifying the designation of the remote driver. The default value is “abaqus”.

    fileCopy : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L36-L38)[¶](#abaqus.Job.Queue.Queue.fileCopy "Permalink to this definition")
    :   A Boolean specifying if the results files are to be copied from the remote machine to
        the local machine. The default value is ON.

    filesToCopy : --is-rst--:py:class:`str` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L51-L55)[¶](#abaqus.Job.Queue.Queue.filesToCopy "Permalink to this definition")
    :   A list of Strings specifying the files to be copied from the remote location to the
        local machine, or ALL. Strings specified in a list are the extensions of the job files
        that will be copied, such as (‘log’, ‘dat’, ‘msg’, ‘sta’, ‘odb’). The default value is
        ALL.

    hostName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L33-L34)[¶](#abaqus.Job.Queue.Queue.hostName "Permalink to this definition")
    :   A String specifying the name of the remote host. The default value is an empty string.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py)[¶](#abaqus.Job.Queue.Queue.name "Permalink to this definition")
    :   A String specifying the name of the new Queue object.

    queueName : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py)[¶](#abaqus.Job.Queue.Queue.queueName "Permalink to this definition")
    :   A String specifying the name of the remote analysis queue.

    remotePlatform : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'LINUX'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/Queue.py#L47-L49)[¶](#abaqus.Job.Queue.Queue.remotePlatform "Permalink to this definition")
    :   A SymbolicConstant specifying the type of operating system on the remote machine. The
        default value is Linux.

*class* Message[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/MessageArray.py#L8-L51)[¶](#abaqus.Job.MessageArray.Message "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Message object contains information about a given phase of the simulation. Job messages are not
    returned if a script is run without the Abaqus/CAE GUI (using the noGUI option).

    Note

    This object can be accessed by:

    ```python
    import job
    mdb.coexecutions[name].jobs[name].messages[i]
    mdb.jobs[name].messages[i]
    ```

    Note

    Check [Message on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-messagepyc.htm?contextscope=all).

    Member Details:

    data : --is-rst--:py:data:`~typing.Optional`\[:py:class:`dict`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/MessageArray.py#L8-L51)[¶](#abaqus.Job.MessageArray.Message.data "Permalink to this definition")
    :   A Dictionary object specifying the data returned by the analysis product. The value
        depends on the message returned. For a list of the possible entries, see the members of
        DataObject.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Job/MessageArray.py)[¶](#abaqus.Job.MessageArray.Message.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of message. Possible values are:

        * ABORTED
        * ANY\_JOB
        * ANY\_MESSAGE\_TYPE
        * COMPLETED
        * END\_STEP
        * ERROR
        * HEADING
        * HEALER\_JOB
        * HEALER\_TYPE
        * INTERRUPTED
        * ITERATION
        * JOB\_ABORTED
        * JOB\_COMPLETED
        * JOB\_INTERRUPTED
        * JOB\_SUBMITTED
        * MONITOR\_DATA
        * ODB\_FILE
        * ODB\_FRAME
        * STARTED
        * STATE\_FRAME
        * STATUS
        * STEP
        * WARNING

[Back to top](#)