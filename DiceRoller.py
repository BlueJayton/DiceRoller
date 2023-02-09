
import random


boost = 10
setback = 10
ability = 10
difficulty = 10
proficiency = 10
challenge = 10
force = 10
results = []
counted_results_dict = {"Successes" : 0, "Failures" : 0,
                        "Advantages" : 0, "Threats" : 0,
                        "Triumphs" : 0, "Despairs" : 0,
                        "Lights" : 0, "Darks" : 0}


#def GetDiceCounts (dicecount):
        

def calculate_boost_dice (boost, results):
    if boost == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(boost):
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

def calculate_setback_dice (setback, results):
    if setback == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in range(setback):
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

def calculate_ability_dice (ability, results):
    if ability == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(ability):
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

def calculate_difficulty_dice (difficulty, results):
    if difficulty == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in range(difficulty):
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

def calculate_proficiency_dice (proficiency, results):
    if proficiency == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(proficiency):
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

def calculate_challenge_dice (challenge, results):
    if challenge == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(challenge):
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

def calculate_force_dice (force, results):
    if force == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in range(force):
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

def reset (dice):
    dice = 0
    
    return


     

#Function Calls
calculate_boost_dice(boost, results)
calculate_setback_dice(setback, results)
calculate_ability_dice(ability, results)
calculate_difficulty_dice(difficulty, results)
calculate_proficiency_dice(proficiency, results)
calculate_challenge_dice(challenge, results)
calculate_force_dice(force, results)

counted_results_dict = count_results(results, counted_results_dict)

cancelled_results_dict = cancel_out_results(counted_results_dict)

print(display_formatted_results(cancelled_results_dict))