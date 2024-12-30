from dotenv import load_dotenv
import os
load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")


from openai import OpenAI
client = OpenAI(api_key=open_api_key)

# # 2/ Create a Thread
thread = client.beta.threads.create()
print(thread.id)

# assistant_id = "asst_Kf55pVdM2HKbzQ2hLOVbPU8l"
# thread_id = "thread_eHCEtico1d1PyyCRuVhNQzne"