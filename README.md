# Aqua Sniper - A Rare Item Sniper Bot for BrickPlanet

Aqua Sniper is a sophisticated tool designed to help you secure any new rare items on BrickPlanet with ease. Please follow the instructions below to set up and use the bot.

## Setup Instructions

1. **Download or clone the repository**: Clone this repository to your local machine to get started.

2. **Configure your account**: Open the `config.json` file and fill in your BrickPlanet username and password. This information is necessary for the bot to operate on your behalf. Additional accounts can be added or removed if desired. Proxies are also not essential, but will increase the speed at which the bot can query the site without being rate-limited.

    ```json
    {
      "users": [
        {
          "username": "FIRST_USERNAME_HERE",
          "password": "FIRST_PASSWORD_HERE"
        },
        {
          "username": "SECOND_USERNAME_HERE",
          "password": "SECOND_PASSWORD_HERE"
        }
      ],
      "proxies": [
        "username:password@192.168.0.1:80",
        "username:password@192.168.0.1:8080",
        "username:password@10.0.0.1:80",
        "username:password@10.0.0.1:8080",
      ]
    }
    ```

3. **Running the sniper**: To get started with the bot, simply run the `RUN.bat` file. This script will not only automatically check and install any necessary Python packages but also initiate the bot immediately after the setup. Use this script each time you want to start the bot.

    ```
    ./RUN.bat
    ```

## Safety & Security

Your account security is of the highest importance. Your login credentials stored in the `config.json` file are only used to automate the login process and are not shared or transmitted anywhere.

## Disclaimer

Please use this bot responsibly and ethically. Adhere to the terms of service of BrickPlanet. I am not responsible for any actions taken against your account for misuse of this bot.

---

Best of luck securing rare items on BrickPlanet!
