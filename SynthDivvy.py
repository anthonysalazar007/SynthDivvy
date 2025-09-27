print("Welcome to SynthDivvy; a program to run synthetic division.\n")
factors = []
terms = []
facsOfLead = []
facsOfConst = []
pOverQ = []
factorsNeg = []

#=== STEP 1: Get factors and convert them to ints, also getting all negative variables =====================================================
numOfFacsLead = int(input(f"How many total possible factors are there from your leading coefficient? (EXCLUDING negative values; those will be accounted for automatically)\n>>"))
numOfFacsConst = int(input(f"How many total possible factors are there from your constant? (EXCLUDING negative values; those will be accounted for automatically)\n>>"))

for a in range(numOfFacsLead): # for each possible factor of the leading coefficient (note; use range since numOfFacsLead is an int)
    responseFacLead = float(input("Enter a factor (Lead) :\n>>")) # asks user to input the factor
    facsOfLead.append(responseFacLead) #adds the factor to a list

for b in range(numOfFacsConst): 
    responseFacConst = float(input("Enter a factor (Constant) :\n>>"))
    facsOfConst.append(responseFacConst)

for p in facsOfConst: #going to divide every factor of the constant by every factor of the leading coefficient
    for q in facsOfLead:
        pOverQ.append(p / q) #adds the result to a new list

for negFacLead in facsOfLead: # all 3 loops loop through all factors and makes them negative, adding them to a new list
    factorsNeg.append(negFacLead * -1)
for negFacConst in facsOfConst:
    factorsNeg.append(negFacConst * -1)
for div in pOverQ:
    factorsNeg.append(div * -1)
factors = facsOfLead + facsOfConst + pOverQ + factorsNeg #combines the two lists, giving all factors both negative and positive
factors = list(set(factors)) #removes duplicates by converting to a set and back to a list
factors.sort() #sorts the list in ascending order
print(f"Your factors are: {factors}")

#=== STEP 2: Get coefficients and convert them to ints ======================================================================================
polyLen = int(input(f"How many terms are in your polynomial? (For example, x^2 + 2x + 10 has 3 terms)\n>>"))
for c in range(polyLen):
    responseTerm = float(input(f"Enter the coefficients of your polynomial\n>>"))
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
    print(f"After dividing by {divisor}, Your coefficients are {currentPolynomial[0:(len(currentPolynomial)-1)]} with a remainder of {currentPolynomial[-1]}\n***")
    currentPolynomial = [] # clear out polynomial for next divisor