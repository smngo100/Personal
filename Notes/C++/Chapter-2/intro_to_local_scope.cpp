2.5 - Introduction to local scope 

////////// Local variables //////////
// Local variables: Variables defined inside the body of a function. 


////////// Local variable lifetime //////////
// Local variable are destroyed in the opposite order of creation at the end of the set of curly braces in whcih it is defined.
  // for a funciton parameter, at the end of the function
// Object's lifetime is defined to be the time between its creation and destruction
// Variable creation and destruction happen during runtime, not compile time 
  // Lifetime is a runtime property

// What happens when an object is destroyed/ Destroyed object becomes invalid.

// Deallocated: Memory used by the object is freed up for reuse.


////////// Local scope (block scope) //////////
// An identifier's scope determines where the identifier can be seen and used within the source code. 
  // In scope: When an identifier can be seen and used. 
  // Out of scope: When an identifier cannot be seen and used.
// Compile-time property
// An identifier with local scope (aka block scope) is usable from the point of definition to the end of the innermost pair of... 
  // ...curly braces containing the identifier (or for function parameters, at the end of the function). 
// Ensures local variables cannot be used before point of deinition or after they're destroyed

// "Out of scope" : An identifier is out of scope anywhere it cannot be accessed within the code.
// "Going out of scope" : Typically applied to objects. Say it goes out of scope at the end of the scope (the end curly brace)


////////// Introduction to temporary objects //////////
// A temporary object (aka anonymous object) is an unnamed object that is used to hold a value that is only needed for a short period of time. 
