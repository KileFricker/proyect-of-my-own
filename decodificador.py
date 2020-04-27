import codecs




def codificador(password):
    return codecs.IncrementalDecoder(password)
