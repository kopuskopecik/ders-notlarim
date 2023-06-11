###  cat /proc/filesystems
- kernelin destekledigi file sistemlerini listeler.

### inode number
- metadatakar ozel yapilar icinde tutulur. Bunlara inodes denir. inode number ile tanimlanirlar. 

### ls -li
- inode numberlar ile beraber listeler

luke@tatooine:~$ ls -li
786458 drwxrwxr-x 2 luke luke 4096 Apr 23 23:43 bin
664485 -rw-rw-r-- 1 luke luke   25 Apr 25 17:29 content
786460 drwxrwxr-x 2 luke luke 4096 Apr 24 00:19 course
664640 drwxrwxr-x 2 luke luke 4096 May  3 17:00 hello

### stat app.py
- inode un icerigini gormek icin kullanilir.
- Besides the owner (uid), the group (gid), permissions (access), number of links (links) and file type (regular file), you can see 3 different time stamps.

luke@tatooine:~$ stat content
  File: content
  Size: 25        	Blocks: 8          IO Block: 4096   regular file
Device: fc02h/64514d	Inode: 664485      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/    luke)   Gid: ( 1000/    luke)
Access: 2020-05-01 15:26:17.606161506 +0200
Modify: 2020-04-25 17:29:17.662325092 +0200
Change: 2020-04-25 17:29:17.662325092 +0200
Birth: -

### Links
- klasorler de aslinda ozel dosyalardir. Onlarin da inode numberslari vardir. 
- isimler inode numberlara eslestirilir. Buna link denir. hardlink 
- ayni klasor icindeki farkli isimler ayni inode number degerine eslestirilebilir.
- ayni isimler farkli klasorlerde olabilir.
- ayni inode degerine sahip farkli isimli dosyalar ayni metadata degerlerine dahiptir. permission isim degistirme gibi bir islem yaptiginda bu durumdaki dosyalar icin hepsi etkilenecektir ayni sekilde.
- dosya silindiginde ise diger dosyalar silinmez. Metadata icindeki link sayisi azalir.

### ln
- link olusturmak icin kullanilir
- ln source [destination]
- eger ayni klasor icinde linkleme yapacaksaniz baska bir isim verebilirsiniz destination olarak
- eger farkli bir klasorde olacaksa ayni ismie kullanabilirsiniz

### softlinks - symbolic links or symlinks 
- asagidaki lsmod bir symlinktir. file typeina bakarsaniz l karakteri var.
- kmod'u isaret ediyor. bu yuzden file size i 4 bytes.
- owner ve permissonlar alakasiz.
- kendi owner ve permissonlari etkin
- link sayisi 1


luke@tatooine:~$ ls -li /bin | sort -nrk3 | head
524329 -rwxr-xr-x 3 root root   34888 Jul  4  2019 bzip2
524329 -rwxr-xr-x 3 root root   34888 Jul  4  2019 bzcat
524329 -rwxr-xr-x 3 root root   34888 Jul  4  2019 bunzip2
524443 -rwxr-xr-x 2 root root    2301 Apr 28  2017 uncompress
524443 -rwxr-xr-x 2 root root    2301 Apr 28  2017 gunzip
535408 lrwxrwxrwx 1 root root       4 Mar 11 20:37 lsmod -> kmod
534653 -rwxr-xr-x 1 root root   30800 Mar  5 18:23 wdctl
534652 -rwxr-xr-x 1 root root   14408 Mar  5 18:23 mountpoint
534651 -rwxr-xr-x 1 root root   38952 Mar  5 18:23 more
534645 -rwxr-xr-x 1 root root  149688 Mar 11 20:37 kmod

### ln -s source [destination]
- symlink olusturmak icin kullanilir
- symlink herhangi bir path, dosya, olmayan bir dosya ya da devicea baglanabilir.
- inode numberlari farkli olur

### readlink hello.py
- nereye bagli oldugunu gosterir.

### Hardlinks vs Symlinks

#### Hardlinks                  #####  Symlinks
- Created with ln                 - Created with ln -s
- Maps a name to an inode         - Maps a name to a path
- Cannot cross devices            - Can point anywhere, even to non-existing paths
- All links have the same owner   - The owner / permissions / file content of the linked file take effect.
/ permissions / file content     

###  UID and GIDs
- user idler /etc/passwd 
- grup idler GIDs /etc/group la eslestirilmistir Linuxta

### chmod
- chmod [options] mode files_or_directories
- mode u belirlemenin 2 yolu var. symbolic ve octal number
- symbolic subject, operation ve bir ve ya birden fazla permissiondan olusur.
- subject: u the owner, g grup, o other, a all - default
- operation: + ekleme permission, - kaldirma permission, =  direk set etme permission
- permissons: r read, w write ve x execute

luke@tatooine:~$ ls -l hello.sh
-rw-rw-r-- 1 luke luke 0 May 12 21:56 hello.sh
luke@tatooine:~$ chmod g-w hello.sh
luke@tatooine:~$ ls -l hello.sh
-rw-r--r-- 1 luke luke 0 May 12 21:56 hello.sh
luke@tatooine:~$ chmod a+x hello.sh
luke@tatooine:~$ ls -l hello.sh
-rwxr-xr-x 1 luke luke 0 May 12 21:56 hello.sh

- sayilarla oktal olarak permissonlari verme.
- bu ilk basta zor gibi ama bir alisinca digerini kullanmiyorsun
- 4 read, 2 write. 1 execute

### A normal directory:
chmod 755 stuff/
ls -ld stuff/
drwxr-xr-x 2 root root 4096 May 12 22:20 stuff/

### A private directory:
chmod 700 .ssh/
ls -ld .ssh/
drwx------ 2 root root 4096 Apr 21 21:36 .ssh/

### A normal file:
chmod 644 README
ls -l README
-rw-r--r-- 1 root root 0 May 12 22:21 README

### A script (needs execute and read permissions):
root@tatooine:~# chmod 755 hello.sh
root@tatooine:~# ls -l hello.sh
-rwxr-xr-x 1 root root 11 May 12 22:23 hello.sh

### chown or chgrp
- owner ya da grupu degistirmek istedigimizde kullanilir
- chown newowner file_or_directoy
- chgrp newgroup file_or_directoy
- chown newowner:newgroup file_or_directoy
- ownershipligi sadece root degistirebilir
- eger dosyanin sahibi iseniz yalnizca grubu degistirebilirsiniz.

### bazi komutlar
- i ya da a harfi, insert modunu acar cursordan sonra
- I: baslangica eklemek icin
- A: sona eklemek icin
- o: bos satir eklemek icin
- Esc: commanda gecmek icin
- :wq: kaydeder ve cikar
- :q kaydetmeden cikar
- :q! : kaydetmeden zorla cikar

### vimtutor
- vim ile ilgili bir tutorial

### umask
- varsayilan olarak verilen permisson degerini gormek ve ayarlamak icin kullanilir.
- $ umask
- $ umask 0022
- Yukarıdaki komut, yeni bir izin maskesi olarak 0022'yi ayarlar. Bu, dosya ve dizinlerin varsayılan olarak 644 (rw-r--r--) izinlerine sahip olacağı anlamına gelir.

### specila file permission
- SUID and SGID ('set user id' and 'set group id') bu set edildiginde calistirilan program, sanki o programin sahibi gibi calistrilir. sudo mesela
- /etc/shadow user sifreleri burda tutulur.

luke@tatooine:~$ ls -l /usr/bin/sudo
-rwsr-xr-x 1 root root 149080 Jan 31 18:18 /usr/bin/sudo

### SUID (Set User ID): 
SUID, bir dosyanın yürütülebilir olması durumunda, o dosyanın sahibinin haklarını geçici olarak değiştirme yeteneğini ifade eder. Bu durumda, dosya o sahibin yetkileriyle çalışır. Örneğin, bir dosyaya SUID özelliği verildiğinde, dosya kullanıcı tarafından çalıştırıldığında geçici olarak dosyanın sahibinin yetkilerini alır. Bu, belirli bir kullanıcının, normalde o kullanıcının yapma hakkına sahip olmadığı işlemleri gerçekleştirmesine olanak sağlar. SUID genellikle sistem programlarında kullanılır.

### SGID (Set Group ID): 
SGID, bir dosyanın yürütülebilir olması durumunda, o dosyanın grup kimliğini geçici olarak değiştirme yeteneğini ifade eder. Bu durumda, dosya o grubun yetkileriyle çalışır. Örneğin, bir dizine SGID özelliği verildiğinde, dizine yeni dosyalar ekleyen kullanıcılar, eklenen dosyaların otomatik olarak dizinin grubunun kimliğine sahip olmasını sağlar. SGID, dosya paylaşımı ve işbirliği gerektiren ortamlarda sıkça kullanılır.

### Sticky Bit: 
Sticky Bit, genellikle paylaşılan dizinlerde kullanılan bir izin özelliğidir. Bir dizine Sticky Bit uygulandığında, sadece dosya sahibi veya kök kullanıcı, o dizindeki dosyaları silme yetkisine sahip olur. Diğer kullanıcılar, kendi dosyalarını silemezler. Bu özellik, çok kullanıcılı sistemlerde veya kamu bilgisayarlarında kullanıcıların birbirlerinin dosyalarını silmesini önlemek için kullanılır. Ayrıca, /tmp gibi geçici dosya dizinlerinde geçici dosyaların güvenliğini sağlamak için de kullanılabilir.

### passwd
- sifre degistirmek icin kullanilir
- sifre degistirme biti x degil s dir asagida oldugu gibi.

luke@tatooine:~$ type passwd
passwd is /usr/bin/passwd
luke@tatooine:~$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd

### /etc/sudoers
- roota tum yetkilerin verildigi dosya

###  SUID, SGID, and Sticky bit yetkileri verme
- 4: SUID, 2 SGID, 1 Sticky Bit
- Numeric ornekler
chmod 1775 dirName
chmod 3755 dirName
- sembolik ornekler
chmod g+s dirName
chmod u+s dirName
chmod g+t dirName
- chatgpt cok guzel ornekler veriyor bunlar icin

### Disks and Partitions
- bircok disk parcalara ayrilmis durumdadir.
- bu parcalar bir tabloda bulunur
- cat /proc/partitions komutu ile parcalari gormek mumkun. 
- lsblk /dev/vda 
- b block device'i temsil eder.

root@tatooine:~# cat /proc/partitions
major minor  #blocks  name
   7        0      96032 loop0
   7        1      96176 loop1
 252        0   14680064 vda
 252        1       1024 vda1
 252        2   14676992 vda2

 root@tatooine:~# lsblk /dev/vda
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
vda    252:0    0  14G  0 disk
├─vda1 252:1    0   1M  0 part
└─vda2 252:2    0  14G  0 part /

luke@tatooine:~$ ll /dev/vd*
brw-rw---- 1 root disk 252, 0 May  5 09:52 /dev/vda
brw-rw---- 1 root disk 252, 1 May  5 09:52 /dev/vda1
brw-rw---- 1 root disk 252, 2 May  5 09:52 /dev/vda2

### Raw devices
- Raw device, genellikle donanım cihazlarından ziyade işletim sistemi düzeyinde bir kavramdır. Raw device, işletim sistemi tarafından yönetilen bir depolama aygıtının düşük seviye erişimini ifade eder. Raw device, verilerin dosya sistemi olmadan doğrudan depolama aygıtına yazılması ve okunması anlamına gelir.

- Birçok depolama aygıtı, işletim sistemi tarafından bir raw device olarak kullanılabilir. Örneğin, sabit diskler, SSD'ler, CD/DVD sürücüleri, USB bellekler, RAID dizileri vb. raw device olarak kullanılabilir. Raw device, bu depolama aygıtlarının dosya sistemi olmadan, doğrudan veri okuma ve yazma işlemlerini gerçekleştirmeyi sağlar.

- Yani, raw device, donanım cihazının kendisi değil, işletim sistemi tarafından düşük seviyede yönetilen bir depolama aygıtının erişim yöntemini ifade eder. İşletim sistemi, raw device üzerindeki veri bloklarını yönetir ve veri okuma/yazma işlemlerini gerçekleştirmek için ilgili sürücüleri kullanır.

### dd command
- yazma ve okuma islemi icin kullanilir.
- dd if=input of=output
- input belirtilmezse stdinden okuma yapar.
- output belirtilmezse stdouttan okuma yapar.

### To wipe the first GiB of the device (overwrite with zeros):
- dd if=/dev/zero of=/dev/sdb bs=1M count=1024

### To make a bootable USB stick from the Ubuntu installation ISO:
- dd if=~luke/Downloads/ubuntu-18.04.4-desktop-amd64.iso of=/dev/sdb status=progress

### To make a compressed backup of a raw partition:
- dd if=/dev/sdb1 | gzip -9 > partition.img.gz

### To restore the partition
- zcat partition.img.gz | dd of=/dev/sdb1

### Mounting and unmounting file systems
- ram device dosya sistemi olmadigindan cok faydali degildir.
- bir dosya sistemini başlatmak da yıkıcı bir işlemdir

### mkfs -t fstype /dev/device
- bir device disk ya da bir parca olabilir.
- fstype burda dosya tipi ornegin ext4, xfs, gibi birsey
- baska bir device'i lunux bir makineye eklemek icin device'in rootunu makinede bir foldera eklemek gerekir.

### mount [options] device mount-point
- device bir partition, usb aygiti, cdrom olabilir.
- mount-point ana makinedeki bir folderdir.
- Example: suppose that /dev/sdb is a USB stick and /dev/sdb1 is a partition on that device with a file system initialised (likely type FAT). To mount the USB stick on, eg /mnt:
mount /dev/sdb1 /mnt
- yukaridaki ornekte mnt'ye kopyalanacak birsey usb bellege de kopyalanacaktir.
tam tersi de gecerlidir.

### mount and cat /etc/mtab ve cat /proc/mounts
- bu iki komut mount edilmis dosya sistemlerini listeler

### umount device ve umount mount-point
- unmount etme

### /etc/fstab
- Varsayılan bağlama noktalarını ve seçeneklerini belirtebileceğiniz özel bir dosya vardır.

### finding files
- type cat, whereis awk, which gzip commandlarin yerini gosterir.
- file sistem tree'si hergun bir kere indekslenir.

### locate [options] pattern
- dosya ya da klasorun yerini gosterir.
- locate -i ignore case while searching * locate -r pattern is a regular expressions

### find [start-directories] [search-criteria] [action]
- Show all files with extension '.jpg' (ignoring case) $ find / -type f -iname '*.jpg'
- Show all files, directories, symlinkks…​ with dodgy ownership: $ find / -nouser -o -nogroup
- Delete all files under /tmp that haven’t been opened for more than 30 days: find /tmp -atime +30 -delete

### xargs
- bir komutu ya da ciktiyi arguman olarak verir.

find . -name '*.log' | xargs grep 'Salary'
date | xargs echo "Tarih:"