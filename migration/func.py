import psycopg2
import csv
import random
import time

def copy_to_db():
    pass

def random_code(l):
    n = []
    for i in range(l):
        n.append(str(random.randint(0, 9)))

    return ''.join(n)

def generate_log(elapsed_time, end_time):
    filename = f"result{random_code(5)}.log"
    f = open(filename, 'w')
    f.write(f"Migration duration: {elapsed_time}s at {end_time}")
    f.close()

def write_csv(csv_file, fields, data):

    writer = csv.DictWriter(csv_file, fieldnames=fields)

    writer.writeheader()

    writer.writerows(data)

def binary_search_recursive(lst, target):
    if len(lst) == 0:
        return None
    else:
        guess = (len(lst) - 1) // 2

        if target == lst[guess][0]:
            return lst[guess][1]
        if target < lst[guess][0]:
            return binary_search_recursive(lst[:guess], target)
        elif target > lst[guess][0]:
            return binary_search_recursive(lst[guess+1:], target)

def search_relation(buid, profiles):

    profile_id = binary_search_recursive(profiles, buid)

    return profile_id

def sort_profiles(profiles_collection):

    # Make profiles list
    profiles = []

    for profile in profiles_collection:
        buids = profile.get('buids', None)

        if buids != None:
            for buid in buids:
                # Fill profiles list
                profiles.append(
                    (str(buid), profile.get('_id')),
                )

    profiles.sort()
    # print(len(profiles))

    return profiles
