# Environment Parser (env_parser)

Rasanya melelahkan menghapus value variabel environment setelah selesai development. Mengapus satu persatu menghabiskan waktu beberapa menit, bisa untuk mengerjakan hal lain. itu mengapa saya membuat package ini supaya lebih mudah untuk membuat *example environment* dari environment sesungguhnya.

## Getting Started

Package ini dapat sudah saya test di `python3.6.10` dan OS `Ubuntu 16.04`. Karena tidak banyak dependency harusnya dapat berjalan juga di OS dan versi python yang berbeda.

### Prerequisites

Secepatnya akan saya coba untuk memasukan ke dalam pip module package supaya memudahkan dalam instalasinya. Untuk sementara ini install melalui file `whl` yang installasinya menggunakan `pip`. Namun sebelumnya install terlebih dahulu, caranya:

```
python setup.py bdist_wheel
```

kemudian akan ter-*generate* file `whl` dalam folder `dist` dengan nama file

```
env_parser-<version>-py3-none-any.whl
```

### Installing

Setelah selesai ter*generate* selanjutnya instalasi melalui file `whl` di atas dengan cara:


```
pip install dist/env_parser-<version>-py3-none-any.whl
```


## How to use

Penggunannya sangat sederhana, ubah *directory* ke *project* anda, kemudian jalankan

```
python -m env_parser
```
maka akan otomatis ter*generate* file `env.example` dalam folder yang sama dengan file `.env`

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