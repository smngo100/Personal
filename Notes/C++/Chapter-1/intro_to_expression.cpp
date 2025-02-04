1.10 - Introduction to Expressions

////////// Expressions //////////
// An expression is a non-empty sequence of literals, variabels, operators, and function calls that calculates a value. 
// The process of executing an expresson is called evaluation. 
// The result value produced is called the result of the expression (also sometimes called the return value).
// Expression do not end in a semicolon, and cannot be compiled by themselves.
  // Rather, they are always evaluated as part of statements.
  // int x{2 + 3}; 
  // 2 + 3 is an expression that has no semicolon -- the semicolon is at the end of the statement containing the expression 
// Syntax:    type identifier{expression}


////////// Expression Statements //////////
// An expression statement is a statement that consists of an expression followed by a semicolon. 
// When the expression statement is executed, the expression will be evaluated.


////////// Subexpression, Full Expressions, and Compound Expressions //////////
// Subexpression: An expression used as an operand. 
  // The subexpressions of x = 4 + 5 are x and 4 + 5. The subexpressions of 4 + 5 are 4 and 5.
// Full expression: An expression that is not a subexpression.
// Compound expression: An expression that contains two or more uses of operations.

NOTE
// The syntax <type> <name> = <expression> is not an expression
// The syntax <expression> <operator> <expression> is an expression
