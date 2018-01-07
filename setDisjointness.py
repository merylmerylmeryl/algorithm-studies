def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def factorial(n):
    """Return n!."""
    return 1 if n == 0 else n * factorial(n-1)
