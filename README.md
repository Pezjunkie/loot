# loot
random loot generator

## Slack App Integration

This repository now includes a Slack app that integrates with the Gemini API to analyze messages in public and private channels.

### Setup

To use the Slack app, you need to:

1.  **Create a Slack app:** Create a new app in your Slack workspace and obtain the necessary credentials (Bot User OAuth Token and Signing Secret).
2.  **Get a Gemini API key:** Obtain an API key from Google AI Studio.
3.  **Set environment variables:** Set the following environment variables:
    *   `SLACK_BOT_TOKEN`: Your Slack app's Bot User OAuth Token.
    *   `SLACK_SIGNING_SECRET`: Your Slack app's Signing Secret.
    *   `GEMINI_API_KEY`: Your Gemini API key.
4.  **Run the app:** Run the `slack_app.py` file.

### Usage

Once the app is running and installed in your Slack workspace, it will automatically listen for messages in channels where it's added. To analyze a message, simply send it in the channel. The app will then:

1.  Send the message content to the Gemini API for analysis.
2.  Receive the analysis from Gemini.
3.  Post the analysis back to the Slack channel.

The analysis will be displayed in the channel, indicating the user who sent the original message.
