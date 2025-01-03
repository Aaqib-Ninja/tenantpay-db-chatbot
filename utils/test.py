

def format_input(input_text, bot_user_id):
    full_bot_id = "<@" + bot_user_id + ">"
    input_text = input_text.replace(full_bot_id, "")
    msg = "Can me provide me an sql statement from the schemas uploaded in your files for the following question?\n"
    msg += input_text
    return msg


input_text = """Can me provide me an sql statement from the schemas uploaded in your files for the following question?
<@U086W0UJ7FG>
What are names 10 of the residents who lives in units?"""


print(format_input(input_text, "U086W0UJ7FG"))


from sql_helper import SQLUtils
processed_sql="""
SELECT u.*
FROM users u
JOIN companies c ON u.companyId = c.companyId
WHERE c.name = 'Apex Property Management & Consulting Inc' AND u.role = 'admin';
"""

sql_utils = SQLUtils()
is_safe_select = sql_utils.is_safe_select(processed_sql)
print("is_safe_select:", is_safe_select)