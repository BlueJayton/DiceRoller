def cancel_out_results (cancel_results_dict):
    
    #Cancel successes and failures out
    if (cancel_results_dict['Successes'] == cancel_results_dict['Failures']):
        cancel_results_dict['Successes'] = 0
        cancel_results_dict['Failures'] = 0
    elif (cancel_results_dict['Successes'] > cancel_results_dict['Failures']):
        cancel_results_dict['Successes'] = cancel_results_dict['Successes'] - cancel_results_dict['Failures']
        cancel_results_dict['Failures'] = 0
    elif (cancel_results_dict['Failures'] > cancel_results_dict['Successes']):
        cancel_results_dict['Failures'] = cancel_results_dict['Failures'] - cancel_results_dict['Successes']
        cancel_results_dict['Successes'] = 0
        
    #Cancel advantages and threats out
    if (cancel_results_dict['Advantages'] == cancel_results_dict['Threats']):
        cancel_results_dict['Advantages'] = 0
        cancel_results_dict['Threats'] = 0
    elif (cancel_results_dict['Advantages'] > cancel_results_dict['Threats']):
        cancel_results_dict['Advantages'] = cancel_results_dict['Advantages'] - cancel_results_dict['Threats']
        cancel_results_dict['Threats'] = cancel_results_dict['Threats'] - cancel_results_dict['Threats']
    elif (cancel_results_dict['Threats'] > cancel_results_dict['Advantages']):
        cancel_results_dict['Threats'] = cancel_results_dict['Threats'] - cancel_results_dict['Advantages']
        cancel_results_dict['Advantages'] = cancel_results_dict['Advantages'] - cancel_results_dict['Advantages']
        
    return cancel_results_dict

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