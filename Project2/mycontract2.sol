// Please paste your contract's solidity code here
// Note that writing a contract here WILL NOT deploy it and allow you to access it from your client
// You should write and develop your contract in Remix and then, before submitting, copy and paste it here

pragma solidity >=0.4.0;

contract Splitwise 
{ 
    
    struct UsersSet 
    {
        address[] userAddress;
        mapping (address => bool) isIn;
    }
    function add(address user) public 
    {
        if (!users.isIn[user]) 
        {
            users.userAddress.push(user);
            users.isIn[user] = true;
        }
    }
    
    struct IOU 
    {
        address creditors;
        uint32 amount;
    }

    UsersSet users;

    mapping( address => mapping(address => IOU) ) debtorCreditors;
    mapping( address => uint256 ) dateLastIOU;

    function getUsers() public view returns (address[] memory)
    {
        return users.userAddress;
    }

    function lookup(address debtor, address creditor) public view returns (uint32)
    {
        return debtorCreditors[debtor][creditor].amount;
    }

    function getCreditorsOf(address debtor) public view returns (address[] memory)
    {
        // TODO
    }

    function getTotalOwed(address debtor) public view returns (uint32 totalOwed)
    {
        totalOwed = 0;
        for(uint i=0; i<users.userAddress.length; i++)
        {
            totalOwed += debtorCreditors[debtor][users.userAddress[i]].amount;
        }
    }

    function getLastActive(address debtor) public view returns (uint256 dateLastActive)
    {
        return dateLastIOU[debtor];
    }

    function add_IOU(address creditor, uint32 amount, uint256 date) public 
    {
        debtorCreditors[msg.sender][creditor].amount += amount;
        dateLastIOU[creditor] = date;
        dateLastIOU[msg.sender] = date;
    }

    function delete_cycle(address[] memory cyclePath) public 
    {
        //Check the cycle exist
        uint32 cycleMinAmount = 1000000000;
        for (uint i = 0; i < cyclePath.length-1; i++) 
        {
            address creditor = cyclePath[i];
            address debtor = cyclePath[i+1];
            if (debtorCreditors[debtor][creditor].amount > 0 && debtorCreditors[debtor][creditor].amount < cycleMinAmount)
            {
                cycleMinAmount = debtorCreditors[debtor][creditor].amount;
            }
        }

        //Remove the minimum amount for each pair in the cycle
        if(cycleMinAmount > 0)
        {
            for (uint i = 0; i < cyclePath.length-1; i++) 
            {
                address creditor = cyclePath[i];
                address debtor = cyclePath[i+1];
                debtorCreditors[debtor][creditor].amount -= cycleMinAmount;
            }
        }
    }
}



