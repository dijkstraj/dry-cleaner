grammar Code;

code: token+;

token: IDENTIFIER | STRING | NUMBER;

KEYWORD: ('import' | 'from' | 'as' | 'if' | 'else' | 'for' | 'while' | 'class' | 'type' | 'typeof' | 'this' | 'function') -> skip;

LINE_COMMENT: '//' ~[\r\n]+ -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

IDENTIFIER: '@'? [a-zA-Z_$][a-zA-Z0-9_$]*;

BRACKET: [{}()[\]] -> skip;

NUMBER: ('.' [0-9]+) | ([0-9]+ ('.' [0-9]+)?);

OPERATOR: ('+' | '.' | '*' | '/' | '-' | '||' | '&&' | '|' | ';' | ':' | ',' | '=' | '!' | '>' | '<') -> skip;

STRING: '\'\'' | '\'' ~[']+ '\'' | '`' ~[`]+ '`';

QUESTIONMARK: '?' -> skip;

WS: [ \t\r\n]+ -> skip;
