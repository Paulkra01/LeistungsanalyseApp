import my_functions as mf
import my_classes as mc
import os


if __name__ == "__main__":
    experiment_name = input("experiment name: ")
    date = input("date: ")


    supervisor = mc.Supervisor(
        first_name=input("supervisor first name: "),
        last_name=input("supervisor last name: "))


    subject = mc.Subject(
        first_name=input("subject first name: "),
        last_name=input("subject last name: "),
        sex=input("subject sex: "),
        birthdate=input("subject birthdate (dd.mm.yyyy): "))


    experiment = mc.Experiment(experiment_name, date, f"{supervisor.first_name} {supervisor.last_name}", f"{subject.first_name} {subject.last_name}")

    if not os.path.exists("jsons"):
        os.makedirs("jsons")

    mc.Experiment.save(experiment, "jsons/experiment.json")
    mc.Subject.save(subject, "jsons/subject.json")
    mc.Supervisor.save(supervisor, "jsons/subject.json")