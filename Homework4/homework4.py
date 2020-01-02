import email
import math
import collections
import os
import operator
import copy

############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):
    message = email.message_from_file(open(email_path, encoding="utf8"))
    tokens = []
    for x in list(email.iterators.body_line_iterator(message)):
        for y in x.split():
            tokens.append(y)
    return tokens

def log_probs(email_paths, smoothing):
    probabilities = {}
    vocabulary = {}
    totalWords = 0
    combined = []
    for path in email_paths:
        tokens = load_tokens(path)
        totalWords += len(tokens)
        combined = combined + tokens
    vocabulary = collections.Counter(combined)
    denominator = totalWords + smoothing * (len(vocabulary) + 1)
    for key, val in vocabulary.items():
        probabilities[key] = math.log((val + smoothing)/denominator)
    probabilities["<UNK>"] = math.log(smoothing/denominator)

    return probabilities

class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        #this is slow but it's apparently not an issue according to piazza answers
        #takes around 15 seconds sometimes
        spamFiles = [name for name in os.listdir(spam_dir)]
        hamFiles = [name for name in os.listdir(ham_dir)]
        self.hamProbDict = log_probs([ham_dir+"/"+i for i in hamFiles], smoothing)
        self.spamProbDict = log_probs([spam_dir+"/"+i for i in spamFiles], smoothing)
        self.spamProb = len(spamFiles)/(len(spamFiles) + len(hamFiles))
        self.hamProb = 1 - self.spamProb
    
    def is_spam(self, email_path):
        tokens = load_tokens(email_path)
        spamValue = math.log(self.spamProb)
        hamValue = math.log(self.hamProb)
        vocabulary = collections.Counter(tokens)
        for token, occurrences in vocabulary.items():
            if token in self.spamProbDict:
                spamValue += self.spamProbDict[token]*occurrences
            else:
                spamValue += self.spamProbDict["<UNK>"]*occurrences
            if token in self.hamProbDict:
                hamValue += self.hamProbDict[token]*occurrences
            else:
                hamValue += self.hamProbDict["<UNK>"]*occurrences
        return spamValue >= hamValue

    def getIndicativeValues(self, reversed, n):
        indicativeValues = copy.deepcopy(self.spamProbDict)
        for key in indicativeValues.keys():
            if key in self.hamProbDict and key != "<UNK>":
                indicativeValues[key] = math.log(math.exp(self.spamProbDict[key])/(self.spamProb * math.exp(self.spamProbDict[key]) + self.hamProb * math.exp(self.hamProbDict[key])))
            else:
                indicativeValues[key] = 0
        indicativeValues = sorted(indicativeValues.items(), key = operator.itemgetter(1), reverse = reversed)
        keyList = []
        for i in range(n):
            keyList.append(indicativeValues[i][0])
        return keyList

    def most_indicative_spam(self, n):
        return self.getIndicativeValues(True, n)

    def most_indicative_ham(self, n):
        return self.getIndicativeValues(False, n)
