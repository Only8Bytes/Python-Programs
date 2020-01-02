import collections
import math

def load_corpus(path):
    lines = []
    corpus = []
    with open(path, "r") as txt:
        lines = txt.readlines()
    for count, line in enumerate(lines):
        pairs = line.split()
        sentence = []
        for pair in pairs:
            sentence.append(tuple(pair.split("=")))
        corpus.append(sentence)
    return corpus

class Tagger(object):

    def __init__(self, sentences):
        #initial tag probabilities
        initialTags = []
        for sentence in sentences:
            initialTags.append(sentence[0][1])
        self.InitialTagProbs = collections.Counter(initialTags)
        for tag in self.InitialTagProbs:
            self.InitialTagProbs[tag] = self.InitialTagProbs[tag]/len(sentences)
        #transition probabilities
        self.TagTransitions = {}
        for sentence in sentences:
            for count, pairs in enumerate(sentence):
                if count != len(sentence) - 1:
                    currentTag = pairs[1]
                    nextTag = sentence[count + 1][1]
                    if currentTag in self.TagTransitions:
                        if nextTag in self.TagTransitions[currentTag]:
                            self.TagTransitions[currentTag][nextTag] += 1
                        else:
                            self.TagTransitions[currentTag][nextTag] = 1
                    else:
                        self.TagTransitions[currentTag] = {}
                        self.TagTransitions[currentTag][nextTag] = 1
        for tag in self.TagTransitions:
            totalTransitions = sum(self.TagTransitions[tag].values())
            for nextTag in self.TagTransitions[tag]:
                self.TagTransitions[tag][nextTag] = self.TagTransitions[tag][nextTag]/totalTransitions
        #emission probabilities
        self.TagEmissions = {}
        self.TokenProbs = {}
        for sentence in sentences:
            for pairs in sentence:
                tag = pairs[1]
                token = pairs[0]
                if tag in self.TagEmissions:
                    if token in self.TagEmissions[tag]:
                        self.TagEmissions[tag][token] += 1
                    else:
                        self.TagEmissions[tag][token] = 1
                else:
                    self.TagEmissions[tag] = {}
                    self.TagEmissions[tag][token] = 1
                if token in self.TokenProbs:
                    if tag in self.TokenProbs[token]:
                        self.TokenProbs[token][tag] += 1
                    else:
                        self.TokenProbs[token][tag] = 1
                else:
                    self.TokenProbs[token] = {}
                    self.TokenProbs[token][tag] = 1
        for tag in self.TagEmissions:
            totalEmissions = sum(self.TagEmissions[tag].values())
            for token in self.TagEmissions[tag]:
                self.TagEmissions[tag][token] = self.TagEmissions[tag][token]/totalEmissions
        for token in self.TokenProbs:
            occurrences = sum(self.TokenProbs[token].values())
            for tag in self.TokenProbs[token]:
                self.TokenProbs[token][tag] = self.TokenProbs[token][tag]/occurrences

    def most_probable_tags(self, tokens):
        tagList = []
        for token in tokens:
            highestProb = 0
            highestTag = ""
            for tag in self.TagEmissions:
                if token in self.TagEmissions[tag]:
                    if self.TagEmissions[tag][token] > highestProb:
                        highestProb = self.TagEmissions[tag][token]
                        highestTag = tag
            tagList.append(highestTag)
        return tagList

    def viterbi_tags(self, tokens):
        tokenProbs = {}
        trellis = {}
        #initialize token probabilities
        for token in tokens:
            if token in self.TokenProbs:
                tokenProbs[token] = self.TokenProbs[token]

        prevToken = None
        #eliminate all but highest probability paths
        for token in tokens:
            trellis[token] = {}
            if prevToken:
                #any token after the first
                for tag in tokenProbs[token]:
                    tokenTagProb = math.log(self.TagEmissions[tag][token])
                    maxProb = None
                    maxPrevTag = None
                    #get max value P(tag_i-1) * P(token_i-1 | tag_i-1) * P(tag_i | tag_i-1) of all previous tags
                    for prevTag in trellis[prevToken]:
                        if maxProb:
                            val = trellis[prevToken][prevTag][0] + math.log(self.TagTransitions[prevTag][tag])
                            if val > maxProb:
                                maxProb = val
                                maxPrevTag = prevTag
                        else:
                            maxProb = trellis[prevToken][prevTag][0] + math.log(self.TagTransitions[prevTag][tag])
                            maxPrevTag = prevTag
                    trellis[token][tag] = (tokenTagProb + maxProb, maxPrevTag, prevToken)
            else:
                #first token
                for tag in tokenProbs[token]:
                    trellis[token][tag] = (math.log(self.InitialTagProbs[tag]) + math.log(self.TagEmissions[tag][token]), None, None)
            prevToken = token

        #back trace to find most probable path
        tags = []
        maxProb = None
        for tag in trellis[tokens[len(tokens) - 1]]:
            if not maxProb:
                maxProb = trellis[tokens[len(tokens) - 1]][tag]
                tags.append(tag)
            if maxProb and trellis[tokens[len(tokens) - 1]][tag][0] > maxProb[0]:
                maxProb = trellis[tokens[len(tokens) - 1]][tag]
                tags[0] = tag
        node = maxProb
        while node[1]:
            tags.insert(0, node[1])
            node = trellis[node[2]][node[1]]
        return tags