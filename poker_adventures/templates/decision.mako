<%inherit file="/room.mako"/>
<h2>Choose what to do:</h2>
<ul>
% for route, room in c.obstacle.exits.items():
<li>
	<a class="target" href=${h.url(controller='room', room=room)}>${route}</a>
</li>
% endfor
</ul>