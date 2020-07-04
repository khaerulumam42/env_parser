# Environment Parser (env_parser)

Rasanya melelahkan menghapus value variabel environment setelah selesai development. Mengapus satu persatu menghabiskan waktu beberapa menit, bisa untuk mengerjakan hal lain. itu mengapa saya membuat package ini supaya lebih mudah untuk membuat *example environment* dari environment sesungguhnya.

## Getting Started

Ada dua bagian repo di project ini, yang pertama dibuat menggunakan `python` yang kedua menggunakan `golang` sehingga ada dua alternatif cara untuk menggunakan *package/library* ini.

### **python**
Package ini dapat sudah saya test di `python3.6.10` dan OS `Ubuntu 16.04`. Karena tidak banyak dependency harusnya dapat berjalan juga di OS dan versi python yang berbeda.

### **golang**
Bahasa **go** yang saya gunakan adalah go versi `go1.12 linux/amd64`, belum saya coba menggunakan versi go lain dan sistem operasi lain, namun tetap tidak menutup kemungkinan akan berjalan dengan lancar.

## Prerequisites

### **python**
Secepatnya akan saya coba untuk memasukan ke dalam pip module package supaya memudahkan dalam instalasinya. Untuk sementara ini install melalui file `whl` yang installasinya menggunakan `pip`. Namun sebelumnya install terlebih dahulu, caranya:

```
python setup.py bdist_wheel
```

kemudian akan ter-*generate* file `whl` dalam folder `dist` dengan nama file

```
env_parser-<version>-py3-none-any.whl
```
### **golang**

Jika python menggunakan pip, di golang menggunakan perintah `go get` namun saya belum mencoba menggunakan `go get` secara langsung untuk menggunakan package ini lol

Jika ingin build sendiri berdasarkan versi golang yang kamu punya, bisa dilakukan dengan cara

```
cd go/cmd/envParser
go build -o env_parser main.go
```
Sehingga akan ter*generate file* bernama `env_parser` yang mana *file* ini adalah *file binary* yang bisa digunakan langsung tanpa menggunakan golang. Cara menggunakannya bisa langsung menuju bagian [How to use](#how-to-use)

## Installing

Setelah selesai ter*generate* selanjutnya instalasi melalui file `whl` di atas dengan cara:


```
pip install dist/env_parser-<version>-py3-none-any.whl
```


## How to use

### **python**
Penggunannya sangat sederhana, ubah *directory* ke *project* anda, kemudian jalankan

```
python -m env_parser
```
maka akan otomatis ter*generate* file `env.example` dalam folder yang sama dengan file `.env`
### **golang**
Inilah alasan mengapa saya membuat yang versi golang, karena dengan menggunakan golang akan sangat mudah dipakai karena otomatis ter-*build* menjadi *file binary*

pertama *copy file binary* yang sudah ter-*generate* ke folder sistem *bin*

```
sudo cp go/cmd/envParser/env_parser /bin/
```

kemudian kamu bisa langsung memakai nya di folder manapun menggunakan

```
env_parser [--force]
```

argumen `--force` digunakan untuk memaksa ***overwrite*** *file output* jika *file* tersebut eksis 

## Versioning

Untuk versioning kita menggunakan konvensi

**major.path.minor**

contoh untuk versi terakhir adalah

**0.0.1**

## Authors

* **Khaerul Umam** - *Initial work* - [khaerulumam42](https://github.com/khaerulumam42)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

this README template is from [PurpleBot](https://github.com/PurpleBooth)