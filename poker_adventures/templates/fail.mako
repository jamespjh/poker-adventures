<%inherit file="/room.mako"/>
<h2> ${c.obstacle.failtext} </h2>

% if hasattr(c.obstacle, 'timer') and c.obstacle.timer:
<div id="timings">
	<p>You may not try again for ${c.obstacle.timer} minutes</p>
	<p>The current time is ${h.now()}</p>
	<p>You may try again at ${h.after(c.obstacle.timer)}<p>
	<p>Make a note of your retry time.</p>
</div>
% endif

<p id="continue"> <a class=target href=${h.url(controller='room', room=c.obstacle.fail)}>
	${c.obstacle.failcontinue}</a>
</p>