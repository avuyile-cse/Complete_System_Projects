console.log("JavaScript Connected")

function updateClock()
{
	const now = new Date();
	const clock = document.getElementById("clock");
	
	clock.innerHTML = now.toLocaleTimeString('en-GB');	
}
setInterval(updateClock,1000);
updateClock();
	