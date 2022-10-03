def get_shaft_runout(shaft_dia=None, is_sr=True):

    def get_crit(shaft_dia):

        if (shaft_dia >= 0.1875) or (shaft_dia <= 1.625) or (shaft_dia == None):
            aC = u'\u2264' + ' 0.002"'
        elif shaft_dia > 1.625:
            aC = u'\u2264' + ' 0.003"'
            
        return aC

    irT = {
        'SI#': '401',
        'Test': 'Shaft Runout',
        'Acceptance\nCriteria': get_crit(),
        'Data': '',
        'Results\n(SAT/UNSAT)': '',
        'M&TE': '',
        'Tech.': '',
        'QA': ''
        }
        
    if not is_sr:
        irT.pop('QA')

    return irT
