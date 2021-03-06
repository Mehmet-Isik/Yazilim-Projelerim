<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Stok-Depo.aspx.cs" Inherits="Mehmet_IŞIK_191601027.Stok_Depo" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <style type="text/css">
        .auto-style1 {
            font-weight: bold;
            font-size: 26px;
            color: #FFFFFF;
        }
        .auto-style2 {
            width: 30%;
            height: 29px;
        }
        .auto-style3 {
            height: 29px;
        }
        .auto-style4 {
            margin-left: 0px;
        }
        .auto-style5 {
            width: 100%;
        }
        .auto-style6 {
            width: 30%;
        }
        </style>
</head>
<body>
    <form id="form1" runat="server">
       <div id="div1" runat="server" style="background-color:#006666; border:2px inset #000; padding:10px; text-align:center; font-size:26px; color:#fff; font-weight:bold" class="auto-style1">
            STOK-DEPO OTOMASYONU</div>
        <asp:ListBox ID="ListBox1" runat="server" BackColor="#33CCCC" Height="121px" style= "width:100%"></asp:ListBox>
             </table>
         <div id="div2" runat="server" style="background-color:#006666; border:2px inset #000; padding:10px; text-align:center; font-size:26px; color:#fff; font-weight:bold">
             ÜRÜN KAYIT</div>
         <table style="width:100%">
             <div id="Ürün Ekleme">
         </br></br>
         <table class="auto-style5">
             <tr>
                 <td class="auto-style2">Kullanıcı Adı:</td>
                 <td class="auto-style3"><asp:TextBox ID="txt_ad" runat="server" Width="100%" BackColor="#33CCCC" CssClass="auto-style4"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">Ürün Kodu:</td>
                 <td><asp:TextBox ID="txt_kod" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">Ürün Tipi:</td>
                 <td><asp:TextBox ID="txt_tip" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">Ürün Markası:</td>
                 <td><asp:TextBox ID="txt_marka" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">Ürün Modeli:</td>
                 <td><asp:TextBox ID="txt_model" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">Ürün Adeti:</td>
                 <td><asp:TextBox ID="txt_adet" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td class="auto-style6">Giriş Tarihi:</td>
                 <td><asp:TextBox ID="txt_tarih" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox></td>

             </tr>
             <tr>
                 <td style="width:30%">
                     <asp:Button ID="btn_ekle" runat="server" Text="ÜRÜN EKLE" BackColor="#33CCCC" Width="441px" OnClick="btn_ekle_Click" Height="29px" />
                 </td>
             </tr>
              <tr>
                 <td style="width:30%">
                     <asp:Button ID="btn_listele" runat="server" Text="LİSTELE" BackColor="#33CCCC" Width="441px" OnClick="btn_listele_Click" Height="29px" />
                 </td>
                  <td>
                      <asp:Label ID="Label2" runat="server" Text="Son Eklenen Ürün:  "></asp:Label>
                  </td>
             </tr>
              <tr>
                 <td style="width:30%">
                     <asp:Button ID="btn_satirtemizle" runat="server" Text="SATIRLARI TEMİZLE" BackColor="#33CCCC" Width="441px" OnClick="btn_satirtemizle_Click" />
                 </td>
                  <td>
                      <asp:Label ID="Label1" runat="server" Text=" ------ "></asp:Label>
                  </td>
             </tr>
             <tr>
                 <td style="width:30%">
                     <asp:Button ID="btn_listetemizle" runat="server" Text="LİSTEYİ TEMİZLE" BackColor="#33CCCC" Width="441px" OnClick="btn_listetemizle_Click" />
                 </td>
             </tr>
              <tr>
                 <td style="width:30%">
                     <asp:Button ID="btn_sil" runat="server" Text="SEÇİLEN ÜRÜNÜ SİL" BackColor="#33CCCC" Width="441px" OnClick="btn_sil_Click" />
                 </td>
                  <td>
                      <asp:Label ID="Label3" runat="server" Text="NOT: "></asp:Label><asp:TextBox ID="txt_not" runat="server" Width="100%" BackColor="#33CCCC"></asp:TextBox>
                  </td>
             </tr>
             <tr>
                  <td style="width:30%">
                     <asp:Button ID="btn_blg" runat="server" Text="FİRMA BİLGİSİ" BackColor="#33CCCC" Width="441px" OnClick="btn_blg_Click" />
                 </td>
             </tr>
    </form>
</body>
</html>
