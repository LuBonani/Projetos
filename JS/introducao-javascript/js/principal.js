var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

var paciente = document.querySelectorAll(".paciente");

for(var i=0; i < paciente.length; i++){

	var altura = paciente[i].querySelector(".info-altura").textContent;
	var peso = paciente[i].querySelector(".info-peso").textContent;

	if(peso <= 0 || peso >= 400 ){
		paciente[i].querySelector(".info-imc").textContent = "Peso invalido";
		paciente[i].classList.add("paciente-invalido"); //adicionando classe para modificar o style no css
	} else if(altura <= 0 || altura >= 3.0){
		paciente[i].querySelector(".info-imc").textContent = "Altura invalida";
		paciente[i].classList.add("paciente-invalido"); //adicionando classe para modificar o style no css
		
	} else{
		var imc = peso / (altura * altura);
		paciente[i].querySelector(".info-imc").textContent = imc.toFixed(2);  // toFixed limita as casas decimais
	}

}
/*
titulo.addEventListener("click", function (){      //event listener
	console.log("Olá, fui clicado" + "  " + "função anonima") // função anonima
}); 
*/

var botaoAdicionar = document.querySelector("#adicionar-paciente");
botaoAdicionar.addEventListener("click", function(event){
	event.preventDefault();  //previne comportamento padrão
	console.log("cliquei");
});
