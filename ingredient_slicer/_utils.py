def _find_substring_indices(text: str, substring: str) -> list:

    """Find the start and end indices of a substring in a string
    Case insensitive, and will return all instances of the substring in the text string
    Args:
        text (str): The text to search for the substring
        substring (str): The substring to search for in the text
    Returns:
        list: A list of lists containing the start and end indices of the substring
    """

    text = text.lower()
    substring = substring.lower()

    substring_length = len(substring)

    L = 0
    substring_indices = []

    for R in range(0, len(text)):
        if R - L == substring_length:
            if text[L:R] == substring:
                substring_indices.append([L, R])
            L += 1
            
    return substring_indices

def _find_and_remove_hyphens_around_substring(text: str, substring: str, debug=False) -> str:

    """Find instances of a substring surrounded by some number of hyphens on the left or right of the substring and remove these hyphens
    Case insensitive, and will return the updated string with the hyphens removed from around the substring and in lower case
    Args:
        text (str): The text to search for the substring
        substring (str): The substring to search for in the text
        debug (bool, optional): Print debug information. Defaults to False.
    Returns:
        str: The updated text with the hyphens removed from around the substring
    """


    text = text.lower()
    substring = substring.lower().replace("-", "")

    substring_length = len(substring)

    L = 0
    substring_indices = []
    hypen_substrings = []

    for R in range(0, len(text)):

        if R - L == substring_length:
            print(f"text[L:R]: {text[L:R]}") if debug else None
            if text[L:R] == substring:
                substring_indices.append([L, R])
                
                has_left_hyphen = False
                has_right_hyphen = False

                # look LEFT of the matched substring
                GO_LEFT_INDEX = L - 1

                print(f"Try to go LEFT of '{substring}' substring") if debug else None
                while GO_LEFT_INDEX >= 0 and (text[GO_LEFT_INDEX] == " " or text[GO_LEFT_INDEX] == "-"):
                    print(f"GO_LEFT_INDEX: {GO_LEFT_INDEX}") if debug else None
                    print(f"text[GO_LEFT_INDEX]: {text[GO_LEFT_INDEX]}") if debug else None
                    if text[GO_LEFT_INDEX] == "-":
                        has_left_hyphen = True
                    GO_LEFT_INDEX -= 1
                print()

                # look RIGHT of the matched substring
                print(f"Try to go RIGHT of '{substring}' substring") if debug else None
                GO_RIGHT_INDEX = R + 1

                while GO_RIGHT_INDEX < len(text) and (text[GO_RIGHT_INDEX] == " " or text[GO_RIGHT_INDEX] == "-"):
                    print(f"GO_RIGHT_INDEX: {GO_RIGHT_INDEX}") if debug else None
                    print(f"text[GO_RIGHT_INDEX]: {text[GO_RIGHT_INDEX]}") if debug else None
                    if text[GO_RIGHT_INDEX] == "-":
                        has_right_hyphen = True
                    GO_RIGHT_INDEX += 1

                look_around_string = text[GO_LEFT_INDEX+1:GO_RIGHT_INDEX]

                if has_left_hyphen or has_right_hyphen:
                    hypen_substrings.append(look_around_string)
                    print(f"Added '{look_around_string}' to hypen_substrings:\n > '{hypen_substrings}'") if debug else None

                print(f"FINAL --> GO_LEFT_INDEX: {GO_LEFT_INDEX} --> has LEFT hypen: {has_left_hyphen}") if debug else None
                print(f"FINAL --> GO_RIGHT_INDEX: {GO_RIGHT_INDEX} --> has RIGHT hypen: {has_right_hyphen}") if debug else None
                print(f"Final substring: '{look_around_string}'") if debug else None

            print(f"Incrementing L from {L} to {L + 1}") if debug else None
            L += 1
        print(f"----" * 5) if debug else None
        print() if debug else None
    
    print(f"hypen_substrings: {hypen_substrings}") if debug else None
    
    for hyphen_substring in hypen_substrings:
        replacement_string = f" {hyphen_substring.replace('-', '').replace(' ', '')} " 
        text = text.replace(hyphen_substring, replacement_string) 
        print(f"Replacing '{hyphen_substring}' in 'text' with '{replacement_string}'\n") if debug else None

    text = text.strip()

    return text