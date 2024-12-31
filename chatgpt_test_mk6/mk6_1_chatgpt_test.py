# from openai import OpenAI
# client = OpenAI()

# assistant = client.beta.assistants.create(
#     name="Schema Query Assistant",
#     instructions="You are a SQL query parser that assists users in generating SQL queries based on uploaded table schemas in knowledge section. You will look into it's knowledge base interpret the schema to craft well-formed SQL queries tailored to the user's specific requests. You should ask for clarification if the schema or query requirements are ambiguous. This GPT avoids assumptions beyond the provided schema and user instructions and focuses on generating syntactically and logically correct SQL.",
#     # tools=[{"type": "code_interpreter"}],
#     tools=[{"type": "file_search"}],
#     model="gpt-4o",
# )

from dotenv import load_dotenv
import os
load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

# 1/ Create an Assistant
from openai import OpenAI
client = OpenAI(api_key=open_api_key)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini",
)
print("1/ Create an Assistant")
print(assistant.id)

# 2/ Create a Thread
thread = client.beta.threads.create()
print("2/ Create a Thread")
print(thread.id)


# 3/ Add a Message to the Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
print("3/ Add a Message to the Thread")


# 4/ Create a Run (Without streaming)
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)
print("4/ Create a Run (Without streaming)")


# 5/ Get Output
if run.status == 'completed':
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    print(messages)
else:
    print(run.status)
    print("run")

print("5/ Get Output")
