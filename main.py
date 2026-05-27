from fastapi import FastAPI, Body
import uvicorn
import sqlite3
from database import (
    get_all_messages,
    create_tables,
    send_message
)

conn = sqlite3.connect("our_db.db", check_same_thread=False)
app = FastAPI()

@app.get("/api")
def get_messages_endpoint(user_id: int):
    cursor = conn.cursor()
    return {"result": get_all_messages(user_id=user_id, cursor=cursor)}

@app.post("/api")
def send_message_endpoint(user_id_from = Body(...), 
                          user_id_to = Body(...), 
                          text = Body(...)
                          ):
    cursor = conn.cursor()
    send_message(user_id_from, user_id_to, text, cursor)

def main():
    cursor = conn.cursor()
    create_tables(cursor)
    uvicorn.run(app)

main()