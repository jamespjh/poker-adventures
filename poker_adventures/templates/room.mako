<%inherit file="/base.mako"/>
<p>${c.main.text}</p>
% if c.main.challenge:
<div id="challenge">
	<div id="cards">
	<p id="chalpre">Try to beat the following cards with a poker hand:</p>
	% for card in c.main.challenge:
		<img class="card" src=${h.card_url(card)}></img>
	% endfor
	</div>
	<div id="boni">
	<p id="bonpre">Add the following cards to your hand as bonuses:</p>
	<ul>
	% for cause, bonus in c.main.boni.items():
	<li>${cause}: ${bonus} card(s)</li>
	% endfor
	</ul>
	</div>
</div>
% endif
<ul>
% for route, room in c.main.exits.items():
<li><a class="target" href=${room.url}>${route}</a></li>
% endfor
</ul>
</div>