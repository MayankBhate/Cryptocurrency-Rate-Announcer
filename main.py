from cryptocurrency import crypto
from speech import Voice
from time import sleep

def main():
    cryptoAPI = 'CryptoCompare_API_key'
    voiceAPI = 'Voice_RSS_API_key'
    cry = 'BTC'
    cur = 'INR'

    cryptocal = crypto(cryptoAPI, cry, cur)
    voiceop = Voice(voiceAPI, 'en-gb')

    while True:
        cryval = cryptocal.getCryptData()
        speech = 'Value of ' + cry + ' is ' + str(cryval) + ' ' + cur
        print(speech)
        aud = voiceop.getVoice(speech)
        voiceop.saveaudio(aud)
        voiceop.playaudio(aud)
        sleep(10)

if __name__ == '__main__':
    main()