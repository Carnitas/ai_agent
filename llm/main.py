import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .call_function import AVAILABLE_FUNCTIONS
from .prompts import SYSTEM_PROMPT


def main() -> None:
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        print('Example: python main.py "How do I fix the calcultor app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(
    client: genai.Client, messages: list[types.Content], verbose: bool
) -> None:

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[AVAILABLE_FUNCTIONS], system_instruction=SYSTEM_PROMPT
        ),
    )
    if verbose and response.usage_metadata:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if response.function_calls:
        print(
            f"Calling function {response.function_calls[0].name}({response.function_calls[0].args})"
        )


if __name__ == "__main__":
    main()
