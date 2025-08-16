// Email Form
document.getElementById("emailForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let response = await fetch("/send-email/", {
        method: "POST",
        body: formData
    });
    let result = await response.json();
    document.getElementById("emailResponse").innerText = result.status;
});

// File Upload Form
document.getElementById("fileForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let response = await fetch("/upload-file/", {
        method: "POST",
        body: formData
    });
    let result = await response.json();
    document.getElementById("fileResponse").innerText = result.status;
});
