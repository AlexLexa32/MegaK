using System;

namespace MegaK {
    class MegaK_lite {
        static void Main() {
            int a, b;
            char q;
            a = Convert.ToInt32(Console.ReadLine());
            q = Convert.ToChar(Console.ReadLine());
            b = Convert.ToInt32(Console.ReadLine());
            switch (q) {
                case '+':
                    Console.Write (a+b);
                    break;
                
                case '-':
                    Console.Write (a-b);
                    break;
                
                case '*':
                    Console.Write (a*b);
                    break;
                
                case '/':
                    Console.Write (a/b);
                    break;
            }
        }
    }
}