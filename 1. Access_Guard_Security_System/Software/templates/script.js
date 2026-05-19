console.log("JavaScript Connected")

function updateClock()
{
	const now = new Date();
	const clock = document.getElementById("clock");
	
	clock.innerHTML = now.toLocaleTimeString('en-US',
	{
		hour:'2-digit',
		minute: '2-digit',
		second: '2-digit'}
	);	
}
setInterval(updateClock,1000);
updateClock();
	