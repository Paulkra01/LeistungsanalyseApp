import my_functions
import json

experiment_name = input("experiment name:")
supervisor = input("supervisor:")
date = input("date:")
subject = input("subject:")

if __name__ == "__main__":
    experiment = my_functions.build_experiment(experiment_name,supervisor,date,subject)
    print(experiment)

# Convert and write JSON object to file
with open("sample.json", "a") as outfile: 
    json.dump(experiment, outfile)
