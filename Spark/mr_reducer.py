from operator import itemgetter 
import sys 
from pathlib import Path

mapper_out_file_path = Path.cwd() / 'mapper_out.txt'
reducer_out_file_path = Path.cwd() / 'reducer_out.txt'

with open(mapper_out_file_path, 'r') as f_in:
    content = f_in.readlines()


current_word = None
current_count = 0

with open(reducer_out_file_path, "w") as f_reducer_out:
# read the entire line from STDIN 
    for line in content:
        if line!='':
            word, count = line.strip().split('\t')
            count = int(count) 
        # this IF-switch only works because Hadoop SORTS map output by key (word) before passed to reducer
        if current_word == word:
            current_count += count
        else: 
            # write result to STDOUT
            if current_word: 
                f_reducer_out.write('%s\t%s\n' %(current_word, current_count))
            current_word = word
            current_count = count

    # do not forget to output the last word if needed! 
    if current_word == word:
        f_reducer_out.write('%s\t%s' %(current_word, current_count))