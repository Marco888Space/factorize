def is_prime(number):
    """
    Checks if a number is prime number.
    """

    divisor_p=2

    while divisor_p<number:
        if number%divisor_p == 0:
            return False
            #print("False")
        else:
            divisor_p+=1
    return True
    #print("True")

def factorize(number):
    """
    Factorizes a number (n!=0, n>0, n is natural number).
    """

    divisor=2

    if (number==0) or (number<0) or (number==1) or (is_prime(number) is True):
        print("ERROR! Factorizing conditions: n>0, n!=0, n>1, n IS NOT PRIME NUMBER.")
        exit()

    while number>1:
        if number%divisor == 0:
            print(divisor)
            number//=divisor
        else:
            divisor+=1

factorize(18)
