#include <iostream>
#include <math.h>

class Cube {
    int _edge;  //ребро куба

public:
    Cube() = default;

    bool setEdge(float a) //Задать ребро
    {
        if (a <= 0)
        {
            std::cout << "shieeeeet ur value is garbage. try again (positive pls)" << std::endl;
            return false;
        }
        _edge = a;
    }

    float getAr() //Площадь
    {
        return _edge * _edge * 6;
    }
    float getVol() //Объём
    {
        return _edge * _edge * _edge;
    }
    float getDg() //Диагональ
    {
        return _edge * sqrt(3);
    }

    ~Cube() = default;
};

int main()
{
    Cube cubik;
    float a;
    std::cout << "yo enter edge value: ";
    std::cin >> a;
    cubik.setEdge(a);
    std::cout << cubik.getAr() << " is Cube`s surface area" << std::endl << cubik.getVol() << " is Cube`s volume" << std::endl << cubik.getDg() << " is leghts of Cube`s diagonal" << std::endl;
}


