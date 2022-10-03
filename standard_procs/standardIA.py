class S_IA():
    

    def __init__(
        self,
        is_sr,
        volt_r,
        shaft_dia,
        is_sleeve_brg,
        hp_rating,
        de_brg_size,
        de_brg_qty,
        ode_brg_size,
        ode_brg_qty,
        inc_e= None,
        inc_m=None,
        brg_housing_fit=None,
        brg_journal_fit=None,
        rotor_shaft_runouts=None,
        rotor_growl=None,
        rotor_bal=None,
        stator_cl=None,
        stator_ti=None,
        rotor_ti=None,
        visual_ins=None
        ):

        self.is_sr = is_sr
        self.volt_r = volt_r
        self.shaft_dia = shaft_dia
        self.is_sleeve_brg = is_sleeve_brg
        self.hp_rating = hp_rating
        
        self.de_brg_size = de_brg_size
        self.de_brg_qty = de_brg_qty
        self.ode_brg_size = ode_brg_size
        self.ode_brg_qty = ode_brg_qty
        
        self.brg_housing_fit = brg_housing_fit
        self.brg_journal_fit = brg_journal_fit
        self.rotor_shaft_runouts = rotor_shaft_runouts
        self.rotor_growl = rotor_growl
        self.rotor_bal = rotor_bal
        self.stator_cl = stator_cl
        self.stator_ti = stator_ti
        self.rotor_ti = rotor_ti
        self.visual_ins = visual_ins

    def get_inc_e(self):
        
        from IR_standard import get_ir
        from PI_standard import get_pi
        from WR_standard import get_wr

        tests = [
            get_ir(self.volt_r, is_sr= self.is_sr),
            get_pi(self.volt_r, is_sr= self.is_sr),
            get_wr(is_sr= self.is_sr)
            ]

        return tests

    def get_inc_m(self):
        from ShaftRunout_standard import get_shaft_runout
        from ShaftEndplay_standard import get_shaft_endplay
        from MotorWeight_standard import get_motor_weight

        tests = [
            get_shaft_runout(self.shaft_dia, is_sr= self.is_sr),
            get_shaft_endplay(self.is_sleeve_brg, self.hp_rating, is_sr= self.is_sr),
            get_motor_weight(is_sr= self.is_sr)
            ]

        return tests
            
            
            
            
        
