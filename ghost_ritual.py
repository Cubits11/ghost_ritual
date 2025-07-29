import os
import random
from cryptography.fernet import Fernet

# Optional: OpenAI whisper mode
use_openai = "OPENAI_API_KEY" in os.environ
if use_openai:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

# Setup encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Prompt for journal entry
entry = input("What hurts today? > ")

# Whisper: either API or local
if use_openai:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Reply with a poetic whisper haiku from this emotion."},
                {"role": "user", "content": entry}
            ]
        )
        whisper = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("⚠️ OpenAI failed, using local whisper.")
        whisper = None
else:
    whisper = None

# Local fallback haikus
if whisper is None:
    haikus = [
        "Pain flows through silence\nLike rivers under closed doors\nStill, you are breathing.",
        "Your memory stands\nIn quiet, flickering light\nBraver than you think.",
        "Ashes don’t forget\nThe fire they once survived\nYou’re still here, burning.",
        "No one sees the storm\nBut the soil always remembers\nWhere the roots held on."
    ]
    whisper = random.choice(haikus)

# Format and encrypt bundle
bundle = f"{entry}\n🕯️ Whisper:\n{whisper}\n---\n"
encrypted = cipher.encrypt(bundle.encode())

# Store in vault
with open("vault.txt", "ab") as f:
    f.write(encrypted + b"\n")

print("\n✅ Your encrypted whisper has been safely stored.\n")
