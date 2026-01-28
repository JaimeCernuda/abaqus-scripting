1

   Abaqus Learning Edition 2025                                  Date 27-Jan-2026   Time 10:19:34
   

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                0.100    
          AND A TOTAL TIME PERIOD OF                            1.00    
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-08
          THE MAXIMUM TIME INCREMENT ALLOWED IS                 1.00    

     LINEAR EQUATION SOLVER TYPE         DIRECT SPARSE

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

 CONVERGENCE TOLERANCE PARAMETERS FOR MOMENT   
     CRITERION FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR ROTATION CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE MOMENT                              1.000E-02
     AVERAGE MOMENT    IS TIME AVERAGE MOMENT   
     ALTERNATE CRIT. FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO MOMENT    RELATIVE TO TIME AVRG. MOMENT        1.000E-05
     CRITERION FOR RESIDUAL MOMENT    WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR ROTATION CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL MOMENT    FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO MOMENT    REL. TO TIME AVRG. MAX. MOMENT       1.000E-05

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 TIME INCREMENTATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AT WHICH LOG. CONVERGENCE RATE CHECK BEGINS         8
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     EQUILIBRIUM ITERATION COUNT FOR CUT-BACK IN NEXT INCREMENT               10
     MAXIMUM EQUILIB. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      4
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            50
     MAXIMUM ATTEMPTS ALLOWED IN AN INCREMENT                                  5
     MAXIMUM DISCON. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      50
     MAXIMUM CONTACT AUGMENTATIONS FOR *SURFACE BEHAVIOR,AUGMENTED LAGRANGE   50
     CUT-BACK FACTOR AFTER DIVERGENCE                                 0.2500    
     CUT-BACK FACTOR FOR TOO SLOW CONVERGENCE                         0.5000    
     CUT-BACK FACTOR AFTER TOO MANY EQUILIBRIUM ITERATIONS            0.7500    
     CUT-BACK FACTOR AFTER TOO MANY SEVERE DISCONTINUITY ITERATIONS   0.2500    
     CUT-BACK FACTOR AFTER PROBLEMS IN ELEMENT ASSEMBLY               0.2500    
     INCREASE FACTOR AFTER TWO INCREMENTS THAT CONVERGE QUICKLY        1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED                       1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DYNAMICS)            1.250    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DIFFUSION)           2.000    
     MINIMUM TIME INCREMENT RATIO FOR EXTRAPOLATION TO OCCUR          0.1000    
     MAX. RATIO OF TIME INCREMENT TO STABILITY LIMIT                   1.000    
     FRACTION OF STABILITY LIMIT FOR NEW TIME INCREMENT               0.9500    
     TIME INCREMENT INCREASE FACTOR BEFORE A TIME POINT                1.000    
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                    100

          LARGE DISPLACEMENT THEORY WILL BE USED

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH      8.62    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  9ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       5.68       TIME AVG. FORCE        5.68    
 LARGEST SCALED RESIDUAL FORCE       1.16       AT NODE        482   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       1.16    
 LARGEST INCREMENT OF DISP.         9.727E-03   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        9.727E-03   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       49.0    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -1.473E-03   AT NODE          1   DOF  5
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -3.093E-02
 LARGEST INCREMENT OF ROTATION     -6.511E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -6.511E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  14ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       5.68       TIME AVG. FORCE        5.68    
 LARGEST SCALED RESIDUAL FORCE     -1.090E-04   AT NODE        471   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -1.090E-04
 LARGEST INCREMENT OF DISP.         9.721E-03   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        8.475E-06   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       49.0    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     9.379E-07   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     1.970E-05
 LARGEST INCREMENT OF ROTATION     -6.507E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -8.723E-09   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.100    
 STEP TIME COMPLETED       0.100    ,  TOTAL TIME COMPLETED        0.100    


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  14ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       11.4       TIME AVG. FORCE        8.55    
 LARGEST SCALED RESIDUAL FORCE      8.805E-04   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      8.805E-04
 LARGEST INCREMENT OF DISP.         9.694E-03   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -2.743E-05   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       49.0    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     4.615E-04   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     9.692E-03
 LARGEST INCREMENT OF ROTATION     -6.499E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.486E-08   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.150    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  6ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       20.0       TIME AVG. FORCE        12.4    
 LARGEST SCALED RESIDUAL FORCE      1.646E-03   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      1.646E-03
 LARGEST INCREMENT OF DISP.         1.452E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        3.455E-05   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       73.8    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     8.564E-04   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     1.798E-02
 LARGEST INCREMENT OF ROTATION     -9.733E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.842E-08   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  6ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       20.0       TIME AVG. FORCE        12.4    
 LARGEST SCALED RESIDUAL FORCE      8.301E-07   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      8.301E-07
 LARGEST INCREMENT OF DISP.         1.455E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        2.879E-05   AT NODE        192   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       73.8    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -3.933E-08   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -8.260E-07
 LARGEST INCREMENT OF ROTATION     -9.733E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.343E-10   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.150    ,  FRACTION OF STEP COMPLETED  0.350    
 STEP TIME COMPLETED       0.350    ,  TOTAL TIME COMPLETED        0.350    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.225    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  10ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       32.7       TIME AVG. FORCE        17.5    
 LARGEST SCALED RESIDUAL FORCE      3.691E-03   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      3.691E-03
 LARGEST INCREMENT OF DISP.         2.172E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.014E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       107.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.902E-03   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     3.994E-02
 LARGEST INCREMENT OF ROTATION     -1.457E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -6.342E-08   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  7ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       32.7       TIME AVG. FORCE        17.5    
 LARGEST SCALED RESIDUAL FORCE      4.349E-06   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      4.349E-06
 LARGEST INCREMENT OF DISP.         2.176E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        4.009E-05   AT NODE        192   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       107.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -9.379E-08   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -1.970E-06
 LARGEST INCREMENT OF ROTATION     -1.457E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     4.511E-10   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.225    ,  FRACTION OF STEP COMPLETED  0.575    
 STEP TIME COMPLETED       0.575    ,  TOTAL TIME COMPLETED        0.575    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.338    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  14ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       51.9       TIME AVG. FORCE        24.3    
 LARGEST SCALED RESIDUAL FORCE      8.261E-03   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      8.261E-03
 LARGEST INCREMENT OF DISP.         3.263E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        2.619E-04   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       151.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     4.195E-03   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     8.809E-02
 LARGEST INCREMENT OF ROTATION     -2.177E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.397E-07   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  12ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       51.9       TIME AVG. FORCE        24.3    
 LARGEST SCALED RESIDUAL FORCE      2.236E-05   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      2.236E-05
 LARGEST INCREMENT OF DISP.         3.248E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.470E-04   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       151.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -5.061E-07   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -1.063E-05
 LARGEST INCREMENT OF ROTATION     -2.177E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.490E-09   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.338    ,  FRACTION OF STEP COMPLETED  0.913    
 STEP TIME COMPLETED       0.913    ,  TOTAL TIME COMPLETED        0.913    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  8.750E-02
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  6ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       56.9       TIME AVG. FORCE        29.8    
 LARGEST SCALED RESIDUAL FORCE      1.605E-03   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      1.605E-03
 LARGEST INCREMENT OF DISP.         8.295E-03   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.267E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION   -5.128E-08
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       210.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     7.963E-04   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     1.672E-02
 LARGEST INCREMENT OF ROTATION     -5.630E-06   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.306E-08   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  8.750E-02,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          6  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      10  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      10  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      10  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      10  WARNING MESSAGES DURING ANALYSIS
                      10  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =      1.1    
       SYSTEM TIME (SEC)    =     0.10    
       TOTAL CPU TIME (SEC) =      1.2    
       WALLCLOCK TIME (SEC) =            2
       MEMORY PEAK (GB)     =            0
