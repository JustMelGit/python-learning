# s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
# s1 = 'abaabaabaabaae'
# import re
# # pat = r'(?<=[qwrtypsdfghjklzxcvbnm]{2})([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm]{2})'
# pat = r'(?<=[qwrtypsdfghjklzxcvbnm]{1})([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm]{1})'
# items = map(lambda x: x.group(1),re.finditer(pat,s,re.IGNORECASE))
# for e in items:
# 	print(e)

# strg = 'jjhv'
# s_str = 'z'

# print(sr[0])



# import re
# strg = 'aaadaa'
# s_str = 'aa'
# pat = re.escape(s_str[0:-1])+'(?=[{}])'.format(re.escape(s_str[-1]))
# g = re.findall(pat,strg)
# if g:
#     for e in re.finditer(pat,strg):
#         print(e.span())
# else:
#     print((-1,-1))        
    


# import re

# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """
# print(html)
# print('\n'*3)
# print (re.sub("(<!--.*?-->)", "", html))


# s = """a = 1;
# b = input();

# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.""".split('\n')

# print(len(s))


# for i,e in enumerate(s):
# 	print(i,e)

# for e in s:
# 	print(e)
# import re
# scope = {}

# if __name__ == '__main__':
#     import re
#     for i in range(12):
#     	# print(s[i])
#     	line = re.sub(r' && ',' and ',s[i])
#     	line = re.sub(r' \|\| ',' or ',line)
#     	print(line)

# def replacement(match):
# 	code = match.group(1)
# 	return 'and'

# # pat = r' (&&) '
# # # s = 'elif a*b > 10 || a/b < 1:'
# import re
# s = r'x&& &&& && && x || | ||\|| x'

# pat = r'(?<=[\s]{1})(&&)(?=[\s]{1})'
# # s1 = 'if a + b > 0 && a - b < 0:'
# print(re.sub(pat,replacement,s))

# s = """vin <vineet@>
# vineet <vineet@gmail.com>
# vineet <vineet@gma.il.co.m>
# vineet <vineet@gma-il.co-m>
# vineet <vineet@gma,il.co@m>
# vineet <vineet@gmail,com>
# vineet <.vin@gmail.com>
# vineet <vin-nii@gmail.com>
# vineet <v__i_n-n_ii@gmail.com>""".split('\n')

# s1 = """this <is@valid.com>
# this <is_som@radom.stuff>
# this <is_it@valid.com>
# this <_is@notvalid.com>""".split('\n')





# if __name__ == '__main__':
#     import re
#     import email.utils as parser
#     for i in range(9):
#         name,email = parser.parseaddr(s[i])
#         # print(name,email)
#         pat = r'[a-zA-Z][\w]+[-._]*[\w]*@[a-zA-Z]+\.[a-zA-Z]{1,3}'
#         g = re.fullmatch(pat,email)
#         if g:
#             print(parser.formataddr((name,email)))





# import re

# pat1 = r'(#[0-9A-F]{6}|#[0-9A-F]{3})'

# s = '''#BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }'''.split('\n')

# text = ''
# for e in s:
# 	text += e

# pat = '{.+?}'
# items = re.findall(pat,text)
# for e in items:
# 	g = re.findall(pat1,e,re.I)
# 	if g:
# 		print(g)


# s = 'foo99'
# pat = r'foo(\d\d\d)?'

# print(re.search(pat,s))





# from html.parser import HTMLParser
# import urllib.request
 
# #Import HTML from a URL
# url = urllib.request.urlopen("file:///C:/Users/gnl999935/Desktop/Downloaded%20webpages/Regular%20Expressions_%20Regexes%20in%20Python%20(Part%201)%20%E2%80%93%20Real%20Python.html")
# html = url.read().decode()
# url.close()

# print(html)






# class Parse(HTMLParser):
#     def __init__(self):
#     #Since Python 3, we need to call the __init__() function of the parent class
#         super().__init__()
#         self.reset()
#     #Defining what the method should output when called by HTMLParser.
#     def handle_starttag(self, tag, attrs):
#         # Only parse the 'anchor' tag.
#         if tag == "a":
#            for name,link in attrs:
#                if name == "href" and link.startswith("http"):
#                    print (link)
 
# p = Parse()
# p.feed(html)








# class Parse(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('Start :',tag)
#         for a in attrs:
#         	print('->',a[0],'>',a[1])
#     def handle_endtag(self, tag):
#         print('End   :',tag)

#     def handle_startendtag(self,tag,attrs):
#     	print('Empty :',tag)
#     	for a in attrs:
#     		print('->',a[0],'>',a[1])







# html1 = '''<article class="hentry">
#   <!-- <header>
#     <h1 class="entry-title">But Will It Make You Happy?</h1>
#     <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
#     <p class="byline author vcard">
#         By <span class="fn">Stephanie Rosenbloom</span>
#     </p>
#   </header> -->

#   <div class="entry-content">
#       <p>...article text...</p>
#       <p>...article text...</p>

#       <figure>
#         <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
#         <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
#       </figure>

#       <p>...article text...</p>
#       <p>...article text...</p>

#       <aside>
#         <h2>Share this Article</h2>
#         <ul>
#           <li>Facebook</li>
#           <li>Twitter</li>
#           <li>Etc</li>
#         </ul>
#       </aside>

#       <div class="entry-content-asset">
#         <a href="photo-full.png">
#           <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
#         </a>
#       </div>

#       <p>...article text...</p>
#       <p>...article text...</p>

#       <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
#   </div>

#   <footer>
#     <p>
#       A version of this article appeared in print on August 8,
#       2010, on page BU1 of the New York edition.
#     </p>
#     <div class="source-org vcard copyright">
#         Copyright 2010 <span class="org fn">The New York Times Company</span>
#     </div>
#   </footer>
# </article>'''


# testParser  = Parse()
# testParser.feed(html1)



# html = '''<!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->'''




# for e in html:
# 	print(e)

# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         import re
#         pat = r'<!--.+?-->'
#         g = re.match(pat,data.strip())
#         if g:
#             print('>>> Single-line Comment')
#             for e in data.split('\n'):
#                 if e != '\n':
#                     print(e)
#         else:
#             print('>>> Multi-line Comment')
#             for e in data.split('\n'):
#             	if e != '\n':
#             		print(e)
#     def handle_data(self, data):
#         print('>>> Data')
#         for e in data.split('\n'):
#             if e != '\n':
#                 print(e)

# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#     	if len(data.split('\n')) > 1:
#     		print('>>> Multi-line Comment')
#     		print(data)
#     	else:
#     		print('>>> Single-line Comment')
#     		print(data)
#     def handle_data(self, data):
#     	if data != '\n':
#     		print(data.strip())

# html = ""       
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'

# print(html)
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()

# s = ['B1CD102354','B1CDEF2354']
# pat1 = r'[A-Z]{1}'

# print(re.findall(pat1,s))


# if __name__ == '__main__':
    
#     import re
#     for i in range(2):
#         txt_str = s[i]
#         g = len(set(txt_str))
#         if g != 10:
#             print('Invalid')
#             continue
#         if not re.fullmatch(r'\w+',txt_str):
#             print('Invalid')
#             continue
#         pat1 = r'[A-Z]{1}'
#         pat2 = r'[0-9]{1}'

#         if len(re.findall(pat1,txt_str)) > 1 and len(re.findall(pat2,txt_str)) > 2:
#         	print('Valid')
#         else:
#         	print('Invalid')
# import re

# xml ='''<feed> xml:lang='en'>
#   <title>HackerRank</title>
#   <subtitle lang='en'>Programming challenges</subtitle>
#   <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#   <updated>2013-12-25T12:00:00</updated>
#   <entry>
#     <author> gender='male'>Harsh</author>
#     <question> type='hard'>XML 1</question>
#     <description> type='text'>This is related to XML parsing</description>
#   </entry>
# </feed>'''

# xml1 = '''
# <Bookstore>
#    <Book ISBN="ISBN-13:978-1599620787" Price="15.23" Weight="1.5">
#       <Title>New York Deco</Title>
#       <Authors>
#          <Author Residence="New York City">
#             <First_Name>Richard</First_Name>
#             <Last_Name>Berenholtz</Last_Name>
#          </Author>
#       </Authors>
#    </Book>
#    <Book ISBN="ISBN-13:978-1579128562" Price="15.80">
#       <Remark>
#       Five Hundred Buildings of New York and over one million other books are available for Amazon Kindle.
#       </Remark>
#       <Title>Five Hundred Buildings of New York</Title>
#       <Authors>
#          <Author Residence="Beijing">
#             <First_Name>Bill</First_Name>
#             <Last_Name>Harris</Last_Name>
#          </Author>
#          <Author Residence="New York City">
#             <First_Name>Jorg</First_Name>
#             <Last_Name>Brockmann</Last_Name>
#          </Author>
#       </Authors>
#    </Book>
# </Bookstore>
# '''



# a_str = ''
# for e in xml:
#   a_str += e.strip()
# # print(re.findall(pat,a_str))

# pat = r'<(.+?)>(.+?)</\1>'

# # s = "<subtitlelang='en'>Programmingchallenges</subtitle>"
# # print(re.findall(pat,s))



# def recurfind(pat,xml):
#   g = re.findall(pat,xml)
#   # print(len(g))
#   if len(g) == 0:
#     print(len(g))
#     # print(g)
#     # print(g)
#     # print(g[0])
#     # print()
#   else:
#     for e in g:
#       print(e)
#       recurfind(pat,e[1])

#       # print(e)
#       # recurfind(pat,e)
#       # if g:
#       #   print(g[0])
#       #   print()

# recurfind(pat,a_str)




# s1 = "<authorgender='male'>Harsh</author><questiontype='hard'>XML1</question><descriptiontype='text'>ThisisrelatedtoXMLparsing</description>"
# print(re.findall(pat,s1))

# import xml.etree.ElementTree as ET
# tree = ET.ElementTree(ET.fromstring(xml1))

# l = 0
# root = tree.getroot()
# # l += len(root.attrib)
# # print(l)
# for child in root.iter():
#   # print(child)
#   print(child.tag,len(child.attrib))
#   print(child.attrib)

#   l += len(child.attrib)
# print(l)


# for element in tree.iter("Author"):
#     print(element.find('First_Name').text,element.find('Last_Name').text)


# print(tree.find('Book[@Weight="1.5"]/Authors/Author/First_Name').text)










# import re

# html2 = '''
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# '''
# html = '''
# <script type="text/javascript" src="js/cufon-yui.js"></script>
# <script type="text/javascript" src="js/TitilliumMaps.font.js"></script><h1>Business Solutions</h1>
# <h2>Business Insurance</h2><script type="text/javascript">
#     Cufon.replace('h1, h2', { fontFamily: "TitilliumMaps26L", hover: true });
# </script>
# '''

# html3 = '''
# <!-- first try HTML5 playback: if serving as XML, expand `controls` to `controls="controls"` and autoplay likewise -->
# <!-- warning: playback does not work on iOS3 if you include the poster attribute! fixed in iOS4.0 -->
# <video width="640" height="360">
#   <!-- MP4 must be first for iPad! -->
#   <source src="__VIDEO__.MP4" type="video/mp4" /><!-- Safari / iOS video    -->
#   <source src="__VIDEO__.OGV" type="video/ogg" /><!-- Firefox / Opera / Chrome10 -->
#   <!-- fallback to Flash: -->
#   <object width="640" height="360" type="application/x-shockwave-flash" data="__FLASH__.SWF">
#     <!-- Firefox uses the `data` attribute above, IE/Safari uses the param below -->
#     <param name="movie" value="__FLASH__.SWF" />
#     <param name="flashvars" value="controlbar=over&image=__POSTER__.JPG&file=__VIDEO__.MP4" />
#     <!-- fallback image. note the title field below, put the title of the video there -->
#     <img src="__VIDEO__.JPG" width="640" height="360" alt="__TITLE__"
#          title="No video playback capabilities, please download the{-truncated-}

# '''


# html4 ='''
# <!--[if !IE 6]><!-->
#   <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />
# <!--<![endif]-->
# <!--[if gte IE 7]>
#   <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />
# <![endif]-->
# <!--[if lte IE 6]>
#   <link rel="stylesheet" type="text/css" media="screen, projection" href="http://universal-ie6-css.googlecode.com/files/ie6.0.3.css" />
# <![endif]-->
# '''


# html5 = '''
# <article class="hentry">
#   <!-- <header>
#     <h1 class="entry-title">But Will It Make You Happy?</h1>
#     <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
#     <p class="byline author vcard">
#         By <span class="fn">Stephanie Rosenbloom</span>
#     </p>
#   </header> -->

#   <div class="entry-content">
#       <p>...article text...</p>
#       <p>...article text...</p>

#       <figure>
#         <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
#         <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
#       </figure>

#       <p>...article text...</p>
#       <p>...article text...</p>

#       <aside>
#         <h2>Share this Article</h2>
#         <ul>
#           <li>Facebook</li>
#           <li>Twitter</li>
#           <li>Etc</li>
#         </ul>
#       </aside>

#       <div class="entry-content-asset">
#         <a href="photo-full.png">
#           <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
#         </a>
#       </div>

#       <p>...article text...</p>
#       <p>...article text...</p>

#       <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
#   </div>

#   <footer>
#     <p>
#       A version of this article appeared in print on August 8,
#       2010, on page BU1 of the New York edition.
#     </p>
#     <div class="source-org vcard copyright">
#         Copyright 2010 <span class="org fn">The New York Times Company</span>
#     </div>
#   </footer>
# </article>
# '''


