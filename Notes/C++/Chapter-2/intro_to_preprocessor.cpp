2.10 - Introduction to the preprocessor 

// Prior to compilation, each code (.cpp) file goes through a PREPROCESSING phrase. 
// In this phase, a program called the PREPROCESSOR makes various changes to the text of the code file.
// When the preprocessor has finished processing a code file, the result is called a TRANSLATION UNIT. 
// The entire process of preprocessing, compiling, and linking is called TRANSLATION. 


////////// Preprocessor directives //////////
// Preprocessor directives (aka directives) are instructions that start with a # symbol and end with a newline (NOT semicolon).


////////// Macro defines //////////
// A MACRO is a rule that defines how input text is converted into replacement output text. 
// 2 basic types of macro: 
  // 1. object-like macros 
  // 2. function-like macros 

// Object-like macros can be defined in one of two ways: 
  #define IDENTIFIER 
  #define IDENTIFIER substitution_text 

