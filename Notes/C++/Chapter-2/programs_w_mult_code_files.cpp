2.8 - Programs with multiple code files

// Use function declaration when code is separated in multiple files
// Esentially, the forward declaration tells the compiler the eistence of an identifier, but it doesn't actually implement anything. 
// It's saying "Hey compiler, this identifier exists somewhere in the program, but not in this file."

// add.cpp: 
int add(int x, int y) 
{ 
  return x + y; 
}

// main.cpp
int add(int x, int y);  // function declaration

#include <iostream> 
int main() 
{ 
  std::cout << "The sum of 3 and 4 is: " << add(3, 4) << "\n";

  return 0;
}
