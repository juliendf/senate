# Senate

Senate is a tool to provide advise on AWS optimisation. <br>
It is aim to provide cost, security and architecture advice.


## AWS Access
The program use environment variable to access AWS datas<br>


**Use local credentials, IAM role or create a .envrc file like** : <br>
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
```
    cd senate
    python main.py 
```

<br>

## Output example
```
⇒  python main.py

################################                                 
Un-used EBS                          
################################
Total number of volumes : 2
Total number of not attached volumes : 0

################################                                                 
Data for : i-08d012335xxxxca258a                                           
################################

# Cloudwatch metric : CPU Utilisation #
Unuseddays : 7
Average CPU Utilisation for the period : 0.613432173778 Pourcent

# Cloudwatch metric : Network In #
Average NetworkIn per hour for the period : 232790 Bytes

# Cloudwatch metric : Network Out #
Average NetworkOut for the period : 49106 Bytes

Total Traffic : 117 MB per day
```

## Docker usage

**create env/env.list** : <br>
```
AWS_DEFAULT_REGION=REGION
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
```

**Build** : <br>
```
docker build -t senatev01 .
```

**run** : <br>
```
docker run --env-file ./env/env.list senatev01
```