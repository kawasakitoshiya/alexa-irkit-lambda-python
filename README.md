Alexa IRKit Lambda python
===

# setup
``` abap
$ npm install -g serverless
$ npm install --save serverless-python-requirements
```

# deploy

``` abap
$ cp ~/.irkit.json . # you use config file of ruby-irkit
$ APPLICATION_ID=amzn1.ask.skill.xxxxxxxxxxxxxxxx sls deploy
```

# Ref
- http://maaash.jp/2016/07/alexa-air-conditioner/
- http://dev.classmethod.jp/cloud/introduction-of-alexa-skill-kit/
- https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interaction-model-reference
