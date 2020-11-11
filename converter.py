import pandas as pd
import os
#masukin path folder tempat file dta disimpen
path = input("Masukan path folder tempat file disimpan: ") +"\\"
nama_file =[]

#Buat list yang isinya semua file dari folder
folder = os.listdir( path )

#sort file yang ekstensinya .dta
for file in folder :
    if file[-3:]== "dta" :
        nama_file.append(file)

#convert file dta ke csv berdasarkan jumlah nama file yang ada di list nama_file
for file  in nama_file :
    data = pd.read_stata(path + file)

    data.to_csv(path + file[:-3] +'csv')