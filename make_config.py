import json
from pathlib import Path


def main():
    config_path = Path("config.json") 

    n = int(input("How many Numbers do You Have: "))

    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
    else:
        config = {
            "group_source": int(input('type group or channel id here not username: ')),
            "accounts": []
        }

    for _ in range(n):
        new_account = {
            "phone": input("phone Number With +Country code: "),
            "api_id": input("api_id Get from my.telegram.org: "),
            "api_hash": input("api_hash Get from my.telegram.org: ")
        }
        config["accounts"].append(new_account)

    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)


if __name__ == '__main__':
    main()
