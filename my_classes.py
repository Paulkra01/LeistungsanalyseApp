import json

class Person():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_heartrate = self.estimate_max_hr(self.sex, self.age)

    def save(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)

    def estimate_max_hr(self, sex, age):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

        


class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)