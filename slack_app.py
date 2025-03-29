import os
from slack_bolt import App
import google.generativeai as genai

# Initialize Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to all incoming messages
@app.message("")
def message_handler(message, say):
    # Extract the text content of the message
    text = message['text']
    channel_id = message['channel']
    user_id = message['user']

    try:
        # Send the message to Gemini for analysis
        response = model.generate_content(f"Analyze the following Slack message: '{text}'")
        analysis = response.text

        # Post the analysis back to the channel
        say(f"Analysis of message from <@{user_id}> in <#{channel_id}>: '{analysis}'")
    except Exception as e:
        # Handle errors from Gemini API
        say(f"Error analyzing message: {e}")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))