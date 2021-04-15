CONTRACT_ABI = [
  {
    "constant": True,
    "inputs": [],
    "name": "getLastSnapshotTakenAtBlock",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_p",
        "type": "uint256"
      }
    ],
    "name": "pendingValidatorsAtPosition",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_snapshotId",
        "type": "uint256"
      }
    ],
    "name": "getSnapshotAddresses",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_newAddress",
        "type": "address"
      }
    ],
    "name": "setProxyStorage",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_address",
        "type": "address"
      },
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "delegatedAmount",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "SNAPSHOTS_PER_CYCLE",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "pendingValidatorsLength",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "newValidatorSetLength",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "DECIMALS",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "isInitialized",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "currentValidatorsLength",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getMinStake",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_p",
        "type": "uint256"
      }
    ],
    "name": "currentValidatorsAtPosition",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "newValidatorSet",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      },
      {
        "name": "_rewardAmount",
        "type": "uint256"
      }
    ],
    "name": "getDelegatorsForRewardDistribution",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      },
      {
        "name": "",
        "type": "uint256[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "MAX_VALIDATORS",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getMaxValidators",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "CYCLE_DURATION_BLOCKS",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getSnapshotsPerCycle",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "requiredSignatures",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "delegators",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "isFinalized",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "DEFAULT_VALIDATOR_FEE",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getCurrentCycleStartBlock",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "totalStakeAmount",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "validatorFee",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      },
      {
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "isDelegator",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "currentValidators",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getCycleDurationBlocks",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "pendingValidators",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getCurrentCycleEndBlock",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "stakeAmount",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "MIN_STAKE",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "delegatorsLength",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getNextSnapshotId",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      },
      {
        "name": "_p",
        "type": "uint256"
      }
    ],
    "name": "delegatorsAtPosition",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getProxyStorage",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "shouldEmitInitiateChange",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "isValidator",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "isPendingValidator",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "payable": True,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "name": "newSet",
        "type": "address[]"
      }
    ],
    "name": "ChangeFinalized",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [],
    "name": "ShouldEmitInitiateChange",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "parentHash",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "newSet",
        "type": "address[]"
      }
    ],
    "name": "InitiateChange",
    "type": "event"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_initialValidator",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getValidators",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "finalizeChange",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "stake",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "delegate",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "withdraw",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      },
      {
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "withdraw",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "cycle",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "emitInitiateChange",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "setValidatorFee",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

blockRewardCon = [
  {
    "constant": True,
    "inputs": [],
    "name": "DECIMALS",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "isInitialized",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "INFLATION",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "BLOCKS_PER_YEAR",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "name": "receivers",
        "type": "address[]"
      },
      {
        "indexed": False,
        "name": "rewards",
        "type": "uint256[]"
      }
    ],
    "name": "Rewarded",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "RewardedOnCycle",
    "type": "event"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_supply",
        "type": "uint256"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "benefactors",
        "type": "address[]"
      },
      {
        "name": "kind",
        "type": "uint16[]"
      }
    ],
    "name": "reward",
    "outputs": [
      {
        "name": "",
        "type": "address[]"
      },
      {
        "name": "",
        "type": "uint256[]"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "onCycleEnd",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "emitRewardedOnCycle",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getTotalSupply",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getRewardedOnCycle",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getInflation",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getBlocksPerYear",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getBlockRewardAmount",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_validator",
        "type": "address"
      }
    ],
    "name": "getBlockRewardAmountPerValidator",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getProxyStorage",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "shouldEmitRewardedOnCycle",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  }
]
