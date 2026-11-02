def count_words(text):
    return len(text.split())


def reverse_text(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    return count


def make_title(text):
    return text.title()
