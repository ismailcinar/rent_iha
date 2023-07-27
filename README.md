## Rent IHA

Bu proje iha kiralamak isteyen kullanıcıların gerekli arayüzler vasıtasıyla iha kiramalamasını ve bu kiraladıkları iha ile ilgili kişisel işlem yapmasını sağlamaktadır. Ayrıca admin kolarak girildiğinde ise iha eklenebilmekte ve gerekli CRUD işlemleri yapılabilmektedir. Projeyi Sqlite veya PostgreSQL ile kullanabilirsiniz. Dockerize edilen halinde veritabanı olarak PostgreSQL bulunuyor. Sqlite ise virtualenv ile kullanılmıştır.
Projede 2 farklı user -kullanıcı- türü bulunmaktadır. admin özelliğine sahip kişi ihalarla ilgili gerekli CRUD işlemlerini yapabiliyorken kiralama işlemini yapamamaktadır. Kullanıcı ise sadece kiralama özelliğine sahiptir. Kullacını kiralanan ihaları listeleyebilmektedir. Kullanıcı kendi kiraladığı iha ilgili işlemler yapabiliyorken diğer bir kullanıcının kiraladığı iha ile ilgili işlem yapamamaktadır.


## Bilgisayarınızda Çalıştırın

Projeyi klonlayın.

```bash
  git clone https://link-to-project
```

Proje dizinine gidin.

```bash
  cd rent_iha 
```

Gerekli paketleri yükleyin.

```bash
  docker build .
  docker-compose up
```

Migrations işlemlerini gerçekleştirin.

```bash
  docker-compose exec web python manage.py makemigrations
  docker-compose exec web python manage.py migrate
```
Kullanıcı oluşturup http://localhost:8000/admin/ sayfasına erişebilirsiniz.
```bash
  docker-compose exec web python manage.py createsuperuser
  
```
Projeyi çalıştırarak kullanabilirsiniz.
```bash
  docker-compose exec web python manage.py runserver
  
```
Projeyi DETAY
```bash
  Projede hem api hem de web görünümü bulunmaktadır. 
   API ile ilgili dökümantasyon http://127.0.0.1:8000/schema/docs#/ url'sinde bulunmaktadır. 
   Gerekli işlemleri buradan yapabilirsiniz.
  
```

## API Kullanımı

#### Tüm ihaları getirir. Ama Admin girişi gereklidir.

```http
  GET /api/uav/
```
#### İstenilen iha'yı getirir.

```http
  GET api/uav/{id}
```
#### Tüm kiralanan ihaları getirir. Ama görüntülemek için kullanıcı girişi gereklidir.

```http
  GET /api/rental-records/
```
#### Kiralanmış iha'ların listesini getirir.

```http
  GET /api/rental-records/{id}
```



  

  
