from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        OP_2DUP, OP_ADD, 3030, OP_EQUALVERIFY, OP_SUB, 9750, OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00488314 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)


"""
python Q2a.py

201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "481b3d72def67fa55d5b3febdd5adf3eef316c1804afce364d51ffacd658309e",
    "addresses": [
      "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
    ],
    "total": 114186,
    "fees": 374128,
    "size": 178,
    "vsize": 178,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-07T21:14:48.7969472Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50",
        "output_index": 1,
        "script": "483045022100fb08e1a5f61b5af2badb57307a63cb8adc17cf0de82ad529c8a1ec9784d1afe7022074f42171e5a32b2f1117e941c24cf180b131751958ccb88a4ba784a92f356faa012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245",
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
        "value": 114186,
        "script": "6e9302d60b889402162687",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
"""