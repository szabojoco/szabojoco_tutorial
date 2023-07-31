const darkModeSwitch2 = document.getElementById("darkModeSwitch2");
const body = document.body;
const darkModeEnabled = localStorage.getItem("darkModeEnabled");

if (darkModeEnabled === "true") {
    body.classList.add("dark-mode");
    darkModeSwitch2.checked = true;
}

darkModeSwitch2.addEventListener("change", () => {
    if (darkModeSwitch2.checked) {
        body.classList.add("dark-mode");
        localStorage.setItem("darkModeEnabled", "true");
    } else {
        body.classList.remove("dark-mode");
        localStorage.setItem("darkModeEnabled", "false");
    }
});
