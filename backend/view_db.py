# # import sqlite3

# # # Connect to the database
# # conn = sqlite3.connect("chat.db")
# # cursor = conn.cursor()

# # # Fetch all rows from the 'responses' table
# # cursor.execute("SELECT * FROM responses")
# # rows = cursor.fetchall()

# # # Print each row
# # for row in rows:
# #     print(row)

# # # Close the connection
# # conn.close()
# -------------------------------------
# import sqlite3

# def get_answer(question):
#     conn = sqlite3.connect("chat.db")
#     cursor = conn.cursor()
    
#     # Fetch the answer for a specific question
#     cursor.execute("SELECT answer FROM responses WHERE question = ?", (question,))
#     answer = cursor.fetchone()
    
#     conn.close()
    
#     if answer:
#         return answer[0]  # Return the answer text
#     else:
#         return "No answer found."

# # Test with a sample question
# question = "How can i contact to dr Heba ahmed elmatboley?"
# print(get_answer(question))
