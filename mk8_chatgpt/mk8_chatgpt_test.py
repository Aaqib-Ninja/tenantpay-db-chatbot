from mk8_chatgpt_helper import OpenAIUtils
from mk8_chatgpt_helper import extract_sql_statement, execute_sql


assistant_id="asst_86Ozc971ubLv1TE48XEfLwAd"
# thread_id = "thread_iRlqdnjJejbZ96CLGV5Ytx6F"
# msg = "Can you fetch the imported bank transactions for the month of October?"
msg = "Can me provide me an sql statement from the schemas uploaded in your files for the following question?\n"
# msg +="Can you tell me which unit is user Lucas assigned to?"
msg +="What are names 10 of the residents who lives in units?"

utils = OpenAIUtils()

thread = utils.create_thread()

print(thread.id)

run = utils.converse(assistant_id=assistant_id, thread_id=thread.id, msg=msg)
messages = utils.client.beta.threads.messages.list(thread_id=thread.id)


raw_gpt_output = messages.data[0].content[0].text.value
print("raw_gpt_output")
print(raw_gpt_output)

processed_sql = extract_sql_statement(raw_gpt_output)
print("processed_sql")
print(processed_sql)

query_output = execute_sql(processed_sql)
print("query_output")
print(query_output)
