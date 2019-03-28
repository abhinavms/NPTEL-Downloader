# Sample Download Link --> https://nptel.ac.in/courses/nptel_download.php?subjectid=106106198

from main import nptel as nptel
import os

# Creating a directory to save the files
os.mkdir("Downloads")
os.chdir("./Downloads")

url = input("Enter URL of the download page - ")
Stream = nptel(url)

# Setting up parameters
ch = 0
while (ch != 3):
   
    # User Menu
    print ("\nWelcome")
    print ("\nMENU")
    print ("1. Download All Files")
    print ("2. Download A Module")
    print ("3. Exit")
    ch = int(input("Enter the choice - "))
    
    if (ch == 1):
        format_ch = 0
        while (format_ch != -1):
            
            print ("\nAvailable format are :")
            print ("1. MP4\n2. FLV\n3. 3GP\n4. MP3\n5. PDF")
            format_ch = int(input("Enter the choice - "))

            if (format_ch == 1):
               format = 'mp4'
            elif (format_ch == 2):
               format = 'flv'
            elif (format_ch == 3):
               format = '3gp'
            elif (format_ch == 4):
               format = 'mp3'
            elif (format_ch == 5):
               format = 'English'
            else:
                print ("Wrong input !!!!")
                format_ch = -1

            Links = Stream.getLinks(format)
            
            count = 1
            if (format == 'English'): 
                for url in Links:
                    print('\nDownloading PDF ',count)
                    nptel.download(url , str(count)+'.'+'pdf')
                    count = count + 1
            else:
                for url in Links:
                    print('\nDownloading ',Links[0].split('=')[3])
                    nptel.download('https://nptel.ac.in/'+ url , str(count)+"."+Links[0].split('=')[3]+'.'+format)
                    count = count + 1

            print ("\nDownload Complete :)\n")
    
    elif (ch == 2):

        # Module To be downloaded
        no = int(input("Enter the Module Number - "))
    
        # Format of the content
        format_ch = 0
        while (format_ch != -1):

            print ("Available format are :\n")
            print ("1. MP4\n2. FLV\n3. 3GP\n4. MP3")
            format_ch = int(input("Enter the choice - "))

            # ["%02d"%(no) - is used to format the module no]
            if (format_ch == 1):
               format = 'mp4'
            elif (format_ch == 2):
               format = 'flv'
            elif (format_ch == 3):
               format = '3gp'
            elif (format_ch == 4):
               format = 'mp3'
            else:
                format_ch = -1
                print ("Wrong input !!!!")
            
            Links = Stream.getLinks(format,'mod'+"%02d"%(no))
            
            count = 1
            for url in Links:
                print('Downloading ',Links[0].split('=')[3])
                nptel.download('https://nptel.ac.in/'+ url , str(count)+"."+Links[0].split('=')[3]+'.'+format)
                count = count + 1

    elif (ch ==3):
        print ("\nHave a nice day :)")
    else:
        print ("\nInvalid Choice !!!!!")