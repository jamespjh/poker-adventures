<%inherit file="/base.mako"/>
<p>${c.main.text}</p>

<div class="starts">

<p class="start-prompt">Starting points:</p>
<ul>
% for room in c.main.starts:
<li>
	<a class="target" href=${h.url(controller='room', room=room.name)}>${room.title}</a>
</li>
% endfor
<ul>
</div>