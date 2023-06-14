# Docker
- 2013 senesinde Docker ortaya cikti.
- Gemi limanlarinda konteynir indiren bindiren kisisler demek.
- Go dili ile yazildi.
- 2016 windows destegi geldi.

### Bilgisayar Parcalari
- CPU:
- RAM: ustunde gecicic olarak bilgi tutmak ve CPU'ya aktarir.
- BIOS: Basic Input- Outout System, bir yazilim. Bilgisayar acildiginda diger donanimlari islemciye tanitir. Ayrica isletim sistemi baslangic ogelerinin HDD, CD-ROM gibi suruculerden yuklanmesini saglar.

### Kernel
- Isletim sistemi 3 bilesenden olusur
- Kernel, kullanici ara yuzu ve uygulamalar.
- BIOS bilgisayar acildiginda boot loader dedigimiz bit uygulamayi yukler. bu da kerneli ekler yani cekirdegi. Donanim ile calisan uygulamalar arasinda bir katmandir. Donanimi yonetmektir. Uygulama Kernelle iletisime gecer. Bu kismi kernel halleder. operating systemin kalbidir.

### Virtulization - Sanallastirma
- Sunucu hizmet saglayan yapi.
- Istemci hizmeti kullanan yapi.
- amac uygulmalari izole bir sekilde calistirmak.
- ayni bilgisayar icinde birden fazla isletim sistemi kurulan yapidir. 
- sanallastirma yazilimi ustune isletim sistemleri kullanilir. (hypervisor)
- amac farkli uygulamalari farkli isletim sisteminde calistirmak.
- amac kaynaklari verimli kullanmak.
- her bir uygulama icin ayri isletim sistemi kuruldugu icin aslinda o kadar da efektif degil. Cunku isletim sistemleri de bir kaynak tuketiyor.
- yonetmesi de zor.

### Container
- Linux cekirdegi uzerine arayuz ve programlar ekleyip paketlersen buna distro deniyor. Redhat, Debian, Centos gibi.
- namespaces eklendi cekirdege. Processleri izole etme ozelligi geldi.
- control groups eklendi. processeslerin kaynak tuketimini kisitlamayi sagliyor temelde.
- containerlar izole bir sekilde uygulamalar calistirabilir. Kendi kerneli yoktur. Yuklu olduklari operating sistemin kernelini kullanirlar. 

### Docker Engine
- Docker daemon, Rest API ve Docker CLI'dan olusur.
- Docker daemon: Ana yonetim merkezi.
- Rest API: Dockwer CLI ile daemon arasinda iletisim saglanan kisim.
- Docker CLI: Disardan Docker daemonu yonetmemizi saglar. Baska bir bilgisayardan da yonetebilirsin farkli bir yerde yuklu olan bir dockeri.
- conatiner, image, data volume ve netrwork ile docker CLI ile iletisim kurar.
- Iki tip Engine vardir.
- Docker Engine Enterprise: Bazi guvenlik onlemleri var. Musteri hizmetleri falan var.
- Docker Engine Community: Ucretsiz her zaman kullandigimiz versiyon. Mirandes firmasina satildi.
- Docker daemon linuxta calisir.

### Image ve Container nedir?
- Uygulamanin paketlenmis halidir. Icinde kernel yoktur. Ihtiyac yoktur. Bir yerde depolanabilir. Bu image calistirdigimizda container olusur.
- Docker-hub imagelarin depolandigi yerlerden biri. gitlabin da var awsin de var. azure'in da var.

### Container ve Sanal Makine - Virtual Machine Farki
- Container bir tek isletim sistemi ile calisir. Kendi icinde isletim istemine ihtiyac duymaz.
- Sanal Makine ise hypervisor yazilimi ile birden fazla isletim sistemini tek bir bilgisayar uzerine kurulur.
- Containerlar daha hizli calisir.
- paketleme isi containerlarla daha kolaydir.

### Windiws Containers
- 2016 yilinda hayatimiza girdi.
- Kullanim bakimindan buyuk farklar yok.

### Docker Versiyonlari
- Windows ve Mac icin bazi linux sanal makine ve baziprogramlari yukler docker kullanabilmek icin.
- Linux icin Docker Engin CE
- Windows icin Docker Desktop for Windows
- Mac icin Docker Desktop for Windows windows 10 icin
- Windows 7-8 ve 10 Home icin Docker Toolbox kurulmalidir.
- her yedi ayda bir major versiyon cikarir community olan.

### Docker Hub
- Imagelarimizi burda depolyabiliyoruz private ve public olarak.
- Docker varsayilan olarak buraya bakar.
- Resmi image'lar burda tutulur.
- Bir tane private image saklamamiza izin verir. Sonrasi parali.
- Public bir cloud servisidir.

### Docker CLI
- CLI Rest API ile docker daemon ile iltisim saglar.
- Asil isi yapan docker daemondir.
- Bir takim ayarlar yaparak cloudtaki bir docker daemon'i da yonetebiliriz. 