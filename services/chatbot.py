import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './chat_bot_private_key.json'

DIALOGFLOW_PROJECT_ID = 'firstchatbot-avbqqg'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


def chat(message):
    text_input = dialogflow.types.TextInput(
        text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print(response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text
