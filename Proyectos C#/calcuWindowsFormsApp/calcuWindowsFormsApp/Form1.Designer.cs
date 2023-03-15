namespace calcuWindowsFormsApp
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtprincipal = new System.Windows.Forms.TextBox();
            this.btnsum = new System.Windows.Forms.Button();
            this.btnres = new System.Windows.Forms.Button();
            this.btnmul = new System.Windows.Forms.Button();
            this.btndiv = new System.Windows.Forms.Button();
            this.btnresultado = new System.Windows.Forms.Button();
            this.btnclear = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // txtprincipal
            // 
            this.txtprincipal.Location = new System.Drawing.Point(13, 13);
            this.txtprincipal.Name = "txtprincipal";
            this.txtprincipal.Size = new System.Drawing.Size(92, 20);
            this.txtprincipal.TabIndex = 0;
            this.txtprincipal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnsum
            // 
            this.btnsum.Location = new System.Drawing.Point(12, 50);
            this.btnsum.Name = "btnsum";
            this.btnsum.Size = new System.Drawing.Size(43, 28);
            this.btnsum.TabIndex = 1;
            this.btnsum.Text = "+";
            this.btnsum.UseVisualStyleBackColor = true;
            this.btnsum.Click += new System.EventHandler(this.btnsum_Click);
            // 
            // btnres
            // 
            this.btnres.Location = new System.Drawing.Point(61, 50);
            this.btnres.Name = "btnres";
            this.btnres.Size = new System.Drawing.Size(43, 28);
            this.btnres.TabIndex = 2;
            this.btnres.Text = "-";
            this.btnres.UseVisualStyleBackColor = true;
            this.btnres.Click += new System.EventHandler(this.btnres_Click);
            // 
            // btnmul
            // 
            this.btnmul.Location = new System.Drawing.Point(13, 84);
            this.btnmul.Name = "btnmul";
            this.btnmul.Size = new System.Drawing.Size(43, 28);
            this.btnmul.TabIndex = 3;
            this.btnmul.Text = "*";
            this.btnmul.UseVisualStyleBackColor = true;
            this.btnmul.Click += new System.EventHandler(this.btnmul_Click);
            // 
            // btndiv
            // 
            this.btndiv.Location = new System.Drawing.Point(62, 84);
            this.btndiv.Name = "btndiv";
            this.btndiv.Size = new System.Drawing.Size(43, 28);
            this.btndiv.TabIndex = 4;
            this.btndiv.Text = "/";
            this.btndiv.UseVisualStyleBackColor = true;
            this.btndiv.Click += new System.EventHandler(this.btndiv_Click);
            // 
            // btnresultado
            // 
            this.btnresultado.Location = new System.Drawing.Point(13, 118);
            this.btnresultado.Name = "btnresultado";
            this.btnresultado.Size = new System.Drawing.Size(42, 28);
            this.btnresultado.TabIndex = 5;
            this.btnresultado.Text = "=";
            this.btnresultado.UseVisualStyleBackColor = true;
            this.btnresultado.Click += new System.EventHandler(this.btnresultado_Click);
            // 
            // btnclear
            // 
            this.btnclear.Location = new System.Drawing.Point(63, 118);
            this.btnclear.Name = "btnclear";
            this.btnclear.Size = new System.Drawing.Size(42, 28);
            this.btnclear.TabIndex = 6;
            this.btnclear.Text = "CE";
            this.btnclear.UseVisualStyleBackColor = true;
            this.btnclear.Click += new System.EventHandler(this.btnclear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(120, 162);
            this.Controls.Add(this.btnclear);
            this.Controls.Add(this.btnresultado);
            this.Controls.Add(this.btndiv);
            this.Controls.Add(this.btnmul);
            this.Controls.Add(this.btnres);
            this.Controls.Add(this.btnsum);
            this.Controls.Add(this.txtprincipal);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtprincipal;
        private System.Windows.Forms.Button btnsum;
        private System.Windows.Forms.Button btnres;
        private System.Windows.Forms.Button btnmul;
        private System.Windows.Forms.Button btndiv;
        private System.Windows.Forms.Button btnresultado;
        private System.Windows.Forms.Button btnclear;
    }
}

