### Conversational Chatbot using Rasa Framework. The Chatbot which is named Wall-E helps Users to get the latest news happening around the world.

Wall-E is deployed on Slack and use nytimes APIs to get top 5 news feed for its users in various categories.

There are articles posted on Medium - How to build a conversational chatbot using Rasa and Python. Its a trilogy of the series.

**Chatbots & Future of Conversational AI**

https://medium.com/@itsromiljain/chatbots-future-of-conversational-ai-842a865b8125

**1. Build a Conversational Chatbot with Rasa Stack and Python— Rasa NLU**

https://medium.com/@itsromiljain/build-a-conversational-chatbot-with-rasa-stack-and-python-rasa-nlu-b79dfbe59491

**2. Build a Conversational Chatbot with Rasa Stack and Python — Rasa Core**

https://medium.com/@itsromiljain/build-a-conversational-chatbot-with-rasa-stack-and-python-rasa-core-41b9c38c26b

**3. Deploy your chatbot on Slack**

https://medium.com/@itsromiljain/3-deploy-your-chatbot-on-slack-1a0e8390f66b

## Various Steps to Train and Run Rasa NLU and Core
**Install miniconda/anaconda**

https://docs.conda.io/en/latest/miniconda.html

**Check conda version**
```
conda --version
```
**Conda Update**
```
conda update conda
```
**Create Virtual Env**
```
conda create -n botenv python=3.6
```
**Activate Virtual Env**
```
conda activate botenv
```
**Initial commands to install Rasa NLU to Virtual Env i.e. botenv**
```
pip install rasa_nlu
```
**To Update existing one**
```
pip install -U rasa_nlu
```
**For dependencies**
**spaCy+sklearn**
```
pip install rasa_nlu[spacy]
python3 -m spacy download en
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
```
**Tensorflow**
pip install rasa_nlu[tensorflow]

**Train Rasa NLU**
```
python3 -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
```
**Run Rasa NLU**
```
python3 -m rasa_nlu.server --path ./models
```
**Initial commands to install Rasa Core & SDK**
```
pip install rasa_core
pip install rasa_core_sdk
```
**To Update existing one**
```
pip install -U rasa_core
```
**Train Rasa Core**
```
python3 -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
```
**Train Rasa Core Interactively**
```
python3 -m rasa_core.train interactive -o models/dialogue -d domain.yml -c policy.yml -s data/stories.md --nlu models/current/nlu
```
**Run Rasa Core**
```
python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```
**Debug Rasa Core**
```
python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --debug
```
**Python**
**Train and Run NLU**
```
python3 nlu_model.py
```
**Train and Run CORE**
```
python3 dialogue_model.py
```
**To run the custom action**
```
python3 -m rasa_core_sdk.endpoint --actions actions
```
