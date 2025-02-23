2.3 - Void Functions (non-value returning functions) 

///// Syntax for a Function Definition /////
returnType identifier() // identifier replaced with the name of your function
{ 
// Your code here
}

////////// Void return values //////////
// To tell the compiler that a function does not return a value, a return type of void is used.
// A function that DOES NOT return a value is called non-value returning function (or a void function).

// DO NOT put a return statement at the end of a non-value returning function. Why? REDUNDANT
  void printHi()
{ 
  std::cout << "Hi" << "\n";
  return; // NOT NEEDED. Redundant since the return will happen at the end of the function anyway!
}


///// Tip /////
// Some statements require values to be provided, and others don't 
// When we have a statement that consists of just a function call, we're calling a function for its behavior, not its return value. 
// When we call a function in a context that requires a value (e.g. std::cout), a value must be provided. 
