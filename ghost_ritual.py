import os
from cryptography.fernet import Fernet
import openai

# Setup
key = Fernet.generate_key()
cipher = Fernet(key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ritual
entry = input("What hurts today? > ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "Reply with a poetic whisper haiku from this emotion."},
              {"role": "user", "content": entry}]
)
whisper = response['choices'][0]['message']['content'].strip()

bundle = f"{entry}\n🕯️ Whisper:\n{whisper}\n---\n"
encrypted = cipher.encrypt(bundle.encode())

with open("vault.txt", "ab") as f:
    f.write(encrypted + b"\n")