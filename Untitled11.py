
# coding: utf-8

# In[48]:


import scipy.special as scsp


# In[49]:


def lower_incomplete_gamma (a,b):
    #これでやっと第１種不完全ガンマ関数　γ(a,b）
    return scsp.gammainc(a,b)*scsp.gamma(a)
def upper_incomplete_gamma(a,b):
    #これでやっと第２種不完全ガンマ関数　Γ(a,b）
    return scsp.gammaincc(a,b)*scsp.gamma(a)

def gamma(a):
    #これでやっとガンマ関数　Γ(z)=z!
    return a*scsp.gamma(a)


# In[50]:


lower_incomplete_gamma(1,2)


# In[51]:


upper_incomplete_gamma(1,2)


# In[64]:




