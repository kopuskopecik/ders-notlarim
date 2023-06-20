### Kubectl config
- Cluster'a baglanmak icin config dosyalarindan okur. Gerekli bilgilere burdan ulasir.
- Kubectl Degerleri varsayilan olarak /home/erdogan/.kube dosyasindan okur.
- Bu dosyanin icinden clusterlar ve herbir cluster'a baglanmak icin userlar bulunur.
- context kisminda hangi cluster'a hangi user ile baglanabilecegim burda belirtilir. namespace de burda belirtilir.

### kubectl config
- Bu komut ile kullanabilecegim subcommandleri goruyorum bu komutla kullanabilecegim.

### kubectl config get-contexts
- contextleri listelr.
- mevcut atanan contextte yildiz olur. Yani o cluster aktif demektir o kubectl icin.

### kubectl config current-context
- secili olan contexti yani clusteri gosterir.

### kubectl config use-context docker-desktop
- context degistirme yani cluster'i degistirme

### kubectl
- tum komutlari gosterir.

### kubectl cluster-info
- uzerinde calistigimiz cluster bilgilerini getirir.

### kubectl cp --help
- cp komutunun nasil kullanildigini gosteriyor.

### kubecl kullanim mantigi
- kubectl eylem(get) object(pod, deployment, service) objectName(podeName)
- contextte namespace belirtilmediyse default namespacete calisir tum komutlar.

### kubectl get pods -n kube-system
- kube-system isimli namespace clusterinda calisir bu komut.

### kubectl get pods -A
- tum namespacelerdeki podlar gelir.

### kubectl get pods -A -o wide
- cikti formatini daha ayrintili gosterir.
- -o diger optinslar, yaml, json, wide, jsonpath, go-template,...

### sadece pod isimlerini alma
- kubectl get pods -A -a json | jq -r ".items[].spec.containers[].name"

### kubectl get pods -A | awk '{print $2}'
- isimleri getirir.