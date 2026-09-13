
"""
Prompt Templates and Variables

Concepts covered:
1. Reusable prompt template
2. Prompt variables
3. Filling variables dynamically
4. Reusing the same prompt for different inputs
"""


# --------------------------------------------------
# 1. Basic prompt template
# --------------------------------------------------

prompt_template = """
You are an AI assistant helping a user understand a technical topic.

Explain the following topic in simple terms:

Topic: {topic}

Target audience: {audience}

Keep the explanation:
- Simple
- Practical
- Easy to understand
"""


# --------------------------------------------------
# 2. Function to fill the prompt variables
# --------------------------------------------------

def create_prompt(topic, audience):
    """
    Fill the prompt template with dynamic values.
    """

    prompt = prompt_template.format(
        topic=topic,
        audience=audience
    )

    return prompt


# --------------------------------------------------
# 3. Test with different variables
# --------------------------------------------------

prompt_1 = create_prompt(
    topic="Prompt Engineering",
    audience="Beginner"
)

prompt_2 = create_prompt(
    topic="Kubernetes",
    audience="Software Engineer"
)

prompt_3 = create_prompt(
    topic="RAG",
    audience="Machine Learning Engineer"
)


# --------------------------------------------------
# 4. Print the generated prompts
# --------------------------------------------------

print("----- PROMPT 1 -----")
print(prompt_1)

print("\n----- PROMPT 2 -----")
print(prompt_2)

print("\n----- PROMPT 3 -----")
print(prompt_3)
