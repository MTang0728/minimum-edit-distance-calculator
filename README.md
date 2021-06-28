# minimum-edit-distance-calculator

This repo contains a simple script that calculates the minimum edit distance between two sequences using dynamic programming.

With the Levenshtein distance metric, Insertion and Deletion each has a cost of 1, and Substitution has a cost of 2.

To run the script, enter the source sequence followed by the target sequence:

`python3 calculator.py source_sequence target_sequence`

for example, to calculate the minimum edit distance between *michael* and *michelle*:

`python3 calculator.py michael michelle`

which yields a distance of 3.
