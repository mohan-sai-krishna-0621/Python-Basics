
import os
import string
from collections import Counter

FILE_NAME = os.path.join(
    os.path.dirname(__file__),
    "sample.txt"
)


def read_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Error: sample.txt was not found.")
    except OSError as error:
        print(f"Error reading file: {error}")

    return None


def analyze_text(text):
    lines = text.splitlines()
    words = text.split()

    # Count characters, including spaces and newline characters
    characters = len(text)

    # Remove punctuation and normalize capitalization
    cleaned_words = [
        word.strip(string.punctuation).lower()
        for word in words
    ]

    # Ignore tokens containing no letters or digits
    cleaned_words = [
        word for word in cleaned_words
        if word and any(char.isalnum() for char in word)
    ]

    word_counts = Counter(cleaned_words)

    return lines, words, characters, word_counts


def display_report(lines, words, characters, word_counts):
    print("\n===== TEXT FILE ANALYSIS =====")
    print("Total lines:", len(lines))
    print("Total words:", len(words))
    print("Total characters:", characters)
    print("Unique words:", len(word_counts))

    if word_counts:
        highest_frequency = max(word_counts.values())

        print("\nMost frequent word(s):")

        for word, count in sorted(word_counts.items()):
            if count == highest_frequency:
                print(f"{word}: {count} times")
    else:
        print("\nNo words found in the file.")


def main():
    print("===== TEXT FILE ANALYZER =====")

    text = read_file()

    if text is None:
        return

    lines, words, characters, word_counts = analyze_text(text)

    display_report(lines, words, characters, word_counts)


if __name__ == "__main__":
    main()
