from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_groq import ChatGroq

load_dotenv()

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project and FireStore Database
3. Retrieve the Project ID
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    
    - gcloud --version
    - gcloud auth application-default login
    - gcloud config set project langchain-test-52c5c (PROJECT_ID)

    - Set your default project to the new Firebase project you created
5. pip install langchain-google-firestore
6. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""
# Initialize Firestore
PROJECT_ID = "langchain-test-52c5c"
SESSION_ID = "user_session_new_2"  # This could be a username or a unique ID (change SESSION_ID for new user)
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
model = ChatGroq(model="mixtral-8x7b-32768")

print("Start chatting with the AI. Type '/bye' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "/bye":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(str(ai_response.content))

    print(f"AI: {ai_response.content}")