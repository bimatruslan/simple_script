import pandas as pd
import os

#Enter your folder path that contains your dta files
#masukin path folder tempat file dta disimpen
path = input("Masukan path folder tempat file disimpan: ") +"\\"
nama_file =[]

#Make a list from all of your file in your folder
#Buat list yang isinya semua file dari folder
folder = os.listdir( path )

#sort the file that have a .dat extention
#sort file yang ekstensinya .dta
for file in folder :
    if file[-3:]== "dta" :
        nama_file.append(file)

#convert all of the dta files based on the amout of files in nama_files into a csv format and save it in your folder
#convert file dta ke csv berdasarkan jumlah nama file yang ada di list nama_file dan simpan dalam foldermu 
for file  in nama_file :
    data = pd.read_stata(path + file)

    data.to_csv(path + file[:-3] +'csv')
