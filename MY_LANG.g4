grammar MY_LANG;

prog: statements EOF ;

statements: define* statement* ;

statement: (print | assign | read ) EOE ;

assign: ID SET expr ;

print : PRINT LEFT_P expr RIGHT_P ;

read : READ LEFT_P ID RIGHT_P;

arg_list : ID (COMA ID)*;

function_header : DEF typ ID LEFT_P  arg_list RIGHT_P;

define : function_header BEGIN statement* END;


expr: expr MUL expr 
    | expr DIV expr 
    | expr ADD expr 
    | expr SUB expr 
    | INT 
    | REAL 
    | ID 
    | LEFT_P expr RIGHT_P;

typ: INT_TYPE | REAL_TYPE;

INT_TYPE : 'int' ;
REAL_TYPE : 'real';
DEF : 'DEFINE';
BEGIN : 'BEGIN';
END : 'END';
PRINT : 'PRINT';
READ : 'READ';
INT : '-'?[0-9]+ ;
REAL : '-'?[0-9]+'.'[0-9]* ;
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