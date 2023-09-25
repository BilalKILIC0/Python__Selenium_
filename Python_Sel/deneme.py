from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from kullanici import ad,sifre,yedekkod,kuladi,mesaj
import time


driver = webdriver.Chrome()                  # Driver 'e Chrome bağlamak için kullandık.
driver.maximize_window()                     # Açılan Ekranı Tam Ekran Olarak Açmak İçin Kullandık.

driver.get("https://www.instagram.com/")     # Bir sayfaya gitmek için .get fonksiyonunu kulanıyoruz.
kontrolet = driver.current_url
print(" Su an ki sayfa : " +kontrolet)
time.sleep(5)                                # Hemen kapanmaması için zaman sınırı getirdik.

def __init__(self,ad,sifre,yedekkod,kuladi,mesaj):

    self.browser = webdriver.Chrome()
    self.username = ad
    self.password = sifre
    self.kod = yedekkod
    self.user = kuladi
    self.message = mesaj



def giris(ad,sifre,yedekkod,kuladi,mesaj):                         # Giriş için fonksiyon oluşturduk.

    usernameInput = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(ad)        # Kullanıcı adi için gerekli yere kullanıcı adını yazdık.
    usurnameInput2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(sifre)    # Şifre için gerekli yere şifreyi yazdık.
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()   #İnstagram giriş butonuna tıklama yeri.
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/button').click()       #İnstagramın sizin için oluşturdğu kod alanına Tıklama yeri.
    time.sleep(5)
    usernameInput3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input').send_keys(yedekkod)  #İnstagramınızdan aldığınız yedek kod Yazma Kutucuğu.
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[2]/button').click() #Doğrula Butonu.
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div').click()  #İnstagram Ara Butonu.
    usernameInput4 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys(kuladi)  #Arama Çubuğu.(Kime MEsaj GÖndermek İstiyorsanız onun İnstagrm hesabının ismini Yazıyorsunuz.)
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a/div[1]/div/div/div[2]/div/div/div/span').click() #Seçilen Kişinin üzerine tıklamak için eklenen kod satırı.
    time.sleep(10)  
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div').click() #Mesaj Gönder Butonu.
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click() #Bu sizde çıkmaya bilir ama AÇıklayayım : Bildirimleri aç paneli Biz Şimdi değile Basacağız.
    time.sleep(5)
    usernameInput5 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p').send_keys(mesaj) #Burada ise Mesaj içeriği yazılan yer (Metin).
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER) # Enter Basmak için Keys Ekleyip Burada Çağırdık.
    time.sleep(5)


giris(ad,sifre,yedekkod,kuladi,mesaj)  #Fonksiyonumuzu Çağırdık Yoksa Program Çalışmaz !!!

 

('''                                                                            ---_Açiklama_---
    Eğer Kodumu Alip Kendiniz Kullanmak İstiyorsaniz Yapmaniz Gerekenler Kullanici.py Diye Bir Python Dosyasi Oluşturup O Kisma ad,sifre,yedekkod,kuladi,mesaj Değişkenlerini
    Oluşturup Kendi İstegram Adresini Girmelisiniz Ve Bilgileri Yeni Girilecek Hesaba Update Etmeniz Gerekmektedir Yoksa Çalişmaz Program. Eğer Buraya Kadar Geldiysen Teşekkürler :=)  ''')
