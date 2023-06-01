grammar GDV_Grammar;

// Regla inicial de la gramática
parse
 : from_input | from_file
 ;

// Regla para pasar por consola
from_input
 : stat
 ;

// Regla para pasar por archivo
from_file
 : (stat)* EOF
 ;

// Las sentencias
stat
 : simple_stat
 | compound_stat
 ;

// Una senetnecia compuesta
compound_stat
 : if_stat
 | while_stat
 | for_stat
 | funcion
 ;

// Una senetnecia simple
simple_stat
 : assignment SEMICOLON
 | importar SEMICOLON
 | retornar SEMICOLON
 | atom SEMICOLON
 | expr SEMICOLON
 | OTHER
 ;

// Una asignación
assignment
 : (variable|accessarray) ASSIGN (expr) 
 ;

// Una senetnecia if
if_stat
 : IF condition_block (ELSE IF condition_block)* (ELSE stat_block)?
 ;

// Una senetnecia while
while_stat
 : WHILE expr stat_block
 ;

// Una senetnecia for
for_stat
 : FOR OPAR (simple_stat)
 (simple_stat) (expr | assignment | retornar | importar | atom | OTHER)
 CPAR stat_block
 ;

// Una declaración de función
funcion
 : FUNCION ID OPAR (parametro (COMMA parametro)*)? CPAR OBRACE (stat)* CBRACE
 ;

// Una senetnecia de importar
importar
 : IMPORT ID (POINT ID)* 
 | FROM ID IMPORT ID 
 ;

// Una senetnecia de retornar
retornar
 : RETORNO ((OPAR expr CPAR) | expr) 
 ;

// Un bloque condicional (la condición y el código a ejecutar si se cumple la condición)
condition_block
 : expr stat_block
 ;

// Bloque de código a ejecutar si se cumple la condición
stat_block
 : OBRACE (stat)* CBRACE
 ;

// Vectores (o arreglos) 
array
 : OKEY (expr (COMMA expr)*)? CKEY
 ;

// Acceso a arreglos o JSON
accessarray
 : variable OKEY ((expr (POINTS (expr)?)?) | POINTS)
 (COMMA ((expr (POINTS (expr)?)?) | POINTS))* CKEY
 ;

// Una variable
variable
 : ID ((POINT ID) | (POINT ID OPAR
 (expr (COMMA expr)*)?
 CPAR))*
 ;

// Parametro de una función
parametro
 : ID (ASSIGN expr)?
 ;

// Expresiones (por ejemplo 2+2)
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

// Llamada a la función
funccall
 : ID OPAR
 (expr (COMMA expr)*)?
 CPAR
 ;

// enteros, flotantes, booleanos, llamada a funciones, strings, vectores, objeto(JSON), acceso a vector, variables y null
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

// JSON
objeto
 : OBRACE (keyvalue (COMMA keyvalue)*)? CBRACE
 ;

// Clave valor, lo que va dentro del JSON
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
