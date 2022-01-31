from playsound import playsound
import requests
class Voice():
    def __init__(self, api_key, hl):
        self.api_key = api_key
        self.hl = hl 
        self.url = 'http://api.voicerss.org/'

    def getVoice(self, src):
        payload = { 
                    'key' : self.api_key,
                    'hl' : self.hl, 
                    'src' : src,
                    'v' : 'Harry'
                     }
        try : 
            r = requests.get(self.url, params= payload)
            print(r.status_code)
            print(r.url)

            if r.status_code != 200:
                raise ValueError('Transaction failed.')

            return r.content
        except Exception as e:
            print("You have a problem.")

    def saveaudio(self, bin):
        f = open('output.wav', 'wb')
        f.write(bin)
        f.close

    def playaudio(self, bin):
        playsound('output.wav')

if __name__ == '__main__':
    alf = Voice('Voice_RSS_API_key', 'en-gb')
    testaudio = alf.getVoice('Hello. This is working correctly.')
    alf.saveaudio(testaudio)
    alf.playaudio(testaudio)