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


// **NOTE**: List-initialization (including value-initialization) is the preferred form of initialization in modern C++


// Q: When should I initialize with { 0 } vs {}?
// Use direct-list-initialization when you’re actually using the initial value:
int x { 0 };    // direct-list-initialization with initial value 0
std::cout << x; // we're using that 0 value here

// Use value-initialization when the object’s value is temporary and will be replaced:
int x {};      // value initialization
std::cin >> x; // we're immediately replacing that value so an explicit 0 would be meaningless


// Initializing multiple variables
int a = 5, b = 6;          // copy-initialization
int c ( 7 ), d ( 8 );      // direct-initialization
int e { 9 }, f { 10 };     // direct-list-initialization
int i {}, j {};            // value-initialization

// Common pitfall
int a, b = 5;     // wrong: a is not initialized to 5!
int a = 5, b = 5; // correct: a and b are initialized to 5


// Unused initialized variables warnings
// There are a few easy ways to fix this:
  // 1) Remove the definition
  // 2) Simply use the variable somewhere

/* However, in some cases, neither of the above options are desirable. 
To address such cases, C++17 introduced the [[maybe_unused]] attribute, which allows us 
to tell the compiler that we’re okay with a variable being unused. The compiler will not 
generate unused variable warnings for such variables. */

#include <iostream>

int main()
{
    [[maybe_unused]] double pi { 3.14159 };  // Don't complain if pi is unused
    [[maybe_unused]] double gravity { 9.8 }; // Don't complain if gravity is unused
    [[maybe_unused]] double phi { 1.61803 }; // Don't complain if phi is unused

    std::cout << pi << '\n';
    std::cout << phi << '\n';

    // The compiler will no longer warn about gravity not being used

    return 0;
}
