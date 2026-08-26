# ========================= Question =========================
# Given an integer n, perform the following conditional actions:
#
# 1. If n is odd, print "Weird".
# 2. If n is even and in the range 2 to 5, print "Not Weird".
# 3. If n is even and in the range 6 to 20, print "Weird".
# 4. If n is even and greater than 20, print "Not Weird".
#
# =============================================================

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")

    elif 2 <= n <= 5:
        print("Not Weird")

    elif 6 <= n <= 20:
        print("Weird")

    else:
        print("Not Weird")
