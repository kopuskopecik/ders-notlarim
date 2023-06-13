### systemd
- systemd, modern Linux dağıtımlarında yaygın olarak kullanılan bir sistem ve hizmet yöneticisidir.
- en kucuk birimine unit denir.
- Paralel Başlatma: systemd, sistem başlangıç sürecini paralel olarak yürütme yeteneğine sahiptir. Bu, işletim sisteminin daha hızlı başlamasını sağlar, çünkü sistem kaynaklarını daha etkin bir şekilde kullanır.

Birim Yönetimi: systemd, hizmetlerin ve sistem bileşenlerinin "birim" adı verilen yapılarla yönetilmesini sağlar. Her birim, bir hizmet veya sistem bileşeni için yapılandırma ve kontrol bilgilerini içerir. Bu birimler, sistem başlangıcında veya istendiğinde otomatik olarak başlatılabilir, durdurulabilir veya yeniden başlatılabilir.

Gelişmiş Günlük Kaydı: systemd, geniş bir günlük kayıt sistemi sunar. Günlükler, hizmetlerin, olayların ve sistem durumunun daha ayrıntılı bir şekilde izlenmesine ve hataların tespit edilmesine yardımcı olur.

Daha İyi Sistem İzleme: systemd, sistem kaynaklarını (CPU, bellek, disk kullanımı vb.) izlemek ve yönetmek için gelişmiş yeteneklere sahiptir. Bu sayede sistem performansı daha iyi izlenebilir ve gerektiğinde sorunları tespit etmek için kullanılabilir.

Cgroups Desteği: systemd, kontrol grupları (cgroups) adı verilen Linux çekirdek özelliğini kullanır. Bu, sistem kaynaklarının daha iyi bir şekilde tahsis edilmesini ve izlenmesini sağlar.
### Systemctl
- systemd uzerindeki servisleri yonetmemize yarayan tooldur.

### sudo systemctl start nginx.service
- nginx servisini baslatir

### sudo systemctl stop nginx.service
- nginx servisini durdurur.

### sudo systemctl restart nginx.service
- nginx servisine restart ceker

### sudo systemctl reload nginx.service
- sistemi durdurmadan tekrar yukler

### sudo systemctl enable nginx.service
- her acilista otomatik calismasini saglar

### sudo systemctl disable nginx.service
- enable ozelligini disable yapmak icin kullanilir

### systemctl list-units
- aktif olan servisleri listelemek icin kullanilir.

### systemctl list-units --all
- aktif olan olmayan hepsini gosterir.

### systemctl list-unit-files
- yuklenmis tum unitlerin listesi

### journald
- bir systemd compenentidir.
- servislerdeki tum loglari toplar.

### journalctl
- eskiden yeniye dogru tum loglari gosterir sistemdeki.

### journalctl -b
- sistem bastan sona acilana kadar ki yani boot edilene kadar ki loglari gosterir.

### journalctl -k
- sadece kerne mesajlari icin

### journalctl -k -b
- boot ve kernel beraber

### systemctl status nginx.service
- This will show you whether the unit is active, information about the process, and the latest journal entries:

### journalctl -u nginx.service
- loglari getirir

### journalctl -b -u nginx.service
- boot edilirken olusan loglari getirir nginx icin

### unit files
- unitler mesela nginx bazi parametrelere sahiptir. Bu parametreler systemd tarafindan uniti yonetmek icin kullanilir. 

### systemctl cat nginx.service
- yukarida bahsedilen parametreleri gormek icin

[erdogan@ip-172-31-15-29 ~]$ systemctl cat nginx.service
# /usr/lib/systemd/system/nginx.service
[Unit]
Description=The nginx HTTP and reverse proxy server
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
# Nginx will fail to start if /run/nginx.pid already exists but has the wrong
# SELinux context. This might happen when running `nginx -t` from the cmdline.
# https://bugzilla.redhat.com/show_bug.cgi?id=1268621
ExecStartPre=/usr/bin/rm -f /run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
KillSignal=SIGQUIT
TimeoutStopSec=5
KillMode=mixed
PrivateTmp=true

[Install]
WantedBy=multi-user.target

### systemctl list-dependencies nginx.service
- unitin calismasi icin gereksinimler
- systemd bunlari calistiri unit start edildiginde

### systemctl list-dependencies --all nginx.service
- daha ayrintili gosterir tree seklinde.

### systemctl show nginx.service
- tum parametreleri gosterir systemd tarafindan kullanilan

### sudo systemctl edit nginx.service
- unit fileí edit etmek iicn kullanilir.

### sudo systemctl edit --full nginx.service
- tum unit fileí edit etmek icin

### sudo systemctl daemon-reload
- degisikliklerin yansimasi icin

### target kavrami
- systemd'in hedefler (targets) olarak adlandırılan bir kavramı vardır. Hedefler, systemd'in başlangıç sürecini kontrol etmek ve sistemdeki hizmetlerin başlatılmasını ve durdurulmasını yönetmek için kullanılan birimlerdir. Hedefler, belirli bir sistem durumunu temsil eder ve ilgili hizmetlerin bu duruma geçişini sağlar.

Her hedef, sistemdeki belirli bir çalışma durumunu veya sistem işlevselliğini temsil eder. Örneğin, "multi-user.target" hedefi, kullanıcıların oturum açabildiği ve çoklu kullanıcılı bir çalışma ortamının olduğu bir durumu temsil eder. "graphical.target" ise grafik tabanlı bir masaüstü ortamının başladığı hedefi ifade eder.

systemd, Linux sisteminin farklı durumlarında (başlangıç, kapanış, hibernate vb.) farklı hedeflerin kullanılmasını sağlar. Sistem başlatma sürecinde, varsayılan olarak "default.target" hedefi kullanılır ve diğer hedeflere geçiş yapar. Örneğin, "multi-user.target" hedefine geçiş yaparak, çoklu kullanıcı moduna geçiş yapılır ve sistem hizmetleri bu hedefe göre başlatılır.

### systemctl list-unit-files --type=target
- sistemde tanimli targetlari gosterir.

### systemctl get-default
- default targeti gosterir.

### sudo systemctl set-default multi-user.target
- default targeti degistirir

### systemctl list-dependencies multi-user.target
- targeta hangi unitlerin bagli oldugunu gosterir.

### sudo systemctl isolate multi-user.target
- targetin icindeki unitleri durdurur.

### sudo systemctl poweroff
- sistemi kapatir.

### sudo systemctl reboot
- sistemi kapatir yeniden acar.

### sudo systemctl rescue
- sistemi kurtarma calistirilir. 