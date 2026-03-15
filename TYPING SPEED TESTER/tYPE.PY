import random
import time

def main():
    print("Welcome to the Typing Speed Tester!")
    answers = input("Type 'start' to start the test: ").strip().lower()
    if answers != "start":
        print("Invalid input.")
        return

    words = [
        "building", "a", "typing", "tester", "with", "random", "word",
        "placement", "makes", "a", "fun", "challenge", "for", "accuracy",
        "and", "speed", "practice", "every", "time", "you", "play"
    ]
    random.shuffle(words)
    sentence = " ".join(words)

    print("\nType this sentence exactly as shown:\n")
    print(sentence)
    print()

    start_time = time.time()
    user_input = input("Your input: ")
    end_time = time.time()

    elapsed_time = max(end_time - start_time, 1e-6)
    correct = user_input.strip() == sentence
    wpm = (len(sentence.split()) / elapsed_time) * 60

    print(f"\nElapsed time: {elapsed_time:.2f} seconds.")
    print(f"You typed the sentence correctly: {'Yes' if correct else 'No'}")
    print(f"Your typing speed is {wpm:.2f} words per minute.")

if __name__ == "__main__":
    main()