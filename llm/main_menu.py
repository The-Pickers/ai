import random
from llm import model

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

Rules:
1. Use '{selected_theme}' to create a short and concise one-sentence message.
2. Do not include the carbon reduction number directly in the sentence.
3. Keep the tone positive and uplifting.
4. You may naturally use 1-2 emojis.
5. Refer to the following example styles:

Examples:
- "A sea turtle has found its freedom 🐢"
- "A whale is gliding through the deep ocean 🐋"
- "A green forest is being reborn 🌳"
- "A tree is growing strong and tall 🌲"
- "A clear river has begun to sing 🏞️"
- "The stars are shining even brighter 🌟"
- "A seed has sprouted 🌱"
- "Flowers are blooming under the sun 🌸"

6. Output only the requested sentence, without any additional explanation or comments.

7. Respond with one sentence in English.

"""

    response = model.generate_content(carbon_reduction_prompt)
    return response.text


