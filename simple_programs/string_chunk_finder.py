tests = [
    'abcdefghijklmnopqrstuvwxyz',
    'abcabcd'
]

expected_results = [
    'abcdefghijklmnopqrstuvwxyz',
    'abcd'
]

def streakFinder(input_string : str) -> str:
    template_order = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    starting_point = 0
    characters_counter = 0

    while characters_counter <= len(input_string):
        characters_counter += 1
    
        for starting_point in range(len(input_string)):
            chunk = input_string[ starting_point : starting_point + characters_counter ]
            if characters_counter == len(chunk):
                # Find chunk in alphabet
                for x in range(len(template_order)):
                    alphabet_chunk = template_order[x : x+characters_counter]
                    
                    if alphabet_chunk == chunk and len(chunk) > len(result):
                        result = alphabet_chunk

    return result
   
   
index = 0  
for input_string in tests:
    result = streakFinder(input_string)
    if result == expected_results[index]:
        print("For input " + input_string + " longest string was " + result)
    else:
        print("Incorrect result for " + input_string + " Received: " + result + " Expected to get: " + expected_results[index])
    index += 1