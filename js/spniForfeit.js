/********************************************************************************
 This file contains the variables and functions that allow for players to have
 multiple potential forfeits.
 ********************************************************************************/
 
/**********************************************************************
 *****                 Forfeit Object Specification               *****
 **********************************************************************/

var CAN_SPEAK = true;
var CANNOT_SPEAK = false;
 
/**********************************************************************
 *****                      Forfeit Variables                     *****
 **********************************************************************/
 
/* locks */
var oneFinished = false;
 
/* orgasm timer */
var ORGASM_DELAY = 4000;
 
/* forfeit timers */
var timers = [0, 0, 0, 0];
 
/**********************************************************************
 *****                      Forfeit Functions                     *****
 **********************************************************************/

/************************************************************
 * Sets the forfeit timer of the given player, with a random
 * offset, if applicable.
 ************************************************************/
function setForfeitTimer (player) {
	// THE TIMER IS HARD SET RIGHT NOW
	timers[player] = players[player].timer;
	
	// THE STAGE IS HARD SET RIGHT NOW
	players[player].stage += 1;
}
 
/************************************************************
 * The forfeit timers of all players tick down, if they have 
 * been set.
 ************************************************************/
function tickForfeitTimers (context) {
    for (var i = 0; i < players.length; i++) {
        if (players[i].out && timers[i] > 0) {
            timers[i]--;
            
			if (i == HUMAN_PLAYER) {
				/* human player */
				if (timers[i] <= 0 && !oneFinished) {
					/* player's timer is up */
					oneFinished = true;
					console.log(players[i].first+" is finishing!");
					$gameClothingLabel.html("<b>You're 'Finished'</b>");
					
					/* save context */
					savedContext = context;
					context = null;
					
					/* set the button state */
					$mainButton.html("Continue");
					$mainButton.attr('disabled', true);
					
					/* finish */
					finishMasturbation(i);
				} else if (timers[i] <= 0) {
					/* two people can't finish at the same time */
					timers[i] = 1;
				} else {
					/* update the player label */
					$gameClothingLabel.html("<b>'Finished' in "+timers[i]+" phases</b>");
					
					if (players[HUMAN_PLAYER].gender == MALE) {
						updateAllBehaviours(i, MALE_MASTURBATING, [NAME], [players[i].first]);
					} else {
						updateAllBehaviours(i, FEMALE_MASTURBATING, [NAME], [players[i].first]);
					}
					updateAllGameVisuals();
				}
			} else {
				/* AI player */
				if (timers[i] <= 0 && !oneFinished) {
					/* this player's timer is up */
					oneFinished = true;
					console.log(players[i].first+" is finishing!");
					
					/* save context */
					savedContext = context;
					context = null;
					
					/* set the button state */
					$mainButton.html("Continue");
					$mainButton.attr('disabled', true);
					
					/* hide everyone else's dialogue bubble */
					for (var j = 1; j < players.length; j++) {
						if (i != j) {
							$gameDialogues[j-1].html("");
							$gameAdvanceButtons[j-1].css({opacity : 0});
							$gameBubbles[j-1].hide();
						}
					}
					
					/* let the player speak again */
					players[i].forfeit = [PLAYER_FINISHING_MASTURBATING, CAN_SPEAK];
					
					/* show them cumming */
					updateBehaviour(i, PLAYER_FINISHING_MASTURBATING, [NAME], [players[i].first]);
					updateGameVisual(i);
					
					/* trigger the callback */
					var player = i;
					window.setTimeout(function(){ finishMasturbation(player); }, ORGASM_DELAY);
				} else if (timers[i] <= 0) {
					/* two people can't finish at the same time */
					timers[i] = 1;
				} else {
					/* random chance they go into heavy masturbation */
					// CHANGE THIS TO ACTIVATE ONLY IN THE LAST 4 TURNS
					var randomChance = getRandomNumber(0, players[i].timer);
					
					if (randomChance > timers[i]-1) {
						/* this player is now heavily masturbating */
						players[i].forfeit = [PLAYER_HEAVY_MASTURBATING, CANNOT_SPEAK];
						updateBehaviour(i, PLAYER_HEAVY_MASTURBATING, [NAME], [players[i].first]);
						updateGameVisual(i);
					}
				}
			}
        }
    }
	
	return context;
}

/************************************************************
 * A player has 'finished' masturbating.
 ************************************************************/
function finishMasturbation (player) {
	// HARD SET STAGE
	players[player].stage += 1;

	/* update other player dialogue */
	if (players[player].gender == MALE) {
		updateAllBehaviours(player, MALE_FINISHED_MASTURBATING, [NAME], [players[player].first]);
	} else if (players[player].gender == FEMALE) {
		updateAllBehaviours(player, FEMALE_FINISHED_MASTURBATING, [NAME], [players[player].first]);
	}
	
	/* update their dialogue */
	if (player != HUMAN_PLAYER) {
		updateBehaviour(player, PLAYER_FINISHED_MASTURBATING, [NAME], [players[player].first]);
	}
	updateAllGameVisuals();
	
	/* update the button */
	$mainButton.html(savedContext);
	
	/* allow progression */
	$mainButton.attr('disabled', false);
	oneFinished = false;
}