import startupURLs
import pageReader
import Constants

for link in startupURLs.getStartups():
    pageReader.SlideCapture(link);

print(f'All Slide Capture successful. Total Execution time is {Constants.totalTime}')