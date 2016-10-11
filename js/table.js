/********************************************************************************
 This file contains the variables and functions for the Table object, which 
 maintains the state of the players and deck. It also contains methods for 
 updating the visual state of the players.
 ********************************************************************************/

/**********************************************************************
 * Enumerations
 **********************************************************************/

/************************************************************
 * An enumeration for stripping rules.
 **/
var eStripRule = {
    LOSER: 'loser',
    WINNER: 'winner'
};


/********************************************************************************
 * Poker Table Object and Elements
 ********************************************************************************/

/**********************************************************************
 * (Object) A poker table and everything involved in it.
 **/
function Table() 
{
    //this.deck = new Deck();
    //this.human = new Player(HUMAN_PLAYER);
    this.ai = [];
    this.rule = eStripRule.LOSER;
}