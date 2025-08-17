def text_counter():
    text = input("Enter your text: ")
    word_count = len(text.split())
    char_count = len(text)
    
    import re
    sentence_count = len(re.findall(r'[.!?]', text))

    print("\nText Counter")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    print(f"Sentences: {sentence_count}")

text_counter()
