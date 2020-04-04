# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
   
    t = [char for char in s ]
    
    for n in range(len(t)):
        if t[n].isupper():
            t[n] = t[n].lower()
        else:
            t[n]=t[n].upper()
    
    new=""
    for x in t:
        new += x
    return new
    
    return


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


