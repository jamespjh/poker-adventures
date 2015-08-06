<%inherit file="/room.mako"/>
<a href=${h.url(controller='room', room=c.obstacle.choose())}>
	${c.obstacle.prompt}
</a>