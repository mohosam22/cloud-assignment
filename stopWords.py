import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
if

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()

    words = re.findall(r'\b\w+\b', text)

    # Custom stop words list with additional words
    custom_stop_words = set(stopwords.words('english'))
    custom_stop_words.update(['customword1', 'customword2', 'customword3'])

    filtered_words = [word for word in words if word not in custom_stop_words]

    # Using NLTK's Porter Stemmer for word stemming
    stemmer = nltk.stem.PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    word_freq = Counter(stemmed_words)

    return word_freq


def print_frequency_table(word_freq):
    print("Stemmed Word\t\tFrequency")  # Adjusted column header
    print("-----------------------------")  # Adjusted table separator
    for word, freq in word_freq.items():
        print(f"{word.ljust(20)}\t{freq}")  # Adjusted formatting


file_path = './paragraphs.txt'

word_freq = process_text(file_path)

print_frequency_table(word_freq)

