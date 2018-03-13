class Hospital(object):
    def __init__(self, h_name, max_capacity):
        self.h_name = h_name
        self.max_capacity = max_capacity
        self.patients = []
    
    def display_info(self):
        print "*"*20
        print self.h_name
        print "Max Capacity: "+str(self.max_capacity)
        print "Current Patients: "+str(len(self.patients))+" patients"
        for val in range (0,len(self.patients)):
            self.patients[val].display()
        print "*"*20
    
    def admit(self, patient):
        if len(self.patients) == self.max_capacity:
            print "Hospital is at maximum capacity ("+str(len(self.patients))+"/"+str(self.max_capacity)+"). Admit failed."
        else:
            self.patients.append(patient)
            print "Hospital capacity: ("+str(len(self.patients))+"/"+str(self.max_capacity)+")"
        return self

class Patient(object):
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies

    def display(self):
        print "-"*20
        print "Patient Name: "+self.name
        print "Allergies: "+self.allergies
        print "-"*20

patient0 = Patient("Allie","peanut")
patient1 = Patient("Bob","none")
patient2 = Patient("Roger","none")

hospital0 = Hospital("University of California San Francisco Benioff Children's Hospital of Oakland",2)
hospital1 = Hospital("University of California San Francisco",2)

hospital0.admit(patient0).admit(patient1).display_info()

hospital0.admit(patient2)