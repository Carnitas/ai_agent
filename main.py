import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
USER_PROMPT = "What is the meaning of life?"
messages = [
    types.Content(role="user", parts=[types.Part(text=USER_PROMPT)]),
]
response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages
)
prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("USER_PROMPT", nargs="?", help="Prompt for the AI agent")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()
    if args.verbose:
        print(f"User prompt: {args.USER_PROMPT}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
