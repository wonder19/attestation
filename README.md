[![Build Status](https://travis-ci.org/test1910md/attestation.svg?branch=master)](https://travis-ci.org/github/test1910md/attestation)

<img src='https://bettercodehub.com/edge/badge/test1910md/attestation?branch=master'>

# Банк Санкт-Петербург
    https://idemo.bspb.ru/welcome

# Выполнил: Марина Дорохова

```sh
Дата создания проекта: 01.08.2020
Инструменты: pytest, selenuim, testrail, travis
Паттерн: PageObject
```
  
# Цели проекта:

- Создать архитектуру проекта
- Создать план тестирования 
- Покрыть автотестами
- Реализовать CI
- Представить отчет с результатами тестирования
 
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
### Allure
 #### Установка allure
 Для генерации отчетов необходимо установить Scoop через PowerShell
 https://scoop.sh/

 После чего нужно выполнить команду
  ```sh
 scoop install allure
 ```
 в окне PowerShell

 #### Генерация отчетов
 После прохождения тестов сформируется папка allure_result в корневой директории проекта

 Для генерации отчета необходимо ввести команду в окне PowerShell
 ```sh
 allure serve ${path}\attestation\allure
 ```
