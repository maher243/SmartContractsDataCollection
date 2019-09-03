"""
Created on Wed Apr 10 17:21:42 2019

@author: Maher Alharby
"""
import requests

class etherscan:
    def __init__(self, apikey, network):
        self.network = network
        self.apikey = apikey
        if network=='mainnet':
            self.apipath = 'https://api.etherscan.io/api?'
        else:
            self.apipath = 'https://api' + '-' + network + '.etherscan.io/api?'

    #### define all functions that we need to use from Etherscan APIs ####
    def getTransactions(self, address, fromblock, toblock,p,c):
        payload = {'module':'account', 'action':'txlist', 'address':address, 'startblock':fromblock, 'endblock':toblock, 'page':p, 'offset':c, 'sort':'asc', 'apykey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getBlockNumber(self):
        payload = {'module':'proxy', 'action':'eth_BlockNumber', 'apykey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getBlockByNumber(self, number):
        payload = {'module':'proxy', 'action':'eth_getBlockByNumber', 'tag':hex(number), 'boolean':'true', 'apykey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getTransactionReceipt(self, txhash):
        payload = {'module':'proxy', 'action':'eth_getTransactionReceipt', 'txhash':txhash, 'apykey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getCode(self, address):
        payload = {'module':'proxy', 'action':'eth_getCode', 'address':address, 'tag':'latest', 'apykey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
