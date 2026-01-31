function addJob() {
    fetch("http://127.0.0.1:5000/add-job", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            title: document.getElementById("title").value,
            location: document.getElementById("location").value,
            salary: document.getElementById("salary").value,
            contact: document.getElementById("contact").value
        })
    }).then(res => res.json())
      .then(data => alert(data.message));
}

fetch("http://127.0.0.1:5000/get-jobs")
.then(res => res.json())
.then(data => {
    let jobDiv = document.getElementById("jobs");
    if (!jobDiv) return;

    data.forEach(job => {
        jobDiv.innerHTML += `
            <div class="job">
                <h4>${job.title}</h4>
                <p>${job.location} | ${job.salary}</p>
                <p>Contact: ${job.contact}</p>
                <button>Apply</button>
            </div>
        `;
    });
});
