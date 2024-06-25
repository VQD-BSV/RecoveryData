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
   print("""\n#Scan #Scan_Image #Get_Image""")

   key = input("==> ")

   # Get key & save
   if key == "Get_Image":
      disk = r'\\.\{}:'.format(part) # disk
      out_file = f"Part_{part}.img"  # out

      # read & write
      with open(disk, 'rb') as disk:
          with open(out_file, 'wb') as w:
              while True:
                  byte = disk.read(1048576) #1MB
                  if not byte:
                      break  # Exit loop
                  # Write byte
                  w.write(byte)

#============main===========
from Disk.get_disk import get_drive_info
import platform, os


while True:
   # Run form 
   sreen()
   info_part = get_disk_info()
#===================================
   # select part
   sel_part = input("\n==> ")

   if sel_part == "x":
      break
#===================================
   if int(sel_part) != 0:
      sreen()

      # part sel
      info_part = info_part.splitlines()
      info_part = info_part[int(sel_part) - 1]

      # key 4 & key 7
      print(info_part[4:])
      tool(info_part[7])


