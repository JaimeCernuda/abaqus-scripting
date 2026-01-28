1

   Abaqus Learning Edition 2025                                  Date 27-Jan-2026   Time 10:23:02
   

                                                                                 
                                                                                 
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


 AVERAGE FORCE                       28.4       TIME AVG. FORCE        28.4    
 LARGEST SCALED RESIDUAL FORCE       29.1       AT NODE        482   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       29.1    
 LARGEST INCREMENT OF DISP.         4.868E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        4.868E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       245.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -3.681E-02   AT NODE          1   DOF  5
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -0.773    
 LARGEST INCREMENT OF ROTATION     -3.255E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.255E-05   AT NODE          1   DOF  5
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
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       28.3       TIME AVG. FORCE        28.3    
 LARGEST SCALED RESIDUAL FORCE     -1.336E-02   AT NODE        471   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -1.336E-02
 LARGEST INCREMENT OF DISP.         4.840E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -2.844E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       244.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.172E-04   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     2.462E-03
 LARGEST INCREMENT OF ROTATION     -3.245E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.153E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       56.9       TIME AVG. FORCE        42.6    
 LARGEST SCALED RESIDUAL FORCE      2.360E-02   AT NODE        432   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      2.360E-02
 LARGEST INCREMENT OF DISP.         4.799E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -4.092E-04   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       244.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.128E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.237    
 LARGEST INCREMENT OF ROTATION     -3.225E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.606E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       56.9       TIME AVG. FORCE        42.6    
 LARGEST SCALED RESIDUAL FORCE      1.184E-04   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      1.184E-04
 LARGEST INCREMENT OF DISP.         4.806E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        6.761E-05   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       244.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -2.880E-06   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -6.048E-05
 LARGEST INCREMENT OF ROTATION     -3.226E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     5.624E-09   AT NODE          1   DOF  4
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
        SOLVER ELAPSED TIME:  13ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       99.3       TIME AVG. FORCE        61.5    
 LARGEST SCALED RESIDUAL FORCE      6.524E-02   AT NODE        432   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      6.524E-02
 LARGEST INCREMENT OF DISP.         7.195E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.221E-03   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 ESTIMATE OF DISP.    CORRECTION    7.693E-07
          FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       368.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     2.009E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.422    
 LARGEST INCREMENT OF ROTATION     -4.801E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -6.670E-07   AT NODE          1   DOF  4
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


 AVERAGE FORCE                       99.3       TIME AVG. FORCE        61.5    
 LARGEST SCALED RESIDUAL FORCE      5.010E-04   AT NODE        483   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      5.010E-04
 LARGEST INCREMENT OF DISP.         7.197E-02   AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.597E-05   AT NODE         21   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       368.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -1.209E-05   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT    -2.538E-04
 LARGEST INCREMENT OF ROTATION     -4.801E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.541E-08   AT NODE          1   DOF  4
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
        SOLVER ELAPSED TIME:  13ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       162.       TIME AVG. FORCE        86.7    
 LARGEST SCALED RESIDUAL FORCE      0.944       AT NODE        139   DOF  3
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      0.944    
 LARGEST INCREMENT OF DISP.         0.107       AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.599E-03   AT NODE        105   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       531.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     4.268E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.896    
 LARGEST INCREMENT OF ROTATION     -7.339E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.370E-06   AT NODE          1   DOF  5
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


 AVERAGE FORCE                       162.       TIME AVG. FORCE        86.7    
 LARGEST SCALED RESIDUAL FORCE     -4.754E-03   AT NODE        139   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -4.754E-03
 LARGEST INCREMENT OF DISP.         0.107       AT NODE         23   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.570E-04   AT NODE        110   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       531.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     3.570E-05   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     7.497E-04
 LARGEST INCREMENT OF ROTATION     -7.339E-05   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.350E-08   AT NODE          1   DOF  6
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
        SOLVER ELAPSED TIME:  7ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       260.       TIME AVG. FORCE        121.    
 LARGEST SCALED RESIDUAL FORCE      2.917E+03   AT NODE        482   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      2.917E+03
 LARGEST INCREMENT OF DISP.        -0.434       AT NODE          9   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -0.303       AT NODE        105   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     -2.45       AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     -51.5    
 LARGEST INCREMENT OF ROTATION     -5.663E-04   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -5.951E-04   AT NODE          1   DOF  4
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
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       263.       TIME AVG. FORCE        122.    
 LARGEST SCALED RESIDUAL FORCE      2.843E+03   AT NODE        482   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      2.843E+03
 LARGEST INCREMENT OF DISP.        -0.419       AT NODE          9   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        0.115       AT NODE        207   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     0.312       AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT      6.55    
 LARGEST INCREMENT OF ROTATION     -5.909E-04   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.758E-04   AT NODE          1   DOF  5
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

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                       262.       TIME AVG. FORCE        122.    
 LARGEST SCALED RESIDUAL FORCE     -1.051E+03   AT NODE        433   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -1.051E+03
 LARGEST INCREMENT OF DISP.        -0.438       AT NODE          9   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        9.802E-02   AT NODE         70   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -0.517       AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     -10.8    
 LARGEST INCREMENT OF ROTATION     -6.549E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     1.695E-04   AT NODE          1   DOF  6
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

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                       262.       TIME AVG. FORCE        122.    
 LARGEST SCALED RESIDUAL FORCE       80.7       AT NODE        482   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       80.7    
 LARGEST INCREMENT OF DISP.         0.373       AT NODE         35   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        0.109       AT NODE        208   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -4.799E-02   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     -1.01    
 LARGEST INCREMENT OF ROTATION     -6.581E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     2.604E-05   AT NODE          1   DOF  4
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
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     5


 AVERAGE FORCE                       262.       TIME AVG. FORCE        122.    
 LARGEST SCALED RESIDUAL FORCE      -1.16       AT NODE        407   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      -1.16    
 LARGEST INCREMENT OF DISP.         0.373       AT NODE         35   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        9.382E-04   AT NODE        206   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.035E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.217    
 LARGEST INCREMENT OF ROTATION     -6.592E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.517E-06   AT NODE          1   DOF  6
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

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     6


 AVERAGE FORCE                       262.       TIME AVG. FORCE        122.    
 LARGEST SCALED RESIDUAL FORCE      9.703E-02   AT NODE        325   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE      9.703E-02
 LARGEST INCREMENT OF DISP.         0.373       AT NODE         35   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -1.193E-03   AT NODE         87   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT       748.    
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     2.172E-04   AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     4.561E-03
 LARGEST INCREMENT OF ROTATION     -6.592E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.225E-07   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   6 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  6 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.338    ,  FRACTION OF STEP COMPLETED  0.913    
 STEP TIME COMPLETED       0.913    ,  TOTAL TIME COMPLETED        0.913    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  8.750E-02
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  14ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       290.       TIME AVG. FORCE        150.    
 LARGEST SCALED RESIDUAL FORCE     -3.753E+03   AT NODE        433   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -3.753E+03
 LARGEST INCREMENT OF DISP.        -0.811       AT NODE          9   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -0.728       AT NODE         86   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.050E+03
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     -3.44       AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     -72.3    
 LARGEST INCREMENT OF ROTATION     -5.500E-04   AT NODE          1   DOF  4
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     4.117E-04   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  8ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       287.       TIME AVG. FORCE        149.    
 LARGEST SCALED RESIDUAL FORCE       174.       AT NODE        481   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       174.    
 LARGEST INCREMENT OF DISP.        -0.827       AT NODE         96   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        1.910E-02   AT NODE         35   DOF  3
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.050E+03
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT    -0.176       AT NODE          1   DOF  4
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     -3.69    
 LARGEST INCREMENT OF ROTATION     -3.889E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     2.579E-04   AT NODE          1   DOF  4
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

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                       287.       TIME AVG. FORCE        149.    
 LARGEST SCALED RESIDUAL FORCE       7.23       AT NODE        325   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE       7.23    
 LARGEST INCREMENT OF DISP.        -0.833       AT NODE         96   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.       -5.625E-03   AT NODE         86   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.050E+03
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     1.353E-02   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     0.284    
 LARGEST INCREMENT OF ROTATION     -3.857E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -1.712E-05   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THE MOMENT    IS ZERO EVERYWHERE BUT THE MOMENT    RESIDUAL OR
          THE ROTATION CORRECTION IS NON-ZERO
 
	SYMMETRIC PURE THREAD-BASED DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  2445
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      1.697e+07
        SOLVER ELAPSED TIME:  16ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             TO_SPECIMEN-1.143 D.O.F. 1 RATIO = 10.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                       287.       TIME AVG. FORCE        149.    
 LARGEST SCALED RESIDUAL FORCE     -0.288       AT NODE        482   DOF  2
   INSTANCE: TO_SPECIMEN-1                                                                   
  CORRESPONDING RESIDUAL FORCE     -0.288    
 LARGEST INCREMENT OF DISP.        -0.833       AT NODE         96   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
 LARGEST CORRECTION TO DISP.        3.718E-04   AT NODE        481   DOF  1
   INSTANCE: TO_SPECIMEN-1                                                                   
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.050E+03
                                                (FROM FORCE     FIELD)
 LARGEST SCALED RESIDUAL MOMENT     2.666E-04   AT NODE          1   DOF  6
   INSTANCE:                                                                                 
  CORRESPONDING RESIDUAL MOMENT     5.599E-03
 LARGEST INCREMENT OF ROTATION     -3.857E-04   AT NODE          1   DOF  5
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.480E-07   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   4 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  4 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  8.750E-02,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          6  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      18  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      18  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      18  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      18  WARNING MESSAGES DURING ANALYSIS
                      18  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =      1.5    
       SYSTEM TIME (SEC)    =     0.20    
       TOTAL CPU TIME (SEC) =      1.7    
       WALLCLOCK TIME (SEC) =            2
       MEMORY PEAK (GB)     =            0
