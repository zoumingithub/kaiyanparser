import codecs
import json


categorized_data = []

def load_data(path='/opt/kaiyanparser/categorylist.txt'):
    global categorized_data
    inf = codecs.open(path,mode='r',encoding='utf-8')
    lines = inf.readlines()
    for line in lines:
        line = line.strip('\n')
        category = json.loads(line,encoding='utf-8')
        cat_id = category['categoryInfo']['id']
        #parse videos
        section_list = category['sectionList']
        for section in section_list:
            if 'itemList' not in section:
                continue
            item_list = section['itemList']
            video_list = []
            for item in item_list:
                if 'data' not in item or 'itemList' not in item['data']:
                    continue
                inner_item_list = item['data']['itemList']
                for inner_item in inner_item_list:
                    if 'data' not in item:
                        continue
                    video = inner_item['data']
                    video_list.append(video)
            if len(video_list)>0: categorized_data.append(video_list)
    inf.close()
