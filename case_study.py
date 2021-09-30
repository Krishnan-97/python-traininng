import case_study_Exception
from case_study_Exception import *

class Employee:
    def __init__(self,emp_id,emp_name,join_date,mgr_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.join_date = join_date
        self.mgr_id = mgr_id

    def display(self):
        print("Employee Id:",self.emp_id," Employee Name:",self.emp_name)


class Timesheet:
    def __init__(self,ts_id,emp_id,mgr_id,act,date,hrs,status,mgr_cmmt):
        self.ts_id = ts_id
        self.emp_id = emp_id
        self.mgr_id = mgr_id
        self.act = act
        self.date = date
        self.hrs = hrs
        self.status = status
        self.mgr_cmmt = mgr_cmmt

    def display(self):
        if(self.hrs < 40):
            raise case_study_Exception.LessThan40Error()
        else:
            print("Timesheet Id:", self.ts_id, "Timesheet Activity:", self.act)

e = Employee(155,"Krishnan","1/1/2021",80)
e.display()

t = Timesheet(1,55,12,"Testing","23/05/2020",48,"completed","accurate results")
t.display()

t = Timesheet(3,38,8,"UI Creation","12/03/2020",24," not completed","not inspected")
t.display()

