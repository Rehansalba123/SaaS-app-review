
import json, os
def save_to_json(data):
    os.makedirs("output", exist_ok=True)
    with open("output/reviews.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
