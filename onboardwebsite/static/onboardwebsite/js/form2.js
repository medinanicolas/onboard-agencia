
const nombrecom = document.getElementById('nombrecom')
const email = document.getElementById('email')
const mensajito = document.getElementById('mensajito')
const mensajes = document.getElementById('mensajes')
const form2 = document.getElementById('form2')

let valida = document.querySelector('.mensajes')

form2.addEventListener("submit", e=>{
  e.preventDefault()
  let warnings = ""
  let entrar = false
  let regexEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
  if (!regexEmail.test(email.value)) {
    warnings+= 'El email no es valido <br>'
    entrar = true
  }
  if (nombrecom.value.length < 5) {
    warnings+= 'El nombre es muy corto <br>'
    entrar = true
  }
  if (nombrecom.value.length > 40) {
    warnings+= 'El nombre es muy largo <br>'
    entrar = true
  }
  if (mensajito.value.length < 20) {
    warnings+= 'El mensaje es muy corto <br>'
    entrar = true
  }  
  if(entrar) {
    mensajes.innerHTML = warnings 
  }
  if (!entrar) {
    alert('Formulario enviado correctamente')
    location.reload();
  }
})

function formatApellido(texto){
  texto.value=texto.value.replace(/[^A-Za-z ]+/g, '')
}