# Discord to Twitter (X) bot

A Discord application using Disnake that allows users to queue tweet messages and send queued messages to twitter. Tweets in queue are automatically
sent after 1 hour.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

1. Clone the project repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Rename the `.env copy` file to `.env`.
4. Open the `.env` file and add your bot token along with your Twitter API Tokens.
5. Open `settings/config.py` and change config accordingly.

## Usage

Instructions on how to use the project or any relevant examples.

```python main.py```

## Bot commands

- `.tweet {message}` - Adds a tweet message to the queue (You are also able to insert media here)
- `.queue` - See queued tweets along with time remaining
- `.info {queue position}` - See more detailed information on the queue position
- `.swap {first queue position} {second queue position}` - Swaps queue positions
- `.push` - Force tweets the first position in the queue

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
