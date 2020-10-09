def count_top10_json():
  import json
  with open("files/newsafr.json") as f:
    json_data = json.load(f)

  titles = json_data["rss"]["channel"]["items"]
  
  desc = []
  unique_word = []
  
  for title in titles:
    # print(title[0])
    desc.append(title['description'])
  # print(desc[1])
  # print()
  for string in desc:
    uniques = string.split(' ')
    # print(uniques)
    for word in uniques:
      if len(word) > 6:
        unique_word.append(word)      
  # print(unique_word)
  counts = []

  for words in unique_word:
    count = 0
    for word in unique_word:
      if word == words:
        count += 1
    # print(count, words)
    if (count, words) not in counts:
      counts.append((count, words))
  # print(counts)
  counts.sort()
  # print(counts)
  counts.reverse()
  # print(counts[0:10])

  for i in range (0, 10):
    count, word = counts[i]
    print(f'на {i+1} месте: слово \"{word}\", встречается {count} раз(а)')
  return
  
count_top10_json()