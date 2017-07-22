import os
import json
import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def response(text):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': text
            }
        }
    }

def handler(event, context):
    logger.debug(json.dumps(event))
    application_id = event['session']['application']['applicationId']
    if application_id != os.environ['APPLICATION_ID']:
        logger.info('invalid application id')
        return response('invalid application id')

    with open('irkit.json') as f:
        config = json.loads(f.read())

    if event['request']['type'] != 'IntentRequest':
        return response('not intent request')

    slots = event['request']['intent']['slots']
    devices_in_config = list(config['Device'].keys())
    device = slots['Device'].get('value')
    if device is None:
        if len(devices_in_config) != 1:
            logger.info('device is not specified and device in config is not 1')
            return response('please specify device')
        device = devices_in_config[0]
    if device not in devices_in_config:
        logger.info('invalid device %s', device)
        return response('invalid device')
    target = slots['Target']['value'].lower()
    control = slots['Control']['value'].lower()

    url = 'https://api.getirkit.com/1/messages'
    device_id = config['Device'][device]['deviceid']
    client_key = config['Device'][device]['clientkey']

    commands_in_config = config['IR'].keys()
    command = f'{target}.{control}'
    if command not in commands_in_config:
        logger.info('invalid command %s', command)
        return response('invalid command')
    message = json.dumps(config['IR'][command])
    params = {
        'deviceid': device_id,
        'clientkey': client_key,
        'message': message
    }
    r =  requests.post(url, data=params)
    r.raise_for_status()
    logger.info('response success fully command: %s', command)
    return response('ir kit received request')
