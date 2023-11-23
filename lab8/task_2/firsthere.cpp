﻿#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <windows.h>
#include <clocale>

int glas_count(std::string glas, std::string comp_wrd) //подсчёт гласных в слове
{
	int counter = 0;

	for (int i = 0; i < comp_wrd.length(); i++)
	{
		for (int x = 0; x < glas.length(); x++)
		{
			if (comp_wrd[i] != glas[x])
			{
				counter++;
			}
		}
	}
	return counter;
}

std::string is_bukv(std::string s) //убирает знаки препинание + в нижний регистр
{
	std::string result;
	for (int i = 0; i < s.length(); i++)
		if (((s[i] >= 'а') and (s[i] <= 'я')) or ((s[i] >= 'А') and (s[i] <= 'Я')))
			result += tolower(s[i]);
	return result;
}

std::string dubl_delete(std::string s, std::string soglas) // дублировать согласные , убрать гласные , ь и ъ не трогать(наверное)
{
	std::string result;
	char mg = 'ь';
	char tv = 'ъ';
	for (int i = 0; i < s.length(); i++)
	{
		for (int j = 0; j < soglas.length(); j++)
		{
			if ((s[i] != soglas[j]) and ((s[i] == mg) or (s[i] == tv)))
			{
				result += s[i];
				break;
			}
			else if (s[i] == soglas[j])
			{
				result += s[i];
				result += s[i];
			}
		}
	}
	return result;
}

int main()
{
	setlocale(LC_ALL, "Russian");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	std::ifstream in("input.txt");
	std::ofstream out("output.txt", std::ios::app);
	std::string mas[2001];
	std::string out_mas[2001];
	std::string glas = "уеаоэяию";
	std::string soglas = "йцкнгшщзхфвпрлджчсмтб";
	int text_size = 0;
	int newword = 0;

	while (!in.eof())
	{
		std::string text;
		in >> text;
		mas[text_size] = text;
		text_size++;
	}


	for (int j = 0; j < text_size; j++) //применяем функцию dubl_delete и добавляем результат в новый массив 
	{
		std::string dodik;
		dodik = mas[j];
		if (glas_count(glas, dodik) >= 3)
		{
			out_mas[newword] = dubl_delete(dodik, soglas);
			newword++;
		}

	}



	std::string temp;

	for (int i = 0; i < newword - 1; i++) //обратная сортировка пузырьком по алфавиту
	{
		for (int j = i + 1; j < newword; j++)
		{
			if (out_mas[j] >= out_mas[i])
			{
				temp = out_mas[j];
				out_mas[j] = out_mas[i];
				out_mas[i] = temp;
			}
			
		}
		
	}

	for (int j = 0; j < newword; j++) //вывод
	{
		std::cout << out_mas[j] << std::endl;
		//out << out_mas[j] << std::endl;
	}

}