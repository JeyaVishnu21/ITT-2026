#This program helps to fint price amount of chandru 

t = int(input("Enter number of test cases:))
for _ in range(t):
    x = int(input("Enter the price amout:"))
    s = input("Enter winner string:")
    chandru_score = 0
    nirmal_score = 0
    for char in s:
        if char == 'C':
            chandru_score += 2
        elif char == 'N':
            nirmal_score += 2
        elif char == 'D':
            chandru_score += 1
            nirmal_score += 1
    if chandru_score > nirmal_score:
        print(60 * x)
    elif nirmal_score > chandru_score:
        print(40 * x)
    else:
        print(55 * x)
