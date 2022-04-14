/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};


function frequencyTableBuilder(arr) {
    var counter = {}
    var key = 0
        for(var i = 0; i < arr.length; i++){
            for(var j = i + 1; j < arr.length ; j++) {
                if (arr[i] === arr[j]){
                    counter[arr[key]] = key;
                    key += 1
                    console.log(arr[key])
                
                }
                else {
                    counter[arr[key]] = 1;
                    console.log([arr[key]])
                }
                
            }
        
        }
    return counter
    }

  // create an empty object to hold the count key will be the array element value will be the elements count
  // loop through the array 
    // check if the key is in the object
    // if not add to the object
    // if it is add to the count
  //return the object

  console.log(arr1[1])
