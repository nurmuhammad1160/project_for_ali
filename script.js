function submitCode() {
  const codeInput = document.getElementById("code");
  const errorText = document.getElementById("error");

  if (codeInput.value.trim() === "") {
    errorText.style.display = "block";
  } else {
    errorText.style.display = "none";
    alert("Код принят: " + codeInput.value);
    // Здесь можно отправить код на сервер
  }
}
