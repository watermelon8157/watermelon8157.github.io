import os
import requests
import json

def download_file(url, target_folder):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(target_folder, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
                
def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        dataList = json.load(json_file)
        cards = [data.get('cards') for data in dataList if 'cards' in data]
        flattenedCards = [item for card in cards for item in card]
        images = ['https://hbr.quest/hbr/' + card.get('image') for card in flattenedCards if 'image' in card]
        
        for url in images:
            download_file(url, 'charactersCardimage')        


# 使用方式
parse_json('characters.json')
print('下載圖片玩成!')