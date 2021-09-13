from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG
    ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        signature, public_key
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00488314 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)


"""
python Q1.py

201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "8143b1022e846f32efdeb3860852e6e13dab99d8e6328f117cc141410cef34b1",
    "addresses": [
      "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS",
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 458314,
    "fees": 30000,
    "size": 191,
    "vsize": 191,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-07T20:00:34.073529704Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50",
        "output_index": 0,
        "script": "4730440220558cd2fa93b916b4b2959253976e36d567b34d161fe717419bd96beff91031d002205f3e9ef0ffa8820358783da57c0ee6631645f1748e9a6bc821b7535a4e985a1d012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245",
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