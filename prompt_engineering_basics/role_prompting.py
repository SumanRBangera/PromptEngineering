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
    """
    Generate role-specific responses with appropriate tone and style.
    """
    role_lower = role.lower()
    
    if role_lower == "teacher":
        return """Step 1: Start with the fundamentals - understand core concepts like variables, loops, and functions.
Step 2: Practice consistently - code a little every day rather than cramming.
Step 3: Learn by doing - build small projects that interest you.
Step 4: Study others' code - read how experienced programmers solve problems.
Step 5: Join a community - discuss with peers and get feedback."""
    
    if role_lower == "chef":
        return """The key is to practice your fundamentals: master basic techniques first.
Season your learning - mix theory with practical coding.
Use fresh ingredients - stay updated with modern languages and tools.
Time your ingredients - don't rush, let concepts sink in naturally.
Taste as you go - test your code frequently to catch mistakes early."""
    
    if role_lower == "salesperson":
        return """Here's why learning to code is your best investment:
✓ Opens doors to high-paying careers (average $100k+)
✓ Build amazing products that change the world
✓ Work flexibly from anywhere
✓ Your skills become more valuable every year
Ready to start your coding journey today? I recommend structured learning paths."""
    
    if role_lower == "coach":
        return """You've got this! Here's the winning strategy:
🎯 Set clear, measurable goals - "Build a web app in 30 days"
💪 Push through the beginner's wall - first 2 weeks are hardest
🏆 Celebrate small wins - every function you write is progress
🔄 Keep showing up - consistency beats intensity
📊 Track your progress - you'll be amazed how far you've come"""
    
    if role_lower == "friend":
        return """Hey! So you wanna learn to code? That's awesome! Here's what worked for me:
- Don't stress about being perfect, just start building stuff you care about
- YouTube tutorials are your friend - watch, pause, code along
- Find a buddy to learn with - it's way more fun
- When you get stuck, Google is your bestie (and Stack Overflow)
- Remember, everyone started as a beginner. You got this! 🚀"""
    
    return f"As a {role}, I would approach your request with the perspective and expertise of that role."


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
