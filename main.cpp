/*
Author: Daniel Jones
Language: C++
IDE: Code::Blocks
Operating System: Pop! OS Linux
Purpose: generates RSA public and private keys for chat encryption.
*/

#include <iostream>
//int gen_rand_prime();

using namespace std;




//generates a random prime number.
long gen_rand_prime(){

    cout << "I'm working!\n";

    return 0;
}




int main()
{
    cout << "Generating random keys. \nBe patient, this might take a few minutes." << endl;


    long p;

    p = gen_rand_prime();

    cout << p << endl;
    return 0;

}
