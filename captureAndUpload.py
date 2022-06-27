from operator import truediv
from tracemalloc import take_snapshot
import cv2
import time
import dropbox
start_time = time.time()

def capture_snapshot():
    currentTime = str(time.time())
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img_"+currentTime+".jpg"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    print("snapshot taken successfully")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

def upload_snapshot(img_name):
    access_token = "sl.BGXs69WoGBfCE3b4Ee0F-a14jiYAprSyKw9j6tcTZMLEGfgXvBKsJ5fB_vg8A-qOOH8NQg0Vcn7VI75arArlrsQh1fpeMwKBtNYMTcCrHR0ac7nKObJxvh-qHPVWoWnJZBDD5_GFV6g"
    file = img_name
    file_from = file
    file_to = '/Exoticc/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read, file_to, mode=dropbox.files.WriteMode.overwrite)
        print("upload has been successful")

def main():
    while(True):
        if((time.time()-start_time) >= 300):
            name = take_snapshot()
            upload_snapshot(name)

main()
