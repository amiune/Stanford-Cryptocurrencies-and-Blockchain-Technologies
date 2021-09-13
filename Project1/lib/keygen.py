from os import urandom
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

SelectParams('testnet')

seckey = CBitcoinSecret.from_secret_bytes(urandom(32))

print("Private key: %s" % seckey)
print("Address: %s" % P2PKHBitcoinAddress.from_pubkey(seckey.pub))

#MyKey
#Private key: cQ32SLNj3dXGRgjD1nBNctH9AqxkjuK8KGFvsW2xKHMjfTWuHDoc
#Address: mySmdNcxA36m9QK4B29VG5UV5knGRxGmSS
#faucet to this address tx id: 6d391ee124233f37d3d95e79fce5c4ce07df898b5ef8dc828b1573295aa8d962

#AliceKey
#Private key: cNTgg87wyn4GVC1u9F9GWzMYAqNGaVEWnpmchn8MUUGDyfeFbCUp
#Address: n4j5D4zvZqUdrdNpEeTtoQZNXLMSqdGio2
#faucet to this address tx id: 

#BobKey
#Private key: cPSrtbq3CjjQ8nSVrVdnA4gvwofbrSL3AgndQfXGHaCaCgW3Tnu6
#Address: mt9bjsLjdjr4ai855PC8gfpJM5V9i8DUoc

#Alice Blockcypher 
#curl -X POST "https://api.blockcypher.com/v1/bcy/test/addrs?token=5a7aff3d5db94189a219691e62b40310"
#{
#  "private": "2136d81b714ccc47737f20d4af1d7300b055c6227cf898b5095a27e719d36040",
#  "public": "02d9adf677d0c642ae6e46a480802ad5ec790604ba0b173fabf2eb6388b7004ced",
#  "address": "BvsoBe7DUeY1N7iYtmm4XFVTPQyzCxVAFr",
#  "wif": "BpSbTXMeuSWHCpyMpeBbbS6xXRZFaVfSeZAon744MSDKsCC7B6sB"
#}

#Bob Blockcypher 
#curl -X POST "https://api.blockcypher.com/v1/bcy/test/addrs?token=5a7aff3d5db94189a219691e62b40310"
#{
#  "private": "e34ada9f06ff86b230934f0fbde72af6f9bf2c12a38f532e6747f8743f20f98a",
#  "public": "03250c8df61d01ac8ad9d6aa8330ead69d9118a47dfbdb4227cee72fbe5460b485",
#  "address": "BvpEHkaShc9RHiWCLKQZKETb4aaaYmjQmA",
#  "wif": "BvwrgsXsoLAZw7Cu15FFdzCtBDPyQ7Wy7uViomvRu6VaBGS9TurG"
#}

#curl -d '{"address": "BvpEHkaShc9RHiWCLKQZKETb4aaaYmjQmA", "amount": 100000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=5a7aff3d5db94189a219691e62b40310
#{
#  "tx_ref": "5ec25cbd595c2583cc80489d3d4f3c4145a91fb23e9c47c6a4670f2ab2fb94fc"
#}
#curl -d '{"address": "BvpEHkaShc9RHiWCLKQZKETb4aaaYmjQmA", "amount": 100000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=5a7aff3d5db94189a219691e62b40310
#{
#  "tx_ref": "be60664c235d91a37e0846e74e1ba0efbfb2cf2231df39842b8558f20fdeca79"
#}

#Question 3:
#Customer1
#Private key: cQE2jH3GRYuyF8aAVdbiH78dQsmdAELg5S2fZnfn51Ht5SryENqG
#Address: mt9bNZnoAxauKrbEM31UFrDCwMgDqwce4R
#Customer2
#Private key: cMzfMEMJPT3KNufppadVKKcMAYHKxuh2Cz3t2BT6XErY2irzGhEy
#Address: mgyhg4SMxACVaTsABUpkSi5tQUe4RYGDEh
#Customer3 
#Private key: cN9aH1SD472jfqkxxFBF7DZyTB21Q6AdZQgR63DrX3kPnGe2RfjX
#Address: mw9rwtp8VdNXHS4ULGvr6WQS8xFKw6E7p3
