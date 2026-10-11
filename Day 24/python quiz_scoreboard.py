scores = {}


def add_score():
    name = input("Enter player name: ").strip()

    if not name:
        print("Player name cannot be empty!")
        return

    try:
        score = int(input("Enter quiz score (0-100): "))

        if score < 0 or score > 100:
            print("Score must be between 0 and 100!")
            return

        scores[name] = score
        print("Score added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_scores():
    if not scores:
        print("No scores available.")
        return

    print("\n===== ALL QUIZ SCORES =====")

    for name, score in scores.items():
        print(f"Player: {name} | Score: {score}")


def show_leaderboard():
    if not scores:
        print("No scores available.")
        return

    print("\n===== LEADERBOARD =====")

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for rank, (name, score) in enumerate(sorted_scores, start=1):
        print(f"{rank}. {name} - {score} points")


def show_top_scorer():
    if not scores:
        print("No scores available.")
        return

    highest_score = max(scores.values())

    print("\n===== TOP SCORER =====")

    for name, score in scores.items():
        if score == highest_score:
            print(f"{name} - {score} points")


def main():
    while True:
        print("\n===== QUIZ SCOREBOARD =====")
        print("1. Add Player Score")
        print("2. View All Scores")
        print("3. Show Leaderboard")
        print("4. Show Top Scorer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_score()

        elif choice == "2":
            view_scores()

        elif choice == "3":
            show_leaderboard()

        elif choice == "4":
            show_top_scorer()

        elif choice == "5":
            print("Thank you for using Quiz Scoreboard!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
