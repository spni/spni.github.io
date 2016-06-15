/********************************************************************************
 This file contains the variables and functions that form the AI of the 
 non-player characters.
 ********************************************************************************/
 
/**********************************************************************
 *****                      AI Action Functions                   *****
 **********************************************************************/
 
/************************************************************
 * Uses a basic poker AI to exchange cards.
 ************************************************************/
function determineAIAction (player) {
	/* determine the current hand */
	determineHand(player);
	
	/* collect the ranks and suits of the cards */
	var hand = hands[player].cards;
	var cardRanks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	var cardSuits = [0, 0, 0, 0];
	
	for (var i = 0; i < hand.length; i++) {
		cardRanks[getCardValue(hand[i]) - 1]++;
		if (getCardValue(hand[i]) == 1) {
			cardRanks[13]++;
		}
		cardSuits[getCardSuitValue(hand[i])]++;
	}
	
	/* if the current hand is good enough, then take a pre-determined action */
	if (hands[player].strength >= STRAIGHT) {
		/* give up nothing */
		hands[player].tradeIns = [false, false, false, false, false];
		console.log("Hand is really good, will trade in nothing. "+hands[player].tradeIns);
		return;
	}
	
	/* if the current hand is good enough, then take a pre-determined action */
	if (hands[player].strength == THREE_OF_A_KIND) {
		/* give up the odd cards out */
		var sameValue = 0;
		for (var i = 0; i < cardRanks.length; i++) {
			if (cardRanks[i] == 3) {
				sameValue = i+1;
				break;
			}
		}
		
		hands[player].tradeIns = [false, false, false, false, false];
		for (var i = 0; i < hand.length; i++) {
			if (getCardValue(hand[i]) != sameValue) {
				hands[player].tradeIns[i] = true;
			}
		}
		console.log("Hand is good, will trade in two cards. "+hands[player].tradeIns);
		return;
	}
	
	/* if the current hand is good enough, then take a pre-determined action */
	if (hands[player].strength == TWO_PAIR) {
		/* give up the odd card out */
		var sameValue = [0, 0];
		for (var i = 1; i < cardRanks.length; i++) {
			if (cardRanks[i] == 2) {
				if (sameValue[0] == 0) {
					sameValue[0] = i+1;
				} else {
					sameValue[1] = i+1;
				}
			}
		}
        
		hands[player].tradeIns = [false, false, false, false, false];
		for (var i = 0; i < hand.length; i++) {
			if (getCardValue(hand[i]) != sameValue[0] && getCardValue(hand[i]) != sameValue[1]) {
				hands[player].tradeIns[i] = true;
			}
		}
		console.log("Hand is good, will trade in one card. "+hands[player].tradeIns);
		return;
	}
	
	/* otherwise, consider your options */
	var one_from_flush = -1;
	var straight_gap = -1;
	var straight_block = -1;
	var one_from_straight = -1;
	
	/* first, look to see if a straight is possible */
	var sequence = 0;
	for (var i = 0; i < cardRanks.length; i++) {
		if (cardRanks[i] == 0 && straight_gap < 0 && sequence != 1) {
			/* 0, potential gap */
			straight_gap = i;
		} else if (cardRanks[i] == 0 && straight_gap < 0 && sequence == 1) {
			/* 0, potential gap and potential block */
			straight_gap = i;
			straight_block = i;
		} else if (cardRanks[i] == 0 && straight_gap >= 0) {
			/* 00, potential gap but restart the sequence */
			straight_gap = i+1;
			sequence = 0;
		} else if (cardRanks[i] == 1) {
			/* 1, adds to the sequence */
			straight_gap = -1;
			sequence++;
		} else if (cardRanks[i] == 2 && straight_block < 0) {
			/* 2, adds to the sequence, the gap, and the block */
			straight_gap = i;
			straight_block = i+1;
			sequence++;
		} else if (cardRanks[i] == 2 && straight_block >= 0) {
			/* 22, no potential*/
			break;
		} else {
			/* >2, no potential */
			break;
		}
		
		/* if there is 4 in sequence */
		if (sequence == hand.length - 1) {
			/* chance at a straight */
			if (straight_block < 0) {
				for (var j = i; j < cardRanks.length; j++) {
					if (cardRanks[i] <= 2) {
						straight_block = j;
					}
				}
			}

			for (var j = 0; j < hand.length; j++) {
				if (getCardValue(hand[j]) == straight_block) {
					one_from_straight = j;
					break;
				}
			}
			break;
		}
	}
	
	/* second, look to see if a flush is possible */
	for (var i = 0; i < cardSuits.length; i++) {
		if (cardSuits[i] == hand.length - 1) {
			/* chance at a flush */
			for (var j = 0; j < hand.length; j++) {
				if (getCardSuitValue(hand[j]) != i) {
					one_from_flush = j;
				}
			}
			break;
		} else if (cardSuits[i] > 1) {
			/* very little chance at a flush */
			break;
		}
	}
	
	/* now, take each remaining hand into special consideration */
	if (hands[player].strength == PAIR) {
		/* if you are one away from a flush, give up the pair for it */
		if (one_from_flush > 0) {
			hands[player].tradeIns = [false, false, false, false, false];
			hands[player].tradeIns[one_from_flush] = true;
			console.log("Hand is okay, going for a flush, trading in one card. "+hands[player].tradeIns);
			return;
		}
		
		/* otherwise, give up every other card */
		var sameValue = 0;
		for (var i = 0; i < cardRanks.length; i++) {
			if (cardRanks[i] == 2) {
				sameValue = i+1;
				break;
			}
		}
		
		hands[player].tradeIns = [false, false, false, false, false];
		for (var i = 0; i < hand.length; i++) {
			if (getCardValue(hand[i]) != sameValue) {
				hands[player].tradeIns[i] = true;
			}
		}
		console.log("Hand is okay, trading in three cards. "+hands[player].tradeIns);
		return;
	}
	
	/* now, take each remaining hand into special consideration */
	if (hands[player].strength == HIGH_CARD) {
		/* if you are one away from a flush, go for it */
		if (one_from_flush > 0) {
			hands[player].tradeIns = [false, false, false, false, false];
			hands[player].tradeIns[one_from_flush] = true;
			console.log("Hand is bad, going for a flush, trading in one card. "+hands[player].tradeIns);
			return;
		}
		
		/* if you are one away from a straight, go for it */
		if (one_from_straight > 0) {
			hands[player].tradeIns = [false, false, false, false, false];
			hands[player].tradeIns[one_from_straight] = true;
			console.log("Hand is bad, going for a straight, trading in one card. "+hands[player].tradeIns);
			return;
		}
		
		/* otherwise, give up everything but the high card */
		var highCard = 0;
		for (var i = cardRanks.length-1; i > 0; i--) {
			if (cardRanks[i] == 1) {
				if (i == 13) {
					highCard = 1;
				} else {
					highCard = i+1;
				}
				break;
			}
		}
		
		hands[player].tradeIns = [false, false, false, false, false];
		for (var i = 0; i < hand.length; i++) {
			if (getCardValue(hand[i]) != highCard) {
				hands[player].tradeIns[i] = true;
			}
		}
		console.log("Hand is bad, trading in four cards. "+hands[player].tradeIns);
		return;
	}
	
	/* end of function, otherwise just trade in everything */
	hands[player].tradeIns = [true, true, true, true, true];
	console.log("Hand is horrid, trading in everything. "+hands[player].tradeIns);
	return;
}