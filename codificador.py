import codecs




def codificador(password):
    return codecs.IncrementalEncoder(password)
