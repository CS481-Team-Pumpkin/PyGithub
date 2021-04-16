""" Testing file for the search_repositories function in MainClass.py. """
""" For testing & researching the function search_repositories."""
from github import Github

g = Github("access_token")

# test search function
#may be space errors happening in query good first issue
#query = 'good-first-issues OR good first issues:>3' #returns until errors from max api calls - but different than either alone (0 for goodfirstissues, many for good-first-issue)
#query = 'good-first-issues OR goodfirstissues OR good first issues:>3' # returns only 90
#query = 'good AND first AND issues:>3' #returns only 33, plural issues or issue
#query = "goodfirstissues:>3" # returns zero
#query = 'good-first-issues:>50' # returs until token error due to max api calls
#query = "good first issues:>3" # returns 33
repositories = g.search_repositories(query)
count = 0
print(query)
for repo in repositories:
    print(repo)
    count+=1
print("count:", count)
