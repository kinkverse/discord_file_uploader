import json

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

FOLDER_TO_WATCH = config["C:\\Users\\taysh\\Pictures\\Auto 21111 stable diff"]
WEBHOOK_URL = config['https://discord.com/api/webhooks/1219572077468712960/cU6SsVoNTAz5mg96Ylxf7X7SA2R9eW7JJHsKEeMYcZMbwHHQLETEP28GdzisdDPqzHyf']

# Rest of your code...
# You can use the FOLDER_TO_WATCH and WEBHOOK_URL variables as needed in the rest of your program.