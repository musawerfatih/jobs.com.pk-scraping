from bs4 import BeautifulSoup
import requests
import csv

url = 'https://jobs.com.pk'
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

# Creating, opening and adding headlines to file
csv_file = open('Pakistan_Jobs.csv', 'w') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['JOB TITLE', 'JOB PLACE', 'DATE', 'LINK'])

all_jobs = soup.find('table', class_='table-jhp')
# print(jobs)
# print(all_jobs.prettify())

jobs = all_jobs.find_all('tr')
# for job in jobs:
#     print(job)
#     print()

for job in jobs:

    job_title = job.find_all('td')[-2].text
    job_place = job.td.a.text
    date = job.find_all('td')[-1].text
    job_link = job.td.a['href']

    print('JOB TITLE: ', job_title, '\n')
    print('JOB PLACE: ', job_place, '\n')
    print('DATE: ', date, '\n')
    print('VISIT LINK: ', job_link)
    print('-'*90)

    csv_writer.writerow([job_title, job_place, date, job_link])

csv_file.close()

