/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let mySet = new Set();
    for(let value of nums){
        if(mySet.has(value))
            return true;
        else
            mySet.add(value);
        
    }
    return false;
    
};