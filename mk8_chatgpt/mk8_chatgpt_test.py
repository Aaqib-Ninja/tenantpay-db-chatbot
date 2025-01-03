from mk8_chatgpt_helper import OpenAIUtils
from mk8_chatgpt_helper import extract_sql_statement, execute_sql
import pandas as pd

# assistant_id="asst_86Ozc971ubLv1TE48XEfLwAd"
# # thread_id = "thread_iRlqdnjJejbZ96CLGV5Ytx6F"
# # msg = "Can you fetch the imported bank transactions for the month of October?"
# msg = "Can me provide me an sql statement from the schemas uploaded in your files for the following question?\n"
# # msg +="Can you tell me which unit is user Lucas assigned to?"
# msg +="What are names 10 of the residents who lives in units?"

# utils = OpenAIUtils()

# thread = utils.create_thread()

# print(thread.id)

# run = utils.converse(assistant_id=assistant_id, thread_id=thread.id, msg=msg)
# messages = utils.client.beta.threads.messages.list(thread_id=thread.id)


# raw_gpt_output = messages.data[0].content[0].text.value
# print("raw_gpt_output")
# print(raw_gpt_output)

# processed_sql = extract_sql_statement(raw_gpt_output)
# print("processed_sql")
# print(processed_sql)


queries = [
"""
    SELECT residentid
    FROM residents
    WHERE firstName="John";
""",
"""
    SELECT lastName
    FROM residents
    WHERE firstName="John";
""",
"""
    SELECT companyid
    FROM residents
    WHERE firstName="John";
""",
]

# processed_sql="""
# SELECT 
#     t.*,
#     ibt.*
# FROM 
#     transactions t
# LEFT JOIN 
#     imported_bank_transactions ibt ON t.transactionId = ibt.transactionId
# WHERE 
#     t.transactionId = 250;"""
query_output_dict_list = []

for query in queries:
    headers, data = execute_sql(query)
    table = [dict(zip(headers, row)) for row in data]
    query_output_dict_list.extend(table)
    
df = pd.DataFrame(query_output_dict_list)
df = df.astype(str)
df.fillna("null", inplace=True)

output_file = "query_outputs.xlsx"
df.to_excel(output_file, index=False)
