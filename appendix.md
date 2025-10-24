# Appendix. Setting up the environment
## A.1 Python
### Preparation
* create Venv
  * windows
    ```commandline
    python -m venv .venv
    ```
  *  Mac/Linux 
    ```commandline
    python3 -m venv .venv
    ```
* Switch to the specific `.venv`
  * windows
    * powershell
      ```commandline
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
      .\.venv\Scripts\Activate.ps1
      ```
    * cmd
      ```commandline
      .\.venv\Scripts\activate.bat
      ```
  *  Mac/Linux 
    ```commandline
     source .venv/bin/activate
    ```
* Stop env
  ```
  deactivate
  ```
### Python libraries used in this book by chapter
| Library             | Link                                          | Chapter | Key required |
|---------------------|-----------------------------------------------|---------|--------------|
| python-dotenv       | https://pypi.org/project/python-dotenv/       | 3       | No           |
| yfinance            | https://pypi.org/project/yfinance/            | 3       | No           |
| pandas              | https://pypi.org/project/pandas/              | 3       | No           |
| NumPy               | https://pypi.org/project/numpy/               | 3       | No           |
| matplotlib          | https://pypi.org/project/matplotlib/          | 3       | No           |
| finviz              | https://pypi.org/project/finviz/              | 3       | Yes          |
| openbb              | https://pypi.org/project/openbb/              | 3       | Yes          |
| alpha-vantage       | https://pypi.org/project/alpha-vantage/       | 3       | Yes          |
| eodhd               | https://pypi.org/project/eodhd/               | 3       | Yes          |
| pytrends            | https://pypi.org/project/pytrends/            | 4       | No           |
| Alpaca-py           | https://pypi.org/project/alpaca-py/           | 6       | Yes          |
| ib_insync           | https://pypi.org/project/ib-insync/           | 6       | No           |
| python_binance      | https://pypi.org/project/python-binance/      | 6       | Yes          |
| SQLAlchemy          | https://pypi.org/project/SQLAlchemy/          | 6       | No           |
| CurrencyConverter   | https://pypi.org/project/CurrencyConverter/   | 6       | No           |
| scikit-learn        | https://pypi.org/project/scikit-learn/        | 8       | No           |
| statsmodels         | https://pypi.org/project/statsmodels/         | 8       | No           |
| openai              | https://pypi.org/project/openai/              | 8       | Yes          |
| google-genai        | https://pypi.org/project/google-genai/        | 8       | Yes          |
| google-generativeai | https://pypi.org/project/google-generativeai/ | 8       | Yes          |
| anthropic           | https://pypi.org/project/anthropic/           | 8       | Yes          |
| transformers        | https://pypi.org/project/transformers/        | 8       | No           |
| langchain           | https://pypi.org/project/langchain/           | 9       | No           |
| Langchain-community | https://pypi.org/project/langchain-community/ | 9       | No           |
| Langchain-openai    | https://pypi.org/project/langchain-openai/    | 9       | Yes          |
| Langchain-core      | https://pypi.org/project/langchain-core/      | 9       | No           |
| mplfinance          | https://pypi.org/project/mplfinance/          | 10      | No           |
| streamlit           | https://pypi.org/project/streamlit/           | 10      | No           |

For example, you can install these three libraries, which we frequently use in this book, in this way:
```bash
pip install yfinance pandas numpy
```
### pip install notebook
```bash
pip install notebook
jupyter notebook
```
## A.4 Development environment
### A.4.1 Anaconda
Refer to the installation routine on the Anaconda web page (https://mng.bz/Rwoa).

### A.4.2 Visual Studio Code
Download and install VS Code for your operating system based on the vendor’s instructions at https://mng.bz/15BR.

### A.4.3 PyCharm
* https://github.com/mkevenaar/chocolatey-packages/blob/master/automatic/pycharm-community/tools/chocolateyInstall.ps1
* https://www.jetbrains.com/pycharm/download/other.html

## A.5 Cloud
* Google Colab
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch02.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch03.ipynb
    * Env `datasource.alphavantage.secret` is the [**Alpha Vantage**](https://www.alphavantage.co/support/#)'s api key.Its usage is at https://pypi.org/project/alpha-vantage/ ,`ALPHAVANTAGE_API_KEY` . 
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch04.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch05.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch06.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch07.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch08.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch09.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch10.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch11.ipynb
  * https://colab.research.google.com/github/robert0714/manning-investing-programmers-stefan-papp-2025/blob/master/ch12.ipynb
  
### A.5.1 **Database**
* SQLite database
* SQL Alchemy library

### A.5.2 Cloud secrets managers
Listing A.2 shows how to use the Boto3 library to access AWS Secrets Manager.
```bash
client = boto3.client('secretsmanager')
try:
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret
except Exception as e:
    print(f"Error retrieving secret: {e}")
    return None
```

## A.6 Export and documentation
* Note-taking platforms such as Notion or Google Sheets.
  
## A.7 LLMs
Using four LLMs in this book:
* Anthropic
* OpenAI
* Google Gemini
* AdaptLLM/finance-chat

## A.8 Brokers and exchanges 
* `Interactive Brokers` —A long-established international broker with a tremendous amount of functionality
* `Alpaca` —A developer-first broker with innovative APIs
* `Binance` —A well-known cryptocurrency exchange

As many different brokers and exchanges are available worldwide, we must be aware that every financial platform requires a KYC process, which requires customers to provide proof of their identity. This procedure is for your protection as investors. Verified users who must authenticate to use a system are less likely to attempt fraud.

While two platforms use API keys to authenticate, Interactive Brokers takes a different approach. Interactive Brokers uses a local installation of a tool called Trader Workstation (TWS) to connect with a Python API. Sometimes, you need to configure the API access with the TWS. Interactive Brokers provides information tailored to your operating system.
