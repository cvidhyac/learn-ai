import os
from collections.abc import Iterable

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionFunctionToolParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

# Load environment variables from .env file
load_dotenv()

"""
An Open API Client Wrapper to make calls for my projects to follow DRY principles
"""


class SimpleOpenApiClient:
    client: OpenAI
    model: str
    temperature: float
    max_completion_tokens: int
    tools: Iterable[ChatCompletionFunctionToolParam] | None

    def __init__(self):
        pass

    def chat_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        return self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_completion_tokens=self.max_completion_tokens,
            tool_choice="auto",
            tools=self.tools,
            messages=messages,
        )

    @staticmethod
    def system_message(content: str) -> ChatCompletionSystemMessageParam:
        return ChatCompletionSystemMessageParam(role="system", content=content)

    @staticmethod
    def user_message(content: str) -> ChatCompletionUserMessageParam:
        return ChatCompletionUserMessageParam(role="user", content=content)

    @staticmethod
    def assistant_message(content: str) -> ChatCompletionAssistantMessageParam:
        return ChatCompletionAssistantMessageParam(role="assistant", content=content)


"""
Builder for SimpleOpenApiClient client

Example:
client = SimpleOpenApiClientBuilder().with_model("gpt4").with_temperature(0.7).build()
"""


class SimpleOpenApiClientBuilder:

    def __init__(self):
        self._model: str = "ibm-granite/granite-4.0-instruct:free"
        self._temperature: float = 0.7
        self._max_completion_tokens: int = 300
        self._base_url: str | None = None
        self._api_key: str | None = None
        self._timeout: int | None = None
        self._client: OpenAI | None = None
        self._tools: Iterable[ChatCompletionFunctionToolParam] | None = None

    def with_model(self, model: str) -> "SimpleOpenApiClientBuilder":
        self._model = model
        return self

    def with_temperature(self, temperature: float) -> "SimpleOpenApiClientBuilder":
        self._temperature = temperature
        return self

    def with_max_completion_tokens(self, max_completion_tokens: int) -> "SimpleOpenApiClientBuilder":
        self._max_completion_tokens = max_completion_tokens
        return self

    def with_base_url(self, base_url: str) -> "SimpleOpenApiClientBuilder":
        self._base_url = base_url
        return self

    def with_api_key(self, api_key: str) -> "SimpleOpenApiClientBuilder":
        self._api_key = api_key
        return self

    def with_timeout(self, timeout: int) -> "SimpleOpenApiClientBuilder":
        self._timeout = timeout
        return self

    def with_tools(self, tools: Iterable[ChatCompletionFunctionToolParam]) -> "SimpleOpenApiClientBuilder":
        self._tools = tools
        return self

    def build(self) -> SimpleOpenApiClient:
        api_key = self._api_key or os.getenv("OPEN_ROUTER_API_KEY")
        base_url = self._base_url or os.getenv("OPEN_ROUTER_BASE_URL")

        if not api_key:
            raise ValueError("API key is required")

        if not base_url:
            raise ValueError("Base url is required")

        client_instance = SimpleOpenApiClient()
        client_instance.model = self._model
        client_instance.temperature = self._temperature
        client_instance.max_completion_tokens = self._max_completion_tokens
        client_instance.tools = self._tools

        openai_dict: dict[str, str | int] = {
            "base_url": base_url,
            "api_key": api_key,
        }

        if self._timeout is not None:
            openai_dict["timeout"] = self._timeout

        client_instance.client = OpenAI(**openai_dict)
        return client_instance
