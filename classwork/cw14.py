def find_missing_letter(chars):
    for i in range(len(chars) - 1):  # Loop through the given list
        if ord(chars[i + 1]) != ord(chars[i]) + 1:  # Check if the next letter is missing
            return chr(ord(chars[i]) + 1)  # Return the missing letter
