from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/")
def home():
    return jsonify(message="Task Manager API v2 is running", version="1.0")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify(error="title is required"), 400
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return jsonify(message="deleted")
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
