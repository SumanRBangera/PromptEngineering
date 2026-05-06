# Prompt Engineering Basics

This folder contains interactive Python demos for core prompt engineering patterns. Each file is a standalone script that can be run independently to explore different prompting techniques.





## Overview

Prompt engineering is the practice of crafting effective prompts to get better responses from language models. Here are 7 essential techniques:


---

## 1. Zero-Shot Prompting (`zero_shot_prompting.py`)

**Definition:**
Zero-shot prompting means providing a task description with NO examples. The model must understand and complete the task based on the instruction alone.

**Key Characteristics:**
- No examples provided
- Simple, direct instructions
- Good for straightforward tasks
- Fast and efficient

**Example:**
```
Task: Translate English to Spanish
Input: Good morning, how are you?

Output: Buenos días, ¿cómo estás?
```

**When to use:**
- Simple tasks the model understands well
- Quick prototyping
- Tasks that don't need complex reasoning

**Run it:**
```bash
python3 zero_shot_prompting.py
```

---

## 2. Few-Shot Prompting (`few_shot_prompting.py`)

**Definition:**
Few-shot prompting provides a small number of examples (2-3) that demonstrate the desired task. The model learns the pattern from examples and applies it to new inputs.

**Key Characteristics:**
- Provides 2-3 example pairs
- Shows input-output relationship
- Model learns the pattern from examples
- More accurate than zero-shot for complex tasks

**Example:**
```
Example 1:
Input: hello
Output: hola

Example 2:
Input: goodbye
Output: adiós

Now apply this pattern:
Input: good morning
Output: buenos días
```

**When to use:**
- Specific formatting or style needed
- Complex transformations
- When you want consistent output format
- Building upon patterns

**Run it:**
```bash
python3 few_shot_prompting.py
```

---

## 3. Chain-of-Thought (CoT) Prompting (`chain_of_thoughts.py`)

**Definition:**
Chain-of-Thought prompting breaks down complex problems into step-by-step reasoning. The model shows its thinking process before providing the final answer.

**Key Characteristics:**
- Step-by-step reasoning visible
- Easier to verify correctness
- Great for math and logic problems
- Improves accuracy on complex tasks

**Example:**
```
Question: What is 45 plus 27?

Response with CoT:
Step 1: Identify the numbers 45 and 27
Step 2: Add them together: 45 + 27 = 72
Answer: 72
```

**When to use:**
- Math and logic problems
- Complex multi-step reasoning
- When you need to audit the thinking process
- Tasks requiring justification

**Run it:**
```bash
python3 chain_of_thoughts.py
```

---

## 4. Instruction Tuning (`instruction_tuning.py`)

**Definition:**
Instruction tuning provides very detailed, explicit instructions with constraints and expected output format. This makes the model's behavior more predictable and controlled.

**Key Characteristics:**
- Clear task definition
- Explicit constraints
- Specified output format
- Highly structured approach
- Maximum control over output

**Example:**
```
TASK: Explain machine learning
CONSTRAINTS: Keep it simple and beginner-friendly
OUTPUT FORMAT: Bullet list with 3 main points

Response:
• Machine Learning is a type of AI that learns from data automatically
• It finds patterns without explicit programming
• Common uses: recommendations, image recognition, predictions
```

**When to use:**
- You need specific output format (JSON, tables, lists)
- Strict constraints required (word limit, language level)
- Production systems needing consistency
- Complex requirements with many specifications

**Run it:**
```bash
python3 instruction_tuning.py
```

---

## 5. Role Prompting (`role_prompting.py`)

**Definition:**
Role prompting assigns a persona or expertise level to the model. The model adopts the personality, tone, and perspective of the assigned role.

**Key Characteristics:**
- Assigns a specific role/persona
- Changes tone and style of response
- Leverages expertise of the role
- Same question, different answers based on role

**Example:**
```
Role: Teacher
Request: How can I learn to code faster?

Response (as Teacher):
Step 1: Start with fundamentals - variables, loops, functions
Step 2: Practice consistently - code a little every day
Step 3: Learn by doing - build small projects
Step 4: Study others' code - read experienced code
Step 5: Join a community - discuss and get feedback
```

**When to use:**
- You want a specific perspective or expertise
- Different tones needed (formal, casual, technical)
- Specialized knowledge required
- Customized output style

**Run it:**
```bash
python3 role_prompting.py
```

---

## 6. Prompt Chaining (`prompt_chaining.py`)

**Definition:**
Prompt chaining breaks complex tasks into multiple sequential prompts. The output of one prompt becomes the input to the next, creating a workflow.

**Key Characteristics:**
- Multi-step approach
- Output of step 1 feeds into step 2
- Better quality results
- Handles complex workflows
- Modular and maintainable

**Example:**
```
Input Task: Write a product description and list benefits for a coffee maker

Step 1 (Planning Prompt):
- Understand the task
- Identify key requirements
- Plan structure

Step 2 (Execution Prompt):
Use the plan from Step 1 to generate the final product description and benefits list
```

**When to use:**
- Complex, multi-part tasks
- Need to validate intermediate steps
- Content creation pipelines
- Analysis and synthesis tasks
- Long-form content generation

**Run it:**
```bash
python3 prompt_chaining.py
```

---

## 7. Output Parsing (`output_parsing.py`)

**Definition:**
Output parsing asks the model to return structured data (usually JSON) that can be programmatically parsed and used in code.

**Key Characteristics:**
- Model returns JSON format
- Easy to extract data programmatically
- Type-safe and validated
- Integrates with code easily
- Reduces string parsing errors

**Example:**
```
Task: Create a shopping list for a picnic

Raw Model Output (JSON):
{
  "items": ["milk", "eggs", "bread"],
  "notes": "Buy fresh produce"
}

Parsed in Python:
parsed["items"][0]  # Returns: "milk"
parsed["notes"]     # Returns: "Buy fresh produce"
```

**When to use:**
- Integration with other systems
- Extracting structured data
- Creating databases/configs automatically
- API response formatting
- Data validation and processing

**Run it:**
```bash
python3 output_parsing.py
```

---

## Quick Comparison Table

| Technique | Use Case | Complexity | Output |
|---|---|---|---|
| Zero-Shot | Simple tasks | Low | Direct answer |
| Few-Shot | Pattern learning | Medium | Learned pattern applied |
| Chain-of-Thought | Complex reasoning | High | Step-by-step reasoning |
| Instruction Tuning | Precise control | Medium-High | Structured, formatted |
| Role Prompting | Specialized perspective | Medium | Role-specific response |
| Prompt Chaining | Multi-step workflows | High | Final result from chain |
| Output Parsing | Structured data | Medium | JSON/structured format |

---
