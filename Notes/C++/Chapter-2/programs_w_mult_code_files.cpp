2.8 - Programs with multiple code files

// Use function declaration when
// Think of this as an import in Python 
// In Python, you import a function from another file, but in C++ you do a function declaration

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
