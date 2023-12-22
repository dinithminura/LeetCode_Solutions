/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
  let stack = []
  for (i = 0; i < s.length; i++) {
    let currentChar = s.substring(i, i + 1);
    if(currentChar ==='(' || currentChar === '[' || currentChar ==='{'){
      stack.push(currentChar)
    }else{
      let prvChar = stack.pop() || '';
      if(!((prvChar == '(' && currentChar == ')') || (prvChar == '[' && currentChar == ']') || (prvChar == '{' && currentChar == '}'))){
        return false;
      }      
    }
  }

  return stack.length === 0;

};
    
// Runtime 67 ms Beats 12.15% Memory 42 MB Beats 78.94%
