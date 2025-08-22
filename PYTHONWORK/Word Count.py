def text_counter():
    while True:
        name = input("Enter your name here: ")
        print(f"\nHello {name}, you're welcome to the Text Counter App")
        print("\nThis app helps you count word, characters and sentences")

        text = input("\nEnter your text: ")
        word_count = len(text.split())
        char_count = len(text)
    
        import re
        sentence_count = len(re.findall(r'[.!?]', text))

        print("\nText Counter")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
        print(f"Sentences: {sentence_count}")

        
        # Ask if user wants to continue
        try_again = input("\n Do you want to calculate again? (yes/no): ").strip().lower()
        if try_again != "yes":
            print("Thank You for using the Text Counter App!")
            break
        
text_counter()
