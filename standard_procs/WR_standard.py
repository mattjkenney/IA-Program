def get_wr(is_dedication=False, winding_type= None, is_sr=True):

    def get_crit(is_dedication):

        if not is_dedication:

            aC = u'\u2264' + ' 5.0%'

        elif is_dedication:
            if winding_type == 'concentric':
                aC = u'\u2264' + ' 2.0%'
            elif winding_type == 'lap':
                aC = u'\u2264' + ' 0.5%'
            
        return aC

    irT = {
        'SI#': '903',
        'Test': 'Winding\nResistance',
        'Acceptance\nCriteria': get_crit(),
        'Data': '1-2:\n1-3:\n2-3:',
        'Results\n(SAT/UNSAT)': '',
        'M&TE': '',
        'Tech.': '',
        'QA': ''
        }
        
    if not is_sr:
        irT.pop('QA')

    return irT
