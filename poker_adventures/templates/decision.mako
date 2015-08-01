<%inherit file="/room.mako"/>
<p class = "preamble">Choose what to do:</p>
<ul>
% for route, room in c.obstacle.exits.items():
<li>
	<a class="target" href=${h.url(controller='room', room=room)}>${route}</a>
</li>
% endfor
</ul>