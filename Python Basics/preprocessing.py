def process(sentences):
    result = []
    result = [i for i in [' '.join(word for word in k.split() if word.isalpha()) for k in sentences]]
    return result
