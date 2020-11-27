print("**********DENISS ZAPLAVNIJS 10.A **********")
print("****************KALKULATORS****************")


#kalkulators, kas ļauj saprast, vai tev ir laba vidēja atzīme par visam valodām salīdzinājumā ar klasi.


print("Sveiki! Es tev palīdzēšu uzzināt, vai tavai klasei ir laba atzīme salīdzinājumā ar skolu\nun mēs arī nokārtosim tavu atzīmi ar tavu klasi.")
#b=skolas vidēja atzīme
X=0,10 #


#1.stunda angļu valoda
b= float(input("\nIevadiet vidējo atzīmi angļu valodā Jūsu skolā: "))
while b<1 or b>10:
  print ("Jums ir kļūda!!!!!!!!")
  b= float (input ("Ievadiet vidējo atzīmi angļu valodā Jūsu skolā: "))
ang=float(input("Ievadiet vidējo klases vērtējumu angļu valodu: "))
if ang>b and ang<=10:
    print ("Jūsu klases atzīme angļu valodā ir ļoti laba, salīdzinājot ar skolu")
if ang==b:
    print ("Jums ir vidēja atzīme salīdzinājot ar skolu ")
while ang<1:
    print ("Jums ir kļūda!!!!!!!!")
    ang=float(input("\nIevadiet vidējo klases vērtējumu angļu valodu: "))
while ang>10:
    print ("Jums ir kļūda!!!!!!!!")
    ang=float(input("\nIevadiet vidējo klases vērtējumu angļu valodu: "))
else:
    if ang<b:
      print("Jums ir slikta atzīme salīdzinājot ar skolu")
  
  


#2.stunda latviešu valoda
b= float(input("\nIevadiet vidējo atzīmi latviešu valodā Jūsu skolā: "))
while b<1 or b>10:
  print ("Jums ir kļūda!!!!!!!!")
  b= float(input("\nIevadiet vidējo atzīmi latviešu valodā Jūsu skolā: "))
lat=float(input("Ievadiet vidējo klases vērtējumu latviešu valodu: "))
if lat>b and lat<=10:
    print ("Jūsu klases atzīme latviešu valodā ir ļoti laba, salīdzinājot ar skolu")
if lat==b:
    print ("Jums ir vidēja atzīme, salīdzinājot ar skolu")
while lat<1:
    print ("Jums ir kļūda!!!!!!!!")
    lat=float(input("Ievadiet vidējo klases vērtējumu latviešu valodā: "))
while lat>10:
    print ("Jums ir kļūda!!!!!!!!")
    lat=float(input("Ievadiet vidējo klases vērtējumu latviešu valodā: "))
else:
  if lat<b:
   print ("Jums ir slikta atzīme, salīdzinājot ar skolu")

#3.stunda Krievu valoda
b= float(input("\nIevadiet vidējo atzīmi krievu valodā Jūsu skolā: "))
while b<1 or b>10:
  print ("Jums ir kļūda!!!!!!!!")
  b= float(input("\nIevadiet vidējo atzīmi krievu valodā Jūsu skolā: "))
kriev=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
if kriev>b and kriev<=10:
    print ("atzīme par Krievu valodu ir ļoti laba, salīdzinājot ar skolu")
if kriev==b:
    print ("Jūms ir vidēja atzīme, salīdzinājot ar skolu")
while kriev<1:
    print ("Jums ir kļūda!!!!!!!!")
    kriev=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
while kriev>10:
    print ("Jums ir kļūda!!!!!!!!")
    kriev=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
else:
  if kriev<b:
    print ("Jums ir slikta atzīme, salīdzinājot ar skolu")


#4.stunda Vācu valoda
b= float(input("\nIevadiet vidējo atzīmi vācu valodā Jūsu skolā: "))
while b<1 or b>10:
  print ("Jums ir kļūda!!!!!!!!")
  b= float(input("\nIevadiet vidējo atzīmi vācu valodā Jūsu skolā: "))
vac=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
if vac>b and vac<=10:
    print ("atzīme par Krievu valodu ir ļoti laba, salīdzinājot ar skolu")
if vac==b:
    print ("Jums ir vidēja atzīme, salīdzinājot ar skolu")
while vac<1:
    print ("Jums ir kļūda!!!!!!!!")
    vac=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
while vac>10:
    print ("Jums ir kļūda!!!!!!!!")
    vac=float(input("Ievadiet vidējo klases vērtējumu krievu valodā: "))
else:
  if vac<b:
    print ("Jums ir slikta atzīme, salīdzinājot ar skolu")


#Manas atzīmes valodās
myang=float(input("\nIevadiet savu vidējo vērtējumu angļu valodā: "))
while myang<1 or myang>10:
  print ("Jums ir kļūda!!!!!!!!")
  myang= float(input("Ievadiet savu vidējo vērtējumu angļu valodā: "))

mylat=float(input("\nIevadiet savu vidējo vērtējumu latviešu valodā: "))
while mylat<1 or mylat>10:
  print ("Jums ir kļūda!!!!!!!!")
  mylat=float(input("Ievadiet savu vidējo vērtējumu latviešu valodā: "))

mykriev=float(input("\nIevadiet savu vidējo vērtējumu krievu valodā: "))
while mykriev<1 or mykriev>10:
  print ("Jums ir kļūda!!!!!!!!")
  myrus= float(input("Ievadiet savu vidējo vērtējumu krievu valodā: ")) 

myvac=float(input("\nIevadiet savu vidējo vērtējumu vācu valodā: "))
while myvac<1 or myvac>10:
  print ("Jums ir kļūda!!!!!!!!")
  myvac= float(input("Ievadiet savu vidējo vērtējumu vācu valodā: "))

if myang<ang:
   print ("Jūsu atzīme par angļu valodu ir sliktāka par klases vidējo")
else:
  print ("Jūsu atzīme  par angļu valodu ir labāka par klases vidējo")

if mylat<lat:
   print ("Jūsu atzīme par latviešu valodu ir sliktāka par klases vidējo")
else:
  print ("Jūsu atzīme  par latviesu valodu ir labāka par klases vidējo")

if mykriev<kriev:
   print ("Jūsu atzīme par krievu valodu ir sliktāka par klases vidējo")
else:
  print ("Jūsu atzīme  par krievu valodu ir labāka par klases vidējo")

if myvac<vac:
   print ("Jūsu atzīme par vācu valodu ir sliktāka par klases vidējo")
else:
  print ("Jūsu atzīme  par vācu valodu ir labāka par klases vidējo")



  

    
