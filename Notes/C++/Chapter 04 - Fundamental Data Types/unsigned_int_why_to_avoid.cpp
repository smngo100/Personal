4.5 - Unsigned integers, and why to avoid them

// Unsigned integers are integers that hold non-negative whole numbers.

//////////////////// Unsigned integer range ////////////////////
// An n-bit unsigned variable has a range of 0 to (2^n) - 1

//////////////////// The controversy over unsigned numbers ////////////////////
// Why avoid? Because of 2 behaviors that cause problems: 
  // 1) Much easier to overflow the bottom of the range, bc the bottom of the range is 0
  // 2) Unexpected behavior can result when you mix signed and unsigend integers
