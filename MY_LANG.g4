grammar MY_LANG;

prog: statements EOF ;

statements: (statement|define|struct)* ;

statement: (print | assign | read | call_function |conditional_stat |loop ) EOE ;

assign: ID SET expr ;

print : PRINT LEFT_P expr RIGHT_P ;

read : READ LEFT_P ID RIGHT_P;

arg_list : typ ID (COMA typ ID)*;

function_header : DEF ID LEFT_P  arg_list RIGHT_P;

define : function_header BEGIN statement* end_function;
end_function : RETURN ID;

call_function: CALL ID LEFT_P expr? (COMA expr)* RIGHT_P ;

loop : loop_header statement* loop_end;

loop_header : REPEAT expr BEGIN;

loop_end : END;

struct: STRUCT ID LEFT_P arg_list RIGHT_P; 

conditional_stat:conditional_header  statement* else_part statement* END;

conditional_header: IF bool_stat DO;

else_part: ELSE DO;

bool_stat:  expr GREATER expr|
            expr LOWER expr|
            expr EQUAL expr ;


typ: INT_TYPE | REAL_TYPE;

expr: expr MUL expr 
    | expr DIV expr 
    | expr ADD expr 
    | expr SUB expr 
    | INT 
    | REAL 
    | ID 
    | LEFT_P expr RIGHT_P
    | call_function;


STRUCT: 'STRUCT';
IF: 'IF';
DO: 'DO';
ELSE : 'ELSE';
REPEAT: 'REPEAT';
CALL : 'CALL';
INT_TYPE : 'INT' ;
REAL_TYPE : 'REAL';
END: 'END';
DEF : 'DEFINE';
BEGIN : 'BEGIN';
RETURN : 'RETURN';
PRINT : 'PRINT';
READ : 'READ';
INT : '-'?[0-9]+ ;
REAL : '-'?[0-9]+'.'[0-9]* ;
GREATER : '>';
LOWER : '<';
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EQUAL: '==';
SET : '=' ;
EOE : ';' ;
COMA: ',' ;
ID : [a-zA-Z][a-zA-Z0-9_]* ;
LEFT_P : '(' ;
RIGHT_P : ')' ;
WS : [ \r\n\t]+ -> skip ;