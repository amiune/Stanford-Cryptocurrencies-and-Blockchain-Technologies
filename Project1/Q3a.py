from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cQE2jH3GRYuyF8aAVdbiH78dQsmdAELg5S2fZnfn51Ht5SryENqG')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cMzfMEMJPT3KNufppadVKKcMAYHKxuh2Cz3t2BT6XErY2irzGhEy')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cN9aH1SD472jfqkxxFBF7DZyTB21Q6AdZQgR63DrX3kPnGe2RfjX')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        OP_3DUP, OP_3DUP, 
        2, my_public_key, cust1_public_key, 2,  OP_CHECKMULTISIG,
        OP_NOTIF,
            2, my_public_key, cust2_public_key, 2,  OP_CHECKMULTISIG,
            OP_NOTIF,
                2, my_public_key, cust3_public_key, 2,  OP_CHECKMULTISIG,
            OP_ENDIF,
        OP_ENDIF
]

######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00488314 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)



"""
Q3a_txout_scriptPubKey = [
        OP_3DUP, OP_3DUP, 
        2, my_public_key, cust1_public_key, 2,  OP_CHECKMULTISIG,
        OP_NOTIF,
            2, my_public_key, cust2_public_key, 2,  OP_CHECKMULTISIG,
            OP_NOTIF,
                2, my_public_key, cust3_public_key, 2,  OP_CHECKMULTISIG,
            OP_ENDIF,
        OP_ENDIF
]


201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "0a609bade76d5a5491de947ad0ffce264b4b958cee7d93ebc6693f2f28d31bc0",
    "addresses": [
      "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
    ],
    "total": 458314,
    "fees": 30000,
    "size": 385,
    "vsize": 385,
    "preference": "medium",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-07T21:34:00.036698269Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50",
        "output_index": 2,
        "script": "473044022023228cb48e9ea06b63af69de4945773f1358b4c691c48f8c084047687e34e46002203a3340c97d922d3f0105a98ce9c6c5d49e676f1c00b69a7e2bed86001c62511b012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245",
        "output_value": 488314,
        "sequence": 4294967295,
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2062863
      }
    ],
    "outputs": [
      {
        "value": 458314,
        "script": "6f6f522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521020b3fd5a6b98cdcd7885ce13cd312eb732e72923c4adc4550c1eb9e77ef05ed1152ae64522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae0452452103089921ed07d627dab78937ca305886b112ce6b407590e67214bc7d439408edca52ae64522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521037e2218cee7f722f89e609834de47bf7546fcf2709d5f5556a5c1417ba51a2faf52ae6868",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}

raw transaction
0100000001509e345962b5838bd2c447a0f7da4422975058bc396fc58e217d3df903bba74e020000006a473044022023228cb48e9ea06b63af69de4945773f1358b4c691c48f8c084047687e34e46002203a3340c97d922d3f0105a98ce9c6c5d49e676f1c00b69a7e2bed86001c62511b012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245ffffffff014afe060000000000db6f6f522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521020b3fd5a6b98cdcd7885ce13cd312eb732e72923c4adc4550c1eb9e77ef05ed1152ae64522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae0452452103089921ed07d627dab78937ca305886b112ce6b407590e67214bc7d439408edca52ae64522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521037e2218cee7f722f89e609834de47bf7546fcf2709d5f5556a5c1417ba51a2faf52ae686800000000


Q3a_txout_scriptPubKey = [
      2, my_public_key, cust1_public_key, 2,  OP_CHECKMULTISIG
]

201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "25ffda56fbacb0de1383a3866de0162de73db00cf497bbe20e7b36279a4bb374",
    "addresses": [
      "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS",
      "zFLdyE1L2mgT1EpEWPtq9q8EAF2NdKi84g"
    ],
    "total": 458314,
    "fees": 30000,
    "size": 238,
    "vsize": 238,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-10T19:56:47.2726342Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50",
        "output_index": 3,
        "script": "483045022100e22bac1c503ee2ab34a01381ef964578842c38a601270d573b3b0414428b032002205b5f8ab0e9a2d4f8c0a849f06e3ba0460944e14e1c164b4665e6e98e6cc96934012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245",
        "output_value": 488314,
        "sequence": 4294967295,
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2062863
      }
    ],
    "outputs": [
      {
        "value": 458314,
        "script": "522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521020b3fd5a6b98cdcd7885ce13cd312eb732e72923c4adc4550c1eb9e77ef05ed1152ae",
        "addresses": [
          "zFLdyE1L2mgT1EpEWPtq9q8EAF2NdKi84g"
        ],
        "script_type": "pay-to-multi-pubkey-hash"
      }
    ]
  }
}

raw transaction:
0100000001509e345962b5838bd2c447a0f7da4422975058bc396fc58e217d3df903bba74e030000006b483045022100e22bac1c503ee2ab34a01381ef964578842c38a601270d573b3b0414428b032002205b5f8ab0e9a2d4f8c0a849f06e3ba0460944e14e1c164b4665e6e98e6cc96934012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245ffffffff014afe06000000000047522102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae04524521020b3fd5a6b98cdcd7885ce13cd312eb732e72923c4adc4550c1eb9e77ef05ed1152ae00000000

"""


"""
Playing with IF and ELSE in scripts:

4 3 OP_ADD 9 OP_EQUAL 
OP_IF 
	OP_TRUE
OP_ELSE 
	4 4 OP_ADD 9 OP_EQUAL  
    OP_NOTIF 
	    4 5 OP_ADD 9 OP_EQUAL
	OP_ENDIF
OP_ENDIF


4 5 OP_3DUP
OP_ADD 7 OP_EQUAL 
OP_NOTIF
    OP_ADD 8 OP_EQUAL
OP_ENDIF
OP_NOTIF
    OP_ADD 9 OP_EQUAL
OP_ENDIF


btcdeb '[4 3 OP_ADD 9 OP_EQUAL OP_NOTIF 4 4 OP_ADD 9 OP_EQUAL OP_ENDIF OP_NOTIF 4 5 OP_ADD 9 OP_EQUAL OP_ENDIF]'

btcdeb '[4 5 OP_2DUP OP_2DUP OP_ADD 9 OP_EQUALVERIFY OP_NOTIF OP_ADD 8 OP_EQUALVERIFY OP_ENDIF OP_NOTIF OP_ADD 9 OP_EQUALVERIFY OP_ENDIF]'

"""