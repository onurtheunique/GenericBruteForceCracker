def strings(lang:str):
    if lang.upper()=="TURK":
        DictTR={#"jobs":"Wordlist oluşturmak için 1.\nBrute Force Saldırısı başlatmak için 2\n\nÇıkış 0.\nSeçimizi giriniz.\n",
                "jobs":"Wordlist oluşturmak için 1.\nBrute Force Saldırısı başlatmak için 2\nWordlist kullanmadan işlem yapmak için 3\nÇıkış 0.\nSeçimizi giriniz.\n",
                "wlv":"Wordlist üetim yönteminizi tercih ediniz.\nYavaş Yöntem için 1\nHızlı yöntem için 2(Geliştirme)\n",
                "lenght":"Parola uzunluğu:\n",
                "updown":"Sadece küçük harf için,1.\nSadece BÜYÜKHARF için,2.\nBüYüK ve KüÇüK karakterler için,3.\n",
                "numbers":"Parola sayı içeriyor mu? Evet/Hayır\n",
                "charlist":"Listeyi oluşturacak karakterler (Opsiyonel):\n",
                "fileloc":"Parola dosyası program ile aynı dizinde olmalıdır.\nParola listesinin adını giriniz\n",
                "force":"Güç Seninle Olsun",
                "found":"Parola bulundu",
                "fnf":"Dosya Bulunamadı!\n",
                "Cc":"Kaba Kuvvet %s saniyede sona erdi\n",
                "record":"Kullanıcı: %s Parola: %s süre: %s\n",
                "wordliststatus":"%s karakter adımı oluşturuluyor \n",
                "wordlistended":"Kelime listesi  %s karakter ile  %s saniyede yaratıldı\n",
                "donein":"işlem %s saniyede tamamlandı \n",
                "terminated":"Dosya Bulunamadı!\nProgram Durduruldu....\n"}
        return DictTR
    elif lang.upper()=="ENG":
        DictENG={#"jobs":"To create a wordlist, type 1.\nTo initiate bruteforce, type 2.\nTo exit the program, type 0.\nEnter your choice:.\n",
                "jobs":"To create a wordlist, type 1.\nTo initiate bruteforce, type 2.\nTo initiate bruteforce without a wordlist 3\nTo exit the program, type 0.\nEnter your choice:.\n",
                "wlv":"Please choose your method of wordlist generation.\nFor the Slow Method, press 1\nFor the Fast Method, press 2 (Development).\n",
                 "lenght":"The length of the password to be generated:\n",
                 "updown":"For only lowercase letters, type 1.\nFor only uppercase letters, type 2.\nFor a combination of both uppercase and lowercase letters, type 3.\n",
                 "numbers":"Does the password include a number? Yes/No\n",
                 "charlist":"Characters to be used when creating the password (Optional):\n",
                 "fileloc":"The password list should be in the same directory as the application.\nEnter the name of the password list:\n\n",
                 "force":"May The Force Be With You",
                "found":"Password Match",
                 "fnf":"File not found!\n",
                "record":"key: %s password: %s cost: %s\n",
                "wordliststatus":"%s chars list ist started \n",
                "wordlistended":"Wordlist with %s chars created in %s seconts\n",
                 "terminated":"File not found!\nProgram terminated....\n",              
                 "donein":"Done! in %s seconds\n",
                 "Cc":"Brute Force Ended in %s seconds\n"}
        return DictENG
    
def charset(lang:str):
     if lang.upper()=="TURK":
        return ['a', 'b', 'c','ç', 'd', 'e', 'f', 'g','ğ', 'h','ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o','ö', 'p', 'q', 'r', 's','ş','t', 'u','ü', 'v', 'y', 'z']
     elif lang.upper()=="ENG":
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']