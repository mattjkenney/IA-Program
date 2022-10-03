def get_motor_weight(sr=True):

    irT = {
        'SI#': 'N/A',
        'Test': 'Motor Weight',
        'Acceptance\nCriteria': 'N/A',
        'Data': '',
        'Results\n(SAT/UNSAT)': 'N/A',
        'M&TE': '',
        'Tech.': '',
        'QA': ''
        }
        
    if not is_sr:
        irT.pop('QA')

    return irT
