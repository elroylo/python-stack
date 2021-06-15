// 7/6/2020

/*
  String: Reverse

  Implement reverseString(str)
  abc
  cba
*/

function reverseString(str) {
  var revString = "";
  for (x = str.length - 1; x >= 0; x--) {
    revstring += str[x];
  }
  return revString;
}

console.log(reverseString("Hello World!"));
console.log(reverseString("Coding Dojo"));
console.log(reverseString("Morning Algorithms"));

/*
  Acronyms

  Create a function that, given a string, returns the string’s acronym
  (first letter of each word capitalized).

  Do it with .split first if you need to, then try to do it without
*/

function acronymCreator (str)
{
var acronym = "";

for (var i = 0; i < str.length; i++)
{
  if (i == 0)
  {
    acronym += str[i];
  }
  else if (str[i] == " ")
  {
    acronym += str[i + 1];
  }
}
return acronym.toUpperCase();
}
console.log(acronymCreator("Hello everyone, how are you?")); //should log "HEHAY"
console.log(acronymCreator("Today is going to be great!")); //should log "TIGTBG"

function acronym(str) {
  var acronym = "";
  
}

/*
  Case insensitive string comparison

  const test1StrA = "ABC"
  const test1StrB = "abc"
  caseInsensitiveCompare(test1StrA, test1StrB) // Output: true

*/
function caseInsensitiveCompare(test1StrA, test1StrB)
{
  if (test1StrA.toUpperCase() == test1StrB.toUpperCase())
  {
    return true;
  }
  else
  {
    return false;
  }
}
console.log(caseInsensitiveCompare("Hello World", "HELLO WORLD")); //true
console.log(caseInsensitiveCompare("Coding Dojo", "Codin Dojo")); //false, misspelled
console.log(caseInsensitiveCompare("JavaScript", "javascript")); //true



// 7/7/2020

/*
  Parens Valid

	Given an str that has parenthesis in it
	return whether the parenthesis are valid
*/

function parensValidStack(str) {
  // code here
  // look at each char in str
  // if (, hold in temp var
  // if ), concat in temp var
  // if (), var result = true
  

  // for loop to iterate thru chars, stop once ( is found
  // reverse for loop to find matching )

  // for (i = 0; i < str.length; i++) {
  //   if (str[i] = "(") {
  //     break
  //   }
  // }
  // for (i = str.length - 1; i >= 0; i++) {
  //   if (str[i] = ")") {
  //     break
  //   }
  // }

  // for loop to iter thru char find (
  // save str[index] of (
  // for loop to iter thru char find )
  // save str[index] of )
  // compare indexes, if ) < ( false

  // for (i = 0; i < str.length; i++) {
    // if (str[i] == "(") {
      // var openParen = i
    // }
  // }

  var i = 0
  var arr = []
  while (i < str.length) {
    if (str[i] === "(") {
      var openParen = i
    }
    if (str[i] === ")") {
      var closedParen = i
      if (openParen < closedParen) {
        arr.push(true);
      }
      else {arr.push(false)}
    }
    i++
  }


}

var test1 = "Y(3(p)p(3)r)s"
parensValidStack(test1)
// Output: true

var test2 = "N(0(p)3"
parensValidStack(test1)
// Output: false - not every parenthesis is closed.

var test3 = "N(0)t ) 0(k"
parensValidStack(test1)
// Output: false - because the underlined ")" is premature: there is nothing open for it to close.

var test4 = "a(b))(c"
parensValidStack(test1)
/*
  Output: false
    - same number of opens and closes but the 2nd closing closes nothing
*/

// ************************************************

/*
  Braces Valid

  Given a string sequence of parentheses, braces and brackets, determine whether it is valid.
*/

function bracesValid(str) {
  // code here
}

var test1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"
bracesValid(test1)
// Output: true

var test2 = "D(i{a}l[ t]o)n{e"
bracesValid(test2)
// Output: false

var test3 = "A(1)s[O (n]0{t) 0}k"
bracesValid(test3)
// Output: false






// 7/8/2020


/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

function isPalindrome(str) {
  var newStr = ""
  for (i = str.length-1; i < str.length; i++) {

  }
}


const test1 = "a x a";
// Output: true

const test2 = "racecar";
// Output: true

const test3 = "Dud";
// Output: false

const test4 = "oho!";
// Output: false

const sadiesFavoriteTestCase = "tacocat";
// Output: true


// Ninja Sensei Bonus / Further Study!

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

const test01 = "what up, daddy-o?";
// Output: "dad"

const test02 = "uh, not much";
// Output: "u"

const test03 = "Yikes! my favorite racecar erupted!";
// Output: "e racecar e"