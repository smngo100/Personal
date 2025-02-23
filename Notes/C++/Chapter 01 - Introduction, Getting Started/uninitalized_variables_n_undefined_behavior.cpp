1.6 Uninitialized variables and undefined behavior

// Uninitialized variable: A variable that has not been given a known value (through initialization or assignment)

// Note: 
// Initialized = The object is given a known value at the point of definition. 
// Assignment = The object is given a known value beyond the point of definition. 
// Uninitialized = The object has not been given a known value yet. 


// Undefined behavior: The result of executing code whose behavior is not well-defined by the C++ language
// Analogy: Undefined behavior is like a box of chocolates. You never know what you're going to get!

// Rule: Take care to avoid all situations that result in undefined behavior, such as using uninitialized variables. 

// Implementation: A specific compiler and the associated standard library it comes with 

// Implementation-defined behavior: Behavior that is defined by the implementation 

// Unspecififed behavior: Behavior is left up to the implemtnation to define, but the implementation is not required to document the behavior
