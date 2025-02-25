3.5 - More debugging tactics

//////////////////// Conditionalizing your debugging code ////////////////////
// Use preprocessor directives 
main.cpp 
#include <iostream> 
#define ENABLE_DEBUG 

int main() { 
#ifdef ENABLE_DEBUG 
std::cerr << "getUserInput() called\n";
#endif
}

// However, not ideal because it still leads to code clutter


//////////////////// Using a logger ////////////////////
// A log is a sequential record of events that have happened, usually time-stamped.
// The process of generating a log is called logging.
// Typically, logs are written to a file on disk (called a log file), so they can be reviewed later.

// Some logs: plog, spdlog
