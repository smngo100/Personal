2.4 - Introduction to function parameters and arguments 

////////// Function parameters and arguments //////////
// Function parameters: A variable used in the header of a function.
// Argument: A value that is passed from the caller to the function when a function call is made.


////////// Unreferenced parameters //////////
// Unreferenced parameters: Functions that have parameters that are not uesd in the body of the funciton.
// Unnamed parameter: A parameter without a name. 
  // Function parameter is optional.
  // Suggests to use a comment to document what the unnamed parameter was.
  // When a function parameter exists but is not used in the body of the function, do not give it a name. Can optionally put a name inside a comment.
      void doSomething(int /*count*/)
      {
      }
