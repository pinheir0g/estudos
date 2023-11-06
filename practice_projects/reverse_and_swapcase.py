def reverse_and_swapcase(sentence):
    """Reverse and Swapcase of a string
    Receives a sentence, reverses the order of the words and swapcase of the letters.
    """
    sep_sentence = sentence.split()
    new_sentence = sep_sentence[::-1]

    new_sentence = " ".join(new_sentence).swapcase()

    return new_sentence

print(reverse_and_swapcase("fUN wonderful are"))
