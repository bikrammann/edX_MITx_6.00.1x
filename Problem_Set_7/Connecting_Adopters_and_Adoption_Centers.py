def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    def gscore_key(x):
        return adopter.get_score(x)
    def gname_key(x):
        return x.get_name()
    s = sorted(list_of_adoption_centers, key=gname_key)
    return sorted(s, key=gscore_key, reverse=True)

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):

    def gscore_key(x):
        return x.get_score(adoption_center)
    def gname_key(x):
        return x.get_name()
    l1 = sorted(list_of_adopters, key=gname_key)
    l2 = sorted(l1, key=gscore_key, reverse=True)
    if n > len(l2): return l2
    return l2[:n + 1]
