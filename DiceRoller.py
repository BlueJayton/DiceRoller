
import random


num_of_boost_dice = 0
num_of_setback_dice = 0
num_of_ability_dice = 0
num_of_difficulty_dice = 0
num_of_proficiency_dice = 0
num_of_challenge_dice = 0
num_of_force_dice = 0
results = []


#def GetDiceCounts (dicecount):
        

def CalculateBoostDice (num_of_boost_dice, results):
    if num_of_boost_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in num_of_boost_dice:
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

def CalculateSetbackDice (num_of_setback_dice, results):
    if num_of_setback_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6]
    for die in num_of_setback_dice:
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

def CalculateAbilityDice (num_of_ability_dice, results):
    if num_of_ability_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in num_of_ability_dice:
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

def CalculateDifficultyDice (num_of_difficulty_dice, results):
    if num_of_difficulty_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8]
    for die in num_of_difficulty_dice:
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

def CalculateProficiencyDice (num_of_proficiency_dice, results):
    if num_of_proficiency_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in num_of_proficiency_dice:
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

def CalculateChallengeDice (num_of_challenge_dice, results):
    if num_of_challenge_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in num_of_challenge_dice:
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

def CalculateForceDice (num_of_force_dice, results):
    if num_of_force_dice == 0:
        return
    
    num_of_faces = [1,2,3,4,5,6,7,8,9,10,11,12]
    for die in num_of_force_dice:
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