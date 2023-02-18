import random

def calculate_boost_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Boost"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(int(dice_dict["Boost"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 3):
            counted_results_dict['Successes'] += 1
        elif (roll == 4):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 5):
            counted_results_dict['Advantages'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 6):
            counted_results_dict['Advantages'] += 1
            
    return

def calculate_setback_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Setback"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(int(dice_dict["Setback"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 3):
            counted_results_dict['Failures'] += 1
        elif (roll == 4):
            counted_results_dict['Failures'] += 1
        elif (roll == 5):
            counted_results_dict['Threats'] += 1
        elif (roll == 6):
            counted_results_dict['Threats'] += 1
            
    return

def calculate_ability_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Ability"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(int(dice_dict["Ability"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            counted_results_dict['Successes'] += 1
        elif (roll == 3):
            counted_results_dict['Successes'] += 1
        elif (roll == 4):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Successes'] += 1
        elif (roll == 5):
            counted_results_dict['Advantages'] += 1
        elif (roll == 6):
            counted_results_dict['Advantages'] += 1
        elif (roll == 7):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 8):
            counted_results_dict['Advantages'] += 1
            counted_results_dict['Advantages'] += 1
            
    return

def calculate_difficulty_dice (dice_dict, counted_results_dict):
    if (int(dice_dict["Difficulty"])) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(int(dice_dict["Difficulty"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            counted_results_dict['Failures'] += 1
        elif (roll == 3):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 4):
            counted_results_dict['Threats'] += 1
        elif (roll == 5):
            counted_results_dict['Threats'] += 1
        elif (roll == 6):
            counted_results_dict['Threats'] += 1
        elif (roll == 7):
            counted_results_dict['Threats'] += 1
            counted_results_dict['Threats'] += 1
        elif (roll == 8):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Threats'] += 1
            
    return

def calculate_proficiency_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Proficiency"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(int(dice_dict["Proficiency"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            counted_results_dict['Successes'] += 1
        elif (roll == 3):
            counted_results_dict['Successes'] += 1
        elif (roll == 4):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Successes'] += 1
        elif (roll == 5):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Successes'] += 1
        elif (roll == 6):
            counted_results_dict['Advantages'] += 1
        elif (roll == 7):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 8):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 9):
            counted_results_dict['Successes'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 10):
            counted_results_dict['Advantages'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 11):
            counted_results_dict['Advantages'] += 1
            counted_results_dict['Advantages'] += 1
        elif (roll == 12):
            counted_results_dict['Triumphs'] += 1
            
    return

def calculate_challenge_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Challenge"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(int(dice_dict["Challenge"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            counted_results_dict['Failures'] += 1
        elif (roll == 3):
            counted_results_dict['Failures'] += 1
        elif (roll == 4):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 5):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 6):
            counted_results_dict['Threats'] += 1
        elif (roll == 7):
            counted_results_dict['Threats'] += 1
        elif (roll == 8):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Threats'] += 1
        elif (roll == 9):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Threats'] += 1
        elif (roll == 10):
            counted_results_dict['Threats'] += 1
            counted_results_dict['Threats'] += 1
        elif (roll == 11):
            counted_results_dict['Threats'] += 1
            counted_results_dict['Threats'] += 1
        elif (roll == 12):
            counted_results_dict['Despairs'] += 1
            
    return

def calculate_force_dice (dice_dict, counted_results_dict):
    if int(dice_dict["Force"]) == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(int(dice_dict["Force"])):
        roll = random.choice(num_of_faces)
        
        if (roll == 1):
            counted_results_dict['Darks'] += 1
        elif (roll == 2):
            counted_results_dict['Darks'] += 1
        elif (roll == 3):
            counted_results_dict['Darks'] += 1
        elif (roll == 4):
            counted_results_dict['Darks'] += 1
        elif (roll == 5):
            counted_results_dict['Darks'] += 1
        elif (roll == 6):
            counted_results_dict['Darks'] += 1
        elif (roll == 7):
            counted_results_dict['Darks'] += 1
            counted_results_dict['Darks'] += 1
        elif (roll == 8):
            counted_results_dict['Lights'] += 1
        elif (roll == 9):
            counted_results_dict['Lights'] += 1
        elif (roll == 10):
            counted_results_dict['Lights'] += 1
            counted_results_dict['Lights'] += 1
        elif (roll == 11):
            counted_results_dict['Lights'] += 1
            counted_results_dict['Lights'] += 1
        elif (roll == 12):
            counted_results_dict['Lights'] += 1
            counted_results_dict['Lights'] += 1
            
    return