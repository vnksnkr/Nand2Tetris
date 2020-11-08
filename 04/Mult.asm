@R0
D=M
@m
M=D //m=RAM[0]
@R1
D=M
@n
M=D //n=RAM[1]
@i
M=1
@R2
M=0
(LOOP)
@i
D=M
@n
D=D-M
@END
D;JGT//checks if i<n
@m
D=M
@R2
M=M+D//RAM[2]+RAM[0]
@i
M=M+1//i++
@LOOP
0;JMP
(END)
@END
0;JMP
