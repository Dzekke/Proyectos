using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace calcuWindowsFormsApp
{
    public partial class Form1 : Form
    {
        double num1, num2, resultado;
        string operacion;
        public Form1()
        {
            InitializeComponent();
        }

        private void btnsum_Click(object sender, EventArgs e)
        {
            operacion = "+";
            num1 = double.Parse(txtprincipal.Text);
            txtprincipal.Clear();
        }

        private void btnres_Click(object sender, EventArgs e)
        {
            operacion = "-";
            num1 = double.Parse(txtprincipal.Text);
            txtprincipal.Clear();
        }

        private void btnmul_Click(object sender, EventArgs e)
        {
            operacion = "*";
            num1 = double.Parse(txtprincipal.Text);
            txtprincipal.Clear();
        }

        private void btndiv_Click(object sender, EventArgs e)
        {
            operacion = "/";
            num1 = double.Parse(txtprincipal.Text);
            txtprincipal.Clear();
        }

        private void btnresultado_Click(object sender, EventArgs e)
        {
            num2 = double.Parse(txtprincipal.Text);

            switch (operacion)
            {
                case "+":
                    resultado = num1 + num2;
                    txtprincipal.Text = resultado.ToString();
                    break;
                case "-":
                    resultado = num1 - num2;
                    txtprincipal.Text = resultado.ToString();
                    break;
                case "*":
                    resultado = num1 * num2;
                    txtprincipal.Text = resultado.ToString();
                    break;
                case "/":
                    resultado = num1 / num2;
                    txtprincipal.Text = resultado.ToString();
                    break;
            }
        }

        private void btnclear_Click(object sender, EventArgs e)
        {
            txtprincipal.Clear();
        }

        

        
    }
}
