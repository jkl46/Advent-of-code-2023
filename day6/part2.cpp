#include <iostream>
#include <stdint.h>

int main()
{
    uint32_t fasterTimes = 0;
    uint32_t time = 55999793;
    uint64_t distance = 401148522741405;

    for (size_t i = 0; i < time; i++)
    {
        if ((i * (time - i)) > distance)
        fasterTimes += 1;
    }
    std::cout << fasterTimes; 
}