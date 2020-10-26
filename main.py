import json
import xml.etree.ElementTree as ET
from collections import Counter


def get_text_json(json_file):
  with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

  news_list =[title['description'] for title in data['rss']['channel']['items']]
  return news_list

def get_text_xml(xml_file):
  parser = ET.XMLParser(encoding='utf-8')
  tree = ET.parse(xml_file, parser)
  root = tree.getroot()
  news_list = [item.find('description').text for item in root.findall('channel/item')]
  return news_list


def get_top_words(news_list, min_word_length, top_words):
  news_list = list(map(lambda x: x.split(' '), news_list))
  news_words = []

  for news in news_list:
    more_than_six = list(filter(lambda x: len(x) > min_word_length, news))
    news_words.extend(more_than_six)

  news_words = Counter(news_words)
  return news_words.most_common()[:top_words]

if __name__ == '__main__':
  print(get_top_words(get_text_json('files/newsafr.json'), 6, 10), sep='\n')
  print()
  print(get_top_words(get_text_xml('files/newsafr.xml'), 6, 10), sep='\n')