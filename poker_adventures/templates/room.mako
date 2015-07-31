<%inherit file="/base.mako"/>
<p>${c.main.text}</p>
% if c.main.challenge:
<div id="challenge">
	<div id="cards">
	<p>Try to beat the following cards with a poker hand:</p>
	% for card in c.main.challenge:
		<img class="card" src=${h.card_url(card)}></img>
	% endfor
	</div>
	<div id="boni">
	<p>You start with one card in your hand.</p>
	<p>Add the following cards to your hand as bonuses:</p>
	<ul>
	% for cause, bonus in c.main.boni.items():
	<li>${cause}: ${bonus} card(s)</li>
	% endfor
	</ul>
	</div>
	<div class="results">
	<p>If you fail,
		<a class="target" href="${h.url(controller='room', room=c.main.name, action='fail')}">click here</a>
	</p>
	<p>Do not cheat: BEWARE SPOILERS</p>
	<p>The current time is ${h.now()}</p>
	<p>If you succeed, 
		<a class="target" href="${h.url(controller='room', room=c.main.success.name)}">click here</a>
	</p>
	</div>
</div>
% endif
<ul>
% for route, room in c.main.exits.items():
<li>
	<a class="target" href=${h.url(controller='room', room=room.name)}>${route}</a>
</li>
% endfor
</ul>
</div>