4.8 - Floating point numbers 

// A floating point type variable is a variable that can hold a number with a fractional component.
// Floating part of the name refers to the fact that the decmal point can "float", it can support a variable number of digits before and after the decimal point.
// Floating point data types are always signed (can hold positive and negative values)

//////////////////// C++ floating point types ////////////////////
// 3 fundamental floating point data types
  // 1) single-precision    float 
  // 2) double-precision    double
  // 3) extended-precision  long double

// Actual size of these types are not defined 


//////////////////// Floating point precision //////////////////// 
// The precision of a floating point type defines how many significant digits it can represent without information loss. 


//////////////////// Outputting floating point values //////////////////// 
// Output manipulators alter how data is output, and are defined in the iomanip header 
// Rounding error: When precision is lost because a number can't be stored precisely 


//////////////////// NaN and Inf //////////////////// 
// IEEE 754 formats for special values
  // Inf represents infinity 
  // NaN stands for "Not a Number" 
  // Signed zero, "positive zero" (+0.0) and "negative zero" (-0.0)
