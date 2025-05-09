from llm.model import model
import json
import os

current_dir = os.path.dirname(__file__)  # mission_complete.py의 디렉토리 경로
json_path = os.path.join(current_dir, "carbon_reduction_data.json")

with open(json_path, "r") as f:
    CARBON_REDUCTION_PER_ITEM = json.load(f)

def calculate_carbon(trash_counts):
    total_carbon = 0
    for item, count in trash_counts.items():
        carbon_per_item = CARBON_REDUCTION_PER_ITEM.get(item, 0)
        total_carbon += carbon_per_item * count
    return total_carbon

# LLM 프롬프트 생성 함수
def generate_mission_summary(trash_data):
    total_carbon = calculate_carbon(trash_data)
    points = int(total_carbon * 100)
    mission_complete_prompt = f"""
You are a cheerful assistant. Generate a short, positive English message about the user's trash collection.

The total carbon reduction is:
{total_carbon:.3f} kg

💡 Rules:
- Strictly use this format:
  "Great job! {total_carbon:.3f} kg carbon reduced! 🌍💚"
  or
  "{total_carbon:.3f} kg CO₂ cut! Earth thanks you!"
- Max 2 sentences.
- Use diverse cheerful expressions.
- Example outputs:
  - Great job! 0.33 kg carbon reduced! 🌍💚
  - 0.33 kg CO₂ cut! Earth thanks you! 🌱
  - Bravo! 0.14 kg CO₂ saved! 🌎💖

⚠ Do not explain anything else. Only return the final message.
"""

    response = model.generate_content(mission_complete_prompt)
    return {
    'message': response.text.strip(),
    'total_carbon': total_carbon,
    'points' : points
    }

