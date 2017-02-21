
import csv
import urllib.parse
import re

### REGEX to find URL
isitaurl = re.compile(r'(hxxp|hxxps://)') 


######################## MAIN FUNCTIONA RETURN ETP IMPORTED INFO AS DICTIONARY #############################################
## Alert ID(0),Message ID(1),Date & Time(2),From(3),Recipients(4),Subject(5),Malware Type(6),Malware File Type(7),Malware Name(8),
## Malware MD5(9),Malware Analysis Application(10),Malware Analysis OS(11),Virus Total(12),Source IP(13),Source Country(14),
## Malware Comunication IP(15),Malware Communication Countries(16),Email Status(17),Threat Type(18),Risk Level(19)
############################################################################################################################

def readETP(etpfile):
	file = etpfile
	etpalerts = {}
	info = []
	
	try: 
		with open(file, 'r') as f:
			reader = csv.reader(f)
			
			for line in reader:
				if not line:
					continue
				elif line[7] in ['doc','exe','zip','jar','htm','7zip','com','pdf','docx','xls','xlsx','js','vbs','ace','rar', 'bz2','bz','docm'] or line[6] == 'Attachment':
					info = { 'Time' : line[2],  'From' : line[3],  'Recipients' : line[4],  'Subject' : line[5], 'Type' : line[7] ,  'Name' : line[8] ,  'MD5' : line[9] ,  'evilips' : line[15] }
				elif line[6] == 'URL':
					url = urllib.parse.urlparse(line[8], scheme='hxxp|hxxps')
					## url[1] contains domain / url[2] contains url path. The path is sent to database in the evilips field to maintain consistency of the dictionary array
					info = { 'Time' : line[2],  'From' : line[3],  'Recipients' : line[4], 'Subject' : line[5],  'Type' : 'url' ,  'Name' : url[1] ,  'MD5' : 'N/A' ,  'evilips' : url[2] }
				elif line[6] == 'Header':
					continue
					# Not sure what this is but it's causing Fauda!
				elif re.match(isitaurl, line[8]):
					# This will catch lines with no TYPE = URL (Hopefully)
					url = urllib.parse.urlparse(line[8], scheme='hxxp|hxxps')
					info = { 'Time' : line[2],  'From' : line[3],  'Recipients' : line[4], 'Subject' : line[5],  'Type' : 'url' ,  'Name' : url[1] ,  'MD5' : 'N/A' ,  'evilips' : url[2] }
				else:
					print ("Found a line I can't digest!! . >.<  I'm just going to drop it like it's hot!! \n")
					print ("Remove this line and try again. Alert ID: ", line[0])
					print ("Name: ",line[8])
					print ("Type: ",line[6])
					print ("MD5: ", line[9])
					print ("Subject: ", line[5])
					break	
					
				etpalerts.update({line[0] : info})
	except Exception as e: print ("Can't open ETP alerts file\n", e)
	
	f.close()
	return (etpalerts)

if __name__ == '__main__':
	etpfile = 'alerts2'
	readETP(etpfile)
	
