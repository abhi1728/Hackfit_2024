var web3;
var address = "0x9469ef1E5518139714834C1d738620dD962D2B96";

async function Connect() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    web3 = new Web3(window.ethereum);
}

if (typeof web3 !== 'undefined') {
    web3 = new Web3(window.ethereum);
} else {
    web3 = new Web3(new Web3.providers.HttpProvider("HTTP://127.0.0.1:7545"));
}

var abi = [
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "amt",
				"type": "int256"
			}
		],
		"name": "depositMoney",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "amt",
				"type": "int256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
];

var contract = new web3.eth.Contract(abi, address);

function deposit() {
    var inputval = document.getElementById('amount').value;

    web3.eth.getAccounts().then(function(accounts) {
        return contract.methods.depositMoney(inputval).send({ from: accounts[0] });
    }).then(function(tmp) {
        $("#amount").val("");
    }).catch(function(error) {
        alert(error);
    });
}

function withdraw() {
    var inputval = document.getElementById('amount').value;

    web3.eth.getAccounts().then(function(accounts) {
        return contract.methods.withdraw(inputval).send({ from: accounts[0] });
    }).then(function(tmp) {
        $("#amount").val("");
    }).catch(function(error) {
        alert(error);
    });
}

function show_balance() {
    contract.methods.getBalance().call().then(function(balance) {
        $("#balance").html(balance);
    });
}