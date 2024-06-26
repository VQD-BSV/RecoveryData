def sreen():
   if platform.system() == "Windows":
       os.system("cls")

   with open("sreen.txt", "r") as r:
      print(r.read())

def get_disk_info():
   # get disk info
   drive_info = get_drive_info()

   count = 0
   info_part = ""
   for drive, info in drive_info.items():
      count += 1
      if f"{info['total_gb']}" == "Unknown":
         info_part += f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']} GB\n"
      else:
         info_part += f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']:.2f} GB\n"

   # out ket qua
   return info_part

def tool(part):
   print("""\n#Scan #Get_Image""")

   key = input("\n==> ")

   # Get key & save image
   if key == "Get_Image":
      disk = r'\\.\{}:'.format(part) # read disk
      out_file = f"Part_{part}.img"  # out file

      # read & write
      with open(disk, 'rb') as disk:
          with open(out_file, 'wb') as w:
              while True:
                  byte = disk.read(1048576) #1 MB
                  if not byte:
                      break  # Exit loop
                  # Write byte
                  w.write(byte)
                  
#============main===========
from Disk.get_disk import get_drive_info
from Scan.scan_image import scan_image
import platform, os, time


while True:
   # Run form 
   sreen()
   info_part = get_disk_info()
   print("\n#Scan_Image")
#===================================
   #Select Part
   sel_part = input("\n==> ")

   # Exit
   if sel_part == "x":
      break
#===================================
   #Scan_Image
   if sel_part == "Scan_Image":
      sreen()
      image = input("Enter File Path: ")
      
      sreen()
      print(f"=> {image}")
      scan_image(image)
   #===================================
   # Check Select Part
   elif int(sel_part) != 0:
      sreen()

      # get line
      info_part = info_part.splitlines()
      info_part = info_part[int(sel_part) - 1]

      # key 4 & key 7
      print(info_part[4:])
      tool(info_part[7])


