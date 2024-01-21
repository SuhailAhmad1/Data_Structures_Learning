def karatsuba_polynomial_multiply(poly1, poly2):
    # Base case: If either polynomial is of degree 0, use simple multiplication
    if len(poly1) == 1 or len(poly2) == 1:
        return [poly1[0] * coeff for coeff in poly2]

    # Find the degree and midpoint of the input polynomials
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    midpoint = max(degree1, degree2) // 2

    # Split the input polynomials into low and high parts
    low1, high1 = poly1[:midpoint + 1], poly1[midpoint + 1:]
    low2, high2 = poly2[:midpoint + 1], poly2[midpoint + 1:]
    print(low1, high1)
    print(low2, high2)
    print()

    # Make sure low and high parts have the same length
    # if len(low1) < len(high1):
    #     low1 = [0] * (len(high1) - len(low1)) + low1
    # if len(low2) < len(high2):
    #     low2 = [0] * (len(high2) - len(low2)) + low2

    # Recursively compute the three products needed
    z0 = karatsuba_polynomial_multiply(low1, low2)
    z1 = karatsuba_polynomial_multiply(
        [low1[i] + high1[i] for i in range(len(low1))],
        [low2[i] + high2[i] for i in range(len(low2))]
    )
    z2 = karatsuba_polynomial_multiply(high1, high2)

    # Combine the results to get the final product
    result = [0] * (degree1 + degree2 + 2)
    for i in range(len(z0)):
        result[i] += z0[i]
        result[i + midpoint + 1] += z0[i]
    for i in range(len(z1)):
        result[i + midpoint] += z1[i]
    for i in range(len(z2)):
        result[i + 2 * midpoint] += z2[i]

    return result


if __name__ == "__main__":
    n = int(input())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    poly1, poly2 = [3,4,5], [5,1,2]
    print(karatsuba_polynomial_multiply(p1, p2))
