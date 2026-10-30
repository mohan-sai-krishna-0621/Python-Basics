
import string
from collections import Counter


def get_text():
    text = input("Enter a sentence or paragraph: ")
    return text


def clean_text(text):
    text = text.lower()

    # Replace punctuation with spaces
    for character in string.punctuation:
        text = text.replace(character, " ")

    return text


def count_words(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    word_counts = Counter(words)

    return words, word_counts


def display_results(words, word_counts):
    if not words:
        print("No words were entered.")
        return

    print("\n===== WORD FREQUENCY REPORT =====")
    print("Total words:", len(words))
    print("Unique words:", len(word_counts))

    print("\nWord counts (highest first):")

    for word, count in sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    ):
        print(f"{word}: {count}")

    most_common_word, frequency = word_counts.most_common(1)[0]

    print("\nMost frequent word:", most_common_word)
    print("Frequency:", frequency)


def main():
    print("===== WORD FREQUENCY COUNTER =====")

    text = get_text()
    words, word_counts = count_words(text)

    display_results(words, word_counts)


if __name__ == "__main__":
    main()
