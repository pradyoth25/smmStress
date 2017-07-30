import pandas as pd
 
stressData1 = pd.read_csv('results_stressed.csv')
stressData2 = pd.read_csv('results_stressed05-22.csv')
stressData3 = pd.read_csv('results_stressed0517.csv')
stressData4 = pd.read_csv('results_stressed0518.csv')
stressData5 = pd.read_csv('results-stressedFriday.csv')
stressData6 = pd.read_csv('results-stressedFriday14.csv')
stressData7 = pd.read_csv('results-stressedSunday03.csv')
stressData8 = pd.read_csv('results-stressedThursday-morning.csv')
stressData9 = pd.read_csv('results-stressedTuesday.csv')
stressData10 = pd.read_csv('results-stressedTuesday04.csv')
stressData11 = pd.read_csv('results-stressedWednesday00.csv')
stressData12 = pd.read_csv('results-stressedWednesday16.csv')
frames = [stressData1, stressData2, stressData3, stressData4, stressData5, stressData6, stressData7, stressData8, stressData9, stressData10, stressData11, stressData12]
fullStress = pd.concat(frames)
fullStress.to_csv('fullStress.csv', sep = ',')
