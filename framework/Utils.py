import json;
import datetime
from datetime import timedelta, date, datetime
import random

class Utils:

    def readJSONDataValue(self,context,parentNode,childNode):
        with open('testdata.json') as f:
            data = json.load(f)
        data1 = data[parentNode]
        value = data1[childNode]
        return value

    def readJSONDataObject(self, context, parentNode):
        with open('testdata.json') as f:
            data = json.load(f)
        dataObj = data[parentNode]
        return dataObj

    def getRandomDate(self,context):
        # current dateTime
        now = datetime.now()
        x = random.randint(150, 500)
        end_date = now + timedelta(days=x)
        end_date = end_date.strftime("%d-%m-%Y")
        return end_date