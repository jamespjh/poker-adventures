<%inherit file="/room.mako"/>
<h1>Enter the required information:</h1>

${h.form(h.url(controller='room', room=c.main.name, action='submit'), method='get')}
<ul>
% for prompt in c.obstacle.requirements:
<li>${prompt}: ${h.text(prompt)}</li>
% endfor
</ul>
<p>${h.submit('submit', 'Submit')}</p>
${h.end_form()}

<p>If you do not know the answers,
	<a class="target" href="${h.url(controller='room', room=c.obstacle.fail)}">
		click here
	</a>
</p>