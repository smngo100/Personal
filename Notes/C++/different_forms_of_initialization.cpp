// 5 common forms of initialization: 

int a;         // default-initialization (no initializer)

// Traditional initialization forms:
int b = 5;     // copy-initialization (initial value after equals sign)
int c ( 6 );   // direct-initialization (initial value in parenthesis)

// Modern initialization forms (preferred):
int d { 7 };   // direct-list-initialization (initial value in braces)
int e {};      // value-initialization (empty braces)


// Default-initialization: When no initializer is provided.
// Copy-initialization: When an initial value is provided after an equals sign.
// Direct-initialization: When an initial value is provided inside parenthesis.
// List-initialization (or uniform initialization or brace initialization): 
  // List-initialization comes in two forms:
    // int width { 5 };      direct-list-initialization (preferred)
    // int height = { 6 };   copy-list-initialization (rarely used)
// Value-initialization: A special form of list-initialization when a variable is initialized using an empty set of braces.
// Zero-initialization: When zeroing occurs
   
// **NOTE**: List-initialization is the preferred form of initialization in modern C++
