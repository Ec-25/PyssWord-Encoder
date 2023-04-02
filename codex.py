"""
Module of Encode & Decode Strings
Each encrypted password is unique, its security is based on the length and the difference between each character
"""

RANGE = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237]


def encode(decoded: str) -> str:
    """
    This function takes a string as input to encode and make its content unreadable, returning another encoded string.
    """
    universal = ""
    univEven = ""
    univOdd = ""
    if len(decoded) != 0:
        for char in range(len(decoded)):
            # initial params
            ascii = ord(decoded[char])
            indx = RANGE.index(ascii)

            # modded by evens
            if char % 2 == 0:
                indx += len(decoded)
            else:
                indx -= len(decoded)

            # check position
            if indx < 0:
                indx = indx + len(RANGE)
            elif indx > 152:
                indx = indx - len(RANGE)

            # new character
            nwAscii = RANGE[indx]
            nwAscii = chr(nwAscii)

            # save by evens
            if char % 2 == 0:
                univEven += nwAscii
            else:
                univOdd += nwAscii

    universal += (univOdd + univEven)

    return universal


def decode(encoded: str) -> str:
    """
    This function takes an already encoded string as input, and returns another decoded string with its plain text.
    """

    universal = ""
    univEven = ""
    univOdd = ""
    nwUnivEven = ""
    nwUnivOdd = ""

    if len(encoded) != 0:
        if len(encoded) % 2 == 0:
            # means that there are the same number of even numbers and odd numbers
            mid = len(encoded) // 2
            univOdd = encoded[:mid]
            univEven = encoded[mid:]

        else:
            mid = (len(encoded) // 2)
            univOdd = encoded[:mid]
            univEven = encoded[mid:]

        for i in range(len(univEven)):
            # initial params
            ascii = ord(univEven[i])
            indx = RANGE.index(ascii)

            # unmodded
            indx -= len(encoded)

            # check position
            if indx < 0:
                indx = indx + len(RANGE)
            elif indx > 152:
                indx = indx - len(RANGE)

            # old params
            odAscii = RANGE[indx]
            char = chr(odAscii)

            # add in var
            nwUnivEven += char

        for j in range(len(univOdd)):
            # initial params
            ascii = ord(univOdd[j])
            indx = RANGE.index(ascii)

            # unmodded
            indx += len(encoded)

            # check position
            if indx < 0:
                indx = indx + len(RANGE)
            elif indx > 152:
                indx = indx - len(RANGE)

            # old params
            odAscii = RANGE[indx]
            char = chr(odAscii)

            # add in var
            nwUnivOdd += char

    # bind
    x = 0
    y = 0
    for k in range(len(encoded)):
        if k % 2 == 0:
            universal += nwUnivEven[x]
            x += 1

        else:
            universal += nwUnivOdd[y]
            y += 1

    return universal
