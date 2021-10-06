//https://www.eclipse.org/paho/clients/js/

function Sensor_On() {

  var EtiquetaSensor1=document.getElementById("sensor1");
  var HiddenSensor1=EtiquetaSensor1.getAttribute("hidden");

  var EtiquetaSensor2=document.getElementById("sensor2");
  var HiddenSensor2=EtiquetaSensor2.getAttribute("hidden");

  if(HiddenSensor1 || HiddenSensor2){
    EtiquetaSensor1.removeAttribute("hidden");
    EtiquetaSensor2.removeAttribute("hidden");
  }else{
    EtiquetaSensor1.setAttribute("hidden", "hidden");
    EtiquetaSensor2.setAttribute("hidden", "hidden");
  }

  }

function Historial_On(){
	
	
	//alert("led off");
	console.log("led off");
	message = new Paho.MQTT.Message("RegistroSensores");
    	message.destinationName = "altairlbn2020@gmail.com/t2";
    	client.send(message);
}	

// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "altairlbn2020@gmail.com",
    password: "Onepiece746",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
	
    client.subscribe("altairlbn2020@gmail.com/t1");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "altairlbn2020@gmail.com/t2";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }
// called when a message arrives
function onMessageArrived(message) {
    console.log("onMessageArrived:"+message.payloadString);//Se muestra en la consola el mensaje recibido
    
    var mensaje=message.payloadString;//Se guarda el mensaje en una variable
    var registro=mensaje.split('_');
    if (registro[0]==("Registro")){//Cuando se conecta por primera vez a la tarjeta
      document.getElementById("historial").innerHTML=registro[1];//Muestra un mensaje de recibido en la web
    }
    var sensores=mensaje.split('-');//Divide el formato en que llegan los valores a razón del espacio en blanco
    document.getElementById("sensor1").innerHTML=sensores[0];//Muestra el primer valor en la etiqueta
    document.getElementById("sensor2").innerHTML=sensores[1];//Muestra el segundo valor en la etiqueta
	
	}

