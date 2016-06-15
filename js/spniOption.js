/********************************************************************************
 This file contains the variables and functions that form the options menu.
 ********************************************************************************/

/**********************************************************************
 *****                      Options Variables                     *****
 **********************************************************************/

$optionsModal = $("#options-modal");
$tableStyleOptions = [$("#options-table-style-1"), $("#options-table-style-2")];
$cardSuggestOptions = [$("#options-card-suggest-1"), $("#options-card-suggest-2")];
$AITurnTimeOptions = [$("#options-ai-turn-time-1"), $("#options-ai-turn-time-2"), $("#options-ai-turn-time-3"), $("#options-ai-turn-time-4"), $("#options-ai-turn-time-5")];
$dealSpeedOptions = [$("#options-deal-speed-1"), $("#options-deal-speed-2"), $("#options-deal-speed-3"), $("#options-deal-speed-4")];

 
/**********************************************************************
 *****                      Option Functions                      *****
 **********************************************************************/
 
/************************************************************
 * The player clicked the options button. Shows the options modal.
 ************************************************************/
function showOptionsModal () {
    $optionsModal.modal('show');
}

/************************************************************
 * Displays the active option correctly.
 ************************************************************/
function setActiveOption (options, choice) {
	/* make all inactive */
	for (var i = 0; i < options.length; i++) {
		options[i].removeClass("active");
	}
	
	/* set the right active option */
	options[choice-1].addClass("active");
}

/************************************************************
 * The player changed the table style.
 ************************************************************/
function setTableStyle (choice) {
	/* get the tables */
	$tables = $('.game-table');
	$surfaces = $('.game-table-surface');
	$areas = $('.opponent-area');
	$player = $('.player-table-area');
	
	/* implement the option change */
	switch (choice) {
		case 1: $tables.removeClass();
				$tables.addClass('bordered game-table');
				$surfaces.removeClass();
				$surfaces.addClass('bordered game-table-surface');
				$areas.removeClass();
				$areas.addClass('bordered opponent-area');
				$player.removeClass();
				$player.addClass('bordered player-table-area');
				break;
		case 2: $tables.removeClass();
				$tables.addClass('bordered game-table game-table-glass');
				$surfaces.removeClass();
				$surfaces.addClass('bordered game-table-surface game-table-surface-glass');
				$areas.removeClass();
				$areas.addClass('bordered opponent-area opponent-area-glass');
				$player.removeClass();
				$player.addClass('bordered player-table-area player-table-area-glass');
				break;
		default: $tables.removeClass();
				 $tables.addClass('bordered game-table');
				 $surfaces.removeClass();
				 $surfaces.addClass('bordered game-table-surface');
				 $areas.removeClass();
				 $areas.addClass('bordered opponent-area');
	}
	setActiveOption($tableStyleOptions, choice);
}

/************************************************************
 * The player changed card suggestion.
 ************************************************************/
function setCardSuggest (choice) {
	/* implement the option change */
	switch (choice) {
		case 1: CARD_SUGGEST = true; break;
		case 2: CARD_SUGGEST = false; break;
		default: CARD_SUGGEST = false;
	}
	setActiveOption($cardSuggestOptions, choice);
}

/************************************************************
 * The player changed the AI turn time.
 ************************************************************/
function setAITurnTime (choice) {
	/* implement the option change */
	switch (choice) {
		case 1: GAME_DELAY = 200; break;
		case 2: GAME_DELAY = 400; break;
		case 3: GAME_DELAY = 700; break;
		case 4: GAME_DELAY = 1000; break;
		case 5: GAME_DELAY = 1500; break;
		default: GAME_DELAY = 600;
	}
	setActiveOption($AITurnTimeOptions, choice);
}

/************************************************************
 * The player changed the card animation speed.
 ************************************************************/
function setDealSpeed (choice) {
	/* implement the option change */
	switch (choice) {
		case 1: ANIM_DELAY = 0;
				ANIM_TIME = 0; 
				break;
		case 2: ANIM_DELAY = 200;
				ANIM_TIME = 500; 
				break;
		case 3: ANIM_DELAY = 500;
				ANIM_TIME = 1000; 
				break;
		case 4: ANIM_DELAY = 800;
				ANIM_TIME = 2000; 
				break;
		default: ANIM_DELAY = 500;
				 ANIM_TIME = 1000; 
				 break;
	}
	setActiveOption($dealSpeedOptions, choice);
}