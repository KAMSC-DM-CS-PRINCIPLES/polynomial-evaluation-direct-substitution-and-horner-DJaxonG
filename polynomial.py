def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result oko
    S = constant_term
    k = 1
    n = 0

    while k < n:
        S += constant_term*(x**k)
        k = k+1
    
    return S


if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again
    pass