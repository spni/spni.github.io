/********************************************************************************
 This file contains the variables and functions that from the behaviours of the
 AI opponents. All the parsing of their files, as well as the structures to store
 that information are stored in this file.
 ********************************************************************************/

/**********************************************************************
 *****                  State Object Specification                *****
 **********************************************************************/
 
/************************************************************
 * Stores information on AI state.
 ************************************************************/
function createNewState (dialogue, image, direction) {
	var newStateObject = {dialogue:dialogue,
                          image:image,
                          direction:direction};
						  
	return newStateObject;
}

/**********************************************************************
 *****                      All Dialogue Tags                     *****
 **********************************************************************/
 
var NAME = "~name~";
var PROPER_CLOTHING = "~Clothing~";
var LOWERCASE_CLOTHING = "~clothing~";
var CARDS = "~cards~";

/**********************************************************************
 *****                    All Dialogue Triggers                   *****
 **********************************************************************/

var SWAP_CARDS = "swap_cards";
var BAD_HAND = "bad_hand";
var OKAY_HAND = "okay_hand";
var GOOD_HAND = "good_hand";
 
var PLAYER_MUST_STRIP_WINNING = "must_strip_winning";
var PLAYER_MUST_STRIP_NORMAL = "must_strip_normal";
var PLAYER_MUST_STRIP_LOSING = "must_strip_losing";
var PLAYER_STRIPPING = "stripping";
var PLAYER_STRIPPED = "stripped";

var PLAYER_MUST_MASTURBATE = "must_masturbate";
var PLAYER_MUST_MASTURBATE_FIRST = "must_masturbate_first";
var PLAYER_START_MASTURBATING = "start_masturbating";
var PLAYER_MASTURBATING = "masturbating";
var PLAYER_HEAVY_MASTURBATING = "heavy_masturbating";
var PLAYER_FINISHING_MASTURBATING = "finishing_masturbating";
var PLAYER_FINISHED_MASTURBATING = "finished_masturbating";

var MALE_HUMAN_MUST_STRIP = "male_human_must_strip";
var MALE_MUST_STRIP = "male_must_strip";

var MALE_REMOVING_ACCESSORY = "male_removing_accessory";
var MALE_REMOVING_MINOR = "male_removing_minor";
var MALE_REMOVING_MAJOR = "male_removing_major";
var MALE_CHEST_WILL_BE_VISIBLE = "male_chest_will_be_visible";
var MALE_CROTCH_WILL_BE_VISIBLE = "male_crotch_will_be_visible";

var MALE_REMOVED_ACCESSORY = "male_removed_accessory";
var MALE_REMOVED_MINOR = "male_removed_minor";
var MALE_REMOVED_MAJOR = "male_removed_major";
var MALE_CHEST_IS_VISIBLE = "male_chest_is_visible";
var MALE_SMALL_CROTCH_IS_VISIBLE = "male_small_crotch_is_visible";
var MALE_MEDIUM_CROTCH_IS_VISIBLE = "male_medium_crotch_is_visible";
var MALE_LARGE_CROTCH_IS_VISIBLE = "male_large_crotch_is_visible";

var MALE_MUST_MASTURBATE = "male_must_masturbate";
var MALE_START_MASTURBATING = "male_start_masturbating";
var MALE_MASTURBATING = "male_masturbating";
var MALE_HEAVY_MASTURBATING = "male_heavy_masturbating";
var MALE_FINISHED_MASTURBATING = "male_finished_masturbating";

var FEMALE_HUMAN_MUST_STRIP = "female_human_must_strip";
var FEMALE_MUST_STRIP = "female_must_strip";

var FEMALE_REMOVING_ACCESSORY = "female_removing_accessory";
var FEMALE_REMOVING_MINOR = "female_removing_minor";
var FEMALE_REMOVING_MAJOR = "female_removing_major";
var FEMALE_CHEST_WILL_BE_VISIBLE = "female_chest_will_be_visible";
var FEMALE_CROTCH_WILL_BE_VISIBLE = "female_crotch_will_be_visible";

var FEMALE_REMOVED_ACCESSORY = "female_removed_accessory";
var FEMALE_REMOVED_MINOR = "female_removed_minor";
var FEMALE_REMOVED_MAJOR = "female_removed_major";
var FEMALE_SMALL_CHEST_IS_VISIBLE = "female_small_chest_is_visible";
var FEMALE_MEDIUM_CHEST_IS_VISIBLE = "female_medium_chest_is_visible";
var FEMALE_LARGE_CHEST_IS_VISIBLE = "female_large_chest_is_visible";
var FEMALE_CROTCH_IS_VISIBLE = "female_crotch_is_visible";

var FEMALE_MUST_MASTURBATE = "female_must_masturbate";
var FEMALE_START_MASTURBATING = "female_start_masturbating";
var FEMALE_MASTURBATING = "female_masturbating";
var FEMALE_HEAVY_MASTURBATING = "female_heavy_masturbating";
var FEMALE_FINISHED_MASTURBATING = "female_finished_masturbating";

var GAME_OVER_VICTORY = "game_over_victory";
var GAME_OVER_DEFEAT = "game_over_defeat";
 
/**********************************************************************
 *****                 Behaviour Parsing Functions                *****
 **********************************************************************/

/************************************************************
 * Loads and parses the start of the behaviour XML file of the 
 * given opponent source folder.
 *
 * The callFunction parameter must be a function capable of 
 * receiving a new player object and a slot number.
 ************************************************************/
function loadBehaviour (folder, callFunction, slot) {
	$.ajax({
        type: "GET",
		url: folder + "behaviour.xml",
		dataType: "text",
		success: function(xml) {
            var first = $(xml).find('first').text();
            var last = $(xml).find('last').text();
            var label = $(xml).find('label').text();
            var gender = $(xml).find('gender').text().trim().toLowerCase(); //convert everything to lowercase, for comparison to the strings "male" and "female"
            var size = $(xml).find('size').text();
            var timer = $(xml).find('timer').text();
            
            var newPlayer = createNewPlayer(folder, first, last, label, gender, size, [], false, "", Number(timer), 0, 0, [], xml);
            
            loadOpponentWardrobe(newPlayer);
            
            newPlayer.current = 0;
			newPlayer.state = parseDialogue($(xml).find('start'), [], []);
			
			callFunction(newPlayer, slot);
		}
	});
}

/************************************************************
 * Parses and loads the wardrobe section of an opponent's XML 
 * file.
 ************************************************************/
function loadOpponentWardrobe (player) {
	/* grab the relevant XML file, assuming its already been loaded */
	var xml = player.xml;
	
	/* find and grab the wardrobe tag */
	$wardrobe = $(xml).find('wardrobe');
	
	/* find and create all of their clothing */
	$wardrobe.find('clothing').each(function () {
		var properName = $(this).attr('proper-name');
		var lowercase = $(this).attr('lowercase');
		var type = $(this).attr('type');
		var position = $(this).attr('position');
		
		var newClothing = createNewClothing(properName, lowercase, type, position, null, 0, 0);
		
		player.clothing.push(newClothing);
	});
}

/************************************************************
 * Parses the dialogue states of a player, given the case object.
 ************************************************************/
function parseDialogue (caseObject, replace, content) {
    var states = [];
	
	caseObject.find('state').each(function () {
        var image = $(this).attr('img');
        var dialogue = $(this).html();
        var direction = $(this).attr('direction');
        
		if (replace && content) {
			for (var i = 0; i < replace.length; i++) {
				dialogue = dialogue.replace(replace[i], content[i]);
			}
		}
        
        states.push(createNewState(dialogue, image, direction));
	});
	
	return states;
}

/************************************************************
 * Updates the behaviour of the given player based on the 
 * provided tag.
 ************************************************************/
function updateBehaviour (player, tag, replace, content) {
	/* determine if the AI is dialogue locked */
	//Allow characters to speak. If we change forfeit ideas, we'll likely need to change this as well.
	//if (players[player].forfeit[1] == CANNOT_SPEAK) {
		/* their is restricted to this only */
		//tag = players[player].forfeit[0];
	//}
    
    if (!players[player]) {
        return;
    }
	
    /* get the AI stage */
    var stageNum = players[player].stage;
	
    /* try to find the stage */
    var stage = null;
    $(players[player].xml).find('behaviour').find('stage').each(function () {
       if (Number($(this).attr('id')) == stageNum) {
           stage = $(this);
       } 
    });
    
    /* quick check to see if the stage exists */
    if (!stage) {
        console.log("Error: couldn't find stage for player "+player+" on stage number "+stageNum+" for tag "+tag);
        return;
    }
    
    /* try to find the tag */
	var found = false;
	$(stage).find('case').each(function () {
		if ($(this).attr('tag') == tag) {
            players[player].current = 0;
			players[player].state = parseDialogue($(this), replace, content);
			found = true;
		}
	});
	
    /* quick check to see if the tag exists */
	if (!found) {
		players[player].state = null;
		console.log("Error: couldn't find "+tag+" dialogue for player "+player+" at stage "+stageNum);
	}
}

/************************************************************
 * Updates the behaviour of all players except the given player 
 * based on the provided tag.
 ************************************************************/
function updateAllBehaviours (player, tag, replace, content) {
	for (i = 1; i < players.length; i++) {
		if (players[i] && i != player) {
			updateBehaviour(i, tag, replace, content);
		}
	}
}