document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.querySelector("form[name='signup_form']");

  if (typeof registerForm != "null") {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();
      let form = e.target;
      let error = document.querySelector("form .error");
      let data = serialize(form);

      console.log(data);
      fetch("http://127.0.0.1:5000/user/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
      })
        .then((response) => response.json())
        .then((data) => {
          if (typeof data["error"] != "undefined") {
            error.textContent = data["error"];
            error.classList.remove("error--hiden");
          } else {
            window.location.href = "/";
            error.classList = "error error--hiden";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }

  const loginform = document.querySelector("form[name='signin_form']");
  if (typeof loginform != "undefined") {
    loginform.addEventListener("submit", (e) => {
      e.preventDefault();
      alert("here");
      let form = e.target;
      let error = document.querySelector("form .error");
      let data = serialize(form);

      fetch("http://127.0.0.1:5000/user/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
      })
        .then((response) => response.json())
        .then((data) => {
          if (typeof data["error"] != "undefined") {
            error.textContent = data["error"];
            error.classList.remove("error--hiden");
          } else {
            window.location.href = "/";
            error.classList = "error error--hiden";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }
});
