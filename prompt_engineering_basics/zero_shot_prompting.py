import textwrap


def build_zero_shot_prompt(task_description: str, user_input: str) -> str:
    prompt = textwrap.dedent(f"""
        You are a helpful assistant.
        Use the instructions below to complete the task.

        TASK:
        {task_description}

        INPUT:
        {user_input}

        RESPONSE:
    """)
    return prompt


def mock_model(prompt: str) -> str:
    if "translate" in prompt.lower():
        return "This is a simulated translation response."
    if "summarize" in prompt.lower():
        return "This is a simulated summary of the input text."
    return "This is a simulated zero-shot response based on the prompt."


def main() -> None:
    print("Zero-Shot Prompting")
    print("Enter a short task description, e.g. translate English to Spanish, summarize text, or classify sentiment.")
    task_description = input("Task description: ").strip()
    user_input = input("Input text: ").strip()

    prompt = build_zero_shot_prompt(task_description, user_input)
    print("\n=== Built Prompt ===")
    print(prompt)

    response = mock_model(prompt)
    print("\n=== Simulated Model Response ===")
    print(response)


if __name__ == "__main__":
    main()
