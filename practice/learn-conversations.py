"""
Example of a basic conversational bot that can answer coding questions interactively and can retain context from previous
question. The example utilizes system, user and assistant prompts, and runs until user quits.
"""
import os
import traceback
from openai import OpenAI, APIStatusError

"""
Execute a prompt for given input message using a free model with medium-creativity and limited tokens
"""


def execute_prompt(input_msg: list[dict[str, str]]) -> str|None:
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENAI_API_KEY"))
    model_to_use = "ibm-granite/granite-4.0-h-micro"
    try:
        response = client.chat.completions.create(
            model=model_to_use,
            temperature=1,
            max_completion_tokens=300,
            messages=input_msg
        )
        return response.choices[0].message.content
    except APIStatusError:
        print(f"Error executing OpenAI using model {model_to_use}, {traceback.print_exc()} ")



"""
Interactive conversational bot that accepts user input and replies to the question posted by the user.
"""


def conversational_bot():
    system_message = """You are a helpful coding tutor that can answer any questions related to programming or coding.
    When asked questions unrelated to coding, please respond with - 'I am not allowed to answer' """
    system_dict = {"role": "system", "content": system_message}
    quit_or_prompt = ''
    msg = [system_dict]
    while quit_or_prompt.lower() != 'q':
        quit_or_prompt = input("Enter a question related to coding, enter q to quit: ")
        if quit_or_prompt.lower() == 'q':
            print("I hope the questions provided enough clarification, please let me know how I can help!")
            break
        user_dict = {"role": "user", "content": quit_or_prompt}
        msg.append(user_dict)
        reply = execute_prompt(msg)
        if reply is not None:
            assistant_dict = {"role": "assistant", "content": reply}
            msg.append(assistant_dict)
            print(f"\nAssistant: {reply}")
        else:
            print("Received error processing the request, please try again!")
            msg.pop()


if __name__ == '__main__':
    conversational_bot()
