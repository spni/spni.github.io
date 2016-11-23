/********************************************************************************
 This file contains the variables and functions that form the title and setup screens
 of the game. The parsing functions for the player.xml file, the clothing organization
 functions, and human player initialization.
 ********************************************************************************/

/**********************************************************************
 *****                   Title Screen UI Elements                 *****
 **********************************************************************/
 
$titlePanels = [$("#title-panel-1"), $("#title-panel-2")];
$nameField = $("#player-name-field");
$genderButtons = [$("#male-gender-button"), $("#female-gender-button")];
$playerSizeContainers = [$("#male-size-container"), $("#female-size-container")];
$maleSizeButtons = [$("#small-junk-button"), $("#medium-junk-button"), $("#large-junk-button")];
$femaleSizeButtons = [$("#small-boobs-button"), $("#medium-boobs-button"), $("#large-boobs-button")];
$clothingTable = $("#title-clothing-table");
$warningLabel = $("#title-warning-label");
$titleCandy = [$("#left-title-candy"), $("#right-title-candy")];

/**********************************************************************
 *****                    Title Screen Variables                  *****
 **********************************************************************/

var CANDY_OPTIONS = 9;
var CANDY_VARIANTS = 4;

var clothingChoices = [];
var selectedChoices = [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false];
 
/**********************************************************************
 *****                    Start Up Functions                      *****
 **********************************************************************/
 
/************************************************************
 * Loads all of the content required to display the title 
 * screen.
 ************************************************************/
function loadTitleScreen () {
	selectedChoices = [false, false, true, false, true, false, true, true, false, true, false, false, true, false, true];
    loadClothing();
}

/************************************************************
 * Loads and parses the player clothing XML file.
 ************************************************************/
function loadClothing () {
	/* clear previously loaded content */
	clothingChoices = [];
	
    /* load all hardcoded clothing, it's just easier this way */
	if (players[HUMAN_PLAYER].gender == eGender.MALE) {
		clothingChoices.push(createNewClothing('Hat', 'hat', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/hat.png", 3, 0));
		clothingChoices.push(createNewClothing('Jacket', 'jacket', MINOR_ARTICLE, UPPER_ARTICLE, "player/male/jacket.png", 3, 1));
		clothingChoices.push(createNewClothing('Shirt', 'shirt', MAJOR_ARTICLE, UPPER_ARTICLE, "player/male/shirt.png", 2, 2));
		clothingChoices.push(createNewClothing('T-Shirt', 't-shirt', MAJOR_ARTICLE, UPPER_ARTICLE, "player/male/tshirt.png", 1, 3));
		clothingChoices.push(createNewClothing('Undershirt', 'undershirt', IMPORTANT_ARTICLE, UPPER_ARTICLE, "player/male/undershirt.png", 0, 4));
		
		clothingChoices.push(createNewClothing('Headphones', 'headphones', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/headphones.png", 3, 5));
		clothingChoices.push(createNewClothing('Belt', 'belt', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/belt.png", 3, 6));
		clothingChoices.push(createNewClothing('Pants', 'pants', MAJOR_ARTICLE, LOWER_ARTICLE, "player/male/pants.png", 2, 7));
		clothingChoices.push(createNewClothing('Shorts', 'shorts', MAJOR_ARTICLE, LOWER_ARTICLE, "player/male/shorts.png", 1, 8));
		clothingChoices.push(createNewClothing('Boxers', 'boxers', IMPORTANT_ARTICLE, LOWER_ARTICLE, "player/male/boxers.png", 0, 9));
		
		clothingChoices.push(createNewClothing('Tie', 'tie', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/tie.png", 3, 10));
		clothingChoices.push(createNewClothing('Gloves', 'gloves', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/gloves.png", 3, 11));
		clothingChoices.push(createNewClothing('Shoes', 'shoes', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/shoes.png", 3, 12));
		clothingChoices.push(createNewClothing('Boots', 'boots', EXTRA_ARTICLE, OTHER_ARTICLE, "player/male/boots.png", 3, 13));
		clothingChoices.push(createNewClothing('Socks', 'socks', MINOR_ARTICLE, OTHER_ARTICLE, "player/male/socks.png", 2, 14));
	} else if (players[HUMAN_PLAYER].gender == eGender.FEMALE) {
		clothingChoices.push(createNewClothing('Hat', 'hat', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/hat.png", 3, 0));
		clothingChoices.push(createNewClothing('Jacket', 'jacket', MINOR_ARTICLE, UPPER_ARTICLE, "player/female/jacket.png", 3, 1));
		clothingChoices.push(createNewClothing('Shirt', 'shirt', MAJOR_ARTICLE, UPPER_ARTICLE, "player/female/shirt.png", 2, 2));
		clothingChoices.push(createNewClothing('Tank Top', 'tank top', MAJOR_ARTICLE, UPPER_ARTICLE, "player/female/tanktop.png", 1, 3));
		clothingChoices.push(createNewClothing('Bra', 'bra', IMPORTANT_ARTICLE, UPPER_ARTICLE, "player/female/bra.png", 0, 4));
		
		clothingChoices.push(createNewClothing('Headphones', 'headphones', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/headphones.png", 3, 5));
		clothingChoices.push(createNewClothing('Belt', 'belt', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/belt.png", 3, 6));
		clothingChoices.push(createNewClothing('Pants', 'pants', MAJOR_ARTICLE, LOWER_ARTICLE, "player/female/pants.png", 2, 7));
		clothingChoices.push(createNewClothing('Skirt', 'skirt', MAJOR_ARTICLE, LOWER_ARTICLE, "player/female/skirt.png", 1, 8));
		clothingChoices.push(createNewClothing('Panties', 'panties', IMPORTANT_ARTICLE, LOWER_ARTICLE, "player/female/panties.png", 0, 9));
		
		clothingChoices.push(createNewClothing('Necklace', 'necklace', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/necklace.png", 3, 10));
		clothingChoices.push(createNewClothing('Gloves', 'gloves', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/gloves.png", 3, 11));
		clothingChoices.push(createNewClothing('Shoes', 'shoes', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/shoes.png", 3, 12));
		clothingChoices.push(createNewClothing('Stockings', 'stockings', EXTRA_ARTICLE, OTHER_ARTICLE, "player/female/stockings.png", 3, 13));
		clothingChoices.push(createNewClothing('Socks', 'socks', MINOR_ARTICLE, OTHER_ARTICLE, "player/female/socks.png", 2, 14));
	}
	updateTitleClothing();
}

/************************************************************
 * Updates the clothing on the title screen.
 ************************************************************/
function updateTitleClothing () {
	if (players[HUMAN_PLAYER].gender == eGender.MALE) {
		$('#female-clothing-container').hide();
		$('#male-clothing-container').show();
	} else if (players[HUMAN_PLAYER].gender == eGender.FEMALE) {
		$('#male-clothing-container').hide();
		$('#female-clothing-container').show();
	}
	
	for (var i = 0; i < selectedChoices.length; i++) {
		if (selectedChoices[i]) {
			$('#'+players[HUMAN_PLAYER].gender+'-clothing-option-'+i).css('opacity', '1');
		} else {
			$('#'+players[HUMAN_PLAYER].gender+'-clothing-option-'+i).css('opacity', '0.4');
		}
	}
	//$warningLabel.html("");
}

/************************************************************
 * Updates the clothing on the title screen based on already
 * worn clothing.
 ************************************************************/
function holdTitleClothing () {
	/* clear selection */
	for (var i = 0; i < selectedChoices.length; i++) {
		selectedChoices[i] = false;
	}
	
	/* hold worn clothing */
	for (var i = 0; i < players[HUMAN_PLAYER].clothing.length; i++) {
		if (players[HUMAN_PLAYER].clothing[i]) {
			selectedChoices[players[HUMAN_PLAYER].clothing[i].id] = true; 
		}
	}
	updateTitleClothing();
}
 
 
/**********************************************************************
 *****                   Interaction Functions                    *****
 **********************************************************************/
 
/************************************************************
 * The player clicked on one of the gender icons on the title 
 * screen, or this was called by an internal source.
 ************************************************************/
function changePlayerGender (gender) {
	players[HUMAN_PLAYER].gender = gender;
	
	/* update visuals */
	if (gender == eGender.MALE) {
		$genderButtons[0].css({opacity: 1});
		$genderButtons[1].css({opacity: 0.4});
		$playerSizeContainers[0].show();
		$playerSizeContainers[1].hide();
	} else if (gender == eGender.FEMALE) {
		$genderButtons[0].css({opacity: 0.4});
		$genderButtons[1].css({opacity: 1});
		$playerSizeContainers[0].hide();
		$playerSizeContainers[1].show();
	}
	loadClothing();
}

/************************************************************
 * The player clicked on one of the size icons on the title 
 * screen, or this was called by an internal source.
 ************************************************************/
function changePlayerSize (size) {
	players[HUMAN_PLAYER].size = size;
	
	/* update visuals */
	if (players[HUMAN_PLAYER].gender == eGender.MALE) {
		if (size == eSize.SMALL) {
			$maleSizeButtons[0].css({opacity: 1});
			$maleSizeButtons[1].css({opacity: 0.4});
			$maleSizeButtons[2].css({opacity: 0.4});
		} else if (size == eSize.LARGE) {
			$maleSizeButtons[0].css({opacity: 0.4});
			$maleSizeButtons[1].css({opacity: 0.4});
			$maleSizeButtons[2].css({opacity: 1});
		} else {
			$maleSizeButtons[0].css({opacity: 0.4});
			$maleSizeButtons[1].css({opacity: 1});
			$maleSizeButtons[2].css({opacity: 0.4});
		}
	} else if (players[HUMAN_PLAYER].gender == eGender.FEMALE) {
		if (size == eSize.SMALL) {
			$femaleSizeButtons[0].css({opacity: 1});
			$femaleSizeButtons[1].css({opacity: 0.4});
			$femaleSizeButtons[2].css({opacity: 0.4});
		} else if (size == eSize.LARGE) {
			$femaleSizeButtons[0].css({opacity: 0.4});
			$femaleSizeButtons[1].css({opacity: 0.4});
			$femaleSizeButtons[2].css({opacity: 1});
		} else {
			$femaleSizeButtons[0].css({opacity: 0.4});
			$femaleSizeButtons[1].css({opacity: 1});
			$femaleSizeButtons[2].css({opacity: 0.4});
		}
	}
}

/************************************************************
 * The player clicked on an article of clothing on the title 
 * screen.
 ************************************************************/
function selectClothing (id) {
	if (selectedChoices[id]) {
		selectedChoices[id] = false;
	} else {
		selectedChoices[id] = true;
	} 
	updateTitleClothing();
}
 
/************************************************************
 * The player clicked on the advance button on the title 
 * screen.
 ************************************************************/
function validateTitleScreen () {
    /* determine the player's name */
	if ($nameField.val() != "") {
		players[HUMAN_PLAYER].first = $nameField.val();
        players[HUMAN_PLAYER].label = $nameField.val();
	} else if (players[HUMAN_PLAYER].gender == "male") {
		players[HUMAN_PLAYER].first = "Mister";
		players[HUMAN_PLAYER].label = "Mister";
	} else if (players[HUMAN_PLAYER].gender == "female") {
		players[HUMAN_PLAYER].first = "Missy";
		players[HUMAN_PLAYER].label = "Missy";
	}
	$gameLabels[HUMAN_PLAYER].html(players[HUMAN_PLAYER].label);
	
	/* count clothing */
	var clothingCount = [0, 0, 0, 0];
	for (var i = 0; i < clothingChoices.length; i++) {
		if (selectedChoices[i]) {
			if (clothingChoices[i].position == UPPER_ARTICLE) {
				clothingCount[0]++;
			} else if (clothingChoices[i].position == LOWER_ARTICLE) {
				clothingCount[1]++;
			} else {
				clothingCount[2]++;
			}
			clothingCount[3]++;
		}
	}
	console.log(clothingCount);

	/* ensure the player is wearing enough clothing */
	if (clothingCount[0] < 1) {
		$warningLabel.html("You must wear at least 1 article of clothing on your upper body.");
		return;
	} else if (clothingCount[1] < 1) {
		$warningLabel.html( "You must wear at least 1 article of clothing on your lower body.");
		return;
	} else if (clothingCount[3] < 2) {
		$warningLabel.html("You must be wearing at least 2 articles of clothing. Nudist.");
		return;
	} else if (clothingCount[3] > 8) {
		$warningLabel.html("You cannot wear more than 8 articles of clothing. Cheater.");
		return;
	}
    
    /* dress the player */
    wearClothing();
	console.log(players[0]);
    
    screenTransition($titleScreen, $selectScreen);
}

/**********************************************************************
 *****                    Additional Functions                    *****
 **********************************************************************/

/************************************************************
 * Takes all of the clothing selected by the player and adds it, 
 * in a particular order, to the list of clothing they are wearing.
 ************************************************************/
function wearClothing () {
	var position = [[], [], []];
	var importantWorn = [false, false];
	
	/* sort the clothing by position */
	for (var i = clothingChoices.length - 1; i >= 0; i--) {
		if (selectedChoices[i] && clothingChoices[i].position == UPPER_ARTICLE) {
			position[0].push(clothingChoices[i]);
		} else if (selectedChoices[i] && clothingChoices[i].position == LOWER_ARTICLE) {
			position[1].push(clothingChoices[i]);
		} else if (selectedChoices[i]) {
			position[2].push(clothingChoices[i]);
		}
	}
	
	/* clear player clothing array */
	players[HUMAN_PLAYER].clothing = [];
	
	/* wear the clothing is sorted order */
	for (var i = 0; i < position[0].length || i < position[1].length; i++) {
		/* wear a lower article, if any remain */
		if (i < position[1].length) {
			if (position[1][i].type == IMPORTANT_ARTICLE) {
				importantWorn[1] = true;
			} else if (!importantWorn[1]) {
				position[1][i].type = IMPORTANT_ARTICLE;
			}
			
			players[HUMAN_PLAYER].clothing.push(position[1][i]);
		}
		
		/* wear an upper article, if any remain */
		if (i < position[0].length) {
			if (position[0][i].type == IMPORTANT_ARTICLE) {
				importantWorn[0] = true;
			} else if (!importantWorn[0]) {
				position[0][i].type = IMPORTANT_ARTICLE;
			}
			
			players[HUMAN_PLAYER].clothing.push(position[0][i]);
		}
	}
	
	/* wear any other clothing */
	for (var i = 0; i < position[2].length; i++) {
		players[HUMAN_PLAYER].clothing.push(position[2][i]);
	}
	
	/* update the visuals */
    displayHumanPlayerClothing();
}
	
 
/************************************************************
 * Randomly selects two characters for the title images.
 ************************************************************/
function selectTitleCandy() {
    console.log("Selecting Candy...");
    var rand1 = getRandomNumber(1, CANDY_OPTIONS + 1);
    var rand2 = getRandomNumber(1, CANDY_OPTIONS + 1);
    var rand3 = getRandomNumber(1, CANDY_VARIANTS + 1);
    var rand4 = getRandomNumber(1, CANDY_VARIANTS + 1);
    
    if (rand2 == rand1) {
        rand2 += 1;
        if (rand2 == CANDY_OPTIONS + 1) {
            rand2 = 1;
        }
    }
    
    $titleCandy[0].attr("src", IMG + "candy/" + rand1 + "-" + rand3 + ".png");
    $titleCandy[1].attr("src", IMG + "candy/" + rand2 + "-" + rand4 + ".png");
}
 