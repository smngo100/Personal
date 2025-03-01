3.6 - Using an integrated debugger: Stepping 

// Program state (aka state): Tracked information


//////////////////// The debugger ////////////////////
// A debugger is a computer program that allows the programmer to control how another program executes and examine the program state while that program is running.
// An integrated debugger is a debugger that uses the same interface as the code editor, so you can debug using the same environment that you use to write your code (rather than having to switch programs).
  
//////////////////// Stepping ////////////////////
// Stepping is the name for a set of related debugger features that let us execute (step through) our code statemeny by statement.

//////////////////// Step into ////////////////////
// Step into command executes next statement, if next statement contains function call, step into causes the program to jump to the top of the funciton being called, where it will pause.
// Step into will enter function calls and execute them line by line
  
//////////////////// Step over ////////////////////
// Similar to step into, step over command executes the next statement in the normal execution path of the program.
// Step over will execute an entire function without stopping and return control to you after the function has been executed. 

//////////////////// Step out ////////////////////
// Step out does not just execute the next line of code
// It executes all remaining code in the function curerntly being executed, and then returns control to you when the function has returned 
