def tokenizer(self, message, vocab):

    words = message.split()

    tokens = []

    for word in words:

        if word in vocab:

            tokens.append(vocab[word])

    return tokens

