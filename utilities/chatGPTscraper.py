import requests
from bs4 import BeautifulSoup
import os

start_link = 69

# URL of the website to scrape
url = 'https://oceans11.lanl.gov/deepwaterimpact/yC11_300x300x300-FourScalars_resolution.html'

# Make a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')
links = links[start_link:len(links) - 1]

file_number = start_link

for link in links:
    # Get the URL of the link
    link_url = link.get('href')
    print(f'Downloading...')
    
    # Make a request to the link URL and get the HTML content
    link_response = requests.get(link_url)
    link_html_content = link_response.content
    
    # Save the HTML content to a file with a .vtk extension
    file_name = os.getcwd() + '\\data\\' + link_url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(link_html_content)
        file_number += 1
        print(f'File {str(file_number)} of {len(links) + start_link} written to: {file_name}')