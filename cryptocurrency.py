import requests
class crypto():
    def __init__(self, api_key, fsym, tsyms):
        self.api_key = api_key
        self.fysm = fsym 
        self.tsyms = tsyms
        self.url = 'https://min-api.cryptocompare.com/data/price'

    def getCryptData(self):
        payload = { 'api_key' : self.api_key, 
                    'fsym' : self.fysm,
                    'tsyms' : self.tsyms  }
        try : 
            r = requests.get(self.url, params= payload)
            print(r.url)
            if r.status_code != 200:
                raise ValueError('Transaction failed.')

            return r.json()[self.tsyms]
        except Exception as e:
            print("You have a problem.")

if __name__ == '__main__':
    BTC = crypto('CryptoCompare_API_key', 'BTC', 'INR')
    print(BTC.getCryptData())

    

