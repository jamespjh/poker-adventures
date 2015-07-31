<%inherit file="/base.mako"/>
<p>${c.main.text}</p>

<ul>
% for route, room in c.main.exits.items():
<li><a class="target" href=${room.url}>${route}</a></li>
% endfor
</ul>
</div>