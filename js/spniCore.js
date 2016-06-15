/********************************************************************************
 This file contains the variables and functions that form the core of the game. 
 The player object, game wide constants, the screen objects, and the overarching 
 flow of the game.
 ********************************************************************************/

/**********************************************************************
 *****                    Game Wide Variables                     *****
 **********************************************************************/

/* source constants */
var imageSource = "img/";
var opponentSource = "opponents/";
 
/* player constants */
var HUMAN_PLAYER = 0;
 
/* gender constants */
var MALE = "male";
var FEMALE = "female"; 

/* size constants */
var LARGE_SIZE = "large";
var MEDIUM_SIZE = "medium";
var SMALL_SIZE = "small";

/* game screens */
$titleScreen = $('#title-screen');
$selectScreen = $('#main-select-screen');
$individualSelectScreen = $('#individual-select-screen');
$groupSelectScreen = $('#group-select-screen');
$gameScreen = $('#game-screen');

/* credit modal */
$creditModal = $('#credit-modal');

/* game table */
var tableOpacity = 1;
$gameTable = $('.game-table');

/* screen state */
$previousScreen = null;

/* useful variables */
var BLANK_PLAYER_IMAGE = "opponents/blank.png";

/* player array */
var players = [null, null, null, null, null];
 
/**********************************************************************
 *****                Player Object Specification                 *****
 **********************************************************************/
 
/************************************************************
 * Creates and returns a new player object based on the 
 * supplied information.
 *
 * folder (string), the path to their folder
 * first (string), their first name.
 * last (string), their last name.
 * gender (constant), their gender.
 * clothing (array of Clothing objects), their clothing.
 * out (boolean), is the player still in the game?
 * forfeit (string), state of their forfeit.
 * timer (integer), time until forfeit is finished.
 * current (integer), their current state.
 * state (array of PlayerState objects), their sequential states.
 * xml (jQuery object), the player's loaded XML file.
 ************************************************************/
function createNewPlayer (folder, first, last, label, gender, size, clothing, out, forfeit, timer, current, stage, state, xml) {
    var newPlayerObject = {folder:folder,
                           first:first,
                           last:last,
                           label:label,
						   size:size,
                           gender:gender,
                           clothing:clothing,
                           out:out,
                           forfeit:forfeit,
                           timer:timer,
                           current:current,
						   stage:stage,
                           state:state,
                           xml:xml};
                           
    return newPlayerObject;
}

/**********************************************************************
 *****              Overarching Game Flow Functions               *****
 **********************************************************************/

/************************************************************
 * Loads the initial content of the game.
 ************************************************************/
function initialSetup () {
    /* start by creating the human player object */
    var humanPlayer = createNewPlayer("", "", "", "", MALE, MEDIUM_SIZE, [], false, "", 20, 0, 0, [], null);
    players[HUMAN_PLAYER] = humanPlayer;
    
	/* enable table opacity */
	tableOpacity = 1;
	$gameTable.css({opacity:1});
	
    /* load the all content */
    loadTitleScreen();
	loadSelectScreen();
	
	/* show the title screen */
	$titleScreen.show();
}

/************************************************************
 * Transitions between two screens.
 ************************************************************/
function screenTransition (first, second) {
	first.hide();
	second.show();
}
 
/************************************************************
 * Switches to the next screen based on the screen provided.
 ************************************************************/
function advanceToNextScreen (screen) {
    if (screen == $titleScreen) {
        /* advance to the select screen */
		screenTransition($titleScreen, $selectScreen);

    } else if (screen == $selectScreen) {
        /* advance to the main game screen */
        $selectScreen.hide();
		loadGameScreen();
        $gameScreen.show();
    }
}

/************************************************************
 * Switches to the last screen based on the screen provided.
 ************************************************************/
function returnToPreviousScreen (screen) {
    if (screen == $selectScreen) {
		/* hold previous screen state */
		holdTitleClothing();
		
        /* return to the title screen */
        $selectScreen.hide();
        $titleScreen.show();
    }
}

/************************************************************
 * Clears the game state so that the game can be restarted.
 ************************************************************/
function clearState () {
	/* clear players */
	for (var i = 0; i < players.length; i++) {
		players[i] = null;
	}
}

/************************************************************
 * Restarts the game.
 ************************************************************/
function restartGame () {
    console.log("restarting the game");
	
	/* start by creating the human player object */
    var humanPlayer = createNewPlayer("", "", "", "", players[HUMAN_PLAYER].gender, players[HUMAN_PLAYER].size, players[HUMAN_PLAYER].clothing, false, "", 20, 0, 0, [], null);
	
	/* clean slate */
	clearState();
	
	/* load the previous human player */
	players[HUMAN_PLAYER] = humanPlayer;
    
	/* enable table opacity */
	tableOpacity = 1;
	$gameTable.css({opacity:1});
	
	/* trigger screen refreshes */
	updateSelectionVisuals();
	updateAllGameVisuals();
	
	/* there is only one call to this right now */
	$gameScreen.hide();
	holdTitleClothing();
	$titleScreen.show();
}

/**********************************************************************
 *****                    Interaction Functions                   *****
 **********************************************************************/
 
/************************************************************
 * The player clicked the credits button. Shows the credits modal.
 ************************************************************/
function showCreditModal () {
    $creditModal.modal('show');
}

/************************************************************
 * The player clicked on a table opacity button.
 ************************************************************/
function toggleTableVisibility () {
	if (tableOpacity > 0) {
		$gameTable.fadeOut();
		tableOpacity = 0;
	} else {
		$gameTable.fadeIn();
		tableOpacity = 1;
	}
}

/**********************************************************************
 *****                     Utility Functions                      *****
 **********************************************************************/

/************************************************************
 * Returns a random number in a range.
 ************************************************************/
function getRandomNumber (min, max) {
	return Math.floor(Math.random() * (max - min) + min);
}