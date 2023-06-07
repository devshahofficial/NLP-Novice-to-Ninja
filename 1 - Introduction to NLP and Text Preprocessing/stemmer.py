from nltk.stem import PorterStemmer


def stemmer(text):
    """
    Perform stemming on the input text using the Porter stemming algorithm.

    Args:
        text (str): The input text to be stemmed.

    Returns:
        str: The stemmed text.
    """
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()

    # Tokenize the text
    tokens = text.split()

    # Stem each token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Join the stemmed tokens back into a single string
    stemmed_text = ' '.join(stemmed_tokens)

    return stemmed_text
