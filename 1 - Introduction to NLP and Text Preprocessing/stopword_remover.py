import spacy


def stopword_remover(text):
    """
    Remove stopwords from the input text using Spacy's built-in stopword list.

    Args:
        text (str): The input text to remove stopwords from.

    Returns:
        str: The text with stopwords removed.
    """
    # Load the English language model in Spacy
    nlp = spacy.load('en_core_web_sm')

    # Process the text
    doc = nlp(text)

    # Remove the stopwords from the text
    stopwords_removed = ' '.join([token.text for token in doc if not token.is_stop])

    return stopwords_removed
