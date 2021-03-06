import os
import datetime

class renderfile:
	def __init__(self,pathfoldes):
		self.file_name = []
		self.file_path = []
		self.file_size = []
		self.file_ctime = []
		self.file_mtime = []
		self.file_type = []		
		for path, dirs, files in os.walk(pathfoldes):
			for file in files:
				stat = os.stat(os.path.join( path, file  ))
				#print(file)
				self.file_name.append(file.split(".")[0])
				self.file_type.append(file.split(".")[-1])
				#print(os.path.join(path, file).replace('\\','/')[1:])
				self.file_path.append(os.path.join(path, file)[1:])
				#print("{:10.2f}".format(stat.st_size/1024))
				self.file_size.append("{:10.2f}".format(stat.st_size/1024))
				#print(datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%H:%M %d/%m/%Y'))
				self.file_mtime.append(datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%H:%M %d/%m/%Y'))
				#print(datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%H:%M %d/%m/%Y'))
				self.file_ctime.append(datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%H:%M %d/%m/%Y'))
		


	def make_html_files(self):

		content = '''<!DOCTYPE html>
<!-- saved from url=(0028)http://localhost/files.html? -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Directory</title>
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>

html {
				height: 100%;
				background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
				overflow: hidden;
				}

				#stars {
				width: 1px;
				height: 1px;
				background: transparent;
				box-shadow: 522px 1734px #FFF , 403px 989px #FFF , 833px 1354px #FFF , 865px 1955px #FFF , 644px 352px #FFF , 1776px 1492px #FFF , 423px 1926px #FFF , 1994px 1122px #FFF , 810px 31px #FFF , 1667px 1409px #FFF , 1101px 476px #FFF , 838px 129px #FFF , 572px 385px #FFF , 105px 1891px #FFF , 1454px 1316px #FFF , 495px 314px #FFF , 29px 1427px #FFF , 1366px 67px #FFF , 1615px 1741px #FFF , 757px 399px #FFF , 1631px 187px #FFF , 1748px 1966px #FFF , 1963px 1459px #FFF , 1335px 433px #FFF , 467px 1010px #FFF , 601px 1724px #FFF , 240px 1155px #FFF , 877px 1085px #FFF , 1728px 1623px #FFF , 1945px 295px #FFF , 964px 837px #FFF , 390px 1753px #FFF , 1609px 1152px #FFF , 862px 210px #FFF , 1783px 1016px #FFF , 38px 1669px #FFF , 721px 657px #FFF , 266px 921px #FFF , 1006px 1472px #FFF , 1985px 807px #FFF , 200px 1085px #FFF , 326px 1115px #FFF , 410px 790px #FFF , 494px 285px #FFF , 875px 866px #FFF , 1750px 1106px #FFF , 1571px 1600px #FFF , 1213px 453px #FFF , 1497px 1862px #FFF , 1052px 1790px #FFF , 1635px 549px #FFF , 1955px 1808px #FFF , 297px 1866px #FFF , 1221px 1014px #FFF , 1199px 1948px #FFF , 434px 1437px #FFF , 639px 1293px #FFF , 39px 1150px #FFF , 31px 1145px #FFF , 173px 806px #FFF , 1962px 986px #FFF , 1130px 1729px #FFF , 271px 747px #FFF , 328px 746px #FFF , 1751px 126px #FFF , 1603px 571px #FFF , 1493px 1786px #FFF , 1280px 80px #FFF , 1348px 1775px #FFF , 408px 1910px #FFF , 537px 318px #FFF , 990px 994px #FFF , 1060px 915px #FFF , 640px 710px #FFF , 683px 186px #FFF , 1900px 1828px #FFF , 1818px 1564px #FFF , 1375px 1104px #FFF , 534px 116px #FFF , 1176px 886px #FFF , 84px 1998px #FFF , 1304px 334px #FFF , 983px 1975px #FFF , 911px 1305px #FFF , 1499px 973px #FFF , 1213px 1862px #FFF , 823px 1028px #FFF , 841px 1582px #FFF , 474px 1149px #FFF , 106px 1486px #FFF , 1448px 737px #FFF , 27px 270px #FFF , 971px 1922px #FFF , 1685px 1739px #FFF , 1855px 1067px #FFF , 418px 409px #FFF , 955px 1929px #FFF , 953px 683px #FFF , 1416px 1613px #FFF , 1546px 579px #FFF , 1974px 385px #FFF , 428px 1930px #FFF , 1693px 1470px #FFF , 666px 1615px #FFF , 1437px 1123px #FFF , 292px 837px #FFF , 473px 1140px #FFF , 593px 176px #FFF , 260px 1847px #FFF , 885px 222px #FFF , 1749px 1645px #FFF , 583px 1841px #FFF , 948px 1728px #FFF , 1645px 1296px #FFF , 290px 1101px #FFF , 1984px 750px #FFF , 679px 185px #FFF , 1131px 631px #FFF , 335px 721px #FFF , 336px 1325px #FFF , 949px 1885px #FFF , 396px 1460px #FFF , 1828px 101px #FFF , 1275px 716px #FFF , 1312px 1648px #FFF , 95px 378px #FFF , 1900px 1341px #FFF , 1035px 1451px #FFF , 208px 1809px #FFF , 300px 60px #FFF , 691px 256px #FFF , 451px 1829px #FFF , 868px 585px #FFF , 498px 1265px #FFF , 525px 460px #FFF , 1397px 414px #FFF , 1204px 539px #FFF , 1208px 596px #FFF , 1106px 1583px #FFF , 222px 1187px #FFF , 1540px 1473px #FFF , 588px 578px #FFF , 640px 1535px #FFF , 1414px 902px #FFF , 1687px 1459px #FFF , 1980px 1725px #FFF , 617px 1992px #FFF , 1238px 1902px #FFF , 853px 1442px #FFF , 760px 1789px #FFF , 1307px 1376px #FFF , 773px 173px #FFF , 1035px 1274px #FFF , 232px 222px #FFF , 1824px 66px #FFF , 1619px 1707px #FFF , 1159px 337px #FFF , 1117px 1500px #FFF , 1964px 77px #FFF , 1504px 531px #FFF , 424px 998px #FFF , 152px 1838px #FFF , 64px 257px #FFF , 1098px 695px #FFF , 956px 246px #FFF , 282px 370px #FFF , 1205px 1060px #FFF , 1745px 1689px #FFF , 1441px 1897px #FFF , 664px 1751px #FFF , 1679px 770px #FFF , 1250px 346px #FFF , 220px 1069px #FFF , 493px 1574px #FFF , 1488px 726px #FFF , 1952px 1596px #FFF , 245px 1849px #FFF , 1148px 339px #FFF , 1233px 987px #FFF , 852px 1365px #FFF , 1460px 91px #FFF , 728px 1623px #FFF , 827px 970px #FFF , 1272px 235px #FFF , 114px 1804px #FFF , 39px 1736px #FFF , 418px 300px #FFF , 1170px 1070px #FFF , 1025px 1593px #FFF , 405px 319px #FFF , 1300px 1246px #FFF , 1918px 21px #FFF , 1469px 1456px #FFF , 1505px 410px #FFF , 770px 1113px #FFF , 111px 1297px #FFF , 1722px 1271px #FFF , 1677px 666px #FFF , 1645px 1061px #FFF , 652px 36px #FFF , 1420px 1210px #FFF , 1128px 84px #FFF , 1173px 4px #FFF , 1537px 1294px #FFF , 695px 732px #FFF , 1638px 426px #FFF , 1133px 1513px #FFF , 1714px 937px #FFF , 1573px 1628px #FFF , 1626px 1319px #FFF , 393px 799px #FFF , 1526px 1402px #FFF , 1895px 1166px #FFF , 1315px 886px #FFF , 32px 1191px #FFF , 1967px 823px #FFF , 1649px 355px #FFF , 1062px 1956px #FFF , 1157px 1000px #FFF , 1015px 685px #FFF , 1978px 957px #FFF , 1991px 379px #FFF , 649px 1608px #FFF , 672px 384px #FFF , 113px 21px #FFF , 1855px 1632px #FFF , 1295px 1116px #FFF , 482px 146px #FFF , 1656px 688px #FFF , 429px 1153px #FFF , 111px 997px #FFF , 583px 1716px #FFF , 470px 59px #FFF , 983px 1012px #FFF , 193px 1034px #FFF , 694px 1958px #FFF , 946px 157px #FFF , 1733px 1110px #FFF , 1339px 600px #FFF , 422px 751px #FFF , 1747px 410px #FFF , 1542px 865px #FFF , 1152px 381px #FFF , 753px 361px #FFF , 822px 746px #FFF , 1878px 354px #FFF , 1353px 1766px #FFF , 1285px 721px #FFF , 418px 1763px #FFF , 1830px 908px #FFF , 1689px 884px #FFF , 778px 75px #FFF , 1468px 1661px #FFF , 1096px 1862px #FFF , 139px 1179px #FFF , 536px 743px #FFF , 979px 321px #FFF , 300px 1603px #FFF , 634px 183px #FFF , 983px 1347px #FFF , 1049px 1803px #FFF , 1657px 1868px #FFF , 1202px 1772px #FFF , 1558px 369px #FFF , 1423px 1726px #FFF , 191px 1301px #FFF , 714px 1478px #FFF , 792px 1278px #FFF , 1699px 1903px #FFF , 114px 582px #FFF , 380px 1847px #FFF , 200px 135px #FFF , 1499px 1281px #FFF , 299px 191px #FFF , 827px 999px #FFF , 1522px 1106px #FFF , 665px 248px #FFF , 1763px 1676px #FFF , 1585px 342px #FFF , 937px 89px #FFF , 1123px 818px #FFF , 1714px 1024px #FFF , 942px 1663px #FFF , 1794px 1921px #FFF , 790px 865px #FFF , 1619px 1549px #FFF , 1645px 322px #FFF , 1521px 949px #FFF , 1301px 1131px #FFF , 628px 1531px #FFF , 1422px 1361px #FFF , 64px 1852px #FFF , 1475px 497px #FFF , 241px 376px #FFF , 533px 1569px #FFF , 489px 1626px #FFF , 514px 1212px #FFF , 121px 1443px #FFF , 895px 173px #FFF , 732px 1363px #FFF , 1583px 1310px #FFF , 1308px 1134px #FFF , 927px 1417px #FFF , 1765px 1350px #FFF , 561px 1978px #FFF , 181px 1956px #FFF , 1311px 729px #FFF , 1840px 1954px #FFF , 507px 621px #FFF , 1518px 1799px #FFF , 1763px 103px #FFF , 1779px 1947px #FFF , 335px 1989px #FFF , 1722px 1870px #FFF , 1067px 593px #FFF , 764px 964px #FFF , 262px 851px #FFF , 1001px 609px #FFF , 901px 1578px #FFF , 1835px 118px #FFF , 1180px 1508px #FFF , 1004px 1635px #FFF , 992px 1699px #FFF , 1044px 1399px #FFF , 1144px 560px #FFF , 629px 318px #FFF , 973px 1437px #FFF , 682px 933px #FFF , 1655px 1539px #FFF , 302px 184px #FFF , 1832px 1810px #FFF , 141px 587px #FFF , 35px 200px #FFF , 1762px 551px #FFF , 1509px 1088px #FFF , 799px 1874px #FFF , 23px 1199px #FFF , 663px 1183px #FFF , 461px 387px #FFF , 129px 460px #FFF , 1805px 148px #FFF , 807px 1616px #FFF , 1580px 1254px #FFF , 1650px 805px #FFF , 1679px 1619px #FFF , 1190px 1648px #FFF , 917px 571px #FFF , 1991px 1570px #FFF , 59px 407px #FFF , 1811px 1926px #FFF , 1826px 1256px #FFF , 1072px 507px #FFF , 1180px 1033px #FFF , 510px 351px #FFF , 1646px 854px #FFF , 240px 1658px #FFF , 1826px 1704px #FFF , 1912px 445px #FFF , 1642px 1754px #FFF , 291px 580px #FFF , 1830px 817px #FFF , 1403px 959px #FFF , 636px 219px #FFF , 329px 923px #FFF , 1680px 1502px #FFF , 125px 1225px #FFF , 1005px 119px #FFF , 621px 1025px #FFF , 199px 219px #FFF , 1324px 1006px #FFF , 1964px 701px #FFF , 1125px 757px #FFF , 808px 1907px #FFF , 592px 1146px #FFF , 150px 1461px #FFF , 149px 835px #FFF , 155px 1216px #FFF , 356px 566px #FFF , 685px 1711px #FFF , 81px 324px #FFF , 1367px 1468px #FFF , 733px 1573px #FFF , 1891px 419px #FFF , 291px 1857px #FFF , 714px 1536px #FFF , 904px 190px #FFF , 507px 1968px #FFF , 1050px 389px #FFF , 995px 962px #FFF , 412px 207px #FFF , 1369px 907px #FFF , 1615px 1637px #FFF , 683px 1612px #FFF , 50px 727px #FFF , 367px 524px #FFF , 1323px 475px #FFF , 1983px 648px #FFF , 1442px 49px #FFF , 1310px 147px #FFF , 814px 1389px #FFF , 1299px 1660px #FFF , 1633px 277px #FFF , 617px 273px #FFF , 1382px 317px #FFF , 571px 710px #FFF , 1846px 259px #FFF , 1764px 1009px #FFF , 1431px 1780px #FFF , 93px 1807px #FFF , 1037px 252px #FFF , 1405px 719px #FFF , 1687px 1055px #FFF , 1397px 1944px #FFF , 159px 1718px #FFF , 1052px 1291px #FFF , 318px 1489px #FFF , 106px 1401px #FFF , 1755px 1876px #FFF , 1006px 280px #FFF , 1530px 1860px #FFF , 745px 875px #FFF , 1329px 1654px #FFF , 327px 1341px #FFF , 1371px 1677px #FFF , 735px 1378px #FFF , 126px 455px #FFF , 1889px 896px #FFF , 1884px 565px #FFF , 182px 168px #FFF , 1940px 1262px #FFF , 314px 583px #FFF , 1748px 1977px #FFF , 1482px 702px #FFF , 210px 1602px #FFF , 1412px 1598px #FFF , 821px 1131px #FFF , 1130px 1835px #FFF , 1778px 608px #FFF , 84px 184px #FFF , 1434px 998px #FFF , 1305px 385px #FFF , 758px 1128px #FFF , 661px 1223px #FFF , 84px 178px #FFF , 1376px 1604px #FFF , 1163px 1375px #FFF , 985px 1087px #FFF , 1854px 670px #FFF , 1593px 262px #FFF , 1510px 1974px #FFF , 1381px 711px #FFF , 1621px 1532px #FFF , 1876px 762px #FFF , 1160px 1469px #FFF , 77px 1379px #FFF , 415px 1259px #FFF , 1401px 50px #FFF , 1141px 336px #FFF , 759px 1948px #FFF , 316px 1466px #FFF , 372px 538px #FFF , 907px 1036px #FFF , 151px 1317px #FFF , 1695px 605px #FFF , 575px 1234px #FFF , 169px 793px #FFF , 835px 1068px #FFF , 1611px 1409px #FFF , 1180px 1194px #FFF , 510px 1674px #FFF , 1297px 221px #FFF , 1798px 1456px #FFF , 959px 478px #FFF , 1368px 802px #FFF , 1922px 1415px #FFF , 443px 341px #FFF , 1609px 1045px #FFF , 229px 139px #FFF , 1068px 119px #FFF , 1871px 400px #FFF , 973px 1906px #FFF , 901px 200px #FFF , 1979px 1837px #FFF , 1134px 441px #FFF , 518px 964px #FFF , 1781px 270px #FFF , 602px 1849px #FFF , 98px 1533px #FFF , 13px 1903px #FFF , 1421px 245px #FFF , 516px 1239px #FFF , 462px 1421px #FFF , 1540px 775px #FFF , 1417px 1107px #FFF , 569px 1655px #FFF , 1388px 799px #FFF , 1903px 741px #FFF , 781px 104px #FFF , 1091px 364px #FFF , 814px 1144px #FFF , 795px 1876px #FFF , 499px 860px #FFF , 1068px 634px #FFF , 135px 358px #FFF , 12px 895px #FFF , 630px 1944px #FFF , 415px 1972px #FFF , 1000px 1829px #FFF , 1668px 606px #FFF , 1014px 1601px #FFF , 1905px 243px #FFF , 1912px 1280px #FFF , 1871px 848px #FFF , 1859px 227px #FFF , 1164px 218px #FFF , 1656px 1195px #FFF , 1006px 526px #FFF , 836px 1883px #FFF , 389px 228px #FFF , 1933px 935px #FFF , 956px 878px #FFF , 1190px 879px #FFF , 1254px 497px #FFF , 545px 784px #FFF , 792px 1688px #FFF , 85px 659px #FFF , 1506px 612px #FFF , 914px 990px #FFF , 1686px 1951px #FFF , 951px 1532px #FFF , 438px 1869px #FFF , 973px 1124px #FFF , 1725px 1503px #FFF , 1036px 630px #FFF , 1655px 619px #FFF , 48px 1164px #FFF , 1940px 869px #FFF , 671px 1100px #FFF , 569px 1306px #FFF , 92px 1447px #FFF , 14px 1956px #FFF , 355px 1763px #FFF , 630px 1788px #FFF , 1732px 1733px #FFF , 633px 1807px #FFF , 1774px 1394px #FFF , 1356px 1176px #FFF , 417px 1440px #FFF , 1946px 1798px #FFF , 604px 341px #FFF , 1341px 7px #FFF , 1486px 1944px #FFF , 1787px 1161px #FFF , 383px 671px #FFF , 1181px 1032px #FFF , 1116px 356px #FFF , 1151px 1007px #FFF , 543px 273px #FFF , 1663px 1759px #FFF , 1281px 1525px #FFF , 1173px 1640px #FFF , 1569px 295px #FFF , 1211px 958px #FFF , 1401px 189px #FFF , 343px 784px #FFF , 512px 1339px #FFF , 1592px 536px #FFF , 1774px 421px #FFF , 500px 385px #FFF , 1569px 488px #FFF , 512px 1171px #FFF , 1127px 944px #FFF , 1203px 1061px #FFF , 99px 695px #FFF , 111px 176px #FFF , 1014px 1111px #FFF , 1955px 1594px #FFF , 1257px 1358px #FFF , 1735px 228px #FFF , 986px 1134px #FFF , 1391px 800px #FFF , 575px 1410px #FFF , 1700px 1357px #FFF , 1507px 810px #FFF , 296px 782px #FFF , 673px 1177px #FFF , 804px 1225px #FFF , 829px 804px #FFF , 1169px 595px #FFF , 1539px 987px #FFF , 180px 1747px #FFF , 1826px 1131px #FFF , 383px 1193px #FFF , 1728px 932px #FFF , 286px 1695px #FFF , 1046px 389px #FFF , 1262px 176px #FFF , 991px 60px #FFF , 766px 1554px #FFF , 387px 530px #FFF , 328px 697px #FFF , 1058px 699px #FFF , 1110px 1937px #FFF , 1103px 1803px #FFF , 1631px 1902px #FFF , 1579px 989px #FFF , 1140px 1666px #FFF , 692px 118px #FFF , 1268px 1836px #FFF , 1198px 148px #FFF , 1818px 982px #FFF , 1591px 791px #FFF , 1231px 1435px #FFF , 1039px 1533px #FFF , 1781px 1959px #FFF , 1845px 644px #FFF , 1319px 5px #FFF , 792px 1102px #FFF , 1885px 1435px #FFF , 910px 1191px #FFF , 497px 55px #FFF , 1260px 574px #FFF , 1212px 229px #FFF , 1571px 1763px #FFF , 1649px 1605px #FFF , 1529px 1418px #FFF , 949px 276px #FFF , 1158px 580px #FFF , 1018px 337px #FFF , 1317px 1690px #FFF , 1238px 1704px #FFF , 1784px 1168px #FFF , 1701px 185px #FFF , 1626px 1443px #FFF , 1285px 1159px #FFF , 1157px 246px #FFF , 411px 273px #FFF , 758px 940px #FFF , 1764px 488px #FFF , 218px 642px #FFF , 1529px 355px #FFF , 703px 794px #FFF , 454px 1934px #FFF , 1791px 173px #FFF , 1432px 104px #FFF , 708px 1827px #FFF , 1168px 838px #FFF , 678px 961px #FFF , 987px 1690px #FFF , 1392px 590px #FFF , 220px 289px #FFF , 50px 1230px #FFF , 35px 55px #FFF , 1993px 963px #FFF , 1259px 1686px #FFF , 952px 1541px #FFF , 1482px 461px #FFF , 186px 83px #FFF , 1843px 935px #FFF , 721px 1063px #FFF , 1450px 1252px #FFF , 224px 1403px #FFF , 1983px 1623px #FFF , 324px 115px #FFF , 1643px 1295px #FFF , 511px 504px #FFF , 809px 174px #FFF , 1212px 1263px #FFF , 643px 1196px #FFF , 958px 419px #FFF , 263px 1534px #FFF , 1763px 1644px #FFF , 1438px 1281px #FFF , 1504px 1746px #FFF , 1555px 1651px #FFF , 854px 483px #FFF , 539px 1755px #FFF , 551px 1030px #FFF , 844px 1091px #FFF , 1437px 720px #FFF , 358px 863px #FFF , 1150px 1399px #FFF , 42px 171px #FFF , 1364px 1748px #FFF , 1232px 1561px #FFF , 265px 1204px #FFF , 1969px 610px #FFF , 1052px 480px #FFF , 1619px 1303px #FFF , 91px 1994px #FFF , 461px 543px #FFF , 645px 11px #FFF , 1251px 504px #FFF , 1991px 1039px #FFF , 819px 1371px #FFF , 1395px 1921px #FFF , 454px 441px #FFF , 1678px 1434px #FFF , 955px 1372px #FFF , 552px 164px #FFF;
				animation: animStar 50s linear infinite;
				}
				#stars:after {
				content: " ";
				position: absolute;
				top: 2000px;
				width: 1px;
				height: 1px;
				background: transparent;
				box-shadow: 522px 1734px #FFF , 403px 989px #FFF , 833px 1354px #FFF , 865px 1955px #FFF , 644px 352px #FFF , 1776px 1492px #FFF , 423px 1926px #FFF , 1994px 1122px #FFF , 810px 31px #FFF , 1667px 1409px #FFF , 1101px 476px #FFF , 838px 129px #FFF , 572px 385px #FFF , 105px 1891px #FFF , 1454px 1316px #FFF , 495px 314px #FFF , 29px 1427px #FFF , 1366px 67px #FFF , 1615px 1741px #FFF , 757px 399px #FFF , 1631px 187px #FFF , 1748px 1966px #FFF , 1963px 1459px #FFF , 1335px 433px #FFF , 467px 1010px #FFF , 601px 1724px #FFF , 240px 1155px #FFF , 877px 1085px #FFF , 1728px 1623px #FFF , 1945px 295px #FFF , 964px 837px #FFF , 390px 1753px #FFF , 1609px 1152px #FFF , 862px 210px #FFF , 1783px 1016px #FFF , 38px 1669px #FFF , 721px 657px #FFF , 266px 921px #FFF , 1006px 1472px #FFF , 1985px 807px #FFF , 200px 1085px #FFF , 326px 1115px #FFF , 410px 790px #FFF , 494px 285px #FFF , 875px 866px #FFF , 1750px 1106px #FFF , 1571px 1600px #FFF , 1213px 453px #FFF , 1497px 1862px #FFF , 1052px 1790px #FFF , 1635px 549px #FFF , 1955px 1808px #FFF , 297px 1866px #FFF , 1221px 1014px #FFF , 1199px 1948px #FFF , 434px 1437px #FFF , 639px 1293px #FFF , 39px 1150px #FFF , 31px 1145px #FFF , 173px 806px #FFF , 1962px 986px #FFF , 1130px 1729px #FFF , 271px 747px #FFF , 328px 746px #FFF , 1751px 126px #FFF , 1603px 571px #FFF , 1493px 1786px #FFF , 1280px 80px #FFF , 1348px 1775px #FFF , 408px 1910px #FFF , 537px 318px #FFF , 990px 994px #FFF , 1060px 915px #FFF , 640px 710px #FFF , 683px 186px #FFF , 1900px 1828px #FFF , 1818px 1564px #FFF , 1375px 1104px #FFF , 534px 116px #FFF , 1176px 886px #FFF , 84px 1998px #FFF , 1304px 334px #FFF , 983px 1975px #FFF , 911px 1305px #FFF , 1499px 973px #FFF , 1213px 1862px #FFF , 823px 1028px #FFF , 841px 1582px #FFF , 474px 1149px #FFF , 106px 1486px #FFF , 1448px 737px #FFF , 27px 270px #FFF , 971px 1922px #FFF , 1685px 1739px #FFF , 1855px 1067px #FFF , 418px 409px #FFF , 955px 1929px #FFF , 953px 683px #FFF , 1416px 1613px #FFF , 1546px 579px #FFF , 1974px 385px #FFF , 428px 1930px #FFF , 1693px 1470px #FFF , 666px 1615px #FFF , 1437px 1123px #FFF , 292px 837px #FFF , 473px 1140px #FFF , 593px 176px #FFF , 260px 1847px #FFF , 885px 222px #FFF , 1749px 1645px #FFF , 583px 1841px #FFF , 948px 1728px #FFF , 1645px 1296px #FFF , 290px 1101px #FFF , 1984px 750px #FFF , 679px 185px #FFF , 1131px 631px #FFF , 335px 721px #FFF , 336px 1325px #FFF , 949px 1885px #FFF , 396px 1460px #FFF , 1828px 101px #FFF , 1275px 716px #FFF , 1312px 1648px #FFF , 95px 378px #FFF , 1900px 1341px #FFF , 1035px 1451px #FFF , 208px 1809px #FFF , 300px 60px #FFF , 691px 256px #FFF , 451px 1829px #FFF , 868px 585px #FFF , 498px 1265px #FFF , 525px 460px #FFF , 1397px 414px #FFF , 1204px 539px #FFF , 1208px 596px #FFF , 1106px 1583px #FFF , 222px 1187px #FFF , 1540px 1473px #FFF , 588px 578px #FFF , 640px 1535px #FFF , 1414px 902px #FFF , 1687px 1459px #FFF , 1980px 1725px #FFF , 617px 1992px #FFF , 1238px 1902px #FFF , 853px 1442px #FFF , 760px 1789px #FFF , 1307px 1376px #FFF , 773px 173px #FFF , 1035px 1274px #FFF , 232px 222px #FFF , 1824px 66px #FFF , 1619px 1707px #FFF , 1159px 337px #FFF , 1117px 1500px #FFF , 1964px 77px #FFF , 1504px 531px #FFF , 424px 998px #FFF , 152px 1838px #FFF , 64px 257px #FFF , 1098px 695px #FFF , 956px 246px #FFF , 282px 370px #FFF , 1205px 1060px #FFF , 1745px 1689px #FFF , 1441px 1897px #FFF , 664px 1751px #FFF , 1679px 770px #FFF , 1250px 346px #FFF , 220px 1069px #FFF , 493px 1574px #FFF , 1488px 726px #FFF , 1952px 1596px #FFF , 245px 1849px #FFF , 1148px 339px #FFF , 1233px 987px #FFF , 852px 1365px #FFF , 1460px 91px #FFF , 728px 1623px #FFF , 827px 970px #FFF , 1272px 235px #FFF , 114px 1804px #FFF , 39px 1736px #FFF , 418px 300px #FFF , 1170px 1070px #FFF , 1025px 1593px #FFF , 405px 319px #FFF , 1300px 1246px #FFF , 1918px 21px #FFF , 1469px 1456px #FFF , 1505px 410px #FFF , 770px 1113px #FFF , 111px 1297px #FFF , 1722px 1271px #FFF , 1677px 666px #FFF , 1645px 1061px #FFF , 652px 36px #FFF , 1420px 1210px #FFF , 1128px 84px #FFF , 1173px 4px #FFF , 1537px 1294px #FFF , 695px 732px #FFF , 1638px 426px #FFF , 1133px 1513px #FFF , 1714px 937px #FFF , 1573px 1628px #FFF , 1626px 1319px #FFF , 393px 799px #FFF , 1526px 1402px #FFF , 1895px 1166px #FFF , 1315px 886px #FFF , 32px 1191px #FFF , 1967px 823px #FFF , 1649px 355px #FFF , 1062px 1956px #FFF , 1157px 1000px #FFF , 1015px 685px #FFF , 1978px 957px #FFF , 1991px 379px #FFF , 649px 1608px #FFF , 672px 384px #FFF , 113px 21px #FFF , 1855px 1632px #FFF , 1295px 1116px #FFF , 482px 146px #FFF , 1656px 688px #FFF , 429px 1153px #FFF , 111px 997px #FFF , 583px 1716px #FFF , 470px 59px #FFF , 983px 1012px #FFF , 193px 1034px #FFF , 694px 1958px #FFF , 946px 157px #FFF , 1733px 1110px #FFF , 1339px 600px #FFF , 422px 751px #FFF , 1747px 410px #FFF , 1542px 865px #FFF , 1152px 381px #FFF , 753px 361px #FFF , 822px 746px #FFF , 1878px 354px #FFF , 1353px 1766px #FFF , 1285px 721px #FFF , 418px 1763px #FFF , 1830px 908px #FFF , 1689px 884px #FFF , 778px 75px #FFF , 1468px 1661px #FFF , 1096px 1862px #FFF , 139px 1179px #FFF , 536px 743px #FFF , 979px 321px #FFF , 300px 1603px #FFF , 634px 183px #FFF , 983px 1347px #FFF , 1049px 1803px #FFF , 1657px 1868px #FFF , 1202px 1772px #FFF , 1558px 369px #FFF , 1423px 1726px #FFF , 191px 1301px #FFF , 714px 1478px #FFF , 792px 1278px #FFF , 1699px 1903px #FFF , 114px 582px #FFF , 380px 1847px #FFF , 200px 135px #FFF , 1499px 1281px #FFF , 299px 191px #FFF , 827px 999px #FFF , 1522px 1106px #FFF , 665px 248px #FFF , 1763px 1676px #FFF , 1585px 342px #FFF , 937px 89px #FFF , 1123px 818px #FFF , 1714px 1024px #FFF , 942px 1663px #FFF , 1794px 1921px #FFF , 790px 865px #FFF , 1619px 1549px #FFF , 1645px 322px #FFF , 1521px 949px #FFF , 1301px 1131px #FFF , 628px 1531px #FFF , 1422px 1361px #FFF , 64px 1852px #FFF , 1475px 497px #FFF , 241px 376px #FFF , 533px 1569px #FFF , 489px 1626px #FFF , 514px 1212px #FFF , 121px 1443px #FFF , 895px 173px #FFF , 732px 1363px #FFF , 1583px 1310px #FFF , 1308px 1134px #FFF , 927px 1417px #FFF , 1765px 1350px #FFF , 561px 1978px #FFF , 181px 1956px #FFF , 1311px 729px #FFF , 1840px 1954px #FFF , 507px 621px #FFF , 1518px 1799px #FFF , 1763px 103px #FFF , 1779px 1947px #FFF , 335px 1989px #FFF , 1722px 1870px #FFF , 1067px 593px #FFF , 764px 964px #FFF , 262px 851px #FFF , 1001px 609px #FFF , 901px 1578px #FFF , 1835px 118px #FFF , 1180px 1508px #FFF , 1004px 1635px #FFF , 992px 1699px #FFF , 1044px 1399px #FFF , 1144px 560px #FFF , 629px 318px #FFF , 973px 1437px #FFF , 682px 933px #FFF , 1655px 1539px #FFF , 302px 184px #FFF , 1832px 1810px #FFF , 141px 587px #FFF , 35px 200px #FFF , 1762px 551px #FFF , 1509px 1088px #FFF , 799px 1874px #FFF , 23px 1199px #FFF , 663px 1183px #FFF , 461px 387px #FFF , 129px 460px #FFF , 1805px 148px #FFF , 807px 1616px #FFF , 1580px 1254px #FFF , 1650px 805px #FFF , 1679px 1619px #FFF , 1190px 1648px #FFF , 917px 571px #FFF , 1991px 1570px #FFF , 59px 407px #FFF , 1811px 1926px #FFF , 1826px 1256px #FFF , 1072px 507px #FFF , 1180px 1033px #FFF , 510px 351px #FFF , 1646px 854px #FFF , 240px 1658px #FFF , 1826px 1704px #FFF , 1912px 445px #FFF , 1642px 1754px #FFF , 291px 580px #FFF , 1830px 817px #FFF , 1403px 959px #FFF , 636px 219px #FFF , 329px 923px #FFF , 1680px 1502px #FFF , 125px 1225px #FFF , 1005px 119px #FFF , 621px 1025px #FFF , 199px 219px #FFF , 1324px 1006px #FFF , 1964px 701px #FFF , 1125px 757px #FFF , 808px 1907px #FFF , 592px 1146px #FFF , 150px 1461px #FFF , 149px 835px #FFF , 155px 1216px #FFF , 356px 566px #FFF , 685px 1711px #FFF , 81px 324px #FFF , 1367px 1468px #FFF , 733px 1573px #FFF , 1891px 419px #FFF , 291px 1857px #FFF , 714px 1536px #FFF , 904px 190px #FFF , 507px 1968px #FFF , 1050px 389px #FFF , 995px 962px #FFF , 412px 207px #FFF , 1369px 907px #FFF , 1615px 1637px #FFF , 683px 1612px #FFF , 50px 727px #FFF , 367px 524px #FFF , 1323px 475px #FFF , 1983px 648px #FFF , 1442px 49px #FFF , 1310px 147px #FFF , 814px 1389px #FFF , 1299px 1660px #FFF , 1633px 277px #FFF , 617px 273px #FFF , 1382px 317px #FFF , 571px 710px #FFF , 1846px 259px #FFF , 1764px 1009px #FFF , 1431px 1780px #FFF , 93px 1807px #FFF , 1037px 252px #FFF , 1405px 719px #FFF , 1687px 1055px #FFF , 1397px 1944px #FFF , 159px 1718px #FFF , 1052px 1291px #FFF , 318px 1489px #FFF , 106px 1401px #FFF , 1755px 1876px #FFF , 1006px 280px #FFF , 1530px 1860px #FFF , 745px 875px #FFF , 1329px 1654px #FFF , 327px 1341px #FFF , 1371px 1677px #FFF , 735px 1378px #FFF , 126px 455px #FFF , 1889px 896px #FFF , 1884px 565px #FFF , 182px 168px #FFF , 1940px 1262px #FFF , 314px 583px #FFF , 1748px 1977px #FFF , 1482px 702px #FFF , 210px 1602px #FFF , 1412px 1598px #FFF , 821px 1131px #FFF , 1130px 1835px #FFF , 1778px 608px #FFF , 84px 184px #FFF , 1434px 998px #FFF , 1305px 385px #FFF , 758px 1128px #FFF , 661px 1223px #FFF , 84px 178px #FFF , 1376px 1604px #FFF , 1163px 1375px #FFF , 985px 1087px #FFF , 1854px 670px #FFF , 1593px 262px #FFF , 1510px 1974px #FFF , 1381px 711px #FFF , 1621px 1532px #FFF , 1876px 762px #FFF , 1160px 1469px #FFF , 77px 1379px #FFF , 415px 1259px #FFF , 1401px 50px #FFF , 1141px 336px #FFF , 759px 1948px #FFF , 316px 1466px #FFF , 372px 538px #FFF , 907px 1036px #FFF , 151px 1317px #FFF , 1695px 605px #FFF , 575px 1234px #FFF , 169px 793px #FFF , 835px 1068px #FFF , 1611px 1409px #FFF , 1180px 1194px #FFF , 510px 1674px #FFF , 1297px 221px #FFF , 1798px 1456px #FFF , 959px 478px #FFF , 1368px 802px #FFF , 1922px 1415px #FFF , 443px 341px #FFF , 1609px 1045px #FFF , 229px 139px #FFF , 1068px 119px #FFF , 1871px 400px #FFF , 973px 1906px #FFF , 901px 200px #FFF , 1979px 1837px #FFF , 1134px 441px #FFF , 518px 964px #FFF , 1781px 270px #FFF , 602px 1849px #FFF , 98px 1533px #FFF , 13px 1903px #FFF , 1421px 245px #FFF , 516px 1239px #FFF , 462px 1421px #FFF , 1540px 775px #FFF , 1417px 1107px #FFF , 569px 1655px #FFF , 1388px 799px #FFF , 1903px 741px #FFF , 781px 104px #FFF , 1091px 364px #FFF , 814px 1144px #FFF , 795px 1876px #FFF , 499px 860px #FFF , 1068px 634px #FFF , 135px 358px #FFF , 12px 895px #FFF , 630px 1944px #FFF , 415px 1972px #FFF , 1000px 1829px #FFF , 1668px 606px #FFF , 1014px 1601px #FFF , 1905px 243px #FFF , 1912px 1280px #FFF , 1871px 848px #FFF , 1859px 227px #FFF , 1164px 218px #FFF , 1656px 1195px #FFF , 1006px 526px #FFF , 836px 1883px #FFF , 389px 228px #FFF , 1933px 935px #FFF , 956px 878px #FFF , 1190px 879px #FFF , 1254px 497px #FFF , 545px 784px #FFF , 792px 1688px #FFF , 85px 659px #FFF , 1506px 612px #FFF , 914px 990px #FFF , 1686px 1951px #FFF , 951px 1532px #FFF , 438px 1869px #FFF , 973px 1124px #FFF , 1725px 1503px #FFF , 1036px 630px #FFF , 1655px 619px #FFF , 48px 1164px #FFF , 1940px 869px #FFF , 671px 1100px #FFF , 569px 1306px #FFF , 92px 1447px #FFF , 14px 1956px #FFF , 355px 1763px #FFF , 630px 1788px #FFF , 1732px 1733px #FFF , 633px 1807px #FFF , 1774px 1394px #FFF , 1356px 1176px #FFF , 417px 1440px #FFF , 1946px 1798px #FFF , 604px 341px #FFF , 1341px 7px #FFF , 1486px 1944px #FFF , 1787px 1161px #FFF , 383px 671px #FFF , 1181px 1032px #FFF , 1116px 356px #FFF , 1151px 1007px #FFF , 543px 273px #FFF , 1663px 1759px #FFF , 1281px 1525px #FFF , 1173px 1640px #FFF , 1569px 295px #FFF , 1211px 958px #FFF , 1401px 189px #FFF , 343px 784px #FFF , 512px 1339px #FFF , 1592px 536px #FFF , 1774px 421px #FFF , 500px 385px #FFF , 1569px 488px #FFF , 512px 1171px #FFF , 1127px 944px #FFF , 1203px 1061px #FFF , 99px 695px #FFF , 111px 176px #FFF , 1014px 1111px #FFF , 1955px 1594px #FFF , 1257px 1358px #FFF , 1735px 228px #FFF , 986px 1134px #FFF , 1391px 800px #FFF , 575px 1410px #FFF , 1700px 1357px #FFF , 1507px 810px #FFF , 296px 782px #FFF , 673px 1177px #FFF , 804px 1225px #FFF , 829px 804px #FFF , 1169px 595px #FFF , 1539px 987px #FFF , 180px 1747px #FFF , 1826px 1131px #FFF , 383px 1193px #FFF , 1728px 932px #FFF , 286px 1695px #FFF , 1046px 389px #FFF , 1262px 176px #FFF , 991px 60px #FFF , 766px 1554px #FFF , 387px 530px #FFF , 328px 697px #FFF , 1058px 699px #FFF , 1110px 1937px #FFF , 1103px 1803px #FFF , 1631px 1902px #FFF , 1579px 989px #FFF , 1140px 1666px #FFF , 692px 118px #FFF , 1268px 1836px #FFF , 1198px 148px #FFF , 1818px 982px #FFF , 1591px 791px #FFF , 1231px 1435px #FFF , 1039px 1533px #FFF , 1781px 1959px #FFF , 1845px 644px #FFF , 1319px 5px #FFF , 792px 1102px #FFF , 1885px 1435px #FFF , 910px 1191px #FFF , 497px 55px #FFF , 1260px 574px #FFF , 1212px 229px #FFF , 1571px 1763px #FFF , 1649px 1605px #FFF , 1529px 1418px #FFF , 949px 276px #FFF , 1158px 580px #FFF , 1018px 337px #FFF , 1317px 1690px #FFF , 1238px 1704px #FFF , 1784px 1168px #FFF , 1701px 185px #FFF , 1626px 1443px #FFF , 1285px 1159px #FFF , 1157px 246px #FFF , 411px 273px #FFF , 758px 940px #FFF , 1764px 488px #FFF , 218px 642px #FFF , 1529px 355px #FFF , 703px 794px #FFF , 454px 1934px #FFF , 1791px 173px #FFF , 1432px 104px #FFF , 708px 1827px #FFF , 1168px 838px #FFF , 678px 961px #FFF , 987px 1690px #FFF , 1392px 590px #FFF , 220px 289px #FFF , 50px 1230px #FFF , 35px 55px #FFF , 1993px 963px #FFF , 1259px 1686px #FFF , 952px 1541px #FFF , 1482px 461px #FFF , 186px 83px #FFF , 1843px 935px #FFF , 721px 1063px #FFF , 1450px 1252px #FFF , 224px 1403px #FFF , 1983px 1623px #FFF , 324px 115px #FFF , 1643px 1295px #FFF , 511px 504px #FFF , 809px 174px #FFF , 1212px 1263px #FFF , 643px 1196px #FFF , 958px 419px #FFF , 263px 1534px #FFF , 1763px 1644px #FFF , 1438px 1281px #FFF , 1504px 1746px #FFF , 1555px 1651px #FFF , 854px 483px #FFF , 539px 1755px #FFF , 551px 1030px #FFF , 844px 1091px #FFF , 1437px 720px #FFF , 358px 863px #FFF , 1150px 1399px #FFF , 42px 171px #FFF , 1364px 1748px #FFF , 1232px 1561px #FFF , 265px 1204px #FFF , 1969px 610px #FFF , 1052px 480px #FFF , 1619px 1303px #FFF , 91px 1994px #FFF , 461px 543px #FFF , 645px 11px #FFF , 1251px 504px #FFF , 1991px 1039px #FFF , 819px 1371px #FFF , 1395px 1921px #FFF , 454px 441px #FFF , 1678px 1434px #FFF , 955px 1372px #FFF , 552px 164px #FFF;
				}

				#stars2 {
				width: 2px;
				height: 2px;
				background: transparent;
				box-shadow: 81px 468px #FFF , 1472px 170px #FFF , 472px 384px #FFF , 1992px 1298px #FFF , 646px 1939px #FFF , 898px 948px #FFF , 1191px 129px #FFF , 1206px 1678px #FFF , 1302px 337px #FFF , 1836px 435px #FFF , 1517px 1596px #FFF , 1860px 837px #FFF , 1088px 1928px #FFF , 145px 1034px #FFF , 1855px 153px #FFF , 645px 1194px #FFF , 542px 1788px #FFF , 18px 1053px #FFF , 914px 1751px #FFF , 1864px 61px #FFF , 883px 1212px #FFF , 802px 984px #FFF , 1900px 522px #FFF , 227px 1724px #FFF , 222px 577px #FFF , 374px 1111px #FFF , 390px 1178px #FFF , 935px 568px #FFF , 1700px 189px #FFF , 725px 38px #FFF , 397px 928px #FFF , 1171px 1669px #FFF , 156px 1880px #FFF , 615px 1154px #FFF , 325px 1275px #FFF , 1870px 287px #FFF , 1988px 1243px #FFF , 1740px 1886px #FFF , 1076px 1872px #FFF , 1998px 395px #FFF , 154px 915px #FFF , 1183px 503px #FFF , 86px 360px #FFF , 1298px 53px #FFF , 876px 1981px #FFF , 1579px 1697px #FFF , 176px 1826px #FFF , 1956px 1911px #FFF , 384px 701px #FFF , 1147px 47px #FFF , 959px 1307px #FFF , 1724px 1406px #FFF , 81px 528px #FFF , 532px 337px #FFF , 1824px 126px #FFF , 1200px 1441px #FFF , 1963px 959px #FFF , 310px 568px #FFF , 1304px 1087px #FFF , 1836px 1182px #FFF , 979px 580px #FFF , 1968px 1428px #FFF , 1331px 635px #FFF , 433px 1344px #FFF , 1100px 1347px #FFF , 982px 1168px #FFF , 1763px 1526px #FFF , 1273px 256px #FFF , 835px 164px #FFF , 404px 1303px #FFF , 1011px 253px #FFF , 1538px 1790px #FFF , 215px 1010px #FFF , 382px 360px #FFF , 762px 1160px #FFF , 307px 1603px #FFF , 1763px 1546px #FFF , 380px 1270px #FFF , 1043px 1954px #FFF , 713px 1796px #FFF , 130px 530px #FFF , 1588px 340px #FFF , 1109px 312px #FFF , 1192px 593px #FFF , 921px 664px #FFF , 710px 1820px #FFF , 1836px 1497px #FFF , 1665px 1515px #FFF , 1086px 32px #FFF , 996px 460px #FFF , 1463px 342px #FFF , 53px 780px #FFF , 1956px 841px #FFF , 152px 1141px #FFF , 119px 492px #FFF , 727px 257px #FFF , 1772px 1344px #FFF , 543px 1155px #FFF , 156px 566px #FFF , 1522px 1421px #FFF , 1088px 1453px #FFF , 1431px 435px #FFF , 790px 1285px #FFF , 1486px 1821px #FFF , 959px 1179px #FFF , 815px 557px #FFF , 1375px 484px #FFF , 895px 403px #FFF , 580px 776px #FFF , 680px 792px #FFF , 936px 379px #FFF , 746px 1105px #FFF , 300px 1293px #FFF , 1315px 551px #FFF , 1435px 1038px #FFF , 676px 595px #FFF , 1784px 930px #FFF , 610px 113px #FFF , 1960px 694px #FFF , 463px 986px #FFF , 824px 1796px #FFF , 1731px 792px #FFF , 1653px 1620px #FFF , 1585px 373px #FFF , 80px 686px #FFF , 326px 792px #FFF , 80px 513px #FFF , 1333px 332px #FFF , 1135px 1349px #FFF , 1233px 52px #FFF , 522px 185px #FFF , 1510px 824px #FFF , 1080px 920px #FFF , 52px 1700px #FFF , 1344px 715px #FFF , 1663px 177px #FFF , 1848px 957px #FFF , 853px 1256px #FFF , 1210px 1392px #FFF , 1091px 512px #FFF , 1125px 1450px #FFF , 22px 894px #FFF , 691px 1493px #FFF , 1587px 1093px #FFF , 1407px 1576px #FFF , 1829px 1411px #FFF , 839px 247px #FFF , 1132px 1943px #FFF , 693px 746px #FFF , 1701px 469px #FFF , 1019px 445px #FFF , 671px 1867px #FFF , 1073px 1512px #FFF , 1820px 675px #FFF , 216px 1796px #FFF , 322px 279px #FFF , 1606px 41px #FFF , 1210px 1684px #FFF , 508px 128px #FFF , 734px 1017px #FFF , 436px 334px #FFF , 1757px 3px #FFF , 346px 1670px #FFF , 1725px 1643px #FFF , 599px 256px #FFF , 1791px 1023px #FFF , 27px 1475px #FFF , 966px 214px #FFF , 247px 600px #FFF , 560px 585px #FFF , 472px 713px #FFF , 835px 1559px #FFF , 397px 1871px #FFF , 1486px 1289px #FFF , 1996px 1857px #FFF , 694px 11px #FFF , 528px 1306px #FFF , 1962px 564px #FFF , 1326px 430px #FFF , 1266px 1290px #FFF , 654px 272px #FFF , 79px 1463px #FFF , 60px 1778px #FFF , 113px 105px #FFF , 1215px 1154px #FFF , 1914px 848px #FFF , 823px 1272px #FFF , 51px 1033px #FFF , 505px 1221px #FFF , 1162px 1524px #FFF , 1191px 1065px #FFF , 187px 769px #FFF , 278px 408px #FFF , 1479px 38px #FFF , 461px 852px #FFF , 1554px 79px #FFF , 10px 415px #FFF , 582px 919px #FFF , 1732px 1840px #FFF , 497px 14px #FFF;
				animation: animStar 100s linear infinite;
				}
				#stars2:after {
				content: " ";
				position: absolute;
				top: 2000px;
				width: 2px;
				height: 2px;
				background: transparent;
				box-shadow: 81px 468px #FFF , 1472px 170px #FFF , 472px 384px #FFF , 1992px 1298px #FFF , 646px 1939px #FFF , 898px 948px #FFF , 1191px 129px #FFF , 1206px 1678px #FFF , 1302px 337px #FFF , 1836px 435px #FFF , 1517px 1596px #FFF , 1860px 837px #FFF , 1088px 1928px #FFF , 145px 1034px #FFF , 1855px 153px #FFF , 645px 1194px #FFF , 542px 1788px #FFF , 18px 1053px #FFF , 914px 1751px #FFF , 1864px 61px #FFF , 883px 1212px #FFF , 802px 984px #FFF , 1900px 522px #FFF , 227px 1724px #FFF , 222px 577px #FFF , 374px 1111px #FFF , 390px 1178px #FFF , 935px 568px #FFF , 1700px 189px #FFF , 725px 38px #FFF , 397px 928px #FFF , 1171px 1669px #FFF , 156px 1880px #FFF , 615px 1154px #FFF , 325px 1275px #FFF , 1870px 287px #FFF , 1988px 1243px #FFF , 1740px 1886px #FFF , 1076px 1872px #FFF , 1998px 395px #FFF , 154px 915px #FFF , 1183px 503px #FFF , 86px 360px #FFF , 1298px 53px #FFF , 876px 1981px #FFF , 1579px 1697px #FFF , 176px 1826px #FFF , 1956px 1911px #FFF , 384px 701px #FFF , 1147px 47px #FFF , 959px 1307px #FFF , 1724px 1406px #FFF , 81px 528px #FFF , 532px 337px #FFF , 1824px 126px #FFF , 1200px 1441px #FFF , 1963px 959px #FFF , 310px 568px #FFF , 1304px 1087px #FFF , 1836px 1182px #FFF , 979px 580px #FFF , 1968px 1428px #FFF , 1331px 635px #FFF , 433px 1344px #FFF , 1100px 1347px #FFF , 982px 1168px #FFF , 1763px 1526px #FFF , 1273px 256px #FFF , 835px 164px #FFF , 404px 1303px #FFF , 1011px 253px #FFF , 1538px 1790px #FFF , 215px 1010px #FFF , 382px 360px #FFF , 762px 1160px #FFF , 307px 1603px #FFF , 1763px 1546px #FFF , 380px 1270px #FFF , 1043px 1954px #FFF , 713px 1796px #FFF , 130px 530px #FFF , 1588px 340px #FFF , 1109px 312px #FFF , 1192px 593px #FFF , 921px 664px #FFF , 710px 1820px #FFF , 1836px 1497px #FFF , 1665px 1515px #FFF , 1086px 32px #FFF , 996px 460px #FFF , 1463px 342px #FFF , 53px 780px #FFF , 1956px 841px #FFF , 152px 1141px #FFF , 119px 492px #FFF , 727px 257px #FFF , 1772px 1344px #FFF , 543px 1155px #FFF , 156px 566px #FFF , 1522px 1421px #FFF , 1088px 1453px #FFF , 1431px 435px #FFF , 790px 1285px #FFF , 1486px 1821px #FFF , 959px 1179px #FFF , 815px 557px #FFF , 1375px 484px #FFF , 895px 403px #FFF , 580px 776px #FFF , 680px 792px #FFF , 936px 379px #FFF , 746px 1105px #FFF , 300px 1293px #FFF , 1315px 551px #FFF , 1435px 1038px #FFF , 676px 595px #FFF , 1784px 930px #FFF , 610px 113px #FFF , 1960px 694px #FFF , 463px 986px #FFF , 824px 1796px #FFF , 1731px 792px #FFF , 1653px 1620px #FFF , 1585px 373px #FFF , 80px 686px #FFF , 326px 792px #FFF , 80px 513px #FFF , 1333px 332px #FFF , 1135px 1349px #FFF , 1233px 52px #FFF , 522px 185px #FFF , 1510px 824px #FFF , 1080px 920px #FFF , 52px 1700px #FFF , 1344px 715px #FFF , 1663px 177px #FFF , 1848px 957px #FFF , 853px 1256px #FFF , 1210px 1392px #FFF , 1091px 512px #FFF , 1125px 1450px #FFF , 22px 894px #FFF , 691px 1493px #FFF , 1587px 1093px #FFF , 1407px 1576px #FFF , 1829px 1411px #FFF , 839px 247px #FFF , 1132px 1943px #FFF , 693px 746px #FFF , 1701px 469px #FFF , 1019px 445px #FFF , 671px 1867px #FFF , 1073px 1512px #FFF , 1820px 675px #FFF , 216px 1796px #FFF , 322px 279px #FFF , 1606px 41px #FFF , 1210px 1684px #FFF , 508px 128px #FFF , 734px 1017px #FFF , 436px 334px #FFF , 1757px 3px #FFF , 346px 1670px #FFF , 1725px 1643px #FFF , 599px 256px #FFF , 1791px 1023px #FFF , 27px 1475px #FFF , 966px 214px #FFF , 247px 600px #FFF , 560px 585px #FFF , 472px 713px #FFF , 835px 1559px #FFF , 397px 1871px #FFF , 1486px 1289px #FFF , 1996px 1857px #FFF , 694px 11px #FFF , 528px 1306px #FFF , 1962px 564px #FFF , 1326px 430px #FFF , 1266px 1290px #FFF , 654px 272px #FFF , 79px 1463px #FFF , 60px 1778px #FFF , 113px 105px #FFF , 1215px 1154px #FFF , 1914px 848px #FFF , 823px 1272px #FFF , 51px 1033px #FFF , 505px 1221px #FFF , 1162px 1524px #FFF , 1191px 1065px #FFF , 187px 769px #FFF , 278px 408px #FFF , 1479px 38px #FFF , 461px 852px #FFF , 1554px 79px #FFF , 10px 415px #FFF , 582px 919px #FFF , 1732px 1840px #FFF , 497px 14px #FFF;
				}

				#stars3 {
				width: 3px;
				height: 3px;
				background: transparent;
				box-shadow: 1679px 1232px #FFF , 1701px 409px #FFF , 463px 1886px #FFF , 1040px 1525px #FFF , 600px 1113px #FFF , 898px 775px #FFF , 1586px 240px #FFF , 1274px 1268px #FFF , 852px 747px #FFF , 1806px 99px #FFF , 1027px 1981px #FFF , 255px 386px #FFF , 318px 1455px #FFF , 1800px 646px #FFF , 375px 1782px #FFF , 1915px 1864px #FFF , 1733px 1987px #FFF , 491px 248px #FFF , 675px 119px #FFF , 1352px 708px #FFF , 231px 839px #FFF , 920px 571px #FFF , 1526px 555px #FFF , 454px 382px #FFF , 1849px 1709px #FFF , 54px 1333px #FFF , 1156px 1627px #FFF , 597px 1504px #FFF , 1489px 769px #FFF , 1252px 1397px #FFF , 41px 562px #FFF , 1195px 635px #FFF , 328px 1839px #FFF , 791px 1668px #FFF , 1225px 59px #FFF , 1618px 1486px #FFF , 950px 464px #FFF , 471px 170px #FFF , 1074px 1838px #FFF , 251px 1046px #FFF , 1204px 909px #FFF , 1208px 1981px #FFF , 283px 394px #FFF , 313px 1889px #FFF , 1984px 1642px #FFF , 1005px 480px #FFF , 650px 904px #FFF , 687px 1084px #FFF , 732px 1250px #FFF , 567px 1567px #FFF , 1130px 81px #FFF , 1801px 55px #FFF , 123px 1652px #FFF , 831px 555px #FFF , 237px 1241px #FFF , 1409px 504px #FFF , 866px 996px #FFF , 305px 169px #FFF , 180px 1306px #FFF , 171px 879px #FFF , 1874px 570px #FFF , 930px 1972px #FFF , 1743px 1285px #FFF , 1873px 989px #FFF , 1535px 57px #FFF , 1807px 1926px #FFF , 1458px 1205px #FFF , 242px 354px #FFF , 297px 1481px #FFF , 878px 568px #FFF , 520px 1816px #FFF , 1108px 1001px #FFF , 1501px 1476px #FFF , 669px 744px #FFF , 1016px 460px #FFF , 697px 1608px #FFF , 1693px 1293px #FFF , 1638px 733px #FFF , 942px 916px #FFF , 1472px 1695px #FFF , 933px 501px #FFF , 1131px 509px #FFF , 930px 1035px #FFF , 230px 778px #FFF , 955px 1875px #FFF , 65px 1923px #FFF , 601px 1957px #FFF , 1687px 189px #FFF , 1938px 59px #FFF , 477px 1513px #FFF , 1313px 1350px #FFF , 1556px 1394px #FFF , 706px 1039px #FFF , 1410px 695px #FFF , 1054px 1444px #FFF , 1108px 1337px #FFF , 1610px 1137px #FFF , 95px 1986px #FFF , 700px 1512px #FFF , 1604px 454px #FFF;
				animation: animStar 150s linear infinite;
				}
				#stars3:after {
				content: " ";
				position: absolute;
				top: 2000px;
				width: 3px;
				height: 3px;
				background: transparent;
				box-shadow: 1679px 1232px #FFF , 1701px 409px #FFF , 463px 1886px #FFF , 1040px 1525px #FFF , 600px 1113px #FFF , 898px 775px #FFF , 1586px 240px #FFF , 1274px 1268px #FFF , 852px 747px #FFF , 1806px 99px #FFF , 1027px 1981px #FFF , 255px 386px #FFF , 318px 1455px #FFF , 1800px 646px #FFF , 375px 1782px #FFF , 1915px 1864px #FFF , 1733px 1987px #FFF , 491px 248px #FFF , 675px 119px #FFF , 1352px 708px #FFF , 231px 839px #FFF , 920px 571px #FFF , 1526px 555px #FFF , 454px 382px #FFF , 1849px 1709px #FFF , 54px 1333px #FFF , 1156px 1627px #FFF , 597px 1504px #FFF , 1489px 769px #FFF , 1252px 1397px #FFF , 41px 562px #FFF , 1195px 635px #FFF , 328px 1839px #FFF , 791px 1668px #FFF , 1225px 59px #FFF , 1618px 1486px #FFF , 950px 464px #FFF , 471px 170px #FFF , 1074px 1838px #FFF , 251px 1046px #FFF , 1204px 909px #FFF , 1208px 1981px #FFF , 283px 394px #FFF , 313px 1889px #FFF , 1984px 1642px #FFF , 1005px 480px #FFF , 650px 904px #FFF , 687px 1084px #FFF , 732px 1250px #FFF , 567px 1567px #FFF , 1130px 81px #FFF , 1801px 55px #FFF , 123px 1652px #FFF , 831px 555px #FFF , 237px 1241px #FFF , 1409px 504px #FFF , 866px 996px #FFF , 305px 169px #FFF , 180px 1306px #FFF , 171px 879px #FFF , 1874px 570px #FFF , 930px 1972px #FFF , 1743px 1285px #FFF , 1873px 989px #FFF , 1535px 57px #FFF , 1807px 1926px #FFF , 1458px 1205px #FFF , 242px 354px #FFF , 297px 1481px #FFF , 878px 568px #FFF , 520px 1816px #FFF , 1108px 1001px #FFF , 1501px 1476px #FFF , 669px 744px #FFF , 1016px 460px #FFF , 697px 1608px #FFF , 1693px 1293px #FFF , 1638px 733px #FFF , 942px 916px #FFF , 1472px 1695px #FFF , 933px 501px #FFF , 1131px 509px #FFF , 930px 1035px #FFF , 230px 778px #FFF , 955px 1875px #FFF , 65px 1923px #FFF , 601px 1957px #FFF , 1687px 189px #FFF , 1938px 59px #FFF , 477px 1513px #FFF , 1313px 1350px #FFF , 1556px 1394px #FFF , 706px 1039px #FFF , 1410px 695px #FFF , 1054px 1444px #FFF , 1108px 1337px #FFF , 1610px 1137px #FFF , 95px 1986px #FFF , 700px 1512px #FFF , 1604px 454px #FFF;
				}

				#title {
				position: absolute;
				top: 50%;
				left: 0;
				right: 0;
				color: #FFF;
				text-align: center;
				font-family: "lato", sans-serif;
				font-weight: 300;
				font-size: 50px;
				letter-spacing: 10px;
				margin-top: -60px;
				padding-left: 10px;
				}
				#title span {
				background: -webkit-linear-gradient(white, #38495a);
				-webkit-background-clip: text;
				-webkit-text-fill-color: transparent;
				}

				@keyframes animStar {
				from {
					transform: translateY(0px);
				}
				to {
					transform: translateY(-2000px);
				}
				}



        h1{
          margin-top: 100px;
		  color: rgb(78, 161, 235);
        }
        container {
				  margin:auto;
				  text-align: center;
			  }

        table{
          background-color: rgba(0, 0, 0, 0.644);
          margin: auto;
          padding: 15px 15px;
          
        }
        tr{
          transition: transform .2s;
		  color: rgb(165, 160, 160);
        }

        tr:hover {
          transform: scale(1.05);
          background-color: rgba(40, 40, 40, 0.88);
          box-shadow: 0px 0px 15px rgb(83, 70, 53)
        }

        td{
          text-indent: 13px;
        }

        th{
          font-size: 17px;
          text-align: left;
          padding: 0px 12px;
        }

        button{
				border: none;
				outline: 0;
				padding: 8px;
				color: white;
				background-color: #000;
				text-align: center;
				cursor: pointer;
				width: 150px;
				font-size: 18px;
				transition: transform .2s;
				font-family: arial;

        margin-left: auto;
        margin-right: auto;

				}
			button:hover, a:hover, button2:hover {
				opacity: 0.7;
				transform: scale(1.1);
			}
      inv{
				position:relative;
			}
      form {
        text-align: center;
      }


		</style>
	</head>
<body>

  <div class = "inv">
    <div id='stars'></div>
    <div id='stars2'></div>
    <div id='stars3'></div>
  </div>


  <div id="container"> 
    <center><h1>Directory Contents</h1></center><br><br>

    <table class="table">
      <thead>
        <tr>
          <th>Filename</th>
          <th>Type</th>
          <th>Size <small>(kilobytes)</small></th>
		      <th>Date Created</th>
          <th>Date Modified</th>
        </tr>
      </thead>
      <tbody>\n'''

		for i in range(len(self.file_name)):
			content += f'''<tr class="aclass">
            <td><a href="{self.file_path[i]}" download="{self.file_name[i]}.{self.file_type[i]}" >{self.file_name[i]}</a></td>
            <td><a>{self.file_type[i]}</a></td>
            <td><a>{self.file_size[i]}</a></td>
            <td><a>{self.file_ctime[i]}</a></td>
			<td><a>{self.file_mtime[i]}</a></td>
		  </tr>\n'''%()

		
		content += '''</tbody></table>
    
  </div><br><br><br><br><br><br>
  <form action="/info.html" method="POST">
    <button type="submit">Back</button>
    </form>
</body>'''

		return content