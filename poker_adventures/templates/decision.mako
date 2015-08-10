<%inherit file="/room.mako"/>
% if len(c.obstacle.exits) > 1:
<h2>Choose what to do:</h2>
% else:
<h2>Continue:</h2>
% endif
<ul>
% for route, room in c.obstacle.exits.items():
<li>
	<a class="target" href=${h.url(controller='room', room=room)}>${route}</a>
</li>
% endfor
</ul>