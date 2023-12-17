/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let mapping = {}
    for(let i=0; i<nums.length ; i++){
        mapping[nums[i]] = i
    }
    for(let i=0; i< nums.length; i++){
        let remainder = target - nums[i];
        if(mapping.hasOwnProperty(remainder) && mapping[remainder] != i){
            return [i, mapping[remainder]]
        }
    }
};

// Runtime 66 ms Beats 53.97% Memory 44.9 MB Beats 7.15%
