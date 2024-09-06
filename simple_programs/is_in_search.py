
def isIn(char, alpha_string):
    '''
    char: a single character
    alpha_string: an alphabetized string
    
    returns: True if char is in alpha_string; False otherwise
    '''
    middle_point = int(len(alpha_string) / 2)

    if len(alpha_string) == 0:
        return False
    
    if char == alpha_string[middle_point]:
        return True
    
    if len(alpha_string) == 1 and char == alpha_string:
        return True
    elif len(alpha_string) == 1 and char != alpha_string:
        return False
    else:
        if char >= alpha_string[middle_point]:
            alpha_string = alpha_string[middle_point:]
        else:
            alpha_string = alpha_string[0: middle_point]
        return isIn(char, alpha_string)



alpha_order = 'abcdefghijklmnopqrstuvwxyz'
# alpha_order = 'cddlqxyz'
alpha_order = 'abc'
look_for = 'n'

print(isIn(look_for, alpha_order))