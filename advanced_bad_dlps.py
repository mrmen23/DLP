import requests
from web3 import Web3
import requests
from datetime import datetime, timedelta

# Connect to the Web3 provider
provider_url = "https://rpc.moksha.vana.org"
web3 = Web3(Web3.HTTPProvider(provider_url))

# Check connection
if not web3.is_connected():
    print("Error: Could not connect to the blockchain.")
else:
    print("Connected to blockchain successfully.")

DLP_Root_implementation_abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "target",
                "type": "address"
            }
        ],
        "name": "AddressEmptyCode",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "AlreadyDistributed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ArityMismatch",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "CheckpointUnorderedInsertion",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "CurrentEpochNotCreated",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "ERC1967InvalidImplementation",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967NonPayable",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EnforcedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EpochEnded",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EpochFinalised",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EpochNotEnded",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EpochNotStarted",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ExpectedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FailedInnerCall",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidDlpList",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidDlpStatus",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidInitialization",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidPerformancePercentages",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidStakeAmount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidStakersPercentage",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidUnstakeAmount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotAllowed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotDlpOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotInitializing",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NothingToClaim",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "PreviousEpochNotFinalised",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ReentrancyGuardReentrantCall",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint8",
                "name": "bits",
                "type": "uint8"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "SafeCastOverflowedUintDowncast",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TooManyDlps",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UUPSUnauthorizedCallContext",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "slot",
                "type": "bytes32"
            }
        ],
        "name": "UUPSUnsupportedProxiableUUID",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "DlpDeregistered",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "dlpAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "ownerAddress",
                "type": "address"
            }
        ],
        "name": "DlpRegistered",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "stakersPercentage",
                "type": "uint256"
            }
        ],
        "name": "DlpStakersPercentageUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            }
        ],
        "name": "EpochCreated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "isFinalised",
                "type": "bool"
            }
        ],
        "name": "EpochPerformancesSaved",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newEpochRewardAmount",
                "type": "uint256"
            }
        ],
        "name": "EpochRewardAmountUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newEpochSize",
                "type": "uint256"
            }
        ],
        "name": "EpochSizeUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint64",
                "name": "version",
                "type": "uint64"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newMaxNumberOfRegisteredDlps",
                "type": "uint256"
            }
        ],
        "name": "MaxNumberOfRegisteredDlpsUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newMinDlpStakeAmount",
                "type": "uint256"
            }
        ],
        "name": "MinDlpStakeAmountUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newNumberOfTopDlps",
                "type": "uint256"
            }
        ],
        "name": "NumberOfTopDlpsUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferStarted",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newTtfPercentage",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newTfcPercentage",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newVduPercentage",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newUwPercentage",
                "type": "uint256"
            }
        ],
        "name": "PerformancePercentagesUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "staker",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "Staked",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "staker",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "claimAmount",
                "type": "uint256"
            }
        ],
        "name": "StakerDlpEpochRewardClaimed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "staker",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "Unstaked",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "UPGRADE_INTERFACE_VERSION",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "acceptOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "addRewardForDlps",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "claimReward",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "lastEpochToClaim",
                "type": "uint256"
            }
        ],
        "name": "claimRewardUntilEpoch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "stakerAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "claimableAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "createEpochs",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "blockNumber",
                "type": "uint256"
            }
        ],
        "name": "createEpochsUntilBlockNumber",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "deregisterDlp",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "dlpOwnerAmount",
                "type": "uint256"
            }
        ],
        "name": "distributeStakeAfterDeregistration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            }
        ],
        "name": "dlpEpochs",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "ttf",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "tfc",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "vdu",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "uw",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "isTopDlp",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "rewardAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakersPercentage",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.DlpEpochInfo",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "dlpAddress",
                "type": "address"
            }
        ],
        "name": "dlpIds",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "dlps",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "dlpAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "ownerAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "enum IDataLiquidityPoolsRoot.DlpStatus",
                        "name": "status",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint256",
                        "name": "registrationBlockNumber",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "grantedAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakersPercentage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.DlpResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "dlpAddress",
                "type": "address"
            }
        ],
        "name": "dlpsByAddress",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "dlpAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "ownerAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "enum IDataLiquidityPoolsRoot.DlpStatus",
                        "name": "status",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint256",
                        "name": "registrationBlockNumber",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "grantedAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakersPercentage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.DlpResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "dlpsCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "epochRewardAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "epochSize",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            }
        ],
        "name": "epochs",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "startBlock",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "endBlock",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "reward",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "isFinalised",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "dlpIds",
                        "type": "uint256[]"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.EpochInfo",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "epochsCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "estimatedDlpReward",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "historyRewardEstimation",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "stakeRewardEstimation",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256[]",
                "name": "dlpIds",
                "type": "uint256[]"
            }
        ],
        "name": "forceRemoveDlps",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "from",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "to",
                "type": "uint256"
            }
        ],
        "name": "getAllDlpAddressesThatAreNotAContract",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "dlpAddress",
                        "type": "address"
                    }
                ],
                "internalType": "struct DataLiquidityPoolsRootImplementation.DlpResponse2[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "from",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "to",
                "type": "uint256"
            }
        ],
        "name": "getAllDlps",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "dlpAddress",
                        "type": "address"
                    }
                ],
                "internalType": "struct DataLiquidityPoolsRootImplementation.DlpResponse2[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address payable",
                        "name": "ownerAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxNumberOfRegisteredDlps",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "numberOfTopDlps",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "minDlpStakeAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "startBlock",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "epochSize",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "epochRewardAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "ttfPercentage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "tfcPercentage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "vduPercentage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "uwPercentage",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct DataLiquidityPoolsRootImplementation.InitParams",
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "isContract",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "maxNumberOfRegisteredDlps",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "minDlpStakeAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "numberOfTopDlps",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pendingOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "dlpAddress",
                "type": "address"
            },
            {
                "internalType": "address payable",
                "name": "dlpOwnerAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "stakersPercentage",
                "type": "uint256"
            }
        ],
        "name": "registerDlp",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "dlpAddress",
                "type": "address"
            },
            {
                "internalType": "address payable",
                "name": "dlpOwnerAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "stakersPercentage",
                "type": "uint256"
            }
        ],
        "name": "registerDlpWithGrant",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "registeredDlps",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "registeredDlpsCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "dlpId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "ttf",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "tfc",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "vdu",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "uw",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.DlpPerformance[]",
                "name": "dlpPerformances",
                "type": "tuple[]"
            },
            {
                "internalType": "bool",
                "name": "isFinalised",
                "type": "bool"
            }
        ],
        "name": "saveEpochPerformances",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "stake",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "staker",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "epochId",
                "type": "uint256"
            }
        ],
        "name": "stakerDlpEpochs",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "dlpId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "epochId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "rewardAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "claimAmount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.StakerDlpEpochInfo",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "stakerAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "stakerDlps",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "dlpId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastClaimedEpochId",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.StakerDlpInfo",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "stakerAddress",
                "type": "address"
            }
        ],
        "name": "stakerDlpsList",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "dlpId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stakeAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastClaimedEpochId",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPoolsRoot.StakerDlpInfo[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "staker",
                "type": "address"
            }
        ],
        "name": "stakerDlpsListCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tfcPercentage",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "numberOfDlps",
                "type": "uint256"
            }
        ],
        "name": "topDlpIds",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalDlpsRewardAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "ttfPercentage",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "unstake",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "stakerAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            }
        ],
        "name": "unstakebleAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "dlpId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "stakersPercentage",
                "type": "uint256"
            }
        ],
        "name": "updateDlpStakersPercentage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newEpochRewardAmount",
                "type": "uint256"
            }
        ],
        "name": "updateEpochRewardAmount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newEpochSize",
                "type": "uint256"
            }
        ],
        "name": "updateEpochSize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newMaxNumberOfRegisteredDlps",
                "type": "uint256"
            }
        ],
        "name": "updateMaxNumberOfRegisteredDlps",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newMinDlpStakeAmount",
                "type": "uint256"
            }
        ],
        "name": "updateMinDlpStakeAmount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newNumberOfTopDlps",
                "type": "uint256"
            }
        ],
        "name": "updateNumberOfTopDlps",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newTtfPercentage",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "newTfcPercentage",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "newVduPercentage",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "newUwPercentage",
                "type": "uint256"
            }
        ],
        "name": "updatePerformancePercentages",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "uwPercentage",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "vduPercentage",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "version",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    }
]

# Initialize Web3 connection
dlp_root_contract = web3.eth.contract(address="0xf408A064d640b620219F510963646Ed2bD5606BB", abi=DLP_Root_implementation_abi)

# Function to fetch and pretty print DLPs
def get_all_dlps_addresses():
    try:
        dlp_data = dlp_root_contract.functions.getAllDlps(0, 500).call()
        addresses = [address for _, address in dlp_data]  # Save addresses to an array
        print(len(addresses))
        return addresses
    
    except Exception as e:
        print(f"Error fetching all DLPs: {e}")
        return []




# Load implementation ABI (assuming this is defined somewhere)
implementation_abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "target",
                "type": "address"
            }
        ],
        "name": "AddressEmptyCode",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "AddressInsufficientBalance",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ECDSAInvalidSignature",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "length",
                "type": "uint256"
            }
        ],
        "name": "ECDSAInvalidSignatureLength",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "s",
                "type": "bytes32"
            }
        ],
        "name": "ECDSAInvalidSignatureS",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "ERC1967InvalidImplementation",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967NonPayable",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EnforcedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ExpectedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FailedInnerCall",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FileAlreadyAdded",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidAttestator",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidInitialization",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidProof",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotInitializing",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ReentrancyGuardReentrantCall",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "SafeERC20FailedOperation",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UUPSUnauthorizedCallContext",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "slot",
                "type": "bytes32"
            }
        ],
        "name": "UUPSUnsupportedProxiableUUID",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256"
            }
        ],
        "name": "FileInvalidated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newFileRewardFactor",
                "type": "uint256"
            }
        ],
        "name": "FileRewardFactorUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256"
            }
        ],
        "name": "FileValidated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint64",
                "name": "version",
                "type": "uint64"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "newMasterKey",
                "type": "string"
            }
        ],
        "name": "MasterKeyUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferStarted",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "newProofInstruction",
                "type": "string"
            }
        ],
        "name": "ProofInstructionUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "contributorAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "proofIndex",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "rewardAmount",
                "type": "uint256"
            }
        ],
        "name": "RewardRequested",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "UPGRADE_INTERFACE_VERSION",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "acceptOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "contributorsRewardAmount",
                "type": "uint256"
            }
        ],
        "name": "addRewardsForContributors",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "contributorAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "contributorFiles",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "fileId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "proofIndex",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "rewardAmount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPool.FileResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "contributorAddress",
                "type": "address"
            }
        ],
        "name": "contributorInfo",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "contributorAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "filesListCount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPool.ContributorInfoResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "contributors",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "contributorAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "filesListCount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPool.ContributorInfoResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contributorsCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "dataRegistry",
        "outputs": [
            {
                "internalType": "contract IDataRegistry",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "fileRewardFactor",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256"
            }
        ],
        "name": "files",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "fileId",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "proofIndex",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "rewardAmount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IDataLiquidityPool.FileResponse",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "filesListAt",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "filesListCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "ownerAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "tokenAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "dataRegistryAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "teePoolAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "masterKey",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "proofInstruction",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "fileRewardFactor",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct DataLiquidityPoolImplementation.InitParams",
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "masterKey",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes[]",
                "name": "data",
                "type": "bytes[]"
            }
        ],
        "name": "multicall",
        "outputs": [
            {
                "internalType": "bytes[]",
                "name": "results",
                "type": "bytes[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pendingOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proofInstruction",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "proofIndex",
                "type": "uint256"
            }
        ],
        "name": "requestReward",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "teePool",
        "outputs": [
            {
                "internalType": "contract ITeePool",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "token",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalContributorsRewardAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newFileRewardFactor",
                "type": "uint256"
            }
        ],
        "name": "updateFileRewardFactor",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "newMasterKey",
                "type": "string"
            }
        ],
        "name": "updateMasterKey",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "newProofInstruction",
                "type": "string"
            }
        ],
        "name": "updateProofInstruction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newTeePool",
                "type": "address"
            }
        ],
        "name": "updateTeePool",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "version",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    }
]


# Load DLP addresses from a text file
# def load_dlp_addresses(filename, start_line=0):
#     """Reads a file starting from a specific line with one address per line and returns them as a list."""
#     with open(filename, 'r') as file:
#         return [line.strip() for i, line in enumerate(file) if i >= start_line and line.strip()]

# Calculate readable time since last transaction
def time_since_last_transaction(timestamp):
    """Returns a string indicating how long ago the last transaction occurred."""
    last_time = datetime.fromtisoformat(timestamp[:-1])  # Convert timestamp to datetime
    now = datetime.now()
    delta = now - last_time

    if delta.days > 0:
        return f"{delta.days} day(s) ago"
    elif delta.seconds // 3600 > 0:
        return f"{delta.seconds // 3600} hour(s) ago"
    else:
        return f"{delta.seconds // 60} minute(s) ago"

# Fetch blockchain data for each DLP address
def get_dlp_data(proxy_address):
    try:
        contract = web3.eth.contract(address=proxy_address, abi=implementation_abi)

        # Call the filesListCount and contributorsCount methods
        files_list_count = contract.functions.filesListCount().call()
        contributors_count = contract.functions.contributorsCount().call()

        # VanaScan API URL for logs and transactions
        logs_url = f'https://api.vanascan.io/api/v2/addresses/{proxy_address}/logs'
        transactions_url = f'https://api.vanascan.io/api/v2/addresses/{proxy_address}/transactions'

        # Fetch logs and transactions
        logs_response = requests.get(logs_url)
        transactions_response = requests.get(transactions_url)

        # Check if responses are successful
        logs_response.raise_for_status()
        transactions_response.raise_for_status()

        # Count logs and transactions
        log_count = len(logs_response.json().get('items', []))
        transaction_items = transactions_response.json().get('items', [])
        transaction_count = len(transaction_items)

        # Get the timestamp of the last transaction if any
        last_transaction_time = transaction_items[-1]['timestamp'] if transaction_items else None

        last_transaction = time_since_last_transaction(last_transaction_time)

        # Output details for logging
        print(f"[INFO] Address: {proxy_address}")
        print(f"[INFO] Files Count: {files_list_count}, Contributors Count: {contributors_count}")
        print(f"[INFO] Log Count: {log_count}, Transaction Count: {transaction_count}")
        if last_transaction_time:
            print(f"[INFO] Last Transaction: {time_since_last_transaction(last_transaction_time)}")

        return files_list_count, contributors_count, log_count, transaction_count, last_transaction
    except Exception as e:
        print(f"[ERROR] Error fetching data for {proxy_address}: {e}")
        return None

# Main function to read each DLP and print counts; log "bad" addresses
def process_dlp_files_and_contributors(filename):
    dlp_addresses = get_all_dlps_addresses()

    # Open the bad_dlp_addresses file in append mode
    with open("bad_dlp_addresses_extended.txt", "a") as bad_file:
        for address in dlp_addresses:
            print(f"[INFO] Fetching data for {address}...")
            data = get_dlp_data(address)

            if data:
                files_list_count, contributors_count, log_count, transaction_count, last_transaction = data
                
                # Prepare the summary line
                summary_line = (f"files: {files_list_count}, contributors: {contributors_count}, "
                                f"logs: {log_count}, transactions: {transaction_count}, last transaction: {last_transaction}\n")
                
                # Write the summary line to the main output file
                with open(filename, "a") as output_file:
                    output_file.write(summary_line)

                # Check if it meets "bad DLP" criteria
                if (files_list_count == 0 and contributors_count == 0 and 
                    log_count < 4 and transaction_count < 4):
                    print(f"[WARNING] Address {address} qualifies as a bad DLP: "
                          f"Files: {files_list_count}, Contributors: {contributors_count}, "
                          f"Logs: {log_count}, Transactions: {transaction_count}")
                    bad_file.write(f"{address}\n")
                    
                # Write the address to the main output file
                with open(filename, "a") as output_file:
                    output_file.write(f"{address}\n")
            else:
                print(f"[ERROR] Could not retrieve data for {address}")

# Run the script
#dlp_file = "dlp_addresses.txt"
process_dlp_files_and_contributors("peekaboo.txt")
