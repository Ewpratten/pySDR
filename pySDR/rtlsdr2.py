from rtlsdr import RtlSdr
import matplotlib
matplotlib.use("agg")

from matplotlib.pyplot import psd

class RTLsdr(object):
	def __init__(self, rate, freq, correction, gain):
		
		# Set up sdr
		self.sample_rate     = rate
		self.center_freq     = freq
		self.freq_correction = correction
		self.gain            = gain
	
	def loadDevice(self):
		try:
			self.radio = RtlSdr()
			
			self.radio.sample_rate     = self.sample_rate
			self.radio.center_freq     = self.center_freq
			self.radio.freq_correction = self.freq_correction
			self.radio.gain            = self.gain
			return True
		except:
			return False
	
	def read(self,width:int):
		return self.radio.read_samples(width).tolist()
	
	def readPSD(self,width:int):
		samples = self.read(width)
		return psd(samples, NFFT=1024, Fs=self.radio.sample_rate/1e6, Fc=self.radio.center_freq/1e6, return_line=True)
		# matplotlib.pyplot.savefig("./scan.png")