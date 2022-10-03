#Parameters:
#   volts: integer or float representing the voltage rating of the component
#   component: {'winding', 'heater', None}, optional, default 'winding'
#   is_sr: bool, default True
def get_ir(volts, component='winding', is_sr=True):

    def get_test_volts(volts, component):

        if component == 'winding':
            if volts < 1000:
                tV = '500 V'
            elif volts in range(1000,2501):
                tV = '1000 V'
            elif volts in range(2501,5001):
                tV = '2500 V'
            elif volts >= 5001:
                tV = '5000 V'
        elif component == 'heater':
            tV = str(volts) + ' V'
        else:
            tV = '250 V'
            
        return tV

    def get_crit(component):

        if component == 'winding':
            aC = u'\u2265' + ' 100 M' + u'\u2126'
        else:
            aC = u'\u2265' + ' 1 M' + u'\u2126'

        return aC

    irT = {
        'SI#': '900',
        'Test': 'Insualtion Resistance\nat ' + get_test_volts(),
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
        

    
