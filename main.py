def main():

    global mn
    global set_job
    global datetime
    global os
    global ts1
    global cjf
    global pk

    from menu import menu as mn
    from classJobForms import set_job
    import datetime
    import os
    import trainingSet1 as ts1
    import classJobForms as cjf
    import pickle as pk
    from speed_torque import create_report

    job = cjf.Job()
    ch = housekeeping(job)
    while ch != 'Exit':
        if ch == 'Create Job':
            job = set_job()
            save_job(job)
        elif ch == 'Select Job':
            job = select_job()
        elif ch == 'Edit Job':
            job = set_job(job)
            save_job(job)
        elif ch == 'Create I&A Documents':
            create_pgs(job)
        elif ch == 'Create Load Test Report':
            create_report(job)
        ch = housekeeping(job)
        
    exiting()

def housekeeping(job):
    
    msg_header = '''
WELCOME TO THE PE OPERATIONS SUITE
##################################

'''
    ops = ['Create Job',
           'Select Job',
           'Edit Job',
           'Create I&A Documents',
           'Create Load Test Report',
           'Exit']
    if job.sec_job_number == None:
        del ops[2:-1]

    print(msg_header)
    print('Current job: ' + str(job.sec_job_number))
    chI = mn(ops)
    ch = ops[chI]

    return ch

def create_pgs(job):

    #job = cjf.Job(**ts1.training_set())
    inc_pgs = job.write_inc_pgs()
    os.startfile(inc_pgs)
    
    return  

def exiting():
    
    msg_exit = '''
#########################################
AWESOME
_________________________________________
'''

    print(msg_exit)

    return

def select_job():

    job_dict_file = open(r'E:\ia_form_program\job_dict.pickle', 'rb')
    job_dict = pk.load(job_dict_file)
    if job_dict == {}:
        print('\nThere are no jobs yet available to select. ')
    else:
        
        keys = tuple(job_dict.keys())
        chI = mn(keys)
        ch = keys[chI]
        job = job_dict.get(ch)
    job_dict_file.close()

    return job

def save_job(job):

    job_dict_file = open(r'E:\ia_form_program\job_dict.pickle', 'rb')
    job_dict = pk.load(job_dict_file)
    try:
        job_dict.update({job.sec_job_number: job})
    except:
        job_dict[job.sec_job_number] = job
    job_dict_file.close()
    job_dict_file = open(r'E:\ia_form_program\job_dict.pickle', 'wb')
    pk.dump(job_dict, job_dict_file)
    job_dict_file.close()
    print('...job saved successfully! ')

    return
        

main()
    
