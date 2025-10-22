def evaluate_polynomial_horner(degree, x, constant_term, coefficients):
    # TODO: Implement polynomial evaluation using Horner's method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    S = coefficients[len(coefficients)-1]
    print(S)
    k = 1
    n = degree-1
    while k <= degree:
        num = coefficients[n-k]
        S = x*S+num
        k += 1
        print(f"num{num} S{S} k{k}")
    S+=constant_term
    S+=1
    return S


if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial_horner function
    # TODO: Ask user if they want to run again
    answer = "y"

    while(answer=="y"):
        enterX = int(input("Enter x: "))
        enterDegree = int(input("Enter degree: "))
        enterConstant = int(input("Enter constant: "))
        coefficients = []

        for i in range(1, enterDegree+1):
            coefficients += (int(input(f"Coefficient of the x^{i} term" )),)
        
        print("")
        print("P(x) = " + str(evaluate_polynomial_horner(enterDegree, enterX, enterConstant, coefficients)))
        print("")
        answer = input("do you want another poly? (y/n): ")
        print("")
