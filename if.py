#karşılaştırma oparatörleri
# < küçüktür, > büyüktür, >= büyük eşittir, <=küçük eşittir, == aşittir, != aşit değildir .

cinsiyet=input("bir harf giriniz:")

if cinsiyet== "e" or cinsiyet=="E":
     print("cinsiyet olarak erkek girdiniz")
     print("if içerisinden selamlar")
     print("şuanda if dışındasın")

elif cinsiyet=="k" or cinsiyet=="K":
     print("cinsiyet olarak kadın girdiniz")
     print("elif içerisinden selamlar")
     print("şuanda elif dışındasın")
else:
   print("ben sana e yada k gir demedim mi!")
print("şuanda if dışındasın")
