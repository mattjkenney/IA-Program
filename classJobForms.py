class Job():
    global datetime
    global os
    global mn
    global MailMerge
    
    import datetime
    import os
    from menu import menu as mn
    from mailmerge import MailMerge

    def __init__(
        self,
        customer_name=None,
        purchase_order=None,
        line_item=None,
        po_revision=None,
        po_date=None,
        delivery_date=None,
        sale_price=None,
        work_description=None,
        unit_description=None,
        is_to_rewind=False,
        is_to_overhaul=True,
        is_to_supply_new_part=False,
        is_for_mov_motor=False,
        is_for_generator=False,
        is_for_motor=True,
        is_foot_mounted=False,
        is_ac=True,
        is_dc=False,
        is_sr=True,
        is_eq=False,
        is_aq=False,
        is_epri=False,
        is_rush=False,
        po_file=None,
        quote_file=None,
        unique_id=None,
        customer_spec=None,
        sec_job_number=None,
        epicor_job_number=None,
        ratings=None):

        self.customer_name = customer_name
        self.purchase_order = purchase_order
        self.line_item = line_item
        self.po_revision = po_revision
        self.po_date = po_date
        self.delivery_date = delivery_date
        self.sale_price = sale_price
        self.work_description = work_description
        self.unit_description = unit_description
        self.is_to_rewind = is_to_rewind
        self.is_to_overhaul = is_to_overhaul
        self.is_to_supply_new_part = is_to_supply_new_part
        self.is_for_mov_motor = is_for_mov_motor
        self.is_for_generator = is_for_generator
        self.is_for_motor = is_for_motor
        self.is_foot_mounted = is_foot_mounted
        self.is_ac= is_ac
        self.is_dc= is_dc
        self.is_sr = is_sr
        self.is_eq = is_eq
        self.is_aq = is_aq
        self.is_epri = is_epri
        self.is_rush = is_rush
        self.po_file = po_file
        self.quote_file = quote_file
        self.unique_id = unique_id
        self.customer_spec = customer_spec
        self.sec_job_number = sec_job_number
        self.epicor_job_number = epicor_job_number
        self.ratings = ratings

    def as_dict(self):

        this_dict = {
            'customer_name': self.customer_name,
            'purchase_order': self.purchase_order,
            'line_item': self.line_item,
            'po_revision': self.po_revision,
            'po_date': self.po_date,
            'delivery_date': self.delivery_date,
            'sale_price': self.sale_price,
            'work_description': self.work_description,
            'unit_description': self.unit_description,
            'is_to_rewind': self.is_to_rewind,
            'is_to_overhaul': self.is_to_overhaul,
            'is_to_supply_new_part': self.is_to_supply_new_part,
            'is_for_mov_motor': self.is_for_mov_motor,
            'is_for_generator': self.is_for_generator,
            'is_for_motor': self.is_for_motor,
            'is_foot_mounted': self.is_foot_mounted,
            'is_ac': self.is_ac,
            'is_dc': self.is_dc,
            'is_sr': self.is_sr,
            'is_eq': self.is_eq,
            'is_aq': self.is_aq,
            'is_epri': self.is_epri,
            'is_rush': self.is_rush,
            'po_file': self.po_file,
            'quote_file': self.quote_file,
            'unique_id': self.unique_id,
            'customer_spec': self.customer_spec,
            'sec_job_number': self.sec_job_number,
            'epicor_job_number': self.epicor_job_number,
            'ratings': self.ratings
            }
        return this_dict

    def edit_rating(self, ratings=None):

        def is_motor_type(parm, kind):
            if (self.is_for_motor == False) and (self.is_for_generator == False):
                n = 'na'
            elif kind == float:
                n = set_float(parm)
            elif kind == str:
                n = set_str(parm)
            elif kind == int:
                n = set_int(parm)
            return n

        if ratings == None:
            rat_dict = {}
            t = list(range(21))
        else:
            rat_dict = self.ratings
            print('\nChoose a rating to edit. ')
            ops = [str(i) for i in rat_dict.items()]
            chI = mn(ops)
            ch = list(rat_dict.items())[chI][0]
            t = [chI]
        
        ratings = {
            'oem': rat_dict.get('oem') if 0 not in t else set_str('oem'),
            'mod': rat_dict.get('mod') if 1 not in t else set_str('mod'),
            'hp': rat_dict.get('hp') if 2 not in t else is_motor_type('hp', float),
            'kW': rat_dict.get('kW') if 3 not in t else is_motor_type('kW', float),
            'voltage': rat_dict.get('voltage') if 4 not in t else is_motor_type('voltage', float),
            'amps': rat_dict.get('amps') if 5 not in t else is_motor_type('amps', float),
            'rpm': rat_dict.get('rpm') if 6 not in t else is_motor_type('rpm', int),
            'phase': rat_dict.get('phase') if 7 not in t else is_motor_type('phase', int),
            'freq': rat_dict.get('freq') if 8 not in t else is_motor_type('frequency', int),
            'design': rat_dict.get('design') if 9 not in t else is_motor_type('NEMA Design', str),
            'kva': rat_dict.get('kva') if 10 not in t else is_motor_type('KVA Code', str),
            'sf': rat_dict.get('sf') if 11 not in t else is_motor_type('service factor', float),
            'ins_cl': rat_dict.get('ins_cl') if 12 not in t else is_motor_type('insulation class', str),
            'amb': rat_dict.get('amb') if 13 not in t else is_motor_type('ambient', float),
            'frame': rat_dict.get('frame') if 14 not in t else is_motor_type('frame designation', str),
            'style': rat_dict.get('style') if 15 not in t else is_motor_type('style', str),
            'type': rat_dict.get('type') if 16 not in t else is_motor_type('type', str),
            'duty': rat_dict.get('duty') if 17 not in t else is_motor_type('duty cycle', str),
            'cfit_shaft_diameter': rat_dict.get('cfit_shaft_diameter') if 18 not in t else is_motor_type('coupling fit shaft diameter (shaft extension diameter)', float),
            'de_brg_size': rat_dict.get('de_brg_size') if 19 not in t else is_motor_type('drive end bearing size', str),
            'ode_brg_size': rat_dict.get('ode_brg_size') if 20 not in t else is_motor_type('opposite drive end bearing size', str),
                }
        self.ratings = ratings
        
        return ratings

    def write_first_page(self):

        template_1 = 'pg_1_templatev2.docx'
        pg_1 = 'pg_1_new.docx'

        pg_1_header = {
            'po': self.purchase_order,
            'li': self.line_item,
            'po_rev': self.po_revision,
            'del_date': str(self.delivery_date),
            'sjn': self.sec_job_number,
            'cust': self.customer_name,
            'wd': self.work_description,
            'ejn': self.epicor_job_number,
            'uid': self.unique_id,
            'udes': self.unit_description
            }

        rat_dict = dictVals_str([self.ratings])[0]

        doc_1 = MailMerge(template_1)
        doc_1.merge(**pg_1_header)
        doc_1.merge(**rat_dict)
        doc_1.write(pg_1)

        return pg_1

    def write_incoming_electrical_form(self, pg_1):

        from docx import Document
        pg_inc_electrical = 'pg_inc_electrical.docx'
        tests = Test(ratings=self.ratings,
                     customer_spec=self.customer_spec,
                     is_sr=self.is_sr)

        strs = dictVals_str([tests.ir, tests.pi, tests.surge, tests.hi_pot])
        
        #electricals = [i for i in strs]
            
        doc = Document(pg_1)
        header = ['SI',
                  'Test',
                  'Acceptance\nCriteria',
                  'Data',
                  'Results\n(Sat/UnSat)',
                  'M&TE',
                  'Tech.',
                  'QA']
        if not self.is_sr:
            header.pop(-1)

        ttable = doc.add_table(len(strs) + 1, len(header), style='Table Grid')
        for i in range(len(header)):
            ttable.cell(0,i).text = header[i]
        
        for i in range(len(strs)):
            n = i + 1
            test = strs[i]
            keys = list(test.keys())
            for j in range(len(keys)):
                ttable.cell(n, j).text = test.get(keys[j])

        doc.save(pg_inc_electrical)

        return pg_inc_electrical

    def write_inc_pgs(self):

        pg_1 = self.write_first_page()
        inc_pgs = self.write_incoming_electrical_form(pg_1)
        return inc_pgs
        

class Test(Job):

    def __init__(self,
                 ratings,
                 customer_spec,
                 is_sr,
                 ir=None,
                 pi=None,
                 wr=None,
                 surge=None,
                 hi_pot=None,
                 core_loss=None,
                 shaft_runout=None,
                 de_bearing_journal_runout=None,
                 ode_bearing_journal_runout=None,
                 flange_flatness=None,
                 rabbet_runout=None,
                 de_bearing_housing_id=None,
                 ode_bearing_housing_id=None,
                 de_shaft_od=None,
                 ode_shaft_od=None):
        
        self.ratings = ratings
        self.customer_spec = customer_spec
        self.is_sr = is_sr
        self.ir = ir
        self.pi = pi
        self.wr = wr
        self.surge = surge
        self.hi_pot = hi_pot
        self.core_loss = core_loss
        self.shaft_runout = shaft_runout
        self.flange_flatness = flange_flatness
        self.rabbet_runout = rabbet_runout
        self.de_bearing_housing_id = de_bearing_housing_id
        self.ode_bearing_housing_id = ode_bearing_housing_id
        self.de_shaft_od = de_shaft_od
        self.ode_shaft_od = ode_shaft_od

    @property
    def ir(self):
        return self._ir

    @ir.setter
    def ir(self, ir):
        
        if ir == None:
            volts = self.ratings.get('voltage')
            if volts <= 1000:
                ir = {
                    'SI': '901\n(rev. 5)',
                    'Test': 'Insulation Resistance\n(500 V for 1 min)',
                    'AC': u'\u2265' + ' 1 M-ohm',
                    'Data': '',
                    'Results': '',
                    'M&TE': '',
                    'Tech.' : '',
                    'QA': ''
                    }
            if not self.is_sr:
                ir.remove('QA')
                
        self._ir = ir
                    
                 
    @property
    def pi(self):
        return self._pi

    @pi.setter
    def pi(self, pi):

        if pi == None:
            volts = self.ratings.get('voltage')
            if volts <= 1000:
                pi = {
                    'SI': '902\n(rev. 5)',
                    'Test': 'Polarization Index',
                    'AC': '<= 2',
                    'Data': '1 min:\n10 min:',
                    'Results': '',
                    'M&TE': '',
                    'Tech.' : '',
                    'QA': ''
                    }
            if not self.is_sr:
                pi.remove('QA')

        self._pi = pi

    @property
    def wr(self):
        return self._wr

    @wr.setter
    def wr(self, wr):

        if wr == None:
            wr = {
                'SI': '903\n(rev. 5)',
                'Test': 'Winding Resistance',
                'AC': '<= 5.0%',
                'Data': '1-2:\n1-3:\n2-3:',
                'Results': 'Sat / UnSat',
                'M&TE': '',
                'Tech.': '',
                'QA': ''
                }
        if not self.is_sr:
            wr.remove('QA')

        self._wr = wr

    @property
    def surge(self):
        return self._surge

    @surge.setter
    def surge(self, surge):

        if surge == None:
            volts = self.ratings.get('voltage')
            surge = {
                'SI': '904\n(rev. 5)',
                'Test': 'Surge\n' + '(' + str(volts * 2 + 1000) + ' V)',
                'AC': 'Acceptable Pattern per SI',
                'Data': '',
                'Results': '',
                'M&TE': '',
                'Tech.': '',
                'QA': ''
                }

        if not self.is_sr:
            surge.remove('QA')

        self._surge = surge

    @property
    def hi_pot(self):
        return self._hi_pot

    @hi_pot.setter
    def hi_pot(self, hi_pot):

        if hi_pot == None:
            volts = self.ratings.get('voltage')
            tv = (volts * 2 + 1000) * 1.7
            hi_pot = {
                'SI': '904\n(rev. 5)',
                'Test': 'High Potential Test\n' + '(' + str(tv) + ' V)',
                'AC': 'No failure',
                'Data': '',
                'Results': '',
                'M&TE': '',
                'Tech.' : '',
                'QA': ''
                }

        if not self.is_sr:
            surge.remove('QA')

        self._hi_pot = hi_pot

def set_job(job=None):

    if job == None:
        job = Job()
        t = list(range(30))
    else:
        print('\nChoose a parameter to edit. ')
        t = [mn(list(job.as_dict().keys()))]
        
    parms = {
        'customer_name': job.customer_name if 0 not in t else set_str("customer's name"),
        'purchase_order': job.purchase_order if 1 not in t else set_str('purchase order'),
        'line_item': job.line_item if 2 not in t else set_str('line item'),
        'po_revision': job.po_revision if 3 not in t else set_str('po revision'),
        'po_date': job.po_date if 4 not in t else set_date('po issue date'),
        'delivery_date': job.delivery_date if 5 not in t else set_date('delivery date'),
        'sale_price': job.sale_price if 6 not in t else set_float('sales price'),
        'work_description': job.work_description if 7 not in t else set_str('work description'),
        'unit_description': job.unit_description if 8 not in t else set_str('unit description'),
        'is_to_rewind': job.is_to_rewind if 9 not in t else set_boolean('for a rewind'),
        'is_to_overhaul': job.is_to_overhaul if 10 not in t else set_boolean('for an overhaul'),
        'is_to_supply_new_part': job.is_to_supply_new_part if 11 not in t else set_boolean('for a new part'),
        'is_for_mov_motor': job.is_for_mov_motor if 12 not in t else set_boolean('for a mov motor'),
        'is_for_generator': job.is_for_generator if 13 not in t else set_boolean('for a generator'),
        'is_for_motor': job.is_for_motor if 14 not in t else set_boolean('for a motor'),
        'is_foot_mounted': job.is_foot_mounted if 15 not in t else set_boolean('for a foot mounted unit'),
        'is_ac': job.is_ac if 16 not in t else set_boolean('for an ac powered unit'),
        'is_dc': job.is_dc if 17 not in t else set_boolean('for a dc powered unit'),
        'is_sr': job.is_sr if 18 not in t else set_boolean('for a Safety Related unit'),
        'is_eq': job.is_eq if 19 not in t else set_boolean('for an Eqvironmental Qualified unit'),
        'is_aq': job.is_aq if 20 not in t else set_boolean('for an Augmented Quality unit'),
        'is_epri': job.is_epri if 21 not in t else set_boolean('for an EQ-EPRI Qualified unit'),
        'is_rush': job.is_rush if 22 not in t else set_boolean('for a RUSH job'),
        'po_file': job.po_file if 23 not in t else set_file('po file'),
        'quote_file': job.quote_file if 24 not in t else set_file('guote file'),
        'unique_id': job.unique_id if 25 not in t else set_str('unique identifier'),
        'customer_spec': job.customer_spec if 26 not in t else set_str('customer specification'),
        'sec_job_number': job.sec_job_number if 27 not in t else set_str('Schule Electric Job Number'),
        'epicor_job_number': job.epicor_job_number if 28 not in t else set_str('EPICOR job number'),
        'ratings': job.ratings if 29 not in t else job.edit_rating()
        }
    
    job = Job(**parms)
        
    return job
    

def set_date(this_date):
    # dependency : import datetime
    
    flag = False
    while flag == False:
        y = input('\nFor the ' + this_date + ', enter the year: ')
        m = input('\nFor the ' + this_date + ', enter the month: ')
        d = input('\nFor the ' + this_date + ', enter the day: ')
        try:
            y = int(y)
            m = int(m)
            d = int(d)
        except:
            print('\nEnter whole numbers only.')
        else:
            flag = True
            date = datetime.date(year= y, month= m, day= d)

    return date

def set_boolean(this_bool):

    flag = False
    while flag == False:
        b = input('\n' + this_bool + '?\nEnter " t " for True, or " f " ' +\
                  'for False: ')
        if b == 't':
            flag = True
            n = True
        elif b == 'f':
            flag = True
            n = False
        else:
            print('\nEnter only " t " or " f ". ')

    return n

def set_file(this_file):
    # dependency : import os
    flag = False
    while flag == False:
        f = input('\nTo skip, hit enter...\nOtherwise, enter the filepath' +\
                  ' for the ' + this_file + ': ')
        if f == '':
            flag = True
            n = None
        elif os.path.isfile(f):
            flag = True
            print('filepath is valid!')
        else:
            print('\nThe entered filepath does not exist.')

    return f

def set_float(this_float):

    msg = 'Enter the ' + this_float + ': '
    
    flag = False
    while flag == False:
        print('\nEnter only numbers. ')
        d = input(msg.rjust(30, ' '))
        try:
            d = float(d)
        except:
            pass
        else:
            flag = True

    return d

def set_str(name):
    msg = 'Enter the ' + name + ': '
    print('\n')
    n = input(msg.rjust(30,' '))

    return n

def set_int(name):
    msg = 'Enter the ' + name + ': '
    
    flag = False
    while flag == False:
        print('\nEnter only numbers. ')
        d = input(msg.rjust(30, ' '))
        try:
            d = int(d)
        except:
            pass
        else:
            flag = True

def dictVals_str(these_dicts):
    #these_dicts must be a list of dictionaries

    new_dicts = []
    for i in range(len(these_dicts)):
        this_dict = {}
        for j in list(these_dicts[i].keys()):
            this_dict[j] = str(these_dicts[i].get(j))
        new_dicts.append(this_dict)
     
    return new_dicts
    
    

