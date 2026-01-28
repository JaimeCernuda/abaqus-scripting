1

   Abaqus Learning Edition 2025                                  Date 27-Jan-2026   Time 10:21:49
   

                                                                                 
                                                                                 
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
        SOLVER ELAPSED TIME:  8ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       17.0       TIME AVG. FORCE        17.0    
 LARGEST SCALED RESIDUAL FORCE       10.5       AT NODE        482   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       10.5    
 LARGEST INCREMENT OF DISP.         2.913E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        2.913E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       147.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -1.325E-02   AT NODE          1   DOF  5
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -0.278    
 LARGEST INCREMENT OF ROTATION     -1.953E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.953E-05   AT NODE          1   DOF  5
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
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 1.E+15     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       17.0       TIME AVG. FORCE        17.0    
 LARGEST SCALED RESIDUAL FORCE     -2.914E-03   AT NODE        471   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -2.914E-03
 LARGEST INCREMENT OF DISP.         2.802E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.110E-03   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION    3.088E-07
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       147.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     2.549E-05   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     5.353E-04
 LARGEST INCREMENT OF ROTATION     -1.950E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -7.801E-08   AT NODE          1   DOF  4
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
        SOLVER ELAPSED TIME:  6ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       34.2       TIME AVG. FORCE        25.6    
 LARGEST SCALED RESIDUAL FORCE      7.903E-03   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      7.903E-03
 LARGEST INCREMENT OF DISP.         2.740E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -6.146E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION   -2.426E-07
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       147.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     4.107E-03   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     8.624E-02
 LARGEST INCREMENT OF ROTATION     -1.942E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.318E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       34.2       TIME AVG. FORCE        25.6    
 LARGEST SCALED RESIDUAL FORCE      1.547E-05   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      1.547E-05
 LARGEST INCREMENT OF DISP.         2.758E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.803E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       147.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -3.638E-07   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -7.639E-06
 LARGEST INCREMENT OF ROTATION     -1.942E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.242E-09   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.150    
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  10ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 1.E+15     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       59.7       TIME AVG. FORCE        37.0    
 LARGEST SCALED RESIDUAL FORCE      1.469E-02   AT NODE        822   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      1.469E-02
 LARGEST INCREMENT OF DISP.         4.244E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.555E-03   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION    6.082E-07
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       221.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     7.466E-03   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.157    
 LARGEST INCREMENT OF ROTATION     -2.900E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.483E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       59.7       TIME AVG. FORCE        37.0    
 LARGEST SCALED RESIDUAL FORCE      6.610E-05   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      6.610E-05
 LARGEST INCREMENT OF DISP.         4.291E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        4.755E-04   AT NODE        192   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION    2.139E-06
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       221.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -1.567E-06   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -3.290E-05
 LARGEST INCREMENT OF ROTATION     -2.900E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     3.488E-09   AT NODE          1   DOF  4
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
        SOLVER ELAPSED TIME:  15ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       97.8       TIME AVG. FORCE        52.2    
 LARGEST SCALED RESIDUAL FORCE      4.873E-02   AT NODE        432   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      4.873E-02
 LARGEST INCREMENT OF DISP.         6.384E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        5.635E-04   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       319.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.615E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.339    
 LARGEST INCREMENT OF ROTATION     -4.320E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -5.369E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       97.8       TIME AVG. FORCE        52.2    
 LARGEST SCALED RESIDUAL FORCE      3.415E-04   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      3.415E-04
 LARGEST INCREMENT OF DISP.         6.392E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        8.890E-05   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       319.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -7.804E-06   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -1.639E-04
 LARGEST INCREMENT OF ROTATION     -4.321E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.124E-08   AT NODE          1   DOF  4
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
        SOLVER ELAPSED TIME:  6ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       155.       TIME AVG. FORCE        72.7    
 LARGEST SCALED RESIDUAL FORCE      -6.16       AT NODE        419   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      -6.16    
 LARGEST INCREMENT OF DISP.         9.594E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        2.353E-03   AT NODE        105   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       450.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     3.502E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.735    
 LARGEST INCREMENT OF ROTATION     -6.515E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     2.337E-06   AT NODE          1   DOF  6
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


 AVERAGE FORCE                       155.       TIME AVG. FORCE        72.7    
 LARGEST SCALED RESIDUAL FORCE      2.408E-02   AT NODE        420   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      2.408E-02
 LARGEST INCREMENT OF DISP.         9.553E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -4.360E-04   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       450.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.919E-04   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     4.029E-03
 LARGEST INCREMENT OF ROTATION     -6.516E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.119E-07   AT NODE          1   DOF  6
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


 AVERAGE FORCE                       169.       TIME AVG. FORCE        88.8    
 LARGEST SCALED RESIDUAL FORCE      -1.14       AT NODE        419   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      -1.14    
 LARGEST INCREMENT OF DISP.         2.472E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -5.090E-04   AT NODE        141   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       627.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     6.347E-03   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.133    
 LARGEST INCREMENT OF ROTATION     -2.003E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.294E-06   AT NODE          1   DOF  6
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
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       169.       TIME AVG. FORCE        88.8    
 LARGEST SCALED RESIDUAL FORCE      3.535E-03   AT NODE        420   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      3.535E-03
 LARGEST INCREMENT OF DISP.         2.495E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        2.340E-04   AT NODE        420   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       627.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -1.135E-05   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -2.383E-04
 LARGEST INCREMENT OF ROTATION     -2.003E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.833E-08   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  8.750E-02,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          6  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      12  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      12  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      12  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      12  WARNING MESSAGES DURING ANALYSIS
                      12  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =      1.1    
       SYSTEM TIME (SEC)    =     0.10    
       TOTAL CPU TIME (SEC) =      1.2    
       WALLCLOCK TIME (SEC) =            1
       MEMORY PEAK (GB)     =            0
