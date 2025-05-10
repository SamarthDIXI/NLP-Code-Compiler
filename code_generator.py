def generate_code(parsed_tokens):
    tokens = [token.lower() for token in parsed_tokens]

    # Rule: If the instruction contains "print"
    if "print" in tokens:
        try:
            msg_index = tokens.index("print") + 1
            message = " ".join(parsed_tokens[msg_index:])
            return f'print("{message}")'
        except IndexError:
            return "# Error: Missing content after 'print'"

    # Rule: If the instruction contains "set X to Y"
    elif "set" in tokens and "to" in tokens:
        try:
            var_index = tokens.index("set") + 1
            val_index = tokens.index("to") + 1
            var_name = parsed_tokens[var_index]
            value = parsed_tokens[val_index]
            return f"{var_name} = {value}"
        except IndexError:
            return "# Error: Missing variable name or value in assignment"

    # Rule: If the instruction contains "if" and "else"
    elif "if" in tokens and "else" in tokens:
        try:
            condition_start = tokens.index("if") + 1
            condition_end = tokens.index("else")
            condition = " ".join(parsed_tokens[condition_start:condition_end]).strip()

            else_condition = " ".join(parsed_tokens[condition_end + 1:]).strip()

            return f"""
if {condition}:
    print("Condition is True")
else:
    print("{else_condition}")
"""
        except (IndexError, ValueError):
            return "# Error: Invalid 'if-else' syntax"

    # Rule: If the instruction contains "for" and "from-to"
    elif "for" in tokens and "from" in tokens and "to" in tokens:
        try:
            start_index = tokens.index("from") + 1
            end_index = tokens.index("to") + 1
            start_value = parsed_tokens[start_index]
            end_value = parsed_tokens[end_index]

            return f"""
for i in range({start_value}, {end_value} + 1):
    print(i)
"""
        except (IndexError, ValueError):
            return "# Error: Invalid 'for' loop syntax"

    # Rule: If the instruction contains "function" and "add"
    elif "function" in tokens and "add" in tokens:
        return (
            "def add(a, b):\n"
            "    return a + b\n"
            "print(add(3, 5))"
        )

    else:
        return "# Error: Unrecognized instruction"

