from bs4 import BeautifulSoup
import  requests

url = 'https://www.tripadvisor.cn/Attractions-g294212-Activities-Beijing.html#ATTRACTION_SORT_WRAPPER'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.listing_title > a[target="_blank"]')
imgs = soup.select('img[width="180"]')
cates = soup.select('div.p13n_reasoning_v ')

print(titles)



for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img'  :img.get('src'),
        'cate' :list(cate.stripped_strings),

    }
    print(data)

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie':'TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; ServerPool=A; TART=%1%enc%3AHsYzjnGXAIDMul7SUflt4BCt%2Fc03VXwXauMnEGMvh5Q1B7Tzz1GF90MdY2rXscTlmcxYZVRNrM4%3D; TAUnique=%1%enc%3AtldHBELviqEkynH8KNM1P%2FqOSi11s4sHzhj8%2FVZDcZw2jHwltRJPGQ%3D%3D; TASSK=enc%3AAMYIg3qSyfebi4irvt4paHOKh8l2EL4lDwQ65r%2Fa4Sxr4hLvGKFPWHT6U49uJyf8%2BDxe%2F4VznOLH0HOQ87xK%2BaGKqFFPaxNAyV%2BEy5fXkvH7xMf7bW0hNVoHvhDRTsE9nA%3D%3D; TAPD=tripadvisor.cn; SecureLogin2=3.4%3AALHfFjFtT6OgGvAw60NmU2duPcZD%2FH6Fv7ZRcj287ieuW7X3yhLKzH%2BFk8%2BTn%2F4R%2Fgv8Htfv6mipwADx2TF0VWjPy9Awf3KP9DcAOemDYy%2BffUGL6Nrmi1d5lXSuNJCG2HymlJIdI%2Bqn4VPvCVKYAMkR74RBkPXXpWHC6m%2Fv6gkoFRr0YvH0ClC7%2BGwC%2FHW0sJaLqt3gIeydnMD%2BKgumI0g%3D; TAAuth3=3%3Aef0182de3f24b97164b2a78e7f0f25c1%3AAFG6ZcUJH5dLLduXuNdxCWFCLbp3p37xiVOpMdaSF6xbWYe%2Blhgdh14QeuDix02TVyrFRLXK1f9DhuqbvdESlYOWhZIlW1diGm6L%2FKXhr0N53J5ksYQ6Bh5e9ua7x08VTjJc%2BjET2tmj8X6TG%2F4%2FKa8%2FCy6ub7qxBIRvQFAPClbVVTG99Eb5zCzwEeMNitirWQ%3D%3D; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C9%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C2%2C1527137840%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C2%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; VRMCID=%1%V1*id.12019*llp.%2F-m12019*e.1527656730881; ki_r=; TAReturnTo=%1%%2FAttraction_Review-g294212-d311534-Reviews-Temple_of_Heaven-Beijing.html; roybatty=TNI1625!AFwiTBuNWQurmtiwGhQglOyhI8StlG8Ljr6rYZx6uBgOoTgROez6ZaNxsOVrBQcxPDiuDgFa7kyIA3XHiMVXWuYN%2FcOQUKl10J2KgTvxJuXC4OzE9AQuhI44t46oaH7PCljbUr7bWZJBoIK4BdN5%2BvZXcAQvBRhqfaxdvig5iF%2FD%2C1; ki_t=1527029649962%3B1527029649962%3B1527052032528%3B1%3B30; TASession=%1%V2ID.B2E53DD025BF1A1C5920CA434AC41DD3*SQ.184*MC.12019*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Flink%3Furl%3D41lDhM1bZ0X5eKs-rSP3UxgPgBVMClVpxlfWfXcj1UpWCCvMvUQ_ArzRXnD4of-U%26wd%3D%26eqid%3D8e182b3c0003cf32000000035b04f696*LP.%2F-m12019*PR.39780%7C*LS.ActionRecord*GR.56*TCPAR.36*TBR.2*EXEX.72*ABTR.85*PHTB.99*FS.78*CPU.33*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.B8357E77F565B9D80BFF144D55023C1A*LF.zhCN*FA.1*DF.0*IR.3*OD.en_US*MS.-1*RMS.-1*TRA.true*LD.311534; TAUD=LA-1526998034501-1*RDD-1-2018_05_22*LG-54005796-2.1.F.*LD-54005797-.....'

}

url_saves = 'https://www.tripadvisor.cn/Saves/1157343'
wb_data = requests.get(url_saves,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)