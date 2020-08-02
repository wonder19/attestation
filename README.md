[https://travis-ci.org/test1910md/attestation.svg?branch=master](https://travis-ci.org/github/test1910md/attestation)
# Банк Санкт-Петербург

  - Дата создания проекта 01.08.2020

### Установка

Необходимо установить все зависимости из requirements.txt

```sh
pip install -r requirements.txt
```

 ### Запуск

Необходимо установить все зависимости из requirements.txt
Перед запуском создайте виртуальное окружение

```sh
pip install virtualenv
virtualenv <env_name>
pytest
```
 ### Pre-commit-hooks
 Перед началом работы, необходимо выполнить команду
  ```sh
pre-commit install
```
для того, чтобы pre-commit запускался перед каждым коммитом

Принудительный запуск pre-commit:
 ```sh
pre-commit run --all-files
```
Запуск конкретного hook:
 ```sh
pre-commit run <hook_id>
```
Пропуск pre-commit:
 ```sh
git commit -m "commiting wihout pre-commit" --no-verify
```
Этапы:
```sh

```
