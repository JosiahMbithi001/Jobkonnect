
  var passwordInput = document.getElementById("password");
  var confirmPasswordInput = document.getElementById("confirm_password");
  var passwordError = document.getElementById("password_error");

  // Add an event listener to the confirm password field
  confirmPasswordInput.addEventListener("keyup", function() {
    var password = passwordInput.value;
    var confirmPassword = confirmPasswordInput.value;

    // Check if the passwords match
    if (password !== confirmPassword) {
      passwordError.textContent = "Passwords do not match.";
    } else {
      passwordError.textContent = ""; // Clear the error message
    }
  });
