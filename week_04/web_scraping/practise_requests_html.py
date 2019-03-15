from requests_html import HTML


from requests_html import HTMLSession

url = 'https://en.wikipedia.org/wiki/Planar_transmission_line'


session = HTMLSession()
r = session.get(url)
print(r.html)

headline = r.html.find('div')

print(headline.html)