def narcissistic( value ):
    digit = len(str(value))
    sum = 0
    # place holder for the value and digit that will decrease
    # in order of magnitude as the loop goes
    intermediate_value = value  
    intermediate_digit = digit
    while intermediate_value > 0:
        # degree of the value is 1 less of to intermidiate_digit the will be raised to
        degree = 10**(intermediate_digit-1)
        current_digit_value = intermediate_value  // degree
        sum += current_digit_value ** digit
        intermediate_value -= degree* current_digit_value
        intermediate_digit -= 1
    return sum == value

