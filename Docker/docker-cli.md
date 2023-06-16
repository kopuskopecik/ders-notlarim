### docker version
- docker versiyonunu gosterir.
- dockerín calistigini anlariz.

### docker info
- temel tum bilgilere burdan ulasabiliyoruz.

### docker
- kullanabilecegimiz commandlari gosterir.
- management commands ve commandsler olarak ikiye ayrilir.
- optionslarda genelde dogrudan docker system-daemon ile ilgili commandlar var.

### docker management-command command
- genel calisma yapisi bu sekilde

### docker container ve docker run
- aynidir

### --help
- yardim alma icin kulaniliyor. Cok faydali. Asama asama her komutu bu sekilde gormek mumkun.
- docker image --help
- docker image rm --help

### docker container run --name ilkcontainer nginx:latest
- ilkcontainer isimli container olusturur.
- image registry'den imageí cekip container run edilir.
- layer layer cekti ve run etti.
- hash kontrolu yapti docker-hub ile
- lokale bakilir image icin once
- sonra registry'e bakar. default olan registry Docker hubt'tir. Ordan image'i cikar.
- Container'a ID verir.
- Container icindeki shell ana makinedeki shell'e baglar. Gelen mesajlari bu sekilde gorebiliyoruz.
- --name optionsi ya da flagi container'a isim verir.

### docker ls
- calisan containerlari gosterir.

### docker ls -a
- durudurulmus containerlari da gosterir.

### container calisma prensibi
- her container image'inda calismasi icin varsayilan olarak ayarlanmis bur uygulama vadir. Bu uygulama calistigi surece contaner calisir. Uygulama durdugunda container kapatilir. Burasi cok onemli.
- Docker image'in icinde birden fazla uygulama vardir.
- ayni adna birden fazla uygulama calistirabiliriz.
- ama Docker container run edildiginde sadece bir uygulama varsayilan olarak sonda calistirilabilir.
- Image'ta ayarlanmis varsayilan uygulama biz hicbirsey yapmadan run edersek calisir. Ama bunu degistirebiliriz.
- Ideal olan containerda tek uygulamanin calismasidir.

### docker container run -p 80:80 ozgurozturknet/adanzyedocker
- apache server'i calistiran bir image
- 80 portundan 80 portuna yonlendiriyor.
- ilk 80 portu hostunkidir. Ikinci 80 container portudur.
- server hep calistigi icin kapanmiyor.
- Container ID olusur. unique

### docker container logs containerID / containerName
- loglari gosterir.
- ID'nin ilk 3-4 harfini girsek de loglar gelir.
- container run edilirken --name kullanmazsak docker random bir isim verir.
- Durmus containerin loglarina bakmak mumkun.

### docker container run --name deneme ozgurozturknet/adanzyedocker java app1
- java app1 varsayilan olarak calisan uygulamanin degistirildigi kisimdir.
- varsayilan uygulama calistirilmaz bu sekilde.

### docker ps -a
- durmus containerlar dahil containerlari listeler

docker ps -a
CONTAINER ID   IMAGE                          COMMAND              CREATED         STATUS                     PORTS     NAMES
679240c26344   ozgurozturknet/adanzyedocker   "httpd-foreground"   6 minutes ago   Exited (0) 5 minutes ago             awesome_rhodes

### Arka planda  container calistirma detached modu
- docker container run -d -p 80:80 nginx:latest
- terminali bize birakir

### docker container rm containerID1 containerID2 - silme islemi
- calismayan containerlar silinir.
- calisanlari silmek icin durdurmak gerekir ya da -f optionsi kullanilir

### docker container rm -f containerID1 containerID2 - zorla silme islemi
- zorla siler

### docker container stop containerID containerID2 - container durdurma
- containeri stop eder.

### docker container exec -it websunucu sh - contianer'a baglanma
- image'larin icinde genelde en az bir shell bulunur.
- it: interaktif modta baglan. Terminal baglantisi kurmak icin
- i:interaktif, t:tty
- cikmak icin exit komutu kullanilir Linux ile ilgili.
- conatiner icinde calisan processleri yani servisleri gormek icin ps komutu calistirilabilir.
- container icinde PID degeri 1 olan uygulama calistigi surece container calistirilir.
- container kapatilinca volume yoksa hersey gider. Image icinde ne varsa o gelir.

/usr/src/myapp # ps
PID   USER     TIME  COMMAND
    1 root      0:00 httpd -DFOREGROUND
    8 daemon    0:00 httpd -DFOREGROUND
    9 daemon    0:00 httpd -DFOREGROUND
   10 daemon    0:00 httpd -DFOREGROUND
   99 root      0:00 sh
  105 root      0:00 ps
 
 ### Docker Katmanli Dosya Sistem Yapisi
 - Union file yapisi var. 
 - Once Base image kullanilir. alpine gibi. an alt katman budur.
 - uygulamami kopyaliyorum. Bu da sonraki katman COPY /mapp /hello.sh
 - CMD /myapp/hello/sh. Baska bir katman daha
 - Yukaridaki bu 3 katman Read/Only layerslaridir yani katmanlaridir.
 - Biz image'i run ettigimizde container yazilabilir katman olusturulur. Container (read/Write) Layer
 - Yapilan her degisiklik bu katmana yazilir. 
 - Image icindeki layerlar degismez.
 - Image icindeki katmanlar sanki tek bir katman gibi gozukur. Buna Union file yapisi denir.
 - Bu esneklik ve hiz kazandiriyor. Boyuttan da kazaniyoruz.
 - Katmanlar sayesinde her calistirilacak container icin ayri katmanlar olusturulmaz. 
 - Yani zaten bir kere download edilmis katmanlar bir daha indirilmez. Duplicate etmez.

 ### docker container prune
 - stop edilmis tum containerlari siler

 ### docker image ls
 - sistemdeki imageleri listeler

 ### docker image prune -a
 - tum imageleri siler
 - -a tamamini siler

 ### docker image pull alpine
 - docker hubtaki alpine image'ini ceker.

 ### Docker container Yasam suresi
 - Tum ayarlamalar image asamasinda halledilir.
 - Tek bir uygulama icin olusturulur.
 - Ana ugulama durdugunda container durur.
 - Containerda sorun varsa image asamasinda cozulur.
 - Containerlar tek kullanimliktir.

 ### Volume - Container Disi Veri Saklama
 - Container icindeki veriye ihtiyacimiz varsa kullanilir.
 - Container, Image gibi bir docker objectidir.
 - Varsayilan host makine ustunde kurulurlar.
 - Buluttada olusturulabilir . Ornegin AWS EBS'te de tutulabilir.

 ### docker volume create ilkvolume
 - volume olusturur.

 ### docker volume inspect ilkvolume
 - ilkvolume volume'u hakkinda bilgileri getirir.
 - Mountpoint volume'in nerde olusturuldugunu gosterir.

 [
    {
        "CreatedAt": "2023-06-13T12:34:17Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/ilkvolume/_data",
        "Name": "ilkvolume",
        "Options": null,
        "Scope": "local"
    }
]

### docker container run -it -v ilkvolume:/uygulama alpine sh
- -v 'den sonra olusturulmus volume ismi
- : 'den sonra container icinde baglamak istedigimiz klasorun ismi. Bu ornekte uygulama
- alpine image'ndan sh komutu calistirilacak
- o klasor yoksa otomatik olusturulur.
- volume daha sonra baska image ile de olusturulabilir. Ayni anda iki container ayni volume'a baglanabilir.

###  ilkvolume:/uygulama:ro
- read only baglanma. sadece okuma yapabilir.

### Bos-Dolu Volume Davranislari
- Olusturulmus bos volume container icinde olmayan bir klasore baglanirsa o klasor container icinde olusturulur. Bu durumda. Bu durumda volume icinde birseyler varsa container icinde de o klasor olusturulur.
- Eger bir volume imaj icerisnde bulunan mevcut baska bir klasore mount edilmisse 
  1. Klasor bossa o anda volume icerisinde hangi dosyalar varsa bu klasorde de o dosyalari gorursunuz.
  2. Klasorde dosya varsa ve volume bossa bu sefer o klasordeki dosyalar volume'a kopyalanir.
  3. Klasorde dosya var ya da yok fakat volume'da dosyalar varsa yani volume bos degilse, bu sefer siz o klasorun icerisinde volume'da ne dosya varsa onu gorursunuz.


### docker container run --rm -it alpine sh
- container olusturulduktan sonra siler. Stop edildiginde yapar bunu.
- container'a baglanir.

### Bind mounts
- Production ortamlar icin mutlaka volume kullanilmalidir.
- Hosttaki bir klasoru container icindeki mount islemine bind mount denir.
- Lokal development icin cok kullanisli.
- Web sitesi uzerinde calisirken her degisikligin hemen yansimasi icin kullanilabilir.

### docker container run -d -p 80:80 -v /home/erdogan/myapp:/usr/share/nginx/html nginx
- hosttaki /home/erdogan/myapp klasorunun icindekileri container icindeki /usr/share/nginx/html mount ettik. 
- hosttaki klasordeki degisklikler container calisirken otomatik yanisr. Development icin cok tatli.
- Bunu lokalde development yaparken kullanmak lazim.

### Docker Plugin-Driver Sistemi
- Moduler bir dizayni var.
- Parca parca ozellik eklenmesi mumkun.
- Storage, log, secrets network icin plugin imkani var.
- docker info komutunun icinde plugins icinde dockerin varsayilan olarak sagladigi pluginsleri gorebilirsiniz. Bunlari degistirmek mumkun. Bunu driver yapisi sayesinde yapariz.

### Docker Network Driver
- Varsayilan olarak 5 driver var.
- Bridge, Host, Macvlan, None, Overlay
- Bridge: varsayilan networktur. Bir network olusturur ve bu network uzerinden router mantigiyla haberlesme yapilir. 
- Host: containerin dogrudan arada hicbirsey olmadan host ile iletisim kurmasidir. Her sistemde host driver ile yaratilmis Host adinda bir network bulunur.
- MacVlan: containerlara mac adersi vererek ayri birer cihaz gibi davranilabilir. Bu sekilde fiziksel aglara baglanabilirler.
- None: Containerin ag baglantisinin olmamasini istersek bunu kullaniriz.
- Overlay: Docker swarm ile ilgilidr. Ayri Hostlar ustunde farkli containerlar calisiyormus gibi calismasi istendigi zaman kullanilir.

### docker network ls
= Docker Network Objelerini gosterir

PS C:\Users\User> docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
b2b1ab6748e9   bridge    bridge    local
e8ab51795f3d   host      host      local
394fb158f659   none      null      local

### docker network inspect bridge
- bridge objesi hakkinda bilgileri getirir.
- subnet ve gateway IP bilgileri var.

### docker image inspect imageName
- spesifik image ile ilgili bilgileri getirir.

### docker container inspect containerID / containerName
- spesifik conatiner ile ilgili bilgileri getirir.

### container olusturup IP bilgilerine ifconfig komutu ile bakma
- 172.17.0.2 bi containerin IP adresi.
- lo kismi local adresi gosterir.

/usr/src/myapp # ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:AC:11:00:02
          inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:696 (696.0 B)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

### Bridge
- docker sisteme yukledigimizde 3 adet network objesi kurulur. bridge, none ve host 
- dokcer0 adinda sanal network interface yaratir ve ona 172.17.0.0 IP adresini verir. Container icinden gonderilecek seyler host ustundeki eth0 sanal network interface'e gonderilir. Ordan da dis dunyaya acilir. eth0 IP adresi 192.168.0.2 olur genelde.
- Ayni bridge networkune bagli containerlar birbirleri ile haberlesebilirler. Direkt IP adreslerine ping atmak mumkun.

### Control + P + Q
- contaier icinden cikar containeri kapatmadan.

### Host
- docker container run -it --name deneme1 --net host nginx sh
- host networku ile container olusturduk.
- ifconfig ile baktigimizda hostun adapterlaerini kullanilir. hostun Iplerini gorururz.

### None
- Sadece local adresini gorursunuz. conatiner icinde. dosariya baglanti olmaz.

### Network and ports
- host ve conatiner arasindaki network docker'a ait bridge network tarafindan gerceklestirilir.
- bridge network 172.17.0.0/16 network IP adresine sahip. Gateway ise 172.17.0.1 IP adresine sahip. Gateway tarafi host ile container arasindaki alisverisi yonetir.
- containerlar ise 172.17.0.2'deb baslayarak IP adresleri alirlar. 
- Host'un IP adresi ise duyelimki 192.168.1.10 olsun. buraya gelen istekler brdige networke ordan containera gider.
- spesifik containera disaridan yani Host'un adresinden ulasabilmek icin ise portlar kullanilir.
- -p ya --publish optionslar kullanilir bunun icin.

### docker container run -d --publish 8080:80 -p 8043:43 nginx
- -p host_port:container_port 
- birden fazla port yonlendirmesi yapabiliyoruz.
- default olarak port publishing tcp protoklunu kullanir.

### udp protokolunu kullanarak port acma
- docker-container run -d -p 53:53/udp nginx

### Network objeleri
- Kendi network objeleri olusturabiliyoruz.
- Yeni bridge networkler olusturabiliriz.
- bazi containerlar birbirini gormesini istemiyorsak izolasyon saglayabiliriz.
- farkli subnet ihtiyacimizi da karsilayabiliriz.
- default bridge networkunde DNS hizmeti yok. Kendi bridge networku olusturulursa container isimler uzerinden ulasmak mumkun.
- container network baglantisini defaul bridge'te kesmek mumkun degil.

### ping websunucu1
- ping atma
- default brdige'te bu isimle ulasmak mumkun degil IP ile ulasmak zorundayiz.

### docker network create kopru1
- kendi bridge networkumuzu olusturma
- varsayilan olarak bridge network kurulur.
- Subnet 172.18.0.0 / 16
- Gateway 172.18.0.1
- 17 - 18 oldu

### docker network inspect kopru1
- olusturdugumuz networkun bilgilerine ulasma IP falan.
- containers kisminda bagli containerlari gorme mumkun

### docker network create kopru2 --driver host
- host networku kurar.

### docker cotainer run -dit --name websunucu --net kopru1 ozgurozturknet/adanzyedocker sh
- container icine baglanmaz. acik bir sekilde bekler. istedigimiz zaman baglanabiliriz

### docker cotainer run -dit --name database --net kopru1 ozgurozturknet/adanzyedocker sh
- container icine baglanmaz. acik bir sekilde bekler. istedigimiz zaman baglanabiliriz

### docker attach websunucu
- -dit ile actigimiz websunucu isimli container'a baglanma.

### ping database
- kendi networkumuzde isimle haberlesebildik.

### Subnet ve Ip adreslerini kendimiz belirleme
- docker network create --driver=bridge --subnet=10.10.0.0/16 --ip-range=10.10.10.0/24 --gateway=10.10.10.10 kopru2
- subneti gatewyi ve container IP araligini biz verdik
- ip range ve gatewayi tanimlamasaydik da otomatik subnete gore IP degerleri verilecekti. 

### containerlar calisirken baska bir networke baglanma
- docker network connect kopru2 database
- Bu olay defaul bridge'te olmaz.
- bir container birden fazla networke baglayabiliyoruz.

### docker network disconnect kopru2 database
- baglantiyi kaldirma

### docker network rm kopru1
- baglantiyi silme

### docker network rm -f kopru1
- aktif kullanilan baglantiyi silme

### Logging
- Linuxta /var/log kalsoru altinda loglar tutulur. sistem ile ilgili loglar orda.
- Ornegin nginx var/log/nginx klasoru altiunda tutar. access.log error.log
- conatinerlardaki loglar docker logs komutu ile ulasilir.

### STDIN. STDOUT ve STDERR
- klavyeden birseyler yazdiniz. Bu giris calistiginiz uygulamanin stdin akisina gider ve uygulamaya gonderilir. Uygulama cevabi da stdout cikisina gonderilir. Terminal bu cikisi gozledigi icin bize gosterir. Hata varsa uygulama stderr cikisna yollar. 
- Uygulamalar ve linux komutlari, girdileri stdin alip stdou ve stderr cikisina atar
- Loglari yakalayabilmek icin uygulamanin stderr ve stdout cikislari kullanmasi gerekir.

## docker logs conatinerName / conatinerID
- container loglarini gorme