document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("modeSwitch").addEventListener("change", (e) => {
    document.body.classList.toggle("dark", e.target.checked);
    document.getElementById("modeLabel").textContent = e.target.checked ? "Dark Mode" : "Light Mode";
  });

  showTab("dashboard");

  loadVPSStatus();
});

function showTab(tabId) {
  document.querySelectorAll(".tab-content").forEach(el => el.classList.remove("active"));
  document.getElementById(tabId).classList.add("active");
}

function appendToTerminal(text) {
  const out = document.getElementById("statusOutput");
  out.innerHTML += `> ${text}<br/>`;
  out.scrollTop = out.scrollHeight;
}

function loadVPSStatus() {
  const list = document.getElementById("vpsList");
  const vpsMock = ["192.168.1.2", "192.168.1.3", "192.168.1.4"];
  list.innerHTML = "";
  vpsMock.forEach(ip => {
    const li = document.createElement("li");
    li.textContent = `${ip} ✅`;
    list.appendChild(li);
  });
}

function runTask() {
  const ip = document.getElementById("ip").value;
  const port = document.getElementById("port").value;
  const time = document.getElementById("time").value;
  appendToTerminal(`Task started: ./run ${ip} ${port} ${time} 24`);
  setTimeout(() => appendToTerminal(`✅ Task completed on 3 VPS`), 3000);
}

function generateKey() {
  const hours = document.getElementById("hours").value;
  const limit = document.getElementById("limit").value;
  const key = `KEY-${Math.random().toString(36).substr(2, 8).toUpperCase()}`;
  document.getElementById("keyOutput").textContent = `Generated: ${key}\nDuration: ${hours}h\nLimit: ${limit}`;
}
