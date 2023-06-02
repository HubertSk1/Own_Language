grammar MY_LANG;

prog: statements EOF ;

statements: statement* ;

statement: (print | assign | read| scale | matrix_add) EOE ;

assign: (ID|matrix_elem) SET expr ;

print : PRINT LEFT_P expr RIGHT_P ;

read : READ LEFT_P ID RIGHT_P;

matrix_add : M_ADD LEFT_P ID COMA ID RIGHT_P;

matrix_elem : ID '['INT COMA INT']' ;

expr: expr MUL expr 
    | expr DIV expr 
    | expr ADD expr 
    | expr SUB expr 
    | INT 
    | REAL 
    | ID 
    | LEFT_P expr RIGHT_P
    | matrix
    | matrix_elem;

row:'[' INT (',' INT)* ']';

matrix: '[' row (',' row)* ']';

scale: SCALE LEFT_P ID COMA INT RIGHT_P;

M_ADD : 'ADD';
SCALE : 'SCALE';
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
COMA: ',' ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
LEFT_P : '(' ;
RIGHT_P : ')' ;
WS : [ \r\n\t]+ -> skip ;