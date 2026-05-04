"""Output parsing demo.

This example shows how to ask for structured output and parse it locally.
"""

import json
import textwrap


def build_parsing_prompt(task: str) -> str:
    return textwrap.dedent(f"""
        You are a structured response assistant.
        Complete the task and return output in valid JSON format.

        TASK: {task}

        RESPONSE (JSON only):
    """)


def mock_model_output(task: str) -> str:
    if "shopping list" in task.lower():
        return json.dumps({"items": ["milk", "eggs", "bread"], "notes": "Buy fresh produce."}, indent=2)
    return json.dumps({"result": f"Simulated structured output for: {task}"}, indent=2)


def main() -> None:
    print("Output Parsing Demo")
    task = input("Task requiring structured output: ").strip()

    prompt = build_parsing_prompt(task)
    print("\n=== Built Prompt ===")
    print(prompt)

    response_text = mock_model_output(task)
    print("\n=== Simulated Model Response ===")
    print(response_text)

    try:
        parsed = json.loads(response_text)
        print("\n=== Parsed Output ===")
        print(parsed)
    except json.JSONDecodeError as exc:
        print("\nFailed to parse simulated response as JSON:", exc)


if __name__ == "__main__":
    main()
