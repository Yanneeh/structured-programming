from pymongo import MongoClient
import psycopg2
import csv
import time
from multiprocessing import Process
from func import *

def migrate_sessions(sessions_collection, profiles_collection, start=0, stop=100):

    sessions = []
    orders = []

    for i in range(start, stop):
        profile_id = search_relation(sessions_collection[i]['buid'][0], profiles)

        session_id = sessions_collection[i]['_id']

        # insert session
        sessions.append({
            'id': session_id,
            'profile_id': profile_id,
            'session_start': sessions_collection[i]['session_start'],
            'session_end': sessions_collection[i]['session_end'],
            'browser_name': sessions_collection[i]['browser']['family'],
            'os_name': sessions_collection[i]['user_agent']['os']['family'],
            'is_mobile_flag': sessions_collection[i]['user_agent']['flags']['is_mobile'],
            'is_tablet_flag': sessions_collection[i]['user_agent']['flags']['is_tablet'],
            'is_email_flag': sessions_collection[i]['user_agent']['flags']['is_email_client'],
            'device_family': sessions_collection[i]['user_agent']['device']['family'],
        })

        # Migrate orders
        if sessions_collection[i].get('order'):
            for product_id in sessions_collection[i]['order']['profucts']:
                orders.append({
                    'session_id': session_id,
                    'product_id': str(product_id)
                })

    orders_file = open('orders.csv', 'w')

    fields = ['session_id', 'product_id']

    # Write data to csv
    write_csv(orders_file, fields, orders)

    sessions_file = open('sessions.csv', 'w')

    fields = ['id', 'profile_id', 'session_start', 'session_end', 'browser_name', 'os_name', 'is_mobile_flag', 'is_tablet_flag', 'is_email_flag', 'device_family']

    # Write data to csv
    write_csv(sessions_file, fields, sessions)

def migrate_profiles(profiles_collection):
    profiles = []
    products = []

    for profile in profiles_collection:
        if profile.get('order'):
            profiles.append({
                'id': profile.get('_id'),
                'first_order': profile['order'].get('first'),
                'last_order': profile['order'].get('latest'),
                'order_amount': profile['order'].get('count')
            })
        else:
            profiles.append({
                'id': profile.get('_id'),
                'first_order': None,
                'last_order': None,
                'order_amount': None
            })

        if profiles.get('previously_recommended'):
            for product in profiles['previously_recommended']:
                products.append({
                    'product_id': str(product),
                    'profile_id': profile.get('_id')
                })

    recommended_file = open('recommended.csv', 'w')

    fields = ['product_id', 'profile_id']

    # Write data to csv
    write_csv(recommended_file, fields, products)

    profiles_file = open('profiles.csv', 'w')

    fields = ['id', 'first_order', 'last_order', 'order_amount']

    # Write data to csv
    write_csv(profiles_file, fields, profiles)

def migrate_products(product_collection):

    products = []

    for product in product_collection:
        if product.get('properties'):
            pass
        if product.get('price'):
            pass
        else:
            products.append({
                'id': product.get('_id'),
                'name': product.get('name'),
                'description',
                'brand',
                'price',
                'discount',
                'stock',
                'category',
                'sub_category',
                'sub_sub_category',
                'sub_sub_sub_category',
                'recommendable',
                'online_online',
                'target_demographic',
                'gender',
                'color',
                'unit',
                'odor_type',
                'series',
                'kind',
                'variant',
                'type',
                'type_of_hair_care',
                'type_of_hair_coloring'
            })


    profiles_file = open('profiles.csv', 'w')

    fields = [
                'id', 'name', 'description', 'brand',
                'price', 'discount', 'stock', 'category',
                'sub_category', 'sub_sub_category', 'sub_sub_sub_category',
                'recommendable', 'online_online', 'target_demographic', 'gender',
                'color', 'unit', 'odor_type', 'series', 'kind', 'variant', 'type',
                'type_of_hair_care', 'type_of_hair_coloring'
    ]

    # Write data to csv
    write_csv(products_file, fields, products)

db = MongoClient('mongodb://localhost:27017')
start_time = time.time()

def main():
    product_collection = db.huwebshop.products.find()

    print('Migrating products')
    migrate_products(product_collection)
    print('Done')

    profiles_collection = db.huwebshop.profiles.find()

    print('Migrating profiles')
    migrate_profiles(profiles_collection)
    print('Done')

    # Sort profiles
    print('Sorting profiles')
    sorted_profiles = sort_profiles(profiles_collection)
    print('Done')

main()

if __name__ == "__main__":

    processes = []

    print('Migrating sessions')

    for i in range(10):
        p = Process(target=migrate_sessions, args=(db.huwebshop.sessions.find(), profiles_collection, i*1000, (i+1)*1000,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print('Done')

    end_time = time.time()

    elapsed_time = end_time - start_time

    # Generate log file
    generate_log(elapsed_time, end_time)
