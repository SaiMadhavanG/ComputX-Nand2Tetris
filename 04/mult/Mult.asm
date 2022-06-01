// ComputX project by Sai Madhavan G IMT2021101

// Program begins here
    @R1
    D=M
    @R2
    M=0
    @b // Assigning value of R1 to b as b will be counter variable
    M=D
(LOOP) // Running a loop which adds value of R1 to R2 b number of times
    @ENDLOOP
    D;JEQ
    @R0
    D=M
    @R2
    M=M+D
    @b
    MD=M-1
    @LOOP
    0;JMP
(ENDLOOP)
@ENDLOOP
0;JMP