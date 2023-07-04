# a) Install dependencies
python3 -m venv env
source env/bin/activate
pip install pygame

# b) Run all necessary parts of the codebase
python player.py &
python enemy.py &
python bullet.py &
