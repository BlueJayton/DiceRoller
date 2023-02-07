
import random


num_of_boost_dice = 0
num_of_setback_dice = 0
num_of_ability_dice = 1
num_of_difficulty_dice = 3
num_of_proficiency_dice = 3
num_of_challenge_dice = 0
num_of_force_dice = 4
results = []
counted_results = []


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

def CountResults (results, counted_results):
    
    successes = 0
    advantages = 0
    triumphs = 0
    threats = 0
    failures = 0
    despairs = 0
    lights = 0
    darks = 0
    
    for word in results:
        if (word == "Success"):
            successes = successes + 1
        elif (word == "Advantage"):
            advantages = advantages + 1
        elif (word == "Triumph"):
            triumphs = triumphs + 1
        elif (word == "Threat"):
            threats = threats + 1
        elif (word == "Failure"):
            failures = failures + 1
        elif (word == "Despair"):
            despairs = despairs + 1
        elif (word == "Light"):
            lights = lights + 1
        elif (word == "Dark"):
            darks = darks + 1
            
    counted_results = [successes, advantages, triumphs, threats, failures, despairs, lights, darks]
    
    return counted_results

def display_to_terminal (counted_results):
    
    

calculate_boost_dice(num_of_boost_dice, results)
calculate_setback_dice(num_of_setback_dice, results)
calculate_ability_dice(num_of_ability_dice, results)
calculate_difficulty_dice(num_of_difficulty_dice, results)
calculate_proficiency_dice(num_of_proficiency_dice, results)
calculate_challenge_dice(num_of_challenge_dice, results)
calculate_force_dice(num_of_force_dice, results)

counted_results = CountResults(results, counted_results)

print(display_to_terminal(counted_results))