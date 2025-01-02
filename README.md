# tenantpay-db-chatbot


# Ollama sqlcoder

[docker](https://hub.docker.com/r/ollama/ollama)

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama



### Google Colab
[Google Colab Notebook link](https://colab.research.google.com/drive/1McNoxMhGiReSS7XzTj-hwAM0Vl8jRf0D)


***
***
***
### Install Python version 3.8
**Note:** Rasa only works with depreciated version python i.e. <= 3.8

Steps to install older python version:

### For Ubuntu/Debian-based systems:
```
sudo apt update
sudo apt install -y build-essential curl libbz2-dev libssl-dev libreadline-dev \
    libsqlite3-dev zlib1g-dev libffi-dev liblzma-dev


# Install Pyenv Use the recommended installation script:
curl https://pyenv.run | bash

# Update Shell Configuration Add Pyenv to your shell's configuration file to make it available globally:
echo -e '\n# Pyenv Configuration' >> ~/.bashrc
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# Verify Installation
pyenv --version
```


###  On Windows
```
# Install Pyenv for Windows
git clone https://github.com/pyenv-win/pyenv-win.git "$HOME/.pyenv"

# Update PATH Add the following to your system's PATH environment variable:
%USERPROFILE%\.pyenv\pyenv-win\bin
%USERPROFILE%\.pyenv\pyenv-win\shims

# Verify Installation Open a new terminal and check
pyenv --version
```

###  Switch to a compatible Python version
```
# Install new version
pyenv install 3.8

# check the currently active global Python version with:
pyenv global

# To use specific version for each project
pyenv versions
pyenv local 3.8.20
```
***

### Create Virtual Environment
```
python -m venv tp-db-venv
source ./tp-db-venv/bin/activate
pip install -r requirements.txt
```


### Open Jupyter Notebooks Server:
```
jupyter notebook
```