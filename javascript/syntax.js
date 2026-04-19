document.getElementById("data").innerHTML = new Date();

function runCode() {
  const hora = new Date().getHours();
  let resultado;

  if (hora < 12) {
    resultado = "It's morning 🌅";
  } else if (hora < 18){
    resultado = "It's afternoon";
  } else {
    resultado = "night 🌙";
  }

  document.getElementById("result").textContent = resultado;
}