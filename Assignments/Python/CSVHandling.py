import csv
import os
'''
csv_file_path = "customers-100.csv"
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
'''

import csv
filepath='customers-100.csv'
'''with open(filepath,'w',newline="") as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(['Index', 'Customer Id', 'First Name', 'Last Name', 'Company', 'City', 'Country', 'Phone 1', 'Phone 2', 'Email', 'Subscription Date', 'Website'])
    data=[['1', 'DD37Cf93aecA6Dc', 'Jatin', 'J', 'XYZ Group', 'East Leonard', 'India', '229.077.5154', '397.884.0519x718', 'jjsts@ss.info', '2020-08-24', 'http://www.jj.com/'],
          ['1', 'DD37Cf93aecA6Dc', 'AMD', 'S', 'XYZ Group', 'East Leonard', 'India', '229.077.5154', '397.884.0519x718', 'AMD@SS.info', '2020-08-24', 'http://www.AMD.com/']
          ]
    csvwriter.writerows(data)
    print("writing had been completed")
   '''
with open(filepath,'a',newline="") as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(['Index', 'Customer Id', 'First Name', 'Last Name', 'Company', 'City', 'Country', 'Phone 1', 'Phone 2', 'Email', 'Subscription Date', 'Website'])
    data=[['1', 'DD37Cf93aecA6Dc', 'Jatin', 'J', 'XYZ Group', 'East Leonard', 'India', '229.077.5154', '397.884.0519x718', 'jjsts@ss.info', '2020-08-24', 'http://www.jj.com/'],
          ['1', 'DD37Cf93aecA6Dc', 'AMD', 'S', 'XYZ Group', 'East Leonard', 'India', '229.077.5154', '397.884.0519x718', 'AMD@SS.info', '2020-08-24', 'http://www.AMD.com/']
          ]
    csvwriter.writerows(data)
    print("writing had been completed")