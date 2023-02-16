
import random


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

def cancel_out_results (counted_results_dict):
    
    #Cancel successes and failures out
    if (counted_results_dict['Successes'] == counted_results_dict['Failures']):
        counted_results_dict['Successes'] = 0
        counted_results_dict['Failures'] = 0
    elif (counted_results_dict['Successes'] > counted_results_dict['Failures']):
        counted_results_dict['Successes'] = counted_results_dict['Successes'] - counted_results_dict['Failures']
        counted_results_dict['Failures'] = 0
    elif (counted_results_dict['Failures'] > counted_results_dict['Successes']):
        counted_results_dict['Failures'] = counted_results_dict['Failures'] - counted_results_dict['Successes']
        counted_results_dict['Successes'] = 0
        
    #Cancel advantages and threats out
    if (counted_results_dict['Advantages'] == counted_results_dict['Threats']):
        counted_results_dict['Advantages'] = 0
        counted_results_dict['Threats'] = 0
    elif (counted_results_dict['Advantages'] > counted_results_dict['Threats']):
        counted_results_dict['Advantages'] = counted_results_dict['Advantages'] - counted_results_dict['Threats']
        counted_results_dict['Threats'] = counted_results_dict['Threats'] - counted_results_dict['Threats']
    elif (counted_results_dict['Threats'] > counted_results_dict['Advantages']):
        counted_results_dict['Threats'] = counted_results_dict['Threats'] - counted_results_dict['Advantages']
        counted_results_dict['Advantages'] = counted_results_dict['Advantages'] - counted_results_dict['Advantages']
        
    return counted_results_dict

def display_formatted_results (results_dict):
    
    output = []
    
    if (results_dict['Successes'] > 1):
        output.append(f"{results_dict['Successes']} successes")
    elif (results_dict['Successes'] == 1):
        output.append(f"{results_dict['Successes']} success")
        
    if (results_dict['Failures'] > 1):
        output.append(f"{results_dict['Failures']} failures")
    elif (results_dict['Failures'] == 1):
        output.append(f"{results_dict['Failures']} failure")
        
    if (results_dict['Advantages'] > 1):
        output.append(f"{results_dict['Advantages']} advantages")
    elif (results_dict['Advantages'] == 1):
        output.append(f"{results_dict['Advantages']} advantage")
        
    if (results_dict['Threats'] > 1):
        output.append(f"{results_dict['Threats']} threats")
    elif (results_dict['Threats'] == 1):
        output.append(f"{results_dict['Threats']} threat")
        
    if (results_dict['Triumphs'] > 1):
        output.append(f"{results_dict['Triumphs']} triumphs")
    elif (results_dict['Triumphs'] == 1):
        output.append(f"{results_dict['Triumphs']} triumph")
        
    if (results_dict['Despairs'] > 1):
        output.append(f"{results_dict['Despairs']} despairs")
    elif (results_dict['Despairs'] == 1):
        output.append(f"{results_dict['Despairs']} despair")
        
    if (results_dict['Lights'] > 1):
        output.append(f"{results_dict['Lights']} light")
    elif (results_dict['Lights'] == 1):
        output.append(f"{results_dict['Lights']} light")
        
    if (results_dict['Darks'] > 1):
        output.append(f"{results_dict['Darks']} dark")
    elif (results_dict['Darks'] == 1):
        output.append(f"{results_dict['Darks']} dark")
        
    if (results_dict['Successes'] == 0 and results_dict['Failures'] == 0 
        and results_dict['Advantages'] == 0 and results_dict['Threats'] == 0 
        and results_dict['Triumphs'] == 0 and results_dict['Despairs'] == 0 
        and results_dict['Lights'] == 0 and results_dict['Darks'] == 0):
            return "It's a wash!!!"
        
    output = ', ' .join(output)
    return output

#def reset (dice):


     

#Function Calls
calculate_boost_dice(boost, counted_results_dict)
calculate_setback_dice(setback, counted_results_dict)
calculate_ability_dice(ability, counted_results_dict)
calculate_difficulty_dice(difficulty, counted_results_dict)
calculate_proficiency_dice(proficiency, counted_results_dict)
calculate_challenge_dice(challenge, counted_results_dict)
calculate_force_dice(force, counted_results_dict)

cancelled_results_dict = cancel_out_results(counted_results_dict)

print(display_formatted_results(cancelled_results_dict))
