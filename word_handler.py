
def get_words():
    with open ("./assets/wordlists/google-10000-english-no-swears.txt", "r") as f:
        words  = f.read().splitlines()

    return words
