# import sys because we need to read and write data to STDIN and STDOUT 
import sys
from pathlib import Path

source_in_file_path = Path.cwd() / 'source_in.txt'
mapper_out_file_path = Path.cwd() / 'mapper_out.txt'
all_words = []

with open(source_in_file_path, 'r') as f_in:
    content = f_in.readlines()
    

# reading entire line from STDIN (standard input)
for line in content: 
    line = line.strip().lower().replace('\t',' ').replace(',','').replace('.','')\
           .replace('"','').replace("'",'').replace(':','')\
           .replace('“','').replace('”','').replace('’','')
    words = line.split()
    all_words = all_words + words
    
all_words.sort()   
with open(mapper_out_file_path, "w") as f_mapper_out:
    for word in all_words: 
        f_mapper_out.write('%s\t%s\n' %(word, '1'))