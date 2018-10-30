#!/usr/bin/env python3

import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="an input csv file is required")
parser.add_argument("output_occ", help="specify an output path for the top 10 occupations")
parser.add_argument("output_sta", help="specify an output path for the top 10 states")
args = parser.parse_args()

with open(args.input, mode='r', encoding='utf-8') as h1b_csv:
    h1b = csv.DictReader(h1b_csv, delimiter = ';')
    n = 0
    top_occ = {}  # top 10 occupations
    top_sta = {}  # top 10 states

    for row in h1b:
        # handle different names of variables used in different years
        if 'CASE_STATUS' in row.keys():
            row['STATUS'] = row['CASE_STATUS']
        if 'SOC_NAME' in row.keys():
            row['LCA_CASE_SOC_NAME'] = row['SOC_NAME']
        if 'WORKSITE_STATE' in row.keys():
            row['LCA_CASE_WORKLOC1_STATE'] = row['WORKSITE_STATE']

        if row['STATUS'] == 'CERTIFIED':
            n += 1
            name = row['LCA_CASE_SOC_NAME']
            state = row['LCA_CASE_WORKLOC1_STATE']

            # count number of certified applications for each OCCUPATION
            if name not in [entry['TOP_OCCUPATIONS'] for entry in top_occ.values()]:
                top_occ[name] = {'TOP_OCCUPATIONS':name, 'NUMBER_CERTIFIED_APPLICATIONS': 1}
            else:
                top_occ[name]['NUMBER_CERTIFIED_APPLICATIONS'] += 1

            # count number of certified applications for each STATE
            if state not in [entry['TOP_STATES'] for entry in top_sta.values()]:
                top_sta[state] = {'TOP_STATES':state, 'NUMBER_CERTIFIED_APPLICATIONS': 1}
            else:
                top_sta[state]['NUMBER_CERTIFIED_APPLICATIONS'] += 1

# calculate percentage of certified applications for each OCCUPATION in all certified applications
for entry in top_occ.values():
    entry['PERCENTAGE'] = str(round(entry['NUMBER_CERTIFIED_APPLICATIONS'] / n * 100, 1)) + '%'

# calculate percentage of certified applications for each STATE in all certified applications
for entry in top_sta.values():
    entry['PERCENTAGE'] = str(round(entry['NUMBER_CERTIFIED_APPLICATIONS'] / n * 100, 1)) + '%'

# sort by number of certified applications in descending order and then by OCCUPATIONS alphabetically
top_occ_sorted = sorted(top_occ.items(), 
                      key=lambda x: (-1*x[1]['NUMBER_CERTIFIED_APPLICATIONS'], x[1]['TOP_OCCUPATIONS']))

# sort by number of certified applications in descending order and then by STATES alphabetically
top_sta_sorted = sorted(top_sta.items(), 
                      key=lambda x: (-1*x[1]['NUMBER_CERTIFIED_APPLICATIONS'], x[1]['TOP_STATES']))

# write out top 10 occupations
with open(args.output_occ, 'w', newline = '') as csvfile:
    fieldnames = ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')

    writer.writeheader()
    counter = 0
    for item in top_occ_sorted:
        if counter < 10:
            writer.writerow(item[1])
            counter += 1

# write out top 10 states
with open(args.output_sta, 'w', newline = '') as csvfile:
    fieldnames = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')

    writer.writeheader()
    counter = 0
    for item in top_sta_sorted:
        if counter < 10:
            writer.writerow(item[1])
            counter += 1