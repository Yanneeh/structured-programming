letters = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'x', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z']

def rot_n(str, n):
    encrypted = []

    str = str.lower()

    for letter in str:
        index = letters.index(letter)

        print(index)

        x = n

        while True:
            if x == 0:
                break
            else:
                if index == (len(letters)-1):
                    index = 0
                    x -= 1
                else:
                    index += 1
                    x -= 1

        encrypted.append(letters[index])


    return ''.join(encrypted)

# Test succesvol
# print(rot_n('hallo', 2))
# Output: jcnnx

# Test #2 succesvol
# print(rot_n('yannick', 2))
# Output: zboojdl
