from ibm_watson import ToneAnalyzerV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from models.Tone import Tone

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

authenticator = IAMAuthenticator(
    apikey='9tkk9V0QLUkKZjy7e_pRQz0_OAMP4Ieq698rpr7l_Na9')
tone_analyzer = ToneAnalyzerV3(
    authenticator=authenticator,
    version='2017-09-21'
)

tone_analyzer.set_service_url(
    'https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/0fdbe374-d0a1-4dca-ae7e-734e7621e732')

tone_analyzer.set_disable_ssl_verification(True)


def detect_tone(message):
    tones = []
    try:
        tone_analysis = tone_analyzer.tone(
            {'text': message}, content_type='application/json').get_result()
        test = tone_analysis['document_tone']['tones']
        print(tone_analysis['document_tone']['tones'])

        for i in test:
            tone = Tone(i['score'], i['tone_id'], i['tone_name'])
            print(tone)
            tones.append(tone)
        print(tones)

    except ApiException as ex:
        print(f'Error: {ex.code} message: {ex.message}')

    return tones
