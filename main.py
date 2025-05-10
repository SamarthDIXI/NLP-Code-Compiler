import spacy
from code_generator import generate_code

nlp = spacy.load("en_core_web_sm")

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        return f"Error executing code: {str(e)}"
    return "Execution successful"

def main():
    print("Enter your instruction (or 'exit' to quit):")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break

        # Parse the instruction using Spacy NLP
        doc = nlp(user_input)
        tokens = [token.text for token in doc]

        print("\nParsed Tokens:", tokens)

        # Generate code based on parsed tokens
        code = generate_code(tokens)

        print("\nGenerated Code:")
        print(code)

        # Try executing the generated code and handle errors
        print("\n--- Execution Output ---")
        result = execute_code(code)
        print(result)
        print("------------------------\n")

if __name__ == "__main__":
    main()
