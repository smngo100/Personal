2.12 - Header guards

//////////////////// Header guards ////////////////////
// Header guard (aka include guard) are conditional compilation directives that take the following form: 
#ifndef SOME_UNIQUE_NAME_HERE
#define SOME_UNIQUE_NAME_HERE

// your declarations (and certain types of definitions) here 

#endif


//////////////////// #pragma once ////////////////////
#pragma once 
// Serves the same purpose as header guards to avoid a header file from being included multiple times. 
// We're requesting the compiler guard the header.
