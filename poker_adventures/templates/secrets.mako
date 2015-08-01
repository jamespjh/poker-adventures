<%inherit file="/room.mako"/>
<h2>Enter the required information:</h2>

${h.form(h.url(controller='room', room=c.main.name, action='submit'), method='get')}
<ul>
% for prompt in c.obstacle.requirements:
<li>${prompt}: ${h.text(prompt, autocomplete = 'off')}</li>
% endfor
</ul>
<p>${h.submit('submit', 'Submit')}</p>
${h.end_form()}

<p>If you do not know the answers,
	<a class="target" href="${h.url(controller='room', room=c.obstacle.fail)}">
		click here
	</a>
</p>