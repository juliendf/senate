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

## Output example
```
⇒  python main.py

#### Unused EBS ####
Total number of volumes : 2
Total number of not attached volumes : 1

Data for : i-01245a878b3b143f5

#### Cloudwatch metric : CPU Utilisation ####
Unuseddays : 14
warning
Average CPU Utilisation for the period : 0.0307568159204 Pourcent

#### Cloudwatch metric : Network In ####
Average NetworkIn per hour for the period : 705 Bytes

#### Cloudwatch metric : Network Out ####
Average NetworkOut for the period : 1085 Bytes
Total Traffic : 41 MB per day