/* Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
*/

for(int i = 0; i < 150; i++)
{
    print(i);
}
for(int i = 5; i < 1000; i+=5)
{
    print(i);
}
for(int i = 1; i < 100; i++)
{
    if(i% 5 = 0)
    {
        print("Coding");
    }
    if(i % 10 = 0)
    {
        print("Coding Dojo");
    }
}
sum = 0;
for(int i = 0; i < 500,000)
{
    if(i % 2 == 1)
    {
        sum += i;
    }
}
print(sum);

for(int i = 2018; i > 0; i--)
{
    if(i > 0){
        print(i);
    }
    i-=3;
}

lowNum = 0;
highNum = i;
mult = 0;