var broker = 'wss://mqtt.eclipseprojects.io:443/mqtt'; //intializing variable broker that holds the borker which is 'wss://mqtt.eclipseprojects.io:443/mqtt'
var client = mqtt.connect(broker); //initializing variable client that holds where the mqtt connect method to the specific broker
var status_header = document.getElementById('status-header') //intializing variable status_header that holds the element id of "status-header"

//now then check if we are now connected now to the broker
client.on('connect', function () {
  status_header.innerHTML = 'Connected to ' + broker; //then display the broker if we are connected successfully.
  console.log('Connected to ' + broker) //check if we are now connected to the broker
})

//Initializing variable sliders that holds the class name of "slider"
var sliders = document.getElementsByClassName("slider");

//initializing variable that handling two events
const events = {
  "mouseup": function(event){ //mouseup event : creating a  function that have a parameter of event 
    console.log(event.target.name, event.target.value); //console log or check 
    client.publish(`clueSlider/${event.target.name}`, event.target.value); //publish now the target topic or the name and its target value
  },
  "input": function(event) { //input element
    document.getElementById(event.target.name).innerHTML = event.target.value; 
  }
}

//loop all the sliders   
for(let slider of sliders){
  for(let key in events){ //loop the events variable to loop through all the events to get the specific event
    slider.addEventListener(key, events[key]); //slider.addEventListener(key, events[key])
  }
}
