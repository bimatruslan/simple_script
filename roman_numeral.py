roman_numeral = { 1 : "I" , 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 11 : "XI", 50: "L", 100: "C", 500: "D", 1000 : "M"}
#function buat convert angka ribuan
def convertRibuan(RIBUAN, ROME) :
  ribuan = RIBUAN
  rome = ROME
  while ribuan > 999 : 
      seribuan = int(ribuan / (ribuan / 1000))
      rome = rome  + roman_numeral[seribuan]
      ribuan = ribuan - 1000
  
  ROME = rome
  return ROME


#function buat convert angka ratusan
def convertRatusan(RATUSAN, ROME) :
  ratusan = RATUSAN
  rome = ROME
  while ratusan > 99 :
    if ratusan >= 900 :
      rome = rome+roman_numeral[1000] + roman_numeral[100]
      ratusan = ratusan - 900

    elif ratusan >= 500 :
      rome = rome+roman_numeral[500]
      ratusan  = ratusan - 500

    elif ratusan >= 400 :
      rome = rome + roman_numeral[100] + roman_numeral[500]
      ratusan = ratusan - 400

    else :
      seratus = int(ratusan / (ratusan/100))
      rome = rome + roman_numeral[seratus]
      ratusan = ratusan - 100
  ROME = rome
  return ROME


#function buat convert angka puluhan
def convertPuluhan(PULUHAN, ROME) :
  puluhan = PULUHAN
  rome = ROME
  while puluhan > 9 :
    if puluhan >= 90 :
      rome = rome+roman_numeral[100] + roman_numeral[10]
      puluhan = puluhan - 90

    elif puluhan >= 50 :
      rome = rome+roman_numeral[50]
      puluhan = puluhan - 50
    
    elif puluhan >= 40 :
      rome = rome + roman_numeral[10] + roman_numeral[50]
      puluhan = puluhan - 40
    else :
      sepuluh = int(puluhan / (puluhan/10))
      rome = rome + roman_numeral[sepuluh]
      puluhan = puluhan - 10

  ROME = rome
  return ROME

#function buat convert angka satuan
def convertSatuan(SATUAN,ROME) :
  satuan = SATUAN
  rome = ROME
  while satuan > 0 :
    if satuan >=  9 :
      rome += roman_numeral[10] + roman_numeral[1]
      satuan -= 9

    elif satuan >= 5 :
      rome += roman_numeral[5]
      satuan -= 5
    
    elif satuan >= 4 :
      rome = rome + roman_numeral[1] + roman_numeral[5]
      satuan -=  4

    else:
      rome = rome + roman_numeral[1]
      satuan -= 1

  ROME = rome
  return ROME


#Funcution buat convert angka dari
def romanConvert( numbers ) :  
  satuan   = numbers % 10
  puluhan  = (numbers % 100 ) - satuan
  ratusan  = (numbers % 1000) - (numbers % 100)
  ribuan   = (numbers%10000) - (numbers % 1000)
  rome = ""
  if ribuan > 3000 :
        print("Batas maksimal nilai yang bisa diconvert adalah 3999")
  else :
      rome_val = convertRibuan(ribuan, rome) + convertRatusan(ratusan,rome) + convertPuluhan(puluhan,rome) + convertSatuan(satuan, rome)
  
      print(rome_val)
  


if __name__ == '__main__':
    romanConvert(int(input("Masukan angka: ")))