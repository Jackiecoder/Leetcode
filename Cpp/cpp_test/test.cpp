#include <iostream>

int main()
{
    int i = 10, i2 = 20;
    int &ri = i;
    std::cout << i << " " << i2 << " " << ri << std::endl;
    ri = i2;
    std::cout << i << " " << i2 << " " << ri << std::endl;

    i = 10;
    int *pi = &i;
    std::cout << i << " " << i2 << " " << *pi << std::endl;
    pi = &i2;
    std::cout << i << " " << i2 << " " << *pi << std::endl;

    int *pnull = nullptr;
    int *pnull2 = 0;
    int *pvalid = &i;
    int *pvalid2 = &i2;

    if (pnull == pnull2)
    {
        std::cout << "hahaha" << std::endl;
    }
    if (pvalid == pvalid2)
    {
        std::cout << i << " " << i2 << " hahahaha" << std::endl;
    }
}