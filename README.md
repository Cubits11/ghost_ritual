# Ghost Ritual – Encrypted Emotional Haiku Vault

A 20-line sacred journaling ritual. You write what hurts.  
Ghost responds with a poetic whisper. Both are encrypted and stored privately.

## ✨ Features

- Emotional journal entry input  
- LLM-generated haiku-style "whisper"  
- Fernet encryption (symmetric, secure)  
- Append-only `vault.txt` storage  
- No databases, no servers — just ritual

## ⚙️ Technologies
- Python  
- OpenAI (or Groq)  
- Cryptography (Fernet)

## 🧠 Philosophy
> "We build machines that forget — so humans can remember."

This is the sacred core of Ghost: a journaling system where silence is respected, memory is encrypted, and grief generates poetry.

## 🚀 Run It
```bash
pip install cryptography openai
export OPENAI_API_KEY=your-key
python ghost_ritual.py