from typing import List, Sequence, Dict
from collections import Counter
import re


# Question 1

def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:
    num_days = len(p)
    list_prob = [0] * (num_days + 1)
    list_prob[0] = 1

    # Dynamic programming approach to calculate probability
    for prob in p:
        for k in range(num_days, 0, -1):
            list_prob[k] = list_prob[k] * (1 - prob) + list_prob[k - 1] * prob
        list_prob[0] *= (1 - prob)

    return sum(list_prob[n + 1:])

p = [0.35] * 365  # Assuming a constant probability of 0.3 for simplicity
n = 120

prob = prob_rain_more_than_n(p, n)
print(f"The probability of raining more than {n} days is {prob:.3f}")


# Example pronunciation dictionary
phonemes_dict = {
    "ABACUS": ["AE", "B", "AH", "K", "AH", "S"],
    "BOOK": ["B", "UH", "K"],
    "THEIR": ["DH", "EH", "R"],
    "THERE": ["DH", "EH", "R"],
    "TOMATO": ["T", "AH", "M", "AA", "T", "OW"],
    "TOMATO_ALT": ["T", "AH", "M", "EY", "T", "OW"]
}

def preprocess_pronunciation_dict(pron_dict: Dict[str, List[str]]) -> Dict[str, List[str]]:
    phoneme_to_words = {}
    for word, phonemes in pron_dict.items():
        phoneme_str = ' '.join(phonemes)
        if phoneme_str not in phoneme_to_words:
            phoneme_to_words[phoneme_str] = []
        phoneme_to_words[phoneme_str].append(word)
    return phoneme_to_words

phoneme_to_words = preprocess_pronunciation_dict(phonemes_dict)

def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> List[List[str]]:
    phoneme_str = ' '.join(phonemes)
    possible_seq = []

    def backtrack(start: int, path: List[str]):
        if start == len(phonemes):
            possible_seq.append(path.copy())
            return

        for end in range(start + 1, len(phonemes) + 1):
            sub_phoneme_str = ' '.join(phonemes[start:end])
            if sub_phoneme_str in phoneme_to_words:
                for w in phoneme_to_words[sub_phoneme_str]:
                    path.append(w)
                    backtrack(end, path)
                    path.pop()

    backtrack(0, [])
    return possible_seq

example_phonemes = ["DH", "EH", "R", "DH", "EH", "R"]
print(find_word_combos_with_pronunciation(example_phonemes))


# Question 3
def find_frequent_words(path: str, n: int) -> List[str]:
    # Read the file contents
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Tokenize the text into words, using regex to handle punctuation and spaces
    w = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_count = Counter(w)

    # Find the n most common words
    common_words = word_count.most_common(n)

    # Extract only the words (without their counts)
    frequent_words = [word for word, count in common_words]

    return frequent_words

data_path = 'shakespeare.txt'  # Replace with the actual path to the dataset
n = 10
frequent_words = find_frequent_words(data_path, n)
print(frequent_words)
