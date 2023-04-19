import requests
from bs4 import BeautifulSoup
import os

def get_data(url, start=0, scalar=0, path=-1):
    if path == -1:
        path = os.getcwd()
    
    path += + '\\' + url.split('/')[-1].split('_')[0]

    if scalar != 0:
        path += f"_sc{scalar}"

    # Create folder for data
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Folder already exists")
    else:
        print(f"Folder created at {path}")
    print(f"Data will be located here: {path}")


    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the links on the webpage
    all_links = soup.find_all('a')

    # Remove the first and last link (they don't have data)
    all_links = all_links[1:len(all_links) - 2]

    # Apply scalar
    if scalar != 0:
        file_counter = 0
        links = []
        for link_index in range(len(all_links)):
            if file_counter == 0:
                links.append(all_links[link_index])
            if file_counter == scalar - 1:
                file_counter = 0
            else:
                file_counter += 1

    links = links[start:]

    file_number = start
    for link in links:
        # Get the URL of the link
        link_url = link.get('href')
        print(f'Downloading...')
        
        # Make a request to the link URL and get the HTML content
        link_response = requests.get(link_url)
        link_html_content = link_response.content
        
        # Save the HTML content to a file with a .vtk extension
        file_name = path + '\\' + link_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(link_html_content)
            file_number += 1
            print(f'File {str(file_number)} of {len(links) + start} written to: {file_name}')

if __name__ == "__main__":
    url = 'https://oceans11.lanl.gov/deepwaterimpact/yB31_460x280x240-AllScalars.html'
    get_data(url, scalar=2, start=127, path='A:\School\SciFiVis\data')