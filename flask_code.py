from flask import Flask, render_template, request
import json  # Working to JSON Files
from datetime import datetime  # For message timestamp

# INIT
app = Flask(__name__)

# GET
@app.route("/", defaults={"room": "general"})
@app.route("/<room>")
def get_room(room):
    return render_template("index.html")


# GET
@app.route("/api/chat/<room>", methods=["GET"])
def get_chat(room):
    with open("chat_data.json", "r") as chats_file:
        chat_data = json.load(chats_file)

    room_data = chat_data.get(room, [])  # Empty list if no room

    # Format each chat message according to the given format
    formatted_messages = [
        f'[{entry["timestamp"]}] {entry["username"]}: {entry["message"]}'
        for entry in room_data
    ]

    # Join all messages with a newline to make it readable
    response_content = "\n".join(formatted_messages)

    return response_content, 200, {"Content-Type": "text/plain"}


# POST
@app.route("/api/chat/<room>", methods=["POST"])
def send(room):
    # Loading the chat data from JSON
    with open("chat_data.json", "r") as chats_file:
        chat_data = json.load(chats_file)
    # Creation of the Room if it dose not exist:
    if room not in chat_data:
        chat_data[room] = []
    # Adds the message as dictionary
    new_message = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "username": request.form["username"],
        "message": request.form["msg"],
    }
    chat_data[room].append(new_message)

    # Writing back to the file in mode: Write
    with open("chat_data.json", "w") as file:
        json.dump(chat_data, file)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# Backup Debug
# username = request.form["username"]
# message = request.form["msg"]

# Print the values to the console for debugging
# print("Username:", request.form["username"])
# print("Message:", request.form["msg"])
