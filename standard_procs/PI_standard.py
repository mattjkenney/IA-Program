#Parameters:
#   volts: integer or float representing the voltage rating of the winding
#   winding: {'new', 'used'}, default 'used'
#   is_sr: bool, default True
def get_pi(volts, winding='used', is_sr=True):

    def get_test_volts(volts):

        if volts < 1000:
            tV = '500 V'
        elif volts in range(1000,2501):
            tV = '1000 V'
        elif volts in range(2501,5001):
            tV = '2500 V'
        elif volts >= 5001:
            tV = '5000 V'
            
        return tV

    def get_crit(winding):

        if winding == 'used':
            aC = u'\u2265' + ' 1.5'
        elif winding == 'new':
            aC = u'\u2265' + ' 2.0'

        return aC

    irT = {
        'SI#': '901',
        'Test': 'PI\nat ' + get_test_volts(),
        'Acceptance\nCriteria': get_crit(),
        'Data': '1 min:\n10 min:\nPI=',
        'Results\n(SAT/UNSAT)': '',
        'M&TE': '',
        'Tech.': '',
        'QA': ''
        }
        
    if not is_sr:
        irT.pop('QA')

    return irT
