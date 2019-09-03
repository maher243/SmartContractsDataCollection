# Smart_Contracts_Collection
A Python script to collect the details of smart contracts' transactions including the bytecode (input) required to deploy/execute contracts.

Our script utilises Etherscan API to retrieve transactions' information such as hash, gas limit, used gas, gas price, input,...etc. The script is able to distinugish between the three types of transactions, which are financial, contract-creation, contract-execution transactions.

For the purpose of the conBench system, a system to benchmark Ethereum smart contracts,  we ignored financial transactions. For contract-execution transactions, our script can also retrieve the details for the transaction that created the contract. This is important since in ConBench system weneed first to deploy the contract before benchmarking a contract-execution transaction. However, in some cases the script is unable to retrieve the contract-creation transaction (e.g., if the transaction was intiated aspart of another contract). In that case, the script return a message "error". It is, however, possible to retrieve it manually.
