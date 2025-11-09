## Building conversations

There are two types of conversations:

- Single turn conversations (non-interactive)
- Multi-turn conversations (interactive)

### What is a single turn conversation?

In the examples [Sentiment classification](../practice/learn-sentiment-classification.py) and
[LLM Temperature analysis](../practice/learn-temperatures.py), we only provided one input
and there was one output.

### What is a multi-turn conversation?

Build on previous prompts depending on how the model responds.

## Roles overview

Roles are the heart of how chat models function. There are three types of roles

- User role (basic examples)
- System role
- Assistant role

Each role will have its own content. Assistant's message will usually adhere to system's
message.

### What are the key characteristics of each role

- System roles control assistant's behavior
- User role: Instruct the assistant
- Assistant: Response to user instruction.
    * Can also be written by developer to provide examples.

### Examples of role-based messages

- System message: You are a helpful python tutor that speaks concisely.
- User message: Explain me the difference between mutable and immutable types in python?

### Mitigating system misuse

In system messages, we can include instructions to restrict its response for messages where
a model should not be providing any advise.

```python
sys_msg = """
You are a finance education assistant that helps students study for their exams.
If you are asked specific questions on real-world financial advise with risk to their finances,
respond with: "I am sorry, I am not allowed to provide financial advice.
"""
```

