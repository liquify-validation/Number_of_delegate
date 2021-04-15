from web3 import Web3
import csv
import json
from datetime import datetime
from fusenetCon import *

RPC_ADDRESS = ''
CONSENSUS_ADDR = Web3.toChecksumAddress('0x3014ca10b91cb3d0ad85fef7a3cb95bcac9c0f79')
web3Fuse = Web3(Web3.HTTPProvider(RPC_ADDRESS))
fuseConsensusContract = web3Fuse.eth.contract(abi=CONTRACT_ABI, address=CONSENSUS_ADDR)
oneDay = 17280

def getValidators(block):
    activeValidator = fuseConsensusContract.functions.getValidators().call(block_identifier=block)
    return activeValidator

def countDelegates(block):
    DECIMAL = 10 ** 18
    vals = getValidators(block)

    numDelegates = 0
    numVals = 0
    totalStaked = 0

    for val in vals:
        totalStaked = totalStaked + fuseConsensusContract.functions.stakeAmount(val).call(block_identifier=block) / DECIMAL
        numVals = numVals + 1
        numDelegates = numDelegates + fuseConsensusContract.functions.delegatorsLength(val).call(block_identifier=block)

    return totalStaked,numVals,numDelegates

if __name__ == "__main__":
    currentSearch = oneDay/2

    block = web3Fuse.eth.getBlock(block_identifier='latest')
    currentBlock = web3Fuse.eth.blockNumber

    NotFound = False

    startBlock = 7853031 + (4 * oneDay)
    block = web3Fuse.eth.getBlock(block_identifier=startBlock)
    newBlock = startBlock
    ts = int(block['timestamp'])
    oldDay = (datetime.utcfromtimestamp(ts).strftime('%A'))
    oldTime = (datetime.utcfromtimestamp(ts).strftime('%H%M'))
    blockList = []
    dataOutput = {}
    lastFound = oldDay
    newBlock = int(newBlock + currentSearch)


    while(newBlock < currentBlock):
        #Binary search for the next day
        block = web3Fuse.eth.getBlock(block_identifier=newBlock)
        ts = int(block['timestamp'])
        Day = (datetime.utcfromtimestamp(ts).strftime('%A'))
        Time = (datetime.utcfromtimestamp(ts).strftime('%H%M'))
        dt = (datetime.utcfromtimestamp(ts).strftime('%Y%m%d'))

        if Time == '0000':
            print(str(newBlock))
            blockList.append(newBlock)
            currentSearch = oneDay
            oldDay = Day
            #grab the stats
            totalStaked,numVals,numDelegates = countDelegates(newBlock)
            dataOutput[dt] = {}
            dataOutput[dt]['delegates'] = numDelegates
            dataOutput[dt]['numVals'] = numVals
            dataOutput[dt]['totalStaked'] = totalStaked
        else:
            if Day != oldDay:
                if lastFound != Day:
                    currentSearch = abs((currentSearch / 2)) * -1
                else:
                    currentSearch = abs((currentSearch / 2))
            else:
                currentSearch = abs((currentSearch / 2))
        newBlock = int(newBlock + currentSearch)

    with open("delegates.json", 'w') as fp:
        json.dump(dataOutput, fp)

    with open("delegates.csv", "w") as csv_file:
        csv_file.write("date,delegates,numVals,totalStaked\n")

        for key in dataOutput:
            keyDate = key[0:4] + '-' + key[4:6] + '-' + key[6:8]
            line = str(keyDate) + ','
            for valKey in dataOutput[key]:
                line += str(dataOutput[key][valKey]) + ','

            line = line[:-1]

            csv_file.write(line + '\n')