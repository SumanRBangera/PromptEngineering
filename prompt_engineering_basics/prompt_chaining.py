"""Prompt chaining demo.

This example shows how to break a larger task into multiple prompts and chain the results.
"""

import textwrap


def build_first_prompt(task: str) -> str:
    return textwrap.dedent(f"""
        You are a planning assistant.
        Break the task into smaller steps.

        TASK: {task}

        Provide a list of steps to complete this task.
    """)


def build_second_prompt(task: str, steps: str) -> str:
    return textwrap.dedent(f"""
        You are an execution assistant.
        Use the plan below to generate a final result.

        TASK: {task}
        PLAN:
        {steps}

        RESPONSE:
    """)


def mock_planner(task: str) -> str:
    return f"1. Understand the task.\n2. Identify the key requirements.\n3. Produce a structured answer for: {task}."


def mock_executor(task: str, steps: str) -> str:
    return f"Final result for '{task}' using the plan:\n{steps}\n\nThis is a simulated chained output."


def main() -> None:
    print("Prompt Chaining Demo")
    task = input("Enter a task to chain, such as 'Write a short product description and a list of benefits': ").strip()

    first_prompt = build_first_prompt(task)
    print("\n=== First Prompt (Planning) ===")
    print(first_prompt)

    plan = mock_planner(task)
    print("\n=== Simulated Plan ===")
    print(plan)

    second_prompt = build_second_prompt(task, plan)
    print("\n=== Second Prompt (Execution) ===")
    print(second_prompt)

    final_response = mock_executor(task, plan)
    print("\n=== Simulated Final Response ===")
    print(final_response)


if __name__ == "__main__":
    main()
