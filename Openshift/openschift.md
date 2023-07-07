### oc get pod
- podlari listeler
- podlar uc asamali gosterilir.
- build, deploy ve running seklinde. Kubernetesten farkli.
- build kisminda image olusturuluyor ve push ediliyor openshift icindeki repisotorye

### oc get svc
- servisleri listeler

### Dinlenen portlar
- servis olusturuken port ayri olarak belirtilmezse proje olusturulurken otomatik olarak 8080. 8778, 9779 gibi portlardan dinleme ve yonlendrime yapar.

### oc edit svc/serviceName
- servisi edit etme
- otomatik etkiler

### oc get route
- Disariya acilmis endpointleri listeler
- ozellikle frontend icin
- Disari acilsa bile service tipi hala ClusterIp degisik.

### oc expose svc/serviceName
- servisi disariya acma

### oc edit route/routeName
- route objectini edit ederek yonlendirilen portu degistirmek mumkun 

### oc projects
- projeleri listeler
- aktif olan projenin ustunde yildiz isareti bulunur. *

### oc new-app --name appName githibRepoUrl#develop
- yeni app olusturma proje icinde
- develop branch ismi
- eger branch ismi belirtilmezse otomatik olarak main branchinden cekecektir.
- strategy belirtilmezse Dockerfile'li baz alarak deployment yapar. source kodtan da yapmak mumkun

### Dockerfile
- eger Dockerfile icinde port expose edilmis ise Openschift bunu gorup servisi o portta ayaga kaldirir. Guzelmis. Default olan 8080'da ayaga kaldirmaz.

### Network
- route edilerek disariya acilan bir servise disaridan erisilmeye calisildiginda openschift gateway uzerinden ilgili servise ulasilir.
- icerden haberlesme durumunda ise dogrudan servis uzerinden iletisim saglanir.

### Elements of Template
- Buildconfig: Image'in dockerfile'dan mi source kodtan mi yoksa hazir dockerhub gibi bir yerde imageten mi build edileceginin ayarlandigi yer.
- ImageStream: Image'in kaydedilip pushlanacagi yer
- DeploymentConfig: pod ozelliklerinin vesaire belirlendigi kisim
- Service: Service kismi
- Route: disariya acilacak mi?
- PersistentVolumeClaim: Zaten biliyoruz dimi.
- Parameters: Template'i dinamik yapip tekrar tekrar kullanabilmek icin kullanilir.

### oc - openschif client
- operating sisteme gore bilgisayara yuklemek lazim. 
- Ardindan opneshicft sandboxtan alinan token bilgileri ile openshift clusterimiza cli'dan baglanmak mumkun.

### oc login --token TOKEN --server=URL
- oc cli'ya baglanma

### oc project ProjectName
- project gecisi

### oc get all
- bulunan project icindeki podlari, servisleri, route'lari herseyi getirir.

### oc get template
- templateleri listeler

### oc create -f templateName
- template'i project icinde olusturur yani aslinda ekler run etmez.

### oc describe templateName
- template hakkinda bilgileri getirir.

### oc new-app --template templateName -p BRANCH_NAME=quay -p ...
- template icindeki objectleri olusturur.

### oc delete template docker-template
- template ile olusturulan objectleri silme

### oc logs -f podName
- loglari canli listeler

### volume claim olusturma
- template ile olusturmak mumkun
- farkli iki app ayni volume'u kullanabilir.

### oc cp lokalFile podName:/tmp/quotes
- lokalden pod icinde dosya kopyalama

### oc rsh -t Podname
- poda baglanma

### oc status
- applicationlarin son durumunu gosterir. build, deploy tum asamalar.

### oc get pods -w
- podlarin durumunu canli gosterir. 

### oc logs -f bc/hello1
- build loglarini getirir.
- bc = build configuration

### oc get all -l app=hello1
- labeli hello1 olan tum objectler gelir. 

### oc delete all -l app=hello1
- labeli hello1 olan tum objectleri siler.

### dc
- deployment configuration

### oc get pods --no-headers
- basliklari kaldirarak podlari listeler

### oc get pods --no-headers -l owner=tech-tejendra
- spesifik poda ulasmanin bir tolu olabilir.

### oc get pods --no-headers -l owner=tec-tejendra -o custom-columns=POD:.metadata.name
- podun ismini getirir.

### oc logs -f $(oc get pods --no-headers -l owner=tec-tejendra -o custom-columns=POD:.metadata.name)
- istedigin podun loglarini getirir.

### oc describe bc hello1 - github webhook kismi
- burda github webhook urlini bulmak mumkun
- generic olani aldi tejendrarana
- build configte secret kismi var. github urle verebilmek icin.
- ardindan githubta webhook kisminda bunu veriyorsun.
- githubda content type'i json yapti.

### oc whoami
- oepnshifte hangi modta baglandigini gosterir.
- developer, admin gibi

### oc delete projectName
- icindeki herseyi siler
- project aslinda namespace demek
- bu kodu Chart.yaml dosyasinin oldugu yerde calistiermak gerekiyor.

### oc set probe deployment DeploymentName --readiness --get-url=URLAdress --initial-delay-seconds=2 --timeout-seconds=2
- readiness probe'u var olan deploymenta sonradan ekleme
- kontrolun durumuna gore ilgili podu servise ekler ya da eklemez.

### oc set prob --help
- komut hakkinda bilgi verir.

### oc set probe deployment DeploymentName --liveness --get-url=http://:8080/healty --initial-delay-seconds=2 --timeout-seconds=2
- liveness ekleme
- kontrol basarili degilse pod tekrar baslatilir. Basarisizsa crashloopbacke duser.