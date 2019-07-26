import scipy.special as scsp

def lower_incomplete_gamma (a,b):
    #これでやっと第１種不完全ガンマ関数　γ(a,b）
    return scsp.gammainc(a,b)*scsp.gamma(a)

def upper_incomplete_gamma(a,b):
    #これでやっと第２種不完全ガンマ関数　Γ(a,b）
    return scsp.gammaincc(a,b)*scsp.gamma(a)

def gamma(a):
    #これでやっとガンマ関数　Γ(z)=z!
    return a*scsp.gamma(a)
