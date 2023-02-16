
import random
import flask

import RollDice
import CancelandFormatResults





boost = 10
setback = 3
ability = 10
difficulty = 11
proficiency = 10
challenge = 7
force = 10
counted_results_dict = {"Successes" : 0, "Failures" : 0,
                        "Advantages" : 0, "Threats" : 0,
                        "Triumphs" : 0, "Despairs" : 0,
                        "Lights" : 0, "Darks" : 0}


#def GetDiceCounts (dicecount):


#def reset (dice):


#Function Calls
RollDice.roll_all_dice (boost, setback, ability, difficulty, proficiency, challenge, force, counted_results_dict)

cancelled_results_dict = CancelandFormatResults.cancel_out_results(counted_results_dict)

print(CancelandFormatResults.display_formatted_results(cancelled_results_dict))