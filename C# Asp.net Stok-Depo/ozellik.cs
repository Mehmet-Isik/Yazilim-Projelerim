using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mehmet_IŞIK_191601027
{
    public abstract class ozellik: IFirmaBilgi
    {
        public string ad { get; set; }
        public int kod { get; set; }
        public string tip { get; set; }
        public string marka { get; set; }
        public string model { get; set; }
        public int adet { get; set; }
        public string tarih { get; set; }
        public string firmablg { get; set; }

        public ozellik()
        {

        }

       
    }
}