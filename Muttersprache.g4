grammar Muttersprache;

tokens {PRINT, READ}

program:   (NEWLINE* statment)+ ;

statment: (assign | print | read) EOE ;

assign: ID SET value ;

print : PRINT LEFT_P value RIGHT_P ;

read : READ ;

value: INT | REAL | ID ;

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
NEWLINE: '\r\n' ;