// C++ reserves a set of 92 words for its own use. These words are called keywords (or reserved words). Each of these keywords has a special meaning within the C++ language.

////////// Identifier naming rules //////////
/* The identifier can not be a keyword. Keywords are reserved.
The identifier can only be composed of letters (lower or upper case), numbers, and the underscore character. That means the name can not contain symbols (except the underscore) 
nor whitespace (spaces or tabs). The identifier must begin with a letter (lower or upper case) or an underscore. It can not start with a number. 
C++ is case sensitive, and thus distinguishes between lower and upper case letters. nvalue is different than nValue is different than NVALUE. */


////////// Identifier naming best practices //////////
// Convetional that variable names begin with a lowercase letter 
// Often, function names start with a lowercase letter 
// If variable or function is multi-word, there are 2 common conventions: 
  // Words seprated underscores (snake_case) 
  // Intercapped (camelCase, since the capital letters stick up like the humps on a camel)
// Identifier names that start with a capital letter are typically used for user-defined types

////////// SUMMARY FOR IDENTIFIER NAMING BEST PRACTICES //////////
  // 1. Conventional that variable names begin with a lowercase letter. If  variable name is a single word, the whole thing should be written in lowercase letters.
  // 2. Avoid naming your identifiers starting with an underscore. Allowed but typically reserved for OS, library, and/or compiler use.
  // 3. Name of your identifiers should make clear what the value they are holding means (particularly if the units aren’t obvious)
  // 4. Avoid abbreviations, except when they are common and unambiguous (e.g. num, cm, idx)
  // 5. For variable declarations, it can be useful to use a comment to describe what a variable is going to be used for, or to explain anything else that might not be obvious. 

// A good rule of thumb is to make the length of an identifier proportional to how specific and accessible the identifier is. This means: 
  // An identifier that exists for only a few statement (e.g. in the body of a short function) can have a shorter name. 
  // An identifier that is accessible from anywhere might benefit from a longer name. 
  // An identifier that represents a non-specific number (e.g. anything the user provides) can have a shorter name. 
  // An identifer that represents a specific value (e.g. the length of an inseam in millimeters) should have a longer name.
