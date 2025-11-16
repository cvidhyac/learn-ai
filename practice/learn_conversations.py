"""
Example of a basic conversational bot that can answer coding questions interactively and can retain context from previous
question. The example utilizes system, user and assistant prompts, and runs until user quits.
"""

import traceback

from api_client import SimpleOpenApiClient, SimpleOpenApiClientBuilder
from dotenv import load_dotenv
from openai import APIStatusError
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
)

# Load environment variables from .env file
load_dotenv()

"""
Execute a prompt for given input message using a free model with medium-creativity and limited tokens
"""


def execute_prompt(api_client: SimpleOpenApiClient, input_msg: list[ChatCompletionMessageParam]) -> str | None:
    try:
        response = api_client.chat_completion(input_msg)
        content = response.choices[0].message.content
        return content if content else None
    except APIStatusError:
        error_msg = traceback.format_exc()
        print(f"Error executing OpenAI prompt, {error_msg}")
        return None


"""
Interactive conversational bot that accepts user input and replies to the question posted by the user.
"""


def conversational_bot():
    api_client: SimpleOpenApiClient = (
        SimpleOpenApiClientBuilder()
        .with_model("ibm-granite/granite-4.0-h-micro")
        .with_temperature(1)
        .with_max_completion_tokens(250)
        .build()
    )

    system_msg_content = """You are a helpful coding tutor that can answer any questions related to programming or coding.
    When asked questions unrelated to coding, please respond with - 'I am not allowed to answer' """
    quit_or_prompt = ""
    sys_msg: ChatCompletionSystemMessageParam = api_client.system_message(system_msg_content)
    msg: list[ChatCompletionMessageParam] = [sys_msg]
    while quit_or_prompt.lower() != "q":
        quit_or_prompt = input("Enter a question related to coding, enter q to quit: ")
        if quit_or_prompt.lower() == "q":
            print("I hope the questions provided enough clarification, please let me know how I can help!")
            break
        user_dict = api_client.user_message(quit_or_prompt)
        msg.append(user_dict)
        reply = execute_prompt(api_client, msg)
        if reply is not None:
            assistant_dict: ChatCompletionAssistantMessageParam = api_client.assistant_message(reply)
            msg.append(assistant_dict)
            print(f"\nAssistant: {reply}")
        else:
            print("Received error processing the request, please try again!")
            msg.pop()


if __name__ == "__main__":
    conversational_bot()
