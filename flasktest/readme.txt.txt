first install python 3.6
then setup path variable in windows
install pip and setup path for it
now pip is working from any where so do pip install virtualenv it will setup virtual env
noe go to project ,then do virtualenv venv  - it will set up virtual enviournment for the project

venv\scripts\activate  :it will activate project enviornment
deactivate : it will deactivate current enviournment

install flask into it
using pip install flask

create hello.py
then set FLASK_APP=hello.py
then  flask run , it will run on port 5000

flask run --host=0.0.0.0 to expose web service publicly . This tells your operating system to listen on all public IPs.

set FLASK_DEBUG=1 it will reload code in each change