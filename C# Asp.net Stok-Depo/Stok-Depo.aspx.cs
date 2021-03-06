using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Mehmet_IŞIK_191601027
{
    public partial class Stok_Depo : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
             
        }

        public static List<Bilgi> blgList = new List<Bilgi>();
        Bilgi blg = new Bilgi();

        protected void btn_ekle_Click(object sender, EventArgs e)
        {
            blg.AD = txt_ad.Text;
            blg.KOD = int.Parse(txt_kod.Text);
            blg.tip = txt_tip.Text;
            blg.marka = txt_marka.Text;
            blg.model = txt_model.Text;
            blg.ADET =int.Parse(txt_adet.Text);
            blg.tarih = txt_tarih.Text;
            blg.FRMBLG = txt_not.Text;

            blgList.Add(blg);
            Label1.Text = ("Kullanıcı Adı: " + blg.AD + " -- Ürün Kodu:  " + blg.KOD + " -- Ürün Tipi: " + blg.tip + " -- Ürün Markası: " + blg.marka + " -- Ürün Modeli: " + blg.model + " -- Ürün Adeti: " + blg.ADET + " -- Giriş Tarihi: " + blg.tarih + " -- NOT: " + blg.FRMBLG); 
        }

        protected void btn_satirtemizle_Click(object sender, EventArgs e)
        {
            txt_ad.Text = "";
            txt_kod.Text = "";
            txt_tip.Text = "";
            txt_marka.Text = "";
            txt_model.Text = "";
            txt_adet.Text = "";
            txt_tarih.Text="";
            txt_not.Text = "";
            Label1.Text = "";
            txt_ad.Focus();
        }

        protected void btn_sil_Click(object sender, EventArgs e)
        {
            ListBox1.Items.RemoveAt(ListBox1.SelectedIndex);
        }

        protected void btn_listele_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < blgList.Count; i++)
            {
                ListBox1.Items.Add("Kullanıcı Adı: " + blgList[i].AD + " -- Ürün Kodu:  " + blgList[i].KOD + " -- Ürün Tipi: " + blgList[i].tip + " -- Ürün Markası: " + blgList[i].marka + " -- Ürün Modeli: " + blgList[i].model + " -- Ürün Adeti: " + blgList[i].ADET + " -- Giriş Tarihi: " + blgList[i].tarih + " //--// NOT: " + blgList[i].FRMBLG);
            }
        }

        protected void btn_listetemizle_Click(object sender, EventArgs e)
        {
            ListBox1.Items.Clear();
        }

        protected void btn_blg_Click(object sender, EventArgs e)
        {
            // MesajBox kullanamadığım için internetten araştırıp böyle bir kalıp kullandım.
            ScriptManager.RegisterClientScriptBlock(this, this.GetType(), "alertMessage", "alert('M.I COMPANY // Since 2020 // E-Mail: M.I@gmail.com // Tel.Number: *****')", true);
        }
    }
}
