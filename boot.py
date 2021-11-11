import requests
import json

def retrieve_messages(channel_id,file_name,headers):
  
  r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages',headers=headers)
  jsonn = json.loads(r.text)
  text_file = open(file_name, "w")
  for value in jsonn:
    text_file.write(value['author']['username']+':'+value['content']+'\n')
    print(value, '\n')
  text_file.close()


file_name1 = "practica1.txt" 
file_name2 = "practica2.txt" 
file_name3 = "practica3.txt" 
file_name4 = "practica4.txt" 
file_name5 = "practica5.txt" 
file_name6 = "practica6.txt"  
#To work I have to impor the nex items:
#headers
#channelid


#retrieve_messages(id_practica1,file_name1)
#retrieve_messages(id_practica2,file_name2)
#retrieve_messages(id_practica3,file_name3)
#retrieve_messages(id_practica4,file_name4)
#retrieve_messages(id_practica5,file_name5)
#retrieve_messages(id_practica6,file_name6)