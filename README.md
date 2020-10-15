# SmartMirror
Akıllı ayna hava durumunu, tarih&saat bilgilerini ve haberleri gösteriyor. Donanımsal olarak Normal camlı bir çerçeve, camı kaplamak için ayna görünümlü geçirgen bir filtre, Raspberry Pi 3 A+ modeli, 16 GB SD kart, android güç adaptörü ve philips 19 inç bir monitör kullandım.

![WhatsApp Image 2020-06-29 at 14 11 35](https://user-images.githubusercontent.com/26454080/96104439-86630980-0ee1-11eb-9c4c-5552000d348b.jpeg)
![image1 (1)](https://user-images.githubusercontent.com/26454080/96104446-882ccd00-0ee1-11eb-825a-1af6031c4f77.png)


**Donanım Kısmı**


50,60 boyutlarında monitörün enine uygun olarak arka kısmı olmayan camlı bir çerçeve yaptırdım. Bu çerçeve camının ön kısmını ayna görünümlü cam filtresiyle kapladım.(Bu filtreleri otosanayide bulabilirsiniz.)Monitörün üstünde kalan boş kısmın arkayı göstermemesi için çerçevenin arkasından siyah cam filtresiyle kapladım. Daha sonra ekrana çerçeveyi bir hamur yapıştırıcıyla yapıştırıp arkasından bantlarla sabitledim. Monitörü HDMI kablosuyla Raspberrye bağladım.(Monitör elektriğini raspberryden çekmiyor ayrı bir power supplierla prizden çekiyor). 16 GBlık SD karta Raspbian işletim sistemini 'balena etcher' programını kullanarak yükledim. Daha sonra raspberryi çalıştırıp ekran ayarlarını yapıp wifiye bağladım. Ekran klavyesi indirdim böylece ssh uzaktan bağlantıya gerek kalmadan mouse ve ekran klavyesiyle raspberryi kullanabilir hale geldim. Githubdan Smart mirror projesini çektikten sonra Thonny editöründe çalıştırarak ekranda aynanın görüntüsünü elde ettim. (feedparser kütüphanesi bazen çalışmıyor tekrar yükleyip silince sorun ortadan kalkıyor) Raspberrynin uykuya almasını engellemek için xscreensaver programını kullandım. Kartın zarar görmemesi için robotistandan gelen kendi kutusunu boyuyarak onu içine yerleştirdim.


![pixiz-08-07-2020-21_01_25](https://user-images.githubusercontent.com/26454080/86959684-f33e6900-c166-11ea-8ed0-663d2f697be2.jpg)
![pixiz-08-07-2020-21_03_05](https://user-images.githubusercontent.com/26454080/86959688-f46f9600-c166-11ea-80bb-2dd1a9237a47.jpg)


