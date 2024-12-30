from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=open_api_key)


run = client.beta.threads.runs.retrieve(
        run_id="run_4ETWxU9RzpuO4TkoCNem07EB", thread_id="thread_91El0GYDWjgusgVDwoWsHJ8o"
    )

print(run)
