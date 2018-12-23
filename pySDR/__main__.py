import rtlsdr2 as sdr
import access as access
from graphics import display as disp


freq = 162500000
gain = 4

print("Constructing sdr classes")
radio = sdr.RTLsdr(2.4e6,freq,60,gain)
disp.setParams(freq)

print("Finding SDR")
sdrs = access.findSDR(access.getDevices())
print(f"Found {len(sdrs)} devices")

# If not 0666 mode, do chmod
if not radio.loadDevice():
	access.getAccess(sdrs)
	radio.loadDevice()

data = radio.read(256*1024)
arr,freq,line = radio.readPSD(256*1024)
print(line)

# # run
# while True:
# 	arr,freq = radio.readPSD(256*1024)
# 	for i,c in enumerate(arr):
# 		disp.plot(freq[i.real],c.real)

# 	disp.clear()