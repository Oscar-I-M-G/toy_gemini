import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
gem_model = 'gemini-2.0-flash-001'


def main():
    args = sys.argv[1:]
    if not args:
        print("AI assistant\nUsage: python main.py <'Promp here'>")
        sys.exit(1)
    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]

    response = client.models.generate_content(
            model=gem_model,
            contents = messages
            )

    print(f"{response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")




if __name__ == "__main__":
    main()
