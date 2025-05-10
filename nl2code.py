def parse_natural_language(instruction):
    instruction = instruction.lower()

    if instruction.startswith("print"):
        content = instruction.replace("print", "", 1).strip()
        return f'print("{content}")'

    elif instruction.startswith("set"):
        parts = instruction.split("to")
        if len(parts) == 2:
            var_name = parts[0].replace("set", "").strip()
            value = parts[1].strip()
            return f"{var_name} = {value}"
        else:
            return "# Error: Invalid assignment format"

    elif "function" in instruction and "add" in instruction:
        return (
            "def add(a, b):\n"
            "    return a + b\n"
            "print(add(3, 5))"
        )

    elif "print numbers from" in instruction:
        # e.g., "Print numbers from 1 to 5"
        parts = instruction.split("from")[1].strip().split("to")
        if len(parts) == 2:
            start = parts[0].strip()
            end = str(int(parts[1].strip()) + 1)  # Python is exclusive in range
            return f"for i in range({start}, {end}):\n    print(i)"

    else:
        return "# Error: Unsupported instruction"


def main():
    print("Enter your instruction (type 'exit' to quit):")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break

        code = parse_natural_language(user_input)
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
