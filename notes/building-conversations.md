## Building conversations

There are two types of conversations:

- Single turn conversations (non-interactive)
- Multi-turn conversations (interactive)

### What is a single turn conversation?

In the examples [Sentiment classification](../practice/learn_sentiment_classification.py) and
[LLM Temperature analysis](../practice/learn_temperatures.py), we only provided one input
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

## Shot Prompting

- One shot prompting:
  LLM uses the user message, any pre-existing system message and its trained knowledge
  to answer the query. Typically single-turn tasks with static prompts are good examples of "one-shot"
  prompting. The accuracy of the LLM response will need more iterations to achieve the desired output.

- Few Shot prompting:
  Utilizes the roles - system, user, and assistant to provide guardrails, precise instructions and examples.
  Multi-turn conversations or more complex analysis usually are good use cases for few-shot prompting.

### System vs assistant vs user - What is the best place to provide example?

* System -> Important template formatting

  For example:

  ```
  Output the information in this format
  field_one | field_two | field_three
  When the user asks questions unrelated to formatting, respond with 'I am not allowed to answer'
  ```
* User -> Context required for new input

For example:

  ```
  Help me format this text to pipe delimited values: userA, userB, userC
  ```

* Assistant -> Example conversations

For example:

```
/user: Help me format the line - fieldA, fieldB : fieldC to pipe-delimited value
returns: fieldA | fieldB | fieldC

/user: What is the weather today?
returns: I am not allowed to answer
```

- Assistant messages are excellent places to provide examples in addition to the examples provided in system and user
  roles. It is a more structured way in shot-prompting.
- More examples provide the application more structure and more accurate responses.

In a new system configuration, it is always advised to include as many "user-assistant" pairs as possible.
