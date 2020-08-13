from flask import Flask, request

app = Flask(__name__)

import pickle

class BankAccount:
    def __init__(self,name,phone,usemoney,spendmoney):
        self.name = name
        self.phone = phone
        self.usemoney = usemoney
        self.spendmoney = spendmoney
    
    def  __str__(self):
        return "請輸入姓名,請輸入聯絡電話,請輸入信用額度,請輸入新增消費金額"
    
    def check_expense(self,money):
        if self.usemoney > self.spendmoney + money :
           self.spendmoney = self.spendmoney + money
        else : 
           print("超過信用額度")
    
    def check_balance(self):
        return  (self.usemoney - self.spendmoney)
"""
x = input("請輸入姓名: , 請輸入聯絡電話: , 請輸入信用額度: ")
if x == "a" :      
    name = input("name: ")        
    phone = input("phone: ")
    usemoney = int(input("usemoney: "))
    spendmoney = int(input("spendmoney: "))
    bankaccount = BankAccount(name,phone,usemoney,spendmoney)
    filename = name + ".pkl"
    
    with open(filename,"wb") as f :
    
        pickle.dump(bankaccount,f)
    del bankaccount
    
elif x == "b" :
    name = input ("name: ")
    money = int(input ("spendmoney: "))
    filename = name + ".pkl"
    
    with open(filename,"rb") as f :
        y = pickle.load(f)
        y.check_expense(money)
    
    with open(filename,"wb") as f :
        pickle.dump(y,f)
"""
def getBalance(name):
    filename = name + ".pkl"
    with open(filename,"rb") as f :
      y = pickle.load(f)
      ans = str(y.check_balance())
    
    return ans


@app.route('/login', methods=['GET', 'POST'])
def login():
#     if request.method == 'POST':
# #         filename = name + ".pkl"
# #         with open(filename,"rb") as f :
# #               y = pickle.load(f)
# #               ans = y.check_balance()
# #         return ans
# #         return 'Hello' + request.values['username']
#         name = request.values['username']
#         return 'Balance ' + getBalance(name)
    
    return '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="zh-TW"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){window.google={kEI:\'xH3bXsyKO4XLmAXtnZmgDA\',kEXPI:\'0,202123,3,4,32,1151585,5662,730,224,3656,1449,206,3204,10,1226,364,1499,576,241,383,246,5,960,169,225,196,737,105,653,3,1217,967,141,279,23,93,3,51,119,243,85,1122851,1197725,424,78,329040,1294,12383,4855,32691,15248,864,17447,11240,9188,8384,4859,1361,9291,3024,4743,11033,1808,4998,7931,5297,2054,622,298,2090,2975,6430,7432,3874,3222,4298,1,221,2774,919,261,2016,8,3681,708,1279,2213,529,149,1103,842,515,1466,56,4258,312,1137,2,2063,606,1839,184,1777,520,1947,2229,95,326,1286,14,2927,2246,474,1346,741,1039,3227,2845,7,6068,6285,4455,642,2040,1,409,2458,1226,1742,3655,1274,108,3407,908,2,1473,440,1642,881,1251,265,2896,2523,2051,840,1337,1098,3,346,230,970,865,373,3545,706,149,189,3312,2489,28,2224,4981,109,643,4,1337,191,17,356,569,1362,1236,1145,327,68,2,8,42,1797,21,2426,504,43,294,580,337,9,43,76,4,62,571,572,39,92,1884,43,74,1225,213,500,640,92,498,1594,156,586,1,252,139,287,795,778,14,86,3,605,148,433,306,237,1014,12,262,263,1263,163,69,838,90,1188,134,328,37,28,342,78,142,12,621,82,495,268,16,446,23,12,246,500,1274,1,482,205,187,93,980,12,676,180,66,153,130,143,253,2,2,52,5804721,1805894,6996022,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,879,9,305,2494,33,71,4,1,17,3,2,12,1,4,2,2,1,1,1,3,1,2,1,3389622,20572126,41,2682692\',kBL:\'TMhW\'};google.sn=\'webhp\';google.kHL=\'zh-TW\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){\ndocument.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);\nvar a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{color:#c03;font-style:normal;font-weight:normal}a em{text-decoration:underline}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){window.google.erd={sp:\'hp\',jsr:100,bv:20};var e=0,f,g=google.erd,k=g.jsr;google.ml=function(b,d,c,h){google.dl&&(google.dl(b,c),e++);if(0>k){window.console&&console.error(b,c);if(-2==k)throw b;var a=!1}else a=!b||!b.message||"Error loading script"==b.message||1<=e&&!h?!1:!0;if(!a)return null;e++;d&&(f=b&&b.message);d=c||{};c=encodeURIComponent;a="/gen_204?atyp=i&ei="+c(google.kEI);google.kEXPI&&(a+="&jexpid="+c(google.kEXPI));a+="&srcpg="+c(g.sp)+"&jsr="+c(g.jsr)+"&bver="+c(g.bv);for(var l in d)a+="&",a+=c(l),a+="=",a+=c(d[l]);a=a+"&emsg="+c(b.name+": "+b.message);a=a+\n"&jsst="+c(b.stack||"N/A");12288<=a.length&&(a=a.substr(0,12288));b=a;h||google.log(0,"",b);return b};window.onerror=function(b,d,c,h,a){f!==b&&google.ml(a instanceof Error?a:Error(b),!1);f=null;1<=e&&(window.onerror=null)};})();</script></head><body bgcolor="#fff"><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>&#25628;&#23563;</b> <a class=gb1 href="https://www.google.com.tw/imghp?hl=zh-TW&tab=wi">&#22294;&#29255;</a> <a class=gb1 href="https://maps.google.com.tw/maps?hl=zh-TW&tab=wl">&#22320;&#22294;</a> <a class=gb1 href="https://play.google.com/?hl=zh-TW&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=TW&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com.tw/nwshp?hl=zh-TW&tab=wn">&#26032;&#32862;</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">&#38642;&#31471;&#30828;&#30879;</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com.tw/intl/zh-TW/about/products?tab=wh"><u>&#26356;&#22810;</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com.tw/history/optout?hl=zh-TW" class=gb4>&#32178;&#38913;&#35352;&#37636;</a> | <a  href="/preferences?hl=zh-TW" class=gb4>&#35373;&#23450;</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=zh-TW&passive=true&continue=https://www.google.com/" class=gb4>&#30331;&#20837;</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="zh-TW" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" autocomplete="off" value="" title="Google &#25628;&#23563;" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google &#25628;&#23563;" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="&#22909;&#25163;&#27683;" name="btnI" type="submit"><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){var id=\'tsuid1\';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\nelse top.location=\'/doodles/\';};})();</script><input value="AINFCbYAAAAAXtuL1LRZpFEttdBLMq19tgaoMfUXgRKZ" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=zh-TW&amp;authuser=0">&#36914;&#38542;&#25628;&#23563;</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/zh-TW/ads/">&#24291;&#21578;&#26381;&#21209;</a><a href="http://www.google.com.tw/intl/zh-TW/services/">&#21830;&#26989;&#35299;&#27770;&#26041;&#26696;</a><a href="/intl/zh-TW/about.html">&#38364;&#26044; Google</a><a href="https://www.google.com/setprefdomain?prefdom=TW&amp;prev=https://www.google.com.tw/&amp;sig=K_BaYtSQ-qaMPx7MGDWWpooA7mhiU%3D">Google.com.tw</a></div></div><p style="font-size:8pt;color:#767676">&copy; 2020 - <a href="/intl/zh-TW/policies/privacy/">&#38577;&#31169;&#27402;</a> - <a href="/intl/zh-TW/policies/terms/">&#26381;&#21209;&#26781;&#27454;</a></p></span></center><script nonce="rOhwollqwWfngF2q4bTcKA==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u=\'/xjs/_/js/k\\x3dxjs.hp.en.sZBwuc7LsCg.O/m\\x3dsb_he,d/am\\x3dAC8ENgc/d\\x3d1/rs\\x3dACT90oG128R1cORLRpQAanRSkqsMDUHqLw\';\nsetTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu=\'/xjs/_/js/k\\x3dxjs.hp.en.sZBwuc7LsCg.O/m\\x3dsb_he,d/am\\x3dAC8ENgc/d\\x3d1/rs\\x3dACT90oG128R1cORLRpQAanRSkqsMDUHqLw\';})();function _DumpException(e){throw e;}\nfunction _F_installCss(c){}\n(function(){google.jl={dw:false,em:[],emw:false,lls:\'default\',pdt:0,snet:true,uwp:true};})();(function(){var pmc=\'{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22dhqt\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22ffql\\x22:\\x22zh-TW\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22isbh\\x22:28,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22&#28165;&#38500;&#25628;&#23563;\\x22,\\x22dym\\x22:\\x22&#24744;&#26159;&#19981;&#26159;&#35201;&#26597;&#65306;\\x22,\\x22lcky\\x22:\\x22&#22909;&#25163;&#27683;\\x22,\\x22lml\\x22:\\x22&#30637;&#35299;&#35443;&#24773;\\x22,\\x22oskt\\x22:\\x22&#36664;&#20837;&#24037;&#20855;\\x22,\\x22psrc\\x22:\\x22&#24050;&#24478;&#24744;&#30340;&#12300;\\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003E&#32178;&#38913;&#35352;&#37636;\\\\u003C/a\\\\u003E&#12301;&#20013;&#31227;&#38500;&#36889;&#31558;&#25628;&#23563;&#35352;&#37636;\\x22,\\x22psrl\\x22:\\x22&#31227;&#38500;\\x22,\\x22sbit\\x22:\\x22&#20197;&#22294;&#25628;&#23563;\\x22,\\x22srch\\x22:\\x22Google &#25628;&#23563;\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22refpd\\x22:true,\\x22refspre\\x22:true,\\x22rfs\\x22:[],\\x22sbpl\\x22:16,\\x22sbpr\\x22:16,\\x22scd\\x22:10,\\x22stok\\x22:\\x22CHlZlYR_hYkXP2wRaMFENxyKCU4\\x22,\\x22uhde\\x22:false}}\';google.pmc=JSON.parse(pmc);})();</script>        </body></html>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=48763)