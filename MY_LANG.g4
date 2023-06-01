grammar MY_LANG;

prog: statements EOF ;

statements: statement* ;

statement: (print | assign | read) EOE ;

assign: ID SET expr ;

print : PRINT LEFT_P expr RIGHT_P ;

read : READ LEFT_P ID RIGHT_P;

expr: expr MUL expr 
    | expr DIV expr 
    | expr ADD expr 
    | expr SUB expr 
    | INT 
    | REAL 
    | ID 
    | LEFT_P expr RIGHT_P
    | matrix;

matrix: '[' row (',' row)* ']';

row:'[' INT (',' INT)* ']';

PRINT : 'PRINT';
READ : 'READ';
INT : [0-9]+ ;
REAL : [0-9]+'.'[0-9]* ;
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
SET : '=' ;
EOE : ';' ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
LEFT_P : '(' ;
RIGHT_P : ')' ;
WS : [ \r\n\t]+ -> skip ;