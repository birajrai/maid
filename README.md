# Maid

Maid is a Discord bot built with Python using the Discord.py library. It is designed to provide useful features to a Discord server, such as a birthday reminder system and a ping command.

## Features

- `>ping` command to check the bot's latency.
- Birthday reminder system that sends a message to a specified channel when it is someone's birthday.

## Installation

1. Clone the repository: `git clone https://github.com/birajrai/maid.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the project directory with the following contents:

token=`<your bot token>`

Replace `<your bot token>` with your actual bot token, which can be obtained from the Discord Developer Portal.

4. Update the `BIRTHDAYS` dictionary in `maid.py` with the names and birthdays of the people you want to track.

5. Update the `CHANNEL_ID` variable in `maid.py` with the ID of the channel where you want the birthday reminders to be sent.

## Usage

1. Run the bot with the command: `python maid.py`
2. Use the `>ping` command to check the bot's latency.
3. The bot will automatically send birthday messages to the specified channel when it is someone's birthday.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/birajrai/maid/blob/main/LICENSE) file for more information.
