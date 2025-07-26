import json

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def is_official_account(username: str) -> bool:
    config = load_config()
    return username in config["public_accounts"] or username in config["hidden_accounts"]