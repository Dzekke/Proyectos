var canvas;
//ctx =contexto
var ctx;
var fps=50;
var imgZoro;

function inicializar() {
	canvas=document.getElementById('canvas');
	ctx=canvas.getContext("2d");

   imgZoro = new Image();
   imgZoro.src = "img/zoro.png";

	setInterval(function(){
		principal();
	},1000/fps);
}


var protagonista=function(x,y){
	this.x=x;
	this.y=y;
	this.velocidad=3; //3px

	this.dibujaProta=function(){
     ctx.drawImage(imgZoro,this.x,this.y);
	}
 	
 	this.mensaje= function(){
 		ctx.font= "30px impact";
 		ctx.fillStyle="#555555";
 		ctx.fillText("x: " + this.x  + "y: " + this.y ,50,85); //100,100 posicion en la que se muestra el texto
 	}

 	this.arriba=function(){
 		this.y-=this.velocidad;
 	}

 	this.abajo=function(){
 		this.y+=this.velocidad;
 	}

 	this.izquierda=function(){
 		this.x-=this.velocidad;
 	}

 	this.derecha=function(){
 		this.x+=this.velocidad;
 	}
}


//ENEMIGOS(CUBOS ROJOS)
personaje=function(x,y){
	this.x=x;
	this.y=y;
	this.derecha=true;
   //metodo para dibujar un rectangulo
	this.dibuja = function(){
		ctx.fillStyle="#FF0000";//color rojo 
		ctx.fillRect(this.x,this.y,50,50);//posicion x,posicion y ,largo,ancho del rectangulo
	}

   this.mueve=function(velocidad){

   if (this.derecha==true) {
   	if (this.x < 400) 
   		this.x+=velocidad;
   
   else{
   	this.derecha=false;
   }
}
 else{
 	if (this.x>50)
 		this.x-=velocidad;
 	else{
 		this.derecha=true;//si se cambia false solo da una vuelta
 	 }
    }
   }
 }
   /*this.mueveIzquierda=function(velocidad){
   	this.y+=velocidad;
   }*/

var per1 = new personaje(10,100); //posicion x,y del personaje 1
var per2 = new personaje(10,200); //posicion x,y del personaje 2
var per3 = new personaje(10,300); //posicion x,y del personaje 3

var prota = new protagonista(200,200);


//lectura por teclado
document.addEventListener("keydown",function(tecla){
	if (tecla.keyCode==38) {
		prota.arriba();
	}
	if (tecla.keyCode==40) {
		prota.abajo();
	}
	if (tecla.keyCode==37) {
		prota.izquierda();
	}
	if (tecla.keyCode==39) {
		prota.derecha();
	}
});


function borraCanvas(){
	canvas.width=500;
	canvas.height=400;
}

function principal(){
	//console.log("funciona");
	borraCanvas();

	per1.dibuja();
	per2.dibuja();
	per3.dibuja();
    per1.mueve(1);
    per2.mueve(5);
    per3.mueve(10);
    prota.dibujaProta();
    prota.mensaje();
    
}