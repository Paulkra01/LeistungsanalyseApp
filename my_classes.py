import json
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)

    def put(self, first_name):
        url = "http://127.0.0.1:5000"
        
        data = {
            "first_name": self.first_name
        }

        data_json = json.dumps(data)

        response = requests.put(url, data=data_json)
        print(response.text)
        

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)


class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate, email):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.birthdate = birthdate
        self.email = email
        self.age = self.calc_age(self.birthdate)
        self.max_heartrate = self.estimate_max_hr(self.sex, self.age)

    
    def estimate_max_hr(self, sex, age):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
    def calc_age(self, birthdate):
        date = datetime.strptime(birthdate, '%d.%m.%Y').date()
        current_date = datetime.now()
        return relativedelta(current_date, date).years
    
    def update_email():
        pass