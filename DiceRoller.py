
import random


num_of_boost_dice = 10
num_of_setback_dice = 10
num_of_ability_dice = 10
num_of_difficulty_dice = 10
num_of_proficiency_dice = 10
num_of_challenge_dice = 10
num_of_force_dice = 10
results = []
counted_results_dict = {"Successes" : 0,
                   "Failures" : 0,
                   "Advantages" : 0,
                   "Threats" : 0,
                   "Triumphs" : 0,
                   "Despairs" : 0,
                   "Lights" : 0,
                   "Darks" : 0}


#def GetDiceCounts (dicecount):
        

def calculate_boost_dice (num_of_boost_dice, results):
    if num_of_boost_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(num_of_boost_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 3):
            results.append("Success")
        elif (roll == 4):
            results.append("Success")
            results.append("Advantage")
        elif (roll == 5):
            results.append("Advantage")
            results.append("Advantage")
        elif (roll == 6):
            results.append("Advantage")
            
    return

def calculate_setback_dice (num_of_setback_dice, results):
    if num_of_setback_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(num_of_setback_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 3):
            results.append("Failure")
        elif (roll == 4):
            results.append("Failure")
        elif (roll == 5):
            results.append("Threat")
        elif (roll == 6):
            results.append("Threat")
            
    return

def calculate_ability_dice (num_of_ability_dice, results):
    if num_of_ability_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(num_of_ability_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            results.append("Success")
        elif (roll == 3):
            results.append("Success")
        elif (roll == 4):
            results.append("Success")
            results.append("Success")
        elif (roll == 5):
            results.append("Advantage")
        elif (roll == 6):
            results.append("Advantage")
        elif (roll == 7):
            results.append("Success")
            results.append("Advantage")
        elif (roll == 8):
            results.append("Advantage")
            results.append("Advantage")
            
    return

def calculate_difficulty_dice (num_of_difficulty_dice, results):
    if num_of_difficulty_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(num_of_difficulty_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            results.append("Failure")
        elif (roll == 3):
            results.append("Failure")
            results.append("Failure")
        elif (roll == 4):
            results.append("Threat")
        elif (roll == 5):
            results.append("Threat")
        elif (roll == 6):
            results.append("Threat")
        elif (roll == 7):
            results.append("Threat")
            results.append("Threat")
        elif (roll == 8):
            results.append("Failure")
            results.append("Threat")
            
    return

def calculate_proficiency_dice (num_of_proficiency_dice, results):
    if num_of_proficiency_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(num_of_proficiency_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            results.append("Success")
        elif (roll == 3):
            results.append("Success")
        elif (roll == 4):
            results.append("Success")
            results.append("Success")
        elif (roll == 5):
            results.append("Success")
            results.append("Success")
        elif (roll == 6):
            results.append("Advantage")
        elif (roll == 7):
            results.append("Success")
            results.append("Advantage")
        elif (roll == 8):
            results.append("Success")
            results.append("Advantage")
        elif (roll == 9):
            results.append("Success")
            results.append("Advantage")
        elif (roll == 10):
            results.append("Advantage")
            results.append("Advantage")
        elif (roll == 11):
            results.append("Advantage")
            results.append("Advantage")
        elif (roll == 12):
            results.append("Triumph")
            
    return

def calculate_challenge_dice (num_of_challenge_dice, results):
    if num_of_challenge_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(num_of_challenge_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 2):
            results.append("Failure")
        elif (roll == 3):
            results.append("Failure")
        elif (roll == 4):
            results.append("Failure")
            results.append("Failure")
        elif (roll == 5):
            results.append("Failure")
            results.append("Failure")
        elif (roll == 6):
            results.append("Threat")
        elif (roll == 7):
            results.append("Threat")
        elif (roll == 8):
            results.append("Failure")
            results.append("Threat")
        elif (roll == 9):
            results.append("Failure")
            results.append("Threat")
        elif (roll == 10):
            results.append("Threat")
            results.append("Threat")
        elif (roll == 11):
            results.append("Threat")
            results.append("Threat")
        elif (roll == 12):
            results.append("Despair")
            
    return

def calculate_force_dice (num_of_force_dice, results):
    if num_of_force_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(num_of_force_dice):
        roll = random.choice(num_of_faces)
        
        if (roll == 1):
            results.append("Dark")
        elif (roll == 2):
            results.append("Dark")
        elif (roll == 3):
            results.append("Dark")
        elif (roll == 4):
            results.append("Dark")
        elif (roll == 5):
            results.append("Dark")
        elif (roll == 6):
            results.append("Dark")
        elif (roll == 7):
            results.append("Dark")
            results.append("Dark")
        elif (roll == 8):
            results.append("Light")
        elif (roll == 9):
            results.append("Light")
        elif (roll == 10):
            results.append("Light")
            results.append("Light")
        elif (roll == 11):
            results.append("Light")
            results.append("Light")
        elif (roll == 12):
            results.append("Light")
            results.append("Light")
            
    return

def count_results (results, counted_results_dict):
        
    for word in results:
        if (word == "Success"):
            counted_results_dict['Successes'] = counted_results_dict['Successes'] + 1
        elif (word == "Failure"):
            counted_results_dict['Failures'] = counted_results_dict['Failures'] + 1
        elif (word == "Advantage"):
            counted_results_dict['Advantages'] = counted_results_dict['Advantages'] + 1
        elif (word == "Threat"):
            counted_results_dict['Threats'] = counted_results_dict['Threats'] + 1
        elif (word == "Triumph"):
            counted_results_dict['Triumphs'] = counted_results_dict['Triumphs'] + 1
        elif (word == "Despair"):
            counted_results_dict['Despairs'] = counted_results_dict['Despairs'] + 1
        elif (word == "Light"):
            counted_results_dict['Lights'] = counted_results_dict['Lights'] + 1
        elif (word == "Dark"):
            counted_results_dict['Darks'] = counted_results_dict['Darks'] + 1
    
    return counted_results_dict

def cancel_out_results (counted_results_dict):
    
    #Cancel successes and failures out
    if (counted_results_dict['Successes'] == counted_results_dict['Failures']):
        counted_results_dict['Successes'] = 0
        counted_results_dict['Failures'] = 0
    elif (counted_results_dict['Successes'] > counted_results_dict['Failures']):
        counted_results_dict['Successes'] = counted_results_dict['Successes'] - counted_results_dict['Failures']
        counted_results_dict['Failures'] = counted_results_dict['Failures'] - counted_results_dict['Failures']
    elif (counted_results_dict['Failures'] > counted_results_dict['Successes']):
        counted_results_dict['Failures'] = counted_results_dict['Failures'] - counted_results_dict['Successes']
        counted_results_dict['Successes'] = counted_results_dict['Successes'] - counted_results_dict['Successes']
        
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
        
    #Cancel triumphs and despairs out
    if (counted_results_dict['Triumphs'] == counted_results_dict['Despairs']):
        counted_results_dict['Triumphs'] = 0
        counted_results_dict['Despairs'] = 0
    elif (counted_results_dict['Triumphs'] > counted_results_dict['Despairs']):
        counted_results_dict['Triumphs'] = counted_results_dict['Triumphs'] - counted_results_dict['Despairs']
        counted_results_dict['Despairs'] = counted_results_dict['Despairs'] - counted_results_dict['Despairs']
    elif (counted_results_dict['Despairs'] > counted_results_dict['Triumphs']):
        counted_results_dict['Despairs'] = counted_results_dict['Despairs'] - counted_results_dict['Triumphs']
        counted_results_dict['Triumphs'] = counted_results_dict['Triumphs'] - counted_results_dict['Triumphs']
        
    return counted_results_dict

def reset ():
    num_of_boost_dice = 0
    num_of_setback_dice = 0
    num_of_ability_dice = 0
    num_of_difficulty_dice = 0
    num_of_proficiency_dice = 0
    num_of_challenge_dice = 0
    num_of_force_dice = 0
    
    return
    
#Function Calls
calculate_boost_dice(num_of_boost_dice, results)
calculate_setback_dice(num_of_setback_dice, results)
calculate_ability_dice(num_of_ability_dice, results)
calculate_difficulty_dice(num_of_difficulty_dice, results)
calculate_proficiency_dice(num_of_proficiency_dice, results)
calculate_challenge_dice(num_of_challenge_dice, results)
calculate_force_dice(num_of_force_dice, results)

counted_results_dict = count_results(results, counted_results_dict)

cancelled_results_dict = cancel_out_results(counted_results_dict)

print(cancelled_results_dict)