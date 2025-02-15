2.7 - Forward declarations and definitions 

// Cannot define a function after main(), it will result in a compile error.
// 2 options: 
  // 1. Reorder the function definitions 
  // 2. Use a forward declaration 

// 1. Reorder the function definition 
  // Move the function before main()
// 2. Use a forward declaration 
  // It allows us to tell the compiler about the existence of an identifier before actually defining the identifier. 
  // To write a forward declaration for a function, we use a function declaration statement (aka function prototype).
  // It consists of the function's return type, name, and parameter types, terminated with a semicolon. 
  // Function body not included.
  int add (int x, int y); // function declaration includes return type, namee, parameters, and semicolon. No function body!


////////// Declarations vs. definitions //////////
// A declaration tells the compiler about the existence of an identifier and its associatedd type informtaion. 
// A definition is a declaration that actually implements (for functions and types) or instantiates (for variables) the identifier.

// All definitions are declarations, BUT not all declarations are definitions.
// Pure declarations: Declarations that aren't definitions.


///// SUMMARY ///// 
/* 
Declaration: Tells compiler about an identifier and its associated type information.
Definition: Implements a function or instantiates a variable. Definitions are also declarations. 
Pure declaration: A declaration that isn't a definition.
Initialization: Provides an initial value for a defined object.
*/
