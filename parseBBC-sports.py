'''
Created on Jun 16, 2014
Modified on Jun 23, 2014
Version 0.12.d
@author: rainier.madruga@gmail.com
A simple Python Program to scrape the BBC Sports website for content.
'''
# Import Libraries needed for Scraping the various web pages
from bs4 import BeautifulSoup
import csv
import urllib2
import datetime

''' ======================================================================== ***
URLs for use in testing the parsing of the World Cup & results:
	France vs Honduras - http://www.bbc.com/sport/0/football/25285092
	Switzerland vs Ecuador - http://www.bbc.com/sport/0/football/25285085
	Full World Cup Results - http://www.bbc.com/sport/football/world-cup/results
	Upcoming Fixtures - http://www.bbc.com/sport/football/fixtures
*** ======================================================================== '''

''' ======================================================================== ***
    TO-DO ITEMS
    Add in CSV Writer to Parse out the Update File (Identifies when / if Page was updated)
    Output Game Date in CSV Details 
    Output Match Results Link to CSV Details
*** ======================================================================== '''

# Create an array of URL Links.
website = ["http://www.bbc.com/sport/0/football/25285092", "http://www.bbc.com/sport/0/football/25285085", "http://www.bbc.com/sport/football/world-cup/results", "http://www.bbc.com/sport/football/fixtures"]

# Open World Cup Results 
gameWeb = urllib2.urlopen(website[2])
gameSoup = BeautifulSoup(gameWeb)
parseVersion = 'WorldCup v0.12.d'

# Output All Results Page to a local HTML file
outputTxt = 'WorldCup-Base.html'
with open(outputTxt, "w") as f:
	 f.write(gameSoup.prettify("utf-8"))
	 f.close()

# Establish the process Date & Time Stamp
ts = datetime.datetime.now().strftime("%H:%M:%S")
ds = datetime.datetime.now().strftime("%Y-%m-%d")

# Output Time & Date Stamp as well as Script Version
print ds + ' | ' + ts
with open('WorldCup-Update.txt', "a") as f:
		f.write(ds + '|' + ts + '|' + parseVersion + '|' + gameSoup.title.get_text() + '\n')
		f.close()

# Find the Main Results Table and Output the Results
divResults = gameSoup.find("div", {"class":"league-table table-narrow mod"})
'''
with open('WorldCup-Results.html', "w") as f:
	f.write(divResults.prettify())
	f.close()
'''

# Initialize Results Output File
with open('MatchRestuls-output.txt', "w") as f:
	f.write(ds + '|' + ts + '|' + parseVersion + '|' + gameSoup.title.get_text() + '\n')
	f.close()

divMatchResults = gameSoup.find_all("div", {"class":"fixtures-table full-table-medium"})
# print divMatchResults
for i in divMatchResults:
	# Create slices for output of results
	resultsHomeTeam = i.find_all("span", {"class":"team-home teams"})
	resultsAwayTeam = i.find_all("span", {"class":"team-away teams"})
	resultsPaddedScore = i.find_all("span", {"class":"score"})
	resultsGameDay = i.find_all("h2", {"class":"table-header"})
	urlList = i.find_all('a', {'class': 'report'})
	
	x = len(resultsHomeTeam)
	z = 0

	# Iterate over the Match Results
	while z < x:
		resultHomeTeam = resultsHomeTeam[z].get_text(strip=True)
		resultAwayTeam = resultsAwayTeam[z].get_text(strip=True)
		resultScore = resultsPaddedScore[z].get_text(strip=True)
		
		# Full URL for BBC Site
		stringURL = urlList[z].get("href")
		href = "http://www.bbc.com" + stringURL
		
		# Create output file and generate Results CSV
		resultOutput = open('MatchRestuls-output.txt', "a")
		resultMatchOutput = [ds, ts, resultHomeTeam, resultScore[0], resultAwayTeam, resultScore[2], href]
		writer = csv.writer(resultOutput, delimiter='|')
		writer.writerow(resultMatchOutput)
		z += 1
	
	# Output the HTML to a local file
	# with open('WorlCup-MatchResults.html', "w") as f:
	# 	f.write(i.prettify())
	#	f.close()

# Update Date for Matches
divUpdateDate = gameSoup.find_all("h2", {"class":"table-header"})
# for i in divUpdateDate:
# 	print i.get_text(strip=True)

# Posts when Matches were last updated on Page
# tableGameResults = divMatchResults.find_all("table", {"class":"table-stats"})

# Output Match Results to a File
'''divMatchDetails = gameSoup.find_all("td", {"class":"match-details"})
for i in divMatchDetails:
	with open('WorldCup-MatchDetails.html', "a") as f:
		f.write(i.prettify())
		f.close()

# Initialize the MatchDetails-output.txt File for appending the Game Scores
with open('MatchDetails-output.txt', "w") as f:
	f.write(ds + " " + ts + '\n')
	f.close()
'''
'''
for i in divMatchDetails:
	# Parse out Home Team and Score
	divHomeTeam = i.find("span", {"class":"team-home teams"})
	divAwayTeam = i.find("span", {"class":"team-away teams"})
	divPaddedScore = i.find("span", {"class":"score"})
	divScore = divPaddedScore.get_text(strip=True)
	
	# Open the file
	csvFile = open('MatchDetails-output.txt', "a")
	
	# Concatenate Line for writing to CSV File
	divMatchOutput = [ds, ts, divHomeTeam.get_text(strip=True), divScore[0], divAwayTeam.get_text(strip=True), divScore[2]] 

	# Create writer object
	writer = csv.writer(csvFile, delimiter='|')
	writer.writerow(divMatchOutput)
'''

# for i in divMatchResults:
	# Parse out Home Team and Score
#	print i
#	print len(i)

# print len(divMatchResults)

'''# Parse out Match Result Game URLs
urlList = divMatchResults.find_all('a', {'class': 'report'})
for i in urlList:
	#Partial URL for Match Results
	stringURL = i.get("href")
	# Full URL for BBC Site
	href = "http://www.bbc.com" + stringURL
	# print i.get_text(strip=True) + ' ' + href
'''