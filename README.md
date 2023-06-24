1. User can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner
4. yarn add @chainlink/contracts ----solve import 0.8

How do we want to test this?

1. 'mainnet-fork'
2. 'development' with mocks
3. 'testnet'

Setting
1. .env:
export PRIVATE_KEY=(wallet private_key)
export WEB3_INFURA_PROJECT_ID=(infura.io sign up)
export ETHERSCAN_TOKEN=(etherscan apply api)
2. don't forget import dotenv or load_dot

Warning!
When you use development test,you use:
import "node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
But if you use public testnet,you use root dir:
import "/Users/a1111/smartcontract-lottery/node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
you know it costed me one hour!!!!

3. vrf_coordinator version is important.this is v1 version.if you use wrong version,testnet can't pass.
vrf_coordinator: '0x2bce784e69d2Ff36c71edcB9F88358dB0DfB55b4'
link_token: '0x326C977E6efc84E512bB9C30f76E30c160eD06FB'
keyhash: '0x0476f9a745b61ea5c0ab224d3a6e4c99f0b02fce4da01143a4f70aa80ae76e8a'
fee: 100000000000000000
# v2  keyhash: '0x79d3d8832d904592c0bf9818b621522c988bb8b0c05cdc3b15aea1b6e8db0c15' please know it
please read bug weblink,you will know what i say.
https://docs.chain.link/docs/vrf/v1/supported-networks/
https://stackoverflow.com/questions/71194882/execution-reverted-during-call-this-transaction-will-likely-revert-if-you-wish

4. def test_can_pick_winner(): This test i give more sleep time.Because when you use goerli,chainlink respone more time.so i change 60 to 240.slove problem that winner is 0x0000000000....





