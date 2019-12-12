# ​Íba Chatbot

## ​1.1.​ Setup

1. Clone project from its repository to make it run locally from computer. For this, you must have the git CLI installed:
```
$ git clone https://github.com/Ibabot/Iba.git
```

2. Install Rasa Open Source with ​pip​. The machine running it is required to have Python 3.6 or 3.7 previously installed.
```
$ pip install rasa
```
_Make sure Microsoft VC++ Compiler is also installed. You can get it from the Visual Studio IDE._

This setup is originally made in the Windows 10 OS. If needed for another operating system, the Rasa official installation guide can be referred to. The Rasa documentation can also be used if something is not working during the installation.[^1]

## ​1.2.​ Development

1. Overview of the files in the project
    `actions/actions.py` - contains custom actions code to implement more complex logical operations and connections to external services and APIs.
    `actions/bank_data.json` - contains the JSON with the current information of branches of Íslandsbanki.
    `data/lookup​` - contains lookup files to improve entity extraction.
    `data/nlu` - contains the training data used for the classifications of intents and extracting entities from user input. 
    `data/stories` - contains the possible conversation paths used to train Rasa’s dialogue management.
    `models/` - contains the trained models. The newest model is automatically used when running the bot.
    `domain.yml` ​- contains the domain, i.e. the brain of the bot (it specifies the intents, entities, slots, and actions your bot should know about) as well as response templates
    `config.yml​` - training configurations for the NLU pipeline and policy ensemble.
    `credentials.yml` - contains credentials for different services used and lists events to be captured and emitted by services that use it.
    `endpoints.yml` ​- contains the webhook configuration for the custom actions.


### ​1.2.1.​ Local Development without Docker

1. To start Íba, a trained model is needed That can be achieved by using the command listed below, using a terminal or the cmd prompt from the root of the project. This command must be performed every time changes are made to the code.
```
$ rasa train
```

2. To talk to the bot on localhost in cmd line interface, use the command below. The ` --​ debug` ​ flag is optional but it will set the server to be verbose during debug time.
```
$ rasa shell​ --debug
```

3. To use the custom actions, a separate terminal must be used. It is needed to run on another port
```
$ rasa run actions
```

### 1.2.2.​ Local Development with Docker

1. Once the download is complete, if using Windows, it is necessary that the OS version has Hyper-V support. More can be read about the issue here:
    [https://docs.docker.com/machine/drivers/hyper-v/​](https://docs.docker.com/machine/drivers/hyper-v/). 
    If your OS version does support Hyper-V, make sure that the feature is enabled.
2. Docker must be installed. You can download it ​[here](https://docs.docker.com/)​.
3. The model must be trained through docker for it to work properly. Navigate to the project’s root directory and type:
```
$ docker run -v ​$(pwd)​:/app rasa/rasa:1.5.1 train --domain domain.yml --data data --out models
```

4. To run the server with docker, type:
```
$ docker run -v ​$(pwd)/​models:/app/models rasa/rasa:1.5.1 run
```

5. To run the action server along with the core server, use the command:
```
docker-compose up
```

## ​1.3.​ Deployment

1. When new code is pushed to the master on Ibabot’s repository, the CI server (Heroku) automatically builds and deploys the project. If the build succeeds, the
    changes are pushed to the core Rasa server ​[https://ibachatbot.heroku.com](​https://ibachatbot.heroku.com) along with the Rasa Action server [https://rasibabot.heroku.com](https://rasibabot.heroku.com).
    Heroku will take in the Dockerfiles and assemble the images to run both servers (action and core). This process is done automatically, and can be edited in the
    `heroku.yml.`

All changes made and pushed to master will automatically build and deploy to production on the website’s URL listed above.


[^1] ​_[https://rasa.com/docs/rasa/user-guide/installation/](https://rasa.com/docs/rasa/user-guide/installation/)_
