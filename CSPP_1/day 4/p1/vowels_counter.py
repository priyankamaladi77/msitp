'''vowels'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''Vowels'''
    #s = raw_input()
    stri = input()
    vowcount = 0
    for char in stri:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowcount += 1
    print(vowcount)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()
