import win32ui
import win32gui
import win32con
import win32api
import cStringIO
import Image
import os
tempDirectory = os.getenv("temp")
ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)

dst = cStringIO.StringIO()

large, small = win32gui.ExtractIconEx(path,0)
win32gui.DestroyIcon(small[0])

#creating a destination memory DC
hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
hbmp = win32ui.CreateBitmap()
hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
hdc = hdc.CreateCompatibleDC()

hdc.SelectObject( hbmp )

#draw a icon in it
hdc.DrawIcon( (0,0), large[0] )
win32gui.DestroyIcon(large[0])

#convert picture
hbmp.SaveBitmapFile( hdc, tempDirectory + "\Icontemp.bmp")

im = Image.open(tempDirectory + "\Icontemp.bmp")
im.save(dst, "JPEG")

dst.seek(0)