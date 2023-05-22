grammar GDV_Grammar;

parse
 : from_input | from_file
 ;

from_input
 : stat
 ;

from_file
 : (stat)* EOF
 ;

stat
 : simple_stat
 | compound_stat
 ;

compound_stat
 : if_stat
 | while_stat
 | for_stat
 | funcion
 ;

simple_stat
 : assignment SEMICOLON
 | importar SEMICOLON
 | retornar SEMICOLON
 | atom SEMICOLON
 | expr SEMICOLON
 | OTHER
 ;

assignment
 : (variable|accessarray) ASSIGN (expr) 
 ;

if_stat
 : IF condition_block (ELSE IF condition_block)* (ELSE stat_block)?
 ;

while_stat
 : WHILE expr stat_block
 ;

for_stat
 : FOR OPAR (simple_stat)
 (simple_stat) (expr | assignment | retornar | importar | atom | OTHER)
 CPAR stat_block
 ;

funcion
 : FUNCION ID OPAR (parametro (COMMA parametro)*)? CPAR OBRACE (stat)* CBRACE
 ;

importar
 : IMPORT ID (POINT ID)* 
 | FROM ID IMPORT ID 
 ;

retornar
 : RETORNO ((OPAR expr CPAR) | expr) 
 ;

condition_block
 : expr stat_block
 ;

stat_block
 : OBRACE (stat)* CBRACE
 ;

array
 : OKEY (expr (COMMA expr)*)? CKEY
 ;

accessarray
 : variable OKEY ((expr (POINTS (expr)?)?) | POINTS)
 (COMMA ((expr (POINTS (expr)?)?) | POINTS))* CKEY
 ;

variable
 : ID ((POINT ID) | (POINT ID OPAR
 (expr (COMMA expr)*)?
 CPAR))*
 ;

parametro
 : ID (ASSIGN expr)?
 ;

expr
 : left=expr POW right=expr                     #powExpr
 | MINUS expr                                   #unaryMinusExpr
 | NOT expr                                     #notExpr
 | left=expr op=(MULT|DIV|MOD) right=expr       #multiplicationExpr
 | left=expr op=(PLUS|MINUS) right=expr         #additiveExpr
 | left=expr op=(LTEQ|GTEQ|LT|GT) right=expr    #relationalExpr
 | left=expr op=(EQ|NEQ) right=expr             #equalityExpr
 | left=expr AND right=expr                     #andExpr
 | left=expr OR right=expr                      #orExpr
 | OPAR expr CPAR 						        #parExpr
 | atom                                         #atomExpr
 ;

funccall
 : ID OPAR
 (expr (COMMA expr)*)?
 CPAR
 ;

atom
 : (INT|FLOAT)  #numberAtom
 | (TRUE|FALSE) #booleanAtom
 | funccall     #funccallAtom
 | STRING       #stringAtom
 | array		#arrayAtom
 | objeto		#objetoAtom
 | accessarray  #accessToarray
 | variable		#accessVariable
 | NIL          #nilAtom
 ;


objeto
 : OBRACE (keyvalue (COMMA keyvalue)*)? CBRACE
 ;

keyvalue
 : variable POINTS expr
 ;

OR : 'or';
AND : 'and';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
POW : '^';
NOT : 'not';

ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';
OKEY : '[';
CKEY : ']';
COMMA : ',';
POINTS: ':';
SEMICOLON : ';' ;

TRUE : 'true';
FALSE : 'false';
NIL : 'null';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
FUNCION: 'function';
RETORNO: 'return';
IMPORT: 'import';
FROM: 'from';
POINT: '.';

ID
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

INT
 : [0-9]+
 ;

FLOAT
 : [0-9]+ '.' [0-9]*
 | '.' [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 | '\'' (~["\r\n] | '""')* '\''
 ;

COMMENT
 : '//' ~[\r\n]* -> skip
 ;

SPACE
 : [ \t\r] -> skip
 ;

NEWLINE
 : [\n] -> skip
 ;

OTHER
 : .
 ;