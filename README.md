# Aqua Sniper - A Rare Item Sniper Bot for BrickPlanet

## Description
Aqua Sniper is a sophisticated tool designed to help you automatically secure any new rare items on BrickPlanet with ease. The sniper will run in the background, continuously checking for new rares, and purchasing them the moment they are detected.

## Features
- **Automatic Purchasing**: Automatically checks for and purchases new rare items released in the shop.
- **Multi-Account Functionality**: Allows for an unlimited number of accounts to be added and used for sniping.
- **Support for Proxies**: Proxies can be added to allow for faster detection of new rares.
- **Daily Login Rewards**: Reauthenticates each account every 24 hours to ensure you get your daily login rewards.

## Installation and Setup
1. **Download or clone the repository**: Clone or download this repository to your local machine to get started.
   ```bash
    git clone https://github.com/AndyAnderson8/BrickPlanet-Sniper.git
    cd BrickPlanet-Sniper
    ```

2. **Configure the sniper**: Open the `config.json` file and fill in your BrickPlanet username and password. This information is necessary for the bot to operate on your behalf. Additional accounts can be added or removed if desired. Proxies are also not essential, but will increase the speed at which the bot can query the site without being rate-limited.
   
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
        "username:password@10.0.0.1:8080"
      ]
    }
    ```
    
3. **Install Required Packages**: Make sure you have Python and pip installed. Then, install the necessary packages:
   
    ```bash
    pip install -r requirements.txt
    ```

4. **Running the sniper**: Launch the `sniper.py` file, and let the tool do the rest.
   
    ```bash
    python sniper.py
    ```

## Safety & Security

Your account security is of the highest importance. Your login credentials stored in the `config.json` file are only used to automate the login process and are not shared or transmitted anywhere.

## Disclaimer

Please use this bot responsibly and ethically. Adhere to the terms of service of BrickPlanet. I am not responsible for any actions taken against your account for misuse of this bot. Use at your own risk.

## License
[MIT](https://choosealicense.com/licenses/mit/)
