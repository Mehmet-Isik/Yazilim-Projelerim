using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;


namespace Mehmet_IŞIK_191601027
{
    public class Bilgi : ozellik
    {
        public string AD
        {
            get { return ad; }
            set { ad = value.ToUpper(); }
        }
        public int KOD
        {
            get { return kod; }
            set { kod = Math.Abs(value); }
        }
        public int ADET
        {
            get { return adet; }
            set { adet = Math.Abs(value); }
        }
        public string FRMBLG
        {
            get { return firmablg; }
            set { if (value.Length < 101)
                    firmablg = value;
                else
                    firmablg = "Fazla Değer Girildi";
                }
        }
    }
}
