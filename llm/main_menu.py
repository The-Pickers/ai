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
You are a friendly and warm-toned AI that creates a short message praising a user's environmental protection activities.

The selected theme is '{selected_theme}'.

🛑 IMPORTANT:
- Your output **must exactly follow the style of the following examples:**

Examples:
- "A sea turtle has found its freedom 🐢"
- "A whale is gliding through the deep ocean 🐋"
- "A green forest is being reborn 🌳"
- "A tree is growing strong and tall 🌲"
- "A clear river has begun to sing 🏞️"
- "The stars are shining even brighter 🌟"
- "A seed has sprouted 🌱"
- "Flowers are blooming under the sun 🌸"

Rules:
1. **The message must be a very short, clear, and simple one-sentence statement.**
2. Use '{selected_theme}' naturally in the message.
3. Do NOT add extra praise, no introductions, and no explanations.
4. 1-2 emojis can be included naturally.
5. Output ONLY the sentence, nothing else.
6. To avoid repetitive wording, vary the sentence structure and wording every time even for the same theme.

"""

    response = model.generate_content(carbon_reduction_prompt)
    return response.text


