### Internet
- En buyuk networklerden biridir.

### Network turleri
- Common Bus Topology: Guvenli degil
- Fully Connected Network Topology: Hizli ama pahali ve karmasik
- Star Network Topology: gunumuzde kullanilan. switch ya da routerla kullanilir. Tren yollarindaki makaslara benzer.
- Mesh Netwotrk Topology: Fully Connected Network Topology ye gore biraz daha  daha yavas ama daha az karisik ve pahali
- Ring Network Topology : Bir baglanti gitse network gitti.

### Network cihazlari
- Hub: akilsiz bir cihaz. Aldigi veriyi diger portlardan gonderirir. 
- Gateway: farkli aglari birbirne baglar. Gelismistir. Iki agin birbirini anlamasini saglar.
- Router: En ileri cihaz. IP adreslerini kullanir. Internete cikisi saglar. Paketleri inceler. Karar verme yetisi var. Routerín internete cikan IP dis IP oluyor. Icerdekiler ayri aglar seklinde oluyor. Paketin ne tarafa gidecegini IP'ler aracailigiyla bilir. 
- Repeater: sinyalleri guclendirir. Cok akilli degil.
- Bridge: Birden fazla agi birbirne baglar. Nispeten akilli. Bilginin gelmedigi yere gonderim yapar.
- Switch: kendisine bagli cihazlari bilir. Mac adresi kullanir. 
- Wireless acces point: Kablosuz cihazlari kendine baglar. TV, bilgisayar. telefon, tablet gibi.
- Firewall: Paket filtreleme yapar. Paketi inceler. icindeki kurallara gore pakete izin verir ya da vermez.
- Baz istasyonlari: sinyalleri guclendirir. repeater gorevi yapar..
- Modem: All in one: Switch, wireless access point, Router(internet) islerinin hepsini tek basina yapiyor. Evlerde kullandigimiz modem bu.

### Internet
- Routerlar ile alici ile verici arasinda iletisim saglanir.
- Evdeki modeme bagli cihazlar icin modem icinde ayri IPler vardir. Kisiye ozel degildir. Disariya acilan IP adresi Uniquedir. Yani modemin icindeki router cikis IP'si unique'tur.

### IP
- 172.16.254.1 - IPv4
- Binary karsiligi var. Her bir noktadan sonra 8 bit var. Toplam 32 bit 4 bayt yapar.
- 8 bit 1 bayttir.
- 10101100.00010000.11111110.00000001
- 256 tane sayi aliyor. 0 ile 255 arasinda deger alir. Hepsi bir oldugunda 255 degeri alir. 
- Internal IP: LAN kismi - Ic kisim
- External IP: Globale acilinan yer. Yani internet gibi.
- Private IP: 
- Public IP: 
- 3 cesit IP cesidi var. A, B, C, D. E

### A
- 10.0.0.0 - 10.255.255.255
- default subnet degeri 255.0.0.0 / 8
- 10 ile baslar

### B
- 172.16.0.0 - 172.31.255.255
- Default subnet degeri255.255.0.0 /16
- 172 ile baslar

### C
- Az cihazli
- 255 tane cihaz alir.
- 192.168.0.0 - 192.168.255.255
- Defauly subnet degeri: 255.255.255.0 / 24
- 192 ile baslar

### Neden Subnet?
- daha verimli kullanmak
- broadcast trafigini azaltmak
- networku daha kolay yonetmek
- guvenligi saglamak

### Subnet
- Bir Ip adresininin hangi Networkte oldugunun belirlenmesi icin kullanlir.
- default subnette kac tane 1 varsa o kadar 8 ekleniyor gosterim icin.
- Her 255 1 dir.
- network ve hostlar icin ayri bolumler olur.
- class A icin: 255.0.0.0 : 255 network icin 0'lar ise hostlar icin ayrilmistir.
- Network kismindan ayni agda olup olmadigini anlar hostlar.
- Subnet eklemesi soldan saga dogru yapilir.
- Prefix subnet kismini gosterir.
- sol tarafta kac tane 1 varsa subnet o sayi ile gosterilir.
- Subnete gore cihaz sayisi degisir.
- 32 bitten olusuyor.
- subnet sayesinde bir IP adresinin Networkunu, broadcast adresini, kullanilabilir ilk ve son adresini bulabiliyoruz.

192.168.1.19 / 24 (CIDR)

IP: 192.168.1.10 / Subnet Mask: 255.255.255.0 1 bitlerinin sayisi(prefix)
                   Subnet 11111111.11111111.11111111.00000000
                              8 +      8 +      8 =       24
Subnet Mask: 11111111.11111111.11111111.00000000
IP         : 11000000.10101000.00000001.00001010 

- Bu IP adresinin ilk 24 biti Network kismini son 8 biti ise Host kismini gosterir.
- Nertwork adresi: 192.168.1.00000000 - host kismina 0'lari ekledik
- Network adresi: 192.168.1.0
- Broadcast adresi: 192.168.1.11111111 - host kismini 1 yaptik
- Broadcast adresi: 192.168.1.255
- Bu networkteki kullanilabilir ilk adres: Network adresinden 1 fazla olan adres:   192.168.1.1
- BU networkteki kullanilabilir son adres: Broadcast adresinden 1 eksik olan adres: 192.168.1.254