tests = [
    'vahnmffyycnjabrkexjjoid',
    'rxgmwawxjyhwsphsfanyzdvw',
    'iwnmmlkny',
    'piqeaojyomtojy',
    'zyxwvutsrqponmlkjihgfedcba',
    'abcdefghijklmnopqrstuvwxyz',
    'xehgouklvpc',
    'pepwpdoagnis',
    'gurkcaduzf',
    'ifhdvqtaufu', 
    'rlcyxlujnqiamyjzaxhqfqxg'
]

expected_results = [
    'ffyy',
    'anyz', 
    'kny',
    'iq', 
    'z', 
    'abcdefghijklmnopqrstuvwxyz',
    'gou',
    'epw',
    'aduz',
    'fh',
    'jnq'
]

""" 
    This function is is using additional letter indexing
"""
def streakFinder(input_string : str) -> str:
    alph_order = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    streak = ""
   
    current_letter_index = -1
    previous_letter_index = -1
   
    while True:
        alphavet_letter_index = 0
        first_letter = input_string[:1]
       
        # Find first letter alphabet index
        while alphavet_letter_index < len(alph_order):
            if first_letter == alph_order[alphavet_letter_index]:
                current_letter_index = alphavet_letter_index
                break
            else:
                alphavet_letter_index += 1
             
        # Check if result is empty - if it is first iteration
        if not len(result):
            # Take first letter and store it as a streak
            streak = input_string[:1]
           
            # Store current result
            result = streak
           
            # Store letter index
            previous_letter_index = current_letter_index
        else:  
            # Streak is not empty, grab first letter and check if that letter is next in the alphabet
            if (
               ( current_letter_index >= previous_letter_index + 1) or
               ( current_letter_index == previous_letter_index )
            ):
                streak += input_string[:1]
               
                # Store letter index
                previous_letter_index = current_letter_index
               
                # Check if result should be updated
                if len(streak) > len(result):
                    result = streak
            # End of a matching streak
            else:
                previous_letter_index = current_letter_index
               
                # Start a new streak
                streak = input_string[:1]              
       
        # Remove first letter from string
        input_string = input_string[1:]
       
        if not len(input_string):
            break

    return result
   
""" 
    This function is is using in build python string properties where strings can be directly compared
    This approach save one while loop
"""
def streakFinderV2(input_string : str) -> str:
    alph_order = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    streak = ""
    letter_to_compare = None

    while True:
        current_letter = input_string[:1]

        # Check if result is empty - if it is first iteration
        if not len(result):
            # Take first letter and store it as a streak
            streak = current_letter
           
            # Store current result
            result = streak
           
            # Store letter for comparison
            letter_to_compare = current_letter
        else:  
            # Streak is not empty, grab first letter and check if that letter is next in the alphabet
            if (
               ( current_letter >= letter_to_compare) or
               ( current_letter == letter_to_compare )
            ):
                streak += current_letter
               
                # Store letter for comparison
                letter_to_compare = current_letter
               
                # Check if result should be updated
                if len(streak) > len(result):
                    result = streak

            # End of a matching streak
            else:
                letter_to_compare = current_letter
               
                # Start a new streak
                streak = current_letter

        # Remove first letter from string
        input_string = input_string[1:]

        if not len(input_string):
            break

    return result

index = 0  
for input_string in tests:
    # result = streakFinder(input_string)
    result = streakFinderV2(input_string)
    if result == expected_results[index]:
        print("For input " + input_string + " longest streak was " + result)
    else:
        print("Incorrect result for " + input_string + " Received: " + result + " Expected to get: " + expected_results[index])
    index += 1
    print('')