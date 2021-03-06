#include<stdio.h>
#include<stdlib.h>



void kategoriBilgisayar();
void kategoriTelefon();
void kategoriTablet();
void kategoriKamera();
void kategoriKulaklik();
void kategoriDrone();
void kategoriAkilliSaat();
void kategoriFotografMakinesi();
void kategoriPowerbank();
void kategoriSanalGerceklikGozlugu();
void kategoriHoparlor();
void kategoriBaglantiKablolari();
void dekont();
void tesekkur();
void birsatiratla();
void ikisatiratla();



int main()

{
	int kategori,tip,model;

	printf("***M.I TEKNOWORLD***\n\n");
	printf("-->(M.I TeknoWorld'e Hosgeldiniz.)\n\n");
	
	do 
	{	
	
	printf(">>>KATEGORILER<<<\n\n");
		
	char urun[13][60] = {"Bilgisayar","Telefon","Tablet","Kamera","Kulaklik","Drone","Akilli Saat","Fotograf Makinesi","Powerbank","Sanal Gerceklik Gozlugu","Hoparlor","Baglanti Kablolari\n","--->>>CIKMAK ICIN 1-12 DISINDA BIR SAYI GIRINIZ!!!.<<<---\n"};

	int x = 0, z = 0;
	
	for(x = 0; x < 13; x++)
	{
		printf("[%d]",x+1);
		
		for(z = 0; z < 60; z++)
		{
			printf("%c",urun[x][z]);
		}
		printf("\n");
	}
	
	printf("Kategori Seciniz:");
	scanf("%d",&kategori);
		
	birsatiratla();
		
	switch(kategori)
	{
		case 1:
			kategoriBilgisayar();
			
			break;
			
		case 2:
			kategoriTelefon();
			
			break;
			
		case 3:
			kategoriTablet();
			
			break;
			
		case 4:
			kategoriKamera();
			
			break ;
				
		case 5:
			kategoriKulaklik();
			
			break;
			
		case 6:
			kategoriDrone();
			
			break;		
		
		case 7:
			kategoriAkilliSaat();
			
			break;	
			
		case 8:
			kategoriFotografMakinesi();
			
			break;
		
		case 9:
			kategoriPowerbank();
			
			break;	
			
		case 10:
			kategoriSanalGerceklikGozlugu();
			
			break;
			
		case 11:
			kategoriHoparlor();
			
			break;	
			
		case 12:
			kategoriBaglantiKablolari();
			
			break;
			
		default:
			
			exit(1);
			
			break;
											
	}
	
	}
	while (kategori <= 12);
	
	
	
	getch();
	
	return 0;
	
}



void kategoriBilgisayar()
{
			int kategori,tip,model;
	
			printf("1-Laptop\n");
			printf("2-Masaustu");
			
			ikisatiratla();
			
			printf("Bilgisayar tipini Seciniz:");
			scanf("%d",&tip);
			
			birsatiratla();
			
			switch(tip)
			{
				case 1:
					printf("1-M.I-LS --> (2000 tl)\n\n (2gb ram)\n (2gb ekran karti)\n (500gb hdd)\n (i3-6.nesil)\n\n");
					printf("2-M.I-LM --> (4000 tl)\n\n (4gb ram)\n (4gb ekran karti)\n (1tb hdd + 256gb ssd)\n (i5-7.nesil)\n\n");
					printf("3-M.I-LL --> (8000 tl)\n\n (8gb ram)\n (6gb ekran karti)\n (256gb hdd + 1tb ssd)\n (i7-9.nesil)\n\n");
					
					printf("Bilgisayar modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 2000 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 4000 tl.\n\n");	
					}
					else if(model == 3)
					{
						printf("--->>> ODENECEK TUTAR: 8000 tl.\n\n");
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
			
					}
					
					tesekkur();
					
					break;
					
				case 2:
					printf("1-M.I-MSS --> (1500 tl)\n\n (2gb ram)\n (2gb ekran karti)\n (500gb hdd)\n (i3-6.nesil)\n\n");
					printf("2-M.I-MSM --> (3500 tl)\n\n (4gb ram)\n (4gb ekran karti)\n (1tb hdd + 256gb ssd)\n (i5-7.nesil)\n\n");
					printf("3-M.I-MSL --> (6500 tl)\n\n (8gb ram)\n (6gb ekran karti)\n (256gb hdd + 1tb ssd)\n (i7-9.nesil)\n\n");
					
					printf("Bilgisayar modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 1500 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 3500 tl.\n\n");	
					}
					else if(model == 3)
					{
						printf("--->>> ODENECEK TUTAR: 6500 tl.\n\n");
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
			}
}



void kategoriTelefon()
{
			int kategori,tip,model;
	
			printf("1-M.I-xt20 --> (1000 tl)\n\n (2gb ram)\n (32gb hafiza)\n (xt-200 islemci)\n\n");
			printf("2-M.I-xt40 --> (2500 tl)\n\n (4gb ram)\n (64gb hafiza)\n (xt-400 islemci)\n\n");
			printf("3-M.I-xt80 --> (4000 tl)\n\n (8gb ram)\n (128gb hafiza)\n (xt-800 islemci)\n\n");
			
			printf("Telefon modelini seciniz:");
			scanf("%d",&model);
			
			birsatiratla();
			
			dekont();
			
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 1000 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 2500 tl.\n\n");	
			}
			else if(model == 3)
			{
			printf("--->>> ODENECEK TUTAR: 4000 tl.\n\n");
			}
			else
	    	{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
					
}



void kategoriTablet()
{
			int kategori,tip,model;
			
			printf("1-M.I-mt93x --> (1250 tl)\n\n (2gb ram)\n (64gb hafiza)\n (mtx-930 islemci)\n\n");
			printf("2-M.I-wt46x --> (2750 tl)\n\n (4gb ram)\n (128gb hafiza)\n (wtx-460 islemci)\n\n");
			
			printf("Tablet modelini seciniz:");
			scanf("%d",&model);
			
			birsatiratla();
			
			dekont();
			
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 1250 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 2750 tl.\n\n");	
			}
			else
	    	{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
}



void kategoriKamera()
{
			int kategori,tip,model;
	
			printf("1-Aksiyon Kamerasi\n");
			printf("2-Guvenlik Kamerasi\n");
			printf("3-Arac Kamerasi");
			
			ikisatiratla();
			
			printf("Kamera tipini Seciniz:");
			scanf("%d",&tip);
			
			birsatiratla();
			
			switch(tip)
			{
				case 1:
					printf("1-M.I-ak-1 --> (500 tl)\n\n (12MP)\n (hd cozunurluk)\n (2.0 inch)\n\n");
					printf("2-M.I-ak-2 --> (1000 tl)\n\n (24MP)\n (full hd cozunurluk)\n (2.0 inch)\n\n");
					printf("3-M.I-ak-3 --> (1500 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (2.0 inch)\n\n");
					
					printf("Kamera modelini Seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
					printf("--->>> ODENECEK TUTAR: 500 tl.\n\n");
					}
					else if(model == 2)
					{
					printf("--->>> ODENECEK TUTAR: 1000 tl.\n\n");	
					}
					else if(model == 3)
					{
					printf("--->>> ODENECEK TUTAR: 1500 tl.\n\n");	
					}
					else
			    	{
					printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
					
				case 2:
					printf("1-M.I-gkd --> (1500 tl)\n\n (24MP)\n (full hd cozunurluk)\n\n");
					printf("2-M.I-gki --> (2500 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (gece goruslu)\n\n");
					
					printf("Kamera modelini Seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
					printf("--->>> ODENECEK TUTAR: 1500 tl.\n\n");
					}
					else if(model == 2)
					{
					printf("--->>> ODENECEK TUTAR: 2500 tl.\n\n");	
					}
					else
			    	{
					printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
					
				case 3:
					printf("1-M.I-aik --> (1250 tl)\n\n (24MP)\n (full hd cozunurluk)\n (gps)\n\n");
					printf("2-M.I-adk --> (1750 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (gece goruslu)\n (gps)\n\n");
					
					printf("Kamera modelini Seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
					printf("--->>> ODENECEK TUTAR: 1250 tl.\n\n");
					}
					else if(model == 2)
					{
					printf("--->>> ODENECEK TUTAR: 1750 tl.\n\n");	
					}
					else
			    	{
					printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
							
				}
}



void kategoriKulaklik()
{
			int kategori,tip,model;
	
			printf("1-Kablolu Kulaklik\n");
			printf("2-Kablosuz Kulaklik");
			
			ikisatiratla();
			
			printf("Kulaklik tipini Seciniz:");
			scanf("%d",&tip);
			
			birsatiratla();
			
			switch(tip)
			{
				case 1:
					printf("1-M.I-klk24 --> (75 tl)\n\n (Kulak ici kulaklik)\n (Frekans:20 Hz)\n (Duyarlilik: 93.2 dB)\n (Direnç: 32 Ohm)\n\n");
					printf("2-M.I-klk42 --> (150 tl)\n\n (Kulak ustu kulaklik)\n (Frekans:20 Hz)\n (Duyarlilik: 93.2 dB)\n (Direnç: 32 Ohm)\n\n");
					
					printf("Kulaklik modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 75 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 150 tl.\n\n");	
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
			
					}
					
					tesekkur();
					
					break;
				
				case 2:
					printf("1-M.I-ksk12 --> (100 tl)\n\n (Kulak içi kulaklik)\n (Bluetooth: V5.0)\n (Batarya: 310 mAh)\n (Þarj Olma Suresi: 1.5 Saat)\n (Çalýþma Menzili: 10m)\n\n");
					printf("2-M.I-ksk21 --> (200 tl)\n\n (Kulak ustu kulaklik)\n (Bluetooth: V5.0)\n (Batarya: 310 mAh)\n (Þarj Olma Suresi: 1.5 Saat)\n (Çalýþma Menzili: 10m)\n\n");
										
					printf("Kulaklik modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 100 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 200 tl.\n\n");	
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
			}
}



void kategoriDrone()
{		
			int kategori,tip,model;

			printf("1-M.I-dx2w4 --> (750 tl)\n\n (boyutu: 40x40x7cm)\n (agirlik: 98gr)\n (cekim mesafesi 100m)\n (ucus suresi: 10-15dk)\n (sarj suresi: 50dk)\n\n");
			printf("2-M.I-dx4w8 --> (1500 tl)\n\n (boyutu: 60x60x10cm)\n (agirlik: 131gr)\n (cekim mesafesi 250m)\n (ucus suresi: 20-25dk)\n (sarj suresi: 90dk)\n (kamera: 8Mp)\n\n");
			
			printf("Drone modelini seciniz:");
			scanf("%d",&model);
			
			birsatiratla();
			
			dekont();
			
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 750 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 1500 tl.\n\n");	
			}
			else
	    	{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
			
}



void kategoriAkilliSaat()
{
			int kategori,tip,model;
	
			printf("1-M.I-as1 --> (150 tl)\n\n (Bluetooth: V5.0)\n (Batarya: 135mAh)\n (Sarj Suresi: 1-2 Saat)\n (Bekleme Suresi: 20 Gün)\n (Aðirlik: 22.1Gr)\n (Boyut: 4.68x1.78x1.26Cm)\n\n");
			printf("2-M.I-as1 --> (350 tl)\n\n (Bluetooth: V5.0)\n (Batarya: 185mAh)\n (Sarj Suresi: 2-3 Saat)\n (Bekleme Suresi: 30 Gün)\n (Aðirlik: 31.1Gr)\n (Boyut: 5.78x1.84x1.31Cm)\n (Su gecirmez)\n\n");
			
			printf("Akilli saat modelini seciniz:");
			scanf("%d",&model);
			
			birsatiratla();
			
			dekont();
			
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 150 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 350 tl.\n\n");	
			}
			else
	    	{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
}



void kategoriFotografMakinesi()
{
			int kategori,tip,model;
	
			printf("1-M.I-fmsx --> (1250 tl)\n\n (16Mp)\n (50x zoom)\n (Batarya: 1500 mAh)\n (Þarj Olma Suresi: 2.5 Saat)\n (Wifi)\n\n");
			printf("2-M.I-fmcy --> (2500 tl)\n\n (48Mp)\n (80x zoom)\n (Batarya: 2000 mAh)\n (Þarj Olma Suresi: 3.5 Saat)\n (Wifi)\n\n");
										
			printf("Fotograf makinesinin modelini seciniz:");
			scanf("%d",&model);
		
			birsatiratla();
				
			dekont();	
					
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 1250 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 2500 tl.\n\n");	
			}
			else
			{
			printf("Hatali Islem!!!\n\n");
			}
				
			tesekkur();	
				
}



void kategoriPowerbank()
{
			int kategori,tip,model;
	
			printf("1-M.I-PWba --> (50 tl)\n\n (Kapasite: 10000mAh)\n (235gr)\n (2 adet usb cikisi)\n (boyutlari: 14x6.75x1.6Cm)\n (sarj Olma Suresi: 1 Saat)\n\n");
			printf("2-M.I-PWbc --> (150 tl)\n\n (Kapasite: 20000mAh)\n (320gr)\n (4 adet usb cikisi)\n (boyutlari: 16x7.85x1.8Cm)\n (sarj Olma Suresi: 2 Saat)\n\n");
										
			printf("Powerbank modelini seciniz:");
			scanf("%d",&model);
		
			birsatiratla();
			
			dekont();
					
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 50 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 150 tl.\n\n");	
			}
			else
			{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
				
}



void kategoriSanalGerceklikGozlugu()
{
			int kategori,tip,model;
	
			printf("1-M.I-sggx1 --> (250 tl)\n\n (445gr)\n (4'-6'inc ekran akilli cep telefonlari ile uyumlu)\n (boyutlari: 19.5x14x11cm)\n\n");
			printf("2-M.I-sggx2 --> (450 tl)\n\n (510gr)\n (3.5'-8'inc ekran akilli cep telefonlari ile uyumlu)\n (boyutlari: 21.5x16x12cm)\n (+ Kumanda)\n\n");
										
			printf("Sanal gerceklik gozlugu modelini seciniz:");
			scanf("%d",&model);
		
			birsatiratla();
			
			dekont();
					
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 250 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 450 tl.\n\n");	
			}
			else
			{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
				
}



void kategoriHoparlor()
{
			int kategori,tip,model;
	
			printf("1-Studyo Hoparlor\n");
			printf("2-Bluetooth Hoparlor");
			
			ikisatiratla();
			
			printf("Hoparlor tipini Seciniz:");
			scanf("%d",&tip);
			
			birsatiratla();
			
			switch(tip)
			{
				case 1:
					printf("1-M.I-EHkv1 --> (2000 tl)\n\n (agirligi: 5.3kg)\n (Yol: 2 yollu)\n (Kabin: Bassreflex)\n (Amplifikasyon: 25W tweeter | 45W woofer)\n (Frekans Cevabýi: 54Hz - 30kHz)\n (Woofer Boyutu: 5')\n (Tweeter : 1 Adet | Woofer : 1 Adet)\n\n");
					printf("2-M.I-EHkv2 --> (3500 tl)\n\n (agirligi: 10.2kg)\n (Yol: 2 yollu)\n (Kabin: Bassreflex)\n (Amplifikasyon: 45W tweeter | 70W woofer)\n (Frekans Cevabýi: 38Hz - 30kHz)\n (Woofer Boyutu: 8')\n (Tweeter : 2 Adet | Woofer : 2 Adet)\n\n");
				
					printf("Hoparlor modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 2000 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 3500 tl.\n\n");	
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
			
					}
					
					tesekkur();
					
					break;
					
				case 2:
					printf("1-M.I-BHs --> (250 tl)\n\n (2gb ram)\n (2gb ekran karti)\n (500gb hdd)\n (i3-6.nesil)\n\n");
					printf("2-M.I-BHm --> (500 tl)\n\n (4gb ram)\n (4gb ekran karti)\n (1tb hdd + 256gb ssd)\n (i5-7.nesil)\n\n");
					
					printf("Hoparlor modelini seciniz:");
					scanf("%d",&model);
					
					birsatiratla();
					
					dekont();
					
					if(model == 1)
					{
						printf("--->>> ODENECEK TUTAR: 250 tl.\n\n");
					}
					else if(model == 2)
					{
						printf("--->>> ODENECEK TUTAR: 500 tl.\n\n");	
					}
					else
					{
						printf("Hatali Islem!!!\n\n");
					}
					
					tesekkur();
					
					break;
			}
}



void kategoriBaglantiKablolari()
{
			int kategori,tip,model;
	
			printf("1-M.I-AUX Kablosu --> (25 tl)\n\n (uzunluk: 30cm)\n (orgu sarim)\n (altin kapli uc)\n\n");
			printf("2-M.I-HDMI Kablosu --> (40 tl)\n\n (uzunluk: 3.5m)\n (bakir kablo)\n\n");
			printf("3-M.I-VGA Kablosu --> (15 tl)\n\n (uzunluk: 2.5m)\n (bakir kablo)\n\n");
			
			printf("Baglanti kablosu modelini seciniz:");
			scanf("%d",&model);
			
			birsatiratla();
			
			dekont();
			
			if(model == 1)
			{
			printf("--->>> ODENECEK TUTAR: 25 tl.\n\n");
			}
			else if(model == 2)
			{
			printf("--->>> ODENECEK TUTAR: 40 tl.\n\n");	
			}
			else if(model == 3)
			{
			printf("--->>> ODENECEK TUTAR: 15 tl.\n\n");
			}
			else
	    	{
			printf("Hatali Islem!!!\n\n");
			}
			
			tesekkur();
			
}



void dekont()
	{
	FILE *outfile,*infile;
		
		char a;
		
		outfile=fopen("dekont.txt","r");
	
		while(!feof(outfile))
		{
			a=getc(outfile);
			
			printf("%c",a);
		}
		fclose(outfile);
		
		ikisatiratla();
		
		return 0;
}			



void tesekkur()
{
	printf("*****Magazamizi Tercih Ettiginiz Icin Tesekkur Ederiz.***** :))\n\n ");
}



void birsatiratla()
{
	printf("\n");
}



void ikisatiratla()
{
	printf("\n\n");
}

