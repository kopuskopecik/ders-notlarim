### docker version
- docker versiypnunu gosterir.
- dockerín calsitigini anlariz.

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
- Ideal olan containerda tek uygulamanin calsimasidir.

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
 - Biz image'i run ettigimizde co0ntainer yazilabilir katman olusturulur. Container (read/Write) Layer
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
 - dokcer hibtaki alpine image'ini ceker.

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
 - volume olustururu.

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
