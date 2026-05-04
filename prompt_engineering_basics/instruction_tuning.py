"""Instruction tuning demo.

This example shows how to refine a prompt with explicit instructions, constraints, and expected format.
"""

import textwrap


def build_instruction_tuned_prompt(task: str, constraints: str, output_format: str) -> str:
    prompt = textwrap.dedent(f"""
        You are a helpful assistant.
        Follow all instructions carefully.

        TASK:
        {task}

        CONSTRAINTS:
        {constraints}

        OUTPUT FORMAT:
        {output_format}

        RESPONSE:
    """)
    return prompt


def mock_model(task: str, constraints: str, output_format: str) -> str:
    """
    Generate a response that follows the constraints and output format.
    """
    task_lower = task.lower()
    
    # Detect if it's about machine learning
    if "machine learning" in task_lower:
        if "bullet" in output_format.lower() or "list" in output_format.lower():
            return """• Machine Learning is a type of AI that learns from data automatically, improving with experience
• It finds patterns in large amounts of information without being explicitly programmed
• Common uses include recommendation systems, image recognition, and predictive analytics"""
        elif "json" in output_format.lower():
            return """{
  "points": [
    "Machine Learning is a type of AI that learns from data automatically",
    "It finds patterns without explicit programming",
    "Common uses: recommendations, image recognition, predictions"
  ]
}"""
        elif "paragraph" in output_format.lower():
            return "Machine Learning is a subset of AI that learns from data automatically without being explicitly programmed. It identifies patterns in large datasets and improves through experience. This technology powers recommendation systems, image recognition, and predictive analytics."
    
    # Generic response for other tasks
    if "bullet" in output_format.lower() or "list" in output_format.lower():
        return f"""• Point 1: {task} - First key aspect
• Point 2: {task} - Second key aspect  
• Point 3: {task} - Third key aspect"""
    elif "json" in output_format.lower():
        return f'{{"task": "{task}", "points": ["Point 1", "Point 2", "Point 3"]}}'
    
    return f"Response for: {task}\nFollowing constraints: {constraints}\nIn format: {output_format}"


def main() -> None:
    print("Instruction Tuning Demo")
    task = input("Task to complete: ").strip()
    constraints = input("Constraints (e.g. keep it short, use bullet points, avoid jargon): ").strip()
    output_format = input("Desired output format (e.g. JSON, bullet list, short paragraph): ").strip()

    prompt = build_instruction_tuned_prompt(task, constraints, output_format)
    print("\n=== Built Prompt ===")
    print(prompt)

    response = mock_model(task, constraints, output_format)
    print("\n=== Simulated Instruction-Tuned Response ===")
    print(response)


if __name__ == "__main__":
    main()
