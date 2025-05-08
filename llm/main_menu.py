import random
from llm.model import model

def select_theme(carbon_reduction):
    if carbon_reduction < 1:
        themes = ["seed 🌱", "sprout 🌿", "flower 🌸"]
    elif carbon_reduction < 10:
        themes = ["tree 🌳", "bird 🐦", "river 🏞️"]
    elif carbon_reduction < 50:
        themes = ["forest 🌲", "fish 🐟", "sea turtle 🐢"]
    else:
        themes = ["whale 🐋", "big forest 🌳🌳", "star 🌟"]

    return random.choice(themes)

def generate_carbon_reduction_message(carbon_reduction):
    selected_theme = select_theme(carbon_reduction)

    carbon_reduction_prompt = f"""
You are a friendly and warm-toned AI that creates a short message highlighting environmental protection results.

The selected theme is '{selected_theme}'.

Types of messages to mix:

1️⃣ Descriptive type (about nature/environment)
   - Describe how nature benefits from eco-friendly actions.

2️⃣ Impact type (about the achievement)
   - Express the positive outcome (e.g., "2 turtles saved!").

🚨 IMPORTANT:
- Prefer Impact type messages that **focus on animals** (e.g., "2 turtles saved").
- Impact type messages should mention **the number of animals saved or protected**.
- Type 1 can appear occasionally, but Type 2 should be the main focus.

🚫 IMPORTANT:
- Output ONLY the final one-sentence message.
- Do NOT mention "you", "your", or any user-centered wording.
- The message must be VERY SHORT: maximum 12 words or 50 characters.
- 1-2 emojis can be included naturally.
- Use simple, impactful language.
- Always vary the sentence structure.
- Absolutely NO long or complex sentences. Keep it short and punchy.
- Long sentences or explanations will be considered incorrect output.

Examples (for your internal guidance ONLY – DO NOT OUTPUT these):

[Type 1: Descriptive]
- "A sea turtle swims freely 🐢."
- "The forest grows greener every day 🌳."
- "A clean river sparkles 🏞️."

[Type 2: Impact]
- "2 turtles saved 🐢🐢."
- "3 dolphins protected 🐬🐬🐬."
- "5 fish released 🐟🐟🐟🐟🐟."
- "Whale habitat expanded 🐋"

"""

    response = model.generate_content(carbon_reduction_prompt)
    return response.text


