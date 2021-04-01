#Python Combobox Application  
import tkinter as tk  
from tkinter import ttk
import stock as st
from stock import Normalize
import pandas as pd
from config.config import *
#df = pd.read_csv("C:\\Users\\Neeraj Kumar S J\\Desktop\\Stock Prediction\\prices_split_adj.csv")
SList = ["A",	"AAL",	"AAP",	"AAPL",	"ABBV",	"ABC",	"ABT",	"ACN",	"ADBE",	"ADI",	"ADM",	"ADP",	"ADS",	"ADSK",	"AEE",	"AEP","AES",	"AET",	"AFL",	"AGN",	"AIG",	"AIV",	"AIZ",	"AJG",	"AKAM",	"ALB",	"ALK",	"ALL",	"ALLE",	"ALXN",	"AMAT",	"AME",	"AMG",	"AMGN",	"AMP",	"AMT",	"AMZN",	"AN",	"ANTM",	"AON",	"APA",	"APC",	"APD",	"APH",	"ARNC",	"ATVI",	"AVB",	"AVGO",	"AVY",	"AWK",	"AXP",	"AYI",	"AZO",	"BA",	"BAC",	"BAX",	"BBBY",	"BBT",	"BBY",	"BCR",	"BDX",	"BEN",	"BHI",	"BIIB",	"BK",	"BLK",	"BLL",	"BMY",	"BSX",	"BWA",	"BXP",	"C",	"CA",	"CAG",	"CAH",	"CAT",	"CB",	"CBG",	"CBS",	"CCI",	"CCL",	"CELG",	"CERN",	"CF",	"CFG",	"CHD",	"CHK",	"CHRW",	"CHTR",	"CI",	"CINF",	"CL",	"CLX",	"CMA",	"CMCSA",	"CME",	"CMG",	"CMI",	"CMS",	"CNC",	"CNP",	"COF",	"COG",	"COH",	"COL",	"COO",	"COP",	"COST",	"COTY",	"CPB",	"CRM",	"CSCO",	"CSRA",	"CSX",	"CTAS",	"CTL",	"CTSH",	"CTXS",	"CVS",	"CVX",	"CXO",	"D",	"DAL",	"DD",	"DE",	"DFS",	"DG",	"DGX",	"DHI",	"DHR",	"DIS",	"DISCA",	"DISCK",	"DLPH",	"DLR",	"DLTR",	"DNB",	"DOV",	"DOW",	"DPS",	"DRI",	"DTE",	"DUK",	"DVA",	"DVN",	"EA",	"EBAY",	"ECL",	"ED",	"EFX",	"EIX",	"EL",	"EMN",	"EMR",	"ENDP",	"EOG",	"EQIX",	"EQR",	"EQT",	"ES",	"ESRX",	"ESS",	"ETFC",	"ETN",	"ETR",	"EVHC",	"EW",	"EXC",	"EXPD",	"EXPE",	"EXR",	"F",	"FAST",	"FB",	"FBHS",	"FCX",	"FDX",	"FE",	"FFIV",	"FIS",	"FISV",	"FITB",	"FL",	"FLIR",	"FLR",	"FLS",	"FMC",	"FOX",	"FOXA",	"FRT",	"FSLR",	"FTI",	"FTR",	"FTV",	"GD",	"GE",	"GGP",	"GILD",	"GIS",	"GLW",	"GM",	"GOOG",	"GOOGL",	"GPC",	"GPN",	"GPS",	"GRMN",	"GS",	"GT",	"GWW",	"HAL",	"HAR",	"HAS",	"HBAN",	"HBI",	"HCA",	"HCN",	"HCP",	"HD",	"HES",	"HIG",	"HOG",	"HOLX",	"HON",	"HP",	"HPE",	"HPQ",	"HRB",	"HRL",	"HRS",	"HSIC",	"HST",	"HSY",	"HUM",	"IBM",	"ICE",	"IDXX",	"IFF",	"ILMN",	"INTC",	"INTU",	"IP",	"IPG",	"IR",	"IRM",	"ISRG",	"ITW",	"IVZ",	"JBHT",	"JCI",	"JEC",	"JNJ",	"JNPR",	"JPM",	"JWN",	"K",	"KEY",	"KHC",	"KIM",	"KLAC",	"KMB",	"KMI",	"KMX",	"KO",	"KORS",	"KR",	"KSS",	"KSU",	"L",	"LB",	"LEG",	"LEN",	"LH",	"LKQ",	"LLL",	"LLTC",	"LLY",	"LMT",	"LNC",	"LNT",	"LOW",	"LRCX",	"LUK",	"LUV",	"LVLT",	"LYB",	"M",	"MA",	"MAA",	"MAC",	"MAR",	"MAS",	"MAT",	"MCD",	"MCHP",	"MCK",	"MCO",	"MDLZ",	"MDT",	"MET",	"MHK",	"MJN",	"MKC",	"MLM",	"MMC",	"MMM",	"MNK",	"MNST",	"MO",	"MON",	"MOS",	"MPC",	"MRK",	"MRO",	"MSFT",	"MSI",	"MTB",	"MTD",	"MU",	"MUR",	"MYL",	"NAVI",	"NBL",	"NDAQ",	"NEE",	"NEM",	"NFLX",	"NFX",	"NI",	"NKE",	"NLSN",	"NOC",	"NOV",	"NRG",	"NSC",	"NTAP",	"NTRS",	"NUE",	"NVDA",	"SWL",	"SWS",	"SWSA",	"O",	"OKE",	"OMC",	"ORCL",	"ORLY",	"OXY",	"PAYX",	"PBCT",	"PBI",	"PCAR",	"PCG",	"PCLN",	"PDCO",	"PEG",	"PEP",	"PFE",	"PFG",	"PG",	"PGR",	"PH",	"PHM",	"PKI",	"PLD",	"PM",	"PNC",	"PNR",	"PSW",	"PPG",	"PPL",	"PRGO",	"PRU",	"PSA",	"PSX",	"PVH",	"PWR",	"PX",	"PXD",	"PYPL",	"QCOM",	"QRVO",	"R",	"RAI",	"RCL",	"REGN",	"RF",	"RHI",	"RHT",	"RIG",	"RL",	"ROK",	"ROP",	"ROST",	"RRC",	"RSG",	"RTN",	"SBUX",	"SCG",	"SCHW",	"SE",	"SEE",	"SHW",	"SIG",	"SJM",	"SLB",	"SLG",	"SNA",	"SNI",	"SO",	"SPG",	"SPGI",	"SPLS",	"SRCL",	"SRE",	"STI",	"STT",	"STX",	"STZ",	"SWK",	"SWKS",	"SWN",	"SYF",	"SYK",	"SYMC",	"SYY",	"T",	"TAP",	"TDC",	"TDG",	"TEL",	"TGNA",	"TGT",	"TIF",	"TJX",	"TMK",	"TMO",	"TRIP",	"TROW",	"TRV",	"TSCO",	"TSN",	"TSO",	"TSS",	"TWX",	"TXN",	"TXT",	"UAA",	"UAL",	"UDR",	"UHS",	"ULTA",	"UNH",	"UNM",	"UNP",	"UPS",	"URBN",	"URI",	"USB",	"UTX",	"V",	"VAR",	"VFC",	"VIAB",	"VLO",	"VMC",	"VNO",	"VRSK",	"VRSN",	"VRTX",	"VTR",	"VZ",	"WAT",	"WBA",	"WDC",	"WEC",	"WFC",	"WFM",	"WHR",	"WLTW",	"WM",	"WMB",	"WMT",	"WRK",	"WU",	"WY",	"WYN",	"WYNN",	"XEC",	"XEL",	"XL",	"XLNX",	"XOM",	"XRAY",	"XRX",	"XYL",	"YHOO",	"YUM",	"ZBH",	"ZION",	"ZTS"]
win = tk.Tk()  
#Application Name  
win.title("N-StocPred")
#Label Creation  
ttk.Label(win, text="Choose Company Name:").grid(column=0,row=0)
win.resizable(100,100)
#Combobox Creation  
number= tk.StringVar()  
numberChosen= ttk.Combobox(win, width=12, textvariable=number)
#Adding Values  
numberChosen['values']=SList
st.Seek_trend = numberChosen['values']
numberChosen.grid(column=1,row=0, sticky="NW")  
numberChosen.current()

#Button Action
#button Creation  
action = ttk.Button(win, text="Predict", command=Normalize)  
action.grid(column=1,row=6, sticky='SW')  

#Checkbox
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
#V1 = tk.Checkbutton(win, text="----------", variable=var1)
V2 = tk.Checkbutton(win, text="High", variable=var2)
V3 = tk.Checkbutton(win, text="Low", variable=var3)
V4 = tk.Checkbutton(win, text="Open", variable=var4)
V5 = tk.Checkbutton(win, text="Close", variable=var5)
V6 = tk.Checkbutton(win, text="Volume", variable=var6)
V2.grid(column=1,row=1, sticky='NW')
V3.grid(column=1,row=2, sticky='NW')
V4.grid(column=1,row=3, sticky='NW')
V5.grid(column=1,row=4, sticky='NW')
V6.grid(column=1,row=5, sticky='NW')

#ToolBar

menu=tk.Menu(win)
Submenu = tk.Menu(menu)
menu.add_cascade(label='File', menu= Submenu)
Submenu.add_cascade(label="Load Data")
Submenu.add_cascade(label="Print Prview")
Submenu.add_cascade(label="Print")
Submenu.add_separator()
Submenu.add_cascade(label="Exit")

Help = tk.Menu(menu)
menu.add_cascade(label='Help', menu= Help)
win.configure(menu = menu)
#Photo
#pic = tk.PhotoImage(file="D:\\neeraj kumar sj\\Studies\\DSU\\CSE_4TH_YR\\8th sem\\project\My Stock\\Hist Stock.png")
#label1 = tk.Label(win, image=pic)
#label1.grid(column=6,row=1, sticky="NE")
pic2 = tk.PhotoImage(file="D:\\neeraj kumar sj\\Studies\\DSU\\CSE_4TH_YR\\8th sem\\project\My Stock\\Predict1.png")
label2 = tk.Label(win, image=pic2)
label2.grid(column=1,row=8, sticky="SW")

#label1.pack()
#label2.pack()

#V2.pack()
#V3.pack()
#V4.pack()
#V5.pack()
#V6.pack()
#Submenu.pack()
#label.pack

#Calling Main()  
win.mainloop()
#***********************************************************


