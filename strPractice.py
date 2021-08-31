text = "Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır"

# str daxilində neçə xarakter olduğunu ekrana yazdırın
print("str daxilində neçə xarakter olduğunu ekrana yazdırın : ")
print(len(text))

# str daxilində neçə hərf olduğunu ekrana yazdırın
print("str daxilində neçə hərf olduğunu ekrana yazdırın : ")
print(len(text) - text.count(" "))

# str daxilindəki sözləri ayrı bir massiv içərisində toplayın
print("str daxilindəki sözləri ayrı bir massiv içərisində toplayın : ")
print(text.split())

# str daxilində neçə sait və neçə samit olduğunu ekrana çap edin
print("str daxilində neçə sait və neçə samit olduğunu ekrana çap edin : ")
saitler = ['a','ı','o','u','e','i','ə','ö','ü']
sait = 0
samit = 0

for x in text.lower():
    if x in saitler:
        sait +=1
    else:
        samit +=1

print(f"""Saitlər : {sait} 
Samitlər : {samit}""")

# str daxilində son iki sözü silən metod yazın
print("str daxilində son iki sözü silən metod yazın : ")
print(' '.join([str(item) for item in text.split()[:-2]]))

# str ni vergülə görə ayırıb iki string halına gətirin
print("str ni vergülə görə ayırıb iki string halına gətirin : ")
print(text.rsplit(", "))

# stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın
print("stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın : ")

word = input("Sözü daxil edin : ")
def stringSearch(word):
    for x in text:
        if word in text:
            print(True)
        else:
            print(False)
        question = input("Yeni söz daxil etmək istəyirsiniz? Y/N\n")
        if question == "Y":
            word = input("Sözü daxil edin : ")
            stringSearch(word)
        else:
            exit()

stringSearch(word)