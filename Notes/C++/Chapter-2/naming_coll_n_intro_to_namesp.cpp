2.9 - Naming collisions and an introduction to namespace 

/* Naming collision (or naming conflict): If two identical identifiers are introduced into the same program 
in a way that the compiler or linker can't tell them apart, the compiler or linker will produce an error. 
*/


////////// Scope regions //////////
// SCOPE REGION: An area of source code where all declared identifiers are considered distinct from names declared in other scope.


////////// Namespaces //////////
// NAMESPACE: Provides another type of scope region (called the namespace scope) that allows you to declare names inside of it for the purpose of disambiguation.


////////// The global namespace //////////
// GLOBAL NAMESPACE (aka global scope): Any name that is not defined inside a class, function, or a namespace is considered to be part of an implicitly-defined namespace.
  // Identifiers decalred inside the global scope are in scope from the point of declaration to the end of the file. 
  // AVOID defining variables  in the global namespace


////////// The std namespace //////////
// std is short for "standard" 


////////// Explicit namespace qualifier std:: //////////
// Straightforward option 
std::cout 

// :: symbol is an operator called the SCOPE RESOLUTION OPERATOR 
// No identifier to left of ::, then the global namespace is assumed
// When an identifier includes a namespace prefix, the identifier is called a QUALIFIED NAME


////////// Using namespace std (and why to avoid it) //////////
#include <iostream>
using namespace std; // this is a using-directive

// USING-DIRECTIVE: It allows us to access names in the namespace without using a namespace prefix
// AVOID using-directives 



