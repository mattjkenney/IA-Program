def get_endplay(is_sleeve_brg, hp_rating, speed-rating, is_sr=True):

    def get_crit(is_sleeve_brg, hp_rating, speed_rating):

        if not is_sleeve_brg:
            aC = 'N/A'
            r = 'N/A'
        elif is_sleeve_brg:
            if speed_rating > 1800:
                if (hp_rating >= 125) or (hp_rating <= 250):
                    aC = u'\u2265' + ' 0.25"'
                    r = ''
                elif (hp_rating >= 300) or (hp_rating <= 500):
                    aC = u'\u2265' + ' 0.50"'
                    r = ''
            elif speed_rating <= 1800:
                aC = u'\u2265' + ' 0.25"'
                r = ''
            
        return (aC, r)

    critR = get_crit()
    irT = {
        'SI#': '202',
        'Test': 'Shaft Endplay',
        'Acceptance\nCriteria': critR[0],
        'Data': '',
        'Results\n(SAT/UNSAT)': critR[1],
        'M&TE': '',
        'Tech.': '',
        'QA': ''
        }
        
    if not is_sr:
        irT.pop('QA')

    return irT
