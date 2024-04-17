import csv, re, json

one = {}
# count = 22000
with open('monster_com-job_sample.csv', encoding='utf8', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    count = 0
    for row in reader:
        if i==0:
            i += 1
            continue
        count += 1
        tokens = re.split(r'[,.\" !?><\-=+@#$/%^&*()\s\\:;{}\[\]~`•]', string=row[5])
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

    with open("jobs.json", "w") as outfile:
        json.dump(one, outfile)

"""
approach:
currently have a frequency table of words
- stats based upon number of times only in documents where it appears
- compare vs regular dataset, find words with negative/positive correlations
- remove those with close to neutral correlation, check only those with positive/negative correlation


"""


