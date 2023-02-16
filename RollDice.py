import GetResults

def roll_all_dice (boost, setback, ability, difficulty, proficiency, challenge, force, counted_results_dict):
    
    GetResults.calculate_boost_dice(boost, counted_results_dict)
    GetResults.calculate_setback_dice(setback, counted_results_dict)
    GetResults.calculate_ability_dice(ability, counted_results_dict)
    GetResults.calculate_difficulty_dice(difficulty, counted_results_dict)
    GetResults.calculate_proficiency_dice(proficiency, counted_results_dict)
    GetResults.calculate_challenge_dice(challenge, counted_results_dict)
    GetResults.calculate_force_dice(force, counted_results_dict)
    
    return