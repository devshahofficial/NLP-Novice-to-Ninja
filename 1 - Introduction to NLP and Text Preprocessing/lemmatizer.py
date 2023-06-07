import spacy


def lemmatizer(text):
    """
    Lemmatize the input text using Spacy.

    Args:
        text (str): The input text to be lemmatized.

    Returns:
        str: The lemmatized text.
    """
    # Load the English language model in Spacy
    nlp = spacy.load('en_core_web_sm')

    # Process the text
    doc = nlp(text)

    # Lemmatize each token and join them back into a single string
    lemmatized_text = ' '.join([token.lemma_ for token in doc])

    return lemmatized_text
