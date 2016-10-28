/********************************************************************************
 This file contains the variables and functions that form the select screens of 
 the game. The parsing functions for the opponent.xml file.
 ********************************************************************************/

/**********************************************************************
 *****               Opponent & Group Specification               *****
 **********************************************************************/
 
/**************************************************
 * Stores meta information about opponents.
 **************************************************/
function createNewOpponent (folder, enabled, first, last, label, image, gender, height, source, artist, writer, description) {
	var newOpponentObject = {folder:folder,
							 enabled:enabled,
                             first:first,
							 last:last,
							 label:label,
							 image:image,
                             gender:gender,
							 height:height,
							 source:source,
                             artist:artist,
                             writer:writer,
							 description:description};
						  
	return newOpponentObject;
}

/**************************************************
 * Stores meta information about groups.
 **************************************************/
function createNewGroup (title, opponents) {
	var newGroupObject = {title:title,
						  opponents:opponents};
						  
	return newGroupObject;
}
 
/**********************************************************************
 *****                  Select Screen UI Elements                 *****
 **********************************************************************/
 
/* main select screen */
$selectTable = $("#select-table");
$selectBubbles = [$("#select-bubble-1"),
                  $("#select-bubble-2"),
                  $("#select-bubble-3"),
                  $("#select-bubble-4")];
$selectDialogues = [$("#select-dialogue-1"),
                    $("#select-dialogue-2"),
                    $("#select-dialogue-3"),
                    $("#select-dialogue-4")];
$selectAdvanceButtons = [$("#select-advance-button-1"),
                         $("#select-advance-button-2"),
                         $("#select-advance-button-3"),
                         $("#select-advance-button-4")];
$selectImages = [$("#select-image-1"),
                 $("#select-image-2"),
                 $("#select-image-3"),
                 $("#select-image-4")];
$selectLabels = [$("#select-name-label-1"),
                 $("#select-name-label-2"),
                 $("#select-name-label-3"),
                 $("#select-name-label-4")];
$selectButtons = [$("#select-slot-button-1"),
                  $("#select-slot-button-2"),
                  $("#select-slot-button-3"),
                  $("#select-slot-button-4")];
$selectMainButton = $("#main-select-button");
 
/* individual select screen */
$individualSelectTable = $("#individual-select-table");
$individualNameLabels = [$("#individual-name-label-1"), $("#individual-name-label-2"), $("#individual-name-label-3"), $("#individual-name-label-4")];
$individualPrefersLabels = [$("#individual-prefers-label-1"), $("#individual-prefers-label-2"), $("#individual-prefers-label-3"), $("#individual-prefers-label-4")];
$individualSexLabels = [$("#individual-sex-label-1"), $("#individual-sex-label-2"), $("#individual-sex-label-3"), $("#individual-sex-label-4")];
$individualHeightLabels = [$("#individual-height-label-1"), $("#individual-height-label-2"), $("#individual-height-label-3"), $("#individual-height-label-4")];
$individualSourceLabels = [$("#individual-source-label-1"), $("#individual-source-label-2"), $("#individual-source-label-3"), $("#individual-source-label-4")];
$individualWriterLabels = [$("#individual-writer-label-1"), $("#individual-writer-label-2"), $("#individual-writer-label-3"), $("#individual-writer-label-4")];
$individualArtistLabels = [$("#individual-artist-label-1"), $("#individual-artist-label-2"), $("#individual-artist-label-3"), $("#individual-artist-label-4")];
$individualDescriptionLabels = [$("#individual-description-label-1"), $("#individual-description-label-2"), $("#individual-description-label-3"), $("#individual-description-label-4")];

$individualImages = [$("#individual-image-1"), $("#individual-image-2"), $("#individual-image-3"), $("#individual-image-4")];
$individualButtons = [$("#individual-button-1"), $("#individual-button-2"), $("#individual-button-3"), $("#individual-button-4")];

$individualPageIndicator = $("#individual-page-indicator");
$individualMaxPageIndicator = $("#individual-max-page-indicator");

/* group select screen */
$groupSelectTable = $("#group-select-table");
$groupNameLabels = [$("#group-name-label-1"), $("#group-name-label-2"), $("#group-name-label-3"), $("#group-name-label-4")];
$groupPrefersLabels = [$("#group-prefers-label-1"), $("#group-prefers-label-2"), $("#group-prefers-label-3"), $("#group-prefers-label-4")];
$groupSexLabels = [$("#group-sex-label-1"), $("#group-sex-label-2"), $("#group-sex-label-3"), $("#group-sex-label-4")];
$groupHeightLabels = [$("#group-height-label-1"), $("#group-height-label-2"), $("#group-height-label-3"), $("#group-height-label-4")];
$groupSourceLabels = [$("#group-source-label-1"), $("#group-source-label-2"), $("#group-source-label-3"), $("#group-source-label-4")];
$groupWriterLabels = [$("#group-writer-label-1"), $("#group-writer-label-2"), $("#group-writer-label-3"), $("#group-writer-label-4")];
$groupArtistLabels = [$("#group-artist-label-1"), $("#group-artist-label-2"), $("#group-artist-label-3"), $("#group-artist-label-4")];
$groupDescriptionLabels = [$("#group-description-label-1"), $("#group-description-label-2"), $("#group-description-label-3"), $("#group-description-label-4")];

$groupImages = [$("#group-image-1"), $("#group-image-2"), $("#group-image-3"), $("#group-image-4")];
$groupNameLabel = $("#group-name-label");
$groupButton = $("#group-button");

$groupPageIndicator = $("#group-page-indicator");
$groupMaxPageIndicator = $("#group-max-page-indicator");

/**********************************************************************
 *****                  Select Screen Variables                   *****
 **********************************************************************/

/* hidden variables */
var mainSelectHidden = false;
var singleSelectHidden = false;
var groupSelectHidden = false;

/* opponent listing file */
var listingFile = "opponents/listing.xml";
var metaFile = "meta.xml";

/* opponent information storage */
var loadedOpponents = [];
var selectableOpponents = [];
var hiddenOpponents = [];
var loadedGroups = [];

/* page variables */
var individualPage = 0;
var groupPage = 0;

/* consistence variables */
var selectedSlot = 0;
var individualSlot = 0;
var shownIndividuals = [null, null, null, null];
var shownGroup = [null, null, null, null];
var randomLock = false;
 
/**********************************************************************
 *****                    Start Up Functions                      *****
 **********************************************************************/
 
/************************************************************
 * Loads all of the content required to display the title 
 * screen.
 ************************************************************/
function loadSelectScreen () {
    loadListingFile();
    
	updateSelectionVisuals();
}

/************************************************************
 * Loads and parses the main opponent listing file.
 ************************************************************/
function loadListingFile () {
	/* clear the previous meta information */
	loadedOpponents = [];
	loadedGroups = [];
	
	/* grab and parse the opponent listing file */
	$.ajax({
        type: "GET",
		url: listingFile,
		dataType: "text",
		success: function(xml) {
			/* start by parsing and loading the individual listings */
			$individualListings = $(xml).find('individuals');
			$individualListings.find('opponent').each(function () {
				var folder = $(this).text();
				console.log("Reading \""+folder+"\" from listing file");
				loadOpponentMeta(OPP + folder);
			});
			
			/* end by parsing and loading the group listings */
			$groupListings = $(xml).find('groups');
			$groupListings.find('group').each(function () {
				var title = $(this).attr('title');
				var opp1 = OPP + $(this).attr('opp1');
				var opp2 = OPP + $(this).attr('opp2');
				var opp3 = OPP + $(this).attr('opp3');
				var opp4 = OPP + $(this).attr('opp4');
				
				var newGroup = createNewGroup(title, [opp1, opp2, opp3, opp4]);
				loadGroupMeta(newGroup);
			});
		}
	});
}

/************************************************************
 * Loads and parses the meta XML file of an opponent.
 ************************************************************/
function loadOpponentMeta (folder) {
	/* grab and parse the opponent meta file */
	$.ajax({
        type: "GET",
		url: folder + metaFile,
		dataType: "text",
		success: function(xml) {			
			/* grab all the info for this listing */
			var enabled = $(xml).find('enabled').text();
			var first = $(xml).find('first').text();
			var last = $(xml).find('last').text();
			var label = $(xml).find('label').text();
			var pic = $(xml).find('pic').text();
			var gender = $(xml).find('gender').text();
			var height = $(xml).find('height').text();
			var from = $(xml).find('from').text();
			var artist = $(xml).find('artist').text();
			var writer = $(xml).find('writer').text();
			var description = $(xml).find('description').text();

			var opponent = createNewOpponent(folder, enabled, first, last, label, pic, gender, height, from, artist, writer, description);
			
			/* add the opponent to the list */
			loadedOpponents.push(opponent);
			selectableOpponents.push(opponent);
	
			/* load the individual select screen */
			individualPage = 0;
			updateIndividualSelectScreen();
		}
	});
}
 
/************************************************************
 * Loads opponents onto the individual select screen based
 * on the currently selected page.
 ************************************************************/
function updateIndividualSelectScreen () {
	/* safety wrap around */
	if (individualPage < 0) {
		/* wrap to last page */
		individualPage = Math.ceil(selectableOpponents.length/4)-1;
	}
	$individualPageIndicator.val(individualPage+1);
	
	/* keep track of how many opponents were on this screen */
	var empty = 0;
	
    /* create and load all of the individual opponents */
	for (var i = individualPage*4; i < (individualPage+1)*4; i++) {
		var index = i - individualPage*4;

		if (i < selectableOpponents.length) {
			shownIndividuals[index] = selectableOpponents[i];
			
			$individualNameLabels[index].html(selectableOpponents[i].first + " " + selectableOpponents[i].last);
			$individualPrefersLabels[index].html(selectableOpponents[i].label);
			$individualSexLabels[index].html(selectableOpponents[i].gender);
			$individualSourceLabels[index].html(selectableOpponents[i].source);
			$individualWriterLabels[index].html(selectableOpponents[i].writer);
			$individualArtistLabels[index].html(selectableOpponents[i].artist);
			$individualDescriptionLabels[index].html(selectableOpponents[i].description);
			
			$individualImages[index].attr('src', selectableOpponents[i].folder + selectableOpponents[i].image);
			if (selectableOpponents[i].enabled == "true") {
				$individualButtons[index].html('Select Opponent');
				$individualButtons[index].attr('disabled', false);
			} else {
				$individualButtons[index].html('Coming Soon');
				$individualButtons[index].attr('disabled', true);
			}
		} else {
			shownIndividuals[index] = null;
			
			$individualNameLabels[index].html("");
			$individualPrefersLabels[index].html("");
			$individualSexLabels[index].html("");
			$individualSourceLabels[index].html("");
			$individualWriterLabels[index].html("");
			$individualArtistLabels[index].html("");
			$individualDescriptionLabels[index].html("");
			
			$individualImages[index].attr('src', BLANK_PLAYER_IMAGE);
			$individualButtons[index].attr('disabled', true);
			
			empty++;
		}
    }
	
	/* reload if the page is empty */
	if (empty == 4 && individualPage != 0) {
		individualPage = 0;
		updateIndividualSelectScreen();
	}
}

/************************************************************
 * Loads the meta information for an entire group.
 ************************************************************/
function loadGroupMeta (group) {
	/* parse the individual information of each group member */
	var groupID = loadedGroups.length;
	loadedGroups.push(group);
	
	for (var i = 0; i < 4; i++) {
		loadGroupMemberMeta (group.opponents[i], groupID, i);
	}
}

/************************************************************
 * Loads the meta information for a single group member.
 ************************************************************/
function loadGroupMemberMeta (folder, groupID, member) {
	/* grab and parse the opponent meta file */
	$.ajax({
		type: "GET",
		url: folder + metaFile,
		dataType: "text",
		success: function(xml) {
			/* grab all the info for this listing */
			var enabled = $(xml).find('enabled').text();
			var first = $(xml).find('first').text();
			var last = $(xml).find('last').text();
			var label = $(xml).find('label').text();
			var pic = $(xml).find('pic').text();
			var gender = $(xml).find('gender').text();
			var height = $(xml).find('height').text();
			var from = $(xml).find('from').text();
			var artist = $(xml).find('artist').text();
			var writer = $(xml).find('writer').text();
			var description = $(xml).find('description').text();

			var opponent = createNewOpponent(folder, enabled, first, last, label, pic, gender, height, from, artist, writer, description);
			
			/* add the opponent information to the group */
			loadedGroups[groupID].opponents[member] = opponent;
	
			/* load the individual select screen */
			groupPage = 0;
			updateGroupSelectScreen();
		}
	});
}

/************************************************************
 * Loads opponents onto the group select screen based on the
 * currently selected page.
 ************************************************************/
function updateGroupSelectScreen () {
	/* safety wrap around */
	if (groupPage < 0) {
		/* wrap to last page */
		groupPage = (loadedGroups.length)-1;
	} else if (groupPage > loadedGroups.length-1) {
		/* wrap to the first page */
		groupPage = 0;
	}
	$groupPageIndicator.val(groupPage+1);
	
    /* create and load all of the individual opponents */
	for (var i = 0; i < 4; i++) {
		var opponent = loadedGroups[groupPage].opponents[i];

		if (opponent) {
			shownGroup[i] = opponent;
			
			$groupNameLabels[i].html(opponent.first + " " + opponent.last);
			$groupPrefersLabels[i].html(opponent.label);
			$groupSexLabels[i].html(opponent.gender);
			$groupSourceLabels[i].html(opponent.source);
			$groupWriterLabels[i].html(opponent.writer);
			$groupArtistLabels[i].html(opponent.artist);
			$groupDescriptionLabels[i].html(opponent.description);
			
			$groupImages[i].attr('src', opponent.folder + opponent.image);
			$groupNameLabel.html(loadedGroups[groupPage].title);
			if (opponent.enabled == "true") {
				$groupButton.html('Select Group');
				$groupButton.attr('disabled', false);
			} else {
				$groupButton.html('Coming Soon');
				$groupButton.attr('disabled', true);
			}
		} else {
			shownIndividuals[i] = null;
			
			$groupNameLabels[i].html("");
			$groupPrefersLabels[i].html("");
			$groupSexLabels[i].html("");
			$groupSourceLabels[i].html("");
			$groupWriterLabels[i].html("");
			$groupArtistLabels[i].html("");
			$groupDescriptionLabels[i].html("");
			
			$groupImages[i].attr('src', BLANK_PLAYER_IMAGE);
		}
    }
}

/**********************************************************************
 *****                   Interaction Functions                    *****
 **********************************************************************/

/************************************************************
 * The player clicked the advance dialogue button on the main
 * select screen.
 ************************************************************/
function advanceSelectDialogue (slot) {
    players[slot].current++;
    
    /* update dialogue */
    $selectDialogues[slot-1].html(players[slot].state[players[slot].current].dialogue);
    
    /* determine if the advance dialogue button should be shown */
    if (players[slot].state.length > players[slot].current+1) {
        $selectAdvanceButtons[slot-1].css({opacity : 1});
    } else {
        $selectAdvanceButtons[slot-1].css({opacity : 0});
    }
    
    /* direct the dialogue bubble */
    if (players[slot].state[players[slot].current].direction) {
        $selectBubbles[slot-1].removeClass();
        
		$selectBubbles[slot-1].addClass("dialogue-bubble dialogue-"+players[slot].state[players[slot].current].direction);
	} else {
		$selectBubbles[slot-1].removeClass();
		$selectBubbles[slot-1].addClass("dialogue-bubble dialogue-centre");
	}
    
    /* update image */
    $selectImages[slot-1].attr('src', players[slot].folder + players[slot].state[players[slot].current].image);
}
 
/************************************************************
 * The player clicked on an opponent slot.
 ************************************************************/
function selectOpponentSlot (slot) {
    if (!players[slot]) {
        /* add a new opponent */
        selectedSlot = slot;
        
		/* shallow copy the selectable list */
		selectableOpponents = [];
		for (var i = 0; i < loadedOpponents.length; i++) {
			selectableOpponents[i] = loadedOpponents[i];
		}
		
		/* update max page indicator */
		$individualMaxPageIndicator.html("of "+Math.ceil(selectableOpponents.length/4));
		
        /* hide selected opponents */
        for (var i = 1; i < players.length; i++) {
            if (players[i]) {
                /* find this opponent's placement in the selectable opponents */
                for (var j = 0; j < selectableOpponents.length; j++) {
                    if (selectableOpponents[j].folder == players[i].folder) {
                        /* this is a selected player */
						selectableOpponents.splice(j, 1);
                    }
                }
            }
        }
		
		/* reload selection screen */
		updateIndividualSelectScreen();
        
        /* switch screens */
		screenTransition($selectScreen, $individualSelectScreen);
    } else {
        /* remove the opponent that's there */
        players[slot] = null;
        updateSelectionVisuals();
    }
}

/************************************************************
 * The player clicked on the select group slot.
 ************************************************************/
function clickedSelectGroupButton () {
	selectedSlot = 1;
    
    $groupMaxPageIndicator.html("of "+loadedGroups.length);
	
	/* switch screens */
	screenTransition($selectScreen, $groupSelectScreen);
}

/************************************************************
 * The player clicked on the select random group slot.
 ************************************************************/
function clickedRandomGroupButton () {
	selectedSlot = 1;
	
    for (var i = 1; i < players.length; i++) {
        players[i] = null;
    }
    
	/* get a random number for the group listings */
	var randomGroupNumber = getRandomNumber(0, loadedGroups.length);
    console.log(loadedGroups[randomGroupNumber].opponents[0]);
    
	/* load the corresponding group */
	loadBehaviour(loadedGroups[randomGroupNumber].opponents[0].folder, updateRandomSelection);
	loadBehaviour(loadedGroups[randomGroupNumber].opponents[1].folder, updateRandomSelection);
	loadBehaviour(loadedGroups[randomGroupNumber].opponents[2].folder, updateRandomSelection);
	loadBehaviour(loadedGroups[randomGroupNumber].opponents[3].folder, updateRandomSelection);
}

/************************************************************
 * The player clicked on the all random button.
 ************************************************************/
function clickedRandomFillButton (predicate) {
	/* compose a copy of the loaded opponents list */
	var loadedOpponentsCopy = [];
	
    for (var i = 1; i < players.length; i++) {
        players[i] = null;
    }
    
	/* only add non-selected opponents from the list */
	for (var i = 0; i < loadedOpponents.length; i++) {
		/* check to see if this opponent is selected */
		var position = -1;
		for (var j = 1; j < players.length; j++) {
			if (players[j] && loadedOpponents[i].folder == players[j].folder) {
				/* this opponent is loaded */
				position = j;
			}
		}
		if (position == -1) {
			if(predicate) {
				if(predicate(loadedOpponents[i])) {
					loadedOpponentsCopy.push(loadedOpponents[i]);
				}
			} else {
				loadedOpponentsCopy.push(loadedOpponents[i]);
			}
		}
	}
	
	/* select random opponents */
	for (var i = 1; i < players.length; i++) {
		/* if slot is empty */
		if (!players[i]) {
			/* select random opponent */
			var randomOpponent = getRandomNumber(0, loadedOpponentsCopy.length);
	
			/* load opponent */
			loadBehaviour(loadedOpponentsCopy[randomOpponent].folder, updateRandomSelection);
			
			/* remove random opponent from copy list */
			loadedOpponentsCopy.splice(randomOpponent, 1);
		}
	}
}

/************************************************************
 * The player clicked on a change stats card button on the 
 * individual select screen.
 ************************************************************/
function changeIndividualStats (target) {
    for (var i = 1; i < 5; i++) {
        for (var j = 1; j < 4; j++) {
            if (j != target) {
                $('#individual-stats-page-'+i+'-'+j).hide();
            }
            else {
                $('#individual-stats-page-'+i+'-'+j).show();
            }
        }
    }
}

/************************************************************
 * The player clicked the select opponent button on the
 * individual select screen.
 ************************************************************/
function selectIndividualOpponent (slot) {
    /* move the stored player into the selected slot and update visuals */
	individualSlot = slot;
	loadBehaviour(shownIndividuals[slot-1].folder, individualScreenCallback, 0);
}

/************************************************************
 * This is the callback for the individual select screen.
 ************************************************************/
function individualScreenCallback (playerObject, slot) {
    players[selectedSlot] = playerObject;
    players[selectedSlot].current = 0;
	
	/* switch screens */
	screenTransition($individualSelectScreen, $selectScreen);
	updateSelectionVisuals();
}

/************************************************************
 * The player is changing the page on the individual screen.
 ************************************************************/
function changeIndividualPage (skip, page) {
	console.log("resigtered");
	if (skip) {
		if (page == -1) {
			/* go to first page */
			individualPage = 0;
		} else if (page == 1) {
			/* go to last page */
			individualPage = Math.ceil(selectableOpponents.length/4)-1;
		} else {
			/* go to selected page */
			individualPage = Number($individualPageIndicator.val()) - 1;
		}
	} else {
		individualPage += page;
	}
	updateIndividualSelectScreen();
}

/************************************************************
 * The player clicked on a change stats card button on the 
 * group select screen.
 ************************************************************/
function changeGroupStats (target) {
    for (var i = 1; i < 5; i++) {
        for (var j = 1; j < 4; j++) {
            if (j != target) {
                $('#group-stats-page-'+i+'-'+j).hide();
            }
            else {
                $('#group-stats-page-'+i+'-'+j).show();
            }
        }
    }
}

/************************************************************
 * The player clicked the select opponent button on the
 * group select screen.
 ************************************************************/
function selectGroup () {
    /* clear the selection screen */
	for (var i = 1; i < 5; i++) {
		players[i] = null;
	}
	updateSelectionVisuals();
	
	/* load the group members */
	for (var i = 0; i < 4; i++) {
		loadBehaviour(loadedGroups[groupPage].opponents[i].folder, groupScreenCallback, i+1);
	}
}

/************************************************************
 * This is the callback for the group select screen.
 ************************************************************/
function groupScreenCallback (playerObject, slot) {
	console.log(slot +" "+playerObject);
    players[slot] = playerObject;
    players[slot].current = 0;
	
	updateSelectionVisuals();
    
    /* switch screens */
	screenTransition($groupSelectScreen, $selectScreen);
}

/************************************************************
 * The player is changing the page on the group screen.
 ************************************************************/
function changeGroupPage (skip, page) {
	if (skip) {
		if (page == -1) {
			/* go to first page */
			groupPage = 0;
		} else if (page == 1) {
			/* go to last page */
			groupPage = loadedGroups.length-1;
		} else {
			/* go to selected page */
			groupPage = Number($groupPageIndicator.val()) - 1;
		}
	} else {
		groupPage += page;
	}
	updateGroupSelectScreen();
}

/************************************************************
 * The player clicked on the back button on the individual or
 * group select screen.
 ************************************************************/
function backToSelect () {
    /* switch screens */
	screenTransition($individualSelectScreen, $selectScreen);
	screenTransition($groupSelectScreen, $selectScreen);
}

/************************************************************
 * The player clicked on the start game button on the main 
 * select screen.
 ************************************************************/
function advanceSelectScreen () {
    advanceToNextScreen($selectScreen);
}

/************************************************************
 * The player clicked on the back button on the main select
 * screen.
 ************************************************************/
function backSelectScreen () {
	screenTransition($selectScreen, $titleScreen);
}

/**********************************************************************
 *****                     Display Functions                      *****
 **********************************************************************/
 
/************************************************************
 * Displays all of the current players on the main select
 * screen.
 ************************************************************/
function updateSelectionVisuals () {
    /* update all opponents */
    for (var i = 1; i < players.length; i++) {
        if (players[i]) {
            /* update dialogue */
            $selectDialogues[i-1].html(players[i].state[players[i].current].dialogue);
            
            /* determine if the advance dialogue button should be shown */
            if (players[i].state.length > players[i].current+1) {
                $selectAdvanceButtons[i-1].css({opacity : 1});
            } else {
                $selectAdvanceButtons[i-1].css({opacity : 0});
            }
			
			/* show the bubble */
			$selectBubbles[i-1].show();
            
            /* update image */
            $selectImages[i-1].attr('src', players[i].folder + players[i].state[players[i].current].image);
            
            /* update label */
            $selectLabels[i-1].html(players[i].label);
            
            /* change the button */
            $selectButtons[i-1].html("Remove Opponent");
            $selectButtons[i-1].removeClass("smooth-button-green");
            $selectButtons[i-1].addClass("smooth-button-red");
        } else {
            /* clear the view */
            $selectDialogues[i-1].html("");
            $selectAdvanceButtons[i-1].css({opacity : 0});
			$selectBubbles[i-1].hide();
            $selectImages[i-1].attr('src', BLANK_PLAYER_IMAGE);
            $selectLabels[i-1].html("Opponent "+i);
            
            /* change the button */
            $selectButtons[i-1].html("Select Opponent");
            $selectButtons[i-1].removeClass("smooth-button-red");
            $selectButtons[i-1].addClass("smooth-button-green");
        }
    }
    
    /* check to see if all opponents are loaded */
    var loaded = 0;
    for (var i = 1; i < players.length; i++) {
        if (players[i]) {
            loaded++;
        }
    }
    
    /* if all opponents are loaded, then enable progression */
    if (loaded >= 2) {
        $selectMainButton.attr('disabled', false);
    } else {
        $selectMainButton.attr('disabled', true);
    }
}
 


/************************************************************
 * This is the callback for the group clicked rows, it
 * updates information on the group screen.
 ************************************************************/
function updateGroupScreen (playerObject) {
    /* find a spot to store this player */
    for (var i = 0; i < storedGroup.length; i++) {
        if (!storedGroup[i]) {
            storedGroup[i] = playerObject;
            $groupLabels[i+1].html(playerObject.label);
            break;
        }
    }

	/* enable the button */
	$groupButton.attr('disabled', false);
}

/************************************************************
 * This is the callback for the random buttons.
 ************************************************************/
function updateRandomSelection (playerObject) {
    /* find a spot to store this player */
    for (var i = 0; i < players.length; i++) {
        if (!players[i]) {
            players[i] = playerObject;
            break;
        }
    }

	updateSelectionVisuals();
}

/************************************************************
 * Hides the table on the single selection screen.
 ************************************************************/
function hideSelectionTable() {
    mainSelectHidden = !mainSelectHidden;
    if (mainSelectHidden) {
        $selectTable.hide();
    }
    else {
        $selectTable.show();
    }
}

/************************************************************
 * Hides the table on the single selection screen.
 ************************************************************/
function hideSingleSelectionTable() {
    singleSelectHidden = !singleSelectHidden;
    if (singleSelectHidden) {
        $individualSelectTable.hide();
    }
    else {
        $individualSelectTable.show();
    }
}

/************************************************************
 * Hides the table on the single selection screen.
 ************************************************************/
function hideGroupSelectionTable() {
    groupSelectHidden = !groupSelectHidden;
    if (groupSelectHidden) {
        $groupSelectTable.hide();
    }
    else {
        $groupSelectTable.show();
    }
}