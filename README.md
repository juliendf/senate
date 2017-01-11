# Senate

Senate is a tool to provide advise on AWS optimisation. <br>
It is aim to provide cost, security and architecture advice.


## AWS Access
The program use environment variable to access AWS datas<br>


**Create a .envrc file like** : <br>
```
export AWS_DEFAULT_REGION=REGION
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx
```

**Install the dependencies needed to run this program** : <br>
```
pip3 install -r requirements.txt
```

## Command

To run the program :<br>
```python main.py ```<br>