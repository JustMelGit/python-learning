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
# xml3 = '''
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
# '''
# import xml.etree.ElementTree as etree
# tree = etree.ElementTree(etree.fromstring(xml3))
# root = tree.getroot()


# depth = 0
# def maxdepth(xml,l):
#    global depth
#    if not root.iter():
#       return l
#    else:
#       for child in xml:
#          maxdepth(child,l+1)
#          if l > depth:
#             depth = l
#    return depth 

# print(maxdepth(root,1))







# data_string = """
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
# """


# data_string = """
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
# </Bookstore>
# """




# data_string1 = """
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
# """




# from lxml import etree
# root = etree.XML(data_string)
# # print(len(root))



# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     if (level == maxdepth):
#         maxdepth += 1
#     # print(maxdepth)
        
#     for child in elem:
#         depth(child, level + 1)
#     return maxdepth-1

# print(depth(root,0))


