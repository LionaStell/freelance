import os


folder = 'otpt'

list_mp4 = os.listdir(folder)
dict_mp4 =  dict()

for i in list_mp4:
  dict_mp4[int(str(str(i.split('.')[0]).split('-')[0])+str(str(i.split('.')[0]).split('-')[1]))] = i

sorted_dict = dict(sorted(dict_mp4.items()))
s_list_mp4 = [i for i in sorted_dict.values()]

for i, val in enumerate(s_list_mp4):
  os.rename(f'{folder}/{val}', f'{folder}/{i+1}.mp4')