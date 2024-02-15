git clone --depth=1 https://github.com/geoffdutton/bash-it.git ~/.bash_it
bash ~/.bash_it/install.sh --silent
# sed -i "s/BASH_IT_THEME='[^']*'/BASH_IT_THEME='new-theme'/g" ~/.bashrc
sed -i "s/BASH_IT_THEME='bobby'/BASH_IT_THEME='bobby-python'/g" ~/.bashrc