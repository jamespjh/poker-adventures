<%inherit file="/room.mako"/>
<p> You have failed. </p>

% if hasattr(c.obstacle, 'timer') and c.obstacle.timer:
<div id="timings">
	<p>You may not try again for ${c.obstacle.timer} minutes</p>
	<p>The current time is ${h.now()}</p>
	<p>You may try again at ${h.after(c.obstacle.timer)}<p>
	<p>Make a note of your retry time.</p>
</div>
% endif

<p> <a class=target href=${h.url(controller='room', room=c.obstacle.fail)}>
	Click here to let someone else try</a>
</p>