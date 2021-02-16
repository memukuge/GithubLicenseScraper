#!/usr/bin/env python
# coding: utf-8

# In[22]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd



# In[11]:


def getDependency(package):
    deplist = []
    load_url = "https://github.com" + package + "/network/dependencies"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    tags = soup.select("a[data-octo-click='dep_graph_package']")
    for tag in tags:
        #print(tag.get('href'))
        if tag.get('href') in deplist:
            pass
            #print("dubble")
        else:
            deplist.append(tag.get('href'))
    return deplist


# In[ ]:





# In[ ]:



    


# In[29]:


def pickupPackage(url):
    package = re.search(r'\/[^/]+\/[^/]+',url[18:])
    return package.group(0)


# In[5]:


def checklicense(package):
    top_url = "https://github.com" + package
    top_html = requests.get(top_url)
    top_soup = BeautifulSoup(top_html.content, "html.parser")
    #print(top_soup)
    ltags = top_soup.select('a[href*="LICENSE"]')
    #print(ltags)
    #print(ltags[0].get_text().strip())
    if len(ltags) == 0 :
        return "NOLICENSE" , ""
    else:
        tag = ltags[0]
        return tag.get_text().strip() , tag.get('href')
    


# In[46]:


def getDict(url):
    packageDict={"package":[],"license":[],"url":[]}
    package = pickupPackage(url)
    list = getDependency(package)
    #print(list)
    for l in list:
        lic,url = checklicense(l)
        packageDict["package"].append(l)
        packageDict["license"].append(lic)
        packageDict["url"].append(url)
        #print(l + ", " + lic + ", " + url)
    return(packageDict)


# In[39]:


def test(url):
    package = pickupPackage(url)
    list = getDependency(package)
    print(list)
    for l in list:
        lic,url = checklicense(l)
        print(l + ", " + lic + ", " + url)


# In[47]:


if __name__ == '__main__' :
    output= getDict("https://github.com/tensorflow/tensorflow")
    print(output)
    my_df = pd.DataFrame.from_dict(output)
    print(my_df)
    my_df.query('license == "View license"')


# In[48]:





# In[49]:





# In[53]:





# In[ ]:




