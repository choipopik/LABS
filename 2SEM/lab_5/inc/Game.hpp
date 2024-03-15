#pragma once
#include <string>

namespace mt
{
	const float pi = acos(-1);

	class Game1
	{
		int m_width;
		int m_height;
		std::string m_capture;
		mt::Circle *m_kpyr;
		int m_n;
		sf::RenderWindow m_window;
		sf::Clock clock;

	public:
		Game1(int width, int height, const std::string& capture)
		{

			m_width = width;
			m_height = height;
			m_capture = capture;
		}

		void Setup(int n)
		{
			m_n = n;

			m_window.create(sf::VideoMode(m_width, m_height), m_capture);
			m_window.setTitle(m_capture);

			srand(time(0));

			m_kpyr = new mt::Circle[m_n];
			for (int i = 0; i < m_n; i++)
			{
				int r = rand() % 30 + 10;
				int x = rand() % 1000 + r;
				if (x - r < 0)
					x = r;
				if (x + r > m_width)
					x = m_width - r;
				int y = rand() % 720 + r;
				if (y - r < 0)
					y = r;
				if (y + r > m_height)
					y = m_height - r;

				int red = rand() % 225;
				int v = rand() % 100 - 200;
				int vAng = rand() % 7;
				m_kpyr[i].Setup(x, y, r, red, v, vAng);
			}
		}

		void brdrColl(Circle& obj)
		{
			float x = obj.X();
			float y = obj.Y();
			float r = obj.R();

			if ((x + r) >= m_width || (x - r) <= 0)
			{
				obj.vang(pi - obj.Alfa());
			}
			if ((y + r) >= m_height || (y - r) <= 0)
			{
				obj.vang(2*pi - obj.Alfa());
				
			}
			
		}

		//просчитываение столкновения с другим шаром

		void ownColl(Circle& obj1, Circle& obj2)
		{
			float x1 = obj1.X();
			float y1 = obj1.Y();
			float r1 = obj1.R();
			float va1 = obj1.Alfa();

			float x2 = obj2.X();
			float y2 = obj2.Y();
			float r2 = obj2.R();
			float va2 = obj2.Alfa();


			float Dx = x1 - x2;
			float Dy = y1 - y2;
			float d = sqrt(Dx * Dx + Dy * Dy); if (d == 0) d = 0.01;
			if (d < r1 + r2)
			{
				float tmp = va1;
				obj1.vang(va2);
				obj2.vang(tmp);
			}
			/*if (obj1.objBounds().contains(x2 + r2, y2 + r2))
			{
				
			}*/

						
		}

		void LifeCycle()
		{
			while (m_window.isOpen())
			{
				sf::Event event;
				while (m_window.pollEvent(event))
				{
					if (event.type == sf::Event::Closed)
						m_window.close();
				}

				//logic
				float dt = clock.getElapsedTime().asSeconds();
				clock.restart();

				for (int i = 0; i < m_n; i++)
					m_kpyr[i].Move(dt);

				//collision

				for (int i = 0; i < m_n; i++)
					brdrColl(m_kpyr[i]);

				for (int i = 0; i < m_n; i++)
					for (int j = i+1; j < m_n; j++)
						ownColl(m_kpyr[i],m_kpyr[j]);

				
				//display

				m_window.clear();
				for (int i = 0; i < m_n; i++)
					m_window.draw(m_kpyr[i].Get());
				m_window.display();
			}
		}

	};


	class Game2
	{
		int m_width;
		int m_height;
		std::string m_capture;
		mt::Rectangle* m_rect;
		int m_n;
		sf::RenderWindow m_window;
	public:
		Game2(int width, int height, const std::string& capture)
		{

			m_width = width;
			m_height = height;
			m_capture = capture;
		}

		void Setup(int n)
		{
			m_n = n;

			m_window.create(sf::VideoMode(m_width, m_height), m_capture);
			m_window.setTitle(m_capture);

			srand(time(0));

			m_rect = new mt::Rectangle[m_n];
			for (int i = 0; i < m_n; i++)
			{
				int x = rand() % 1000;
				int y = rand() % 720;
				int recth = rand() % 300 + 1;
				int rectw = rand() % 300 + 1;
				int angle = rand() % 360;
				int red = rand() % 225;
				m_rect[i].Setup(x, y, red, recth, rectw, angle);
			}
		}

		void LifeCycle()
		{
			while (m_window.isOpen())
			{
				sf::Event event;
				while (m_window.pollEvent(event))
				{
					if (event.type == sf::Event::Closed)
						m_window.close();
				}

				m_window.clear();
				for (int i = 0; i < m_n; i++)
					m_window.draw(m_rect[i].Get());
				m_window.display();
			}
		}
	};

	
	class Game3
	{
		int m_width;
		int m_height;
		std::string m_capture;
		mt::Triangle* m_trig;
		int m_n;
		sf::RenderWindow m_window;

	public:
		Game3(int width, int height, const std::string& capture)
		{

			m_width = width;
			m_height = height;
			m_capture = capture;
		}

		void Setup(int n)
		{
			m_n = n;

			m_window.create(sf::VideoMode(m_width, m_height), m_capture);
			m_window.setTitle(m_capture);

			srand(time(0));

			m_trig = new mt::Triangle[m_n];
			for (int i = 0; i < m_n; i++)
			{
				int x = rand() % 1000;
				int y = rand() % 720;
				int r = rand() % 300 + 1;
				int red = rand() % 225;
				int angle = rand() % 360;
				m_trig[i].Setup(x, y, r, red, angle);
			}
		}

		void LifeCycle()
		{
			while (m_window.isOpen())
			{
				sf::Event event;
				while (m_window.pollEvent(event))
				{
					if (event.type == sf::Event::Closed)
						m_window.close();
				}

				m_window.clear();
				for (int i = 0; i < m_n; i++)
					m_window.draw(m_trig[i].Get());
				m_window.display();
			}
		}
	};

	class Game4
	{
		int m_width;
		int m_height;
		std::string m_capture;
		mt::Line* m_line;
		int m_n;
		sf::RenderWindow m_window;
	public:
		Game4(int width, int height, const std::string& capture)
		{

			m_width = width;
			m_height = height;
			m_capture = capture;
		}

		void Setup(int n)
		{
			m_n = n;

			m_window.create(sf::VideoMode(m_width, m_height), m_capture);
			m_window.setTitle(m_capture);

			srand(time(0));

			m_line = new mt::Line[m_n];
			for (int i = 0; i < m_n; i++)
			{
				int x = rand() % 1000;
				int y = rand() % 720;
				int linelen = rand() % 300 + 1;
				int angle = rand() % 360;
				int red = rand() % 225;
				m_line[i].Setup(x,y,red,linelen,angle);
			}
		}

		void LifeCycle()
		{
			while (m_window.isOpen())
			{
				sf::Event event;
				while (m_window.pollEvent(event))
				{
					if (event.type == sf::Event::Closed)
						m_window.close();
				}

				m_window.clear();
				for (int i = 0; i < m_n; i++)
					m_window.draw(m_line[i].Get());
				m_window.display();
			}
		}
	};
}