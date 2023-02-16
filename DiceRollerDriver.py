
import flask
import RollDice
import CancelandFormatResults
import GetDiceNums

app = flask.Flask(__name__)

@app.route('/')
def driver():
    dice_dict = {"Boost" : 10, "Setback" : 10,
                 "Ability" : 10, "Difficulty" : 10,
                 "Proficiency" : 10, "Challenge" : 10,
                 "Force" : 10}
    
    counted_results_dict = {"Successes" : 0, "Failures" : 0,
                        "Advantages" : 0, "Threats" : 0,
                        "Triumphs" : 0, "Despairs" : 0,
                        "Lights" : 0, "Darks" : 0}

    #def GetDiceCounts (dicecount):

    #def reset (dice):

    #Function Calls
    RollDice.roll_all_dice (dice_dict, counted_results_dict)

    cancelled_results_dict = CancelandFormatResults.cancel_out_results(counted_results_dict)
    display_results = CancelandFormatResults.display_formatted_results(cancelled_results_dict)
    
    return flask.render_template (
        "webpage.html",
        dice_dict = dice_dict,
        counted_results_dict = counted_results_dict,
        display_results = display_results
    )

app.run(debug=True)