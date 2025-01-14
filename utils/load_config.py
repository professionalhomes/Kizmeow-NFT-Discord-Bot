import json


def load_config_from_json(uid):
    with open('setting.json', 'r', encoding='utf-8') as file:
        setting_data = json.load(file)
        setting_data = setting_data.setdefault(
            uid,
            {
                'button': False,
                'language': 'en-US',
                'visibility': False
            }
        )

    return (
        setting_data['button'],
        setting_data['language'],
        setting_data['visibility']
    )
