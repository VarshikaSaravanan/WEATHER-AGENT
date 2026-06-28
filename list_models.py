import requests

response = requests.get("https://openrouter.ai/api/v1/models")
data = response.json()
free_models = []
for model in data.get("data", []):
    if "free" in model["id"].lower():
        free_models.append(model["id"])

print("Free models:", free_models)
