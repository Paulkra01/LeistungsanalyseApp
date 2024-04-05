import my_functions

experiment_name = input("experiment name:")
supervisor = input("supervisor:")
date = input("date:")
subject = input("subject:")

if __name__ == "__main__":
    print(my_functions.build_experiment(experiment_name,supervisor,date,subject))
