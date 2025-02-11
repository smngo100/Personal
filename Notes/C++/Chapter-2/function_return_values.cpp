2.2 - Function return values (value-returning functions) 

////////// Return Values //////////
// To return a value back to the caller, 2 things are needed: 
  // 1. Function has to indicate what type of value will be returned.
    // Return type: The type that is defined before the function's name.
  // 2. Inside the funciton that will return a value, we use a return statement to indicate the specific value being returned to the caller. 
    // Consists of the return keyword, followed by an expression (aka return expression), ending with a semicolon.

// The process of returning a copied value back to the caller is named return by value.


////////// Staatus Code //////////
// The return value from main() is sometimes called a status code (or less commonly, an exit code, or rarely a return code).
// The status code is used to signal whether your program was successful or not.

///// What it means /////
// Status code of 0 means the program ran normally (program executed and behaved as expected) 
// A non-zero status code often used to indciate some kind of failure.


////////// A value-returning function that does not return a value will produce undefined behavior //////////
// A function that returns a value is called a value-returning function.
  // Function is value-returning if the return type is anything other than void.
  // Must return a value of that type, otherwise undefined behavior will result.

  
