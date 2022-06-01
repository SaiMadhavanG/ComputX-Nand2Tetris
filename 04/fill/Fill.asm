// Project for computX by Sai Madhavan G IMT2021101
// Program begins here
(BEGIN)

// First, we initialise the required variables and check if a key is pressed or not
@count
M=0
@8192
D=A
@max
M=D
@24576
D=M
@EMPTYLOOP
D;JEQ
@FILLOOP
0;JEQ

// If a key is pressed, we enter this block which fills the screen by
// seting the values of all the words present in the screen as -1
(FILLOOP)
@count
D=M
@max
D=M-D
@BEGIN
D;JEQ
@SCREEN
D=A
@count
A=M+D
M=-1
@count
M=M+1
@FILLOOP
0;JMP

// If a key is not pressed, we enter this block which emptys the screen by
// seting the values of all the words present in the screen as 0
(EMPTYLOOP)
@count
D=M
@max
D=M-D
@BEGIN
D;JEQ
@SCREEN
D=A
@count
A=M+D
M=0
@count
M=M+1
@EMPTYLOOP
0;JMP