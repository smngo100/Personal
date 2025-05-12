#include <iostream>
#include <filesystem>
#include <vector>
#include <algorithm>
#include <unistd.h>     // For fork(), chdir(), execv()
#include <wait.h>       // For waitpid()
#include <fcntl.h>      // For file control options like O_WRONLY

namespace fs = std::filesystem;         // Alias for std::filesystem
std::vector<std::string> succ_cmds;     // Vector to store successful commands for history feature

/**
 * Changes current directory based on path
 * 
 * @param currentDir - Current working directory
 * @param path - Destination path (absolute or relative)
 * @return New current directory path
 */
fs::path change_directory(const fs::path& currentDir, const std::string& path) {
    fs::path newPath;

    // Handle absolute vs relative paths
    if (path[0] == '/') {
        newPath = path; // Absolute path
    }
    else {
        newPath = currentDir / path;    // Relative path
    }

    // Check if path exists before changing
    if (fs::exists(newPath)) {
        return fs::canonical(newPath);  // Resolves ".." references
    }
    else {
        std::cout << "Path does not exist" << std::endl;
        return currentDir;
    }
}

/**
 * Lists contents of the current directory
 * Directories are listed first, then files (both in alphabetical order)
 * 
 * @param currentDir - Directory to list
 */
void list_directory(const fs::path& currentDir) {
    // Separate vectors for directories and files
    std::vector<fs::path> directories;
    std::vector<fs::path> files;

    // Sort contents into appropriate vectors
    for (const auto& entry : fs::directory_iterator(currentDir)) {
        if (entry.is_directory()) {
            directories.push_back(entry.path());
        }
        else {
            files.push_back(entry.path());
        }
    }

    // Sort both vectors alphabetically
    std::sort(directories.begin(), directories.end());
    std::sort(files.begin(), files.end());

    // Print directories first
    for (const auto& dir : directories) {
        std::cout << dir.filename().string() << " (Directory)" << std::endl;
    }

    // Print files second
    for (const auto& file : files) {
        std::cout << file.filename().string() << std::endl;
    }
}

/**
 * Prints the current working directory as part of shell prompt
 * 
 * @param workingDir - Current working directory
 */
void workDir(const fs::path& workingDir) {
    std::cout << workingDir.string() << " $ ";
}

/**
 * Display command history in reverse order (most recent first)
 * Uses reverse iterators to traverse the vector from end to beginning
 */
void history() {
    for (auto itr {succ_cmds.rbegin()}; itr != succ_cmds.rend(); ++itr) {
        std::cout << *itr << std::endl;
    }
}

/**
 * Executes external programs with arguments and optional output redirection
 * 
 * @param command - Full command string with program path, arguments, and optional redirection
 */
void executeProgram(const std::string& command) {
    // Check for output redirection
    size_t redirect = command.find("> ");
    std::string actualCommand = command;
    std::string outputFileName = "";
    // ^ Will store the name of an output file if the user includes an output redirection in
    // their command

    // If redirection is requested, split command and output file name
    if (redirect != std::string::npos) {
        actualCommand = command.substr(0, redirect);
        outputFileName = command.substr(redirect + 2); // Skip '> '
    }

    fs::path programPath;
    std::vector<std::string> programArgs;

    // Create string stream for parsing command parts
    // Wraps the string actualCommand in a stream so we can extract words from it using >>
    std::istringstream iss(actualCommand);

    // Get the program path (first part of command)
    std::string path;
    iss >> path;    // Reads the first word from the stream
    programPath = path;    // Assigns it to programPath, which is the program to execute

    // Read arguments until end of stream
    std::string arg;
    while (!iss.eof()) {
        iss >> arg;

        // Only add non-empty arguments
        if (arg.length() > 0) {
            programArgs.push_back(arg);
        }
    }

    // Create dynamic array for C-style arguments needed by execv
    // Size is program arguments + 2 (for program name and nullptr terminator)
    char** cargs {new char*[programArgs.size() + 2]};

    // Fill in program arguments
    // Loop through the entire vector
    for (size_t i{0}; i < programArgs.size(); ++i) {
        cargs[i + 1] = programArgs[i].data();
    }

    // Null-terminate the argument list (required by execv)
    cargs[programArgs.size() + 1] = nullptr;

    // First argument is the program path itself (convention for execv)
    cargs[0] = path.data();

    // Create child process
    int cid {fork()};

    if (cid == 0) {
        // Child process code
        
        // Handle redirection if requested
        if (redirect != std::string::npos) {
            // Open output file (create if doesn't exist, truncate if does)
            int outputFile = open(outputFileName.c_str(), 
                                 O_WRONLY | O_CREAT | O_TRUNC,
                                 S_IRUSR | S_IWUSR);

            // Redirect stdout and stderr to the file
            dup2(outputFile, STDOUT_FILENO);
            dup2(outputFile, STDERR_FILENO);
        }

        // Execute the program
        if (execv(programPath.c_str(), cargs) == -1) {
            std::cout << "There was an error when trying to exec" << std::endl
                      << "Error number " << errno << std::endl;
            exit(1);
        }
    }
    else {
        // Parent process code
        
        // Wait for child to complete
        int statusCode;
        waitpid(cid, &statusCode, 0);    // Wait so that parent knows if child succeeded or failed
        
        // Report non-zero exit status
        if (statusCode != 0) {
            std::cout << "Program failed with code " << statusCode << std::endl;
        }
        
        // Free dynamically allocated memory
        delete[] cargs;
    }
}

/**
 * Exit the shell
 */
void quit() {
    exit(0);
}

int main() {
    std::cout << "Welcome to ElbeeShell" << "\n\n";
    
    // Initialize working directory to root
    fs::path workingDir = "/";

    // Change to the working directory at OS level as well
    if (chdir(workingDir.c_str()) != 0) {
        std::cout << "Failed to change to working directory: " << workingDir.string() << std::endl;
    }

    // Main shell loop
    while (true) {
        // Print the prompt with current directory
        workDir(workingDir);

        // Read input
        std::string input;
        std::getline(std::cin, input);

        // Parse command and path
        std::string command;    // Stores the command (e.g. "cd" "list")
        std::string path;       // Stores path after the command
        size_t space = input.find(' ');
        if (space != std::string::npos) {
            command = input.substr(0, space);
            path = input.substr(space + 1);
        }
        else {
            command = input;
            path = "";
        }

        // Process commands
        if (command == "workdir") {
            std::cout << "Working directory: " << workingDir.string() << std::endl;
            // Move command to history using std::move for optimization
            succ_cmds.push_back(std::move(command));
        }
        else if (command == "cd") {
            // Change directory both in the shell and at OS level
            workingDir = change_directory(workingDir, path);
            if (chdir(workingDir.c_str()) != 0) {
                std::cout << "Failed to change to working directory: " << workingDir.string() << std::endl;
            }
            succ_cmds.push_back(std::move(command));
        }
        else if (command == "list") {
            list_directory(workingDir);
            succ_cmds.push_back(std::move(command));
        }
        else if (command == "history") {
            // Note: history command itself is not added to history
            history();
        }
        else if (command == "exit") {
            quit();
        }
        else {
            // Execute external program if not a built-in command
            executeProgram(input);
        }

        // Print blank line after each command for readability
        std::cout << std::endl;
    }
    return 0;
}
