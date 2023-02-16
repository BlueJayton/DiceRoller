import GetResults

def roll_all_dice (dice_dict, counted_results_dict):
    
    GetResults.calculate_boost_dice(dice_dict["Boost"], counted_results_dict)
    GetResults.calculate_setback_dice(dice_dict["Setback"], counted_results_dict)
    GetResults.calculate_ability_dice(dice_dict["Ability"], counted_results_dict)
    GetResults.calculate_difficulty_dice(dice_dict["Difficulty"], counted_results_dict)
    GetResults.calculate_proficiency_dice(dice_dict["Proficiency"], counted_results_dict)
    GetResults.calculate_challenge_dice(dice_dict["Challenge"], counted_results_dict)
    GetResults.calculate_force_dice(dice_dict["Force"], counted_results_dict)
    
    return