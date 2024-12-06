import requests
from pathlib import Path

downloadurl = "https://raw.githubusercontent.com/fivethirtyeight/data/\
master/nba-elo/nbaallelo.csv"
target_csv_path = Path.cwd() / 'nba_all_elo.csv'

response = requests.get(downloadurl)
if response.status_code == requests.codes.ok:
    with target_csv_path.open(mode='wb') as file:
        file.write(response.content)
    print("Download ready.")
else:
    print("Can NOT download.")