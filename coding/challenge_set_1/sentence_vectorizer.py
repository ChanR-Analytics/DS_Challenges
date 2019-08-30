# Problem 2 Solution
import numpy as np
import pandas as pd
from scipy.stats import mode
import string

def wordVectorizer(sentence: str):
    # Remove Punctuation
    sentence = sentence.lower().translate(sentence.maketrans('', '', string.punctuation))
    # Create a list of the words in the sentence and remove whitespace
    words = sentence.strip().split(" ")
    # Tokenize the words in the list
    vector = {i: words.count(i) for i in words}
    # Create an array of the word frequencies
    vectorArr = np.array(list(vector.values())).astype(np.int32)
    # Generate the summary statistics
    mean = vectorArr.mean()
    median = np.median(vectorArr)
    s_mode = mode(vectorArr)[0][0]
    range = vectorArr.max() - vectorArr.min()
    std = vectorArr.std()
    variance = np.var(vectorArr)
    # Create a list of the summary stats
    stats = [mean, median, s_mode, range, std, variance]
    return stats

frameDict = {}
frameList = []
count = 0
while count < 10:
    sentence = input("Put in a sentence: ")
    frameDict[f"Sentence {count + 1}"] = wordVectorizer(sentence)
    frameDF = pd.DataFrame.from_dict(frameDict)
    frameList.append(frameDF)
    count += 1
    
finalDF = frameList[-1].T
finalDF.columns = ['mean', 'median', 'mode', 'range', 'standard deviation', 'variance']
finalDF.to_csv("coding/challenge_set_1/results.csv", index=False)
