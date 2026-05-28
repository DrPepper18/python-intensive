from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
import uvicorn
import sqlite3
from client import client
from database import (
    get_all_messages,
    create_tables,
    send_message,
    add_sample_users
)


conn = sqlite3.connect("our_db.db", check_same_thread=False)
app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(client)

@app.get("/api")
def get_messages_endpoint(user_id: int):
    cursor = conn.cursor()
    try:
        messages = get_all_messages(user_id=user_id, cursor=cursor)
        result = []
        for msg in messages:
            result.append({
                "id": msg[0],
                "user_from_id": msg[1],
                "user_to_id": msg[2],
                "text": msg[3],
                "timestamp": msg[4]
            })
        return {"result": result}
    finally:
        cursor.close()


@app.post("/api")
def send_message_endpoint(user_id_from = Body(...), 
                          user_id_to = Body(...), 
                          text = Body(...)
                          ):
    cursor = conn.cursor()
    try:
        send_message(user_id_from, user_id_to, text, cursor)
        return {"status": "ok", "message": "Message sent successfully"}
    finally:
        cursor.close()


def main():
    cursor = conn.cursor()
    try:
        create_tables(cursor)
        add_sample_users(cursor)
    finally:
        cursor.close()
    
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()