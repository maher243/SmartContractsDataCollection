# Smart_Contracts_Data_Collection
A Python script to collect the details of Ethereum smart contract transactions such as Gas Limit, Gas Price as well as the bytecode (input data) required to deploy and execute smart contracts.

Ethereum has two types of transactions, which are financial and contract transactions. Financial transactions are to move Ether between accounts, while contract transactions are to either deploy a new contract to the blockchain (contract-creation) or execute an existing one (contrac-execution).

Our script utilises Etherscan API to retrieve transactions' information such as hash, gas limit, used gas, gas price, input,...etc. The script is able to distinugish and identify the type of transactions (financial, contract-creation and contract-execution transactions).

For the purpose of the measurment system, a system to measure the execution time (CPU Time) of Ethereum smart contracts,  we ignored financial transactions. For contract-execution transactions, our script can also retrieve the details for the transaction that created the contract. This is important since in the measurment system we need first to deploy the contract before measuring the CPU Time of a contract-execution transaction. The only way we found to retrieve the contract-creation transaction is by checking the first transaction sent to the contract address. The contract address is drievn from the attribute "to" for the contract-execution transaction.

However, in some cases the script is unable to retrieve the contract-creation transaction (e.g., if the transaction was intiated as part of another contract). In that case, the script return a message "error". It is, however, possible to retrieve it manually.
