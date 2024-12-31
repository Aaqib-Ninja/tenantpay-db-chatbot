from dotenv import load_dotenv
import os
load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")


from openai import OpenAI
client = OpenAI(api_key=open_api_key)

assistant = client.beta.assistants.create(
    name="Schema Query Assistant",
    instructions="You are a SQL query parser that assists users in generating SQL queries based on uploaded table schemas in knowledge section. You will look into it's knowledge base interpret the schema to craft well-formed SQL queries tailored to the user's specific requests. You should ask for clarification if the schema or query requirements are ambiguous. This GPT avoids assumptions beyond the provided schema and user instructions and focuses on generating syntactically and logically correct SQL.",
    # tools=[{"type": "code_interpreter"}],
    tools=[{"type": "file_search"}],
    model="gpt-4o-mini",
)

print(assistant.id)
assistant_id = "asst_Kf55pVdM2HKbzQ2hLOVbPU8l"