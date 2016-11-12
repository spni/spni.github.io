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

/* The first and last rounds a character starts heavy masturbation, counted in phases before they finish */
var HEAVY_FIRST_ROUND = 6
var HEAVY_LAST_ROUND = 2
 
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
    if (player == HUMAN_PLAYER) {
      $gamePlayerCountdown.html(timers[player]);
    }
	
	// THE STAGE IS HARD SET RIGHT NOW
	players[player].stage += 1;
}

/************************************************************
 * Sleep for the specified amount of time in milliseconds.
 * Blocks the thread.
 ************************************************************/
function blockingSleep(time){
	var now = new Date().getTime();
    while(new Date().getTime() < now + time){ /* wait */ }
}

/************************************************************
 * The forfeit timers of all players tick down, if they have 
 * been set.
 ************************************************************/
function tickForfeitTimers (context) {
    var masturbatingPlayers = [];
	var showMasturbatingThreshold = 0.2; //probability of doing a "this character is masturbating" event
	var masturbationDelay = 400; //wait for 400ms so that the player can see what the characters are saying
	
    for (var i = 0; i < players.length; i++) {
        if (players[i] && players[i].out && timers[i] > 0) {
        	timers[i]--;
            
			if (i == HUMAN_PLAYER) {
				/* human player */
				if (timers[i] <= 0 && !oneFinished) {
					/* player's timer is up */
                    $gamePlayerCountdown.hide();
					oneFinished = true;
					console.log(players[i].label+" is finishing!");
					$gameClothingLabel.html("<b>You're 'Finished'</b>");
					
					/* save context */
					savedContext = context;
					context = null;
					
					/* set the button state */
					$mainButton.html("Continue");
					$mainButton.attr('disabled', false);
					actualMainButtonState = false;
					
					/* finish */
					finishMasturbation(i);
				} else if (timers[i] <= 0) {
					/* two people can't finish at the same time */
					timers[i] = 1;
				} else {
					/* update the player label */
					$gameClothingLabel.html("<b>'Finished' in "+timers[i]+" phases</b>");
				    $gamePlayerCountdown.html(timers[i]);	
                  
					if (players[HUMAN_PLAYER].gender == eGender.MALE) {
						updateAllBehaviours(i, MALE_MASTURBATING, [NAME], [players[i].label]);
					} else {
						updateAllBehaviours(i, FEMALE_MASTURBATING, [NAME], [players[i].label]);
					}
					updateAllGameVisuals();
				}
			} else {
				/* AI player */
				if (timers[i] <= 0 && !oneFinished) {
					/* this player's timer is up */
					oneFinished = true;
					console.log(players[i].label+" is finishing!");
					
					/* save context */
					savedContext = context;
					context = null;
					
					/* set the button state */
					$mainButton.html("Continue");
					$mainButton.attr('disabled', false);
					actualMainButtonState = false;
					
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
					updateBehaviour(i, PLAYER_FINISHING_MASTURBATING, [NAME], [players[i].label]);
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
					var randomChance = getRandomNumber(HEAVY_LAST_ROUND, HEAVY_FIRST_ROUND);
					
					if (randomChance > timers[i]-1) {
						/* this player is now heavily masturbating */
						players[i].forfeit = [PLAYER_HEAVY_MASTURBATING, CANNOT_SPEAK];
						updateBehaviour(i, PLAYER_HEAVY_MASTURBATING, [NAME], [players[i].label]);
						updateGameVisual(i);
					}
					
					masturbatingPlayers.push(i);
				}
			}
        }
    }
	
	//show an NPC player masturbating, if there is one available and the chance is met
	if (masturbatingPlayers.length > 0 && Math.random() < showMasturbatingThreshold){
		var playerToShow = masturbatingPlayers[getRandomNumber(0, masturbatingPlayers.length)];//index of player chosen to show masturbating//players[]
		for (var i = 0; i < players.length; i++){
			updateBehaviour(i, (i == playerToShow) ? players[i].forfeit[0] : (players[playerToShow].gender == eGender.MALE ? MALE_MASTURBATING : FEMALE_MASTURBATING), [NAME], [players[playerToShow].label]);
		}
		updateAllGameVisuals();
		blockingSleep(masturbationDelay); // wait so that you can see what they say
	}
	
	return context;
}

/************************************************************
 * A player has 'finished' masturbating.
 ************************************************************/
function finishMasturbation (player) {
	// HARD SET STAGE
	players[player].stage += 1;
    players[player].forfeit = [PLAYER_FINISHED_MASTURBATING, CAN_SPEAK];

	/* update other player dialogue */
	if (players[player].gender == eGender.MALE) {
		updateAllBehaviours(player, MALE_FINISHED_MASTURBATING, [NAME], [players[player].label]);
	} else if (players[player].gender == eGender.FEMALE) {
		updateAllBehaviours(player, FEMALE_FINISHED_MASTURBATING, [NAME], [players[player].label]);
	}
	
	/* update their dialogue */
	if (player != HUMAN_PLAYER) {
		updateBehaviour(player, PLAYER_FINISHED_MASTURBATING, [NAME], [players[player].label]);
	}
	updateAllGameVisuals();
	
	/* update the button */
	$mainButton.html(savedContext);
	
	/* allow progression */
	$mainButton.attr('disabled', false);
	actualMainButtonState = false;
	oneFinished = false;
}