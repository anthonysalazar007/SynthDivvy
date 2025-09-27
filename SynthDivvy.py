print("Welcome to SynthDivvy; a program to run synthetic division.")
factors = []
factorsNeg = []
terms = []

#=== STEP 1: Get factors and convert them to ints, also getting all negative variables =====================================================
numOfFacs = int(input(f"How many total possible factors are there from your leading coefficient and constant? (EXCLUDING negative values; those will be accounted for automatically)\n>>"))
for a in range(numOfFacs):
    responseFac = int(input("Enter a factor (Input fractions as decimals):\n>>"))
    factors.append(responseFac)
for b in factors: #creates a list of negative factors
    factorsNeg.append(b * -1)
factors = factors + factorsNeg #combines the two lists, giving all factors both negative and positive


#=== STEP 2: Get coefficients and convert them to ints ======================================================================================
polyLen = int(input(f"How many terms are in your polynomial? (For example, x^2 + 2x + 10 has 3 terms)\n>>"))
for c in range(polyLen):
    responseTerm = int(input(f"Enter the coefficients of your polynomial\n>>"))
    terms.append(responseTerm)

#=== ACTUAL MATH PART NOW ===

for divisor in factors: #loops through all possible rational roots (divisors)
    currentPolynomial = [terms[0]] # as first term pulls through, we start the new polynomial with only that
    curVal = divisor * terms[0] #as the first coeffeiecient is always brought down, we multiply it by the divisor to get the next value and start at the second term
    for term in terms[1:len(terms)]: #loops through all coefficients of the polynomial starting at 2nd term (Note to self, slice with coloons not commas)
        curVal += term #adds the current term to the current value
        currentPolynomial.append(curVal)
        curVal *= divisor #multiplies the current value by the divisor to get the next value
        #===Calculations done, now to check if the remainder is 0===
    if currentPolynomial[-1] == 0: #if the remainder is 0, then the divisor is a root
        print(f"THIS FACTOR IS A ROOT!: {divisor}")
    print(f"After dividing by {divisor}, Your coefficients are {currentPolynomial[0:(len(currentPolynomial)-1)]} with a remainder of {currentPolynomial[-1]}")
    currentPolynomial = [] # clear out polynomial for next divisor