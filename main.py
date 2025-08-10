from apis.dummy_api import (
    summarize_text,
    correct_grammar,
    rewrite_tone,
    translate_text,
    generate_headline,
    extract_keywords
)
from utils.input_output import get_user_input, display_output
from utils.logger import log_interaction

def main():
    print("\n🤖 AI Content Assistant - Menu")
    while True:
        print("\nChoose an option:")
        print("1. Summarize Text")
        print("2. Grammar Correction")
        print("3. Rewrite Tone")
        print("4. Translate")
        print("5. Generate Headline")
        print("6. Extract Keywords")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            text = input("Enter text to summarize: ")
            response = summarize_text(text)

        elif choice == "2":
            text = input("Enter text to correct grammar: ")
            response = correct_grammar(text)

        elif choice == "3":
            text = input("Enter text to rewrite: ")
            tone = input("Enter tone (e.g., formal, funny): ")
            response = rewrite_tone(text, tone)

        elif choice == "4":
            text = input("Enter text to translate: ")
            lang = input("Enter language code (e.g., 'hi' for Hindi): ")
            response = translate_text(text, lang)

        elif choice == "5":
            text = input("Enter text for headline generation: ")
            response = generate_headline(text)

        elif choice == "6":
            text = input("Enter text to extract keywords from: ")
            response = extract_keywords(text)

        elif choice == "7":
            print("👋 Exiting Assistant.")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1–7.")
            continue

        display_output(response)
        log_interaction(choice, response)

if __name__ == "__main__":
    main()
