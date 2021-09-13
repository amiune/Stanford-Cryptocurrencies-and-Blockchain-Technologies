from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00114186 - 0.0003 # amount of BTC in the output you're sending minus fee
txid_to_spend = (
        '481b3d72def67fa55d5b3febdd5adf3eef316c1804afce364d51ffacd658309e')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [
        6390, -3360
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)


"""
python Q2b.py

201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "b1d251a251ca90fc9b9fc93c3cebdded05e57df07f991728ca3c6cbcab104bbf",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 84186,
    "fees": 30000,
    "size": 91,
    "vsize": 91,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-07T21:31:56.136248192Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "481b3d72def67fa55d5b3febdd5adf3eef316c1804afce364d51ffacd658309e",
        "output_index": 0,
        "script": "02f61802208d",
        "output_value": 114186,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 2063749
      }
    ],
    "outputs": [
      {
        "value": 84186,
        "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
        "addresses": [
          "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}
"""