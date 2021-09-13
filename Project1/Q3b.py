from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q3a import (Q3a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 3a.
    return [
        OP_0, bank_sig, cust1_sig
    ]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00488314 - 0.0009 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '0a609bade76d5a5491de947ad0ffce264b4b958cee7d93ebc6693f2f28d31bc0')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)



"""
python Q3b.py

201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "ca72f19b74598e28a6ddb0128379fdba4b2fdd91f2ffdfdbbf88d50086c70a06",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 398314,
    "fees": 60000,
    "size": 231,
    "vsize": 231,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-11T22:23:23.338876213Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "0a609bade76d5a5491de947ad0ffce264b4b958cee7d93ebc6693f2f28d31bc0",
        "output_index": 0,
        "script": "00483045022100c19fcc1c89c8990765bf89e8faeb2a93b124a19556290a4c0bd318e6d7dcc15d022050055612ecb8cc7e8e10c33adaffb2d9c2a59376bfa401fa083469bfe6bf7bd10147304402204c470e4d7dec668d86b216442ecf0c0d3738e36d613294be8d1d4a2aaa550c7f02207c9fbf0c8acf76b7c5dacb4bace829243ba7f168cc1730e319330643960ff6b401",
        "output_value": 458314,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 2063751
      }
    ],
    "outputs": [
      {
        "value": 398314,
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