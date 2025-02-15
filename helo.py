def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  # Splitting text into words based on whitespace
    return len(words)

def get_user_input():
    """Handles user input and ensures it is not empty."""
    while True:
        text = input("Enter a sentence or paragraph: ").strip()
        if text:
            return text
        else:
            print("Error: No input provided. Please enter some text.")

def main():
    """Main function to execute the Word Counter program."""
    print("\n--- Welcome to the Word Counter Program ---\n")
    
    # Get valid user input
    text = get_user_input()
    
    # Count words
    word_count = count_words(text)
    
    # Display result with formatting
    print("\n--- Word Count Result ---")
    print(f"Total Words: {word_count}")
    print("-------------------------")

# Run the program
if __name__ == "__main__":
    main()