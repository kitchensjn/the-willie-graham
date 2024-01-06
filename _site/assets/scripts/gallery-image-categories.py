file = open("../../_data/gallery-metadata.tsv", "r")
file.readline()

all_cats = []
for line in file:
    cats = line.replace("\n", "").split("\t")[-1].split(",")
    if cats[0] != "":
        all_cats.extend(cats)

print(list(set(all_cats)))
    