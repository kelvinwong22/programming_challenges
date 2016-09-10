#!/usr/bin/env python
"""
Consider the following algorithm to generate a sequence of numbers. Start with an
integer n. If n is even, divide by 2. If n is odd, multiply by 3 and add 1. Repeat this
process with the new value of n, terminating when n = 1. 

For example, the following
sequence of numbers will be generated for n = 22:
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

It is conjectured (but not yet proven) that this algorithm will terminate at n = 1 for
every integer n. Still, the conjecture holds for all integers up to at least 1, 000, 000.
For an input n, the cycle-length of n is the number of numbers generated up to and
including the 1. In the example above, the cycle length of 22 is 16. Given any two
numbers i and j, you are to determine the maximum cycle length over all numbers
between i and j, including both endpoints.
"""

def algorithm(n):
    '''if even, divide by 2, if odd multiply by 3 and add 1.'''
    cycle_num = 1
    while n != 1:
        if n % 2 == 0:
            # n is even
            n = n/ 2
            cycle_num += 1
        else:
            #n is odd
            n = (n * 3) + 1 
            cycle_num += 1

    return (cycle_num)

def main ():
    
    #Ask the user for two numbers in the format of i j (1 10)
    input_numbers = raw_input('Please provide two numbers, between 1 and 1,000,000, in the form of 1 10: ')
    
    numbers = input_numbers.split(' ')
    
    if len(numbers) != 2:
        print('2 numbers were not provided. Exiting...')
        return 0
    
    numbers = map(int, numbers)
    a, b = numbers
    if a > b :
        int_range = xrange(b, (a + 1))
    else:
        int_range = xrange(a, (b + 1))
    
    max_cycle = 0
    for i in int_range:
        temp_cycle = algorithm(i)
        
        if max_cycle < temp_cycle:
            max_cycle = temp_cycle

    print("{} {} {}".format(a, b, max_cycle))
    
if __name__ == '__main__':
    main()
    