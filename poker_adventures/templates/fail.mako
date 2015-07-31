<%inherit file="/base.mako"/>
<p> You have failed </p>

<div id="timings">
	<p>You may not try again for ${c.main.timer} minutes</p>
	<p>The current time is ${h.now()}</p>
	<p>You may try again at ${h.after(c.main.timer)}<p>
	<p>Make a note of your retry time.</p>
</div>

<p> <a class=target href=${h.url(controller='room', room=c.main.fail.name)}>
	Click here to let someone else try</a>
</p>