## Tool Calls

- Agent makes tool calls
- LLM tells the agent what it needs and agent executes the tool calls and returns the response back to user.

Standard conversation history between your agent and LLM needs a :
- system prompt
- user prompt
- assistant prompt

- tool calls are made for external API where the LLM doesn't have pre-trained data. For example, what is the
weather today?

### What makes the tool calls?

An agentic system like ChatGPT comprises an agent runtime + LLM.

- LLM Generates the tool call (text based JSON)
- Agentic system / agent executes the tool call
- Tool itself - runs code

### Multi-hop tool calls

- After making a particular tool call T1, agent can make second tool call T2
- Returns final response to user once LLM has flat response consolidated from all tool calls

## Human in the loop pattern
- Why? because tool calls are consequential and have side effects (requires strong guardrails)
- Get a human to approve / evaluate what AI thinks should be done, once approved get AI to execute the call
