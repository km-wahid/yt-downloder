document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("download-form");
  const statusText = document.getElementById("status");

  form.onsubmit = async function (e) {
    e.preventDefault();
    statusText.innerText = "Starting download...";
    const formData = new FormData(form);
    const response = await fetch("/start-download", {
      method: "POST",
      body: formData,
    });
    const { download_id } = await response.json();

    const interval = setInterval(async () => {
      const res = await fetch(`/check-progress/${download_id}`);
      if (res.headers.get("Content-Type").includes("application/json")) {
        const data = await res.json();
        if (data.status === "done") {
          statusText.innerText = "Download complete!";
          clearInterval(interval);
        } else {
          statusText.innerText = `Progress: ${data.status}`;
        }
      } else {
        const blob = await res.blob();
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "download.mp4";
        a.click();
        statusText.innerText = "Downloaded!";
        clearInterval(interval);
      }
    }, 1000);
  };
});
