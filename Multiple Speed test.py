import speedtest
import matplotlib.pyplot as plt
import time
list_download_speed=[]
list_upload_speed=[]

for i in range(5):
    print('hello')
    st=speedtest.Speedtest()
    speed_download=round(st.download()/1000000,2)
    list_download_speed.append(str(speed_download))
    
    speed_upload=round(st.upload()/1000000,2)
    list_upload_speed.append(str(speed_upload))
    time.sleep(60)
    print(list_download_speed)    
    print(list_upload_speed)
    
x=[1,2,3,4,5]
plt.plot(x,list_download_speed,Label="Download Speed")
plt.plot(x,list_upload_speed,Label="Upload Speed")
plt.title("Multple Speedtest")
plt.legend()
plt.show()