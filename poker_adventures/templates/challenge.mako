<%inherit file="/room.mako"/>
<div class="obstacle">
	<div id="cards">
	<h2>Try to beat the following cards with a poker hand:</h2>
	% for card in c.obstacle.cards:
		<img class="card" src=${h.card_url(card)}></img>
	% endfor
	</div>
	<div id="boni">
	<p>You start with one card in your hand. 
	Add one card per teammate and any universal bonuses.
	If you've already succeeded in this challenge, there's no need to check again.</p>
	% if c.obstacle.boni:
	<p>The following special abilities also apply:</p>
	<ul>
	% for cause in c.obstacle.boni:
	<li>${cause}</li>
	% endfor
	</ul>
	%endif
	</div>
	<div class="results">
	<p>If you fail,
		<a class="target" href="${h.url(controller='room', room=c.main.name, action='fail')}">click here</a>
	</p>
	<p>Do not cheat: BEWARE SPOILERS</p>
	<p>The current time is ${h.now()}</p>
	<p>If you succeed, 
		<a class="target" href="${h.url(controller='room', room=c.obstacle.success)}">click here</a>
	</p>
	</div>
</div>