# CarsApiPython

Uygulamayı açmak için CarsApiPython/CarsApiPython/deneme.py isimli dosya ve proje start up olarak ayarlanmalıdır. Defaultta ayarlıdır

apiden istek atmak için aşağıdaki URL'i kullanabilirsiniz
http://localhost:5000/cars/list?year=2020&year=2020&trans=automatic&brand=bmw
parametreler yukarıdaki şekilde değiştirilerek kullanılabilir


yıl parametresi farklı girilse dahi ilk girilen yılı alır.


Selenium ile gezdiği için driver tarafından sorun olabilir ve uygulama kırılabilir.
Eğer uygulama herhangi bir parametre yüzünden patlarsa apiden tekrar istek atılması gerekmektedir.


araç sayısı için 98. satırdaki for döngüsünde bulunan değer değiştireler istek kadar araç bilgisi elde edilebilir
