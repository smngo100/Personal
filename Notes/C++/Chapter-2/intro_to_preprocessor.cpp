2.10 - Introduction to the preprocessor 

// Prior to compilation, each code (.cpp) file goes through a PREPROCESSING phrase. 
// In this phase, a program called the PREPROCESSOR makes various changes to the text of the code file.
// When the preprocessor has finished processing a code file, the result is called a TRANSLATION UNIT. 
// The entire process of preprocessing, compiling, and linking is called TRANSLATION. 


//////////////////// Preprocessor directives ////////////////////
// Preprocessor directives (aka directives) are instructions that start with a # symbol and end with a newline (NOT semicolon).


//////////////////// Macro defines ////////////////////
// A MACRO is a rule that defines how input text is converted into replacement output text. 
// 2 basic types of macro: 
  // 1. object-like macros 
  // 2. function-like macros 

// Object-like macros can be defined in one of two ways: 
  #define IDENTIFIER 
  #define IDENTIFIER substitution_text 

// Avoid macros with substitution text


//////////////////// Conditional compilation ////////////////////
// the CONDITIONAL COMPILATION PREPROCESSOR directive allows you to specify under what conditions something will or won't compile. 

#define 
// Defines a macro, which can be tested for existence or value.

#if, #elif, #else, #endif 
// Conrol which code blocks are compiled based on a constant expression or macro definition. 

#ifdef 
// Checks if a macro is defined. 

#ifndef 
// Checks if a macro is not defined.

//////////////////// #if 0 ////////////////////
#if 0 
// Used to exclude a block of code from being compiled (as if it were inside a comment body)
// Why use this over multi-line commenting? Because multi-line comments are non-nestable
// To temporarily re-enable code that has been wrapped in an #if 0, you can change the #if 0 to #if 1
