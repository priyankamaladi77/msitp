'''square'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''square'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    #step = 0.1
    # your code starts here
    val = int(input())
    ans = 0.0
    inc = 0.1
    count = 0
    while abs(ans**2 - val) >= epsilon:
        ans += inc
        count += 1
    if abs(ans**2 - val) >= epsilon:
        print("failed on square root of", val)
    else:
        print(ans, 'is close square root of', val)
if __name__ == "__main__":
    main()
