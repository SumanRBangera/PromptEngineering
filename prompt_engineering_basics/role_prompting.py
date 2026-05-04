"""Role prompting demo.

This example shows how to assign a role to the assistant and customize output style.
"""

import textwrap


def build_role_prompt(role: str, request: str) -> str:
    prompt = textwrap.dedent(f"""
        You are an assistant acting as a {role}.
        Speak in the tone and style that fits this role.

        Request: {request}

        Response:
    """)
    return prompt


def mock_model(role: str, request: str) -> str:
    if role.lower() == "teacher":
        return "As a teacher, I would explain the concept clearly, step by step, using simple examples."
    if role.lower() == "chef":
        return "As a chef, I recommend fresh ingredients, balanced flavors, and timing the steps carefully."
    if role.lower() == "salesperson":
        return "As a salesperson, I would highlight benefits, create urgency, and suggest a strong call to action."
    return f"As a {role}, I would answer your request with the appropriate role style."


def main() -> None:
    print("Role Prompting Demo")
    print("Choose a role such as teacher, chef, salesperson, coach, or friend.")
    role = input("Role: ").strip()
    request = input("Request for the assistant: ").strip()

    prompt = build_role_prompt(role, request)
    print("\n=== Built Prompt ===")
    print(prompt)

    response = mock_model(role, request)
    print("\n=== Simulated Role-Based Response ===")
    print(response)


if __name__ == "__main__":
    main()
