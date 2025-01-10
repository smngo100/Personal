iostream   // io stands for input/output
std::cout  // cout stands for "character output"; uses the insertion operator << to provide data
std::cin   // cint stands for "character input"; uses the extraction operator >> to put the input data in a variable     


// Concatenate (link together) multiple pieces of output
#include <iostream> 
int main() 
{
  std::cout << "Hello" << " world!"; 
  return 0;
}


// Using std::endl to output a newline 
#include <iostream> 
int main() 
{
  std::cout << "Hi!" << std::endl;  // std::endl will cause the cursor to move to the next line 
  std::cout << "My name is Muffin." << std::endl;
  return 0;
}
// Best practice: Output a newline whenever a line of output is complete.


// std::cout is buffered
// Buffer: When the requested output "gets in line", and is stored in a region of memory set aside to collect such requests.
// Flushed: Periodically, the buffer is flushed, meaning all of the data collected in the buffer is transferred to its destination (in this case, the console).
// Unbuffered output: Each individual output request is sent directly to the output device. 


// Using \n to output a newline 
// std::endl is often inefficient as it flushes the buffer, however, \n outputs a newline without flushing the output buffer.
#include <iostream> // for std::cout
int main()
{
  int x{ 5 };
  std::cout << "x is equal to: " << x << '\n';  // single quoted (by itself) (conventional)
  std::cout << "Yep." << "\n";                  // double quoted (by itself) (unconventional but okay)
  std::cout << "And that's all, folks!\n";      // between double quotes in existing text (conventional)
  return 0;
}
// Prefer \n over std::endl when outputting text to the console.


// std::cin
#include <iostream>
int main()
{
  std::cout << "Enter a number: "; 
  int x{}; 
  std::cin >> x; 
  std::cout << "You entered << x << '\n';
  return 0;
}
// When writing an INPUT line, you don't need to write '\n' because the user will press the enter key to get their input accepted, and this will move the cursor to the next line of the console.

// It's possible to input more than one value on a single line:
#include <iostream>  // for std::cout and std::cin
int main()
{
    std::cout << "Enter two numbers separated by a space: ";
    int x{}; // define variable x to hold user input (and value-initialize it)
    int y{}; // define variable y to hold user input (and value-initialize it)
    std::cin >> x >> y; // get two numbers and store in variable x and y respectively
    std::cout << "You entered " << x << " and " << y << '\n';
    return 0;
}


// std::cin is buffered
