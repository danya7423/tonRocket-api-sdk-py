from requests import get, post, delete

class RocketApi():
    def __init__(self, access_token):
        self.access_token = str(access_token)
        self.baseUrl = 'https://pay.ton-rocket.com'
        self.headers = {'Content-Type': 'application/json', 'Rocket-Pay-Key': self.access_token}

    def getVersion(self):
        return get(f'{self.baseUrl}/version', headers=self.headers).json()

    def getAppInfo(self):
        return get(f'{self.baseUrl}/app/info', headers=self.headers).json()

    def transfer(self, data):
        if 'amount' not in data:
            raise Exception('amount is required')
        if 'tgUserId' not in data:
            raise Exception('tgUserId is required')

        if 'currency' not in data:
            data['currency'] = 'TONCOIN'
        if 'transferId' not in data:
            data['transferId'] = '12345'    
        if 'comment' not in data:
            data['comment'] = ''    
        
        response = post(f'{self.baseUrl}/app/transfer',
                        headers = self.headers,
                        json = {
                            'tgUserId': data['id'],
                            'amount': data['amount'],
                            'currency': data['currency'],
                            'transferId': data['transferId'],
                            'comment': data['comment']
                        }).json()
        return response
    
    def withdrawal(self, data):
        if 'amount' not in data:
            raise Exception('amount is required')
        if 'address' not in data:
            raise Exception('address is required')

        if 'currency' not in data:
            data['currency'] = 'TONCOIN'
        if 'withdrawalId' not in data:
            data['withdrawalId'] = '12345'    
        if 'comment' not in data:
            data['comment'] = ''    
        
        response = post(f'{self.baseUrl}/app/withdrawal',
                        headers = self.headers,
                        json = {
                            'address': data['address'],
                            'amount': data['amount'],
                            'currency': data['currency'],
                            'withdrawalId': data['withdrawalId'],
                            'comment': data['comment']
                        }).json()
        return response

    def createCheque(self, data):
        if 'chequePerUser' not in data:
            raise Exception('chequePerUser is required')
        if 'usersNumber' not in data:
            raise Exception('usersNumber is required')
        if 'refProgram' not in data:
            raise Exception('refProgram is required')

        if 'password' not in data:
            data['password'] = ''
        if 'description' not in data:
            data['description'] = ''    
        if 'sendNotifications' not in data:
            data['sendNotifications'] = False
        if 'enableCaptcha' not in data:
            data['enableCaptcha'] = True
        if 'telegramResourcesIds' not in data:
            data['telegramResourcesIds'] = []
        
        response = post(f'{self.baseUrl}/multi-cheques',
                        headers = self.headers,
                        json = data
                        ).json()
        return response

    def getCheques(self):
        return get(f'{self.baseUrl}/multi-cheques', headers=self.headers).json()

    def getCheque(self, data):
        if 'id' not in data:
            raise Exception('id is required')

        return get(f"{self.baseUrl}/multi-cheques/{data['id']}", headers=self.headers).json()

    def deleteCheque(self, data):
        if 'id' not in data:
            raise Exception('id is required')
            
        return delete(f"{self.baseUrl}/multi-cheques/{data['id']}", headers=self.headers).json()

    def createInvoice(self, data):
        if 'amount' not in data:
            raise Exception('amount is required')

        if 'description' not in data:
            data['description'] = ''
        if 'hiddenMessage' not in data:
            data['hiddenMessage'] = ''    
        if 'callbackUrl' not in data:
            data['callbackUrl'] = ""
        if 'payload' not in data:
            data['payload'] = ""
        if 'expiredIn' not in data:
            data['expiredIn'] = 0
        
        response = post(f'{self.baseUrl}/tg-invoices',
                        headers = self.headers,
                        json = data
                        ).json()
        return response

    def getInvoices(self):
        return get(f'{self.baseUrl}/tg-invoices', headers=self.headers).json()

    def getInvoice(self, data):
        if 'id' not in data:
            raise Exception('id is required')

        return get(f"{self.baseUrl}/tg-invoices/{data['id']}", headers=self.headers).json()

    def deleteInvoice(self, data):
        if 'id' not in data:
            raise Exception('id is required')
            
        return delete(f"{self.baseUrl}/tg-invoices/{data['id']}", headers=self.headers).json()

    def getCoins(self):
        return get(f'{self.baseUrl}/coins', headers=self.headers).json()

    def getCurrencies(self, data):
        if 'coinFrom' not in data:
            raise Exception('coinFrom is required')

        if 'coinTo' not in data:
            raise Exception('coinTo is required')

        return get(f'{self.baseUrl}/currencies/rate?coinFrom={data["coinFrom"]}&coinTo={data["coinTo"]}', headers=self.headers).json()