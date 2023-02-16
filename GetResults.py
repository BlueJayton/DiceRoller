import random

def calculate_boost_dice (boost, counted_results_dict):
    if boost == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(boost):
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

def calculate_setback_dice (setback, counted_results_dict):
    if setback == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(setback):
        roll = random.choice(num_of_faces)
        
        if (roll == 3):
            counted_results_dict['Failures'] += 1
        elif (roll == 4):
            counted_results_dict['Failures'] += 1
        elif (roll == 5):
            counted_results_dict['Failures'] += 1
        elif (roll == 6):
            counted_results_dict['Failures'] += 1
            
    return

def calculate_ability_dice (ability, counted_results_dict):
    if ability == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(ability):
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

def calculate_difficulty_dice (difficulty, counted_results_dict):
    if difficulty == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(difficulty):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            counted_results_dict['Failures'] += 1
        elif (roll == 3):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 4):
            counted_results_dict['Failures'] += 1
        elif (roll == 5):
            counted_results_dict['Failures'] += 1
        elif (roll == 6):
            counted_results_dict['Failures'] += 1
        elif (roll == 7):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 8):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
            
    return

def calculate_proficiency_dice (proficiency, counted_results_dict):
    if proficiency == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(proficiency):
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

def calculate_challenge_dice (challenge, counted_results_dict):
    if challenge == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(challenge):
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
            counted_results_dict['Failures'] += 1
        elif (roll == 7):
            counted_results_dict['Failures'] += 1
        elif (roll == 8):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 9):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 10):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 11):
            counted_results_dict['Failures'] += 1
            counted_results_dict['Failures'] += 1
        elif (roll == 12):
            counted_results_dict['Despairs'] += 1
            
    return

def calculate_force_dice (force, counted_results_dict):
    if force == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(force):
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