
# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup

import re
# Opening the html file
# existing_op_falling_water.html
# new_op_falling_water.html

file_1_name = r"Arma_3_Preset_10th_2024"

def ret_download_link(html_name: str) -> None:
  HTMLFile = open(html_name+".html", "r") 
    
  # Reading the file 
  index = HTMLFile.read() 
    
  # Creating a BeautifulSoup object and specifying the parser 
  S = BeautifulSoup(index, 'lxml') 
    
  # Using the find_all method to find all elements of a tag 
  with open(html_name + '.txt', 'w') as f:
    for tag in S.find_all('a', {'data-type': 'Link'}): 
        f.write(f'{tag.text}\n')
  
  return None

ret_download_link(file_1_name)

def ret_steamcmd_lines(file_1_name) -> None:
    with open('command_lines.txt', 'w') as f: 
        f.write('// https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_an_App\n')

        f.write('@ShutdownOnFailedCommand 1\n')
        f.write('@NoPromptForPassword 1\n')
        f.write('force_install_dir ../serverfiles/mods \n')

        f.write('login ChikinArma svpXGABI\n')


        with open(file_1_name + '.txt', 'r') as g:
            for line in g.readlines():
                mod_id = re.search("([0-9]+)$",line)
                f.write(f'workshop_download_item 233780 {mod_id[0]}\n')

        f.write('quit')


    return None

ret_steamcmd_lines(file_1_name)