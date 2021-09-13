// Please paste your contract's solidity code here
// Note that writing a contract here WILL NOT deploy it and allow you to access it from your client
// You should write and develop your contract in Remix and then, before submitting, copy and paste it here

pragma solidity >=0.4.0;

contract Splitwise 
{ 
    struct IOU 
    {
        address debtor;
        address creditor;
        uint32 amount;
        uint256 date;
    }

    IOU[] public listIOUs;

    function getIOUsCount() public view returns (uint)
    {
        return listIOUs.length;
    }

    function getIOU(uint idx) public view returns (IOU memory)
    {
        return listIOUs[idx];
    }

    function getIOUsArray() public view returns (IOU[] memory)
    {
        return listIOUs;
    }

    function lookup(address debtor, address creditor) public view returns (uint32 ret)
    {
        for (uint i = 0; i < listIOUs.length; i++) 
        {
            if(listIOUs[i].debtor == debtor && listIOUs[i].creditor == creditor)
            {
                ret += listIOUs[i].amount;
            }
        }
    }

    function add_IOU(address creditor, uint32 amount) public 
    {
        IOU memory newIOU;
        newIOU.debtor = msg.sender;
        newIOU.creditor = creditor;
        newIOU.amount = amount;
        listIOUs.push(newIOU); 
    }

    function add_IOU_with_date(address creditor, uint32 amount, uint256 date) public 
    {
        IOU memory newIOU;
        newIOU.debtor = msg.sender;
        newIOU.creditor = creditor;
        newIOU.amount = amount;
        newIOU.date = date;
        listIOUs.push(newIOU); 
    }

    function delete_cycle(address[] memory users) public
    {
        //Check the cycle exist
        uint32 cycleMinAmount = 1000000000;
        for (uint i = 0; i < users.length - 1; i++)
        {
            address debtor = users[i];
            address creditor = users[i+1];
            for (uint j = 0; j < listIOUs.length; j++) 
            {
                if(listIOUs[j].creditor == creditor && listIOUs[j].debtor == debtor && listIOUs[j].amount < cycleMinAmount)
                {
                    cycleMinAmount = listIOUs[j].amount;
                }
            }
        }

        //Remove the minimum amount for each pair in the cycle
        if(cycleMinAmount != 0 && cycleMinAmount != 1000000000)
        {
            for (uint i = 0; i < users.length - 1; i++)
            {
                address debtor = users[i];
                address creditor = users[i+1];
                uint32 remainingAmountToDelete = cycleMinAmount;
                for (uint j = 0; j < listIOUs.length; j++) 
                {
                    if(listIOUs[j].creditor == creditor && listIOUs[j].debtor == debtor && remainingAmountToDelete > 0)
                    {
                        if(listIOUs[j].amount > remainingAmountToDelete)
                        {
                            listIOUs[j].amount -= remainingAmountToDelete;
                            remainingAmountToDelete = 0;
                        }
                        else
                        {
                            listIOUs[j].amount = 0;
                            remainingAmountToDelete -= listIOUs[j].amount;
                        }
                    }
                }
            }

        }

    }
}



