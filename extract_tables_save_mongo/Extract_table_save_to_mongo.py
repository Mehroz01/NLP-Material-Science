import PyPDF2
from tabula import read_pdf
from os import listdir
from pathlib import Path
import json
import os.path
import os

import pymongo
data_set=[]
table_dict={}

path=os.getcwd()+'/PDF_files/' 
# #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# #myclient = pymongo.MongoClient("mongodb://cloud8@192.168.23.108:9876")
myclient = pymongo.MongoClient('192.168.23.108:9876')
mydb = myclient["processed_data006"]
# mycol = mydb['testing']
mycol = mydb['testing_page006']

pdf_files=listdir(path)
for i in range(0,len(pdf_files)):
    if os.path.splitext(pdf_files[i])[1][1:]=='pdf':
        pdf_path=path+pdf_files[i]
        pdf_name=pdf_files[i]
        reader = PyPDF2.PdfFileReader(open(pdf_path, mode='rb' ))
        n = reader.getNumPages() 

        
        for page in range(n):
            
            
            d = read_pdf(pdf_path, multiple_tables=True,Lattice=True,java_options="-Dfile.encoding=UTF8",
              pages = page)

            
            #print('\n type of d is ',type(d))
            print('-')
            if len(d)!=0:
                #table_dict=table_dict.clear()
                table_dict=0
                table_dict={}

                table_dict['tables']=d
                table_dict['page']=page
                table_dict['detail']=pdf_name
                print('\n PDF detail name ',pdf_name)    
                
                #print('\n tale appending ',table_dict)
                #print('\n table dictionary is ',table_dict)
                
                data_set.append(table_dict)
                
                #table_dict={}
                #print('\n appending List',data_set)
                d=0
                

information={}

for dict_num in range(0,len(data_set)):
    for table_num in range (0,len(data_set[dict_num]['tables'])):
        df=data_set[dict_num]['tables'][table_num]
        #print('\n dataframe type is ',type(df))
        #print('\n data_set[dict_num][tables][table_num]',data_set[dict_num]['tables'][table_num])
        if len(df)!=0:
            table = df.to_dict('dict')
            information['detail']=data_set[dict_num]['detail']
            information['tables']=table
            information['page']=data_set[dict_num]['page']   

            records = json.dumps(information)
            loaded_r = json.loads(records)
            print('\n **********************************************************')
            #print(loaded_r)
            print('\n **********************************************************')
            #print(loaded_r)
            x = mycol.insert_one(loaded_r)

            print('\n inserted id : ',x.inserted_id)             




