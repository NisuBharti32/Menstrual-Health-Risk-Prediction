document.addEventListener("DOMContentLoaded", () => {
 

    const themeToggle = document.getElementById("themeToggle");
 
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark");
    } else {
        document.body.classList.remove("dark");
    } 
    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const isDark = document.body.classList.toggle("dark");

            localStorage.setItem("theme", isDark ? "dark" : "light");
        });
    } 
    const passwordInput = document.getElementById("password");
    const togglePassword = document.getElementById("togglePassword");

    if (passwordInput && togglePassword) {
        togglePassword.addEventListener("click", () => {

            const isHidden = passwordInput.type === "password";
            passwordInput.type = isHidden ? "text" : "password";

            togglePassword.classList.toggle("fa-eye", !isHidden);
            togglePassword.classList.toggle("fa-eye-slash", isHidden);

        });
    }

});


