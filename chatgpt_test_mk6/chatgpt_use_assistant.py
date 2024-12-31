from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=open_api_key)

assistant_id = "asst_Kf55pVdM2HKbzQ2hLOVbPU8l"
thread_id = "thread_eHCEtico1d1PyyCRuVhNQzne"

print("3/ Add a Message to the Thread")

# 4/ Create a Run (Without streaming)
run = client.beta.threads.runs.create_and_poll(
    # thread_id=thread.id,
    # assistant_id=assistant.id,
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)
print("4/ Create a Run (Without streaming)")
print(run.id)



# 5/ Get Output
if run.status == 'completed':
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    print(messages)
else:
    print(run.status)
    print("run")

print("5/ Get Output")

print(run)
