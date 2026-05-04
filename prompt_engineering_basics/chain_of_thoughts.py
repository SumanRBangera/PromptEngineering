import textwrap
import re


def build_cot_prompt(question: str) -> str:
    prompt = textwrap.dedent(f"""
        You are a reasoning assistant.
        Answer the question and show your thought process step by step.

        Question: {question}

        Answer with reasoning:
    """)
    return prompt


def mock_model(question: str) -> str:
    numbers = [int(num) for num in re.findall(r"-?\d+", question)]
    if len(numbers) >= 2 and any(op in question for op in ["plus", "minus", "times", "divided"]):
        a, b = numbers[0], numbers[1]
        if "plus" in question:
            result = a + b
            return f"Step 1: Identify the numbers {a} and {b}.\nStep 2: Add them together: {a} + {b} = {result}.\nAnswer: {result}."
        if "minus" in question:
            result = a - b
            return f"Step 1: Identify the numbers {a} and {b}.\nStep 2: Subtract: {a} - {b} = {result}.\nAnswer: {result}."
        if "times" in question or "multiply" in question:
            result = a * b
            return f"Step 1: Identify the numbers {a} and {b}.\nStep 2: Multiply: {a} * {b} = {result}.\nAnswer: {result}."
        if "divided" in question or "divide" in question:
            if b != 0:
                result = a / b
                return f"Step 1: Identify the numbers {a} and {b}.\nStep 2: Divide: {a} / {b} = {result}.\nAnswer: {result}."
    return "Step 1: Read the question carefully.\nStep 2: Think about the best way to answer it.\nStep 3: Provide the final answer.\nAnswer: This is a simulated chain-of-thought response."


def main() -> None:
    print("Chain-of-Thought Prompting Demo")
    question = input("Enter a question (e.g. 'What is 12 plus 7?' or 'How should I prepare for a presentation?'): ").strip()

    prompt = build_cot_prompt(question)
    print("\n=== Built Prompt ===")
    print(prompt)

    response = mock_model(question)
    print("\n=== Simulated Chain-of-Thought Response ===")
    print(response)


if __name__ == "__main__":
    main()
