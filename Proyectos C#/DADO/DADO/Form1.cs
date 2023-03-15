using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DADO
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random r = new Random();

            double caras = r.Next(0,1);

            label1.Text = caras.ToString();
        }
    }
}



 /*int dado;
            char respuesta;
            Random rdn = new Random();

            do
            {
                dado = rdn.Next(1, 7);

                Console.WriteLine("el dado cayo en la cara:  " + dado);

                Console.WriteLine("¿Quieres volver a tirar el dado? S/N");
                respuesta = char.Parse(Console.ReadLine());

            } while (respuesta == 'S'  );
             while (lanzamientos=126);
            Console.ReadKey();

            [1,2,3,4,5,6,7]*/
