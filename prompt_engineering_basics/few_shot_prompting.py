import textwrap


def build_few_shot_prompt(examples: list[tuple[str, str]], new_input: str) -> str:
    example_text = "\n\n".join(
        f"Example {i+1}:\nInput: {inp}\nOutput: {out}" for i, (inp, out) in enumerate(examples)
    )
    prompt = textwrap.dedent(f"""
        You are a helpful assistant.
        Use the examples below to answer the next question.

        {example_text}

        Now answer this:
        Input: {new_input}
        Output:
    """)
    return prompt


def mock_model(prompt: str, examples: list[tuple[str, str]], new_input: str) -> str:
    """
    Improved mock model that analyzes examples and generates contextual responses.
    """
    # Simple pattern detection: look at the relationship between examples
    if len(examples) >= 2:
        # Check if it's a translation pattern (common transformation)
        example_pairs = [(e[0].lower(), e[1].lower()) for e in examples]
        
        # For demonstration, generate a response based on the pattern
        # In a real scenario, this would be an actual LLM
        if any("hello" in e[0].lower() for e in examples):
            # Translation pattern detected
            if "good morning" in new_input.lower():
                return "Buenos días"
            elif "good" in new_input.lower():
                return "Bueno"
    
    # Default intelligent response
    if "translate" in prompt.lower():
        return "Simulated translation response based on the pattern shown."
    if "summarize" in prompt.lower():
        return "Simulated summary following the provided examples."
    return "Simulated response following the pattern from examples."


def main() -> None:
    print("Few-Shot Prompting Demo")
    print("This script uses a few examples, then asks for a new input to continue the pattern.")
    example_count = 2
    examples = []
    for i in range(example_count):
        inp = input(f"Example {i+1} input: ").strip()
        out = input(f"Example {i+1} output: ").strip()
        examples.append((inp, out))
        print()

    new_input = input("New input to continue the pattern: ").strip()

    prompt = build_few_shot_prompt(examples, new_input)
    print("\n=== Built Prompt ===")
    print(prompt)

    response = mock_model(prompt, examples, new_input)
    print("\n=== Simulated Model Response ===")
    print(response)


if __name__ == "__main__":
    main()
