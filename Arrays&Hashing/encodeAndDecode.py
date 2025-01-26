def encode(strings: list[str]) -> str: 
    """
    Encodes a list of string into a single string that can be decoded
    """
    encodedStr = ""
    
    for string in strings: 
        # Get the length of the string to determine how many characters it has
        strLength = len(string)
        strEncoding = str(strLength) + "#"
        encodedStr += strEncoding + string
        
    return encodedStr

def decode(encodedStr: str) -> list[str]: 
    """
    Decodes an encoded string into a list of individual strings
    """ 
    # The first two character will always say how far to go first
    stoppingIdx = int(encodedStr[0]) + 2
    decodedStr = "" 
    onDelimiter = False 
    decoding = []

    for i in range(2, len(encodedStr)): 
        if(i == stoppingIdx): 
            stoppingIdx = i + int(encodedStr[i]) + 2
            onDelimiter = True
            decoding.append(decodedStr)
            decodedStr = ""
        elif(onDelimiter):
            onDelimiter = False 
        else: 
            decodedStr += encodedStr[i]
            onDelimiter = False 
    decoding.append(decodedStr)

    return decoding 


    
strings = ["why", "hel6#lo", "there"]
print("Encoding ['why', 'hel6#lo', 'there']")
print("Result:", encode(strings))

encodedStr = encode(strings)
print("Decoding 3#why7#hel6#lo5#there")
print("Result:", decode(encodedStr))