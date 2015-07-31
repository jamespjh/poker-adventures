<%inherit file="/base.mako"/>
<p>${c.main.text}</p>

<div class="starts">
<p class="start-prompt">Starting points:</p>
% for room in c.main.starts:
<p>${room.title}</p>
% endfor
</div>