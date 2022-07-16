# SDK для работы с TON Rocket

## ⚙️ Установка

```shell
pip install tonrocketapisdk
```

## 🔐 Авторизация

Как получить токен написано [тут](https://pay.ton-rocket.com/api/).

```python
from tonrocketapisdk import *

api = RocketApi('токен')
```

## ⬇️ Навигация

#### 🚀 [Методы](#🚀-методы)
##### [- getAppInfo](#getappinfo)
##### [- transfer](#transfer)
##### [- withdrawal](#withdrawal)

##### [- createCheque](#createcheque)
##### [- getCheques](#getcheques)
##### [- getCheque](#getcheque)
##### [- editCheque](#editcheque)
##### [- deleteCheque](#deletecheque)

##### [- createInvoice](#createinvoice)
##### [- getInvoices](#getinvoices)
##### [- getInvoice](#getinvoice)
##### [- deleteInvoice](#deleteinvoice)

##### [- getCoins](#getcoins)
##### [- getCurrencies](#getcurrencies)

## 🚀 Методы

Параметры отмеченные знаком * являются обзательными

### getAppInfo 
[Документация](https://pay.ton-rocket.com/api/#/app/AppsController_getAppInfo)
| Параметр | Информация |
|---------|-------------|
| Не принимает параметров |

Пример:
```python
api.getAppInfo()
```

### transfer 
[Документация](https://pay.ton-rocket.com/api/#/app/AppsController_transfer)
| Параметр | Информация |
|---------|-------------|
| tgUserId* | ID получателя перевода |
| amount* | Сумма перевода |
| currency | Валюта перевода. По умолчанию: "TONCOIN" |
| transferId | По умолчанию: "12345" |
| description | По умолчанию: "" |

Пример:
```python
api.transfer({
  "tgUserId": 87209764,
  "currency": "TONCOIN",
  "amount": 1.23,
  "transferId": "abc-def",
  "description": "You are awesome!"
})
```

### withdrawal
[Документация](https://pay.ton-rocket.com/api/#/app/AppsController_withdrawal)
| Параметр | Информация |
|---------|-------------|
| address* | TON кошелек, на который нужно отправить монеты |
| amount* | Сумма перевода |
| currency | Валюта для вывода. По умолчанию: "TONCOIN" |
| withdrawalId | По умолчанию: "12345" |
| comment | По умолчанию: "" |

Пример:
```python
api.withdrawal({
  "address": "EQB1cmpxb3R-YLA3HLDV01Rx6OHpMQA_7MOglhqL2CwJx_dz",
  "currency": "TONCOIN",
  "amount": 1.23,
  "withdrawalId": "abc-def",
  "comment": "You are awesome!"
})
```

### createCheque
[Документация](https://pay.ton-rocket.com/api/#/multi-cheques/ChequesController_createCheque)
Все параметры как в документации

Пример:
```python
api.createCheque({
  "chequePerUser": 0.005,
  "usersNumber": 100,
  "refProgram": 50,
  "password": "pwd",
  "description": "This cheque is the best",
  "sendNotifications": true,
  "enableCaptcha": true,
  "telegramResourcesIds": [
    "-1001799549067"
  ]
})
```

### getCheques
[Документация](https://pay.ton-rocket.com/api/#/multi-cheques/ChequesController_getCheques)
| Параметр | Информация |
|---------|-------------|
| Не принимает параметров |

Пример:
```python
api.getCheques()
```

### getCheque
[Документация](https://pay.ton-rocket.com/api/#/multi-cheques/ChequesController_getCheque)
| Параметр | Информация |
|---------|-------------|
| id* | ID чека |

Пример:
```python
api.getCheque({
  id: 1234
})
```

### deleteCheque
[Документация](https://pay.ton-rocket.com/api/#/multi-cheques/ChequesController_deleteCheque)
| Параметр | Информация |
|---------|-------------|
| id* | ID чека |

Пример:
```python
api.deleteCheque({
  id: 1234
})
```

### createInvoice
[Документация](https://pay.ton-rocket.com/api/#/tg-invoices/InvoicesController_createInvoice)

Все параметры как в документации

Пример:
```python
api.createInvoice({
  "amount": 1.23,
  "description": "best thing in the world, 1 item",
  "hiddenMessage": "thank you",
  "callbackUrl": "https://t.me/ton_rocket",
  "payload": "some custom payload I want to see in webhook or when I request invoice",
  "expiredIn": 10
})
```

### getInvoices
[Документация](https://pay.ton-rocket.com/api/#/tg-invoices/InvoicesController_getInvoices)
| Параметр | Информация |
|---------|-------------|
| Не принимает параметров |

Пример:
```python
api.getInvoices()
```

### getInvoice
[Документация](https://pay.ton-rocket.com/api/#/tg-invoices/InvoicesController_getInvoice)
| Параметр | Информация |
|---------|-------------|
| id* | ID счёта |

Пример:
```python
api.getInvoice({
  id: 1234
})
```

### deleteInvoice
[Документация](https://pay.ton-rocket.com/api/#/tg-invoices/InvoicesController_deleteInvoice)
| Параметр | Информация |
|---------|-------------|
| id* | ID счёта |

Пример:
```python
api.deleteInvoice({
  id: 1234
})
```

### getCoins
[Документация](https://pay.ton-rocket.com/api/#/coins/CoinsController_get)
| Параметр | Информация |
|---------|-------------|
| Не принимает параметров |

Пример:
```python
api.getCoins()
```

### getCurrencies
[Документация](https://pay.ton-rocket.com/api/#/currencies/CurrenciesController_getRates)
| Параметр | Информация |
|---------|-------------|
| coinFrom* | ID токена |
| coinTo* | ID токена |

Пример:
```python
api.getCurrencies({
  coinFrom: Assets.TON,
  coinTo: Assets.SCALE
})
```