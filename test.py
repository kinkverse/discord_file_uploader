import json

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

FOLDER_TO_WATCH = config['C:\\Users\\taysh\\Pictures\\Auto 21111 stable diff']
WEBHOOK_URL = config['https://discord.com/api/webhooks/1219572077468712960/cU6SsVoNTAz5mg96Ylxf7X7SA2R9eW7JJHsKEeMYcZMbwHHQLETEP28GdzisdDPqzHyf']

# Print the contents of the config dictionary
print(config)

# Rest of your code...