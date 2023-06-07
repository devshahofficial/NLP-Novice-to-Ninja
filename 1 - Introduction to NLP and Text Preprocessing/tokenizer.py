import spacy


def tokenizer(text):
    """
    Tokenize the input text using Spacy.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list: A list of tokens extracted from the text.
    """
    # Load the English language model in Spacy
    nlp = spacy.load('en_core_web_sm')

    # Tokenize the text
    doc = nlp(text)

    # Extract the tokens from the document
    tokens = [token.text for token in doc]

    return tokens
