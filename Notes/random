#include <chrono>                 // For timing the simulation
#include <iostream>               // For input/output
#include <random>                 // For random number generation
#include <thread>                 // For parallel execution

/**
 * Monte Carlo simulation to estimate Pi
 *
 * @param numberOfTrials - Number of dart throws to simulate
 * @param hitCount - Pointer to dynamic storage for storing hit count
 *                   (Used for thread communication back to main)
 */

// Parallel execution: multiple threads of execution run at the same time, on separate cores

// int *hitCount is a pointer to an integer in memory where the # of "hits" will be stored,
// so that the result can be returned from the thread back to main
void monteCarloPi(int numberOfTrials, int *hitCount) {
    // Create random number generation tools
    // Uses hardware-based random device as seed source for better randomness
    std::random_device rd {};
    std::default_random_engine engine {rd()};

    // Create uniform distribution for x,y coordinates between 0.0 and 1.0
    // This implements the "dart throwing" in the Monte Carlo simulation
    std::uniform_real_distribution<double> darts{0.0, 1.0};

    // Counter for darts that land in the quarter circle
    int hits{0};

    // Simulation loop - each iteration is one "dart throw"
    for (int i = 0; i < numberOfTrials; i++) {
        // Generate random x,y coordinates (the "dart throw")
        double dartX {darts(engine)};
        double dartY {darts(engine)};

        // Calculate distance from origin using Pythagorean theorem
        // If distance <= 1.0, the dart landed inside the quarter circle
        double distance {std::sqrt(dartX * dartX + dartY * dartY)};
        if (distance <= 1.0) {
            ++hits;
        }
    }

    // Store the hit count to the provided pointer, so it stores the result back in memory the main threads owns
    // This line writes the value of hits into the memory location that hitCount points to
    // thus passing the result back to the main thread
    // This is how the thread communicates results back to main
    *hitCount = hits;

    // The following code was commented out because Pi calculation happens in main
    // with the combined results from all threads
    //double piEstimate = (4.0 * hits) / numberOfTrials;
    //std::cout << "PI estimate: " << piEstimate << std::endl;
}

int main()
{
    // Constants for the simulation
    const int totalThrows = 20000000;    // Total number of dart throws as specified in assignment
    const int numberOfThreads = 4;       // Using 4 parallel threads for the calculation
    const int throwsPerThread = totalThrows / numberOfThreads;  // Divide work evenly

    // Start timing the simulation
    auto start {std::chrono::high_resolution_clock::now()};

    // Create 4 pointers to dynamic storage for thread communication
    // Each pointer points to its own memory that will store the result of each thread
    // Each thread will store its hit count in one of these locations
    int *hits1 = new int{};  // Initialize to zero
    int *hits2 = new int{};
    int *hits3 = new int{};
    int *hits4 = new int{};

    // Create and launch 4 threads to run the Monte Carlo simulation in parallel
    // Each thread processes throwsPerThread darts independently
    std::thread t1(monteCarloPi, throwsPerThread, hits1);
    std::thread t2(monteCarloPi, throwsPerThread, hits2);
    std::thread t3(monteCarloPi, throwsPerThread, hits3);
    std::thread t4(monteCarloPi, throwsPerThread, hits4);

    // join() method waits for the thread to complete its execution before proceeding
    // Wait for all threads to complete before proceeding
    // join() call block the main thread until each of the 4 threads has finished
    // Once done, the values pointed to hits 1 - hits 4 are valid and contain the hit counts
    // The main thread continues execution
    t1.join();
    t2.join();
    t3.join();
    t4.join();

    // Calculate total hits across all threads
    int totalHits = *hits1 + *hits2 + *hits3 + *hits4;

    // Calculate pi using formula: pi = 4 * (hits / totalThrows)
    double piEstimate = (4.0 * totalHits) / totalThrows;

    // Stop timing
    auto end {std::chrono::high_resolution_clock::now()};

    // Clean up dynamically allocated memory to prevent memory leaks
    delete hits1;
    delete hits2;
    delete hits3;
    delete hits4;

    // Calculate duration and output results
    auto duration {end - start};
    std::cout << "PI estimate: " << piEstimate << std::endl;
    std::cout << "Simulation took "
              << std::chrono::duration_cast<std::chrono::milliseconds>(duration).count()
              << " milliseconds" << std::endl;

    return 0;
}
