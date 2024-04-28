# Aqua Sniper - A Rare Item Sniper for BrickPlanet

## Description
Aqua Sniper is a sophisticated tool designed to help you automatically secure any new rare items on BrickPlanet with 
ease. The sniper will run in the background, continuously checking for new rares, and purchasing them the moment they 
are detected.

## Features
- **Automatic Purchasing**: Automatically checks for and purchases new rare items released in the shop.
- **Multi-Account Functionality**: Allows for an unlimited number of accounts to be added and used for sniping.
- **Support for Proxies**: Proxies can be added to obscure who is making repeated requests.
- **Daily Login Rewards**: Reauthenticates each account every 24 hours to ensure you get your daily login rewards.

## Installation and Setup
   1. **Download the latest release**: Download and unzip the [latest release](https://github.com/AndyAnderson8/Aqua-Sniper/releases/)
      to your machine and enter the directory.

   2. **Configure the sniper**: Open the `credentials.yaml` file and fill in your BrickPlanet username and password. 
      This information is necessary for the bot to operate on your behalf. Additional accounts can be added or removed 
      if desired. Proxies are also not essential, but will increase the speed at which the bot can query the site without 
      being rate-limited.
   
       ```yaml
          users:
            - username: user1
              password: pass1
        
            - username: user2
              password: pass2
       ```
      
      If proxies are desired, they may be added directly below user credentials, as so:
   
      ```yaml
          proxies:
            - "username:password@192.168.0.1:8080"
            - "username:password@192.168.0.1:8081"
      ```

      Please note, while proxies may be added, they are not necessary for standard operation.

   3. **Run the sniper**: Launch the `BrickPlanet-AIO.exe` file, and let the tool do the rest.

## Safety & Security
Your account security is of the highest importance. Your login credentials stored in the `credentials.yaml` file are 
only used to automate the login process and are not shared or transmitted anywhere.

## Disclaimer
Please use this bot responsibly and ethically. Adhere to the terms of service of BrickPlanet. I am not responsible for 
any actions taken against your account for misuse of this bot. Use at your own risk.

## License
[MIT](https://github.com/AndyAnderson8/BrickPlanet-Sniper/blob/main/LICENSE)
