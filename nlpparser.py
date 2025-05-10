import spacy

nlp = spacy.load("en_core_web_sm")

def parse_instruction(instruction):
    doc = nlp(instruction.lower())

    # Rule: If verb is "print"
    if any(token.lemma_ == "print" for token in doc):
        quoted = instruction.lower().replace("print", "").strip()
        return f'print("{quoted}")'

    # Rule: If it starts with "set X to Y"
    if "set" in instruction.lower() and "to" in instruction.lower():
        parts = instruction.lower().split("to")
        if len(parts) == 2:
            var_name = parts[0].replace("set", "").strip()
            value = parts[1].strip()
            return f"{var_name} = {value}"

    # Rule: If the instruction mentions "function" and "add"
    if "function" in instruction.lower() and "add" in instruction.lower():
        return (
            "def add(a, b):\n"
            "    return a + b\n"
            "print(add(3, 5))"
        )

    return "# Sorry, I couldn't understand this instruction."

def main():
    print("Enter your instruction (type 'exit' to quit):")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break

        code = parse_instruction(user_input)
        print("\nGenerated Code:")
        print(code)

        print("\n--- Execution Output ---")
        try:
            exec(code)
        except Exception as e:
            print(f"Error while executing: {e}")
        print("------------------------\n")

if __name__ == "__main__":
    main()
