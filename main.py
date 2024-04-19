import my_functions as mf
import json
import my_classes as mc



if __name__ == "__main__":
    experiment_name = input("experiment name:")
    supervisor = input("supervisor:")
    date = input("date:")
    subject = input("subject:")

    first_name = input("first name:")
    last_name = input("last name:")
    sex = input("sex:")
    age = input("age:")

    experiment = mc.Experiment(experiment_name,supervisor,date,subject)
    person = mc.Person(first_name, last_name, sex, age)

    mc.Experiment.save(experiment, "experiment.json")
    mc.Person.save(person,"person.json")