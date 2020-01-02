import string
import re
import random
import math

def tokenize(text):
    punct = r'[\s{}]'.format(re.escape(string.punctuation))
    result = re.split("("+punct+")", text)
    result = list(filter(lambda a: a != " " and a != "", result))
    return result

def ngrams(n, tokens):
    result = []
    for i, token in enumerate(tokens):
        context = []
        for j in range(n - 1):
            if i - j - 1 < 0:
                context.insert(0, "<START>")
            else:
                context.insert(0, tokens[i - j - 1])
        result.append((tuple(context), token))
    #<END>
    context = []
    for i in range(n - 1):
        if len(tokens) - 1 - i < 0:
            context.insert(0, "<START>")
        else:
            context.insert(0, tokens[len(tokens) - 1 - i])
    result.append((tuple(context), "<END>"))
    return result

class NgramModel(object):

    def __init__(self, n):
        self.Order = n
        self.NGrams = {}
        self.Vocab = {}

    def update(self, sentence):
        result = ngrams(self.Order, tokenize(sentence))
        for x in result:
            if x[0] in self.Vocab:
                self.Vocab[x[0]] += 1
            else:
                self.Vocab[x[0]] = 1
                self.NGrams[x[0]] = {}
            if x[1] in self.NGrams[x[0]]:
                self.NGrams[x[0]][x[1]] += 1
            else:
                self.NGrams[x[0]][x[1]] = 1

    def prob(self, context, token):
        occurrences = self.NGrams[context][token] if token in self.NGrams[context] else 0
        return occurrences/self.Vocab[context]

    def random_token(self, context):
        r = random.random()
        tokens = list(self.NGrams[context].keys())
        tokens = sorted(tokens, key = lambda a: self.NGrams[context][a])
        count = 0
        for token in tokens:
            probability = self.prob(context, token)
            if count + probability > r:
                return token
            count += probability

    def random_text(self, token_count):
        result = ""
        context = tuple(["<START>"] * (self.Order - 1)) 
        for i in range(token_count):
            token = self.random_token(context)
            if token == "<END>":
                context = tuple(["<START>"] * (self.Order - 1))
            elif self.Order > 1:
                context = tuple(list(context)[1:] + [token])
            if result != "":
                result = result + " " + token
            else:
                result = token
        return result

    def perplexity(self, sentence):
        result = ngrams(self.Order, tokenize(sentence))
        perplex = 0
        for ngram in result:
            perplex += math.log((1/self.prob(ngram[0], ngram[1])))
        perplex = math.exp(perplex)
        perplex = pow(perplex, 1/len(result))
        return perplex

def create_ngram_model(n, path):
    txtfile = open(path, "r")
    model = NgramModel(n)
    for line in txtfile.readlines():
        model.update(line)
    return model
