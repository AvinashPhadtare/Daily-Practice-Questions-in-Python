# ========================= Question =========================
#
# You are given the coefficients of a polynomial P.
#
# Your task is to find the value of P at point x.
#
# Example:
#
# Input:
# 1.1 2 3
# 0
#
# Output:
# 3.0
#
# Explanation:
#
# The given polynomial is:
# P(x) = 1.1x^2 + 2x + 3
#
# The given value is x = 0.
#
# Substituting x = 0:
# P(0) = 1.1(0)^2 + 2(0) + 3
# P(0) = 3.0
#
# Important Points:
#
# 1. Import the NumPy module using import numpy as np.
#
# 2. Read the space-separated polynomial coefficients.
#
# 3. Convert the coefficients into a NumPy array of floats.
#
# 4. Read the value of x.
#
# 5. Use np.polyval(P, x) to evaluate the polynomial at x.
#
# 6. Print the result.
#
# ============================================================

# ======================= Solution ===========================
import numpy as np

P = np.array(input().split(), dtype=float)

x = float(input())

print(np.polyval(P, x))
