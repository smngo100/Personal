4.6 - Fixed-width integers and size_t

// Used a fix-width integer type when you need an integral type that has a guaranteed range.
// Avoid the fast and least integral types because they may exhibit different behaviors on architectures where they resolve to different sizes. 
