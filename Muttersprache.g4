grammar Muttersprache;

prog: statments  EOF ;

statments: statment* ; 

statment: (print |assign  | read) EOE ;

assign: ID SET value ;

print : PRINT LEFT_P value RIGHT_P ;

read : READ  LEFT_P ID RIGHT_P;

value: INT | REAL | ID ;

PRINT : 'PRINT';
READ : 'READ';
INT :   [0-9]+ ;
REAL : [0-9]+'.'[0-9]* ;
MUL :   [ ]*'*'[ ]* ;
DIV :   [ ]*'/'[ ]* ;
ADD :   [ ]*'+'[ ]* ;
SUB :   [ ]*'-'[ ]* ;
SET :   [ ]*'='[ ]* ;
COMA :  [ ]*','[ ]* ;
EOE :   [ ]*';'[ ]* ;
ID  :   [a-zA-Z0-9]+[ ]* ;
LEFT_P : [ ]*'('[ ]* ;
RIGHT_P : [ ]*')'[ ]* ;
NEWLINE: '\r\n' -> skip;