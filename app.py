from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_jobs():
    try:
        with open("jobs.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_jobs(jobs):
    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

@app.route("/add-job", methods=["POST"])
def add_job():
    job = request.json
    jobs = load_jobs()
    jobs.append(job)
    save_jobs(jobs)
    return jsonify({"message": "Job Added Successfully"})

@app.route("/get-jobs", methods=["GET"])
def get_jobs():
    return jsonify(load_jobs())

@app.route("/delete-job", methods=["POST"])
def delete_job():
    title = request.json["title"]
    jobs = load_jobs()
    jobs = [j for j in jobs if j["title"] != title]
    save_jobs(jobs)
    return jsonify({"message": "Job Deleted"})

if __name__ == "__main__":
    app.run(debug=True)
