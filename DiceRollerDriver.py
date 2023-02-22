
import flask
from flask import request
import RollDice
import CancelandFormatResults
import ResetDice

app = flask.Flask(__name__)

dice_dict = {"Boost" : 0, "Setback" : 0,
             "Ability" : 0, "Difficulty" : 0,
             "Proficiency" : 0, "Challenge" : 0,
             "Force" : 0}
    
counted_results_dict = {"Successes" : 0, "Failures" : 0,
                        "Advantages" : 0, "Threats" : 0,
                        "Triumphs" : 0, "Despairs" : 0,
                        "Lights" : 0, "Darks" : 0}

display_results = []

@app.route('/', methods = ['POST', 'GET'])
def driver():
    
    counted_results_dict = {"Successes" : 0, "Failures" : 0,
                            "Advantages" : 0, "Threats" : 0,
                            "Triumphs" : 0, "Despairs" : 0,
                            "Lights" : 0, "Darks" : 0}
    
    if request.method == 'POST':
        
        if request.form['submit_button'] == 'Roll':
            dice_dict["Boost"] = request.form.get("boost")
            dice_dict["Setback"] = request.form.get("setback")
            dice_dict["Ability"] = request.form.get("ability")
            dice_dict["Difficulty"] = request.form.get("difficulty")
            dice_dict["Proficiency"] = request.form.get("proficiency")
            dice_dict["Challenge"] = request.form.get("challenge")
            dice_dict["Force"] = request.form.get("force")
        
            RollDice.roll_all_dice (dice_dict, counted_results_dict)
        elif request.form['submit_button'] == 'Reset':
            ResetDice.reset_dice(dice_dict)

    cancelled_results_dict = CancelandFormatResults.cancel_out_results(counted_results_dict)
    display_results = CancelandFormatResults.display_formatted_results(cancelled_results_dict, dice_dict)
    
    
    return flask.render_template (
        "webpage.html",
        dice_dict = dice_dict,
        display_results = display_results
    )

app.run(debug = True)