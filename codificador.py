import codecs



def codificador(password):
    Password= []
    for letter in password[0:]:
        letter=ord(letter)
        Password.append(letter)
    Hi = []
    for lette in Password:
        str(lette)
        Hi.append(lette)
    strings = [str(integer) for integer in Hi]
    a_string = "".join(strings)
    done = int(a_string)
    return done
