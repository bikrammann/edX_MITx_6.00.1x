def count_occurrence(s):
    count = 0
    pos = s.find("bob")
    while pos != -1:
        count += 1
        pos = s.find("bob", pos+1)
    print("Number of times bob occurs is: {}".format(count))

count_occurrence(s)