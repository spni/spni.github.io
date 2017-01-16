/********************************************************************************
 This file contains the variables and functions that form the options menu.
 ********************************************************************************/

/**********************************************************************
 *****                      Options Variables                     *****
 **********************************************************************/

$optionsModal = $("#options-modal");
$tableStyleOptions = [$("#options-table-style-1"), $("#options-table-style-2"), $("#options-table-style-3")];
$autoFadeOptions = [$("#options-auto-fade-1"), $("#options-auto-fade-2")];
$cardSuggestOptions = [$("#options-card-suggest-1"), $("#options-card-suggest-2")];
$AITurnTimeOptions = [$("#options-ai-turn-time-1"), $("#options-ai-turn-time-2"), $("#options-ai-turn-time-3"), $("#options-ai-turn-time-4"), $("#options-ai-turn-time-5")];
$dealSpeedOptions = [$("#options-deal-speed-1"), $("#options-deal-speed-2"), $("#options-deal-speed-3"), $("#options-deal-speed-4")];
$autoForfeitOptions = [$("#options-auto-forfeit-1"), $("#options-auto-forfeit-2"), $("#options-auto-forfeit-3"), $("#options-auto-forfeit-4")];

$masturbationTimerBox = $("#player-masturbation-timer-box");
$masturbationWarningLabel = $("#masturbation-warning-label");
 
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
        case 3: $tables.removeClass();
				$tables.addClass('bordered game-table game-table-none');
				$surfaces.removeClass();
				$surfaces.addClass('bordered game-table-surface game-table-surface-none');
				$areas.removeClass();
				$areas.addClass('bordered opponent-area opponent-area-none');
				$player.removeClass();
				$player.addClass('bordered player-table-area player-table-area-none');
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
 * The player changed fade option.
 ************************************************************/
function setAutoFade (choice) {
	/* implement the option change */
	switch (choice) {
		case 1: AUTO_FADE = true; break;
		case 2: AUTO_FADE = false; break;
		default: AUTO_FADE = true;
	}
	setActiveOption($autoFadeOptions, choice);
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
		case 1: GAME_DELAY = 0; break;
		case 2: GAME_DELAY = 300; break;
		case 3: GAME_DELAY = 600; break;
		case 4: GAME_DELAY = 800; break;
		case 5: GAME_DELAY = 1200; break;
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
		case 2: ANIM_DELAY = 150;
				ANIM_TIME = 500; 
				break;
		case 3: ANIM_DELAY = 350;
				ANIM_TIME = 1000; 
				break;
		case 4: ANIM_DELAY = 800;
				ANIM_TIME = 2000; 
				break;
		default: ANIM_DELAY = 350;
				 ANIM_TIME = 1000; 
				 break;
	}
	setActiveOption($dealSpeedOptions, choice);
}

function setAutoForfeit (choice) {
	switch (choice) {
		case 4: AUTO_FORFEIT = false;
				break;
		default: AUTO_FORFEIT = true;
				 break;
	}
	setActiveOption($autoForfeitOptions, choice);
  
    switch (choice) {
		case 1: FORFEIT_DELAY = 4000;
				break;
		case 2: FORFEIT_DELAY = 7500;
				break;
		case 3: FORFEIT_DELAY = 10000;
				break;
		default: FORFEIT_DELAY = 7500;
				 break;
	}
}

$("#options-modal").on("hidden.bs.modal", function () {
	if (players[HUMAN_PLAYER].out && AUTO_FORFEIT) {
		setTimeout(advanceGame, FORFEIT_DELAY);
		$mainButton.attr('disabled', true);
	} else {
		$mainButton.attr('disabled', actualMainButtonState);
	}
});


$backgroundSettings = [$("#settings-background-1"), $("#settings-background-2"), $("#settings-background-3"), $("#settings-background-4"), $("#settings-background-5"), $("#settings-background-6"), $("#settings-background-7"), $("#settings-background-8")];


/************************************************************
 * The player clicked the options button. Shows the options modal.
 ************************************************************/
function showGameSettingsModal () {
	loadMasturbationTimer(); //set data values
    $gameSettingsModal.modal('show');
}


/************************************************************
 * The player changed the background.
 ************************************************************/
function setBackground (choice) {
	/* implement the option change */
	switch (choice) {
		case 1: $("body").css("background-image", "url(img/background1.png)"); break;
		case 2: $("body").css("background-image", "url(img/background2.png)"); break;
        case 3: $("body").css("background-image", "url(img/background3.png)"); break;
        case 4: $("body").css("background-image", "url(img/background4.png)"); break;
        case 5: $("body").css("background-image", "url(img/background5.png)"); break;
        case 6: $("body").css("background-image", "url(img/background6.png)"); break;
        case 7: $("body").css("background-image", "url(img/background7.png)"); break;
        case 8: $("body").css("background-image", "url(img/background8.png)"); break;
		default: $("body").css("background-image", "url(img/background1.png)");
	}
	setActiveOption($backgroundSettings, choice);
}

/************************************************************
 * Loading the player masturbation timer.
 ************************************************************/
function loadMasturbationTimer () {
	$masturbationTimerBox.val(players[HUMAN_PLAYER].timer);
	$masturbationWarningLabel.css("visibility", "hidden");
}
 /************************************************************
 * The player changed their masturbation timer.
 ************************************************************/

function changeMasturbationTimer () {
	var newTimerValue = $masturbationTimerBox.val();
	var newTime = Number(newTimerValue);
	var isValidTimerValue = (newTime != "NaN") && (newTime > 0);
	if (isValidTimerValue){
		players[HUMAN_PLAYER].timer = newTime;
	}
	$masturbationWarningLabel.css("visibility", isValidTimerValue ? "hidden" : "visible");
}