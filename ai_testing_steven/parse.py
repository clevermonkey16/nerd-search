import csv, re, json

one = {}
two = {}
three = {}
# count = 3909
with open('DataScientist.csv', encoding='utf8', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    count = 0
    for row in reader:
        if i==0:
            i += 1
            continue
        count += 1
        tokens = re.split(r'[,.\" !?><\-=+@#$/%^&*()\s\\:;{}\[\]~`•]', string=row[4])
        freq = {}
        for s in tokens:
            s = s.lower()
            if len(s) < 1: continue
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        for key, value in freq.items():
            # if value <= 1: continue
            if key in one:
                one[key] += value
            else:
                one[key] = value
    topop = []
    for key in one:
        if one[key] <= 10:
            topop.append(key)
    for elem in topop:
        one.pop(elem)
    # print(one)
    sorted_one = sorted(one.items(), key=lambda x:x[1])
    print(sorted_one)
    print("size:", len(one))
    print("count:", count)

    with open("ds.json", "w") as outfile:
        json.dump(one, outfile)



