2.11 - Header files

//////////////////// Header files ////////////////////
// Header file: Have a .h extenion, or .hpp extension, or no extension at all 
// Used to propagate a bunch of related forward declarations into a code file 
// Essentially, they allow us to put declarations in one place and then import them whenever we need them.


//////////////////// Using standard library header files ////////////////////
// When we #include <iostream>, we're requesting that the preprocessor copy all of the content (including forward declarations...
// ...for std::cout) from the file named "iostream" into the file doing the #include.
// When you #inlcude a file, the content of the included file is inserted at the point of inclusion. This provides a useful way to pull in declarations from another file.


//////////////////// Using header files to propagate forward declarations ////////////////////
// If a header file is paired with a code file (e.g. add.h with add.cpp), they should both have the same base name (add)
// To use the header file in main.cpp or any file, we have to #include (sing quotes, not angle brackets) 
#include "add.h" 


//////////////////// Source files should include their paired header ////////////////////
// Source files should #include their paired header file (if one exists) 
// Avoid #including .cpp files 


//////////////////// Angled brackets vs double quotes ////////////////////
// Angled brackets vs double quotes helps give the preprocessor a clue as to where it should look for header files.
// Use angled brackets to include headers that come with your compiler, OS, or third-party libraries you've installed elsewhere on your system.
// Use double quotes to include header files that you've written or are expected to be found in the current directory. 


//////////////////// Transitive includes ////////////////////
/* When your source (.cpp) file #includes a header file, you'll also get any other header files that are #included by that header
files those include, and so on). These additional header files are sometimes called transitive includes, as they're included 
implicitly rather than explicity. */
// BEST PRACTICE: Each file should explicitly #include all of the header files it needs to compile. Do not rely on headers included transitively from other headers.

// To maximize the chance that missing includes will be flagged by compiler, order your #includes as follows (skipping any that are not relevant):
  /* 
  * The paired header file for this code file (e.g. add.cpp should #include "add.h")
  * Other headers from the same project (e.g. #include "mymath.h")
  * 3rd party library headers (e.g. #include <boost/tuple/tuple.hpp>)
  * Standard library headers (e.g. #include <iostream>)
  */
// Headers should be sorted alphabetically 
