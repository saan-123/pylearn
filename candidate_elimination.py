import csv
with open ('./Datasets/trainingexamples.csv') as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

    specific = data[0][:-1]
    general = [['?' for _ in specific] for _ in specific]

    for i in data:
        attr_values = i[:-1]
        outcome = i[-1]

        for j in range(len(specific)):
            if outcome == "Yes":
                if attr_values[j] != specific[j]:
                    specific[j] = '?'
                    general[j][j] = '?'
            elif outcome == "No":
                if attr_values[j] != specific[j]:
                    general[j][j] = specific [j]
                else:
                    general[j][j] = '?'

        print(f"Step {data.index(i)} of Candidate Elimination Algorithm")
        print(f"Specific Hypothesis: {specific} ")
        print (f"General Hypothesis: {general}")

    generalHypothesis = [list(filter(lambda x: x != '?', i)) for i in general]
    print(f"Final General Hypothesis: {specific}")
    print(f"Final General Hypothesis: {generalHypothesis}")