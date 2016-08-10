def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, (num-1)):
        if ((num % i) == 0):
            return False
            break

    return True


def godel_number(array):

    if (len(array) == 0):
        return 0

    primearray = [2]
    i0 = 2
    while(len(primearray) < len(array)):
        
        i0 += 1
        if is_prime(i0):
            primearray.append(i0)
        
    encoding = 2**int(array[0])
    
    if (len(array) > 1):
        for i1 in range(1, len(array)):
            encoding = encoding*((primearray[i1])**int(array[i1]))

    return encoding


#Example use:
#print(str(godel_number([35, 23])) + "\n")
