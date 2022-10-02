import pandas as pd
import numpy as np
import itertools as iter
import re

newdf = {}
#Constant
DATA = {
    "FILE": "FF&E.xlsx",
    "SUITE_PATTERN": re.compile("\d"),
    "ITEM_PATTERN": re.compile("\w+$")
}

#import function 

def fetchData(data):
    return pd.read_excel(data, header = 0)


mainDf = fetchData(DATA['FILE'])


#captures all the suite # out of the description
def numericExtractor(text):
    return ''.join( DATA['SUITE_PATTERN'].findall(text))

def get_SuiteNum():    
    return mainDf['Item Description'].apply(numericExtractor)

#captures all the item  out of the description
def itemExtractor(text):
    return ''.join(str(ele) for ele in DATA['ITEM_PATTERN'].findall(text))

def get_Item():    
    return mainDf['Item Description'].apply(itemExtractor)
    
def get_Cost():
    return mainDf['Line Amount']



newdf = {
    "Suite Number" : get_SuiteNum(), 
    "Item": get_Item(),
    "Cost": get_Cost(),

}

eibdf = pd.DataFrame(newdf)

def printer():

    with pd.ExcelWriter("EIB_INFO.xlsx") as writer:
        eibdf.to_excel(writer, sheet_name= "CHECKOUT",index_label= None )

printer()
