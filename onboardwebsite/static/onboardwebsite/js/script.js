// Validar formulario
const nombre = document.getElementById('nombre')
const apellido = document.getElementById('apellido')
const email = document.getElementById('correo')
const telefono = document.getElementById('telefono')
const mensajes = document.getElementById('mensajes')
const rut = document.getElementById('rut')
const form = document.getElementById('form')

let valida = document.querySelector('.mensajes')

form.addEventListener("submit", e=>{
  e.preventDefault()
  let warnings = ""
  let entrar = false
  let regexEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
  let regexRut = !/^[0-9]+[-|‐]{1}[0-9kK]{1}$/
  let regexTelefono = /^\d{9}$/
  if (nombre.value.length < 5) {
    warnings+= 'El nombre es muy corto <br>'
    entrar = true
  }
  if (nombre.value.length > 30) {
    warnings+= 'El nombre es muy largo <br>'
    entrar = true
  }
  if (apellido.value.length < 5) {
    warnings+= 'El apellido es muy corto <br>'
    entrar = true
  }
  if (apellido.value.length > 50) {
    warnings+= 'El apellido es muy largo <br>'
    entrar = true
  }
  if (!regexEmail.test(email.value)) {
    warnings+= 'El email no es valido <br>'
    entrar = true
  }
  if (!validarRut(rut.value)) {
    warnings+= 'El rut no es valido <br>'
    entrar = true
  }
  if (!regexTelefono.test(telefono.value)) {
    warnings+= 'El telefono debe tener 9 digitos <br>'
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


// funcion formatear rut
function formatRut(rut){
  rut.value=rut.value.replace(/[^0-9k]+/g, '')
  .replace( /^(\d{1,2})(\d{3})(\d{3})(\w{1})$/, '$1.$2.$3-$4')
}

// funcion formatear numero
function formatnumber(numero){
  numero.value=numero.value.replace(/[^0-9k]+/g, '')
}

//formatear nombre
function formatNombre(texto){
  texto.value=texto.value.replace(/[^A-Za-z]+/g, '')
}

//formatear apellido
function formatApellido(texto){
  texto.value=texto.value.replace(/[^A-Za-z ]+/g, '')
}

// funcion rut valido

function validarRut(rut){
  var tmp = rut.split('-');
  var contador = 0;
  var digv = tmp[1];
  var auxdg = 0;
  var rut = tmp[0];
  var rut = rut.split('.').join("");
  if (rut.length == 8) {
    contador+= parseInt(rut[7])*2;
    contador+= parseInt(rut[6])*3;
    contador+= parseInt(rut[5])*4;
    contador+= parseInt(rut[4])*5;
    contador+= parseInt(rut[3])*6;
    contador+= parseInt(rut[2])*7;
    contador+= parseInt(rut[1])*2;
    contador+= parseInt(rut[0])*3;
    auxdg = Math.floor(contador%11);
    auxdg = 11 - auxdg;
    if (auxdg == 10) {
      if (digv == "k") {
        return true;
      }else {
        return false;
      }
      
    }else if (auxdg == 11) {
      if (digv == "0" ) {
        return true;
      }else{
        return false;
      }
    }else {
      if (auxdg == parseInt(digv)) {
        return true;
      } else {
        return false;
      }
    }
  }
  else if (rut.length == 7) {
    contador+= parseInt(rut[6])*2;
    contador+= parseInt(rut[5])*3;
    contador+= parseInt(rut[4])*4;
    contador+= parseInt(rut[3])*5;
    contador+= parseInt(rut[2])*6;
    contador+= parseInt(rut[1])*7;
    contador+= parseInt(rut[0])*2;
    auxdg = Math.floor(contador%11);
    auxdg = 11 - auxdg;
    if (auxdg == 10) {
      if (digv == "k") {
        return true;
      }else {
        return false;
      }
      
    }else if (auxdg == 11) {
      if (digv == "0" ) {
        return true;
      }else{
        return false;
      }
    }else {
      if (auxdg == parseInt(digv)) {
        return true;
      } else {
        return false;
      }
    }
    
  }else{
    return false;
  }

}