import os
import requests

def get_filenames(start_path, size=1):
    small_files = []
    for filename in os.listdir(start_path):
        filepath = os.path.join(start_path, filename)
        if os.path.isfile(filepath) and os.path.getsize(filepath) < size * 1024 * 1024:
            small_files.append(filepath.split('\\')[-1])
    return small_files

def download(url, save_loc, file_number=-1, len_files=1):
    # Make a request to the link URL and get the HTML content
    print(f'Downloading from {url}...')
    link_response = requests.get(url)
    link_html_content = link_response.content

    file_name = save_loc + '/' + url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(link_html_content)

    if file_number > -1:
        print(f'File {str(file_number)} of {len_files} written to: {file_name}')
    else:
        print(f'File written to: {file_name}')

def download_by_threshold(save_loc, url, size=1, start=0):
    files = get_filenames(save_loc, size)

    file_number = start
    files = files[start:]
    for link in files:
        # Get the URL of the link
        link_url = url + '/' + link
        
        download(link_url, save_loc, file_number, len(files) + start)
        file_number += 1

if __name__ == '__main__':
    url = 'http://oceans11.lanl.gov/deepwaterimpact/yB31/460x280x240-AllScalars'
    start_path = 'D:/school/yB31_sc2/yB31_oneblock_BIG'
    # download_by_threshold(start_path, small_files, url)
    broken = ['yB31_oneblock_36813.vti', 'yB31_oneblock_37813.vti', 'yB31_oneblock_38141.vti', 'yB31_oneblock_40447.vti', 'yB31_oneblock_40797.vti',
              'yB31_oneblock_41147.vti','yB31_oneblock_41264.vti','yB31_oneblock_41489.vti','yB31_oneblock_42756.vti',
              'yB31_oneblock_43219.vti', 'yB31_oneblock_43331.vti','yB31_oneblock_43440.vti','yB31_oneblock_43656.vti',
              'yB31_oneblock_44494.vti','yB31_oneblock_44593.vti','yB31_oneblock_44800.vti', 'yB31_oneblock_44999.vti',
              'yB31_oneblock_45308.vti','yB31_oneblock_45632.vti','yB31_oneblock_45690.vti','yB31_oneblock_45806.vti',
              '']
    file_number = 0
    for file in broken:
        file_number += 1
        download(url + '/' + file, start_path, file_number, len(broken))