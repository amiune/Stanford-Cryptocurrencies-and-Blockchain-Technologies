from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC, 
    bob_secret_key_BTC, bob_public_key_BTC, bob_address_BTC,
    alice_secret_key_BCY, alice_public_key_BCY, alice_address_BCY, 
    bob_secret_key_BCY, bob_public_key_BCY, bob_address_BCY,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction



def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    private_key = my_private_key
    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    amount_to_send = 0.01983259 - 0.0003 # amount of BTC in the output you're splitting minus fee
    # fee estimates: https://live.blockcypher.com/btc-testnet/

    txid_to_spend = ('6d391ee124233f37d3d95e79fce5c4ce07df898b5ef8dc828b1573295aa8d962')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    n = 4 # number of outputs to split the input into
    # For n, choose a number larger than what you immediately need, 
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)


"""
python split_test_coins.py


201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "4ea7bb03f93d7d218ec56f39bc5850972244daf7a047c4d28b83b56259349e50",
    "addresses": [
      "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
    ],
    "total": 1953256,
    "fees": 30003,
    "size": 294,
    "vsize": 294,
    "preference": "high",
    "relayed_by": "190.17.120.197",
    "received": "2021-08-02T18:31:25.830594559Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 4,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "6d391ee124233f37d3d95e79fce5c4ce07df898b5ef8dc828b1573295aa8d962",
        "output_index": 0,
        "script": "483045022100e6112acb20296c077dbead4050bd6e4c9bc54e11d4eda1859f6ec2ea319052d302205b008b740684cd24cb4e69b7fa583c13ecb9b15bdb1d99a2b6b45f091a878cb0012102c66bc4da0c1d1a0746675fb109ae3ca7d92f31a1cf47489d967560ceae045245",
        "output_value": 1983259,
        "sequence": 4294967295,
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2062823
      }
    ],
    "outputs": [
      {
        "value": 488314,
        "script": "76a914c4a7b22b95deb94da3b9bd17b5e9ebc6a72806eb88ac",
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 488314,
        "script": "76a914c4a7b22b95deb94da3b9bd17b5e9ebc6a72806eb88ac",
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 488314,
        "script": "76a914c4a7b22b95deb94da3b9bd17b5e9ebc6a72806eb88ac",
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 488314,
        "script": "76a914c4a7b22b95deb94da3b9bd17b5e9ebc6a72806eb88ac",
        "addresses": [
          "mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}

"""