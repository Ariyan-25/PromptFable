document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("darkModeToggle");

    if (!toggle) return;

    const isDark = localStorage.getItem("darkMode") === "true";
    updateTheme(isDark);

    toggle.addEventListener("click", () => {
        const current = document.documentElement.classList.toggle("dark");
        localStorage.setItem("darkMode", current);
        toggle.textContent = current ? "☀️ Light Mode" : "🌙 Dark Mode";
    });
});

function updateTheme(isDark) {
    if (isDark) {
        document.documentElement.classList.add("dark");
        document.getElementById("darkModeToggle").textContent = "☀️ Light Mode";
    } else {
        document.documentElement.classList.remove("dark");
        document.getElementById("darkModeToggle").textContent = "🌙 Dark Mode";
    }
}

// Typing effect
function showLoading() {
    const loading = document.getElementById("loading");
    const typing = document.getElementById("typing");
    loading.style.display = "block";
    typing.innerHTML = "";

    let dots = 0;
    setInterval(() => {
        dots = (dots + 1) % 4;
        typing.innerHTML = `<em>Writing the story${'.'.repeat(dots)}</em>`;
    }, 500);
}
