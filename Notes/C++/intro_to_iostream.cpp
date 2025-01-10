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
