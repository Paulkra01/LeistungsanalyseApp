import my_functions as mf
import json
import my_classes as mc



if __name__ == "__main__":
    experiment_name = input("experiment name:")
    date = input("date:")
    subject = input("subject:")
    supervisor = input("supervisor:")

    first_name = input("first name:")
    last_name = input("last name:")
    sex = input("sex:")
    birthdate = (input("birthdate (d.m.y):"))

    experiment = mc.Experiment(experiment_name, date, supervisor, subject)
    person = mc.Person(first_name, last_name, sex, birthdate)

    mc.Experiment.save(experiment, "experiment.json")
    mc.Person.save(person,"person.json")