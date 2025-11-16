# Prompt engineering

* Write effective prompt including context, words, verbs, output length
* Using `max_completion_tokens` may result in incomplete sentences

## Well crafted prompts
- Start with instructions
- Use delimited inputs, use backticks of triple strings / f-strings
- Well crafted prompts can be in markdown syntax

## TRACE framework
T.R.A.C.E framework

Task: Specify the task or challenge, define guardrails and constraints.
Request: Articulate the direct request, specify type of response or next sequence of actions.
Action: Detail the actions the AI should undertake, provide guidance on how to approach the task.
Context: Provide background information, reference to enhance AI's understanding and relevance of the response.
Examples:  Provide examples of what the AI should execute for the given prompt, include formats in the examples.
