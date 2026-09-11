class person:
    def __init__(self,person_id,name,age,gender):
        self.person_id=person_id
        self.name=name
        self.age=age
        self.gender=gender

    def display_details(self):
        print('id;',self.person_id)    
        print('name:',self.name)
        print('age:',self.age)
        print('gender:',self.gender)

class doctor(person):
    def __init__(self, person_id, name, age, gender,specialization,consultation_fee):
        super().__init__(person_id, name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
    def calculate_charges(self):
        return self.consultation_fee
    def display_details(self):
        print('\n---doctor details---')
        super().display_details()
        print('specialization:',self.specialization)
        print('consultation_fee:',self.consultation_fee)

class patient(person):
    def __init__(self,person_id,name,age,gender,disease,tretment_details):
        super().__init__(person_id, name, age, gender)
        self.disease=disease
        self.treatment_details=tretment_details

    def get_disease(self):
        return self.__disease
    def get_treatment(self,treatment):
        return self.__treatment

    def display_details(self):
           print('\n---patient details---')
           super().display_details()
           print('disease:',self.disease)
           print('treatment:',self.treatment_details)   
d1=doctor('a101','durai',30,'male','cardiologist',4000)
d2=doctor('b102','mahes',40,'female','neurologist',5000)
d3=doctor('c103','kavi',40,'female','dermalogist',6000)


p1=patient('d1','kavi',19,'female','fever','tablets')
p2=patient('d2','priya',20,'female','bp','medcins')
p3=patient('d3','siva',19,'male','fever','tablets')
p4=patient('d4','karthi',29,'male','cold','tablets')
p5=patient('d5','vineethi',21,'male','headche','tablets')


d1.display_details()
d2.display_details()
d3.display_details()

p1.display_details()
p2.display_details()
p3.display_details()
p4.display_details()
p5.display_details()

print('\nconsultaion charge:',d1.calculate_charges())