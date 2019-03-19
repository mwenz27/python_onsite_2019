'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''

from requests_html import HTMLSession

url = 'https://en.wikipedia.org/wiki/Ubud'

session = HTMLSession()
r = session.get(url)

# * all the information recorded in the infobox on the right
# First inspect the element the ID was reference #toc
about = r.html.find('#toc', first=True)
#print(about.text)

# * 2 links to images on the site
# * an interesting fact or quote from the page
# * a collection of all the resources (titles and links) related to the page
img = r.html.find('img')  #
for i in img:
    # print(i)
    pass


# an interesting fact or quote from the page


p = r.html.find('p')  #

for i in p:
    print(i)






# r.find('toc')
#
# print(r)
# r.html.render()
#
# for link in r.html.absolute_links:
#     print(link)



````