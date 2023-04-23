import json
from scrapingant_client import ScrapingAntClient
import time
import math
import requests
from datetime import datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

html_str = """<!DOCTYPE html><html lang="en-us" class="a-ws a-js a-audio a-video a-canvas a-svg a-drag-drop a-geolocation a-history a-webworker a-autofocus a-input-placeholder a-textarea-placeholder a-local-storage a-gradients a-hires a-transform3d a-touch-scrolling a-text-shadow a-text-stroke a-box-shadow a-border-radius a-border-image a-opacity a-transform a-transition a-ember" data-19ax5a9jf="dingo" data-aui-build-date="3.23.1-2023-04-19"><!-- sp:feature:head-start --><head><script async="" src="https://images-na.ssl-images-amazon.com/images/I/31bJewCvY-L.js" crossorigin="anonymous"></script><script>var aPageStart = (new Date()).getTime();</script><meta charset="utf-8">
<!-- sp:end-feature:head-start -->
<!-- sp:feature:csm:head-open-part1 -->

<script type="text/javascript">var ue_t0=ue_t0||+new Date();</script>
<!-- sp:end-feature:csm:head-open-part1 -->
<!-- sp:feature:cs-optimization -->
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="https://images-na.ssl-images-amazon.com">
<link rel="dns-prefetch" href="https://m.media-amazon.com">
<link rel="dns-prefetch" href="https://completion.amazon.com">
<!-- sp:end-feature:cs-optimization -->
<!-- sp:feature:csm:head-open-part2 -->
<script type="text/javascript">
window.ue_ihb = (window.ue_ihb || window.ueinit || 0) + 1;
if (window.ue_ihb === 1) {

var ue_csm = window,
    ue_hob = +new Date();
(function(d){var e=d.ue=d.ue||{},f=Date.now||function(){return+new Date};e.d=function(b){return f()-(b?0:d.ue_t0)};e.stub=function(b,a){if(!b[a]){var c=[];b[a]=function(){c.push([c.slice.call(arguments),e.d(),d.ue_id])};b[a].replay=function(b){for(var a;a=c.shift();)b(a[0],a[1],a[2])};b[a].isStub=1}};e.exec=function(b,a){return function(){try{return b.apply(this,arguments)}catch(c){ueLogError(c,{attribution:a||"undefined",logLevel:"WARN"})}}}})(ue_csm);


    var ue_err_chan = 'jserr-rw';
(function(d,e){function h(f,b){if(!(a.ec>a.mxe)&&f){a.ter.push(f);b=b||{};var c=f.logLevel||b.logLevel;c&&c!==k&&c!==m&&c!==n&&c!==p||a.ec++;c&&c!=k||a.ecf++;b.pageURL=""+(e.location?e.location.href:"");b.logLevel=c;b.attribution=f.attribution||b.attribution;a.erl.push({ex:f,info:b})}}function l(a,b,c,e,g){d.ueLogError({m:a,f:b,l:c,c:""+e,err:g,fromOnError:1,args:arguments},g?{attribution:g.attribution,logLevel:g.logLevel}:void 0);return!1}var k="FATAL",m="ERROR",n="WARN",p="DOWNGRADED",a={ec:0,ecf:0,
pec:0,ts:0,erl:[],ter:[],buffer:[],mxe:50,startTimer:function(){a.ts++;setInterval(function(){d.ue&&a.pec<a.ec&&d.uex("at");a.pec=a.ec},1E4)}};l.skipTrace=1;h.skipTrace=1;h.isStub=1;d.ueLogError=h;d.ue_err=a;e.onerror=l})(ue_csm,window);


var ue_id = 'BNJYY9EBY54VZZF6X4X6',
    ue_url = '/rd/uedata',
    ue_navtiming = 1,
    ue_mid = 'ATVPDKIKX0DER',
    ue_sid = '139-5329492-5095613',
    ue_sn = 'www.amazon.com',
    ue_furl = 'fls-na.amazon.com',
    ue_surl = 'https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.prod',
    ue_int = 0,
    ue_fcsn = 1,
    ue_urt = 3,
    ue_rpl_ns = 'cel-rpl',
    ue_ddq = 1,
    ue_fpf = '//fls-na.amazon.com/1/batch/1/OP/ATVPDKIKX0DER:139-5329492-5095613:BNJYY9EBY54VZZF6X4X6$uedata=s:',
    ue_sbuimp = 1,
    ue_ibft = 0,
    ue_sswmts = 0,
    ue_jsmtf = 0,
    ue_fnt = 0,
    ue_lpsi = 6000,
    ue_no_counters = 1,

    ue_swi = 1;
var ue_viz=function(){(function(b,e,a){function k(c){if(b.ue.viz.length<p&&!l){var a=c.type;c=c.originalEvent;/^focus./.test(a)&&c&&(c.toElement||c.fromElement||c.relatedTarget)||(a=e[m]||("blur"==a||"focusout"==a?"hidden":"visible"),b.ue.viz.push(a+":"+(+new Date-b.ue.t0)),"visible"==a&&(b.ue.isl&&q("at"),l=1))}}for(var l=0,q=b.uex,f,g,m,n=["","webkit","o","ms","moz"],d=0,p=20,h=0;h<n.length&&!d;h++)if(a=n[h],f=(a?a+"H":"h")+"idden",d="boolean"==typeof e[f])g=a+"visibilitychange",m=(a?a+"V":"v")+
"isibilityState";k({});d&&e.addEventListener(g,k,0);b.ue&&d&&(b.ue.pageViz={event:g,propHid:f})})(ue_csm,ue_csm.document,ue_csm.window)};

(function(d,h,N){function H(a){return a&&a.replace&&a.replace(/^\s+|\s+$/g,"")}function u(a){return"undefined"===typeof a}function B(a,b){for(var c in b)b[v](c)&&(a[c]=b[c])}function I(a){try{var b=N.cookie.match(RegExp("(^| )"+a+"=([^;]+)"));if(b)return b[2].trim()}catch(c){}}function O(k,b,c){var q=(x||{}).type;if("device"!==c||2!==q&&1!==q)k&&(d.ue_id=a.id=a.rid=k,w&&(w=w.replace(/((.*?:){2})(\w+)/,function(a,b){return b+k})),D&&(e("id",D,k),D=0)),b&&(w&&(w=w.replace(/(.*?:)(\w|-)+/,function(a,
c){return c+b})),d.ue_sid=b),c&&a.tag("page-source:"+c),d.ue_fpf=w}function P(){var a={};return function(b){b&&(a[b]=1);b=[];for(var c in a)a[v](c)&&b.push(c);return b}}function y(d,b,c,q){q=q||+new E;var f,m;if(b||u(c)){if(d)for(m in f=b?e("t",b)||e("t",b,{}):a.t,f[d]=q,c)c[v](m)&&e(m,b,c[m]);return q}}function e(d,b,c){var e=b&&b!=a.id?a.sc[b]:a;e||(e=a.sc[b]={});"id"===d&&c&&(Q=1);return e[d]=c||e[d]}function R(d,b,c,e,f){c="on"+c;var m=b[c];"function"===typeof m?d&&(a.h[d]=m):m=function(){};b[c]=
function(a){f?(e(a),m(a)):(m(a),e(a))};b[c]&&(b[c].isUeh=1)}function S(k,b,c,q){function p(b,c){var d=[b],g=0,f={},m,h;c?(d.push("m=1"),f[c]=1):f=a.sc;for(h in f)if(f[v](h)){var q=e("wb",h),p=e("t",h)||{},n=e("t0",h)||a.t0,l;if(c||2==q){q=q?g++:"";d.push("sc"+q+"="+h);for(l in p)u(p[l])||null===p[l]||d.push(l+q+"="+(p[l]-n));d.push("t"+q+"="+p[k]);if(e("ctb",h)||e("wb",h))m=1}}!J&&m&&d.push("ctb=1");return d.join("&")}function m(b,c,g,e,f){if(b){var k=d.ue_err;d.ue_url&&!e&&!f&&b&&0<b.length&&(e=
new Image,a.iel.push(e),e.src=b,a.count&&a.count("postbackImageSize",b.length));w?(f=h.encodeURIComponent)&&b&&(e=new Image,b=""+d.ue_fpf+f(b)+":"+(+new E-d.ue_t0),a.iel.push(e),e.src=b):a.log&&(a.log(b,"uedata",{n:1}),a.ielf.push(b));k&&!k.ts&&k.startTimer();a.b&&(k=a.b,a.b="",m(k,c,g,1))}}function A(b){var c=x?x.type:F,d=2==c||a.isBFonMshop,c=c&&!d,e=a.bfini;Q||(e&&1<e&&(b+="&bfform=1",c||(a.isBFT=e-1)),d&&(b+="&bfnt=1",a.isBFT=a.isBFT||1),a.ssw&&a.isBFT&&(a.isBFonMshop&&(a.isNRBF=0),u(a.isNRBF)&&
(d=a.ssw(a.oid),d.e||u(d.val)||(a.isNRBF=1<d.val?0:1)),u(a.isNRBF)||(b+="&nrbf="+a.isNRBF)),a.isBFT&&!a.isNRBF&&(b+="&bft="+a.isBFT));return b}if(!a.paused&&(b||u(c))){for(var l in c)c[v](l)&&e(l,b,c[l]);a.isBFonMshop||y("pc",b,c);l="ld"===k&&b&&e("wb",b);var s=e("id",b)||a.id;l||s===a.oid||(D=b,ba(s,(e("t",b)||{}).tc||+e("t0",b),+e("t0",b)));var s=e("id",b)||a.id,t=e("id2",b),g=a.url+"?"+k+"&v="+a.v+"&id="+s,J=e("ctb",b)||e("wb",b),z;J&&(g+="&ctb="+J);t&&(g+="&id2="+t);1<d.ueinit&&(g+="&ic="+d.ueinit);
if(!("ld"!=k&&"ul"!=k||b&&b!=s)){if("ld"==k){try{h[K]&&h[K].isUeh&&(h[K]=null)}catch(I){}if(h.chrome)for(t=0;t<L.length;t++)T(G,L[t]);(t=N.ue_backdetect)&&t.ue_back&&t.ue_back.value++;d._uess&&(z=d._uess());a.isl=1}a._bf&&(g+="&bf="+a._bf());d.ue_navtiming&&f&&(e("ctb",s,"1"),a.isBFonMshop||y("tc",F,F,M));!C||a.isBFonMshop||U||(f&&B(a.t,{na_:f.navigationStart,ul_:f.unloadEventStart,_ul:f.unloadEventEnd,rd_:f.redirectStart,_rd:f.redirectEnd,fe_:f.fetchStart,lk_:f.domainLookupStart,_lk:f.domainLookupEnd,
co_:f.connectStart,_co:f.connectEnd,sc_:f.secureConnectionStart,rq_:f.requestStart,rs_:f.responseStart,_rs:f.responseEnd,dl_:f.domLoading,di_:f.domInteractive,de_:f.domContentLoadedEventStart,_de:f.domContentLoadedEventEnd,_dc:f.domComplete,ld_:f.loadEventStart,_ld:f.loadEventEnd,ntd:("function"!==typeof C.now||u(M)?0:new E(M+C.now())-new E)+a.t0}),x&&B(a.t,{ty:x.type+a.t0,rc:x.redirectCount+a.t0}),U=1);a.isBFonMshop||B(a.t,{hob:d.ue_hob,hoe:d.ue_hoe});a.ifr&&(g+="&ifr=1")}y(k,b,c,q);var r,n;l||b&&
b!==s||ca(b);(c=d.ue_mbl)&&c.cnt&&!l&&(g+=c.cnt());l?e("wb",b,2):"ld"==k&&(a.lid=H(s));for(r in a.sc)if(1==e("wb",r))break;if(l){if(a.s)return;g=p(g,null)}else c=p(g,null),c!=g&&(c=A(c),a.b=c),z&&(g+=z),g=p(g,b||a.id);g=A(g);if(a.b||l)for(r in a.sc)2==e("wb",r)&&delete a.sc[r];z=0;a._rt&&(g+="&rt="+a._rt());c=h.csa;if(!l&&c)for(n in r=e("t",b)||{},c=c("PageTiming"),r)r[v](n)&&c("mark",da[n]||n,r[n]);l||(a.s=0,(n=d.ue_err)&&0<n.ec&&n.pec<n.ec&&(n.pec=n.ec,g+="&ec="+n.ec+"&ecf="+n.ecf),z=e("ctb",b),
"ld"!==k||b||a.markers?a.markers&&a.isl&&!l&&b&&B(a.markers,e("t",b)):(a.markers={},B(a.markers,e("t",b))),e("t",b,{}));a.tag&&a.tag().length&&(g+="&csmtags="+a.tag().join("|"),a.tag=P());n=a.viz||[];(r=n.length)&&(g+="&viz="+n.splice(0,r).join("|"));u(d.ue_pty)||(g+="&pty="+d.ue_pty+"&spty="+d.ue_spty+"&pti="+d.ue_pti);a.tabid&&(g+="&tid="+a.tabid);a.aftb&&(g+="&aftb=1");!a._ui||b&&b!=s||(g+=a._ui());a.a=g;m(g,k,z,l,b&&"string"===typeof b&&-1!==b.indexOf("csa:"))}}function ca(a){var b=h.ue_csm_markers||
{},c;for(c in b)b[v](c)&&y(c,a,F,b[c])}function A(a,b,c){c=c||h;if(c[V])c[V](a,b,!1);else if(c[W])c[W]("on"+a,b)}function T(a,b,c){c=c||h;if(c[X])c[X](a,b,!1);else if(c[Y])c[Y]("on"+a,b)}function Z(){function a(){d.onUl()}function b(a){return function(){c[a]||(c[a]=1,S(a))}}var c={},e,f;d.onLd=b("ld");d.onLdEnd=b("ld");d.onUl=b("ul");e={stop:b("os")};h.chrome?(A(G,a),L.push(a)):e[G]=d.onUl;for(f in e)e[v](f)&&R(0,h,f,e[f]);d.ue_viz&&ue_viz();A("load",d.onLd);y("ue")}function ba(e,b,c){var f=d.ue_mbl,
p=h.csa,m=p&&p("SPA"),p=p&&p("PageTiming");f&&f.ajax&&f.ajax(b,c);m&&p&&(m("newPage",{requestId:e,transitionType:"soft"}),p("mark","transitionStart",b));a.tag("ajax-transition")}d.ueinit=(d.ueinit||0)+1;var a=d.ue=d.ue||{};a.t0=h.aPageStart||d.ue_t0;a.id=d.ue_id;a.url=d.ue_url;a.rid=d.ue_id;a.a="";a.b="";a.h={};a.s=1;a.t={};a.sc={};a.iel=[];a.ielf=[];a.viz=[];a.v="0.247493.0";a.paused=!1;var v="hasOwnProperty",G="beforeunload",K="on"+G,V="addEventListener",X="removeEventListener",W="attachEvent",
Y="detachEvent",da={cf:"criticalFeature",af:"aboveTheFold",fn:"functional",fp:"firstPaint",fcp:"firstContentfulPaint",bb:"bodyBegin",be:"bodyEnd",ld:"loaded"},E=h.Date,C=h.performance||h.webkitPerformance,f=(C||{}).timing,x=(C||{}).navigation,M=(f||{}).navigationStart,w=d.ue_fpf,Q=0,U=0,L=[],D=0,F;a.oid=H(a.id);a.lid=H(a.id);a._t0=a.t0;a.tag=P();a.ifr=h.top!==h.self||h.frameElement?1:0;a.markers=null;a.attach=A;a.detach=T;if("000-0000000-8675309"===d.ue_sid){var $=I("cdn-rid"),aa=I("session-id");
$&&aa&&O($,aa,"cdn")}d.uei=Z;d.ueh=R;d.ues=e;d.uet=y;d.uex=S;a.reset=O;a.pause=function(d){a.paused=d};Z()})(ue_csm,ue_csm.window,ue_csm.document);


ue.stub(ue,"event");ue.stub(ue,"onSushiUnload");ue.stub(ue,"onSushiFlush");

ue.stub(ue,"log");ue.stub(ue,"onunload");ue.stub(ue,"onflush");
(function(b){var a=b.ue,g=1===b.ue_no_counters;a.cv={};a.cv.scopes={};a.cv.buffer=[];a.count=function(b,f,c){var e={},d=a.cv,h=c&&0===c.c;e.counter=b;e.value=f;e.t=a.d();c&&c.scope&&(d=a.cv.scopes[c.scope]=a.cv.scopes[c.scope]||{},e.scope=c.scope);if(void 0===f)return d[b];d[b]=f;d=0;c&&c.bf&&(d=1);g||(ue_csm.ue_sclog||!a.clog||0!==d||h?a.log&&a.log(e,"csmcount",{c:1,bf:d}):a.clog(e,"csmcount",{bf:d}));a.cv.buffer.push({c:b,v:f})};a.count("baselineCounter2",1);a&&a.event&&(a.event({requestId:b.ue_id||
"rid",server:b.ue_sn||"sn",obfuscatedMarketplaceId:b.ue_mid||"mid"},"csm","csm.CSMBaselineEvent.4"),a.count("nexusBaselineCounter",1,{bf:1}))})(ue_csm);



var ue_hoe = +new Date();
}
window.ueinit = window.ue_ihb;
</script>

<!-- 1gwyt3154o3fa9e4rffn3fx9pm9b5fjvplt6nrjz4fzi7cgjw -->
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 9849)</script>
<!-- sp:end-feature:csm:head-open-part2 -->
<!-- sp:feature:aui-assets -->
<link rel="stylesheet" href="https://m.media-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,410yLeQZHKL.css,31OSFXVtM5L.css,013z33uKh2L.css,017DsKjNQJL.css,0131vqwP5UL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11fJbvhE5HL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21P6CS3L9LL.css,01oDR3IULNL.css,41Axm2+z87L.css,01XPHJk60-L.css,01S0vRENeAL.css,21IbH+SoKSL.css,11MrAKjcAKL.css,21fecG8pUzL.css,11a5wZbuKrL.css,01CFUgsA-YL.css,31pHA2U5D9L.css,11qour3ND0L.css,116t+WD27UL.css,11gKCCKQV+L.css,11061HxnEvL.css,11oHt2HYxnL.css,01j2JE3j7aL.css,11JQtnL-6eL.css,21KA2rMsZML.css,11jtXRmppwL.css,0114z6bAEoL.css,21uwtfqr5aL.css,11QyqG8yiqL.css,11K24eOJg4L.css,11F2+OBzLyL.css,01890+Vwk8L.css,01g+cOYAZgL.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&amp;VGEEt8I0#us.not-trident.388250-T1.432724-T1.577951-T1.577971-T1.577969-T1.632675-T1.577970-T1">
<script>
(function(d,g,R,G){function v(a){w&&w.tag&&w.tag(l(":","aui",a))}function n(a,b){w&&w.count&&w.count("aui:"+a,0===b?0:b||(w.count("aui:"+a)||0)+1)}function q(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function r(a){return"function"===typeof a}function B(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function l(a,b,c,d){b=b&&c?b+a+c:b||c;return d?l(a,b,d):b}function H(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(u){a[b]=
c}return c}function wa(a,b,c){var d=c=a.length,f=function(){d--||(S.push(b),T||(setTimeout(ha,0),T=!0))};for(f();c--;)ia[a[c]]?f():(C[a[c]]=C[a[c]]||[]).push(f)}function xa(a,b,c,d,f){var e=g.createElement(a?"script":"link");B(e,"error",d);f&&B(e,"load",f);a?(e.type="text/javascript",e.async=!0,c&&/AUIClients|images[/]I/.test(b)&&e.setAttribute("crossorigin","anonymous"),e.src=b):(e.rel="stylesheet",e.href=b);g.getElementsByTagName("head")[0].appendChild(e)}function ja(a,b){return function(c,u){function f(){xa(b,
c,e,function(b){U?n("resource_unload"):e?(e=!1,n("resource_retry"),f()):(n("resource_error"),a.log("Asset failed to load: "+c));b&&b.stopPropagation?b.stopPropagation():d.event&&(d.event.cancelBubble=!0)},u)}if(ka[c])return!1;ka[c]=!0;n("resource_count");var e=!0;return!f()}}function ya(a,b,c){for(var d={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,e,d){b.logError(c,e,d,a)}},f=[],e=0;e<c.length;e++)I.hasOwnProperty(c[e])&&(f[e]=
V.hasOwnProperty(c[e])?V[c[e]](I[c[e]],d):I[c[e]]);return f}function D(a,b,c,u,f){return function(e,g){function n(){var a=null;u?a=g:r(g)&&(W.start=z(),a=g.apply(d,ya(e,h,x)),W.end=z());if(b){I[e]=a;a=e;for(ia[a]=!0;(C[a]||[]).length;)C[a].shift()();delete C[a]}W.done=!0}var h=f||this;r(e)&&(g=e,e=G);b&&(e=e?e.replace(la,""):"__NONAME__",X.hasOwnProperty(e)&&h.error(l(", reregistered by ",l(" by ",e+" already registered",X[e]),h.attribution),e),X[e]=h.attribution);for(var x=[],A=0;A<a.length;A++)x[A]=
a[A].replace(la,"");var W=E[e||"anon"+ ++za]={depend:x,registered:z(),namespace:h.namespace};e&&Aa.hasOwnProperty(e);c?n():wa(x,h.guardFatal(e,n),e);return{decorate:function(a){V[e]=h.guardFatal(e,a)}}}}function ma(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:D(b,!1,a,!1,this),register:D(b,!0,a,!1,this)}}}function Y(a,b){return function(c,d){d||(d=c,c=G);var f=this.attribution;return function(){y.push(b||{attribution:f,name:c,logLevel:a});var e=d.apply(this,arguments);
y.pop();return e}}}function J(a,b){this.load={js:ja(this,!0),css:ja(this)};H(this,"namespace",b);H(this,"attribution",a)}function na(){g.body?t.trigger("a-bodyBegin"):setTimeout(na,20)}function F(a,b){a.className=Z(a,b)+" "+b}function Z(a,b){return(" "+a.className+" ").split(" "+b+" ").join(" ").replace(/^ | $/g,"")}function oa(a){try{return a()}catch(b){return!1}}function aa(a){return d.matchMedia?d.matchMedia(a):{matches:!1}}function K(){if(L){var a=h.mobile||h.tablet?ba.matches&&M.matches:M.matches;
if(pa!==a){var b={w:d.innerWidth||k.clientWidth,h:d.innerHeight||k.clientHeight};if(17<Math.abs(ca.w-b.w)||50<Math.abs(ca.h-b.h))ca=b,(pa=a)?F(k,"a-ws"):k.className=Z(k,"a-ws")}}}function Ba(a){(L=a===G?!L:!!a)&&K()}function Ca(){return L}"use strict";var N=R.now=R.now||function(){return+new R},z=function(a){return a&&a.now?a.now.bind(a):N}(d.performance),O=z(),Aa={},p=d.AmazonUIPageJS||d.P;if(p&&p.when&&p.register){O=[];for(var m=g.currentScript;m;m=m.parentElement)m.id&&O.push(m.id);return p.log("A copy of P has already been loaded on this page.",
"FATAL",O.join(" "))}var w=d.ue;v();v("aui_build_date:3.23.1-2023-04-19");var S=[],Da=[],T=!1;var ha=function(){for(var a=setTimeout(ha,0),b=N();Da.length||S.length;)if(S.shift()(),50<N()-b)return;clearTimeout(a);T=!1};var ia={},C={},ka={},U=!1;B(d,"beforeunload",function(){U=!0;setTimeout(function(){U=!1},1E4)});var la=/^prv:/,X={},I={},V={},E={},za=0,da=String.fromCharCode(92),y=[],qa=!0,ra=d.onerror;d.onerror=function(a,b,c,u,f){f&&"object"===typeof f||(f=Error(a,b,c),f.columnNumber=u,f.stack=
b||c||u?l(da,f.message,"at "+l(":",b,c,u)):G);var e=y.pop()||{};f.attribution=l(":",f.attribution||e.attribution,e.name);f.logLevel=e.logLevel;f.attribution&&console&&console.log&&console.log([f.logLevel||"ERROR",a,"thrown by",f.attribution].join(" "));y=[];ra&&(e=[].slice.call(arguments),e[4]=f,ra.apply(d,e))};J.prototype={logError:function(a,b,c,u){b={message:b,logLevel:c||"ERROR",attribution:l(":",this.attribution,u)};if(d.ueLogError)return d.ueLogError(a||b,a?b:null),!0;console&&console.error&&
(console.log(b),console.error(a));return!1},error:function(a,b,c,d){a=Error(l(":",d,a,c));a.attribution=l(":",this.attribution,b);throw a;},guardError:Y(),guardFatal:Y("FATAL"),guardCurrent:function(a){var b=y[y.length-1];return b?Y(b.logLevel,b).call(this,a):a},guardTime:function(a){var b=y[y.length-1],c=b&&b.name;return c&&c in E?function(){var b=z(),d=a.apply(this,arguments);E[c].async=(E[c].async||0)+z()-b;return d}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:D([],!0,!0,!0),
register:D([],!0),execute:D([]),AUI_BUILD_DATE:"3.23.1-2023-04-19",when:ma(),now:ma(!0),trigger:function(a,b,c){var g=N();this.declare(a,{data:b,pageElapsedTime:g-(d.aPageStart||NaN),triggerTime:g});c&&c.instrument&&P.when("prv:a-logTrigger").execute(function(b){b(a)})},handleTriggers:function(){this.log("handleTriggers deprecated")},attributeErrors:function(a){return new J(a)},_namespace:function(a,b){return new J(a,b)},setPriority:function(a){qa?qa=!1:this.log("setPriority only accept the first call.")}};
var t=H(d,"AmazonUIPageJS",new J);var P=t._namespace("PageJS","AmazonUI");P.declare("prv:p-debug",E);t.declare("p-recorder-events",[]);t.declare("p-recorder-stop",function(){});H(d,"P",t);na();if(g.addEventListener){var sa;g.addEventListener("DOMContentLoaded",sa=function(){t.trigger("a-domready");g.removeEventListener("DOMContentLoaded",sa,!1)},!1)}var k=g.documentElement,ea=function(){var a=["O","ms","Moz","Webkit"],b=g.createElement("div");return{testGradients:function(){return!0},test:function(c){var d=
c.charAt(0).toUpperCase()+c.substr(1);c=(a.join(d+" ")+d+" "+c).split(" ");for(d=c.length;d--;)if(""===b.style[c[d]])return!0;return!1},testTransform3d:function(){return!0}}}();p=k.className;var ta=/(^| )a-mobile( |$)/.test(p),ua=/(^| )a-tablet( |$)/.test(p),h={audio:function(){return!!g.createElement("audio").canPlayType},video:function(){return!!g.createElement("video").canPlayType},canvas:function(){return!!g.createElement("canvas").getContext},svg:function(){return!!g.createElementNS&&!!g.createElementNS("http://www.w3.org/2000/svg",
"svg").createSVGRect},offline:function(){return navigator.hasOwnProperty&&navigator.hasOwnProperty("onLine")&&navigator.onLine},dragDrop:function(){return"draggable"in g.createElement("span")},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!d.history||!d.history.pushState)},webworker:function(){return!!d.Worker},autofocus:function(){return"autofocus"in g.createElement("input")},inputPlaceholder:function(){return"placeholder"in g.createElement("input")},textareaPlaceholder:function(){return"placeholder"in
g.createElement("textarea")},localStorage:function(){return"localStorage"in d&&null!==d.localStorage},orientation:function(){return"orientation"in d},touch:function(){return"ontouchend"in g},gradients:function(){return ea.testGradients()},hires:function(){var a=d.devicePixelRatio&&1.5<=d.devicePixelRatio||d.matchMedia&&d.matchMedia("(min-resolution:144dpi)").matches;n("hiRes"+(ta?"Mobile":ua?"Tablet":"Desktop"),a?1:0);return a},transform3d:function(){return ea.testTransform3d()},touchScrolling:function(){return q(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|SOFTWARE=([5-9]|[1-9][0-9]+)(.[0-9]{1,2})+.*DEVICE=iPhone|Chrome|Silk|Firefox|Trident.+?; Touch/i)},
ios:function(){return q(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&&!q(/trident|Edge/i)},android:function(){return q(/android.([1-9]|[L-Z])/i)&&!q(/trident|Edge/i)},mobile:function(){return ta},tablet:function(){return ua},rtl:function(){return"rtl"===k.dir}};for(m in h)h.hasOwnProperty(m)&&(h[m]=oa(h[m]));for(var fa="textShadow textStroke boxShadow borderRadius borderImage opacity transform transition".split(" "),Q=0;Q<fa.length;Q++)h[fa[Q]]=oa(function(){return ea.test(fa[Q])});var L=!0,ca={w:0,
h:0},ba=aa("(orientation:landscape)"),M=h.mobile||h.tablet?aa("(min-width:451px)"):aa("(min-width:1250px)");ba.addListener&&ba.addListener(K);M.addListener&&M.addListener(K);var pa;K();var va={getItem:function(a){try{return d.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return d.localStorage.setItem(a,b)}catch(c){}}};k.className=Z(k,"a-no-js");F(k,"a-js");!q(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||d.navigator.standalone||q(/safari/i)||F(k,"a-ember");p=[];for(m in h)h.hasOwnProperty(m)&&
h[m]&&p.push("a-"+m.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()}));F(k,p.join(" "));k.setAttribute("data-aui-build-date","3.23.1-2023-04-19");t.register("p-detect",function(){return{capabilities:h,localStorage:h.localStorage&&va,toggleResponsiveGrid:Ba,responsiveGridEnabled:Ca}});q(/UCBrowser/i)||h.localStorage&&F(k,va.getItem("a-font-class"));t.declare("a-event-revised-handling",!1);t.execute("RetailPageServiceWorker",function(){function a(a,b){f.controller&&a?(a={feature:"retail_service_worker_messaging",
command:a},b&&(a.data=b),f.controller.postMessage(a)):a&&n("sw:sw_message_no_ctrl",1)}function b(a){var b=a.data;if(b&&"retail_service_worker_messaging"===b.feature&&b.command&&b.data){var c=b.data;a=d.ue;var e=d.ueLogError;switch(b.command){case "log_counter":a&&r(a.count)&&c.name&&a.count(c.name,0===c.value?0:c.value||1);break;case "log_tag":a&&r(a.tag)&&c.tag&&(a.tag(c.tag),b=d.uex,a.isl&&r(b)&&b("at"));break;case "log_error":e&&r(e)&&c.message&&e({message:c.message,logLevel:c.level||"ERROR",attribution:c.attribution||
"RetailServiceWorker"});break;case "log_weblab_trigger":if(!c.weblab||!c.treatment)break;a&&r(a.trigger)?a.trigger(c.weblab,c.treatment):(n("sw:wt:miss"),n("sw:wt:miss:"+c.weblab+":"+c.treatment));break;default:n("sw:unsupported_message_command",1)}}}function c(){e.forEach(function(a){v(a)})}function h(a,b,c){if(b){a=q(/Chrome/i)&&!q(/Edge/i)&&!q(/OPR/i)&&!a.capabilities.isAmazonApp&&!q(new RegExp(da+"bwv"+da+"b"));var d="sw:browser:"+c+":";b.browser&&a&&(e.push(d+"supported"),b.browser.action(d,
c));!a&&b.browser&&e.push(d+"unsupported")}}try{var f=navigator.serviceWorker}catch(x){v("sw:nav_err")}(function(){if(f){var c=function(){a("page_loaded",{rid:d.ue_id,mid:d.ue_mid,pty:d.ue_pty,sid:d.ue_sid,spty:d.ue_spty,furl:d.ue_furl})};B(f,"message",b);a("client_messaging_ready");t.when("load").execute(c);B(f,"controllerchange",function(){a("client_messaging_ready");"complete"===g.readyState&&c()})}})();var e=[],k=function(a,b){var c=d.uex,e=d.uet;a=l(":","aui","sw",a);"ld"===b&&r(c)?c("ld",a,
{wb:1}):r(e)&&e(b,a,{wb:1})},m=function(a,b,c){function e(a){b&&r(b.failure)&&b.failure(a)}function g(){x=setTimeout(function(){v(l(":","sw:"+m,h.TIMED_OUT));e({ok:!1,statusCode:h.TIMED_OUT,done:!1});k(m,"ld")},c||4E3)}var h={NO_CONTROLLER:"no_ctrl",TIMED_OUT:"timed_out",UNSUPPORTED_BROWSER:"unsupported_browser",UNEXPECTED_RESPONSE:"unexpected_response"},m=l(":",a.feature,a.command),x,A=!0;if("MessageChannel"in d&&f&&"controller"in f)if(f.controller){var p=new MessageChannel;p.port1.onmessage=function(c){(c=
c.data)&&c.feature===a.feature&&c.command===a.command?(A&&(k(m,"cf"),A=!1),k(m,"af"),clearTimeout(x),c.done||g(),c.ok?b&&r(b.success)&&b.success(c):e(c),c.done&&k(m,"ld")):n(l(":","sw:"+m,h.UNEXPECTED_RESPONSE),1)};g();k(m,"bb");f.controller.postMessage(a,[p.port2])}else v(l(":","sw:"+a.feature,h.NO_CONTROLLER)),e({ok:!1,statusCode:h.NO_CONTROLLER,done:!0});else v(l(":","sw:"+a.feature,h.UNSUPPORTED_BROWSER)),e({ok:!1,statusCode:h.UNSUPPORTED_BROWSER,done:!0})};(function(){f?(k("ctrl_changed","bb"),
f.addEventListener("controllerchange",function(){v("sw:ctrl_changed");k("ctrl_changed","ld")})):n(l(":","sw:ctrl_changed","sw_unsupp"),1)})();(function(){var a=function(){k(b,"ld");var a=d.uex;m({feature:"page_proxy",command:"request_feature_tags"},{success:function(b){b=b.data;Array.isArray(b)&&b.forEach(function(a){"string"===typeof a?v(l(":","sw:ppft",a)):n(l(":","sw:ppft","invalid_tag"),1)});n(l(":","sw:ppft","success"),1);w&&w.isl&&r(a)&&a("at")},failure:function(a){n(l(":","sw:ppft","error:"+
(a.statusCode||"ppft_error")),1)}})};if("requestIdleCallback"in d){var b=l(":","ppft","callback_ricb");d.requestIdleCallback(a,{timeout:1E3})}else b=l(":","ppft","callback_timeout"),setTimeout(a,0);k(b,"bb")})();var p={reg:{},unreg:{}};p.reg.browser={action:function(a,b){f.register("/service-worker.js").then(function(){n(a+"success")}).catch(function(c){t.logError(c,"[AUI SW] Failed to "+b+" service worker: ","ERROR","RetailPageServiceWorker");n(a+"failure")})}};(function(a){var b=a.reg,g=a.unreg;
f&&f.getRegistrations?(P.when("A").execute(function(a){h(a,g,"unregister")}),B(d,"load",function(){P.when("A").execute(function(a){h(a,b,"register");c()})})):(b&&b.browser&&e.push("sw:browser:register:unsupported"),g&&g.browser&&e.push("sw:browser:unregister:unsupported"),c())})(p)});t.declare("a-fix-event-off",!1);n("pagejs:pkgExecTime",z()-O)})(window,document,Date);
(function(b){function q(a,e,d){function g(a,b,c){var f=Array(e.length);~l&&(f[l]={});~m&&(f[m]=c);for(c=0;c<n.length;c++){var g=n[c],h=a[c];f[g]=h}for(c=0;c<p.length;c++)g=p[c],h=b[c],f[g]=h;a=d.apply(null,f);return~l?f[l]:a}"string"!==typeof a&&b.P.error("C001");-1===a.indexOf("@")&&-1<a.indexOf("/")&&(-1<a.indexOf("es3")||-1<a.indexOf("evergreen"))&&(a=a.substring(0,a.lastIndexOf("/")));if(!r[a]){r[a]=!0;d||(d=e,e=[]);a=a.split(":",2);var c=a[1]?a[0]:void 0,f=(a[1]||a[0]).replace(/@capability\//,
"@c/"),k=c?b.P._namespace(c):b.P,t=!f.lastIndexOf("@c/",0),u=!f.lastIndexOf("@m/",0),n=[];a=[];var p=[],v=[],m=-1,l=-1;for(c=0;c<e.length;c++){var h=e[c];"module"===h&&k.error("C002");"exports"===h?l=c:"require"===h?m=c:h.lastIndexOf("@p/",0)?h.lastIndexOf("@c/",0)&&h.lastIndexOf("@m/",0)?(n.push(c),a.push("mix:"+h)):(p.push(c),v.push(h)):(n.push(c),a.push(h.substr(3)))}k.when.apply(k,a).register("mix:"+f,function(){var a=[].slice.call(arguments);return t||u||~m||p.length?{capabilities:v,cardModuleFactory:function(b,
c){b=g(a,b,c);b.P=k;return b},require:~m?q:void 0}:g(a,[],function(){})});(t||u)&&k.when("mix:@amzn/mix.client-runtime","mix:"+f).execute(function(a,b){a.registerCapabilityModule(f,b)});k.when("mix:"+f).register("xcp:"+f,function(a){return a});var q=function(a,b,c){try{var e=-1<f.indexOf("/")?f.split("/")[0]:f,d=a[0],g=d.lastIndexOf("./",0)?d:e+"/"+d.substr(2),h=g.lastIndexOf("@p/",0)?"mix:"+g:g.substr(3);k.when(h).execute(function(a){try{b(a)}catch(x){c(x)}})}catch(w){c(w)}}}}"use strict";var r=
{};b.mix_d||((b.Promise?P:P.when("3p-promise")).register("@p/promise-is-ready",function(a){b.Promise=b.Promise||a}),(Array.prototype.includes?P:P.when("a-polyfill")).register("@p/polyfill-is-ready",function(){}),b.mix_d=function(a,b,d){P.when("@p/promise-is-ready","@p/polyfill-is-ready").execute("@p/mix-d-deps",function(){q(a,b,d)})},b.xcp_d=b.mix_d,P.when("mix:@amzn/mix.client-runtime").execute(function(a){P.declare("xcp:@xcp/runtime",a)}));b.mixTimeout||(b.mixTimeout=function(a,e,d){b.mixCardInitTimeouts||
(b.mixCardInitTimeouts={});b.mixCardInitTimeouts[e]&&clearTimeout(b.mixCardInitTimeouts[e]);b.mixCardInitTimeouts[e]=setTimeout(function(){P.log("Client-side initialization timeout","WARN",a)},d)});b.mix_csa_map=b.mix_csa_map||{};b.mix_csa_internal=b.mix_csa_internal||function(a,e,d){return b.mix_csa_map[e]=b.mix_csa_map[e]||b.csa(a,d)};b.mix_csa_internal_key=b.mix_csa_internal_key||function(a,b){for(var d="",e=0;e<b.length;e++){var c=b[e];void 0!==a[c]&&"object"!==typeof a[c]&&(d+=c+":"+a[c]+",")}if(!d)throw Error("bad mix-csa key gen.");
return d};b.mix_csa_event=b.mix_csa_event||function(a){try{var e=b.mix_csa_internal_key(a,["producerId"])}catch(d){return P.logError(d,"MIX C005","WARN",void 0),function(){}}try{return b.mix_csa_internal("Events",e,a)}catch(d){return P.logError(d,"MIX C004","WARN",e),function(){}}};b.mix_csa=b.mix_csa||function(a,e){try{e=e||"";var d=document.querySelectorAll(a);if(1<d.length)for(var g=0;g<d.length;g++){if(d[g].querySelector(e)){var c=d[g];break}}else 1===d.length&&(c=d[0]);if(!c)throw Error(" ");
return b.mix_csa_internal("Content",a,{element:c})}catch(f){return P.logError(f,"MIX C004","WARN",a),function(){}}}})(window);
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('sp.load.js').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/61ZS63EQSsL.js?AUIClients/AmazonUIjQuery');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/11Y+5x+kkTL._RC|51Am7NcREVL.js,11yKORv-GTL.js,11GgN1+C7hL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,516j7qaWchL.js,11kWu3cNjYL.js,11wr1I7-WYL.js,11OREnu1epL.js,11Wm6BwZ+6L.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31nfKXylf6L.js,01ezj5Rkz1L.js,11bEz2VIYrL.js,31o2NGTXThL.js,01rpauTep4L.js,01XC3MnuvfL.js_.js?AUIClients/AmazonUI&MFdCk5El#567364-T1.432724-T1.577970-T1');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/51EIwpasq4L.js?AUIClients/CardJsRuntimeBuzzCopyBuild');
});
</script>
<!-- sp:end-feature:aui-assets -->
<!-- sp:feature:nav-inline-css -->
<!-- NAVYAAN CSS -->

<style type="text/css">
.nav-sprite-v1 .nav-sprite, .nav-sprite-v1 .nav-icon {
  background-image: url(https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png);
  background-position: 0 1000px;
  background-repeat: repeat-x;
}
.nav-spinner {
  background-image: url(https://m.media-amazon.com/images/G/01/javascripts/lib/popover/images/snake._CB485935611_.gif);
  background-position: center center;
  background-repeat: no-repeat;
}
.nav-timeline-icon, .nav-access-image, .nav-timeline-prime-icon {
  background-image: url(https://m.media-amazon.com/images/G/01/gno/sprites/timeline_sprite_1x._CB485945973_.png);
  background-repeat: no-repeat;
}
</style>
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41H4XraWzVL._RC|71a3cNe7BIL.css,41VtAmDG4YL.css,11OsNOdrK6L.css,11Nt6-9ZX+L.css,31IK8nB9EAL.css,31YZpDCYJPL.css,21MKjoYL8wL.css,41yQj5y2obL.css,110Nj+wUGYL.css,31OvHRW+XiL.css,01R53xsjpjL.css,11iUHDm4--L.css,415g7iDx4VL.css,01YWmXMYw8L.css_.css?AUIClients/NavDesktopUberAsset&amp;ByL3fEaj#desktop.488657-T1.427118-T3.269915-T2.551149-T1">
<!-- sp:end-feature:nav-inline-css -->
<!-- sp:feature:host-assets -->














<script>
'use strict';
(function searchOnErrorOverride () {
    
    var MSG_FILTERS = [ 
            
            [/^\s*Script error?.\s*$/, 's-script-error'],
            
            [/\w+\salready registered/, 's-already-registered-error']
        ],
        FILE_FILTERS = [ 
            
            [/^(chrome-extension|moz-extension|safari-extension):\/\//, 's-ext-error']
        ],
        original = window.onerror || function () {};
    function check (value, filters) {
        var i = 0, rx, counter;
        for (; i < filters.length; i++) {
            rx = filters[i][0];
            counter = filters[i][1];
            if (rx.test(value)) {
                ue.count(counter, (ue.count(counter) || 0) + 1);
                return true;
            }
        }
        return false;
    }
    
    function searchOnErrorWrapper (message, file, line, col, error) {
        try {
            if (ue && ue.count) { 
                if (check(message, MSG_FILTERS)) return;
                if (check(file, FILE_FILTERS)) return;
            }
        } catch (err) {}
        
        original.call(this, message, file, line, col, error);
    }
    
    searchOnErrorWrapper.skipTrace = 1;
    window.onerror = searchOnErrorWrapper;
}());
(function searchUELogErrorHandlers () {
    var FATAL = 'FATAL',
        ERROR = 'ERROR',
        
        DOWNGRADE_MSGS = ['A copy of P has already been loaded on this page.'],
        COUNTER = 's-downgraded-js-error';
    
    function downgrade(rec) {
        try {
            if (!rec) return;
            
            if (rec.logLevel !== FATAL) return;
            for (var i = 0; i < DOWNGRADE_MSGS.length; i++) {
                if (rec.m === DOWNGRADE_MSGS[i]) {
                    
                    rec.logLevel = ERROR;
                    if (ue && ue.count) {
                        ue.count(COUNTER, (ue.count(COUNTER) || 0) + 1);
                    }
                    return;
                }
            }
        } catch (err) {}
    }
    
    if (!window.ue_err) return;
    if (!window.ue_err.errorHandlers) {window.ue_err.errorHandlers = [];}
    window.ue_err.errorHandlers.push({
        name: 's-downgrade',
        handler: downgrade
    });
}());
</script>


<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01mI9NDJJTL._RC|01Hw8JIiKbL.css,11AQMRD3rsL.css,71K2D4eQgyL.css,01aTTaL5f8L.css,010ntAIO6fL.css,013Xm+zjr6L.css,41h2OmYEqwL.css,01mYUbZszyL.css,01+A2nZ3DKL.css,11IaasccbKL.css,01m4HdUj51L.css,11ABzUvcTsL.css,31nVNWpONgL.css,21vMq+Jd19L.css,01t92z-YvaL.css,01h5jb0krML.css_.css?AUIClients/SearchAssets&amp;079szpGr#556265-T1.470082-T1.592566-T1">
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01+6LDwsu8L._RC|01ixfc-7StL.css,21dv0pdmGZL.css,11oqoK-MptL.css,01+neHskhqL.css,01mfj61BPYL.css,01Luz-sfd0L.css,01CXpQgAC8L.css,21BUT35X5SL.css,01LfrrxE-KL.css,31wUat9O8SL.css,31oq6AE42vL.css,01-EZOuOkuL.css,01WwDxHvBQL.css,01uVg0XT9XL.css,01OpjCq+SSL.css,41Y5FbwH52L.css,11VKiAMd89L.css,0171-O+nBwL.css,01L7G1u+L5L.css,21K0oo63ZeL.css,01rdVnPkgmL.css,21lfAdOTDRL.css,01K0fSFz6eL.css,014eilLW+IL.css,01MU0Cb7yFL.css,017ZL57GkjL.css,01CHSSMW4hL.css_.css?AUIClients/SearchPartnerAssets&amp;UNuukQ40#us.592566-T1.483929-T1">
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/31lcFM9-DtL.css?AUIClients/DetailPageAllOffersDisplayAssets&amp;jVGJ2ERz#436403-T1">
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01tJTKp89CL._RC|21GzhyHwjOL.css,01Q-bj+2dgL.css,21Tzy7QDnmL.css,01EsS3sB+PL.css,01KekeD+C0L.css,01XR1PRX6GL.css,01SGj-l7qnL.css,11ZMJvzBqdL.css,21vMq+Jd19L.css,01M6XwEY1qL.css,718pDboA0XL.css,11s-hnAUnfL.css,01MPYXlmzdL.css,11gm9Pqo3ZL.css,01JsvXDH4cL.css,01GgmOtso9L.css,01iweABC--L.css,01PeEGXX79L.css_.css?AUIClients/ProductUIAssets&amp;a4xHKmVg#556265-T1.470082-T1.429886-T3.468961-T1">


    <script>
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/11mVszy8FIL.js?AUIClients/AmazonRushAssetLoader');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/41kCtwlCFqL.js?AUIClients/AmazonRushFramework');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/21cuxCuJB9L.js?AUIClients/AmazonRushRouter');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/11A1Q93BHbL._RC|31YYsFFQrXL.js,31Iq4x9+ecL.js,01BPbuoKVCL.js,31QAousiwfL.js,01+nIi7vQ6L.js,315IZLuJm+L.js,31+Y3z8AhgL.js,01r1r3sVlxL.js,21Ys41aj48L.js,115Ysi-lEWL.js,01XQQDMWkKL.js,012z3lMdhOL.js,11dFVWwNCJL.js,01b82LFIRTL.js,11mrFqrCmiL.js,01lGmx6mYIL.js,015CwW0puPL.js,21jeZDicdtL.js,01MsgM7hzDL.js,21dMhWokf7L.js,21FazyjPQmL.js,01FA0ZefFJL.js_.js?AUIClients/SearchAssets');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/01zKhl-DyGL._RC|21ojI99jc4L.js,41pa4zoYJAL.js,01N0G7oHRlL.js,31afBQnlthL.js,21Gn8WTjh2L.js,11viIoOEOPL.js,01PRkM1aDfL.js,21s01qABMwL.js,21wma4EBp3L.js,415m3-nSyeL.js,21p-Cc6hWJL.js,31M5iaJEqeL.js,21SubJ7cGnL.js,119j-jV1U3L.js,01yvf1weXCL.js,21O7Mwm2eJL.js,21fAUGxUxsL.js,51muTcl-zGL.js,31DHAiTy0zL.js,01ly-sHeg8L.js,31-CB6cPKmL.js,01acF69nbrL.js,31CF7mNdGYL.js,21i4Nr0pHgL.js,21zQdE9ch2L.js,21ptL48PNRL.js,11jC1BUSQzL.js,013Fzw-eTvL.js,21QnPVLIO1L.js,31i0Hd4f3IL.js,01993rJ5roL.js,011gqdvx+zL.js,01HV1B-ydIL.js,01RWIxvuYCL.js,012USBOk43L.js,01GsEhoWBNL.js,51JAs7k8KoL.js_.js?AUIClients/SearchPartnerAssets&gUuVEIJZ#us.483929-T1');
(function(r){var p=window.AmazonUIPageJS||window.P,v=p._namespace||p.attributeErrors,f=v?v("DynamicImageLoader",""):p;f.guardFatal?f.guardFatal(r)(f,window):f.execute(function(){r(f,window)})})(function(r,p,v){r.register("dynamic-image-loader",function(){function f(a,b,c){if(Array.prototype.indexOf&&a.indexOf===Array.prototype.indexOf)return a.indexOf(b,c);a&&a instanceof Array||r.error("Invalid arr passed to A.indexOfArray: "+a,"A.util","indexOfArray");c=parseInt(c,10);c=isNaN(c)?0:c;if(!isFinite(c))return-1;
for(var h=a.length;c<h;c++)if(a[c]===b)return c;return-1}function v(){var a=w.screen;return w.devicePixelRatio||(a&&a.systemXDPI&&a.logicalXDPI&&0<a.logicalXDPI?a.systemXDPI/a.logicalXDPI:1)}function B(a,b,c,h){var m=[];a&&m.push([a,(b||1).toString()]);for(a=null;null!==(a=C.exec(c||""));)3<=a.length&&m.push([a[1],a[2]]);c=[];a=[];for(b=0;b<m.length;++b){var k=m[b],D=k[0],k=k[1];if(0>f(a,k)){var t=parseFloat(k);y(t)&&(a.push(k),c.push([D,t]))}}c.sort(function(a,c){return a[1]-c[1]});for(b=0;b<c.length;++b)if(k=
c[b],k[1]>=h||b===c.length-1)return k;return null}function y(a){return!!(a&&isFinite(a)&&0<a&&10>=a)}function x(a){function b(){var l=[];if("none"!==t)return l;t="loading";if(!a||!a.length)return f(),l;for(l=0;l<a.length;++l){var g=a[l];if(g&&!g.srcset&&!g.hasAttribute("data-image-status")){var d,e=g,b=r;d={sourceDensity:null,url:null,density:null};var k=e.getAttribute("srcset")||e.getAttribute("data-image-source-set"),h=e.getAttribute("data-image-source-density");if(e.src&&(k=e.src,d.sourceDensity=
1,h)){var m=parseFloat(h);y(m)&&(d.sourceDensity=m)}e=e.srcset||e.getAttribute("srcset")||e.getAttribute("data-image-source-set");if(b=B(k,h,e,b))d.url=b[0],d.density=b[1];!d.url||d.url===g.src||d.url===g.currentSrc||d.sourceDensity&&d.density<=d.sourceDensity||(d.element=g,g.setAttribute("data-image-status","loading"),n.push(d))}}l=n.slice();n.length?(p=n.length,c()):f();return l}function c(){for(;n.length&&4>q.length;)h(n.shift())}function h(a){var g=a.element,d=new Image;d.onload=function(){g.src=
a.url;k(a)};d.onerror=function(){k(a)};d.onabort=function(){k(a)};a.image=d;q.push(a);if(g.tagName&&"div"===g.tagName.toLowerCase()&&g.parentNode){var c=g;m(g,d);a.element=g=d;d.src=a.url;c.parentNode.replaceChild(g,c)}else d.src=a.url}function m(a,c){for(var d=0;d<a.attributes.length;++d){var e=a.attributes[d];if(e&&"string"===typeof e.name&&"string"===typeof e.value&&("id"===e.name||"class"===e.name||0===e.name.indexOf("data-")||0===e.name.indexOf("aria-"))){var b=e.value;if("class"===e.name&&b&&
(b=b.replace("data-image-stub","").replace(E,"").replace(F," "),!b))continue;c.setAttribute(e.name,b)}}for(d=0;d<z.length;++d)e=z[d],b=a.getAttribute("data-image-"+e),"string"===typeof b&&c.setAttribute(e,b)}function k(a){a.image&&(a.image.onload=a.image.onerror=a.image.onabort=null);a.element.setAttribute("data-image-status","done");for(var b=0;b<q.length;++b)if(q[b]===a){q.splice(b,1);break}++u===p?f():c()}function f(){if("done"!==t){t="done";for(var a=0;a<q.length;++a){var b=q[a].element;b.onload=
b.onerror=b.onabort=null;b.removeAttribute("data-image-status");b.src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"}q=[];for(a=0;a<n.length;++a)n[a].element.removeAttribute("data-image-status");n=[]}}var t="none",r=v(),p=0,n=[],q=[],u=0;try{b()}catch(l){throw f(),l;}return{close:f}}function A(){var a=w.document;a.querySelectorAll&&!u&&(a=a.querySelectorAll("img[data-image-load]"),u=x(a))}var u=null,C=/ *([^ ]+) +([^x, ]+)x *(?:,|$)/g,z="width height alt usemap title role class".split(" "),
E=/^ +| +$/g,F=/ +/g,w=p;(function(){w.P.when("cf").execute(function(){A()})})();return{load:x,loadChildren:function(a){for(var b=[],c=0;c<a.length;++c){var h=a[c];if(h&&h.querySelectorAll)for(var h=h.querySelectorAll("[data-image-load]"),f=0;f<h.length;++f)b.push(h[f])}return x(b)},loadImages:A,cancelLoading:function(){u&&(u.close(),u=null)}}})});
(function(l){var h=window.AmazonUIPageJS||window.P,g=h._namespace||h.attributeErrors,f=g?g("GenericLatencyMeasure",""):h;f.guardFatal?f.guardFatal(l)(f,window):f.execute(function(){l(f,window)})})(function(l,h,g){(function(f,h){function q(b){function k(a){return m(a,(m(a)||0)+1)}function n(a,c){var e;f.ueLogError&&f.ueLogError(a,{logLevel:"ERROR",attribution:"doGenericPageLatencyMeasurement."+c});e="GenericLatencyMeasurement.JavascriptException";k(e);k(e+"."+c)}function p(a){return a?a.constructor===
Array?a:Array.prototype.slice.call(a):[]}function r(a){var c,e={time:-1},b;for(c=0;c<d.loadRecs.length;c++)(b=d.loadRecs[c])&&b.idx<=a&&b.time>e.time&&(e.time=b.time,e.counter=b.idx);return-1<e.time?e:g}function t(){var a,c={time:-1,counter:0,pixels:0},b,f;for(a=0;a<d.loadRecs.length;a++)(b=d.loadRecs[a])&&b.inInitialViewport&&(b.time>c.time&&(c.time=b.time),c.counter++,f=b.elem.naturalWidth,b=b.elem.naturalHeight,c.pixels+=f&&b?f*b:0);return-1<c.time?c:g}function z(){var a,c;if(!d.domReadyImages)return!1;
if(d.domReadyImagePlaceholders)for(a=0;a<d.domReadyImagePlaceholders.length;a++)if(c=d.domReadyImagePlaceholders[a]){c=b.imagePlaceholderConverter(c);if(!1===c)return!1;d.domReadyImages.push(c);d.domReadyImagePlaceholders[a]=null}d.domReadyImagePlaceholders=null;return d.domReadyImages.every(function(a,c){if(!a)return!0;if(!b.elemFilter(a))return d.domReadyImages[c]=null,!0;if(!a.complete||-1===d.startingImages.indexOf(a)&&-1===d.loadElems.indexOf(a))return!1;d.domReadyImages[c]=null;return!0})}function u(){var a;
if(!d.closed&&z()){for(a=0;a<d.loadRecs.length;a++)b.elemFilter(d.loadRecs[a].elem)||(d.loadRecs[a]=null);var c=h.documentElement,e=h.body;a={};var l,k;l=b.elemClassifier(d.loadElems,{scrollTop:f.scrollY||f.pageYOffset||c.scrollTop||e.scrollTop,scrollLeft:f.scrollX||f.pageXOffset||c.scrollLeft||e.scrollLeft,clientHeight:c.clientHeight,clientWidth:c.clientWidth,clientTop:c.clientTop||e.clientTop||0,clientLeft:c.clientLeft||e.clientLeft||0,topBound:0,bottomBound:c.clientHeight});for(c=0;c<d.loadRecs.length;c++)e=
d.loadRecs[c],k=l[c],e&&k&&(e.idx=k.idx,e.inInitialViewport=k.inInitialViewport);b.cfIdx!==g&&(a.cf=0>b.cfIdx?t():r(b.cfIdx));b.atfIdx!==g&&(a.atf=0>b.atfIdx?t():r(b.atfIdx));a.elemRecs=d.loadRecs;a.cf===g&&b.cfIdx!==g&&m("GenericLatencyMeasurement.MeasurementFailed.CF",1);a.atf===g&&b.atfIdx!==g&&m("GenericLatencyMeasurement.MeasurementFailed.ATF",1);b.measurementClosedCallback(a);d.closed=!0}}function A(a){var c;try{c=a.target,-1===d.loadElems.indexOf(c)&&(d.loadElems.push(c),d.loadRecs.push({time:+new Date,
elem:c}),b.elemLoadHandler&&b.elemLoadHandler(c),u())}catch(e){n(e,"elemLoadHandler")}}function B(a){var c=a.target;c&&"IMG"===c.tagName?k("GenericLatencyMeasurement.FailedToLoadImages"):k("GenericLatencyMeasurement.FailedToLoad");b.elemErrorHandler&&b.elemErrorHandler(a)}function v(){try{d={startingImages:p(b.parentElem.getElementsByTagName("img")),loadElems:[],loadRecs:[]}}catch(a){n(a,"resetMeasurementState")}}function w(){try{d.domReadyImages=p(b.parentElem.getElementsByTagName("img")),b.imagePlaceholderFinder&&
(d.domReadyImagePlaceholders=p(b.imagePlaceholderFinder())),u()}catch(a){n(a,"domReadyHandler")}}function x(a,c){a&&(a.call?a(c):l.when("A").execute("latency-glm-sinkCustomEvent",function(b){b.on(a,c)}))}var y,d,m;return function(){try{if(!f.ue)throw Error("GLM requires that window.ue be available before it initializes");m=m||ue.count;if(y)return m("GenericLatencyMeasurement.DuplicateInitialization",1),!1;if(!(b.parentElem&&b.elemFilter&&b.elemClassifier)||b.cfIdx===g&&b.atfIdx===g||!b.measurementClosedCallback)throw Error("One or more required attributes of the specializationArgs object is missing - not meausuring latency");
if(!b.parentElem.addEventListener)return m("GenericLatencyMeasurement.BrowserNotSupported",1),y=!0,!1;v();b.parentElem.addEventListener("load",A,!0);b.parentElem.addEventListener("error",B,!0);h.addEventListener("DOMContentLoaded",w,!1);x(b.ajaxDOMContentLoadedEvent,w);x(b.ajaxStartingEvent,v);return q.initialized=!0}catch(a){n(a,"initializer")}}()}l.declare("doGenericPageLatencyMeasurement",q)})(h,document)});
(function(h){var b=window.AmazonUIPageJS||window.P,f=b._namespace||b.attributeErrors,g=f?f("SearchDesktopPageLatencyMeasure",""):b;g.guardFatal?g.guardFatal(h)(g,window):g.execute(function(){h(g,window)})})(function(h,b,f){h.now("doGenericPageLatencyMeasurement").execute("s-doSearchDesktopPageLatencyMeasurement-kickoff",function(g){function l(a){return"number"===typeof a}function r(){var a;a=(a=t.querySelectorAll(".s-latency-cf-section IMG[data-image-latency\x3ds-product-image]"))?a.constructor===
Array?a:Array.prototype.slice.call(a):[];return a}function v(a){var c;if(!n&&(n=document.getElementById("search"),!n))return!1;for(c=a.parentElement;c&&c!==n;)c=c.parentElement;return c!==n||"IMG"!==a.tagName||a.complete&&1>=Math.min(a.naturalHeight,a.naturalWidth)?!1:!0}function w(a,c){var d,m=[],b,e,h,k;if(!a)return f;d=r();for(b=0;b<a.length;b++)if(e=a[b],"IMG"!==e.tagName)m.push(null);else{k={};m.push(k);h=d.indexOf(e);-1<h&&(k.idx=h);h=k;k=c;var g=void 0,l=void 0,g=void 0,l=!1;k&&e.parentNode&&
1<e.height&&1<e.width&&null!==e.offsetParent&&(g=e.getBoundingClientRect(),l=g.top+k.scrollTop-k.clientTop,g=g.left+k.scrollLeft-k.clientLeft,l=l<=k.clientHeight&&g<=k.clientWidth);h.inInitialViewport=l}return m}function x(a){var c,d=-1;if(!u&&"IMG"===a.tagName&&"s-product-image"===a.getAttribute("data-image-latency")){if(!e.resultImages&&(e.resultImages=r(),!e.resultImages.length)){e.resultImages=null;return}a=e.resultImages.indexOf(a);c=e.resultImages.length;12<=c?3<=a&&(d=0):8<=c?3<=a&&(d=50):
a===c-1&&(d=100);-1<d&&(setTimeout(function(){h.register("cf");h.register("af")},d),u=!0)}}function y(a){var c={},d;(d=a.cf)&&l(d.time)&&l(d.counter)&&(c.cf=d);(d=a.atf)&&l(d.time)&&l(d.counter)&&l(d.pixels)&&(c.atf=d);return c}function z(a){for(;a&&a.classList&&!a.classList.contains("s-result-item");)a=a.parentElement;a=parseInt(a&&a.getAttribute("data-index"),10);return isNaN(a)?0:a}function A(a){var c=0,d=0;a=a.elemRecs||[];var m,b;for(m=0;m<a.length;m++)(b=a[m])&&b.inInitialViewport&&b.elem&&
("s-product-image"===b.elem.getAttribute("data-image-latency")&&c++,d=Math.max(d,z(b.elem)));return{searchResultImageCount:c,lastSearchItemIndex:d}}function B(a){var c,d;d=A(a);a=y(a);if(e.isAjax)h.now("Rush").execute("s-doSearchDesktopPageLatencyMeasurement-ajaxTransferMeasurement",function(b){if(b){if(c=a.cf)b.trigger(b.metrics.EVENTS.CRITICAL_FEATURE_COMPLETE,{timeOverride:c.time}),b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.CfIdx",value:c.counter});(c=a.atf)?
(b.trigger(b.metrics.EVENTS.ABOVE_THE_FOLD_COMPLETE,{timeOverride:c.time}),b.trigger(b.metrics.EVENTS.FUNCTIONAL_COMPLETE,{timeOverride:c.time}),b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.NumInInitialViewport",value:c.counter}),b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.ThousandsPixelsInInitialViewport",value:parseInt(c.pixels/1E3,10)}),b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.NumSearchResultImagesInInitialViewport",
value:d.searchResultImageCount})):(b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.NumInInitialViewport",value:0}),b.trigger(b.metrics.EVENTS.COUNTER_READY,{counter:"Search.GenericLatencyMeasurement.ThousandsPixelsInInitialViewport",value:0}));b.trigger(b.metrics.EVENTS.LOAD_COMPLETE)}});else{if(c=a.cf)b.uet("cf",f,f,c.time),b.ue.count("Search.GenericLatencyMeasurement.CfIdx",c.counter,f);(c=a.atf)?(b.uet("af",f,f,c.time),b.uet("fn",f,f,c.time),b.ue.count("Search.GenericLatencyMeasurement.NumInInitialViewport",
c.counter,f),b.ue.count("Search.GenericLatencyMeasurement.ThousandsPixelsInInitialViewport",parseInt(c.pixels/1E3,10),f),b.ue.count("Search.GenericLatencyMeasurement.NumSearchResultImagesInInitialViewport",d.searchResultImageCount,f),b.ue.count("Search.GenericLatencyMeasurement.LastSearchItemIndexInInitialViewport",d.lastSearchItemIndex,f)):(b.ue.count("Search.GenericLatencyMeasurement.NumInInitialViewport",0,f),b.ue.count("Search.GenericLatencyMeasurement.ThousandsPixelsInInitialViewport",0,f),b.ue.tag("ZeroInViewport"))}}
function C(a){e={isAjax:a.isAjax};e.isAjax&&p&&p()}function D(){e.isAjax&&q&&q()}function E(a){p=a}function F(a){q=a}var e={},t=document,n,u,p,q;(function(){g&&b.uet&&b.ue&&b.ue.count&&b.ue.tag&&(h.when("Rush","s-web-application-controller").execute("s-desktop-latency-measure-ajaxEventSinker",function(a,b){a.on(b.ACTIONS.LOAD_SEARCH_PAGE_STARTING,C);a.on(b.ACTIONS.LOAD_SEARCH_PAGE_COMPLETE,D)}),g({parentElem:t,elemFilter:v,elemClassifier:w,atfIdx:-1,cfIdx:0,elemLoadHandler:x,measurementClosedCallback:B,
ajaxStartingEvent:E,ajaxDOMContentLoadedEvent:F}))})()})});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('af', 'ready').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/314KUnfp3+L.js?AUIClients/AllOffersDisplayIngressAssets&P3lk6dwL#368370-C');
});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('aodIngressClick').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61iG0Nufx3L.js?AUIClients/DetailPageAllOffersDisplayAssets&0kA5iGHK#language-en.436403-T1.433783-T2.403176-C.368370-C.630374-T1');
});
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/01GT6fWw-jL._RC|21jfY81shVL.js,01mbLYIbb6L.js,41NPz88sBEL.js,41uxLCy6gXL.js,11jWtxew3JL.js,017HkCEd5gL.js,21DHhna6ycL.js,21COqMqoqsL.js,01DTApdmRGL.js,11P9+f2WoeL.js,11s69IMeXSL.js,01peSwKV8mL.js,01Sdh4wVe3L.js,110ytKZKSiL.js,01SSs1udVFL.js,017MBv9t0oL.js,21L76DIvY4L.js,21fbsMlRZ+L.js,0102ySY2JzL.js,01jf6L0IuVL.js,01-0s1MjxEL.js,015FiitmhFL.js,017cIAbvZsL.js,21QT3gUErJL.js,01MJ-h1wjNL.js_.js?AUIClients/ProductUIAssets&ONiAKe2i#528635-T1.470082-T1');
</script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/11mVszy8FIL.js?AUIClients/AmazonRushAssetLoader"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/41kCtwlCFqL.js?AUIClients/AmazonRushFramework"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/21cuxCuJB9L.js?AUIClients/AmazonRushRouter"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/11A1Q93BHbL._RC|31YYsFFQrXL.js,31Iq4x9+ecL.js,01BPbuoKVCL.js,31QAousiwfL.js,01+nIi7vQ6L.js,315IZLuJm+L.js,31+Y3z8AhgL.js,01r1r3sVlxL.js,21Ys41aj48L.js,115Ysi-lEWL.js,01XQQDMWkKL.js,012z3lMdhOL.js,11dFVWwNCJL.js,01b82LFIRTL.js,11mrFqrCmiL.js,01lGmx6mYIL.js,015CwW0puPL.js,21jeZDicdtL.js,01MsgM7hzDL.js,21dMhWokf7L.js,21FazyjPQmL.js,01FA0ZefFJL.js_.js?AUIClients/SearchAssets"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/01zKhl-DyGL._RC|21ojI99jc4L.js,41pa4zoYJAL.js,01N0G7oHRlL.js,31afBQnlthL.js,21Gn8WTjh2L.js,11viIoOEOPL.js,01PRkM1aDfL.js,21s01qABMwL.js,21wma4EBp3L.js,415m3-nSyeL.js,21p-Cc6hWJL.js,31M5iaJEqeL.js,21SubJ7cGnL.js,119j-jV1U3L.js,01yvf1weXCL.js,21O7Mwm2eJL.js,21fAUGxUxsL.js,51muTcl-zGL.js,31DHAiTy0zL.js,01ly-sHeg8L.js,31-CB6cPKmL.js,01acF69nbrL.js,31CF7mNdGYL.js,21i4Nr0pHgL.js,21zQdE9ch2L.js,21ptL48PNRL.js,11jC1BUSQzL.js,013Fzw-eTvL.js,21QnPVLIO1L.js,31i0Hd4f3IL.js,01993rJ5roL.js,011gqdvx+zL.js,01HV1B-ydIL.js,01RWIxvuYCL.js,012USBOk43L.js,01GsEhoWBNL.js,51JAs7k8KoL.js_.js?AUIClients/SearchPartnerAssets&amp;gUuVEIJZ#us.483929-T1"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/01GT6fWw-jL._RC|21jfY81shVL.js,01mbLYIbb6L.js,41NPz88sBEL.js,41uxLCy6gXL.js,11jWtxew3JL.js,017HkCEd5gL.js,21DHhna6ycL.js,21COqMqoqsL.js,01DTApdmRGL.js,11P9+f2WoeL.js,11s69IMeXSL.js,01peSwKV8mL.js,01Sdh4wVe3L.js,110ytKZKSiL.js,01SSs1udVFL.js,017MBv9t0oL.js,21L76DIvY4L.js,21fbsMlRZ+L.js,0102ySY2JzL.js,01jf6L0IuVL.js,01-0s1MjxEL.js,015FiitmhFL.js,017cIAbvZsL.js,21QT3gUErJL.js,01MJ-h1wjNL.js_.js?AUIClients/ProductUIAssets&amp;ONiAKe2i#528635-T1.470082-T1"></script>

    <script>
P.when('rush-asset-loader').execute('rush-manifest-registration', function (ral) {
    ral.addManifest({"name":"AmazonRushAssetLoader","fingerprint":"79A06FC031676792F019ECEB41D0719078AC3CF2"});
    ral.addManifest( {"name":"AmazonRushFramework","fingerprint":"7E24E7E167B3CE1299EEDF1727468C556B411830"});
    ral.addManifest( {"name":"AmazonRushRouter","fingerprint":"EEB15E30F28E95E7CA883B2E72FC6510A9B76096"});
});
</script>
    
    <script>P.declare('s\-glux\-widget\-refresh', null);</script>




<title>Amazon.com : bookstore amazon</title>


<!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-assets -->
<!-- sp:feature:csm:head-close -->
<script type="text/javascript">
window.ue_ihe = (window.ue_ihe || 0) + 1;
if (window.ue_ihe === 1) {
(function(c){c&&1===c.ue_jsmtf&&"object"===typeof c.P&&"function"===typeof c.P.when&&c.P.when("mshop-interactions").execute(function(e){"object"===typeof e&&"function"===typeof e.addListener&&e.addListener(function(b){"object"===typeof b&&"ORIGIN"===b.dataSource&&"number"===typeof b.clickTime&&"object"===typeof b.events&&"number"===typeof b.events.pageVisible&&(c.ue_jsmtf_interaction={pv:b.events.pageVisible,ct:b.clickTime})})})})(ue_csm);
(function(c,e,b){function m(a){f||(f=d[a.type].id,"undefined"===typeof a.clientX?(h=a.pageX,k=a.pageY):(h=a.clientX,k=a.clientY),2!=f||l&&(l!=h||n!=k)?(r(),g.isl&&e.setTimeout(function(){p("at",g.id)},0)):(l=h,n=k,f=0))}function r(){for(var a in d)d.hasOwnProperty(a)&&g.detach(a,m,d[a].parent)}function s(){for(var a in d)d.hasOwnProperty(a)&&g.attach(a,m,d[a].parent)}function t(){var a="";!q&&f&&(q=1,a+="&ui="+f);return a}var g=c.ue,p=c.uex,q=0,f=0,l,n,h,k,d={click:{id:1,parent:b},mousemove:{id:2,
parent:b},scroll:{id:3,parent:e},keydown:{id:4,parent:b}};g&&p&&(s(),g._ui=t)})(ue_csm,window,document);


(function(s,l){function m(b,e,c){c=c||new Date(+new Date+t);c="expires="+c.toUTCString();n.cookie=b+"="+e+";"+c+";path=/"}function p(b){b+="=";for(var e=n.cookie.split(";"),c=0;c<e.length;c++){for(var a=e[c];" "==a.charAt(0);)a=a.substring(1);if(0===a.indexOf(b))return decodeURIComponent(a.substring(b.length,a.length))}return""}function q(b,e,c){if(!e)return b;-1<b.indexOf("{")&&(b="");for(var a=b.split("&"),f,d=!1,h=!1,g=0;g<a.length;g++)f=a[g].split(":"),f[0]==e?(!c||d?a.splice(g,1):(f[1]=c,a[g]=
f.join(":")),h=d=!0):2>f.length&&(a.splice(g,1),h=!0);h&&(b=a.join("&"));!d&&c&&(0<b.length&&(b+="&"),b+=e+":"+c);return b}var k=s.ue||{},t=3024E7,n=ue_csm.document||l.document,r=null,d;a:{try{d=l.localStorage;break a}catch(u){}d=void 0}k.count&&k.count("csm.cookieSize",document.cookie.length);k.cookie={get:p,set:m,updateCsmHit:function(b,e,c){try{var a;if(!(a=r)){var f;a:{try{if(d&&d.getItem){f=d.getItem("csm-hit");break a}}catch(k){}f=void 0}a=f||p("csm-hit")||"{}"}a=q(a,b,e);r=a=q(a,"t",+new Date);
try{d&&d.setItem&&d.setItem("csm-hit",a)}catch(h){}m("csm-hit",a,c)}catch(g){"function"==typeof l.ueLogError&&ueLogError(Error("Cookie manager: "+g.message),{logLevel:"WARN"})}}}})(ue_csm,window);


(function(l,e){function c(b){b="";var c=a.isBFT?"b":"s",d=""+a.oid,g=""+a.lid,h=d;d!=g&&20==g.length&&(c+="a",h+="-"+g);a.tabid&&(b=a.tabid+"+");b+=c+"-"+h;b!=f&&100>b.length&&(f=b,a.cookie?a.cookie.updateCsmHit(m,b+("|"+ +new Date)):e.cookie="csm-hit="+b+("|"+ +new Date)+n+"; path=/")}function p(){f=0}function d(b){!0===e[a.pageViz.propHid]?f=0:!1===e[a.pageViz.propHid]&&c({type:"visible"})}var n="; expires="+(new Date(+new Date+6048E5)).toGMTString(),m="tb",f,a=l.ue||{},k=a.pageViz&&a.pageViz.event&&
a.pageViz.propHid;a.attach&&(a.attach("click",c),a.attach("keyup",c),k||(a.attach("focus",c),a.attach("blur",p)),k&&(a.attach(a.pageViz.event,d,e),d({})));a.aftb=1})(ue_csm,ue_csm.document);


ue_csm.ue.stub(ue,"impression");


ue.stub(ue,"trigger");


if(window.ue&&uet) { uet('bb'); }

}
</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 3172)</script>
<!-- sp:end-feature:csm:head-close -->
<!-- sp:feature:head-close -->
<script>
window.P && P.register('bb');
if (typeof ues === 'function') {
  ues('t0', 'portal-bb', new Date());
  ues('ctb', 'portal-bb', 1);
}
</script>
<script type="text/javascript" async="" charset="utf-8" src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.f6332db.js?csm_attribution=APE-SafeFrame" crossorigin="anonymous"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/11-OOS888GL.js?xcp"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://m.media-amazon.com/images/I/61ZS63EQSsL.js?AUIClients/AmazonUIjQuery"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://m.media-amazon.com/images/I/11Y+5x+kkTL._RC|51Am7NcREVL.js,11yKORv-GTL.js,11GgN1+C7hL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,516j7qaWchL.js,11kWu3cNjYL.js,11wr1I7-WYL.js,11OREnu1epL.js,11Wm6BwZ+6L.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31nfKXylf6L.js,01ezj5Rkz1L.js,11bEz2VIYrL.js,31o2NGTXThL.js,01rpauTep4L.js,01XC3MnuvfL.js_.js?AUIClients/AmazonUI&amp;MFdCk5El#567364-T1.432724-T1.577970-T1"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://m.media-amazon.com/images/I/51EIwpasq4L.js?AUIClients/CardJsRuntimeBuzzCopyBuild"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/412HK5CgpXL._RC|71mLbqg5g8L.js,01QvReFeJyL.js,01phmzCOwJL.js,01eOvPdxG7L.js,717Oay18SNL.js,41gNKoK0s7L.js,115pV8Rl02L.js,01+pnQJuQ0L.js,21rDHgaooIL.js,41rU9l+NGKL.js,51t-JTxfnwL.js,317BC63dC8L.js,11lEMI5MhIL.js,31UsGkeqBUL.js,01LEzWzrPZL.js,01AqeWA7PKL.js_.js?AUIClients/NavDesktopUberAsset&amp;E09Bu59x#desktop.language-en.us.488400-T1.488413-T1.375680-T1.479940-T1.455533-T1.432287-T1.420134-T1.366740-T1.551149-T1"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/314KUnfp3+L.js?AUIClients/AllOffersDisplayIngressAssets&amp;P3lk6dwL#368370-C"></script><style></style></head><!-- sp:end-feature:head-close -->
<!-- sp:feature:start-body -->
<body class="a-m-us a-aui_72554-c a-aui_accordion_a11y_role_354025-t1 a-aui_killswitch_csa_logger_372963-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate"><div id="a-page"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;a-wlab-states&quot;}">{"AUI_TNR_V2_180836":"C","AUI_ACCORDION_A11Y_ROLE_354025":"T1","AUI_PRELOAD_261698":"C","AUI_TEMPLATE_WEBLAB_CACHE_333406":"C","AUI_72554":"C","AUI_KILLSWITCH_CSA_LOGGER_372963":"C","AUI_REL_NOREFERRER_NOOPENER_309527":"C","AUI_PCI_RISK_BANNER_210084":"C"}</script><script>typeof uex === 'function' && uex('ld', 'portal-bb', {wb: 1})</script><!-- sp:end-feature:start-body -->
<!-- sp:feature:csm:body-open -->


<script>
!function(){function n(n,t){var r=i(n);return t&&(r=r("instance",t)),r}var r=[],c=0,i=function(t){return function(){var n=c++;return r.push([t,[].slice.call(arguments,0),n,{time:Date.now()}]),i(n)}};n._s=r,this.csa=n}();;
csa('Config', {"ContentInteractionsSummary.FlushInterval":5000});
if (window.csa) {
    csa("Config", {
        'Application': 'Retail:Prod:www.amazon.com',
        'Events.Namespace': 'csa',
        'ObfuscatedMarketplaceId': 'ATVPDKIKX0DER',
        'Events.SushiEndpoint': 'https://unagi.amazon.com/1/events/com.amazon.csm.csa.prod',
        'CacheDetection.RequestID': "BNJYY9EBY54VZZF6X4X6",
        'CacheDetection.Callback': window.ue && ue.reset,
        'LCP.elementDedup': 1
    });

    csa("Events")("setEntity", {
        page: {requestId: "BNJYY9EBY54VZZF6X4X6", meaningful: "interactive"},
        session: {id: "139-5329492-5095613"}
    });
}
!function(r){var i,e,o="splice",u=r.csa,f={},c={},a=r.csa._s,s=0,l=0,g=-1,h={},v={},d={},n=Object.keys,p=function(){};function t(n,t){return u(n,t)}function m(n,t){var r=c[n]||{};k(r,t),c[n]=r,l++,S(U,0)}function w(n,t,r){var i=!0;return t=D(t),r&&r.buffered&&(i=(d[n]||[]).every(function(n){return!1!==t(n)})),i?(h[n]||(h[n]=[]),h[n].push(t),function(){!function(n,t){var r=h[n];r&&r[o](r.indexOf(t),1)}(n,t)}):p}function b(n,t){if(t=D(t),n in v)return t(v[n]),p;return w(n,function(n){return t(n),!1})}function y(n,t){if(u("Errors")("logError",n),f.DEBUG)throw t||n}function E(){return Math.abs(4294967295*Math.random()|0).toString(36)}function D(n,t){return function(){try{return n.apply(this,arguments)}catch(n){y(n.message||n,n)}}}function S(n,t){return r.setTimeout(D(n),t)}function U(){for(var n=0;n<a.length;){var t=a[n],r=t[0]in c;if(!r&&!e)return void(s=t.length);r?(a[o](s=n,1),I(t)):n++}g=l}function I(n){var arguments,t=c[n[0]],r=(arguments=n[1])[0];if(!t||!t[r])return y("Undefined function: "+t+"/"+r);i=n[3],c[n[2]]=t[r].apply(t,arguments.slice(1))||{},i=0}function O(){e=1,U()}function k(t,r){n(r).forEach(function(n){t[n]=r[n]})}b("$beforeunload",O),m("Config",{instance:function(n){k(f,n)}}),u.plugin=D(function(n){n(t)}),t.config=f,t.register=m,t.on=w,t.once=b,t.blank=p,t.emit=function(n,t,r){for(var i=h[n]||[],e=0;e<i.length;)!1===i[e](t)?i[o](e,1):e++;v[n]=t||{},r&&r.buffered&&(d[n]||(d[n]=[]),100<=d[n].length&&d[n].shift(),d[n].push(t||{}))},t.UUID=function(){return[E(),E(),E(),E()].join("-")},t.time=function(n){var t=i?new Date(i.time):new Date;return"ISO"===n?t.toISOString():t.getTime()},t.error=y,t.warn=function(n,t){if(u("Errors")("logWarn",n),f.DEBUG)throw t||n},t.exec=D,t.timeout=S,t.interval=function(n,t){return r.setInterval(D(n),t)},(t.global=r).csa._s.push=function(n){n[0]in c&&(!a.length||e)?(I(n),a.length&&g!==l&&U()):a[o](s++,0,n)},U(),S(function(){S(O,f.SkipMissingPluginsTimeout||5e3)},1)}("undefined"!=typeof window?window:global);csa.plugin(function(o){var f="addEventListener",e="requestAnimationFrame",t=o.exec,r=o.global,u=o.on;o.raf=function(n){if(r[e])return r[e](t(n))},o.on=function(n,e,t,r){if(n&&"function"==typeof n[f]){var i=o.exec(t);return n[f](e,i,r),function(){n.removeEventListener(e,i,r)}}return"string"==typeof n?u(n,e,t,r):o.blank}});csa.plugin(function(o){var t,n,r={},e="localStorage",c="sessionStorage",a="local",i="session",u=o.exec;function s(e,t){var n;try{r[t]=!!(n=o.global[e]),n=n||{}}catch(e){r[t]=!(n={})}return n}function f(){t=t||s(e,a),n=n||s(c,i)}function l(e){return e&&e[i]?n:t}o.store=u(function(e,t,n){f();var o=l(n);return e?t?void(o[e]=t):o[e]:Object.keys(o)}),o.storageSupport=u(function(){return f(),r}),o.deleteStored=u(function(e,t){f();var n=l(t);if("function"==typeof e)for(var o in n)n.hasOwnProperty(o)&&e(o,n[o])&&delete n[o];else delete n[e]})});csa.plugin(function(n){n.types={ovl:function(n){var r=[];if(n)for(var i in n)n.hasOwnProperty(i)&&r.push(n[i]);return r}}});csa.plugin(function(i){function e(n){return function(e){i("Metrics",{producerId:"csa",dimensions:{message:e}})("recordMetric",n,1)}}function n(r){var o,t,l=i("Events",{producerId:r.producerId}),u=["name","type","csm","adb"],c={url:"pageURL",file:"f",line:"l",column:"c"};this.log=function(e){if(!function(e){if(!e)return!0;for(var n in e)return!1;return!0}(e)){var n=r.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};l("log",function(n){return o=i.UUID(),t={messageId:o,schemaId:r.schemaId||"<ns>.Error.4",errorMessage:n.m||null,attribution:n.attribution||null,logLevel:"FATAL",url:null,file:null,line:null,column:null,stack:n.s||[],context:{},surfaceInfo:{}},n.logLevel&&(t.logLevel=""+n.logLevel),u.forEach(function(e){n[e]&&(t.context[e]=n[e])}),"INFO"===n.logLevel||Object.keys(c).forEach(function(e){"number"!=typeof n[c[e]]&&"string"!=typeof n[c[e]]||(t[e]=""+n[c[e]])}),t}(e),n)}}}i.register("Errors",{instance:function(e){return new n(e||{})},logError:e("jsError"),logWarn:e("jsWarn")})});csa.plugin(function(o){var r,e,n,t,a,i="function",u="willDisappear",f="$app.",p="$document.",c="focus",s="blur",d="active",l="resign",$=o.global,b=o.exec,m=o.config["Transport.AnonymizeRequests"]||!1,g=o("Events"),h=$.location,v=$.document||{},y=$.P||{},P=(($.performance||{}).navigation||{}).type,w=o.on,k=o.emit,E=v.hidden,T={};h&&v&&(w($,"beforeunload",D),w($,"pagehide",D),w(v,"visibilitychange",R(p,function(){return v.visibilityState||"unknown"})),w(v,c,R(p+c)),w(v,s,R(p+s)),y.when&&y.when("mash").execute(function(e){e&&(w(e,"appPause",R(f+"pause")),w(e,"appResume",R(f+"resume")),R(f+"deviceready")(),$.cordova&&$.cordova.platformId&&R(f+cordova.platformId)(),w(v,d,R(f+d)),w(v,l,R(f+l)))}),e=$.app||{},n=b(function(){k(f+"willDisappear"),D()}),a=typeof(t=e[u])==i,e[u]=b(function(){n(),a&&t()}),$.app||($.app=e),"complete"===v.readyState?A():w($,"load",A),E?S():x(),o.on("$app.blur",S),o.on("$app.focus",x),o.on("$document.blur",S),o.on("$document.focus",x),o.on("$document.hidden",S),o.on("$document.visible",x),o.register("SPA",{newPage:I}),I({transitionType:{0:"hard",1:"refresh",2:"back-button"}[P]||"unknown"}));function I(n,e){var t=!!r,a=(e=e||{}).keepPageAttributes;t&&(k("$beforePageTransition"),k("$pageTransition")),t&&!a&&g("removeEntity","page"),r=o.UUID(),a?T.id=r:T={schemaId:"<ns>.PageEntity.1",id:r,url:m?h.href.split("?")[0]:h.href,server:h.hostname,path:h.pathname,referrer:m?v.referrer.split("?")[0]:v.referrer,title:v.title},Object.keys(n||{}).forEach(function(e){T[e]=n[e]}),g("setEntity",{page:T}),k("$pageChange",T,{buffered:1}),t&&k("$afterPageTransition")}function A(){k("$load"),k("$ready"),k("$afterload")}function D(){k("$ready"),k("$beforeunload"),k("$unload"),k("$afterunload")}function S(){E||(k("$visible",!1,{buffered:1}),E=!0)}function x(){E&&(k("$visible",!0,{buffered:1}),E=!1)}function R(n,t){return b(function(){var e=typeof t==i?n+t():n;k(e)})}});csa.plugin(function(c){var e="Events",t="UNKNOWN",s="id",a="all",n="messageId",i="timestamp",u="producerId",o="application",r="obfuscatedMarketplaceId",f="entities",d="schemaId",l="version",p="attributes",v="<ns>",g="session",h=c.config,m=(c.global.location||{}).host,y=h[e+".Namespace"]||"csa_other",I=h.Application||"Other"+(m?":"+m:""),b=h["Transport.AnonymizeRequests"]||!1,O=c("Transport"),E={},U=function(e,t){Object.keys(e).forEach(t)};function A(n,i,o){U(i,function(e){var t=o===a||(o||{})[e];e in n||(n[e]={version:1,id:i[e][s]||c.UUID()}),N(n[e],i[e],t)})}function N(t,n,i){U(n,function(e){!function(e,t,n){return"string"!=typeof t&&e!==l?c.error("Attribute is not of type string: "+e):!0===n||1===n||(e===s||!!~(n||[]).indexOf(e))}(e,n[e],i)||(t[e]=n[e])})}function S(o,e,r){U(e,function(e){var t=o[e];if(t[d]){var n={},i={};n[s]=t[s],n[u]=t[u]||r,n[d]=t[d],n[l]=t[l]++,n[p]=i,k(n),N(i,t,1),w(i),O("log",n)}})}function k(e){e[i]=function(e){return"number"==typeof e&&(e=new Date(e).toISOString()),e||c.time("ISO")}(e[i]),e[n]=e[n]||c.UUID(),e[o]=I,e[r]=h.ObfuscatedMarketplaceId||t,e[d]=e[d].replace(v,y)}function w(e){delete e[l],delete e[d],delete e[u]}function D(o){var r={};this.log=function(e,t){var n={},i=(t||{}).ent;return e?"string"!=typeof e[d]?c.error("A valid schema id is required for the event"):(k(e),A(n,E,i),A(n,r,i),A(n,e[f]||{},i),U(n,function(e){w(n[e])}),e[u]=o[u],e[f]=n,void O("log",e,t)):c.error("The event cannot be undefined")},this.setEntity=function(e){b&&delete e[g],A(r,e,a),S(r,e,o[u])}}h["KillSwitch."+e]||c.register(e,{setEntity:function(e){b&&delete e[g],A(E,e,a),S(E,e,"csa")},removeEntity:function(e){delete E[e]},instance:function(e){return new D(e)}})});csa.plugin(function(s){var c,g="Transport",l="post",f="preflight",r="csa.cajun.",i="store",a="deleteStored",u="sendBeacon",t="__merge",e="messageId",n=".FlushInterval",o=0,d=s.config[g+".BufferSize"]||2e3,h=s.config[g+".RetryDelay"]||1500,p=s.config[g+".AnonymizeRequests"]||!1,v={},y=0,m=[],E=s.global,R=E.document,b=s.timeout,k=E.Object.keys,w=s.config[g+n]||5e3,I=w,O=s.config[g+n+".BackoffFactor"]||1,S=s.config[g+n+".BackoffLimit"]||3e4,B=0;function T(n){if(864e5<s.time()-+new Date(n.timestamp))return s.warn("Event is too old: "+n);y<d&&(n[e]in v||(v[n[e]]=n,y++),"function"==typeof n[t]&&n[t](v[n[e]]),!B&&o&&(B=b(q,function(){var n=I;return I=Math.min(n*O,S),n}())))}function q(){m.forEach(function(e){var o=[];k(v).forEach(function(n){var t=v[n];e.accepts(t)&&o.push(t)}),o.length&&(e.chunks?e.chunks(o).forEach(function(n){D(e,n)}):D(e,o))}),v={},B=0}function D(t,e){function o(){s[a](r+n)}var n=s.UUID();s[i](r+n,JSON.stringify(e)),[function(n,t,e){var o=E.navigator||{},r=E.cordova||{};if(p)return 0;if(!o[u]||!n[l])return 0;n[f]&&r&&"ios"===r.platformId&&!c&&((new Image).src=n[f]().url,c=1);var i=n[l](t);if(!i.type&&o[u](i.url,i.body))return e(),1},function(n,t,e){if(!n[l])return 0;var o=n[l](t),r=o.url,i=o.body,c=o.type,f=new XMLHttpRequest,a=0;function u(n,t,e){f.open("POST",n),f.withCredentials=!p,e&&f.setRequestHeader("Content-Type",e),f.send(t)}return f.onload=function(){f.status<299?e():s.config[g+".XHRRetries"]&&a<3&&b(function(){u(r,i,c)},++a*h)},u(r,i,c),1}].some(function(n){try{return n(t,e,o)}catch(n){}})}k&&(s.once("$afterload",function(){o=1,function(e){(s[i]()||[]).forEach(function(n){if(!n.indexOf(r))try{var t=s[i](n);s[a](n),JSON.parse(t).forEach(e)}catch(n){s.error(n)}})}(T),s.on(R,"visibilitychange",q,!1),q()}),s.once("$afterunload",function(){o=1,q()}),s.on("$afterPageTransition",function(){y=0,I=w}),s.register(g,{log:T,register:function(n){m.push(n)}}))});csa.plugin(function(n){var r=n.config["Events.SushiEndpoint"];n("Transport")("register",{accepts:function(n){return n.schemaId},post:function(n){var t=n.map(function(n){return{data:n}});return{url:r,body:JSON.stringify({events:t})}},preflight:function(){var n,t=/\/\/(.*?)\//.exec(r);return t&&t[1]&&(n="https://"+t[1]+"/ping"),{url:n}},chunks:function(n){for(var t=[];500<n.length;)t.push(n.splice(0,500));return t.push(n),t}})});csa.plugin(function(n){var t,a,o,r,e=n.config,i="PageViews",d=e[i+".ImpressionMinimumTime"]||1e3,s="hidden",c="innerHeight",g="innerWidth",l="renderedTo",f=l+"Viewed",m=l+"Meaningful",u=l+"Impressed",p=1,v=2,h=3,w=4,y=5,P="loaded",I=7,T=8,b=n.global,E=n.on,V=n("Events",{producerId:"csa"}),$=b.document,M={},S={},H=y;function K(e){if(!M[I]){var i;if(M[e]=n.time(),e!==h&&e!==P||(t=t||M[e]),t&&H===w)a=a||M[e],(i={})[m]=t-o,i[f]=a-o,R("PageView.4",i),r=r||n.timeout(j,d);if(e!==y&&e!==p&&e!==v||(clearTimeout(r),r=0),e!==p&&e!==v||R("PageRender.3",{transitionType:e===p?"hard":"soft"}),e===I)(i={})[m]=t-o,i[f]=a-o,i[u]=M[e]-o,R("PageImpressed.2",i)}}function R(e,i){S[e]||(i.schemaId="<ns>."+e,V("log",i,{ent:"all"}),S[e]=1)}function W(){0===b[c]&&0===b[g]?(H=T,n("Events")("setEntity",{page:{viewport:"hidden-iframe"}})):H=$[s]?y:w,K(H)}function j(){K(I),r=0}function k(){var e=o?v:p;M={},S={},a=t=0,o=n.time(),K(e),W()}function q(){var e=$.readyState;"interactive"===e&&K(h),"complete"===e&&K(P)}e["KillSwitch."+i]||($&&void 0!==$[s]?(k(),E($,"visibilitychange",W,!1),E($,"readystatechange",q,!1),E("$afterPageTransition",k),E("$timing:loaded",q),n.once("$load",q)):n.warn("Page visibility not supported"))});csa.plugin(function(c){var s=c.config["Interactions.ParentChainLength"]||35,e="click",r="touches",f="timeStamp",o="length",u="pageX",g="pageY",p="pageXOffset",h="pageYOffset",m=250,v=5,d=200,l=.5,t={capture:!0,passive:!0},X=c.global,Y=c.emit,n=c.on,x=X.Math.abs,a=(X.document||{}).documentElement||{},y={x:0,y:0,t:0,sX:0,sY:0},N={x:0,y:0,t:0,sX:0,sY:0};function b(t){if(t.id)return"//*[@id='"+t.id+"']";var e=function(t){var e,n=1;for(e=t.previousSibling;e;e=e.previousSibling)e.nodeName===t.nodeName&&(n+=1);return n}(t),n=t.nodeName;return 1!==e&&(n+="["+e+"]"),t.parentNode&&(n=b(t.parentNode)+"/"+n),n}function I(t,e,n){var a=c("Content",{target:n}),i={schemaId:"<ns>.ContentInteraction.1",interaction:t,interactionData:e,messageId:c.UUID()};if(n){var r=b(n);r&&(i.attribution=r);var o=function(t){for(var e=t,n=e.tagName,a=!1,i=t?t.href:null,r=0;r<s;r++){if(!e||!e.parentElement){a=!0;break}n=(e=e.parentElement).tagName+"/"+n,i=i||e.href}return a||(n=".../"+n),{pc:n,hr:i}}(n);o.pc&&(i.interactionData.parentChain=o.pc),o.hr&&(i.interactionData.href=o.hr)}a("log",i),Y("$content.interaction",i)}function i(t){I(e,{interactionX:""+t.pageX,interactionY:""+t.pageY},t.target)}function C(t){if(t&&t[r]&&1===t[r][o]){var e=t[r][0];N=y={e:t.target,x:e[u],y:e[g],t:t[f],sX:X[p],sY:X[h]}}}function D(t){if(t&&t[r]&&1===t[r][o]&&y&&N){var e=t[r][0],n=t[f],a=n-N.t,i={e:t.target,x:e[u],y:e[g],t:n,sX:X[p],sY:X[h]};N=i,d<=a&&(y=i)}}function E(t){if(t){var e=x(y.x-N.x),n=x(y.y-N.y),a=x(y.sX-N.sX),i=x(y.sY-N.sY),r=t[f]-y.t;if(m<1e3*e/r&&v<e||m<1e3*n/r&&v<n){var o=n<e;o&&a&&e*l<=a||!o&&i&&n*l<=i||I((o?"horizontal":"vertical")+"-swipe",{interactionX:""+y.x,interactionY:""+y.y,endX:""+N.x,endY:""+N.y},y.e)}}}n(a,e,i,t),n(a,"touchstart",C,t),n(a,"touchmove",D,t),n(a,"touchend",E,t)});csa.plugin(function(r){var a,o,t,e="MutationObserver",c="observe",n="disconnect",s="mutObs",f="_csa_flt",l="_csa_llt",b="_csa_mr",d="_csa_mi",m="lastChild",p="length",_={childList:!0,subtree:!0},g=10,h=4,u=r.global,i=u.document,v=i.body||i.documentElement,y=Date.now,O=[],k=[],w=[],L=0,B=0,I=0,M=1,Y=[],$=[],x=0,A=r.blank,C={buffered:1},D=0;function E(e){r.global.ue_csa_ss_tag||r.emit("$csmTag:"+e,0,C)}y&&u[e]?(E(s+"Yes"),L=0,o=new u[e](N),(t=new u[e](F))[c](v,{attributes:!0,subtree:!0,attributeFilter:["src"],attributeOldValue:!0}),A=r.on(u,"scroll",S,{passive:!0}),r.once("$ready",V),M&&T(),r.register("SpeedIndexBuffers",{getBuffers:function(e){e&&(V(),S(),e(L,Y,O,k,w),o&&o[n](),t&&t[n](),A())},registerListener:function(e){a=e},replayModuleIsLive:function(){r.raf(V)}})):E(s+"No");function F(e){O.push({t:y(),m:e})}function N(e){k.push({t:y(),m:e}),D||E(s+"Active"),D=I=1,a&&a()}function S(){I&&(w.push({t:y(),y:B}),B=u.pageYOffset,I=0)}function T(){for(var e=v,t=y(),n=[],s=[],u=0,i=0;e;)e[f]?++u:(e[f]=t,n.push(e),i=1),s[p]<h&&s.push(e),e[d]=x,e[l]=t,e=e[m];i&&(u<$[p]&&function(e){for(var t=e,n=$[p];t<n;t++){var s=$[t];if(s){if(s[b])break;if(s[d]<x){s[b]=1,o[c](s,_);break}}}}(u),$=s,Y.push({t:t,m:n}),++x,I=i,a&&a()),M&&(i?r.raf(T):r.timeout(T,g))}function V(){M&&(M=0,T(),o[c](v,_))}});

var ue_csa_ss_tag = false;
csa.plugin(function(b){var a=b.global,e=a.uet,f=a.uex,c=a.ue,d=a.Object,g={largestContentfulPaint:"lcp",speedIndex:"si",atfSpeedIndex:"atfsi",visuallyLoaded50:"vl50",visuallyLoaded90:"vl90",visuallyLoaded100:"vl100"},k="perfNo perfYes browserQuiteFn browserQuiteUd browserQuiteLd browserQuiteMut mutObsNo mutObsYes mutObsActive startVL endVL".split(" ");b&&e&&f&&d.keys&&c&&(d.keys(g).forEach(function(h){b.on("$timing:"+h,function(a){var b=g[h];if(c.isl){var d="csa:"+b;e(b,d,void 0,a);f("at",d)}else e(b,
void 0,void 0,a)})}),a.ue_csa_ss_tag||k.forEach(function(a){b.on("$csmTag:"+a,function(){c.tag&&c.tag(a);c.isl&&f("at","csa:"+a)},{buffered:1})}))});

</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 15802)</script>
<!-- sp:end-feature:csm:body-open -->
<!-- sp:feature:nav-inline-js -->
<!-- NAVYAAN JS -->

<script type="text/javascript">!function(n){function e(n,e){return{m:n,a:function(n){return[].slice.call(n)}(e)}}document.createElement("header");var r=function(n){function u(n,r,u){n[u]=function(){a._replay.push(r.concat(e(u,arguments)))}}var a={};return a._sourceName=n,a._replay=[],a.getNow=function(n,e){return e},a.when=function(){var n=[e("when",arguments)],r={};return u(r,n,"run"),u(r,n,"declare"),u(r,n,"publish"),u(r,n,"build"),r.depends=n,r.iff=function(){var r=n.concat([e("iff",arguments)]),a={};return u(a,r,"run"),u(a,r,"declare"),u(a,r,"publish"),u(a,r,"build"),a},r},u(a,[],"declare"),u(a,[],"build"),u(a,[],"publish"),u(a,[],"importEvent"),r._shims.push(a),a};r._shims=[],n.$Nav||(n.$Nav=r("rcx-nav")),n.$Nav.make||(n.$Nav.make=r)}(window)</script><script type="text/javascript">
$Nav.importEvent('navbarJS-beaconbelt');
$Nav.declare('img.sprite', {
  'png32': 'https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png',
  'png32-2x': 'https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-2x-hm-dsk-reorg._CB405937547_.png'
});
$Nav.declare('img.timeline', {
  'timeline-icon-2x': 'https://m.media-amazon.com/images/G/01/gno/sprites/timeline_sprite_2x._CB443581191_.png'
});
window._navbarSpriteUrl = 'https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png';
$Nav.declare('img.pixel', 'https://m.media-amazon.com/images/G/01/x-locale/common/transparent-pixel._CB485935036_.gif');
</script>

<img src="https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png" style="display:none" alt="">
<script type="text/javascript">var nav_t_after_preload_sprite = + new Date();</script>
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/412HK5CgpXL._RC|71mLbqg5g8L.js,01QvReFeJyL.js,01phmzCOwJL.js,01eOvPdxG7L.js,717Oay18SNL.js,41gNKoK0s7L.js,115pV8Rl02L.js,01+pnQJuQ0L.js,21rDHgaooIL.js,41rU9l+NGKL.js,51t-JTxfnwL.js,317BC63dC8L.js,11lEMI5MhIL.js,31UsGkeqBUL.js,01LEzWzrPZL.js,01AqeWA7PKL.js_.js?AUIClients/NavDesktopUberAsset&E09Bu59x#desktop.language-en.us.488400-T1.488413-T1.375680-T1.479940-T1.455533-T1.432287-T1.420134-T1.366740-T1.551149-T1');
});
</script>
<!-- sp:end-feature:nav-inline-js -->
<!-- sp:feature:nav-skeleton -->
<!-- sp:end-feature:nav-skeleton -->
<!-- sp:feature:navbar -->

<!--Pilu -->


  <!-- NAVYAAN -->











<!-- navmet initial definition -->



<script type="text/javascript">
    if(window.navmet===undefined) {
      window.navmet=[];
      if (window.performance && window.performance.timing && window.ue_t0) {
        var t = window.performance.timing;
        var now = + new Date();
        window.navmet.basic = {
          'networkLatency': (t.responseStart - t.fetchStart),
          'navFirstPaint': (now - t.responseStart),
          'NavStart': (now - window.ue_t0)
        };
        window.navmet.push({key:"NavFirstPaintStart",end:+new Date(),begin:window.ue_t0});
      }
    }
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainStart",end:+new Date(),begin:window.ue_t0});
    }
</script>




<script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <script type="text/javascript">
    // Nav start should be logged at this place only if request is NOT progressively loaded.
    // For progressive loading case this metric is logged as part of skeleton.
    // Presence of skeleton signals that request is progressively loaded.
    if(!document.getElementById("navbar-skeleton")) {
      window.uet && uet('ns');
    }
    window._navbar = (function (o) {
      o.componentLoaded = o.loading = function(){};
      o.browsepromos = {};
      o.issPromos = [];
      return o;
    }(window._navbar || {}));
    window._navbar.declareOnLoad = function () { window.$Nav && $Nav.declare('page.load'); };
    if (window.addEventListener) {
      window.addEventListener("load", window._navbar.declareOnLoad, false);
    } else if (window.attachEvent) {
      window.attachEvent("onload", window._navbar.declareOnLoad);
    } else if (window.$Nav) {
      $Nav.when('page.domReady').run("OnloadFallbackSetup", function () {
        window._navbar.declareOnLoad();
      });
    }
    window.$Nav && $Nav.declare('logEvent.enabled',
      'false');

    window.$Nav && $Nav.declare('config.lightningDeals', {});
  </script>

    <style mark="aboveNavInjectionCSS" type="text/css">
       #nav-flyout-ewc .nav-flyout-buffer-left { display: none; } #nav-flyout-ewc .nav-flyout-buffer-right { display: none; } div#navSwmHoliday.nav-focus {border: none;margin: 0;}
    </style>
    <script mark="aboveNavInjectionJS" type="text/javascript">
      try {
        if(window.navmet===undefined)window.navmet=[]; if(window.$Nav) { $Nav.when('$', 'config', 'flyout.accountList', 'SignInRedirect', 'dataPanel').run('accountListRedirectFix', function ($, config, flyout, SignInRedirect, dataPanel) { if (!config.accountList) { return; } flyout.getPanel().onData(function (data) { if (SignInRedirect) { var $anchors = $('[data-nav-role=signin]', flyout.elem()); $.each($anchors, function(i, anchorEl) {SignInRedirect.setRedirectUrl($(anchorEl), null, null);});}});}); $Nav.when('$').run('defineIsArray', function(jQuery) { if(jQuery.isArray===undefined) { jQuery.isArray=function(param) { if(param.length===undefined) { return false; } return true; }; } }); $Nav.declare('config.cartFlyoutDisabled', 'true'); $Nav.when('$','$F','config','logEvent','panels','phoneHome','dataPanel','flyouts.renderPromo','flyouts.sloppyTrigger','flyouts.accessibility','util.mouseOut','util.onKey','debug.param').build('flyouts.buildSubPanels',function($,$F,config,logEvent,panels,phoneHome,dataPanel,renderPromo,createSloppyTrigger,a11yHandler,mouseOutUtility,onKey,debugParam){var flyoutDebug=debugParam('navFlyoutClick');return function(flyout,event){var linkKeys=[];$('.nav-item',flyout.elem()).each(function(){var $item=$(this);linkKeys.push({link:$item,panelKey:$item.attr('data-nav-panelkey')});});if(linkKeys.length===0){return;} var visible=false;var $parent=$('<div class=\'nav-subcats\'></div>').appendTo(flyout.elem());var panelGroup=flyout.getName()+'SubCats';var hideTimeout=null;var sloppyTrigger=createSloppyTrigger($parent);var showParent=function(){if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} if(visible){return;} var height=$('#nav-flyout-shopAll').height(); $parent.css({'height': height});$parent.animate({width:'show'},{duration:200,complete:function(){$parent.css({overflow:'visible'});}});visible=true;};var hideParentNow=function(){$parent.stop().css({overflow:'hidden',display:'none',width:'auto',height:'auto'});panels.hideAll({group:panelGroup});visible=false;if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;}};var hideParent=function(){if(!visible){return;} if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} hideTimeout=setTimeout(hideParentNow,10);};flyout.onHide(function(){sloppyTrigger.disable();hideParentNow();this.elem().hide();});var addPanel=function($link,panelKey){var panel=dataPanel({className:'nav-subcat',dataKey:panelKey,groups:[panelGroup],spinner:false,visible:false});if(!flyoutDebug){var mouseout=mouseOutUtility();mouseout.add(flyout.elem());mouseout.action(function(){panel.hide();});mouseout.enable();} var a11y=a11yHandler({link:$link,onEscape:function(){panel.hide();$link.focus();}});var logPanelInteraction=function(promoID,wlTriggers){var logNow=$F.once().on(function(){var panelEvent=$.extend({},event,{id:promoID});if(config.browsePromos&&!!config.browsePromos[promoID]){panelEvent.bp=1;} logEvent(panelEvent);phoneHome.trigger(wlTriggers);});if(panel.isVisible()&&panel.hasInteracted()){logNow();}else{panel.onInteract(logNow);}};panel.onData(function(data){renderPromo(data.promoID,panel.elem());logPanelInteraction(data.promoID,data.wlTriggers);});panel.onShow(function(){var columnCount=$('.nav-column',panel.elem()).length;panel.elem().addClass('nav-colcount-'+columnCount);showParent();var $subCatLinks=$('.nav-subcat-links > a',panel.elem());var length=$subCatLinks.length;if(length>0){var firstElementLeftPos=$subCatLinks.eq(0).offset().left;for(var i=1;i<length;i++){if(firstElementLeftPos===$subCatLinks.eq(i).offset().left){$subCatLinks.eq(i).addClass('nav_linestart');}} if($('span.nav-title.nav-item',panel.elem()).length===0){var catTitle=$.trim($link.html());catTitle=catTitle.replace(/ref=sa_menu_top/g,'ref=sa_menu');var $subPanelTitle=$('<span class=\'nav-title nav-item\'>'+ catTitle+'</span>');panel.elem().prepend($subPanelTitle);}} $link.addClass('nav-active');});panel.onHide(function(){$link.removeClass('nav-active');hideParent();a11y.disable();sloppyTrigger.disable();});panel.onShow(function(){a11y.elems($('a, area',panel.elem()));});sloppyTrigger.register($link,panel);if(flyoutDebug){$link.click(function(){if(panel.isVisible()){panel.hide();}else{panel.show();}});} var panelKeyHandler=onKey($link,function(){if(this.isEnter()||this.isSpace()){panel.show();}},'keydown',false);$link.focus(function(){panelKeyHandler.bind();}).blur(function(){panelKeyHandler.unbind();});panel.elem().appendTo($parent);};var hideParentAndResetTrigger=function(){hideParent();sloppyTrigger.disable();};for(var i=0;i<linkKeys.length;i++){var item=linkKeys[i];if(item.panelKey){addPanel(item.link,item.panelKey);}else{item.link.mouseover(hideParentAndResetTrigger);}}};});};
      } catch ( err ) {
        if ( window.$Nav ) {
          window.$Nav.when('metrics', 'logUeError').run(function(metrics, log) {
            metrics.increment('NavJS:AboveNavInjection:error');
            log(err.toString(), {
              'attribution': 'rcx-nav',
              'logLevel': 'FATAL'
            });
          });
        }
      }
    </script>

  <noscript>
    <style type="text/css"><!--
      #navbar #nav-shop .nav-a:hover {
        color: #ff9900;
        text-decoration: underline;
      }
      #navbar #nav-search .nav-search-facade,
      #navbar #nav-tools .nav-icon,
      #navbar #nav-shop .nav-icon,
      #navbar #nav-subnav .nav-hasArrow .nav-arrow {
        display: none;
      }
      #navbar #nav-search .nav-search-submit,
      #navbar #nav-search .nav-search-scope {
        display: block;
      }
      #nav-search .nav-search-scope {
        padding: 0 5px;
      }
      #navbar #nav-search .nav-search-dropdown {
        position: relative;
        top: 5px;
        height: 23px;
        font-size: 14px;
        opacity: 1;
        filter: alpha(opacity = 100);
      }
    --></style>
 </noscript>
<script type="text/javascript">window.navmet.push({key:'PreNav',end:+new Date(),begin:window.navmet.tmp});</script>

<a id="nav-top"></a>




<a id="skiplink" tabindex="0" class="skip-link">Skip to main content</a>

<script type="text/javascript">window.navmet.tmp=+new Date();</script>
<!-- Navyaan Upnav -->
    <div id="nav-upnav" aria-hidden="true" data-cel-widget="nav-upnav">
      <!-- unw1 failed -->
      
    </div>
<script type="text/javascript">window.navmet.push({key:'UpNav',end:+new Date(),begin:window.navmet.tmp});</script>


<script type="text/javascript">window.navmet.main=+new Date();</script>



<header id="navbar-main" class="nav-opt-sprite nav-flex nav-locale-us nav-lang-en nav-ssl nav-unrec nav-progressive-attribute">

   
  <div id="navbar" cel_widget_id="Navigation-desktop-navbar" role="navigation" class="nav-sprite-v1 celwidget nav-bluebeacon nav-a11y-t1 bold-focus-hover layout2 nav-flex layout3 layout3-alt nav-packard-glow hamburger nav-progressive-attribute using-mouse" data-csa-c-id="a5ljr1-l5dysu-svx9mo-btp1r3" data-cel-widget="Navigation-desktop-navbar">
    
    <div id="nav-belt">
      <div class="nav-left">
        <script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <div id="nav-logo">
    <a href="/ref=nav_logo" id="nav-logo-sprites" class="nav-logo-link nav-progressive-attribute" aria-label="Amazon">
      <span class="nav-sprite nav-logo-base"></span>
      <span id="logo-ext" class="nav-sprite nav-logo-ext nav-progressive-content"></span>
      <span class="nav-logo-locale">.us</span>
    </a>
  </div>
<script type="text/javascript">window.navmet.push({key:'Logo',end:+new Date(),begin:window.navmet.tmp});</script>
        
<div id="nav-global-location-slot">
    <span id="nav-global-location-data-modal-action" class="a-declarative nav-progressive-attribute" data-a-modal="{&quot;width&quot;:375, &quot;closeButton&quot;:&quot;false&quot;,&quot;popoverLabel&quot;:&quot;Choose your location&quot;, &quot;ajaxHeaders&quot;:{&quot;anti-csrftoken-a2z&quot;:&quot;gKl2ama3MOsCQhUJA+dje42G0EIPUsp7/qdmdroAAAAMAAAAAGREWMhyYXcAAAAA;hLU6LyxhKGWtYq+914RTNDzQimpOqQUtf+TXtZAlVtSjAAAAAGREWMgAAAAB&quot;}, &quot;name&quot;:&quot;glow-modal&quot;, &quot;url&quot;:&quot;/portal-migration/hz/glow/get-rendered-address-selections?deviceType=desktop&amp;pageType=Search&amp;storeContext=books&amp;actionSource=desktop-modal&quot;, &quot;footer&quot;:&quot;<span class=\&quot;a-declarative\&quot; data-action=\&quot;a-popover-close\&quot; data-a-popover-close=\&quot;{}\&quot;><span class=\&quot;a-button a-button-primary\&quot;><span class=\&quot;a-button-inner\&quot;><button name=\&quot;glowDoneButton\&quot; class=\&quot;a-button-text\&quot; type=\&quot;button\&quot;>Done</button></span></span></span>&quot;,&quot;header&quot;:&quot;Choose your location&quot;}" data-action="a-modal">
        <a id="nav-global-location-popover-link" class="nav-a nav-a-2 a-popover-trigger a-declarative nav-progressive-attribute" tabindex="0">
            <div class="nav-sprite nav-progressive-attribute" id="nav-packard-glow-loc-icon"></div>
            <div id="glow-ingress-block">
                <span class="nav-line-1 nav-progressive-content" id="glow-ingress-line1">
                   Deliver to
                </span>
                <span class="nav-line-2 nav-progressive-content" id="glow-ingress-line2">
                   Argentina
                </span>
            </div>
        </a>
        </span>
        <input data-addnewaddress="add-new" id="unifiedLocation1ClickAddress" name="dropdown-selection" type="hidden" value="add-new" class="nav-progressive-attribute">
        <input data-addnewaddress="add-new" id="ubbShipTo" name="dropdown-selection-ubb" type="hidden" value="add-new" class="nav-progressive-attribute">
        <input id="glowValidationToken" name="glow-validation-token" type="hidden" value="gKl2ama3MOsCQhUJA+dje42G0EIPUsp7/qdmdroAAAAMAAAAAGREWMhyYXcAAAAA;hLU6LyxhKGWtYq+914RTNDzQimpOqQUtf+TXtZAlVtSjAAAAAGREWMgAAAAB" class="nav-progressive-attribute">
</div>

<div id="nav-global-location-toaster-script-container" class="nav-progressive-content">
</div>

      </div>
          <div class="nav-fill">
            <script type="text/javascript">window.navmet.tmp=+new Date();</script>
<div id="nav-search">
  <div id="nav-bar-left"></div>
  <form id="nav-search-bar-form" accept-charset="utf-8" action="/s/ref=nb_sb_noss" class="nav-searchbar nav-progressive-attribute" method="GET" name="site-search" role="search">

    <div class="nav-left">
      <div id="nav-search-dropdown-card">
        
  <div class="nav-search-scope nav-sprite">
    <div class="nav-search-facade" data-value="search-alias=aps">
      <span id="nav-search-label-id" class="nav-search-label nav-progressive-content" style="width: auto;">Literature &amp; Fiction</span>
      <i class="nav-icon"></i>
    </div>
    <label id="searchDropdownDescription" for="searchDropdownBox" class="nav-progressive-attribute" style="display:none">Select the department you want to search in</label>
    <select aria-describedby="searchDropdownDescription" class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown" data-nav-digest="HEZwrcP+xZexMD2D2ODyHsC9wC0=" data-nav-selected="0" id="searchDropdownBox" name="url" style="display: block; top: 2.5px;" tabindex="0" title="Search in">
        <option selected="selected" current="true" data-root-alias="stripbooks" value="node=17">Literature &amp; Fiction</option>
        <option value="search-alias=aps">All Departments</option>
        <option value="search-alias=arts-crafts-intl-ship">Arts &amp; Crafts</option>
        <option value="search-alias=automotive-intl-ship">Automotive</option>
        <option value="search-alias=baby-products-intl-ship">Baby</option>
        <option value="search-alias=beauty-intl-ship">Beauty &amp; Personal Care</option>
        <option current="parent" value="search-alias=stripbooks-intl-ship">Books</option>
        <option value="search-alias=fashion-boys-intl-ship">Boys' Fashion</option>
        <option value="search-alias=computers-intl-ship">Computers</option>
        <option value="search-alias=deals-intl-ship">Deals</option>
        <option value="search-alias=digital-music">Digital Music</option>
        <option value="search-alias=electronics-intl-ship">Electronics</option>
        <option value="search-alias=fashion-girls-intl-ship">Girls' Fashion</option>
        <option value="search-alias=hpc-intl-ship">Health &amp; Household</option>
        <option value="search-alias=kitchen-intl-ship">Home &amp; Kitchen</option>
        <option value="search-alias=industrial-intl-ship">Industrial &amp; Scientific</option>
        <option value="search-alias=digital-text">Kindle Store</option>
        <option value="search-alias=luggage-intl-ship">Luggage</option>
        <option value="search-alias=fashion-mens-intl-ship">Men's Fashion</option>
        <option value="search-alias=movies-tv-intl-ship">Movies &amp; TV</option>
        <option value="search-alias=music-intl-ship">Music, CDs &amp; Vinyl</option>
        <option value="search-alias=pets-intl-ship">Pet Supplies</option>
        <option value="search-alias=instant-video">Prime Video</option>
        <option value="search-alias=software-intl-ship">Software</option>
        <option value="search-alias=sporting-intl-ship">Sports &amp; Outdoors</option>
        <option value="search-alias=tools-intl-ship">Tools &amp; Home Improvement</option>
        <option value="search-alias=toys-and-games-intl-ship">Toys &amp; Games</option>
        <option value="search-alias=videogames-intl-ship">Video Games</option>
        <option value="search-alias=fashion-womens-intl-ship">Women's Fashion</option>
    </select>
  </div>

      </div>
    </div>
    <div class="nav-fill">
      <div class="nav-search-field ">
        <label for="twotabsearchtextbox" style="display: none;">Search Amazon</label>
        <input type="text" id="twotabsearchtextbox" value="bookstore amazon" name="field-keywords" autocomplete="off" placeholder="Search Amazon" class="nav-input nav-progressive-attribute" dir="auto" tabindex="0" aria-label="Search Amazon" spellcheck="false">
      </div>
      <div id="nav-iss-attach"></div>
    </div>
    <div class="nav-right">
      <div class="nav-search-submit nav-sprite">
        <span id="nav-search-submit-text" class="nav-search-submit-text nav-sprite nav-progressive-attribute" aria-label="Go">
          <input id="nav-search-submit-button" type="submit" class="nav-input nav-progressive-attribute" value="Go" tabindex="0">
        </span>
      </div>
    </div>
  </form>
</div>
<script type="text/javascript">window.navmet.push({key:'Search',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
      <div class="nav-right">
          <script type="text/javascript">window.navmet.tmp=+new Date();</script>
          <div id="nav-tools" class="layoutToolbarPadding">
              
              
              
              
  <a href="/customer-preferences/edit?ie=UTF8&amp;preferencesReturnUrl=%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dsr_nr_p_n_condition-type_1&amp;ref_=topnav_lang_ais" id="icp-nav-flyout" class="nav-a nav-a-2 icp-link-style-2" aria-label="Choose a language for shopping.">
    <span class="icp-nav-link-inner">
      <span class="nav-line-1">
      </span>
      <span class="nav-line-2">
        <span class="icp-nav-flag icp-nav-flag-us icp-nav-flag-lop"></span>
          <div>EN</div>
        <span class="nav-icon nav-arrow" style="visibility: visible;"></span>
      </span>
    </span>
  </a>

              
  <a href="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dnav_ya_signin&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=usflex&amp;openid.mode=checkid_setup&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;" class="nav-a nav-a-2   nav-progressive-attribute" data-nav-ref="nav_ya_signin" data-nav-role="signin" data-ux-jq-mouseenter="true" id="nav-link-accountList" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-accountList" data-csa-c-content-id="nav_ya_signin" data-csa-c-id="d2cb7d-4khcgj-wo9ok6-qewf3q">
  <div class="nav-line-1-container"><span id="nav-link-accountList-nav-line-1" class="nav-line-1 nav-progressive-content">Hello, sign in</span></div>
  <span class="nav-line-2 ">Account &amp; Lists<span class="nav-icon nav-arrow" style="visibility: visible;"></span>
  </span>
</a>

              
<a href="/gp/css/order-history?ref_=nav_orders_first" class="nav-a nav-a-2   nav-progressive-attribute" id="nav-orders" tabindex="0">
  <span class="nav-line-1">Returns</span>
  <span class="nav-line-2">&amp; Orders<span class="nav-icon nav-arrow"></span></span>
</a>

              
              
  <a href="/gp/cart/view.html?ref_=nav_cart" aria-label="0 items in cart" class="nav-a nav-a-2 nav-progressive-attribute" id="nav-cart">
    <div id="nav-cart-count-container">
      <span id="nav-cart-count" aria-hidden="true" class="nav-cart-count nav-cart-0 nav-progressive-attribute nav-progressive-content">0</span>
      <span class="nav-cart-icon nav-sprite"></span>
    </div>
    <div id="nav-cart-text-container" class=" nav-progressive-attribute">
      <span aria-hidden="true" class="nav-line-1">
        
      </span>
      <span aria-hidden="true" class="nav-line-2">
        Cart
        <span class="nav-icon nav-arrow"></span>
      </span>
    </div>
  </a>

          </div>
          <script type="text/javascript">window.navmet.push({key:'Tools',end:+new Date(),begin:window.navmet.tmp});</script>

      </div>
    </div><div id="nav-flyout-iss-anchor"><div id="nav-flyout-searchAjax" class="nav-issFlyout nav-flyout"><div class="nav-template nav-flyout-content"></div><div class="autocomplete-results-container"><div class="two-pane-results-container"><div class="left-pane-results-container"></div><div class="right-pane-results-container"></div></div></div></div></div><div id="nav-flyout-anchor"><div class="nav-ewc-arrow"></div><div id="nav-flyout-amazonprime" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-accountList" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content"><div id="nav-al-container"><div id="nav-al-signin"><div id="nav-flyout-ya-signin" class="nav-flyout-content nav-flyout-accessibility"><a href="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dnav_signin&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=usflex&amp;openid.mode=checkid_setup&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;" rel="nofollow" class="nav-action-signin-button" data-nav-role="signin" data-nav-ref="nav_signin"><span class="nav-action-inner">Sign in</span></a><div id="nav-flyout-ya-newCust" class="nav_pop_new_cust nav-flyout-content nav-flyout-accessibility">New customer? <a href="https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26dc%3D%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26i%3Dstripbooks%26k%3Dbookstore%2520amazon%26qid%3D1682200770%26ref%3Dsr_nr_p_n_condition-type_1%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref_%3Dnav_newcust&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=usflex&amp;openid.mode=checkid_setup&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;" rel="nofollow" class="nav-a">Start here.</a></div></div></div><div id="nav-al-wishlist" class="nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility"><div class="nav-title" id="nav-al-title">Your Lists</div><a href="/hz/wishlist/ls?triggerElementID=createList&amp;ref_=nav_ListFlyout_navFlyout_createList_lv_redirect" class="nav-link nav-item"><span class="nav-text">Create a List</span></a> <a href="/registries?ref_=nav_ListFlyout_find" class="nav-link nav-item"><span class="nav-text">Find a List or Registry</span></a></div><div id="nav-al-your-account" class="nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility"><div class="nav-title">Your Account</div><a href="/gp/css/homepage.html?ref_=nav_AccountFlyout_ya" class="nav-link nav-item"><span class="nav-text">Account</span></a> <a id="nav_prefetch_yourorders" href="/gp/css/order-history?ref_=nav_AccountFlyout_orders" class="nav-link nav-item"><span class="nav-text">Orders</span></a> <a href="/gp/yourstore?ref_=nav_AccountFlyout_recs" class="nav-link nav-item"><span class="nav-text">Recommendations</span></a> <a href="/gp/history?ref_=nav_AccountFlyout_browsinghistory" class="nav-link nav-item"><span class="nav-text">Browsing History</span></a> <a href="/gp/video/watchlist?ref_=nav_AccountFlyout_ywl" class="nav-link nav-item"><span class="nav-text">Watchlist</span></a> <a href="/gp/video/library?ref_=nav_AccountFlyout_yvl" class="nav-link nav-item"><span class="nav-text">Video Purchases &amp; Rentals</span></a> <a href="/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku" class="nav-link nav-item"><span class="nav-text">Kindle Unlimited</span></a> <a href="/hz/mycd/myx?pageType=content&amp;ref_=nav_AccountFlyout_myk" class="nav-link nav-item"><span class="nav-text">Content &amp; Devices</span></a> <a href="/gp/subscribe-and-save/manager/viewsubscriptions?ref_=nav_AccountFlyout_sns" class="nav-link nav-item"><span class="nav-text">Subscribe &amp; Save Items</span></a> <a href="/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions" class="nav-link nav-item"><span class="nav-text">Memberships &amp; Subscriptions</span></a> <a href="https://music.amazon.com?ref=nav_youraccount_cldplyr" class="nav-link nav-item"><span class="nav-text">Music Library</span></a></div></div></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-amazonfresh" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-groceries" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-transientFlyout" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-health" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abAcquisition" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abActivation" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abAccountLink" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatAcquisition" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatActivation" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatAccountLink" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-icp" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-icp-footer-flyout" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div></div>
    <div id="nav-main" class="nav-sprite">
      <div class="nav-left">
        <script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <a href="javascript: void(0)" id="nav-hamburger-menu" role="button" aria-label="Open Menu" data-csa-c-type="widget" data-csa-c-slot-id="HamburgerMenuDesktop" data-csa-c-interaction-events="click" data-csa-c-id="3b2ibo-64a939-9cmz5z-13sley">
    <i class="hm-icon nav-sprite"></i>
    <span class="hm-icon-label">All</span>
  </a>
  
<script type="text/javascript">
  var hmenu = document.getElementById("nav-hamburger-menu");
  hmenu.setAttribute("href", "javascript: void(0)");
  window.navHamburgerMetricLogger = function() {
    if (window.ue && window.ue.count) {
      var metricName = "Nav:Hmenu:IconClickActionPending";
      window.ue.count(metricName, (ue.count(metricName) || 0) + 1);
    }
    window.$Nav && $Nav.declare("navHMenuIconClicked",!0);
    window.$Nav && $Nav.declare("navHMenuIconClickedNotReadyTimeStamp", Date.now());
  };
  hmenu.addEventListener("click", window.navHamburgerMetricLogger);
  window.$Nav && $Nav.declare('hamburgerMenuIconAvailableOnLoad', false);
</script>  
<script type="text/javascript">window.navmet.push({key:'HamburgerMenuIcon',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
      <div class="nav-fill">
        
 <div id="nav-shop">
 </div>
        <div id="nav-xshop-container">
          <div id="nav-xshop" class="nav-progressive-content">
            <script type="text/javascript">window.navmet.tmp=+new Date();</script>
<a href="/gp/goldbox?ref_=nav_cs_gb" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_0" data-csa-c-content-id="nav_cs_gb" data-csa-c-id="rdv7nj-wbeucp-ntof3t-o3iuil">Today's Deals</a>

<a href="/gp/help/customer/display.html?nodeId=508510&amp;ref_=nav_cs_customerservice" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_1" data-csa-c-content-id="nav_cs_customerservice" data-csa-c-id="4nvl1d-9gd8ll-reiowv-k1utwu">Customer Service</a>

<a href="/gp/browse.html?node=16115931011&amp;ref_=nav_cs_registry" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_2" data-csa-c-content-id="nav_cs_registry" data-csa-c-id="2ljebr-ffd23w-cvs2eb-a404n8">Registry</a>

<a href="/gift-cards/b/?ie=UTF8&amp;node=2238192011&amp;ref_=nav_cs_gc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_3" data-csa-c-content-id="nav_cs_gc" data-csa-c-id="ddgw3v-tclure-rfq6wn-6tor16">Gift Cards</a>

<a href="/b/?_encoding=UTF8&amp;ld=AZUSSOA-sell&amp;node=12766669011&amp;ref_=nav_cs_sell" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_4" data-csa-c-content-id="nav_cs_sell" data-csa-c-id="cxpzft-q997vy-2b7pbm-hgdzjj">Sell</a>

<a href="/gp/help/customer/accessibility" aria-label="Click to call our Disability Customer Support line, or reach us directly at 1-888-283-1678" class="nav-hidden-aria  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_5" data-csa-c-id="mdjewj-o7kjg1-y7hjp6-3qotz1">Disability Customer Support</a>
<script type="text/javascript">window.navmet.push({key:'CrossShop',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
        </div>
      </div>
      <div class="nav-right">
        <script type="text/javascript">window.navmet.tmp=+new Date();</script><!-- Navyaan SWM -->
<div id="nav-swmslot" class="nav-swm-text-widget">
  <a href="/deals/?_encoding=UTF8&amp;ref_=nav_swm_undefined&amp;pf_rd_p=df25d76e-dbbb-4d9e-8795-b234a49106b3&amp;pf_rd_s=nav-sitewide-msg-text-export&amp;pf_rd_t=4201&amp;pf_rd_i=navbar-4201&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_r=BNJYY9EBY54VZZF6X4X6" id="swm-link" class="nav_a nav-swm-text nav-progressive-attribute nav-progressive-content" tabindex="0">Shop great deals now</a>
</div><script type="text/javascript">window.navmet.push({key:'SWM',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
    </div>

    <div id="nav-subnav-toaster"></div>

    
    <div id="nav-progressive-subnav">
      <script type="text/javascript">window.navmet.tmp=+new Date();</script>

<div id="nav-subnav" data-category="books">
  <a href="/books-used-books-textbooks/b/?ie=UTF8&amp;node=283155&amp;ref_=topnav_storetab_b" class="nav-a nav-b" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Books" tabindex="0">
    <span class="nav-a-content">
      Books
      
    </span>
  </a>
  <a href="/Advanced-Search-Books/b/?ie=UTF8&amp;node=241582011&amp;ref_=sv_b_1" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Advanced Search" tabindex="0">
    <span class="nav-a-content">
      Advanced Search
      
    </span>
  </a>
  <a href="/gp/new-releases/books/?ie=UTF8&amp;ref_=sv_b_2" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="New Releases" tabindex="0">
    <span class="nav-a-content">
      New Releases
      
    </span>
  </a>
  <a href="/b/?ie=UTF8&amp;node=16857165011&amp;ref_=sv_b_3" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Best Sellers &amp; More" tabindex="0">
    <span class="nav-a-content">
      Best Sellers &amp; More
      
    </span>
  </a>
  <a href="/amazonbookclubs/?_encoding=UTF8&amp;ref_=sv_b_4" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Amazon Book Clubs" tabindex="0">
    <span class="nav-a-content">
      Amazon Book Clubs
      
    </span>
  </a>
  <a href="/Childrens-Books/b/?ie=UTF8&amp;node=4&amp;ref_=sv_b_5" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Children's Books" tabindex="0">
    <span class="nav-a-content">
      Children's Books
      
    </span>
  </a>
  <a href="/New-Used-Textbooks-Books/b/?ie=UTF8&amp;node=465600&amp;ref_=sv_b_6" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Textbooks" tabindex="0">
    <span class="nav-a-content">
      Textbooks
      
    </span>
  </a>
  <a href="/rentals/b/?ie=UTF8&amp;node=17853655011&amp;ref_=sv_b_7" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Textbook Rentals" tabindex="0">
    <span class="nav-a-content">
      Textbook Rentals
      
    </span>
  </a>
  <a href="/b/?ie=UTF8&amp;node=390919011&amp;ref_=sv_b_8" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" aria-label="Best Books of the Month" tabindex="0">
    <span class="nav-a-content">
      Best Books of the Month
      
    </span>
  </a>
<!-- nav-linktree-subnav - 'books' -->
</div>

<script type="text/javascript">window.navmet.push({key:'Subnav',end:+new Date(),begin:window.navmet.tmp});</script>
    </div>

    <script type="text/javascript">
(function() {
  var viewportWidth = function() {
    return window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;
  };

  if (typeof uet === 'function') {  uet('x1', 'ewc', {wb: 1}); }

  window.$Nav && $Nav.declare('config.ewc', (function() {
    var config = {"enablePersistent":true,"viewportWidthForPersistent":1400,"isEWCLogging":1,"isEWCStateExpanded":true,"EWCStateReason":"fixed","isSmallScreenEnabled":true,"isFreshCustomer":false,"errorContent":{"html":"<div class='nav-ewc-error'><span class='nav-title'>Oops!</span><p class='nav-paragraph'>There's a problem loading your cart right now.</p><a href='/gp/cart/view.html?ref_=nav_err_ewc_timeout' class='nav-action-button'><span class='nav-action-inner'>Your Cart</span></a></div>"},"url":"/cart/ewc/compact?hostPageType=Search&hostSubPageType=List&hostPageRID=BNJYY9EBY54VZZF6X4X6&prerender=0&storeName=books","cartCount":0,"freshCartCount":0,"almCartCount":0,"primeWardrobeCartCount":0,"isCompactViewEnabled":true,"isCompactEWCRendered":true,"isWiderCompactEWCRendered":true,"EWCBrowserCacheKey":"EWC_Cache_139-5329492-5095613__USD_en_US","isContentRepainted":false,"clearCache":false,"loadFromCacheWithDelay":0,"delayRenderingTillATF":false};
    var hasAui = window.P && window.P.AUI_BUILD_DATE;
    var isRTLEnabled = (document.dir === 'rtl');
    config.pinnable = config.pinnable && hasAui;
    config.isMigrationTreatment = true;

    config.flyout = (function() {
      var navbelt = document.getElementById('nav-belt');
      var navCart = document.getElementById('nav-cart');
      var ewcFlyout = document.getElementById('nav-flyout-ewc');
      var persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-full-height-persistent-hover';
      var flyout = {};

      var getDocumentScrollTop = function() {
        return (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
      };

      var isWindow = function(obj) {
        return obj != null && obj === obj.window;
      };

      var getWindow = function(elem) {
        return isWindow(elem) ? elem : elem.nodeType === 9 && elem.defaultView;
      };

      var getOffset = function(elem) {
        if (elem.getClientRects && !elem.getClientRects().length) {
          return {top: 0};
        }

        var rect = elem.getBoundingClientRect
          ? elem.getBoundingClientRect()
          : {top: 0};

        if (rect.width || rect.height) {
          var doc = elem.ownerDocument;
          var win = getWindow(doc);
          return {
            top: rect.top + win.pageYOffset - doc.documentElement.clientTop
          };
        }
        return rect;
      };

      flyout.align = function() {
        var newTop = getOffset(navbelt).top - getDocumentScrollTop();
        ewcFlyout.style.top = (newTop > 0 ? newTop + 'px' : 0);
      };

      flyout.hide = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = '')
          : (ewcFlyout.style.right = '');
      };

      if(typeof config.isCompactEWCRendered === 'undefined') {
        if (
          (config.isSmallScreenEnabled && viewportWidth() < 1400) ||
          (config.isCompactViewEnabled && viewportWidth() >= 1400)
        ) {
          config.isCompactEWCRendered = true;
          config.isEWCStateExpanded = true;
          config.url = config.url.replace("/gp/navcart/sidebar", "/cart/ewc/compact");
        } else {
          config.isCompactEWCRendered = false;
        }
      }

      var viewportQualifyForPersistent = function () {
        return (config.isCompactEWCRendered)
          ? true
          : viewportWidth() >= 1400;
      }

      flyout.hasQualifiedViewportForPersistent = viewportQualifyForPersistent;

      var getEWCRightOffset = function() {
        if (!config.isCompactEWCRendered) {
          return 0;
        }

        var $navbelt = document.getElementById('nav-belt');
        if ($navbelt === undefined || $navbelt === null) {
          return 0;
        }

        var EWCCompactViewWidth = (config.isWiderCompactEWCRendered  && viewportWidth() >= 1280) ? 130 : 100;
        var scrollLeft = (window.pageXOffset !== undefined)
          ? window.pageXOffset
          : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
        var scrollXAxis = Math.abs(scrollLeft);
        var windowWidth = document.documentElement.clientWidth;
        var navbeltWidth = $navbelt.offsetWidth;
        var isPartOfNavbarNotVisible = (navbeltWidth + EWCCompactViewWidth) > windowWidth;

        if (isPartOfNavbarNotVisible) {
          return 0 - (navbeltWidth - scrollXAxis - windowWidth + EWCCompactViewWidth);
        } else {
          return 0;
        }
      }

      flyout.getEWCRightOffsetCssProperty = function () {
        return getEWCRightOffset() + 'px';
      }

      if (config.isCompactEWCRendered) {
        persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-compact-view';
        if (config.isWiderCompactEWCRendered) { persistentClassOnBody += ' nav-ewc-wider-compact-view'; }
      }

      flyout.show = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = flyout.getEWCRightOffsetCssProperty())
          : (ewcFlyout.style.right = flyout.getEWCRightOffsetCssProperty());
      };

      var isIOSDevice = function() {
        return (/iPad|iPhone|iPod/.test(navigator.platform) ||
                (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) &&
                !window.MSStream;
      }

      var checkForPersistent = function() {
        if (!hasAui) {
          return { result: false, reason: 'noAui' };
        }
        if (!config.enablePersistent) {
          return { result: false, reason: 'config' };
        }
        if (!viewportQualifyForPersistent()) {
          return { result: false, reason: 'viewport' };
        }
        if (isIOSDevice()) {
          return { result: false, reason: 'iOS' };
        }
        if (!config.cartCount > 0) {
          return { result: false, reason: 'emptycart' };
        }
        return { result: true };
      };

      flyout.ableToPersist = function() {
        return checkForPersistent().result;
      };
      var persistentClassRegExp = '(?:^|\\s)' + persistentClassOnBody + '(?!\\S)';
      flyout.applyPageLayoutForPersistent = function() {
        if (!document.documentElement.className.match( new RegExp(persistentClassRegExp) )) {
          document.documentElement.className += ' ' + persistentClassOnBody;
        }
      };

      flyout.unapplyPageLayoutForPersistent = function() {
        document.documentElement.className = document.documentElement.className.replace( new RegExp(persistentClassRegExp, 'g'), '');
      };

      flyout.persist = function() {
        flyout.applyPageLayoutForPersistent();
        flyout.show();
        if (config.isCompactEWCRendered) {
          flyout.align();
        }
      };

      flyout.unpersist = function() {
        flyout.unapplyPageLayoutForPersistent();
        flyout.hide();
      };
      
      var persistentCheck = checkForPersistent();
    

      var resizeCallback = function() {
        
        if (flyout.ableToPersist()) {
          flyout.persist();
        }
        else {
          flyout.unpersist();
        }
      };

      flyout.bindEvents = function() {
        if (window.addEventListener) {
          window.addEventListener('resize', resizeCallback, false);
          
          if (config.isCompactEWCRendered) {
            window.addEventListener('scroll', flyout.align, false);
          }
        }
      };

      flyout.unbindEvents = function() {
        if (window.removeEventListener) {
          window.removeEventListener('resize', resizeCallback, false);
          
          if (config.isCompactEWCRendered) {
            window.removeEventListener('scroll', flyout.align, false);
          }
        }
      };
      
      var ewcDefaultPersistence = function() {
      
        if (persistentCheck.result) {
          flyout.persist();
          if (window.ue && ue.tag) {
            ue.tag('ewc:persist');
          }
        } else {
          if (window.ue && ue.tag) {
            ue.tag('ewc:unpersist');
            if (persistentCheck.reason === 'noAui') {
              ue.tag('ewc:unpersist:noAui');
            }
            if (persistentCheck.reason === 'viewport') {
              ue.tag('ewc:unpersist:viewport');
            }
            if (persistentCheck.reason === 'emptycart') {
              ue.tag('ewc:unpersist:emptycart');
            }
            if (persistentCheck.reason === 'iOS') {
              ue.tag('ewc:unpersist:iOS');
            }
          }
        }
      };
      
      ewcDefaultPersistence();
      
      if (window.ue && ue.tag)  {
        if (flyout.hasQualifiedViewportForPersistent()) {
          ue.tag('ewc:bview');
        }
        else {
          ue.tag('ewc:sview');
        }
      }
      flyout.bindEvents();
      flyout.cache = function () {
    const cache = window.sessionStorage;
    const CACHE_KEY = "EWCBrowserCacheKey";
    const CACHE_EXPIRY = "EWCBrowserCacheExpiry"; 
    const CACHE_VALUE = "EWCBrowserCacheValue"; 
    const isSessionStorageValid = function () {
        return window && cache && cache instanceof Storage;
    };
    const isCachePresent = function (key) {
        return cache.length > 0 && cache.getItem(key);
    }
    const isValidType = function (value) {
        // Prevents accessing empty key-value and internal methods(prototypes) of storage
        // TODO: Log metrics for invalid access;
        return value && value.constructor == String;
    }
    return {
        getCache: function (key) {
            const value = isCachePresent(key);
            return (isValidType(value)) ? value : null;
        },
        setCache: function (key, value) {
            const oldValue = isCachePresent(key);
            const cacheExpiryTime = isCachePresent(CACHE_EXPIRY);
            // Set the expiry when there's no existing cache - to prevent resetting expiry on page navigation
            if (!cacheExpiryTime) {
                var currentTime = new Date();
                cache.setItem(CACHE_EXPIRY, new Date(currentTime.getTime() + 5 * 60000))
            }
            // TODO: Log length of old and new cache values when logMetrics is true
            cache.setItem(key, value);
        },
        updateCacheAndEwcContainer: function (cacheKey, newEwcContent) {
            const $ = $Nav.getNow("$");
            const $currentEwc = $("#ewc-content");
            if (!$currentEwc.length) {
                var $content = $('#nav-flyout-ewc .nav-ewc-content');
                $content.html(newEwcContent);
                this.setCache(CACHE_KEY, cacheKey);
                if (window.ue && window.ue.count) {
                    var current = window.ue.count("ewc-init-cache") || 0;
                    window.ue.count("ewc-init-cache", current + 1);
                }
            } else {
                var $newEwcContent = $('<div />');
                var EWC_CONTENT_BODY_SCROLL_SELECTOR = ".ewc-scroller--selected";
                if (newEwcContent) { // 1. Updates EWC container with new HTML 
                    const $newEwcHtml = $newEwcContent.html(newEwcContent).find("#ewc-content");
                    const offSet = $currentEwc.find(EWC_CONTENT_BODY_SCROLL_SELECTOR).position().top - $currentEwc.find(".ewc-active-cart--selected").position().top;
                    $currentEwc.html($newEwcHtml.html());
                    $currentEwc.find(EWC_CONTENT_BODY_SCROLL_SELECTOR).scrollTop(offSet);
                    if (typeof window.uex === 'function') {
                        window.uex('ld', 'ewc-reflect-new-state', {wb: 1});
                    }
                } else {
                    // 2. Fetches cached response and updates it's html with new state on EWC Update
                    const cachedEwc = this.getCache(CACHE_VALUE);
                    $newEwcContent = $newEwcContent[0];
                    $(cachedEwc).map(function (elementIndex, element) {
                         $newEwcContent.appendChild((element.id === "ewc-content") ? $currentEwc.clone()[0] : element);
                    });
                    newEwcContent = $newEwcContent.innerHTML;
                    if (window.ue && window.ue.count) {
                        var current = window.ue.count("ewc-update-cache") || 0;
                        window.ue.count("ewc-update-cache", current + 1);
                    }
                }
                $newEwcContent.remove();
            }
            this.setCache(CACHE_VALUE, newEwcContent);
        },
        removeCache: function (key) {
            return cache.removeItem(key);
        }
    }
}
;
      return flyout;
    }());
     
     
     
const CACHE_KEY = "EWCBrowserCacheKey";
const CACHE_VALUE = "EWCBrowserCacheValue"; 
const CACHE_EXPIRY = "EWCBrowserCacheExpiry"; 
var cache = config.flyout.cache();

const isCacheValid = function () {
  // Check for page types and tenure of the cache
  const clearCache = config.clearCache;
  const cacheExpiryTime = cache.getCache(CACHE_EXPIRY);
  const isCacheExpired = new Date() > new Date(cacheExpiryTime);
  const cacheKey = config.EWCBrowserCacheKey;
  const oldCacheKey = cache.getCache(CACHE_KEY);
  const isCacheValid = !clearCache && !isCacheExpired && cacheKey == oldCacheKey;
  if (!isCacheValid && window.ue && window.ue.count) {
    var current = window.ue.count("ewc-cache-invalidated") || 0;
    window.ue.count("ewc-cache-invalidated", current + 1);
  }
  return isCacheValid;
}
function loadFromCache() {
    if (window.uet && typeof window.uet === 'function') {
        window.uet('bb', 'ewc-loaded-from-cache', {wb: 1});
    }
    if (cache) {
        if (isCacheValid()) {
            var content = cache.getCache(CACHE_VALUE);
            if (content) {
                var $ewcContainer = document.getElementById("nav-flyout-ewc").getElementsByClassName("nav-ewc-content")[0];
                var $ewcContent = document.getElementById("ewc-content");
                if ($ewcContainer && !$ewcContent) {
                    $ewcContainer.innerHTML = content;
                    // Execute scripts from cache
                    const ewcJavascript = document.getElementById("ewc-content").parentNode.querySelectorAll(':scope > script');
                    ewcJavascript.forEach(function (script) {
                        var scriptTag = document.createElement("script");
                        scriptTag.innerHTML = script.innerHTML;
                        document.body.appendChild(scriptTag);
                    });
                    if (typeof window.uex === 'function') {
                        window.uex('ld', 'ewc-loaded-from-cache', {wb: 1});
                    }
                } else if (window.ue && window.ue.count && typeof window.ue.count === 'function') {
                    var currentFailure = window.ue.count("ewc-slow-cache") || 0;
                    window.ue.count("ewc-slow-cache", currentFailure + 1);
                }
            }
        } else {
            cache.removeCache(CACHE_VALUE);
            cache.removeCache(CACHE_KEY);
            cache.removeCache(CACHE_EXPIRY);
        }
    }
}
function delayBy(delayTime) {
    if (delayTime) {
        window.setTimeout(function() {
            loadFromCache();
        }, delayTime)
    } else {
        loadFromCache();
    }
}
if(config.delayRenderingTillATF) {
    (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('atf').execute("EverywhereCartLoadFromCacheOnAtf", function () {
        delayBy(config.loadFromCacheWithDelay);
    });
} else {
    delayBy(config.loadFromCacheWithDelay);
}

    return config;
  }()));

  if (typeof uet === 'function') {
    uet('x2', 'ewc', {wb: 1});
  }

  if (window.ue && ue.tag) {
    ue.tag('ewc');
    ue.tag('ewc:unrec');
    ue.tag('ewc:cartsize:0');

    if ( window.P && window.P.AUI_BUILD_DATE ) {
      ue.tag('ewc:aui');
    } else {
      ue.tag('ewc:noAui');
    }
  }
}());
</script>
  <div id="nav-flyout-ewc" class="nav-ewc-lazy-align nav-ewcFlyout nav-flyout nav-locked" style="top: 0px; height: 679px;"><div class="nav-flyout-body ewc-beacon" tabindex="-1"><div class="nav-ewc-content"></div></div><div class="nav-template nav-flyout-content" style="display: none;"> </div></div></div>

  
  

</header>


<script type="text/javascript">window.navmet.push({key:'NavBar',end:+new Date(),begin:window.navmet.main});</script>


<script type="text/javascript">
  if (window.ue_t0) {
    window.navmet.push({key:"NavMainPaintEnd",end:+new Date(),begin:window.ue_t0});
    window.navmet.push({key:"NavFirstPaintEnd",end:+new Date(),begin:window.ue_t0});
  }
</script>


<script type="text/javascript">
    <!--
    
    window.$Nav && $Nav.when("data").run(function(data) { data({"freshTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<style>#nav-flyout-fresh{width:269px;padding:0;}#nav-flyout-fresh .nav-flyout-content{padding:0;}</style><a href='/amazonfresh'><img src='https://images-na.ssl-images-amazon.com/images/G/01/omaha/images/yoda/flyout_72dpi._V270255989_.png' /></a>"}}}},"cartTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_cart_timeout"},"title":"Oops!","paragraph":"Unable to retrieve your cart."}}}},"primeTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<a href='/gp/prime'><img src='https://images-na.ssl-images-amazon.com/images/G/01/prime/piv/YourPrimePIV_fallback_CTA._V327346943_.jpg' /></a>"}}}},"ewcTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_ewc_timeout"},"title":"Oops!","paragraph":"There's a problem loading your cart right now."}}}},"errorWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wishlist","url":"/gp/registry/wishlist/?ref_=nav_err_wishlist"},"title":"Oops!","paragraph":"Unable to retrieve your wishlist"}}}},"emptyWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wishlist","url":"/gp/registry/wishlist/?ref_=nav_err_empty_wishlist"},"title":"Oops!","paragraph":"Your list is empty"}}}},"yourAccountContent":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Account","url":"/gp/css/homepage.html?ref_=nav_err_youraccount"},"title":"Oops!","paragraph":"Unable to retrieve your account"}}}},"shopAllTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"Unable to retrieve departments, please try again later"}}}},"kindleTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"Unable to retrieve list, please try again later"}}}}}); });
window.$Nav && $Nav.when("util.templates").run("FlyoutErrorTemplate", function(templates) {
      templates.add("flyoutError", "<# if(error.title) { #><span class='nav-title'><#=error.title #></span><# } #><# if(error.paragraph) { #><p class='nav-paragraph'><#=error.paragraph #></p><# } #><# if(error.button) { #><a href='<#=error.button.url #>' class='nav-action-button' ><span class='nav-action-inner'><#=error.button.text #></span></a><# } #>");
    });

    if (typeof uet == 'function') {
    uet('bb', 'iss-init-pc', {wb: 1});
  }
  if (!window.$SearchJS && window.$Nav) {
    window.$SearchJS = $Nav.make('sx');
  }

  var opts = {
    host: "completion.amazon.com/search/complete"
  , marketId: "1"
  , obfuscatedMarketId: "ATVPDKIKX0DER"
  , searchAliases: ["aps","amazon-custom-products","amazon-devices","amazonbasics","amazonfresh","amazon-pharmacy","wholefoods","allthebestpets","bartelldrugs","bristolfarms","cardenas","familyfare","freshthyme","kegnbottle","missionwinespirits","petfoodexpress","savemart","sousaswineliquors","surdyksliquorcheeseshop","weis","stripbooks","popular","apparel","electronics","sporting","sports-and-fitness","outdoor-recreation","fan-shop","garden","videogames","toys-and-games","jewelry","digital-text","digital-music","prime-digital-music","watches","grocery","hpc","instant-video","handmade","handmade-jewelry","handmade-home-and-kitchen","prime-instant-video","shop-instant-video","baby-products","office-products","software","smart-home","magazines","tools","automotive","misc","industrial","mi","pet-supplies","digital-music-track","digital-music-album","mobile","mobile-apps","movies-tv","music-artist","music-album","music-song","stripbooks-spanish","electronics-accessories","photo","audio-video","computers","furniture","kitchen","audible","audiobooks","beauty","shoes","arts-crafts","appliances","gift-cards","pets","outdoor","lawngarden","collectibles","replacement-parts","financial","fine-art","fashion","fashion-womens","fashion-womens-clothing","fashion-womens-jewelry","fashion-womens-shoes","fashion-womens-watches","fashion-womens-handbags","fashion-mens","fashion-mens-clothing","fashion-mens-jewelry","fashion-mens-shoes","fashion-mens-watches","fashion-girls","fashion-girls-clothing","fashion-girls-jewelry","fashion-girls-shoes","fashion-girls-watches","fashion-boys","fashion-boys-clothing","fashion-boys-jewelry","fashion-boys-shoes","fashion-boys-watches","fashion-baby","fashion-baby-boys","fashion-baby-girls","fashion-luggage","3d-printing","tradein-aps","todays-deals","live-explorations","local-services","vehicles","video-shorts","warehouse-deals","luxury-beauty","banjo-apps","black-friday","cyber-monday","alexa-skills","subscribe-with-amazon","courses","edu-alt-content","amazon-global-store","prime-wardrobe","under-ten-dollars","tempo","specialty-aps-sns","luxury"]
  , filterAliases: []
  , pageType: "Search"
  , requestId: "BNJYY9EBY54VZZF6X4X6"
  , sessionId: "139-5329492-5095613"
  , language: "en_US"
  , customerId: ""
  , asin: ""
  , b2b: 0
  , fresh: 0
  , isJpOrCn: 0
  , isUseAuiIss: 1
};

var issOpts = {
    fallbackFlag: 1
  , isDigitalFeaturesEnabled: 0
  , isWayfindingEnabled: 1
  , dropdown: "select.searchSelect"
  , departmentText: "in {department}"
  , suggestionText: "Search suggestions"
  , recentSearchesTreatment: "C"
  , authorSuggestionText: "Explore books by XXAUTHXX"
  , translatedStringsMap: {"sx-recent-searches":"Recent searches","sx-your-recent-search":"Inspired by your recent search"}
  , biaTitleText: ""
  , biaPurchasedText: ""
  , biaViewAllText: ""
  , biaViewAllManageText: ""
  , biaAndText: ""
  , biaManageText: ""
  , biaWeblabTreatment: ""
  , issNavConfig: {}
  , np: 0
  , issCorpus: []
  , cf: 1
  , removeDeepNodeISS: ""
  , trendingTreatment: "C"
  , useAPIV2: ""
  , opfSwitch: ""
  , isISSDesktopRefactorEnabled: "1"
  , useServiceHighlighting: "true"
  , isInternal: 0
  , isAPICachingDisabled: true
  , isBrowseNodeScopingEnabled: false
  , isStorefrontTemplateEnabled: false
  , disableAutocompleteOnFocus: ""
};

  if (opts.isUseAuiIss === 1 && window.$Nav) {
  window.$Nav.when('sx.iss').run('iss-mason-init', function(iss){
    var issInitObj = buildIssInitObject(opts, issOpts, true);
    new iss.IssParentCoordinator(issInitObj);

    $SearchJS.declare('canCreateAutocomplete', issInitObj);
  });
} else if (window.$SearchJS) {
  var iss;

  // BEGIN Deprecated globals
  var issHost = opts.host
    , issMktid = opts.marketId
    , issSearchAliases = opts.searchAliases
    , updateISSCompletion = function() { iss.updateAutoCompletion(); };
  // END deprecated globals


  $SearchJS.when('jQuery', 'search-js-autocomplete-lib').run('autocomplete-init', initializeAutocomplete);
  $SearchJS.when('canCreateAutocomplete').run('createAutocomplete', createAutocomplete);

} // END conditional for window.$SearchJS
  function initializeAutocomplete(jQuery) {
  var issInitObj = buildIssInitObject(opts, issOpts);
  $SearchJS.declare("canCreateAutocomplete", issInitObj);
} // END initializeAutocomplete
  function initSearchCsl(searchCSL, issInitObject) {
  searchCSL.init(
    opts.pageType,
    (window.ue && window.ue.rid) || opts.requestId
  );
  $SearchJS.declare("canCreateAutocomplete", issInitObject);
} // END initSearchCsl
  function createAutocomplete(issObject) {
  iss = new AutoComplete(issObject);

  $SearchJS.publish("search-js-autocomplete", iss);

  logMetrics();
} // END createAutocomplete
  function buildIssInitObject(opts, issOpts, isNewIss) {
    var issInitObj = {
        src: opts.host
      , sessionId: opts.sessionId
      , requestId: opts.requestId
      , mkt: opts.marketId
      , obfMkt: opts.obfuscatedMarketId
      , pageType: opts.pageType
      , language: opts.language
      , customerId: opts.customerId
      , fresh: opts.fresh
      , b2b: opts.b2b
      , aliases: opts.searchAliases
      , fb: issOpts.fallbackFlag
      , isDigitalFeaturesEnabled: issOpts.isDigitalFeaturesEnabled
      , isWayfindingEnabled: issOpts.isWayfindingEnabled
      , issPrimeEligible: issOpts.issPrimeEligible
      , deptText: issOpts.departmentText
      , sugText: issOpts.suggestionText
      , filterAliases: opts.filterAliases
      , biaWidgetUrl: opts.biaWidgetUrl
      , recentSearchesTreatment: issOpts.recentSearchesTreatment
      , authorSuggestionText: issOpts.authorSuggestionText
      , translatedStringsMap: issOpts.translatedStringsMap
      , biaTitleText: ""
      , biaPurchasedText: ""
      , biaViewAllText: ""
      , biaViewAllManageText: ""
      , biaAndText: ""
      , biaManageText: ""
      , biaWeblabTreatment: ""
      , issNavConfig: issOpts.issNavConfig
      , cf: issOpts.cf
      , ime: opts.isJpOrCn
      , mktid: opts.marketId
      , qs: opts.isJpOrCn
      , issCorpus: issOpts.issCorpus
      , deepNodeISS: {
          searchAliasAccessor: function($) {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAlias()) ||
                   $('select.searchSelect').children().attr('data-root-alias');
          },
          searchAliasDisplayNameAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAliasDisplayName());
          }
        }
      , removeDeepNodeISS: issOpts.removeDeepNodeISS
      , trendingTreatment: issOpts.trendingTreatment
      , useAPIV2: issOpts.useAPIV2
      , opfSwitch: issOpts.opfSwitch
      , isISSDesktopRefactorEnabled: issOpts.isISSDesktopRefactorEnabled
      , useServiceHighlighting: issOpts.useServiceHighlighting
      , isInternal: issOpts.isInternal
      , isAPICachingDisabled: issOpts.isAPICachingDisabled
      , isBrowseNodeScopingEnabled: issOpts.isBrowseNodeScopingEnabled
      , isStorefrontTemplateEnabled: issOpts.isStorefrontTemplateEnabled
      , disableAutocompleteOnFocus: issOpts.disableAutocompleteOnFocus
      , asin: opts.asin
    };
  
    // If we aren't using the new ISS then we need to add these properties
    
    if (!isNewIss) {
      issInitObj.dd = issOpts.dropdown; // The element with id searchDropdownBox doesn't exist in C.
      issInitObj.imeSpacing = issOpts.imeSpacing;
      issInitObj.isNavInline = 1;
      issInitObj.triggerISSOnClick = 0;
      issInitObj.sc = 1;
      issInitObj.np = issOpts.np;
    }
  
    return issInitObj;
  } // END buildIssInitObject
  function logMetrics() {
  if (typeof uet == 'function' && typeof uex == 'function') {
      uet('be', 'iss-init-pc',
          {
              wb: 1
          });
      uex('ld', 'iss-init-pc',
          {
              wb: 1
          });
  }
} // END logMetrics
  
    
window.$Nav && $Nav.declare('config.navDeviceType','desktop');

window.$Nav && $Nav.declare('config.navDebugHighres',false);

window.$Nav && $Nav.declare('config.pageType','Search');
window.$Nav && $Nav.declare('config.subPageType','List');

window.$Nav && $Nav.declare('config.dynamicMenuUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdynamic\x2Dmenu.html');

window.$Nav && $Nav.declare('config.dismissNotificationUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdismissnotification.html');

window.$Nav && $Nav.declare('config.enableDynamicMenus',true);

window.$Nav && $Nav.declare('config.isInternal',false);

window.$Nav && $Nav.declare('config.isBackup',false);

window.$Nav && $Nav.declare('config.isRecognized',false);

window.$Nav && $Nav.declare('config.transientFlyoutTrigger','\x23nav\x2Dtransient\x2Dflyout\x2Dtrigger');

window.$Nav && $Nav.declare('config.subnavFlyoutUrl','\x2Fnav\x2Fajax\x2FsubnavFlyout');
window.$Nav && $Nav.declare('config.isSubnavFlyoutMigrationEnabled',true);

window.$Nav && $Nav.declare('config.recordEvUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Frecordevent.html');
window.$Nav && $Nav.declare('config.recordEvInterval',15000);
window.$Nav && $Nav.declare('config.sessionId','139\x2D5329492\x2D5095613');
window.$Nav && $Nav.declare('config.requestId','BNJYY9EBY54VZZF6X4X6');

window.$Nav && $Nav.declare('config.alexaListEnabled',true);

window.$Nav && $Nav.declare('config.readyOnATF',true);

window.$Nav && $Nav.declare('config.dynamicMenuArgs',{"rid":"BNJYY9EBY54VZZF6X4X6","isFullWidthPrime":0,"isPrime":0,"dynamicRequest":1,"weblabs":"","isFreshRegionAndCustomer":"","primeMenuWidth":310});

window.$Nav && $Nav.declare('config.customerName',false);

window.$Nav && $Nav.declare('config.customerCountryCode','AR');

window.$Nav && $Nav.declare('config.yourAccountPrimeURL',null);

window.$Nav && $Nav.declare('config.yourAccountPrimeHover',true);

window.$Nav && $Nav.declare('config.searchBackState',{});

window.$Nav && $Nav.declare('nav.inline');

(function (i) {
  if(window._navbarSpriteUrl) {
    i.onload = function() {window.uet && uet('ne')};
    i.src = window._navbarSpriteUrl;
  }
}(new Image()));

window.$Nav && $Nav.declare('config.autoFocus',false);

window.$Nav && $Nav.declare('config.responsiveTouchAgents',["ieTouch"]);

window.$Nav && $Nav.declare('config.responsiveGW',false);

window.$Nav && $Nav.declare('config.pageHideEnabled',false);

window.$Nav && $Nav.declare('config.sslTriggerType','flyoutProximityLarge');
window.$Nav && $Nav.declare('config.sslTriggerRetry',0);

window.$Nav && $Nav.declare('config.doubleCart',false);

window.$Nav && $Nav.declare('config.signInOverride',true);

window.$Nav && $Nav.declare('config.signInTooltip',false);

window.$Nav && $Nav.declare('config.isPrimeMember',false);

window.$Nav && $Nav.declare('config.packardGlowTooltip',false);

window.$Nav && $Nav.declare('config.packardGlowFlyout',false);

window.$Nav && $Nav.declare('config.rightMarginAlignEnabled',true);

window.$Nav && $Nav.declare('config.flyoutAnimation',false);

window.$Nav && $Nav.declare('config.campusActivation','null');

window.$Nav && $Nav.declare('config.primeTooltip',false);

window.$Nav && $Nav.declare('config.primeDay',false);

window.$Nav && $Nav.declare('config.disableBuyItAgain',false);

window.$Nav && $Nav.declare('config.enableCrossShopBiaFlyout',false);

window.$Nav && $Nav.declare('config.pseudoPrimeFirstBrowse',null);

window.$Nav && $Nav.declare('config.sdaYourAccount',false);

window.$Nav && $Nav.declare('config.csYourAccount',{"url":"/gp/youraccount/navigation/sidepanel"});

window.$Nav && $Nav.declare('config.cartFlyoutDisabled',true);

window.$Nav && $Nav.declare('config.isTabletBrowser',false);

window.$Nav && $Nav.declare('config.HmenuProximityArea',[200,200,200,200]);

window.$Nav && $Nav.declare('config.HMenuIsProximity',true);

window.$Nav && $Nav.declare('config.isPureAjaxALF',false);

window.$Nav && $Nav.declare('config.accountListFlyoutRedesign',false);

window.$Nav && $Nav.declare('config.navfresh',false);

window.$Nav && $Nav.declare('config.isFreshRegion',false);

if (window.ue && ue.tag) { ue.tag('navbar'); };

window.$Nav && $Nav.declare('config.blackbelt',true);

window.$Nav && $Nav.declare('config.beaconbelt',true);

window.$Nav && $Nav.declare('config.accountList',true);

window.$Nav && $Nav.declare('config.iPadTablet',false);

window.$Nav && $Nav.declare('config.searchapiEndpoint',false);

window.$Nav && $Nav.declare('config.timeline',false);

window.$Nav && $Nav.declare('config.timelineAsinPriceEnabled',false);

window.$Nav && $Nav.declare('config.timelineDeleteEnabled',false);



window.$Nav && $Nav.declare('config.extendedFlyout',false);

window.$Nav && $Nav.declare('config.flyoutCloseDelay',600);

window.$Nav && $Nav.declare('config.pssFlag',0);

window.$Nav && $Nav.declare('config.isPrimeTooltipMigrated',false);

window.$Nav && $Nav.declare('config.isDynamicWishListMigrationEnabled',true);

window.$Nav && $Nav.declare('config.hashCustomerAndSessionId','45f426108b40eda929af97dacd4140df972747a9');

window.$Nav && $Nav.declare('config.isExportMode',true);

window.$Nav && $Nav.declare('config.languageCode','en_US');

window.$Nav && $Nav.declare('config.environmentVFI','AmazonNavigationCards\x2Fdevelopment\x40B6124830925\x2DAL2_x86_64');



window.$Nav && $Nav.declare('config.isHMenuBrowserCacheDisable',false);

window.$Nav && $Nav.declare('config.signInUrlWithRefTag','https\x3A\x2F\x2Fwww.amazon.com\x2Fap\x2Fsignin\x3Fopenid.pape.max_auth_age\x3D0\x26openid.return_to\x3Dhttps\x253A\x252F\x252Fwww.amazon.com\x252Fs\x252F\x253F_encoding\x253DUTF8\x2526dc\x253D\x2526ds\x253Dv1\x25253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8\x2526hvadid\x253D623182854892\x2526hvdev\x253Dc\x2526hvlocint\x253D9061323\x2526hvlocphy\x253D1000060\x2526hvnetw\x253Dg\x2526hvqmt\x253Db\x2526hvrand\x253D6662995798799223789\x2526hvtargid\x253Dkwd\x2D13263126\x2526hydadcr\x253D20698_13296112\x2526i\x253Dstripbooks\x2526k\x253Dbookstore\x252520amazon\x2526qid\x253D1682200770\x2526ref\x253Dsr_nr_p_n_condition\x2Dtype_1\x2526rh\x253Dn\x25253A283155\x25252Cn\x25253A17\x25252Cp_n_condition\x2Dtype\x25253A6461716011\x2526rnid\x253D6461714011\x2526tag\x253Dgooghydr\x2D20\x2526ref_\x253DnavSignInUrlRefTagPlaceHolder\x26openid.identity\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.assoc_handle\x3Dusflex\x26openid.mode\x3Dcheckid_setup\x26openid.claimed_id\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.ns\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x26');

window.$Nav && $Nav.declare('config.isSmile',false);

window.$Nav && $Nav.declare('config.regionalStores',[]);

window.$Nav && $Nav.declare('config.isALFRedesignPT2',true);

window.$Nav && $Nav.declare('config.isNavALFRegistryGiftList',false);

window.$Nav && $Nav.declare('config.marketplaceId','ATVPDKIKX0DER');

window.$Nav && $Nav.declare('config.exportTransitionState','none');

window.$Nav && $Nav.declare('config.enableAeeXopFlyout',false);

window.$Nav && $Nav.declare('config.isPrimeFlyoutMigrationEnabled',false);

window.$Nav && $Nav.declare('config.isAjaxMigrated',true);

window.$Nav && $Nav.declare('config.isAjaxSubnavFlyoutMigrated',true);

window.$Nav && $Nav.declare('config.isAjaxRefTagLoggerMigrated',true);

if (window.P && typeof window.P.declare === "function" && typeof window.P.now === "function") {
  window.P.now('packardGlowIngressJsEnabled').execute(function(glowEnabled) {
    if (!glowEnabled) {
      window.P.declare('packardGlowIngressJsEnabled', true);
    }
  });
  window.P.now('packardGlowStoreName').execute(function(storeName) {
    if (!storeName) {
      window.P.declare('packardGlowStoreName','books');
    }
  });
}

window.$Nav && $Nav.declare('configComplete');

    -->
</script>


<a id="skippedLink" tabindex="-1"></a>

<script type="text/javascript">window.navmet.MainEnd = new Date();</script>
<script type="text/javascript">
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainEnd",end:+new Date(),begin:window.ue_t0});
    }
</script>
<!-- sp:end-feature:navbar -->
<!-- sp:feature:host-atf -->


<div id="search">
    








    
    
    
        







<script>P.declare('s\-clean\-url', "\/s?k=bookstore+amazon\x26i=stripbooks\x26rh=n%3A283155%2Cn%3A17%2Cp_n_condition\-type%3A6461716011\x26dc\x26ds=v1%3A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8\x26hvadid=623182854892\x26hvdev=c\x26hvlocint=9061323\x26hvlocphy=1000060\x26hvnetw=g\x26hvqmt=b\x26hvrand=6662995798799223789\x26hvtargid=kwd\-13263126\x26hydadcr=20698_13296112\x26qid=1682200770\x26rnid=6461714011\x26tag=googhydr\-20\x26ref=sr_nr_p_n_condition\-type_1");</script>
<script>P.declare('s\-device\-env', "WEB");</script>


<script>P.declare('aapi\-token\-dcp', "1@g+\/y9WnQUwlfC8a4PPIrgvTZYpspisI55wLLMB3EiLyMAAAAAQAAAABkRFjIcmF3AAAAAGfA1H5nd8xGEcC32Fh1BA==@NFT8IE");</script>
<script>P.declare('s\-swrs\-version', "859EEEE7101FC1BA625B83656D7B4D01,D41D8CD98F00B204E9800998ECF8427E");</script>
<script>P.declare('s\-navbar\-prefetch\-config', {"pauseEnabled":false,"pauseTimeout":0,"minKeywordLen":0});</script>
<script>P.declare('s\-ajax\-calls\-via\-http\-post\-enabled', true);</script>
<script>P.declare('s\-ajax\-customer\-action\-flagging\-enabled', true);</script>


<script>P.declare('s\-metadata', {"totalResultCount":62815,"asinOnPageCount":24,"searchAlias":"stripbooks","keywords":"bookstore amazon","store":"books","merchantId":"","merchantName":"","placeholderText":"","rid":"BNJYY9EBY54VZZF6X4X6","page":1,"rescopeParameter":"n","rescopeNode":"17","persistSearchScopeInMShop":false,"scopedCategoryName":"","sid":"139\-5329492\-5095613","cid":"","locale":"en_US","marketplaceId":"ATVPDKIKX0DER"});</script>



    

    



<span data-component-type="s-result-info-bar" class="rush-component" data-component-id="3">
    
    
        <div data-uuid="7eb5090d-1e2a-4f48-8d7b-11d87c1f7294" cel_widget_id="UPPER-RESULT_INFO_BAR-0" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=UPPER template=RESULT_INFO_BAR widgetId=result-info-bar" data-csa-c-id="bnyj82-ohr643-u71irg-8uug88" data-cel-widget="UPPER-RESULT_INFO_BAR-0">








    
        <h1 class="a-size-base s-desktop-toolbar a-text-normal">
            <div class="s-desktop-width-max sg-row-align-items-center s-wide-grid-style-t2 s-wide-grid-style sg-row">
        <div class="sg-col-14-of-20 sg-col-18-of-24 sg-col s-breadcrumb sg-col-10-of-16 sg-col-6-of-12"><div class="sg-col-inner">
            <div class="a-section a-spacing-small a-spacing-top-small">
                <span>1-24 of over 60,000 results for</span><span> </span><span class="a-color-state a-text-bold">"bookstore amazon"</span>
            </div>
        </div></div>
        <div class="sg-col-6-of-20 sg-col sg-col-6-of-16 sg-col-6-of-24 sg-col-6-of-12"><div class="sg-col-inner">
            <div class="a-section a-spacing-small a-spacing-top-small a-text-right">
                






<form method="get" action="/s" class="aok-inline-block a-spacing-none">
    
        <input type="hidden" name="k" value="bookstore amazon">
    
        <input type="hidden" name="i" value="stripbooks">
    
        <input type="hidden" name="rh" value="n:283155,n:17,p_n_condition-type:6461716011">
    
        <input type="hidden" name="dc" value="">
    
        <input type="hidden" name="hvadid" value="623182854892">
    
        <input type="hidden" name="hvdev" value="c">
    
        <input type="hidden" name="hvlocint" value="9061323">
    
        <input type="hidden" name="hvlocphy" value="1000060">
    
        <input type="hidden" name="hvnetw" value="g">
    
        <input type="hidden" name="hvqmt" value="b">
    
        <input type="hidden" name="hvrand" value="6662995798799223789">
    
        <input type="hidden" name="hvtargid" value="kwd-13263126">
    
        <input type="hidden" name="hydadcr" value="20698_13296112">
    
        <input type="hidden" name="qid" value="1682200775">
    
        <input type="hidden" name="rnid" value="6461714011">
    
        <input type="hidden" name="tag" value="googhydr-20">
    
        <input type="hidden" name="ref" value="sr_nr_p_n_condition-type_1">
    
    <span class="a-dropdown-container"><label for="s-result-sort-select" class="a-native-dropdown">Sort by:</label><select name="s" autocomplete="off" id="s-result-sort-select" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative">
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=relevancerank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_relevancerank&amp;ds=v1%3Adq7y0iHsne82aD9Ang6ni0sdzHkPFHcZqpda4q%2Fgadk" value="relevancerank" selected="">Featured</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=price-asc-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_price-asc-rank&amp;ds=v1%3APb1gNOzhX1MWCcJJRIyuuczk3F9y7dvMUWedpGpFYE4" value="price-asc-rank">Price: Low to High</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=price-desc-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_price-desc-rank&amp;ds=v1%3A0DSnCOrUcD8yoApDaNOOxiaHo1BYSZ0Wv8AKJuADjAs" value="price-desc-rank">Price: High to Low</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=review-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_review-rank&amp;ds=v1%3AAek5sVcEhKOYZ%2FqSiJjMz9LWWkKqtYJ%2FPK9DO57Htsw" value="review-rank">Avg. Customer Review</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=date-desc-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_date-desc-rank&amp;ds=v1%3A58USaEOZpx79iF507zw3K3QCVw21KAzXxkSlVHboiKg" value="date-desc-rank">Publication Date</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=review-count-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_review-count-rank&amp;ds=v1%3Ak%2FWhcNpVoB8GYoVB2ruEuq%2BUYJT642mg6QyhIubEG3o" value="review-count-rank">Most reviews</option>
        
            <option data-url="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;s=exact-aware-popularity-rank&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_st_exact-aware-popularity-rank&amp;ds=v1%3A%2BwRu71WrC5yTQ9PXgHwdp0LSOK531iaIfoKMDLSB4WM" value="exact-aware-popularity-rank">Best Sellers</option>
        
    </select><span tabindex="-1" aria-label="Sort by:" class="a-button a-button-dropdown a-button-small" aria-hidden="true" id="a-autoid-0" style="min-width: 0%;"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true" data-csa-c-id="1xduzi-quwiqe-iav6fj-vahbxf" id="a-autoid-0-announce"><span class="a-dropdown-label">Sort by:</span><span class="a-dropdown-prompt">Featured</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span>
    <noscript><span class="a-button a-button-base"><span class="a-button-inner"><input class="a-button-input" type="submit" value="Go"/><span class="a-button-text" aria-hidden="true">Go</span></span></span></noscript>
</form>

            </div>
        </div></div>
    </div>
        </h1>
    
    

</div>
    
</span>

<div class="s-desktop-width-max s-desktop-content s-wide-grid-style-t2 s-opposite-dir s-wide-grid-style sg-row">
      <div class="sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16"><div class="sg-col-inner">
          <div id="s-skipLinkTargetForMainSearchResults" tabindex="-1"></div>

          
          <span data-component-type="s-search-results" class="rush-component s-latency-cf-section" data-component-id="4">
              
              <div class="s-main-slot s-result-list s-search-results sg-row">
                  






    <div data-asin="" data-index="0" class="a-section a-spacing-none s-result-item s-flex-full-width s-border-bottom-none s-widget s-widget-spacing-large" data-cel-widget="search_result_0"><div data-uuid="e0b032de-e72a-4729-8e70-108b799f1d1f" cel_widget_id="MAIN-TOP_BANNER_MESSAGE-0" class="s-widget-container s-spacing-mini s-widget-container-height-mini celwidget slot=MAIN template=TOP_BANNER_MESSAGE widgetId=messaging-messages-results-header-builder" data-csa-c-id="b2g2w9-3dv2p6-t70inv-70ec54" data-cel-widget="MAIN-TOP_BANNER_MESSAGE-0">



<span data-component-type="s-messaging-widget-results-header" class="rush-component" data-component-id="1">
    <div class="a-section a-spacing-none s-messaging-widget-results-header">
        <div tabindex="0" class="s-no-outline">
            <span class="a-size-medium-plus a-color-base a-text-bold">Results</span>
        </div>
    </div>
</span>
</div></div>

    
    
    

    

    <div data-asin="0778361055" data-index="1" data-uuid="4dc0976c-fc9a-4cca-aa0e-312053eb27e5" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="5" data-cel-widget="search_result_1"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-1" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1" data-csa-c-pos="1" data-csa-c-item-id="amzn1.asin.1.0778361055" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="sh2mz5-l67dk6-q0fj72-dfqa11" data-cel-widget="MAIN-SEARCH_RESULTS-1"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276800011&amp;pinnedAsins=0778361055"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;0778361055&quot;}" data-component-id="6"><div class="a-row a-badge-region"><span id="0778361055-gift-guide" class="a-badge" aria-labelledby="0778361055-gift-guide-label 0778361055-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="0778361055-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="0778361055-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Romance</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="7"><a class="a-link-normal s-no-outline" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778361055/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/91myaLomiyL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Bookstore on the Beach: A Novel" data-image-index="1" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778361055/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1"><span class="a-size-base-plus a-color-base a-text-normal">The </span> <span class="a-size-base-plus a-color-base a-text-bold a-text-normal">Bookstore</span> <span class="a-size-base-plus a-color-base a-text-normal"> on the Beach: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Brenda-Novak/e/B001IGNW9G?ref=sr_ntt_srch_lnk_1&amp;qid=1682200775&amp;sr=1-1">Brenda Novak</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.5 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=0778361055&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="ak0ugg-26ni3j-33etzp-glumc1"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.5 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="3,250"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778361055/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1#customerReviews"><span class="a-size-base s-underline-text">3,250</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778361055/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778361055/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.95</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">95</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$16.99</span><span aria-hidden="true">$16.99</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$1.18</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/0778361055/ref=sr_1_1_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-1&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_1_aod?asin=0778361055&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-1&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="zzyi0-t8g6zh-skbyll-glx2u0"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/0778361055/ref=sr_1_1_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-1&amp;hvrand=6662995798799223789">(109 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="mq1el7-c6f5ad-e3djtd-1oug8z"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/The-Bookstore-on-the-Beach/dp/B089ZHHX82/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Beach-Novel-Brenda-Novak-ebook/dp/B08D3R45CG/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778311759/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Mass Market Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Beach-Novel-Brenda-Novak/dp/0778311384/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Beach-Brenda-Novak/dp/1799960293/ref=sr_1_1?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-1">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1250037751" data-index="2" data-uuid="b403bd26-1be6-427f-9928-2fd1944ad26e" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="8" data-cel-widget="search_result_2"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-2" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_2" data-csa-c-pos="2" data-csa-c-item-id="amzn1.asin.1.1250037751" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="fpniae-1wz5em-1zh7ck-tjo89j" data-cel-widget="MAIN-SEARCH_RESULTS-2"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276797011&amp;pinnedAsins=1250037751"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;1250037751&quot;}" data-component-id="9"><div class="a-row a-badge-region"><span id="1250037751-gift-guide" class="a-badge" aria-labelledby="1250037751-gift-guide-label 1250037751-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1250037751-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="1250037751-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Literature &amp; Fiction</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="10"><a class="a-link-normal s-no-outline" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1250037751/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81ehEnDuFmL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Mr. Penumbra's 24-Hour Bookstore" data-image-index="2" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1250037751/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2"><span class="a-size-base-plus a-color-base a-text-normal">Mr. Penumbra's 24-Hour </span> <span class="a-size-base-plus a-color-base a-text-bold a-text-normal">Bookstore</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Robin-Sloan/e/B004G7KNN2?ref=sr_ntt_srch_lnk_2&amp;qid=1682200775&amp;sr=1-2">Robin Sloan</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.2 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1250037751&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="6gsaey-9tcpd0-r9w382-v67d5u"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"><span class="a-icon-alt">4.2 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="12,769"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1250037751/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2#customerReviews"><span class="a-size-base s-underline-text">12,769</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1250037751/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1250037751/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.39</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">39</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$18.00</span><span aria-hidden="true">$18.00</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$1.24</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1250037751/ref=sr_1_2_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-2&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_2_aod?asin=1250037751&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-2&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="ol4mms-mpoxyr-pgib8a-ymkbv5"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1250037751/ref=sr_1_2_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-2&amp;hvrand=6662995798799223789">(220 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="t4q2e9-hoax0o-ng5fjs-24g9nd"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Mr-Penumbras-24-Hour-Bookstore-audiobook/dp/B009KF05D8/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Mr-Penumbras-24-Hour-Bookstore-Novel-ebook/dp/B008FPOIT6/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/0374214913/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Mr-Penumbras-24-Hour-Bookstore-Novel/dp/1427233748/ref=sr_1_2?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-2">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1501116851" data-index="3" data-uuid="dbcdf2d0-4d31-4250-a8b0-cdd1d48e9c9e" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="11" data-cel-widget="search_result_3"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-3" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_3" data-csa-c-pos="3" data-csa-c-item-id="amzn1.asin.1.1501116851" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="yd84ia-uhzth6-gug4oc-nns6wb" data-cel-widget="MAIN-SEARCH_RESULTS-3"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=tv_grch_bg&amp;node=23579471011&amp;pinnedAsins=1501116851"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;1501116851&quot;}" data-component-id="12"><div class="a-row a-badge-region"><span id="1501116851-gift-guide" class="a-badge" aria-labelledby="1501116851-gift-guide-label 1501116851-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1501116851-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Goodreads Choice</span></span></span><span id="1501116851-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Award nominee</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="13"><a class="a-link-normal s-no-outline" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1501116851/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/613Nx847GDL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Midnight at the Bright Ideas Bookstore: A Novel" data-image-index="3" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1501116851/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3"><span class="a-size-base-plus a-color-base a-text-normal">Midnight at the Bright Ideas </span> <span class="a-size-base-plus a-color-base a-text-bold a-text-normal">Bookstore</span> <span class="a-size-base-plus a-color-base a-text-normal">: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Matthew-Sullivan/e/B06X418ZD3?ref=sr_ntt_srch_lnk_3&amp;qid=1682200775&amp;sr=1-3">Matthew Sullivan</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.2 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1501116851&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="yfztr1-5i7idu-qs6i8y-gs2aow"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"><span class="a-icon-alt">4.2 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="4,342"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1501116851/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3#customerReviews"><span class="a-size-base s-underline-text">4,342</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1501116851/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1501116851/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$14.19</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">19</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$18.00</span><span aria-hidden="true">$18.00</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$1.33</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1501116851/ref=sr_1_3_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-3&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_3_aod?asin=1501116851&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-3&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="rrtmk3-ly7i9c-9h9rte-7i1afp"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1501116851/ref=sr_1_3_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-3&amp;hvrand=6662995798799223789">(150 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="rtv96u-6th6mn-4vlsmd-fgzddr"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Midnight-Bright-Ideas-Bookstore-Novel-ebook/dp/B01MDTCBVZ/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/B071VTRF45/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Midnight-Bright-Ideas-Bookstore-Thorndike/dp/1432842560/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Midnight-Bright-Ideas-Bookstore-Novel/dp/1508285039/ref=sr_1_3?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-3">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B0BB52CCND" data-index="4" data-uuid="7d37c49a-89a7-4069-abde-38b7f4e79e24" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="14" data-cel-widget="search_result_4"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-4" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_4" data-csa-c-pos="4" data-csa-c-item-id="amzn1.asin.1.B0BB52CCND" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="hxopdt-66jw93-pz6yne-6cw3et" data-cel-widget="MAIN-SEARCH_RESULTS-4"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;B0BB52CCND&quot;}" data-component-id="15"><div class="a-row a-badge-region"><span id="B0BB52CCND-best-seller" class="a-badge" aria-labelledby="B0BB52CCND-best-seller-label B0BB52CCND-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B0BB52CCND-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="B0BB52CCND-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Single Authors Short Stories</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="16"><a class="a-link-normal s-no-outline" href="/Bookstore-Sisters-Short-Story-ebook/dp/B0BB52CCND/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81OrrjDgaSL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Bookstore Sisters: A Short Story" data-image-index="4" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Bookstore-Sisters-Short-Story-ebook/dp/B0BB52CCND/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4"><span class="a-size-base-plus a-color-base a-text-normal">The </span> <span class="a-size-base-plus a-color-base a-text-bold a-text-normal">Bookstore</span> <span class="a-size-base-plus a-color-base a-text-normal"> Sisters: A Short Story</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Alice-Hoffman/e/B000AQ05CC?ref=sr_ntt_srch_lnk_4&amp;qid=1682200775&amp;sr=1-4">Alice Hoffman</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B0BB52CCND&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="wp7syi-kicnx5-cnr6sk-u5aztj"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="34,120"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Sisters-Short-Story-ebook/dp/B0BB52CCND/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4#customerReviews"><span class="a-size-base s-underline-text">34,120</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Bookstore-Sisters-Short-Story-ebook/dp/B0BB52CCND/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Bookstore-Sisters-Short-Story-ebook/dp/B0BB52CCND/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$0.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">0<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> </a> <span class="a-letter-space"></span><span class="aok-inline-block s-image-logo-view"><span class="aok-relative s-icon-text-small"><i class="a-icon a-icon-kindle-unlimited a-icon-small" role="img" aria-label="Kindle Unlimited."></i></span><span></span></span> </div><div class="a-row a-size-small a-color-secondary"><span>Free with Kindle Unlimited membership </span><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/ku2?passThroughAsin=B0BB52CCND&amp;ref_=mbs_ku_lp">Join Now</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span>Or $1.99 to buy</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other format: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Bookstore-Sisters-Short-Story/dp/B0BFXJSYBT/ref=sr_1_4?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-4">Audible Audiobook</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09ZN4WVQJ" data-index="5" data-uuid="2c1d3be4-b8a5-43cc-8b53-f0489c0ad4ea" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="17" data-cel-widget="search_result_5"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-5" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_5" data-csa-c-pos="5" data-csa-c-item-id="amzn1.asin.1.B09ZN4WVQJ" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="cyxqno-8z3581-3r730b-5b6g71" data-cel-widget="MAIN-SEARCH_RESULTS-5"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;B09ZN4WVQJ&quot;}" data-component-id="18"><div class="a-row a-badge-region"><span id="B09ZN4WVQJ-best-seller" class="a-badge" aria-labelledby="B09ZN4WVQJ-best-seller-label B09ZN4WVQJ-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B09ZN4WVQJ-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="B09ZN4WVQJ-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Legal Thrillers</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="19"><a class="a-link-normal s-no-outline" href="/Boys-Biloxi-Legal-Thriller/dp/B09ZN4WVQJ/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/71SsE2GRElL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Boys from Biloxi: A Legal Thriller" data-image-index="5" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Boys-Biloxi-Legal-Thriller/dp/B09ZN4WVQJ/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5"><span class="a-size-base-plus a-color-base a-text-normal">The Boys from Biloxi: A Legal Thriller</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><span class="a-size-base">John Grisham</span><span class="a-size-base">, </span><span class="a-size-base">Michael Beck</span><span class="a-size-base">, et al.</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.4 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09ZN4WVQJ&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="hnok89-9vmmlf-tds26t-q0hv75"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="47,617"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller/dp/B09ZN4WVQJ/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5#customerReviews"><span class="a-size-base s-underline-text">47,617</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Boys-Biloxi-Legal-Thriller/dp/B09ZN4WVQJ/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Audible Audiobook</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-mini a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Boys-Biloxi-Legal-Thriller/dp/B09ZN4WVQJ/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$0.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">0<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary"> </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$35.00</span><span aria-hidden="true">$35.00</span></span></div> </a> </div><div class="a-row a-size-small a-color-secondary"><span class="a-color-secondary">Free with Audible trial</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller-ebook/dp/B09ZK4KVTX/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller/dp/0385548923/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller/dp/059346950X/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller/dp/0593607449/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Audio CD</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Boys-Biloxi-Legal-Thriller/dp/B0BKZYQ6Y8/ref=sr_1_5?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-5">Mass Market Paperback</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09QKSLPN9" data-index="6" data-uuid="1cccf87d-dfa0-4bfb-8c49-16b11dae740c" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="20" data-cel-widget="search_result_6"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-6" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_6" data-csa-c-pos="6" data-csa-c-item-id="amzn1.asin.1.B09QKSLPN9" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="e0byjs-hc44w1-kgin3q-egab96" data-cel-widget="MAIN-SEARCH_RESULTS-6"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276798011&amp;pinnedAsins=B09QKSLPN9"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;B09QKSLPN9&quot;}" data-component-id="21"><div class="a-row a-badge-region"><span id="B09QKSLPN9-gift-guide" class="a-badge" aria-labelledby="B09QKSLPN9-gift-guide-label B09QKSLPN9-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B09QKSLPN9-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="B09QKSLPN9-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Mystery, Thriller &amp; Suspense</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="22"><a class="a-link-normal s-no-outline" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch-ebook/dp/B09QKSLPN9/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/7165XmbMsAL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Desert Star (Renée Ballard Book 5)" data-image-index="6" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch-ebook/dp/B09QKSLPN9/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6"><span class="a-size-base-plus a-color-base a-text-normal">Desert Star (Renée Ballard Book 5)</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B07S9TJLRZ?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-6"><span>Book 5 of 5: Renée Ballard</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.7 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09QKSLPN9&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="k89s6x-k88ymc-hfl9j3-wnkm48"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.7 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="44,605"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch-ebook/dp/B09QKSLPN9/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6#customerReviews"><span class="a-size-base s-underline-text">44,605</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch-ebook/dp/B09QKSLPN9/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch-ebook/dp/B09QKSLPN9/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$14.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">Print List Price: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$29.00</span><span aria-hidden="true">$29.00</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-Desert-Star/dp/B09X295Y68/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch/dp/0316485659/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch/dp/1538725010/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Desert-Ren%C3%A9e-Ballard-Harry-Bosch/dp/1668602687/ref=sr_1_6?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-6">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09G9D94VW" data-index="7" data-uuid="a61203bc-936d-4ed8-b621-95f4b7bd0166" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="23" data-cel-widget="search_result_7"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-7" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_7" data-csa-c-pos="7" data-csa-c-item-id="amzn1.asin.1.B09G9D94VW" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="4hwwd9-6tqkcb-97c5le-kxhq1n" data-cel-widget="MAIN-SEARCH_RESULTS-7"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;B09G9D94VW&quot;}" data-component-id="24"><div class="a-row a-badge-region"><span id="B09G9D94VW-best-seller" class="a-badge" aria-labelledby="B09G9D94VW-best-seller-label B09G9D94VW-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B09G9D94VW-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="B09G9D94VW-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Animal Fiction</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="25"><a class="a-link-normal s-no-outline" href="/Horse-Novel-Geraldine-Brooks-ebook/dp/B09G9D94VW/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81P0W3YcvXL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Horse: A Novel" data-image-index="7" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Horse-Novel-Geraldine-Brooks-ebook/dp/B09G9D94VW/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7"><span class="a-size-base-plus a-color-base a-text-normal">Horse: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Geraldine-Brooks/e/B000APM13Y?ref=sr_ntt_srch_lnk_7&amp;qid=1682200775&amp;sr=1-7">Geraldine Brooks</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.6 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09G9D94VW&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="eeo8i6-hhtb76-tfg53j-j6plnj"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="22,692"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Horse-Novel-Geraldine-Brooks-ebook/dp/B09G9D94VW/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7#customerReviews"><span class="a-size-base s-underline-text">22,692</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Horse-Novel-Geraldine-Brooks-ebook/dp/B09G9D94VW/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Horse-Novel-Geraldine-Brooks-ebook/dp/B09G9D94VW/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$13.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">Digital List Price: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$14.99</span><span aria-hidden="true">$14.99</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-Horse-A-Novel/dp/B09HRDB3C6/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Horse-Novel-Geraldine-Brooks/dp/0399562966/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Horse-Novel-Random-House-Large/dp/0593556488/ref=sr_1_7?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-7">Paperback</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09QH6C42C" data-index="8" data-uuid="c93e9eda-bbc7-43a4-8125-27a447007aea" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="26" data-cel-widget="search_result_8"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-8" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_8" data-csa-c-pos="8" data-csa-c-item-id="amzn1.asin.1.B09QH6C42C" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="haahxz-tfywu9-n952q6-fyfwu8" data-cel-widget="MAIN-SEARCH_RESULTS-8"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;B09QH6C42C&quot;}" data-component-id="27"><div class="a-row a-badge-region"><span id="B09QH6C42C-best-seller" class="a-badge" aria-labelledby="B09QH6C42C-best-seller-label B09QH6C42C-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B09QH6C42C-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="B09QH6C42C-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Small Town &amp; Rural Fiction</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="28"><a class="a-link-normal s-no-outline" href="/Audible-Demon-Copperhead-A-Novel/dp/B09QH6C42C/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/91bS0lS-JUL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Demon Copperhead: A Novel" data-image-index="8" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Audible-Demon-Copperhead-A-Novel/dp/B09QH6C42C/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8"><span class="a-size-base-plus a-color-base a-text-normal">Demon Copperhead: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><span class="a-size-base">Barbara Kingsolver</span><span class="a-size-base">, </span><span class="a-size-base">Charlie Thurston</span><span class="a-size-base">, et al.</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.6 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09QH6C42C&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="c4a2ns-6ai61d-45u5ib-84jeuw"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="32,288"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-Demon-Copperhead-A-Novel/dp/B09QH6C42C/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8#customerReviews"><span class="a-size-base s-underline-text">32,288</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Audible-Demon-Copperhead-A-Novel/dp/B09QH6C42C/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8">Audible Audiobook</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-mini a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Audible-Demon-Copperhead-A-Novel/dp/B09QH6C42C/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$0.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">0<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary"> </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$34.90</span><span aria-hidden="true">$34.90</span></span></div> </a> </div><div class="a-row a-size-small a-color-secondary"><span class="a-color-secondary">Free with Audible trial</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-base"><span>Ages: 9 years and up</span><br><br></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Demon-Copperhead-Novel-Barbara-Kingsolver-ebook/dp/B09QMHZ53K/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Demon-Copperhead-Novel-Barbara-Kingsolver/dp/0063251922/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Demon-Copperhead-Novel-Barbara-Kingsolver/dp/B0B14MBL41/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8">Audio CD</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Demon-Copperhead-Novel-Barbara-Kingsolver/dp/0063251981/ref=sr_1_8?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-8">Paperback</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B0B7R4Q5DJ" data-index="9" data-uuid="d75e4b36-a9e5-41aa-aef7-49546fbb9df9" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="29" data-cel-widget="search_result_9"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-9" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_9" data-csa-c-pos="9" data-csa-c-item-id="amzn1.asin.1.B0B7R4Q5DJ" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="zubx1-ea3lkd-b5qeoe-ukbnca" data-cel-widget="MAIN-SEARCH_RESULTS-9"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;B0B7R4Q5DJ&quot;}" data-component-id="30"><div class="a-row a-badge-region"><span id="B0B7R4Q5DJ-best-seller" class="a-badge" aria-labelledby="B0B7R4Q5DJ-best-seller-label B0B7R4Q5DJ-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B0B7R4Q5DJ-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="B0B7R4Q5DJ-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Sibling Fiction</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="31"><a class="a-link-normal s-no-outline" href="/Hello-Beautiful-Novel-Ann-Napolitano-ebook/dp/B0B7R4Q5DJ/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/91l-m7D1naL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Hello Beautiful (Oprah's Book Club): A Novel" data-image-index="9" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Hello-Beautiful-Novel-Ann-Napolitano-ebook/dp/B0B7R4Q5DJ/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9"><span class="a-size-base-plus a-color-base a-text-normal">Hello Beautiful (Oprah's Book Club): A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ann-Napolitano/e/B001K8VW5S?ref=sr_ntt_srch_lnk_9&amp;qid=1682200775&amp;sr=1-9">Ann Napolitano</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.5 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B0B7R4Q5DJ&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="zfn4s-u379ju-s1kemt-8ap92g"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.5 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="6,988"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Hello-Beautiful-Novel-Ann-Napolitano-ebook/dp/B0B7R4Q5DJ/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9#customerReviews"><span class="a-size-base s-underline-text">6,988</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Hello-Beautiful-Novel-Ann-Napolitano-ebook/dp/B0B7R4Q5DJ/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Hello-Beautiful-Novel-Ann-Napolitano-ebook/dp/B0B7R4Q5DJ/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$13.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">Print List Price: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$28.00</span><span aria-hidden="true">$28.00</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-Hello-Beautiful-A-Novel/dp/B0B7VC23QG/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Hello-Beautiful-Novel-Ann-Napolitano/dp/0593243730/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Hello-Beautiful-Oprahs-Book-Club/dp/0593682939/ref=sr_1_9?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-9">Paperback</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09PMZ93DT" data-index="10" data-uuid="a8230765-08ad-4a6b-a0ca-f994b3de5687" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="32" data-cel-widget="search_result_10"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-10" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_10" data-csa-c-pos="10" data-csa-c-item-id="amzn1.asin.1.B09PMZ93DT" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="ab2vuw-80oz0w-emkc12-ed3u14" data-cel-widget="MAIN-SEARCH_RESULTS-10"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="33"><a class="a-link-normal s-no-outline" href="/No-Plan-Jack-Reacher-Novel-ebook/dp/B09PMZ93DT/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81XnZPCUpxL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="No Plan B: A Jack Reacher Novel" data-image-index="10" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/No-Plan-Jack-Reacher-Novel-ebook/dp/B09PMZ93DT/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10"><span class="a-size-base-plus a-color-base a-text-normal">No Plan B: A Jack Reacher Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B0775W2V36?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-10"><span>Book 27 of 28: Jack Reacher</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.2 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09PMZ93DT&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="slhs8v-iizv5c-u8sn81-jj1txv"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"><span class="a-icon-alt">4.2 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="44,347"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel-ebook/dp/B09PMZ93DT/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10#customerReviews"><span class="a-size-base s-underline-text">44,347</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/No-Plan-Jack-Reacher-Novel-ebook/dp/B09PMZ93DT/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/No-Plan-Jack-Reacher-Novel-ebook/dp/B09PMZ93DT/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$14.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel/dp/B09PNW5723/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel/dp/1984818546/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel/dp/1984818570/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Mass Market Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel/dp/1984818562/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/No-Plan-Jack-Reacher-Novel/dp/0593452763/ref=sr_1_10?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-10">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B092T9M6LJ" data-index="11" data-uuid="52215941-ed27-4ccb-9451-79f0a4f9b99c" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="34" data-cel-widget="search_result_11"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-11" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_11" data-csa-c-pos="11" data-csa-c-item-id="amzn1.asin.1.B092T9M6LJ" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="bg4iat-u6grv7-veunq0-2b0h5g" data-cel-widget="MAIN-SEARCH_RESULTS-11"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276797011&amp;pinnedAsins=B092T9M6LJ"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;B092T9M6LJ&quot;}" data-component-id="35"><div class="a-row a-badge-region"><span id="B092T9M6LJ-gift-guide" class="a-badge" aria-labelledby="B092T9M6LJ-gift-guide-label B092T9M6LJ-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B092T9M6LJ-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="B092T9M6LJ-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Literature &amp; Fiction</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="36"><a class="a-link-normal s-no-outline" href="/Latecomer-Jean-Hanff-Korelitz-ebook/dp/B092T9M6LJ/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/71IKL9+LAGL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Latecomer: A Novel" data-image-index="11" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Latecomer-Jean-Hanff-Korelitz-ebook/dp/B092T9M6LJ/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11"><span class="a-size-base-plus a-color-base a-text-normal">The Latecomer: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Jean-Hanff-Korelitz/e/B001HCV342?ref=sr_ntt_srch_lnk_11&amp;qid=1682200775&amp;sr=1-11">Jean Hanff Korelitz</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.4 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B092T9M6LJ&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="pwyhgt-35jzz5-qseyjz-zccy7e"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="6,343"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Latecomer-Jean-Hanff-Korelitz-ebook/dp/B092T9M6LJ/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11#customerReviews"><span class="a-size-base s-underline-text">6,343</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Latecomer-Jean-Hanff-Korelitz-ebook/dp/B092T9M6LJ/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Latecomer-Jean-Hanff-Korelitz-ebook/dp/B092T9M6LJ/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$14.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Latecomer-Jean-Hanff-Korelitz/dp/1250790794/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/The-Latecomer/dp/B094DYXRSY/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Latecomer-Novel-Jean-Hanff-Korelitz/dp/1250790786/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Latecomer-Jean-Hanff-Korelitz/dp/1250839238/ref=sr_1_11?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-11">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B084WYDYLW" data-index="12" data-uuid="34f3d701-4b24-41e6-bf5b-7db2dee6a30b" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="37" data-cel-widget="search_result_12"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-12" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_12" data-csa-c-pos="12" data-csa-c-item-id="amzn1.asin.1.B084WYDYLW" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="gc8sc8-37m1z-chv8wg-g14wd2" data-cel-widget="MAIN-SEARCH_RESULTS-12"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="38"><a class="a-link-normal s-no-outline" href="/28-Summers-Elin-Hilderbrand-ebook/dp/B084WYDYLW/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81LTmKp+PWL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="28 Summers" data-image-index="12" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/28-Summers-Elin-Hilderbrand-ebook/dp/B084WYDYLW/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12"><span class="a-size-base-plus a-color-base a-text-normal">28 Summers</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B098323B49?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-12"><span>Book 1 of 2: 28 Summers</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.6 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B084WYDYLW&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="sk9er5-lk4fh5-curit1-s6gf04"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="44,664"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers-Elin-Hilderbrand-ebook/dp/B084WYDYLW/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12#customerReviews"><span class="a-size-base s-underline-text">44,664</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/28-Summers-Elin-Hilderbrand-ebook/dp/B084WYDYLW/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/28-Summers-Elin-Hilderbrand-ebook/dp/B084WYDYLW/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$12.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers/dp/B088798Q2H/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers-Elin-Hilderbrand/dp/0316428647/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers-Elin-Hilderbrand/dp/0316305677/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Mass Market Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers-Elin-Hilderbrand/dp/0316420042/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/28-Summers-Elin-Hilderbrand/dp/1549112570/ref=sr_1_12?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-12">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    

    
    
    

    

    <div data-asin="B08ZJVVB5S" data-index="14" data-uuid="a0beb81f-3522-467d-9aee-784859b84438" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="39" data-cel-widget="search_result_13"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-14" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_13" data-csa-c-pos="13" data-csa-c-item-id="amzn1.asin.1.B08ZJVVB5S" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="ydk5m-uqpx7i-tpwzck-xqrg92" data-cel-widget="MAIN-SEARCH_RESULTS-14"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276798011&amp;pinnedAsins=B08ZJVVB5S"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;B08ZJVVB5S&quot;}" data-component-id="40"><div class="a-row a-badge-region"><span id="B08ZJVVB5S-gift-guide" class="a-badge" aria-labelledby="B08ZJVVB5S-gift-guide-label B08ZJVVB5S-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B08ZJVVB5S-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="B08ZJVVB5S-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Mystery, Thriller &amp; Suspense</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="41"><a class="a-link-normal s-no-outline" href="/Man-Who-Died-Twice-Thursday/dp/B08ZJVVB5S/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/71FcHGpPRqL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Man Who Died Twice: A Thursday Murder Club Mystery" data-image-index="13" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Man-Who-Died-Twice-Thursday/dp/B08ZJVVB5S/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13"><span class="a-size-base-plus a-color-base a-text-normal">The Man Who Died Twice: A Thursday Murder Club Mystery</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B08RDVHNTB?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-13"><span>Book 2 of 4: A Thursday Murder Club Mystery</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.6 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B08ZJVVB5S&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="2t3k3g-mesq6b-oi81z0-qko0xa"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="69,372"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Man-Who-Died-Twice-Thursday/dp/B08ZJVVB5S/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13#customerReviews"><span class="a-size-base s-underline-text">69,372</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Man-Who-Died-Twice-Thursday/dp/B08ZJVVB5S/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13">Audible Audiobook</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Man-Who-Died-Twice-Thursday/dp/B08ZJVVB5S/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$0.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">0<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary"> </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$20.90</span><span aria-hidden="true">$20.90</span></span></div> </a> </div><div class="a-row a-size-small a-color-secondary"><span class="a-color-secondary">Free with Audible trial</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Man-Who-Died-Twice-Thursday-ebook/dp/B08YRM9NBM/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Man-Who-Died-Twice-Thursday/dp/1984881019/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Man-Who-Died-Twice-Thursday/dp/1984880993/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Man-Who-Died-Twice-Thursday/dp/024199358X/ref=sr_1_13?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-13">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="0062060627" data-index="15" data-uuid="764d9727-ecff-4cf4-983a-e78987f4c4a6" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="42" data-cel-widget="search_result_14"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-15" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_14" data-csa-c-pos="14" data-csa-c-item-id="amzn1.asin.1.0062060627" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="6t7awb-z609xa-fqpjj-83n0sk" data-cel-widget="MAIN-SEARCH_RESULTS-15"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276797011&amp;pinnedAsins=0062060627"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;0062060627&quot;}" data-component-id="43"><div class="a-row a-badge-region"><span id="0062060627-gift-guide" class="a-badge" aria-labelledby="0062060627-gift-guide-label 0062060627-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="0062060627-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="0062060627-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Literature &amp; Fiction</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="44"><a class="a-link-normal s-no-outline" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060627/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Song of Achilles: A Novel" data-image-index="14" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060627/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14"><span class="a-size-base-plus a-color-base a-text-normal">The Song of Achilles: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Madeline-Miller/e/B005GG116K?ref=sr_ntt_srch_lnk_14&amp;qid=1682200775&amp;sr=1-14">Madeline Miller</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.6 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=0062060627&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="r1scvl-b4pk4t-ievcbc-ne93er"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="84,408"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060627/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14#customerReviews"><span class="a-size-base s-underline-text">84,408</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060627/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060627/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$11.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$17.99</span><span aria-hidden="true">$17.99</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$4.00</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/0062060627/ref=sr_1_14_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-14&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_14_aod?asin=0062060627&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-14&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="5mbvuj-8phiv4-3dncvn-vsd1hf"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/0062060627/ref=sr_1_14_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-14&amp;hvrand=6662995798799223789">(117 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="gwsjgd-ntmhmw-lfvjjs-nmqgro"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/The-Song-of-Achilles-audiobook/dp/B007HI3IQ6/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Song-Achilles-Novel-Madeline-Miller-ebook/dp/B006IE2IO8/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Song-Achilles-Novel-Madeline-Miller/dp/0062060619/ref=sr_1_14?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-14">Hardcover</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1496736249" data-index="16" data-uuid="3e49f3a3-1da9-4298-913a-ad9577100670" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="45" data-cel-widget="search_result_15"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-16" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_15" data-csa-c-pos="15" data-csa-c-item-id="amzn1.asin.1.1496736249" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="6biu50-ngny66-xocsc7-ncp0y5" data-cel-widget="MAIN-SEARCH_RESULTS-16"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276797011&amp;pinnedAsins=1496736249"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;1496736249&quot;}" data-component-id="46"><div class="a-row a-badge-region"><span id="1496736249-gift-guide" class="a-badge" aria-labelledby="1496736249-gift-guide-label 1496736249-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1496736249-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="1496736249-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Literature &amp; Fiction</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="47"><a class="a-link-normal s-no-outline" href="/Spanish-Daughter-Lorena-Hughes/dp/1496736249/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81RLK4Dtp5L._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Spanish Daughter: A Gripping Historical Novel Perfect for Book Clubs" data-image-index="15" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Spanish-Daughter-Lorena-Hughes/dp/1496736249/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15"><span class="a-size-base-plus a-color-base a-text-normal">The Spanish Daughter: A Gripping Historical Novel Perfect for Book Clubs</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Lorena-Hughes/e/B071NSS7Z5?ref=sr_ntt_srch_lnk_15&amp;qid=1682200775&amp;sr=1-15">Lorena Hughes</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.1 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1496736249&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="yg1n3s-i9vu3y-k62qz9-3jj763"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"><span class="a-icon-alt">4.1 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="4,964"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Spanish-Daughter-Lorena-Hughes/dp/1496736249/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15#customerReviews"><span class="a-size-base s-underline-text">4,964</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Spanish-Daughter-Lorena-Hughes/dp/1496736249/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Spanish-Daughter-Lorena-Hughes/dp/1496736249/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$10.50</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">10<span class="a-price-decimal">.</span></span><span class="a-price-fraction">50</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$15.95</span><span aria-hidden="true">$15.95</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$3.89</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1496736249/ref=sr_1_15_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-15&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_15_aod?asin=1496736249&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-15&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="cx9fpx-m07r2x-yhm918-w0zcsg"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1496736249/ref=sr_1_15_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-15&amp;hvrand=6662995798799223789">(106 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="n1giii-4om6hs-67qvys-tu0gd7"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-base"><span>Ages: 5 years and up</span><br><br></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Spanish-Daughter-Lorena-Hughes-ebook/dp/B091MQ9XHN/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-The-Spanish-Daughter/dp/B09M96XPHM/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Spanish-Daughter-Lorena-Hughes/dp/163808338X/ref=sr_1_15?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-15">Library Binding</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B09CNDSKZJ" data-index="17" data-uuid="b6247a2e-e36e-4215-9b38-ae965fd4d140" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="48" data-cel-widget="search_result_16"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-17" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_16" data-csa-c-pos="16" data-csa-c-item-id="amzn1.asin.1.B09CNDSKZJ" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="x2kcl2-cka3vg-lhddch-ic8oxw" data-cel-widget="MAIN-SEARCH_RESULTS-17"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276798011&amp;pinnedAsins=B09CNDSKZJ"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;B09CNDSKZJ&quot;}" data-component-id="49"><div class="a-row a-badge-region"><span id="B09CNDSKZJ-gift-guide" class="a-badge" aria-labelledby="B09CNDSKZJ-gift-guide-label B09CNDSKZJ-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="B09CNDSKZJ-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="B09CNDSKZJ-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Mystery, Thriller &amp; Suspense</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="50"><a class="a-link-normal s-no-outline" href="/Treasure-State-Cassie-Dewell-Novels-ebook/dp/B09CNDSKZJ/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81g+7cxUexL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Treasure State: A Cassie Dewell Novel (Cassie Dewell Novels Book 6)" data-image-index="16" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Treasure-State-Cassie-Dewell-Novels-ebook/dp/B09CNDSKZJ/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16"><span class="a-size-base-plus a-color-base a-text-normal">Treasure State: A Cassie Dewell Novel (Cassie Dewell Novels Book 6)</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B084H87WPC?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-16"><span>Book 6 of 6: Cassie Dewell</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.5 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09CNDSKZJ&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="kiiv13-vuuusg-akcs79-744bir"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.5 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="6,004"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Treasure-State-Cassie-Dewell-Novels-ebook/dp/B09CNDSKZJ/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16#customerReviews"><span class="a-size-base s-underline-text">6,004</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Treasure-State-Cassie-Dewell-Novels-ebook/dp/B09CNDSKZJ/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Treasure-State-Cassie-Dewell-Novels-ebook/dp/B09CNDSKZJ/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$14.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-Treasure-State/dp/B09L5BCKR5/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Treasure-State-Cassie-Dewell-Novels/dp/1250766966/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Treasure-State-Cassie-Dewell-Novels/dp/1250889553/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Treasure-State-Cassie-Dewell-Novels/dp/1250896428/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Mass Market Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Treasure-State-C-J-Box/dp/125085220X/ref=sr_1_16?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-16">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1496726537" data-index="18" data-uuid="8d223bbe-4e63-4038-8f1c-f7987f44cbf6" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="51" data-cel-widget="search_result_17"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-18" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_17" data-csa-c-pos="17" data-csa-c-item-id="amzn1.asin.1.1496726537" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="l5rjwm-xg5jan-7sczao-kv5en5" data-cel-widget="MAIN-SEARCH_RESULTS-18"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="52"><a class="a-link-normal s-no-outline" href="/Nurses-Secret-Amanda-Skenandore/dp/1496726537/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81pA0ppfmUL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Nurse's Secret: A Thrilling Historical Novel of the Dark Side of Gilded Age New York City" data-image-index="17" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Nurses-Secret-Amanda-Skenandore/dp/1496726537/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17"><span class="a-size-base-plus a-color-base a-text-normal">The Nurse's Secret: A Thrilling Historical Novel of the Dark Side of Gilded Age New York City</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Amanda-Skenandore/e/B07CK4V2Q5?ref=sr_ntt_srch_lnk_17&amp;qid=1682200775&amp;sr=1-17">Amanda Skenandore</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1496726537&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="l27fv7-uu26bg-kzbhlq-4tsvx0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="8,735"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Nurses-Secret-Amanda-Skenandore/dp/1496726537/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17#customerReviews"><span class="a-size-base s-underline-text">8,735</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Nurses-Secret-Amanda-Skenandore/dp/1496726537/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Nurses-Secret-Amanda-Skenandore/dp/1496726537/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$16.95</span><span aria-hidden="true">$16.95</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$4.45</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1496726537/ref=sr_1_17_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-17&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_17_aod?asin=1496726537&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-17&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="435k88-dmk9ct-ug5up1-455d99"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1496726537/ref=sr_1_17_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-17&amp;hvrand=6662995798799223789">(91 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="mp0p5y-549eos-qxlbgm-awsq0a"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Nurses-Secret-Amanda-Skenandore-ebook/dp/B09HRCJYDL/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Audible-The-Nurses-Secret/dp/B09YL7LRTQ/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Nurses-Secret-Amanda-Skenandore/dp/B0BR6JBDSS/ref=sr_1_17?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-17">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1501171356" data-index="19" data-uuid="a137f76e-5691-44cc-99b3-94151d34f74a" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="53" data-cel-widget="search_result_18"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-19" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_18" data-csa-c-pos="18" data-csa-c-item-id="amzn1.asin.1.1501171356" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="8y0gs0-lyu1qh-14h39y-j64v2c" data-cel-widget="MAIN-SEARCH_RESULTS-19"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;1501171356&quot;}" data-component-id="54"><div class="a-row a-badge-region"><span id="1501171356-best-seller" class="a-badge" aria-labelledby="1501171356-best-seller-label 1501171356-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1501171356-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="1501171356-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Women's Domestic Life Fiction</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="55"><a class="a-link-normal s-no-outline" href="/Last-Thing-He-Told-Me/dp/1501171356/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/71LyuJP7yUL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Last Thing He Told Me: A Novel" data-image-index="18" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Last-Thing-He-Told-Me/dp/1501171356/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18"><span class="a-size-base-plus a-color-base a-text-normal">The Last Thing He Told Me: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Laura-Dave/e/B001ILME68?ref=sr_ntt_srch_lnk_18&amp;qid=1682200775&amp;sr=1-18">Laura Dave</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1501171356&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="6oi5ku-bw0qi3-squ0d2-ktnz05"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="129,328"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Last-Thing-He-Told-Me/dp/1501171356/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18#customerReviews"><span class="a-size-base s-underline-text">129,328</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Last-Thing-He-Told-Me/dp/1501171356/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Last-Thing-He-Told-Me/dp/1501171356/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$12.47</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">47</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$17.99</span><span aria-hidden="true">$17.99</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Last-Thing-He-Told-Me/dp/B08N393GT5/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Last-Thing-He-Told-Me-ebook/dp/B08LDY1MKW/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Last-Thing-He-Told-Me/dp/1501171348/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Last-Thing-He-Told-Me/dp/1797124749/ref=sr_1_18?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-18">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B0B841CBYC" data-index="20" data-uuid="752551f9-4ac3-4818-b835-869583be5508" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="56" data-cel-widget="search_result_19"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-20" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_19" data-csa-c-pos="19" data-csa-c-item-id="amzn1.asin.1.B0B841CBYC" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="8vj7ce-x3f1d2-m6bf75-xof3wd" data-cel-widget="MAIN-SEARCH_RESULTS-20"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="57"><a class="a-link-normal s-no-outline" href="/Dedication-Murder-Beyond-Bookstore-Mystery-ebook/dp/B0B841CBYC/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81n0R+eUZiL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Dedication to Murder (A Beyond the Page Bookstore Mystery Book 9)" data-image-index="19" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Dedication-Murder-Beyond-Bookstore-Mystery-ebook/dp/B0B841CBYC/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19"><span class="a-size-base-plus a-color-base a-text-normal">Dedication to Murder (A Beyond the Page </span> <span class="a-size-base-plus a-color-base a-text-bold a-text-normal">Bookstore</span> <span class="a-size-base-plus a-color-base a-text-normal"> Mystery Book 9)</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B07Z4LD5WR?binding=kindle_edition&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tkin&amp;qid=1682200775&amp;sr=1-19"><span>Book 9 of 9: A Beyond the Page Bookstore Mystery</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Dedication-Murder-Beyond-Bookstore-Mystery-ebook/dp/B0B841CBYC/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Dedication-Murder-Beyond-Bookstore-Mystery-ebook/dp/B0B841CBYC/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$6.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">6<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">Digital List Price: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$8.54</span><span aria-hidden="true">$8.54</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary"><span aria-label="This title will be released on April 25, 2023."><span class="a-color-secondary">This title will be released on April 25, 2023.</span></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Dedication-Murder-Beyond-Bookstore-Mystery/dp/1496735145/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19">Mass Market Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Dedication-Murder-Beyond-Bookstore-Mystery/dp/B0C1LKMKTB/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Dedication-Murder-Beyond-Bookstore-Mystery/dp/B0BYFNFH5C/ref=sr_1_19?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-19">Paperback</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1538752840" data-index="21" data-uuid="f3352b22-23da-4144-9f73-cc8d87db939f" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="58" data-cel-widget="search_result_20"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-21" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_20" data-csa-c-pos="20" data-csa-c-item-id="amzn1.asin.1.1538752840" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="gmh0px-xhhoy3-gn3n5d-o7xxrd" data-cel-widget="MAIN-SEARCH_RESULTS-21"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276798011&amp;pinnedAsins=1538752840"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;1538752840&quot;}" data-component-id="59"><div class="a-row a-badge-region"><span id="1538752840-gift-guide" class="a-badge" aria-labelledby="1538752840-gift-guide-label 1538752840-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1538752840-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="1538752840-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Mystery, Thriller &amp; Suspense</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="60"><a class="a-link-normal s-no-outline" href="/Summer-House-James-Patterson/dp/1538752840/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/615YoZtasFL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Summer House" data-image-index="20" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Summer-House-James-Patterson/dp/1538752840/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20"><span class="a-size-base-plus a-color-base a-text-normal">The Summer House</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/James-Patterson/e/B000APZGGS?ref=sr_ntt_srch_lnk_20&amp;qid=1682200775&amp;sr=1-20">James Patterson</a> <span class="a-size-base"> and </span><span class="a-size-base">Brendan DuBois</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.5 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1538752840&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="5vwpyr-hwfhdw-x4bkqj-nnsd6s"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.5 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="19,025"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Summer-House-James-Patterson/dp/1538752840/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20#customerReviews"><span class="a-size-base s-underline-text">19,025</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Summer-House-James-Patterson/dp/1538752840/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Mass Market Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Summer-House-James-Patterson/dp/1538752840/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$1.49</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1538752840/ref=sr_1_20_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-20&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_20_aod?asin=1538752840&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-20&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="ue2iqo-dy5yxg-8uipa8-de7m7v"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1538752840/ref=sr_1_20_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-20&amp;hvrand=6662995798799223789">(122 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="8pd8pv-axfkdq-vqhdnw-l6glal"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Summer-House-James-Patterson-ebook/dp/B07YSNFBBS/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/The-Summer-House/dp/B0876BRFGX/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Summer-House-James-Patterson/dp/0316539554/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Summer-House-James-Patterson/dp/1538752832/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Summer-House-James-Patterson/dp/1549184458/ref=sr_1_20?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-20">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B08TVFZ44W" data-index="22" data-uuid="d23a3435-81c1-47ae-ac50-1ccc1d7892c3" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="61" data-cel-widget="search_result_21"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-22" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_21" data-csa-c-pos="21" data-csa-c-item-id="amzn1.asin.1.B08TVFZ44W" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="l6tj25-12tntc-8i2rfh-5vigoh" data-cel-widget="MAIN-SEARCH_RESULTS-22"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="62"><a class="a-link-normal s-no-outline" href="/Sooley-Novel-John-Grisham-ebook/dp/B08TVFZ44W/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/711CrspK-kL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Sooley: A Novel" data-image-index="21" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Sooley-Novel-John-Grisham-ebook/dp/B08TVFZ44W/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21"><span class="a-size-base-plus a-color-base a-text-normal">Sooley: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/John-Grisham/e/B000AQ40M8?ref=sr_ntt_srch_lnk_21&amp;qid=1682200775&amp;sr=1-21">John Grisham</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.5 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B08TVFZ44W&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="1ox47j-liyhov-bg8y4l-ulss2c"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.5 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="42,463"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Sooley-Novel-John-Grisham-ebook/dp/B08TVFZ44W/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21#customerReviews"><span class="a-size-base s-underline-text">42,463</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Sooley-Novel-John-Grisham-ebook/dp/B08TVFZ44W/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Sooley-Novel-John-Grisham-ebook/dp/B08TVFZ44W/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Sooley-A-Novel/dp/B08TX4D8R5/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Sooley-Novel-John-Grisham/dp/0593359534/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Sooley-Novel-John-Grisham/dp/0385547684/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Sooley-Novel-John-Grisham/dp/0593459288/ref=sr_1_21?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-21">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1501110365" data-index="23" data-uuid="fb7cf3df-ebd8-4b61-9e89-1c64f85f6204" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="63" data-cel-widget="search_result_22"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-23" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_22" data-csa-c-pos="22" data-csa-c-item-id="amzn1.asin.1.1501110365" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="92ns15-365uh0-mki4ui-25wfgk" data-cel-widget="MAIN-SEARCH_RESULTS-23"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;best-seller&quot;,&quot;asin&quot;:&quot;1501110365&quot;}" data-component-id="64"><div class="a-row a-badge-region"><span id="1501110365-best-seller" class="a-badge" aria-labelledby="1501110365-best-seller-label 1501110365-best-seller-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1501110365-best-seller-label" class="a-badge-label" data-a-badge-color="sx-orange" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Best Seller</span></span></span><span id="1501110365-best-seller-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">in Contemporary Women Fiction</span></span></div></span></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="65"><a class="a-link-normal s-no-outline" href="/Ends-Us-Novel-Colleen-Hoover/dp/1501110365/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81s0B6NYXML._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="It Ends with Us: A Novel (1)" data-image-index="22" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Ends-Us-Novel-Colleen-Hoover/dp/1501110365/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22"><span class="a-size-base-plus a-color-base a-text-normal">It Ends with Us: A Novel (1)</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/dp/B09SHQ4JRH?binding=paperback&amp;searchxofy=true&amp;ref_=dbs_s_bs_series_rwt_tpbk&amp;qid=1682200775&amp;sr=1-22"><span>Book 1 of 2: It Ends with Us</span> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.7 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1501110365&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="j2nd3d-a6700z-ce867a-9095jk"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.7 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="265,617"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ends-Us-Novel-Colleen-Hoover/dp/1501110365/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22#customerReviews"><span class="a-size-base s-underline-text">265,617</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Ends-Us-Novel-Colleen-Hoover/dp/1501110365/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Ends-Us-Novel-Colleen-Hoover/dp/1501110365/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$9.95</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">95</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$16.99</span><span aria-hidden="true">$16.99</span></span></div> </a> </div><div class="a-row a-size-small a-color-secondary"><span data-component-type="s-coupon-component" class="rush-component" data-component-props="{&quot;asin&quot;:&quot;1501110365&quot;}" data-component-id="66"><span class="s-coupon-clipped aok-hidden"><span class="a-color-base">$0.21 coupon applied at checkout</span></span><span class="s-coupon-unclipped"><span class="a-size-base s-highlighted-text-padding aok-inline-block s-coupon-highlight-color">Save $0.21</span> <span class="a-color-base"> with coupon</span></span></span> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$2.49</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1501110365/ref=sr_1_22_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-22&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_22_aod?asin=1501110365&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-22&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="qrcd7c-5l6qwa-ackf31-aexyag"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1501110365/ref=sr_1_22_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-22&amp;hvrand=6662995798799223789">(225 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="ooazpt-ejg87n-f7ssz8-q4dtmu"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/It-Ends-with-Us-Colleen-Hoover-audiobook/dp/B01GGU0XWC/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ends-Us-Novel-Colleen-Hoover-ebook/dp/B0176M3U10/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ends-Us-Special-Collectors-Novel/dp/1668021048/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ends-Us-Colleen-Hoover/dp/1797107453/ref=sr_1_22?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-22">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="B08WCFQVR8" data-index="24" data-uuid="4d154510-b082-4a05-820b-bde8250d6373" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="67" data-cel-widget="search_result_23"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-24" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_23" data-csa-c-pos="23" data-csa-c-item-id="amzn1.asin.1.B08WCFQVR8" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="np4rnt-sa9bpu-fn81sh-dcgdnq" data-cel-widget="MAIN-SEARCH_RESULTS-24"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 28px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="68"><a class="a-link-normal s-no-outline" href="/Never-Novel-Ken-Follett-ebook/dp/B08WCFQVR8/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/91OlkNx-VpL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="Never: A Novel" data-image-index="23" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Never-Novel-Ken-Follett-ebook/dp/B08WCFQVR8/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23"><span class="a-size-base-plus a-color-base a-text-normal">Never: A Novel</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Ken-Follett/e/B000APHCPQ?ref=sr_ntt_srch_lnk_23&amp;qid=1682200775&amp;sr=1-23">Ken Follett</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B08WCFQVR8&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="uwnok0-5ue56f-5yzbj4-cqw9y2"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="39,769"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Never-Novel-Ken-Follett-ebook/dp/B08WCFQVR8/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23#customerReviews"><span class="a-size-base s-underline-text">39,769</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Never-Novel-Ken-Follett-ebook/dp/B08WCFQVR8/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23">Kindle</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Never-Novel-Ken-Follett-ebook/dp/B08WCFQVR8/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$10.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">10<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">Print List Price: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$20.00</span><span aria-hidden="true">$20.00</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-color-base">Available instantly</span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Never-Novel-Ken-Follett/dp/0593300033/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23">Paperback</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Never-A-Novel/dp/B08WCMBZR6/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Never-Novel-Ken-Follett/dp/0593300017/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23">Hardcover</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Never-Novel-Ken-Follett/dp/0593458818/ref=sr_1_23?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-23">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="1542034299" data-index="25" data-uuid="fd0feda1-8f29-4155-9808-4d3c9244369c" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" data-component-id="69" data-cel-widget="search_result_24"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-25" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_24" data-csa-c-pos="24" data-csa-c-item-id="amzn1.asin.1.1542034299" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="mbcevj-sw9dda-405g1a-foliki" data-cel-widget="MAIN-SEARCH_RESULTS-25"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="a-section a-spacing-none puis-status-badge-container aok-relative s-grid-status-badge-container puis-expand-height"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/kindle-dbs/books-category/browse-redirect/?ref=ess_dp_epicks&amp;node=17276798011&amp;pinnedAsins=1542034299"><span data-component-type="s-status-badge-component" class="rush-component" data-component-props="{&quot;badgeType&quot;:&quot;gift-guide&quot;,&quot;asin&quot;:&quot;1542034299&quot;}" data-component-id="70"><div class="a-row a-badge-region"><span id="1542034299-gift-guide" class="a-badge" aria-labelledby="1542034299-gift-guide-label 1542034299-gift-guide-supplementary" data-a-badge-supplementary-position="right" tabindex="0" data-a-badge-type="status"><span id="1542034299-gift-guide-label" class="a-badge-label" data-a-badge-color="sx-secondary" aria-hidden="true"><span class="a-badge-label-inner a-text-ellipsis"><span class="a-badge-text" data-a-badge-color="sx-cloud">Editors' pick</span></span></span><span id="1542034299-gift-guide-supplementary" class="a-badge-supplementary-text a-text-ellipsis" aria-hidden="true">Best Mystery, Thriller &amp; Suspense</span></span></div></span> </a> </div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized" style="padding-top: 0px !important;"><span data-component-type="s-product-image" class="rush-component" data-component-id="71"><a class="a-link-normal s-no-outline" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1542034299/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81fHGvdh-XL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="The Quarry Girls: A Thriller" data-image-index="24" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1542034299/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24"><span class="a-size-base-plus a-color-base a-text-normal">The Quarry Girls: A Thriller</span> </a> </h2><div class="a-row a-size-base a-color-secondary"><span class="a-size-base">by </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Jess-Lourey/e/B001IODOR8?ref=sr_ntt_srch_lnk_24&amp;qid=1682200775&amp;sr=1-24">Jess Lourey</a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=1542034299&amp;ref=acr_search__popover&amp;contextId=search&quot;}" data-csa-c-id="evyyvv-69juvx-y688fl-47z8l8"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="38,269"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1542034299/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24#customerReviews"><span class="a-size-base s-underline-text">38,269</span> </a> </span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1542034299/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24">Paperback</a> </div><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1542034299/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$11.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$15.95</span><span aria-hidden="true">$15.95</span></span></div> </a> </div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span class="a-size-small a-color-base">Ships to Argentina</span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br><span class="a-color-base">$7.96</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/1542034299/ref=sr_1_24_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-24&amp;hvrand=6662995798799223789&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_24_aod?asin=1542034299&amp;pc=sp&amp;hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-24&amp;hvrand=6662995798799223789&amp;rrid=BNJYY9EBY54VZZF6X4X6&quot;}" data-csa-c-id="r9m14e-s1klcg-hudw1f-e4td5e"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/1542034299/ref=sr_1_24_olp?hvlocphy=1000060&amp;hvnetw=g&amp;rnid=6461714011&amp;keywords=bookstore+amazon&amp;hvadid=623182854892&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;hvlocint=9061323&amp;s=books&amp;hydadcr=20698_13296112&amp;hvdev=c&amp;hvqmt=b&amp;hvtargid=kwd-13263126&amp;sr=1-24&amp;hvrand=6662995798799223789">(74 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display" data-csa-c-id="wb55hr-qkavxw-of9xif-utcmcw"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-small"><div class="a-row a-size-small a-color-base"><span class="a-size-base a-color-secondary">Other formats: </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/The-Quarry-Girls-A-Thriller/dp/B09QF3RCS8/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24">Audible Audiobook</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Quarry-Girls-Thriller-Jess-Lourey-ebook/dp/B09G6DMDVR/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24">Kindle</a> <span class="a-size-base a-color-secondary">, </span><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Quarry-Girls-Thriller-Jess-Lourey/dp/1713656124/ref=sr_1_24?hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;keywords=bookstore+amazon&amp;qid=1682200775&amp;refinements=p_n_condition-type%3A6461716011&amp;rnid=6461714011&amp;s=books&amp;sr=1-24">Audio CD</a> </div></div></div></div></div></div></div></div>

    
    
    

    

    <div data-asin="" data-index="26" class="a-section a-spacing-none s-result-item s-flex-full-width s-widget s-widget-spacing-large" data-cel-widget="search_result_25"><div data-uuid="2e473b0c-abcb-48cb-bb62-f7a86bee2e74" cel_widget_id="MAIN-PAGINATION-26" class="s-widget-container s-spacing-medium s-widget-container-height-medium celwidget slot=MAIN template=PAGINATION widgetId=pagination-button" data-csa-c-id="q23l0p-xh00mz-kcril5-u7ldmt" data-cel-widget="MAIN-PAGINATION-26"><div class="a-section a-text-center s-pagination-container" role="navigation"><span class="s-pagination-strip"><span class="s-pagination-item s-pagination-previous s-pagination-disabled " aria-disabled="true"><svg xmlns="http://www.w3.org/2000/svg" width="8" height="12" viewBox="0 0 8 12" focusable="false" aria-hidden="true"><path d="M5.874.35a1.28 1.28 0 011.761 0 1.165 1.165 0 010 1.695L3.522 6l4.113 3.955a1.165 1.165 0 010 1.694 1.28 1.28 0 01-1.76 0L0 6 5.874.35z"></path></svg>Previous</span><script>P.declare('s\-optimized\-pagination\-config', {"prefetchTargetIndex":0,"enabled":true});</script><span class="s-pagination-item s-pagination-selected" aria-label="Current page, page 1">1</span><a href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;dc&amp;page=2&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;ref=sr_pg_2" aria-label="Go to page 2" class="s-pagination-item s-pagination-button">2</a><a href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;dc&amp;page=3&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;ref=sr_pg_3" aria-label="Go to page 3" class="s-pagination-item s-pagination-button">3</a><span class="s-pagination-item s-pagination-ellipsis" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="2" viewBox="0 0 10 2" focusable="false" aria-hidden="true"><path d="M9 2c-.608 0-1-.425-1-1s.392-1 1-1 1 .448 1 1c0 .575-.392 1-1 1zM5 2c-.608 0-1-.425-1-1s.392-1 1-1 1 .448 1 1c0 .575-.392 1-1 1zM1 2c-.608 0-1-.425-1-1s.392-1 1-1 1 .448 1 1c0 .575-.392 1-1 1z"></path>...</svg></span><span class="s-pagination-item s-pagination-disabled" aria-disabled="true">50</span><a href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&amp;dc&amp;page=2&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;ref=sr_pg_1" aria-label="Go to next page, page 2" class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator">Next<svg xmlns="http://www.w3.org/2000/svg" width="8" height="12" viewBox="0 0 8 12" focusable="false" aria-hidden="true"><path d="M2.126.35a1.28 1.28 0 00-1.761 0 1.165 1.165 0 000 1.695L4.478 6 .365 9.955a1.165 1.165 0 000 1.694 1.28 1.28 0 001.76 0L8 6 2.126.35z"></path></svg></a></span></div></div></div>

    
    
    

    

    <div data-asin="" data-index="27" class="a-section a-spacing-none s-result-item s-flex-full-width s-widget s-widget-spacing-large" data-cel-widget="search_result_26"><div data-uuid="9fbcebea-4306-4d4e-ac71-ab4d9c590c9a" cel_widget_id="MAIN-FEEDBACK-27" class="s-widget-container s-spacing-medium s-widget-container-height-medium celwidget slot=MAIN template=FEEDBACK widgetId=feedback" data-csa-c-id="z6i98q-52q70h-x5tsfr-vluqef" data-cel-widget="MAIN-FEEDBACK-27">







    
    








<div class="a-section a-spacing-medium a-spacing-top-medium">
    <div class="sg-row">
        <div class="sg-col-10-of-12 sg-col-10-of-20 sg-col sg-col-10-of-16 sg-col-10-of-24"><div class="sg-col-inner">
            
                <div class="a-section a-spacing-small"><div class="a-section a-spacing-none a-text-bold"><span class="a-size-medium-plus a-color-base">Need help?</span></div></div>
            
            <div class="a-row a-spacing-base a-size-base"><a class="a-size-base a-color-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/gp/help/customer/display.html?nodeId=468556">Visit the help section</a> <span class="a-size-base a-color-base"> or </span><a class="a-size-base a-color-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/gp/help/customer/contact-us">contact us</a> </div>
        </div></div>
    </div>
</div>

</div></div>

    
    
    

    

    <div data-asin="" data-index="28" class="a-section a-spacing-none s-result-item s-flex-full-width s-widget s-widget-spacing-large" data-cel-widget="search_result_27"><div data-uuid="611e9499-813e-4346-8221-69b9e5e9ec02" class="s-widget-container s-spacing-medium s-widget-container-height-medium"><div class="celwidget pd_rd_w-7Rx0z content-id-amzn1.sym.f379a86b-4bda-4701-bdc8-544e8d535b33:amzn1.sym.f379a86b-4bda-4701-bdc8-544e8d535b33 pf_rd_p-f379a86b-4bda-4701-bdc8-544e8d535b33 pf_rd_r-BNJYY9EBY54VZZF6X4X6 pd_rd_wg-J4fMS pd_rd_r-81b9c7d1-4f8c-4407-8d05-14c5157fc135 c-f" cel_widget_id="ape-safeframe-card_loom-desktop-footer-slot_63" data-csa-op-log-render="" data-csa-c-content-id="amzn1.sym.f379a86b-4bda-4701-bdc8-544e8d535b33:amzn1.sym.f379a86b-4bda-4701-bdc8-544e8d535b33" data-csa-c-slot-id="DsUnknown-64" data-csa-c-type="widget" data-csa-c-painter="ape-safeframe-card-cards" data-csa-c-id="f22yzl-wbp4t7-y7fp84-n8ngs9" data-cel-widget="ape-safeframe-card_loom-desktop-footer-slot_63"><script>if(window.mix_csa){window.mix_csa('[cel_widget_id="ape-safeframe-card_loom-desktop-footer-slot_63"]', '#CardInstanceMAcD7Va_iyzHfagyHj7-dQ')('mark', 'bb')}</script>
<script>if(window.uet){window.uet('bb','ape-safeframe-card_loom-desktop-footer-slot_63',{wb: 1})}</script>
<!--CardsClient--><div class="root" id="CardInstanceMAcD7Va_iyzHfagyHj7-dQ" data-card-metrics-id="ape-safeframe-card_loom-desktop-footer-slot_63" data-mix-claimed="true"><script type="text/javascript">var importScript = importScript || function (src, errorMessage, forceInternalCall) {var script = document.createElement("script"); script.type = "text/javascript"; script.async = true; script.charset = "utf-8"; script.src = src; script.onerror = function() {logError(errorMessage); }; if (!forceInternalCall || forceInternalCall === 'false') {script.setAttribute("crossorigin", "anonymous"); } (document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(script); };</script><script type="text/javascript">window.sfLogErrors = window.sfLogErrors || false;</script><script type="text/javascript">var logError = logError || function (msg, ex) { ex = ex || new Error(msg); if (window.ue && typeof ue.count == 'function') { ue.count('adplacements:safeFrameError', 1); } if (!window.sfLogErrors) return; if (window.ueLogError) { window.ueLogError(ex, { logLevel: 'ERROR', attribution: 'APE-safeframe', message: msg + ' ' }); } else if (typeof console !== 'undefined' && console.error) { console.error(msg, ex); } }; </script><script type="text/javascript">var instrumentation;!function(){"use strict";var e={568:function(e,t,n){var r=this&&this.__createBinding||(Object.create?function(e,t,n,r){void 0===r&&(r=n);var i=Object.getOwnPropertyDescriptor(t,n);i&&!("get"in i?!t.__esModule:i.writable||i.configurable)||(i={enumerable:!0,get:function(){return t[n]}}),Object.defineProperty(e,r,i)}:function(e,t,n,r){void 0===r&&(r=n),e[r]=t[n]}),i=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),o=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n in e)"default"!==n&&Object.prototype.hasOwnProperty.call(e,n)&&r(t,e,n);return i(t,e),t};Object.defineProperty(t,"__esModule",{value:!0}),t.AD_LOAD_COUNTERS=t.csa=t.csm=void 0;var a=o(n(472));t.csm=a;var c=o(n(481));t.csa=c;var u=n(922);Object.defineProperty(t,"AD_LOAD_COUNTERS",{enumerable:!0,get:function(){return u.AD_LOAD_COUNTERS}})},922:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.AD_LOAD_COUNTERS=void 0,t.AD_LOAD_COUNTERS={HTML_REACHED:"adload:htmlreached"}},481:function(e,t,n){var r=this&&this.__createBinding||(Object.create?function(e,t,n,r){void 0===r&&(r=n);var i=Object.getOwnPropertyDescriptor(t,n);i&&!("get"in i?!t.__esModule:i.writable||i.configurable)||(i={enumerable:!0,get:function(){return t[n]}}),Object.defineProperty(e,r,i)}:function(e,t,n,r){void 0===r&&(r=n),e[r]=t[n]}),i=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),o=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n in e)"default"!==n&&Object.prototype.hasOwnProperty.call(e,n)&&r(t,e,n);return i(t,e),t};Object.defineProperty(t,"__esModule",{value:!0}),t.addCsaEntity=t.logCsaEvent=t.initCsaEvents=t.markCsaLatencyMetric=t.initCsaLatencyPlugin=t.csa=void 0;var a=o(n(876));t.csa=new function(){this.latencyPlugin=void 0,this.events=void 0},t.initCsaLatencyPlugin=function(e){window.csa?t.csa.latencyPlugin=window.csa("Content",{element:e}):console.log(window)},t.markCsaLatencyMetric=function(e,n){try{t.csa.latencyPlugin("mark",e,n)}catch(e){a.logError("Error with initiating CSA",e)}},t.initCsaEvents=function(){window.csa&&(t.csa.events=window.csa("Events",{producerId:"adplacements"}))},t.logCsaEvent=function(e,n,r){try{t.csa.events("log",{schemaId:"ApeSafeframe.csaEvent.1",metricName:e+":"+n+":"+r,metricValue:1},{ent:"all"})}catch(e){a.logError("Error with initiating CSA",e)}},t.addCsaEntity=function(e){try{t.csa.events("setEntity",{adCreativeMetaData:e})}catch(e){a.logError("Error with initiating CSA",e)}}},472:function(e,t){function n(e,t,n,r){var i=[e,t,n];return r&&i.push(r),i}Object.defineProperty(t,"__esModule",{value:!0}),t.addCsmTag=t.sendCsmCounter=t.sendCsmLatencyMetric=void 0,t.sendCsmLatencyMetric=function(e,t,r,i,o){var a;if(function(e){e.bb="uet",e.af="uet",e.cf="uet",e.be="uet",e.ld="uex"}(a||(a={})),a.hasOwnProperty(e)){var c=a[e].toString(),u=i?i+":":"";"function"==typeof window[c]&&(window[c].apply(this,n(e,"adplacements:"+u+t.replace(/_/g,":"),{wb:1},o)),r&&window[c].apply(this,n(e,"adplacements:"+u+r,{wb:1},o)))}},t.sendCsmCounter=function(e,t,n,r){if(window.ue&&"function"==typeof window.ue.count){var i="adplacements:"+n;if(e&&(i+=":"+e.replace(/_/g,":")),window.ue.count(i,r),t){var o="adplacements:"+(n&&t?n+":":n)+t;window.ue.count(o,r)}}},t.addCsmTag=function(e,t,n,r){if(window.ue&&window.ue.tag){if(t){var i=e+":"+t.replace(/_/g,":")+(r?":"+r:"");window.ue.tag(i)}if(n){var o=e+":"+n+(r?":"+r:"");window.ue.tag(o)}t||n||window.ue.tag(e+(r?":"+r:""))}}},876:function(e,t,n){var r=this&&this.__createBinding||(Object.create?function(e,t,n,r){void 0===r&&(r=n);var i=Object.getOwnPropertyDescriptor(t,n);i&&!("get"in i?!t.__esModule:i.writable||i.configurable)||(i={enumerable:!0,get:function(){return t[n]}}),Object.defineProperty(e,r,i)}:function(e,t,n,r){void 0===r&&(r=n),e[r]=t[n]}),i=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),o=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n in e)"default"!==n&&Object.prototype.hasOwnProperty.call(e,n)&&r(t,e,n);return i(t,e),t};Object.defineProperty(t,"__esModule",{value:!0}),t.logError=void 0;var a=o(n(472));t.logError=function(e,t){var n=t||new Error(e);console.error(e,t),a.sendCsmCounter("",null,"safeFrameError",1),window.sfHostLogErrors&&(window.ueHostLogError?window.ueHostLogError(n,{logLevel:"ERROR",attribution:"APE-safeframe",message:e+" "}):"undefined"!=typeof console&&console.error&&console.error(e,n))}}},t={},n=function n(r){var i=t[r];if(void 0!==i)return i.exports;var o=t[r]={exports:{}};return e[r].call(o.exports,o,o.exports,n),o.exports}(568);instrumentation=n}();</script><script type="text/javascript">if (instrumentation) {instrumentation.csa.initCsaEvents(); instrumentation.csm.sendCsmCounter('Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom', '763d0af2-6ac3-4627-a3f3-fa9484d521a7', instrumentation.AD_LOAD_COUNTERS.HTML_REACHED, 1); instrumentation.csa.logCsaEvent(instrumentation.AD_LOAD_COUNTERS.HTML_REACHED, 'Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom', '763d0af2-6ac3-4627-a3f3-fa9484d521a7'); } if (typeof uet === 'function') {if (typeof ues === 'function') {var scope = 'Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom'; var placementId = '763d0af2-6ac3-4627-a3f3-fa9484d521a7'; ues('wb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); uet('bb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); if (placementId) {ues('wb', 'adplacements:' + placementId, {wb:1}); uet('bb', 'adplacements:' + placementId, {wb:1}); } } } function addListener(event, listener) {if (window.addEventListener) {window.addEventListener(event, listener, false); } else if (window.attachEvent) {window.attachEvent('on' + event, listener); } } function removeListener(event, listener) {if (window.removeEventListener) {window.removeEventListener(event, listener, false); } else if (window.detachEvent) {window.detachEvent('on' + event, listener); } } function windowHeight() {return window.innerHeight || document.documentElement.clientHeight; } function windowWidth() {return window.innerWidth || document.documentElement.clientWidth; } function isViewableInDirection(nearReference, farReference, containerLength) {if (nearReference > 0) {return (containerLength > nearReference); } else {return (farReference > 0); } }</script><script type="text/javascript">try {window.renderingWeblabs = window.renderingWeblabs ? window.renderingWeblabs : {}; window.renderingWeblabs = Object.assign(window.renderingWeblabs, JSON.parse('{}')); } catch (ex) {if (typeof logError === 'function') {logError('Rendering Weblab parse error', ex); } }</script><script type="text/javascript">function updateViewableLatency(adDivId, slot, placementId, arid, csaLatencyPlugin) { try { var rect = document.getElementById(adDivId).getBoundingClientRect();        if (isViewableInDirection(rect.top, rect.bottom, windowHeight()) && isViewableInDirection(rect.left, rect.right, windowWidth())) {            if(typeof uet == 'function') { uet('bb', 'adplacements:viewablelatency:' + slot, {wb:1}); if (placementId) { uet('bb', 'adplacements:viewablelatency:' + placementId, {wb:1}); } } csaLatencyPlugin('mark', 'viewablelatency:bodyBegin'); if (window.apeViewableLatencyTrackers[arid].loaded) { csaLatencyPlugin('mark', 'viewablelatency:loaded'); } if (typeof uex == 'function' && window.ue && typeof ue.count == 'function') { if (window.apeViewableLatencyTrackers[arid].loaded) { uex('ld', 'adplacements:viewablelatency:' + slot, {wb:1}); if (placementId) { uex('ld', 'adplacements:viewablelatency:' + placementId, {wb:1});  } ue.count('adplacements:htmlviewed:loaded:' + slot, 1);                    if (placementId) {                        ue.count('adplacements:htmlviewed:loaded:' + placementId, 1);}} ue.count('adplacements:htmlviewed:' + slot, 1);                if (placementId) {                    ue.count('adplacements:htmlviewed:' + placementId, 1);                }            }            window.apeViewableLatencyTrackers[arid].viewed = true;            if (window.apeViewableLatencyTrackers[arid].tracker) {                removeListener('scroll', window.apeViewableLatencyTrackers[arid].tracker);                removeListener('resize', window.apeViewableLatencyTrackers[arid].tracker);            }        }    } catch (ex) { window.apeViewableLatencyTrackers[arid].valid = false;    }}</script><div id="ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement" class="copilot-secure-display celwidget text/x-dacx-safeframe" data-ad-details="{&quot;mediaType&quot;:&quot;D&quot;,&quot;disableResizeFunc&quot;:true,&quot;disableAdReporterSlot&quot;:&quot;false&quot;,&quot;advertisementStyle&quot;:{&quot;color&quot;:&quot;rgb(85,85,85)&quot;,&quot;display&quot;:&quot;inline-block&quot;,&quot;font&quot;:&quot;11px \&quot;Amazon Ember Regular\&quot;, \&quot;Amazon Ember\&quot;, Arial&quot;,&quot;position&quot;:&quot;absolute&quot;,&quot;right&quot;:&quot;0px&quot;,&quot;top&quot;:&quot;4.5px&quot;},&quot;feedbackDivStyle&quot;:{&quot;height&quot;:&quot;14px&quot;,&quot;position&quot;:&quot;relative&quot;,&quot;top&quot;:&quot;2px&quot;},&quot;adPlacementMetaData&quot;:{&quot;searchTerms&quot;:&quot;Ym9va3N0b3JlIGFtYXpvbg==&quot;,&quot;pageUrl&quot;:&quot;aHR0cHM6Ly93d3cuYW1hem9uLmNvbS9zP2s9Ym9va3N0b3JlK2FtYXpvbiZpPXN0cmlwYm9va3Mmcmg9biUzQTI4MzE1NSUyQ24lM0ExNyUyQ3Bfbl9jb25kaXRpb24tdHlwZSUzQTY0NjE3MTYwMTEmZGMmaHZhZGlkPTYyMzE4Mjg1NDg5MiZodmRldj1jJmh2bG9jaW50PTkwNjEzMjMmaHZsb2NwaHk9MTAwMDA2MCZodm5ldHc9ZyZodnFtdD1iJmh2cmFuZD02NjYyOTk1Nzk4Nzk5MjIzNzg5Jmh2dGFyZ2lkPWt3ZC0xMzI2MzEyNiZoeWRhZGNyPTIwNjk4XzEzMjk2MTEyJnFpZD0xNjgyMjAwNzcwJnJuaWQ9NjQ2MTcxNDAxMSZ0YWc9Z29vZ2h5ZHItMjAmcmVmPXNyX25yX3Bfbl9jb25kaXRpb24tdHlwZV8xJmRzPXYxJTNBMERuWWNYWUVrRHJ3b1N1RW4xemtpejEycGhLS3RiMUw4NTVPTFZoT2prOA==&quot;,&quot;adElementId&quot;:&quot;ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement&quot;,&quot;pageType&quot;:&quot;Search&quot;,&quot;slotName&quot;:&quot;auto-bottom-advertising-0&quot;},&quot;adFeedbackInfo&quot;:{&quot;adProgramId&quot;:null,&quot;boolFeedback&quot;:true,&quot;sponsoredText&quot;:&quot;U3BvbnNvcmVkIDxiIGlkPSJhcGVfU2VhcmNoX2F1dG8tYm90dG9tLWFkdmVydGlzaW5nLTBfcG9ydGFsLWJhdGNoLWZhc3QtYnRmLWxvb21fZmVlZGJhY2tJY29uIiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB2ZXJ0aWNhbC1hbGlnbjogdGV4dC1ib3R0b207IG1hcmdpbjogMXB4IDBweDsgd2lkdGg6IDE0cHg7IGhlaWdodDogMTJweDsgYmFja2dyb3VuZDogdXJsKCdodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvRy8wMS9hZC1mZWVkYmFjay9pbmZvX2ljb25fMVhzcHJpdGUucG5nJykgMHB4IDBweCBuby1yZXBlYXQgc2Nyb2xsIHRyYW5zcGFyZW50OyIvPg==&quot;,&quot;adFeedbackOnTop&quot;:false,&quot;endPoint&quot;:&quot;/af/feedback-link&quot;},&quot;placementId&quot;:&quot;763d0af2-6ac3-4627-a3f3-fa9484d521a7&quot;,&quot;adCreativeMetaData&quot;:{&quot;adProgramId&quot;:null,&quot;adCreativeTemplateName&quot;:null,&quot;adId&quot;:null,&quot;adCreativeId&quot;:null,&quot;adNetwork&quot;:&quot;cs&quot;},&quot;measurementHtmlEncoded&quot;:&quot;&quot;,&quot;htmlContentEncoded&quot;:&quot;&quot;,&quot;expParams&quot;:{&quot;useOnPageVisible&quot;:&quot;true&quot;,&quot;allowedPages&quot;:&quot;goldbox, customerreviews, checkoutthankyou, detail, search, gateway&quot;},&quot;allowlistedCustomMessageEvents&quot;:[&quot;openPsAdPopover&quot;,&quot;openATCModal&quot;,&quot;setPartner&quot;,&quot;sendMetrics&quot;,&quot;wrap&quot;],&quot;allowlistedQueryParamKeys&quot;:[&quot;sf-overrideVariationId&quot;,&quot;sf-overridePredictorId&quot;,&quot;sf-forceFailure&quot;],&quot;allowedDomains&quot;:[&quot;g-ecx.images-amazon.com&quot;],&quot;allowedCookies&quot;:[&quot;amzn-app-ctxt&quot;],&quot;adPixels&quot;:[],&quot;adPixelDelay&quot;:0,&quot;size&quot;:{&quot;height&quot;:&quot;90px&quot;,&quot;width&quot;:&quot;728px&quot;},&quot;aaxInstrPixelUrl&quot;:null,&quot;serverSideFetchAd&quot;:&quot;false&quot;,&quot;slot&quot;:&quot;Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom&quot;,&quot;pageType&quot;:&quot;Search&quot;,&quot;subPageType&quot;:&quot;portal-batch-fast-btf-loom&quot;,&quot;slotName&quot;:&quot;auto-bottom-advertising-0&quot;,&quot;src&quot;:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=763d0af2-6ac3-4627-a3f3-fa9484d521a7&amp;src=500&amp;slot=auto-bottom-advertising-0&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,&quot;adServer&quot;:&quot;cs&quot;,&quot;arid&quot;:&quot;d8e4bcf6168f41eab5e4908036a4820c&quot;,&quot;allowChangeSize&quot;:true,&quot;allowedSizes&quot;:[{&quot;width&quot;:&quot;728px&quot;,&quot;height&quot;:&quot;90px&quot;}],&quot;loadAfter&quot;:&quot;immediate&quot;,&quot;firePixelsAfter&quot;:&quot;immediate&quot;,&quot;extraDelay&quot;:0,&quot;isCardsFlow&quot;:true,&quot;viewabilityStandards&quot;:[{&quot;p&quot;:0,&quot;t&quot;:0,&quot;def&quot;:&quot;amzn&quot;},{&quot;p&quot;:50,&quot;t&quot;:1,&quot;def&quot;:&quot;iab&quot;},{&quot;p&quot;:100,&quot;t&quot;:1,&quot;def&quot;:&quot;groupm&quot;}],&quot;aaxImpPixelUrl&quot;:null,&quot;abpStatus&quot;:&quot;0&quot;,&quot;abpAcceptable&quot;:&quot;true&quot;,&quot;advertisementTextHTMLContentEncoded&quot;:&quot;PGRpdiBpZD0iYXBlX1NlYXJjaF9hdXRvLWJvdHRvbS1hZHZlcnRpc2luZy0wX3BvcnRhbC1iYXRjaC1mYXN0LWJ0Zi1sb29tX3RleHQtd3JhcHBlciIgPjxkaXYgaWQ9ImFwZV9TZWFyY2hfYXV0by1ib3R0b20tYWR2ZXJ0aXNpbmctMF9wb3J0YWwtYmF0Y2gtZmFzdC1idGYtbG9vbV90ZXh0IiAgPlNwb25zb3JlZDwvZGl2PjwvZGl2Pg==&quot;,&quot;safeframe&quot;:&quot;https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.f6332db.js&quot;,&quot;sfPageStyle&quot;:&quot;<style>@media screen and (max-width:240px){ div[id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ width:auto !important;margin-left:auto !important; left:auto !important} div[id$=search_btf_search-mWeb_text-wrapper]{ width:auto !important;margin-left:auto !important;left:auto !important}}@media screen and (orientation:landscape){ [id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ max-width:728px !important; margin-left:auto !important; margin-right:auto !important;} [id$=search_btf_search-mWeb_text-wrapper]{ max-width:728px !important;margin:auto !important}}#mobile-ad-image-centered{background-size:728px 90px !important}</style>&quot;,&quot;isDesktop&quot;:true}" aria-hidden="true" data-csa-c-type="widget" data-csa-c-slot-id="adplacements:Search:auto-bottom-advertising-0:portal-batch-fast-btf-loom" data-csa-c-content-id="763d0af2-6ac3-4627-a3f3-fa9484d521a7" data-csa-op-log-render="" style="width:728px;height:120px;margin-left:auto;margin-right:auto;margin-top:16px" data-csa-c-id="yglpk8-wckv9m-7u5ql2-3un9dh" data-arid="d8e4bcf6168f41eab5e4908036a4820c" cel_widget_id="adplacements:Search:auto-bottom-advertising-0:portal-batch-fast-btf-loom" data-cel-widget="adplacements:Search:auto-bottom-advertising-0:portal-batch-fast-btf-loom"><iframe name="{&quot;mediaType&quot;:&quot;D&quot;,&quot;disableResizeFunc&quot;:true,&quot;disableAdReporterSlot&quot;:&quot;false&quot;,&quot;advertisementStyle&quot;:{&quot;color&quot;:&quot;rgb(85,85,85)&quot;,&quot;display&quot;:&quot;inline-block&quot;,&quot;font&quot;:&quot;11px \&quot;Amazon Ember Regular\&quot;, \&quot;Amazon Ember\&quot;, Arial&quot;,&quot;position&quot;:&quot;absolute&quot;,&quot;right&quot;:&quot;0px&quot;,&quot;top&quot;:&quot;4.5px&quot;},&quot;feedbackDivStyle&quot;:{&quot;height&quot;:&quot;14px&quot;,&quot;position&quot;:&quot;relative&quot;,&quot;top&quot;:&quot;2px&quot;},&quot;adPlacementMetaData&quot;:{&quot;searchTerms&quot;:&quot;Ym9va3N0b3JlIGFtYXpvbg==&quot;,&quot;pageUrl&quot;:&quot;aHR0cHM6Ly93d3cuYW1hem9uLmNvbS9zP2s9Ym9va3N0b3JlK2FtYXpvbiZpPXN0cmlwYm9va3Mmcmg9biUzQTI4MzE1NSUyQ24lM0ExNyUyQ3Bfbl9jb25kaXRpb24tdHlwZSUzQTY0NjE3MTYwMTEmZGMmaHZhZGlkPTYyMzE4Mjg1NDg5MiZodmRldj1jJmh2bG9jaW50PTkwNjEzMjMmaHZsb2NwaHk9MTAwMDA2MCZodm5ldHc9ZyZodnFtdD1iJmh2cmFuZD02NjYyOTk1Nzk4Nzk5MjIzNzg5Jmh2dGFyZ2lkPWt3ZC0xMzI2MzEyNiZoeWRhZGNyPTIwNjk4XzEzMjk2MTEyJnFpZD0xNjgyMjAwNzcwJnJuaWQ9NjQ2MTcxNDAxMSZ0YWc9Z29vZ2h5ZHItMjAmcmVmPXNyX25yX3Bfbl9jb25kaXRpb24tdHlwZV8xJmRzPXYxJTNBMERuWWNYWUVrRHJ3b1N1RW4xemtpejEycGhLS3RiMUw4NTVPTFZoT2prOA==&quot;,&quot;adElementId&quot;:&quot;ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement&quot;,&quot;pageType&quot;:&quot;Search&quot;,&quot;slotName&quot;:&quot;auto-bottom-advertising-0&quot;},&quot;adFeedbackInfo&quot;:{&quot;adProgramId&quot;:null,&quot;boolFeedback&quot;:true,&quot;sponsoredText&quot;:&quot;U3BvbnNvcmVkIDxiIGlkPSJhcGVfU2VhcmNoX2F1dG8tYm90dG9tLWFkdmVydGlzaW5nLTBfcG9ydGFsLWJhdGNoLWZhc3QtYnRmLWxvb21fZmVlZGJhY2tJY29uIiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB2ZXJ0aWNhbC1hbGlnbjogdGV4dC1ib3R0b207IG1hcmdpbjogMXB4IDBweDsgd2lkdGg6IDE0cHg7IGhlaWdodDogMTJweDsgYmFja2dyb3VuZDogdXJsKCdodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvRy8wMS9hZC1mZWVkYmFjay9pbmZvX2ljb25fMVhzcHJpdGUucG5nJykgMHB4IDBweCBuby1yZXBlYXQgc2Nyb2xsIHRyYW5zcGFyZW50OyIvPg==&quot;,&quot;adFeedbackOnTop&quot;:false,&quot;endPoint&quot;:&quot;/af/feedback-link&quot;},&quot;placementId&quot;:&quot;763d0af2-6ac3-4627-a3f3-fa9484d521a7&quot;,&quot;adCreativeMetaData&quot;:{&quot;adProgramId&quot;:null,&quot;adCreativeTemplateName&quot;:null,&quot;adId&quot;:null,&quot;adCreativeId&quot;:null,&quot;adNetwork&quot;:&quot;cs&quot;},&quot;measurementHtmlEncoded&quot;:&quot;&quot;,&quot;htmlContentEncoded&quot;:&quot;&quot;,&quot;expParams&quot;:{&quot;useOnPageVisible&quot;:&quot;true&quot;,&quot;allowedPages&quot;:&quot;goldbox, customerreviews, checkoutthankyou, detail, search, gateway&quot;},&quot;allowlistedCustomMessageEvents&quot;:[&quot;openPsAdPopover&quot;,&quot;openATCModal&quot;,&quot;setPartner&quot;,&quot;sendMetrics&quot;,&quot;wrap&quot;],&quot;allowlistedQueryParamKeys&quot;:[&quot;sf-overrideVariationId&quot;,&quot;sf-overridePredictorId&quot;,&quot;sf-forceFailure&quot;],&quot;allowedDomains&quot;:[&quot;g-ecx.images-amazon.com&quot;,&quot;d3l3lkinz3f56t.cloudfront.net&quot;,&quot;g-ecx.images-amazon.com&quot;,&quot;z-ecx.images-amazon.com&quot;,&quot;images-na.ssl-images-amazon.com&quot;,&quot;g-ec4.images-amazon.com&quot;,&quot;images-cn.ssl-images-amazon.com&quot;],&quot;allowedCookies&quot;:[&quot;amzn-app-ctxt&quot;],&quot;adPixels&quot;:[],&quot;adPixelDelay&quot;:0,&quot;size&quot;:{&quot;height&quot;:&quot;90px&quot;,&quot;width&quot;:&quot;728px&quot;},&quot;aaxInstrPixelUrl&quot;:null,&quot;serverSideFetchAd&quot;:&quot;false&quot;,&quot;slot&quot;:&quot;Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom&quot;,&quot;pageType&quot;:&quot;Search&quot;,&quot;subPageType&quot;:&quot;portal-batch-fast-btf-loom&quot;,&quot;slotName&quot;:&quot;auto-bottom-advertising-0&quot;,&quot;src&quot;:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=763d0af2-6ac3-4627-a3f3-fa9484d521a7&amp;src=500&amp;slot=auto-bottom-advertising-0&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,&quot;adServer&quot;:&quot;cs&quot;,&quot;arid&quot;:&quot;d8e4bcf6168f41eab5e4908036a4820c&quot;,&quot;allowChangeSize&quot;:true,&quot;allowedSizes&quot;:[{&quot;width&quot;:&quot;728px&quot;,&quot;height&quot;:&quot;90px&quot;},{&quot;height&quot;:&quot;90px&quot;,&quot;width&quot;:&quot;728px&quot;}],&quot;loadAfter&quot;:&quot;immediate&quot;,&quot;firePixelsAfter&quot;:&quot;immediate&quot;,&quot;extraDelay&quot;:0,&quot;isCardsFlow&quot;:true,&quot;viewabilityStandards&quot;:[{&quot;p&quot;:0,&quot;t&quot;:0,&quot;def&quot;:&quot;amzn&quot;},{&quot;p&quot;:50,&quot;t&quot;:1,&quot;def&quot;:&quot;iab&quot;},{&quot;p&quot;:100,&quot;t&quot;:1,&quot;def&quot;:&quot;groupm&quot;}],&quot;aaxImpPixelUrl&quot;:null,&quot;abpStatus&quot;:&quot;0&quot;,&quot;abpAcceptable&quot;:&quot;true&quot;,&quot;advertisementTextHTMLContentEncoded&quot;:&quot;PGRpdiBpZD0iYXBlX1NlYXJjaF9hdXRvLWJvdHRvbS1hZHZlcnRpc2luZy0wX3BvcnRhbC1iYXRjaC1mYXN0LWJ0Zi1sb29tX3RleHQtd3JhcHBlciIgPjxkaXYgaWQ9ImFwZV9TZWFyY2hfYXV0by1ib3R0b20tYWR2ZXJ0aXNpbmctMF9wb3J0YWwtYmF0Y2gtZmFzdC1idGYtbG9vbV90ZXh0IiAgPlNwb25zb3JlZDwvZGl2PjwvZGl2Pg==&quot;,&quot;safeframe&quot;:&quot;https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.f6332db.js&quot;,&quot;sfPageStyle&quot;:&quot;<style>@media screen and (max-width:240px){ div[id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ width:auto !important;margin-left:auto !important; left:auto !important} div[id$=search_btf_search-mWeb_text-wrapper]{ width:auto !important;margin-left:auto !important;left:auto !important}}@media screen and (orientation:landscape){ [id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ max-width:728px !important; margin-left:auto !important; margin-right:auto !important;} [id$=search_btf_search-mWeb_text-wrapper]{ max-width:728px !important;margin:auto !important}}#mobile-ad-image-centered{background-size:728px 90px !important}</style>&quot;,&quot;isDesktop&quot;:true,&quot;hostDomain&quot;:&quot;https://www.amazon.com&quot;,&quot;queryParams&quot;:{},&quot;aPageStart&quot;:1682200776020,&quot;adStartTime&quot;:1682200776491,&quot;safeFrameSrc&quot;:&quot;https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/sf-1.50.f6332db.html&quot;}" id="ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_iframe" height="90px" width="728px" class="" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" allowtransparency="true" data-arid="d8e4bcf6168f41eab5e4908036a4820c" src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/sf-1.50.f6332db.html" sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation allow-same-origin" style=""></iframe><div id="ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement_Feedback" style="height: 14px; position: relative; top: 2px;"><script>(function (window, document, Math) {
    try {
        var changeLinkColor = function () {
            document.getElementById("ad-feedback-text-auto-bottom-advertising-0").style.color = '#111111';
            document.getElementById("ad-feedback-sprite-auto-bottom-advertising-0").style.background = 'transparent url("https://m.media-amazon.com/images/G/01/ad-feedback/info_icon_1Xsprite.png") no-repeat 0px -12px';
        }
        var defaultLinkBehaviour = function() {
            document.getElementById("ad-feedback-text-auto-bottom-advertising-0").style.textDecoration = 'none';
            document.getElementById("ad-feedback-text-auto-bottom-advertising-0").style.color = '#555555';
            document.getElementById("ad-feedback-sprite-auto-bottom-advertising-0").style.background = 'transparent url("https://m.media-amazon.com/images/G/01/ad-feedback/info_icon_1Xsprite.png") no-repeat scroll 0px 0px';
        }
window.changeLinkColor2a6849c8af504f6e89161a0fc5c785f9 = changeLinkColor;
window.defaultLinkBehaviour2a6849c8af504f6e89161a0fc5c785f9 = defaultLinkBehaviour;
    } catch(ex) {
        if(window.ueLogError) {
            var additionalInfo = {
                logLevel : 'ERROR',
                attribution : 'Ad Feedback',
                message : 'Error in Feedback js '
            };
            window.ueLogError(ex, additionalInfo);
        }
    }
})(window, document, Math);</script><a data-a-modal="{&quot;url&quot;:&quot;/af/feedback-form?pl=%7B%22adPlacementMetaData%22%3A%7B%22searchTerms%22%3A%22Ym9va3N0b3JlIGFtYXpvbg%3D%3D%22%2C%22pageUrl%22%3A%22aHR0cHM6Ly93d3cuYW1hem9uLmNvbS9zP2s9Ym9va3N0b3JlK2FtYXpvbiZpPXN0cmlwYm9va3Mmcmg9biUzQTI4MzE1NSUyQ24lM0ExNyUyQ3Bfbl9jb25kaXRpb24tdHlwZSUzQTY0NjE3MTYwMTEmZGMmaHZhZGlkPTYyMzE4Mjg1NDg5MiZodmRldj1jJmh2bG9jaW50PTkwNjEzMjMmaHZsb2NwaHk9MTAwMDA2MCZodm5ldHc9ZyZodnFtdD1iJmh2cmFuZD02NjYyOTk1Nzk4Nzk5MjIzNzg5Jmh2dGFyZ2lkPWt3ZC0xMzI2MzEyNiZoeWRhZGNyPTIwNjk4XzEzMjk2MTEyJnFpZD0xNjgyMjAwNzcwJnJuaWQ9NjQ2MTcxNDAxMSZ0YWc9Z29vZ2h5ZHItMjAmcmVmPXNyX25yX3Bfbl9jb25kaXRpb24tdHlwZV8xJmRzPXYxJTNBMERuWWNYWUVrRHJ3b1N1RW4xemtpejEycGhLS3RiMUw4NTVPTFZoT2prOA%3D%3D%22%2C%22adElementId%22%3A%22ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement%22%2C%22pageType%22%3A%22Search%22%2C%22slotName%22%3A%22auto-bottom-advertising-0%22%7D%2C%22adCreativeMetaData%22%3A%7B%22adProgramId%22%3Anull%2C%22adCreativeTemplateName%22%3Anull%2C%22adId%22%3Anull%2C%22adCreativeId%22%3Anull%2C%22adNetwork%22%3A%22cs%22%7D%7D&amp;daFlg=true&amp;ie=UTF-8&quot;,     &quot;name&quot;:&quot;shared-placement-feedback-modal-auto-bottom-advertising-0&quot;,&quot;header&quot;:&quot;Leave feedback&quot;,&quot;width&quot;:&quot;460&quot;}" style="position: absolute; top: 2px; right: 0px; display: inline-block; font-size: 11px; color: rgb(85, 85, 85);
        cursor: pointer; text-decoration: none;" data-action="a-modal" class="a-declarative" tabindex="0">
        <span style="text-decoration: none;" id="ad-feedback-text-auto-bottom-advertising-0" onmouseover="window.changeLinkColor2a6849c8af504f6e89161a0fc5c785f9()" onmouseout="window.defaultLinkBehaviour2a6849c8af504f6e89161a0fc5c785f9()" aria-hidden="false" aria-label="Leave feedback on Sponsored ad"> Sponsored
        <b id="ad-feedback-sprite-auto-bottom-advertising-0" style="display: inline-block; vertical-align: text-bottom; margin: 1px 0px; width: 14px; height: 12px; background: transparent url(&quot;https://m.media-amazon.com/images/G/01/ad-feedback/info_icon_1Xsprite.png&quot;) no-repeat scroll 0px 0px;"></b></span></a></div></div><script type="text/javascript">if(window.csa) {var csaLatencyPlugin; var placementDiv = document.getElementById('ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement'); if (!true) {csaLatencyPlugin = window.csa('Content', {element: placementDiv.parentNode}); } else {csaLatencyPlugin = window.csa('Content', {element: placementDiv}); } csaLatencyPlugin('mark', 'bodyBegin'); } try {window.apeViewableLatencyTrackers = window.apeViewableLatencyTrackers || {}; var adDivId = 'ape_Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom_placement'; var slot = 'Search_auto-bottom-advertising-0_portal-batch-fast-btf-loom'.replace(/\_/g, ':'); var placementId = '763d0af2-6ac3-4627-a3f3-fa9484d521a7'; var arid = 'd8e4bcf6168f41eab5e4908036a4820c'; window.apeViewableLatencyTrackers[arid] = window.apeViewableLatencyTrackers[arid] || {}; window.apeViewableLatencyTrackers[arid].valid = true; updateViewableLatency(adDivId, slot, placementId, arid, csaLatencyPlugin); if (window.apeViewableLatencyTrackers[arid].valid) {if (!window.apeViewableLatencyTrackers[arid].viewed) {window.apeViewableLatencyTrackers[arid].tracker = throttle(function() {updateViewableLatency(adDivId, slot, placementId, arid, csaLatencyPlugin); }, 20); addListener('scroll', window.apeViewableLatencyTrackers[arid].tracker); addListener('resize', window.apeViewableLatencyTrackers[arid].tracker); } } } catch(ex) {if (window.apeViewableLatencyTrackers) {if (window.apeViewableLatencyTrackers['d8e4bcf6168f41eab5e4908036a4820c']) {window.apeViewableLatencyTrackers['d8e4bcf6168f41eab5e4908036a4820c'].valid = false; } } logError('Error initializing viewable latency instrumentation', ex); }</script><script type="text/javascript">try {window['auto-bottom-advertising-0'] = {}; window['auto-bottom-advertising-0'].adStartTime = (new Date()).getTime(); if(window.DAsf) {window.DAsf.loadAds(); } else if (window.MAsf) {window.MAsf.loadAds(); } else {var sfSrc='https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.f6332db.js?csm_attribution=APE-SafeFrame'; importScript (sfSrc);} } catch(ex) {console.log('Error appending DAsf library'); logError('Error appending DAsf library', ex); }</script></div><script>if(window.mix_csa){window.mix_csa('[cel_widget_id="ape-safeframe-card_loom-desktop-footer-slot_63"]', '#CardInstanceMAcD7Va_iyzHfagyHj7-dQ')('mark', 'be')}</script>
<script>if(window.uet){window.uet('be','ape-safeframe-card_loom-desktop-footer-slot_63',{wb: 1})}</script>
<script>P.when('mix:@amzn/mix.client-runtime', 'mix:ape-safeframe-card__7EyRfVzy').execute(function (runtime, cardModule) {runtime.registerCardFactory('CardInstanceMAcD7Va_iyzHfagyHj7-dQ', cardModule).then(function(){if(window.mix_csa){window.mix_csa('[cel_widget_id="ape-safeframe-card_loom-desktop-footer-slot_63"]', '#CardInstanceMAcD7Va_iyzHfagyHj7-dQ')('mark', 'functional')}if(window.uex){window.uex('ld','ape-safeframe-card_loom-desktop-footer-slot_63',{wb: 1})}});});
</script>
<script>P.load.js('https://images-na.ssl-images-amazon.com/images/I/11-OOS888GL.js?xcp');
</script>
</div></div></div>

    
    
    

    



    
        
        

        
    
    


              </div>
              <div class="s-result-list-placeholder aok-hidden sg-row">
                  <div class="a-spinner-wrapper"><span class="a-spinner a-spinner-medium"></span></div>
              </div>
          </span>

          <div class="s-screenreader">
              
              <a class="a-link-normal aok-offscreen" title="tab to go back to filtering menu" href="#s-skipLinkTargetForFilterOptions">
                  Go back to filtering menu
              </a>
          </div>

          
          <span data-component-type="s-pagination" class="rush-component" data-component-id="72"></span>
      </div></div>
      <div class="sg-col-4-of-24 sg-col-4-of-12 s-matching-dir sg-col-4-of-16 sg-col sg-col-4-of-20"><div class="sg-col-inner">
          <div class="s-screenreader">
              
              <a class="a-link-normal aok-offscreen" title="tab to skip to main search results" href="#s-skipLinkTargetForMainSearchResults">
                  Skip to main search results
              </a>
          </div>
          <div id="s-skipLinkTargetForFilterOptions" tabindex="-1"></div>

          
          <div class="a-section">
              <span data-component-type="s-filters-panel-view" class="rush-component" data-component-id="73">
                  
                      
                      <div data-uuid="ba960af3-e20c-4c0c-9421-297a689fd512" cel_widget_id="LEFT-REFINEMENTS-0" class="s-widget-container s-spacing-medium s-widget-container-height-medium celwidget slot=LEFT template=REFINEMENTS widgetId=refinements" data-csa-c-id="ptsuxn-618kmv-acfxej-435c3n" data-cel-widget="LEFT-REFINEMENTS-0">





<div id="s-refinements" class="a-section a-spacing-none">
  
  <div class="a-section a-spacing-double-large">
    
    
      






<div id="departments" class="a-section a-spacing-none">
    
    
        








    
    
        <div id="n-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Department</span>
        </div>
    
    



<ul data-csa-c-content-id="" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="n-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="j7edjv-8p8lg7-6o3hx9-e682d4">
    
    

    
    
        







<li id="n" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="off" class="a-link-normal s-navigation-item" href="/s?k=bookstore+amazon&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_ex_n_0&amp;ds=v1%3AnaAiRwN7vFCRpUN%2FD0q5vPvLyvqwBwJ0xQ%2Fs5hE6qSY">
      
    
        <span class="s-back-arrow aok-inline-block"></span>
    
    <span class="a-size-base a-color-base">Any Department</span>
  
    </a>
  
  


</span></li>










    
        







<li id="n/283155" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="off" class="a-link-normal s-navigation-item" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cp_n_condition-type%3A6461716011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;tag=googhydr-20&amp;ref=sr_ex_n_1&amp;ds=v1%3AdoOLSq%2B6umHbZCxafMal8Ep9P1k0g%2FVP8u6dhzDGHkU">
      
    
        <span class="s-back-arrow aok-inline-block"></span>
    
    <span class="a-size-base a-color-base">Books</span>
  
    </a>
  
  


</span></li>










    
        







<li id="n/17" class="a-spacing-micro s-navigation-indent-1"><span class="a-list-item">
  











  
  
    
    
    <span class="a-size-base a-color-base a-text-bold">Literature &amp; Fiction</span>
  
  


</span></li>










    

    
    
    

    
    
</ul>

    
</div>

    
      






<div id="reviewsRefinements" class="a-section a-spacing-none">
    
    
        








    
    
        <div id="p_72-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Customer Reviews</span>
        </div>
    
    



<ul data-csa-c-content-id="2661617011" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="p_72-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="m72gcp-yy3jlv-o884wc-lapw3w">
    
    

    
    
        







<li id="p_72/2661618011"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_72%3A2661618011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=2661617011&amp;tag=googhydr-20&amp;ref=sr_nr_p_72_1&amp;ds=v1%3Af7yXNZ3mIF15IO9JpfxRw7fFJMLsrn62NOOdxQ4iVUw">
      
    <section aria-label="4 Stars &amp; Up">
      <i class="a-icon a-icon-star-medium a-star-medium-4"><span class="a-icon-alt">4 Stars &amp; Up</span></i>
      <span class="a-size-small a-color-base">&amp; Up</span>
    </section>
  
    </a>
  
  


</span></li>

    
        







<li id="p_72/2661619011"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_72%3A2661619011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=2661617011&amp;tag=googhydr-20&amp;ref=sr_nr_p_72_2&amp;ds=v1%3AiDZxAbAOg0SrY4B5ooAQUrkg8s9UW43dt5HpZs%2FEBIg">
      
    <section aria-label="3 Stars &amp; Up">
      <i class="a-icon a-icon-star-medium a-star-medium-3"><span class="a-icon-alt">3 Stars &amp; Up</span></i>
      <span class="a-size-small a-color-base">&amp; Up</span>
    </section>
  
    </a>
  
  


</span></li>

    
        







<li id="p_72/2661620011"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_72%3A2661620011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=2661617011&amp;tag=googhydr-20&amp;ref=sr_nr_p_72_3&amp;ds=v1%3A8cYvrvvMw5vFVr45MdidnlHk3uwHX8ZeK%2BKH4Mzeckw">
      
    <section aria-label="2 Stars &amp; Up">
      <i class="a-icon a-icon-star-medium a-star-medium-2"><span class="a-icon-alt">2 Stars &amp; Up</span></i>
      <span class="a-size-small a-color-base">&amp; Up</span>
    </section>
  
    </a>
  
  


</span></li>

    
        







<li id="p_72/2661621011"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_72%3A2661621011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=2661617011&amp;tag=googhydr-20&amp;ref=sr_nr_p_72_4&amp;ds=v1%3AcU4Ml0CqTijp2tje6kCylh6xx9xVJ3rCiwWb2dQyNbk">
      
    <section aria-label="1 Star &amp; Up">
      <i class="a-icon a-icon-star-medium a-star-medium-1"><span class="a-icon-alt">1 Star &amp; Up</span></i>
      <span class="a-size-small a-color-base">&amp; Up</span>
    </section>
  
    </a>
  
  


</span></li>

    

    
    
    

    
    
</ul>

    
</div>

    
      






<div id="priceRefinements" class="a-section a-spacing-none">
    
    
        








    
    
        <div id="p_n_deal_type-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Deals &amp; Discounts</span>
        </div>
    
    



<ul data-csa-c-content-id="23566063011" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="p_n_deal_type-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="kn2dq-4uwmrl-i4ctb0-c5z6m">
    
    

    
    
        





<li id="p_n_deal_type/23566065011" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_n_deal_type%3A23566065011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=23566063011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_deal_type_1&amp;ds=v1%3AQhtTUDdNE9%2FI%2FuvvlpoaCNh1x045m5Ne3%2FFGWyFw%2BJ0">
      
    <span class="a-size-base a-color-base">All Discounts</span>
  
    </a>
  
  


</span></li>


    
        





<li id="p_n_deal_type/23566064011" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_n_deal_type%3A23566064011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=23566063011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_deal_type_2&amp;ds=v1%3AYyunQLJyi5DfNp%2F7reaOAUqBEeT3fyLg5%2B5Ss7Y6mNA">
      
    <span class="a-size-base a-color-base">Today's Deals</span>
  
    </a>
  
  


</span></li>


    

    
    
    

    
    
</ul>

    
</div>

    
      






<div id="filters" class="a-section a-spacing-none">
    
    
        








    
    
        <div id="p_n_condition-type-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Condition</span>
        </div>
    
    



<ul data-csa-c-content-id="6461714011" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="p_n_condition-type-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="mhkroi-jjas45-s3xzx9-lbnzz3">
    
    
        <li class="a-spacing-micro s-list-item"><span class="a-list-item">
            <a class="a-link-normal s-navigation-item s-navigation-clear-link" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;tag=googhydr-20&amp;ref=sr_ex_p_n_condition-type_0&amp;ds=v1%3AlQbLuGb8JF%2FC34KW1o7%2BUrTuhLjb2ogik1E%2B%2BtNttNc">
                <span class="s-back-arrow aok-inline-block"></span>
                <span class="a-size-base a-color-base">Condition</span>
            </a>
        </span></li>
    

    
    
        





<li id="p_n_condition-type/6461716011" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_condition-type_1&amp;ds=v1%3ACmflsK1tY9y2SWT2NLHIY7kgOscd3DqJV%2FYrJaU1HeA">
      
    <span class="a-size-base a-color-base a-text-bold">New</span>
  
    </a>
  
  


</span></li>


    
        





<li id="p_n_condition-type/6461718011" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461718011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=6461714011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_condition-type_2&amp;ds=v1%3AIzQMcAmBGnCT%2F5dwsH%2BcVYWRLnlm2RinEmA8iDElSAI">
      
    <span class="a-size-base a-color-base">Used</span>
  
    </a>
  
  


</span></li>


    

    
    
    

    
    
</ul>

    
        








    
    
        <div id="p_n_is-global-store-asin-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Amazon Global Store</span>
        </div>
    
    



<ul data-csa-c-content-id="16354392011" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="p_n_is-global-store-asin-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="h2tjh3-mw8w1z-gitxgo-ymhs17">
    
    

    
    
        






<li id="p_n_is-global-store-asin/16354393011" aria-label="Amazon Global Store" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" tabindex="-1" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_n_is-global-store-asin%3A16354393011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=16354392011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_is-global-store-asin_1&amp;ds=v1%3AWwLJSmZOY4yPRii1dqfIeTgnYYC6RN99XtDjfq5VQYA">
      
    <div class="a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    <span class="a-size-base a-color-base">Amazon Global Store</span>

    
  
    </a>
  
  


</span></li>

    

    
    
    

    
    
</ul>

    
        








    
    
        <div id="p_n_availability-title" class="a-section a-spacing-small">
            <span class="a-size-base a-color-base puis-bold-weight-text">Availability</span>
        </div>
    
    



<ul data-csa-c-content-id="2661599011" data-csa-c-slot-id="nav-ref" data-csa-c-type="element" aria-labelledby="p_n_availability-title" class="a-unordered-list a-nostyle a-vertical a-spacing-medium" data-csa-c-id="65iiea-fjw5gl-di9s1q-cak1px">
    
    

    
    
        






<li id="p_n_availability/2661601011" aria-label="Include Out of Stock" class="a-spacing-micro"><span class="a-list-item">
  











  
    <a data-routing="" class="a-link-normal s-navigation-item" rel="nofollow" tabindex="-1" href="/s?k=bookstore+amazon&amp;i=stripbooks&amp;rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011%2Cp_n_availability%3A2661601011&amp;dc&amp;hvadid=623182854892&amp;hvdev=c&amp;hvlocint=9061323&amp;hvlocphy=1000060&amp;hvnetw=g&amp;hvqmt=b&amp;hvrand=6662995798799223789&amp;hvtargid=kwd-13263126&amp;hydadcr=20698_13296112&amp;qid=1682200775&amp;rnid=2661599011&amp;tag=googhydr-20&amp;ref=sr_nr_p_n_availability_2&amp;ds=v1%3AZznaiWbtktqnGUZ6GSDo7oX3HRQepwHrrDzIXTgyQ48">
      
    <div class="a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    <span class="a-size-base a-color-base">Include Out of Stock</span>

    
  
    </a>
  
  


</span></li>

    

    
    
    

    
    
</ul>

    
</div>

    
  </div>
</div>
</div>
                  
                      
                      <div data-uuid="57d03b01-e4a5-4371-b6d1-7893745b61fb" cel_widget_id="LEFT-SAFE_FRAME-1" class="s-widget-container s-spacing-medium s-widget-container-height-medium s-left-ads-item celwidget slot=LEFT template=SAFE_FRAME widget=loom-desktop-skyscraper_adPlacements:amazon.us.Search.search-desktop-loom.auto-left-advertising-1:null pf_rd_p=bc1ecf49-f761-4e28-9d00-d6eaa9787a51 pf_rd_r=BNJYY9EBY54VZZF6X4X6 pd_rd_wg-MBnpm pd_rd_w-bTneI content-id=amzn1.sym.bc1ecf49-f761-4e28-9d00-d6eaa9787a51:amzn1.sym.bc1ecf49-f761-4e28-9d00-d6eaa9787a51 pd_rd_r-12c1c0da-5406-44f9-9360-6d381729e9e2 widgetId=loom-desktop-skyscraper_adPlacements:amazon.us.Search.search-desktop-loom.auto-left-advertising-1:null" data-csa-c-content-id="amzn1.sym.bc1ecf49-f761-4e28-9d00-d6eaa9787a51:amzn1.sym.bc1ecf49-f761-4e28-9d00-d6eaa9787a51" data-csa-op-log-render="" data-csa-c-slot-id="LEFT" data-csa-c-type="widget" data-csa-c-id="joq57d-wccrjt-rtour1-6yox66" data-cel-widget="LEFT-SAFE_FRAME-1">
<div class="amzn-safe-frame-container">
        <script> window.uet && uet('bb', 'searchSafeFrame:LEFT', {wb: 1}); </script>

    <div class="amzn-safe-frame-sizing" style="width: 160px;">
        <iframe srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;3b9d2369-41c0-4713-bfd6-93100e1036de&quot;;</script>
    <script>
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <div id='ape_Search_auto-left-advertising-1_search-desktop-loom_wrapper' class='celwidget'  aria-hidden='true' > <style>@media screen and (max-width:240px){ div[id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ width:auto !important;margin-left:auto !important; left:auto !important} div[id$=search_btf_search-mWeb_text-wrapper]{ width:auto !important;margin-left:auto !important;left:auto !important}}@media screen and (orientation:landscape){ [id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ max-width:160px !important; margin-left:auto !important; margin-right:auto !important;} [id$=search_btf_search-mWeb_text-wrapper]{ max-width:160px !important;margin:auto !important}}#mobile-ad-image-centered{background-size:160px 600px !important}</style> <div id='ape_Search_auto-left-advertising-1_search-desktop-loom_placement' ></div></div><script type=&quot;text/javascript&quot;>SafeFrameClient.on('clientReady', function() {var sendCsmMetric=function(b,d){var a=SafeFrameClient.sendMetrics;if(typeof a===&quot;function&quot;){var c=d?d+&quot;:&quot;:&quot;&quot;;a(b,&quot;adplacements:&quot;+c+&quot;search:auto-left-advertising-1:search-desktop-loom&quot;);a(b,&quot;adplacements:&quot;+c+&quot;861886d1-4725-46d2-8855-cf52b935b57c&quot;);}};sendCsmMetric(&quot;bb&quot;);window[&quot;auto-left-advertising-1&quot;]={};window[&quot;auto-left-advertising-1&quot;].adStartTime=(new Date()).getTime();document.addEventListener(&quot;ihjsloaded&quot;,function(){var a={abpStatus:&quot;0&quot;,sfInnerStyle:&quot;&quot;,containerSelector:&quot;#ape_Search_auto-left-advertising-1_search-desktop-loom_placement&quot;,sfLogErrors:&quot;false&quot;,onError:SafeFrameClient.collapse,iframeSrc:&quot;https://d1lxz4vuik53pc.cloudfront.net/ii/1664280591753/inner.html&quot;,iframeId:&quot;ad-placements_inner-frame&quot;,scope:&quot;search:auto-left-advertising-1:search-desktop-loom&quot;,loadAfter:&quot;immediate&quot;,extraDelay:&quot;0&quot;,prerenderLogicEnabled:&quot;false&quot;,adWidth:&quot;160px&quot;,adHeight:&quot;600px&quot;,maxAdWidth:&quot;&quot;,boolFeedback:&quot;true&quot;,encodedHtmlContent:&quot;true&quot;,prefetchEnabled:&quot;false&quot;,src:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=861886d1-4725-46d2-8855-cf52b935b57c&amp;src=500&amp;slot=auto-left-advertising-1&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,aaxInstrPixelUrl:&quot;&quot;,aaxImpPixelUrl:&quot;&quot;,pageType:&quot;Search&quot;,slotName:&quot;auto-left-advertising-1&quot;,subPageType:&quot;search-desktop-loom&quot;,htmlContent:&quot;&quot;,adNetwork:&quot;cs&quot;,invalidFallback:&quot;true&quot;,extras:&quot;{}&quot;};try{window.initInnerHost(a);}catch(b){SafeFrameClient.collapse();}});var scriptElement=document.createElement(&quot;script&quot;);scriptElement.src=&quot;https://d1lxz4vuik53pc.cloudfront.net/ih/1664280594355/inner-host.min.js&quot;;scriptElement.type=&quot;text/javascript&quot;;scriptElement.async=true;sendCsmMetric(&quot;af&quot;);document.body.appendChild(scriptElement);});</script>

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;3b9d2369-41c0-4713-bfd6-93100e1036de&quot;;</script>
    <script>
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <div id='ape_Search_auto-left-advertising-1_search-desktop-loom_wrapper' class='celwidget'  aria-hidden='true' > <style>@media screen and (max-width:240px){ div[id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ width:auto !important;margin-left:auto !important; left:auto !important} div[id$=search_btf_search-mWeb_text-wrapper]{ width:auto !important;margin-left:auto !important;left:auto !important}}@media screen and (orientation:landscape){ [id$=ape_search_btf_search-mWeb-Percolate-AdPlacementTemplate_wrapper]{ max-width:160px !important; margin-left:auto !important; margin-right:auto !important;} [id$=search_btf_search-mWeb_text-wrapper]{ max-width:160px !important;margin:auto !important}}#mobile-ad-image-centered{background-size:160px 600px !important}</style> <div id='ape_Search_auto-left-advertising-1_search-desktop-loom_placement' ></div></div><script type=&quot;text/javascript&quot;>SafeFrameClient.on('clientReady', function() {var sendCsmMetric=function(b,d){var a=SafeFrameClient.sendMetrics;if(typeof a===&quot;function&quot;){var c=d?d+&quot;:&quot;:&quot;&quot;;a(b,&quot;adplacements:&quot;+c+&quot;search:auto-left-advertising-1:search-desktop-loom&quot;);a(b,&quot;adplacements:&quot;+c+&quot;861886d1-4725-46d2-8855-cf52b935b57c&quot;);}};sendCsmMetric(&quot;bb&quot;);window[&quot;auto-left-advertising-1&quot;]={};window[&quot;auto-left-advertising-1&quot;].adStartTime=(new Date()).getTime();document.addEventListener(&quot;ihjsloaded&quot;,function(){var a={abpStatus:&quot;0&quot;,sfInnerStyle:&quot;&quot;,containerSelector:&quot;#ape_Search_auto-left-advertising-1_search-desktop-loom_placement&quot;,sfLogErrors:&quot;false&quot;,onError:SafeFrameClient.collapse,iframeSrc:&quot;https://d1lxz4vuik53pc.cloudfront.net/ii/1664280591753/inner.html&quot;,iframeId:&quot;ad-placements_inner-frame&quot;,scope:&quot;search:auto-left-advertising-1:search-desktop-loom&quot;,loadAfter:&quot;immediate&quot;,extraDelay:&quot;0&quot;,prerenderLogicEnabled:&quot;false&quot;,adWidth:&quot;160px&quot;,adHeight:&quot;600px&quot;,maxAdWidth:&quot;&quot;,boolFeedback:&quot;true&quot;,encodedHtmlContent:&quot;true&quot;,prefetchEnabled:&quot;false&quot;,src:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=861886d1-4725-46d2-8855-cf52b935b57c&amp;src=500&amp;slot=auto-left-advertising-1&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,aaxInstrPixelUrl:&quot;&quot;,aaxImpPixelUrl:&quot;&quot;,pageType:&quot;Search&quot;,slotName:&quot;auto-left-advertising-1&quot;,subPageType:&quot;search-desktop-loom&quot;,htmlContent:&quot;&quot;,adNetwork:&quot;cs&quot;,invalidFallback:&quot;true&quot;,extras:&quot;{}&quot;};try{window.initInnerHost(a);}catch(b){SafeFrameClient.collapse();}});var scriptElement=document.createElement(&quot;script&quot;);scriptElement.src=&quot;https://d1lxz4vuik53pc.cloudfront.net/ih/1664280594355/inner-host.min.js&quot;;scriptElement.type=&quot;text/javascript&quot;;scriptElement.async=true;sendCsmMetric(&quot;af&quot;);document.body.appendChild(scriptElement);});</script>

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-use-srcdoc-fallback="true" data-auto-load="true" onload="(function(el, ts){ P.when('amzn-safe-frame-auto-loader').execute(function(fn){ fn(el, ts); }); }(this, +(new Date())));" data-frame-id="3b9d2369-41c0-4713-bfd6-93100e1036de" data-frame-attribution="100b9977e4f43a1f9559ec91432f7ae0550a8e6a" data-additional-attribution="ctiHash: 951d90adaf94afda05197eb644cbaec054f30a27;slotId:LEFT" data-metrics-scope="searchSafeFrame:LEFT" height="600" class="amzn-safe-frame aok-block" frameborder="0" scrolling="no" src="javascript:window.frameElement.getAttribute(&quot;data-srcdoc&quot;);"></iframe>
                <div class="amzn-safe-frame-footer amzn-safe-frame-footer-below"><a class="s-ad-feedback-link" href="#" aria-hidden="false" aria-label="Leave feedback on Sponsored ad">Sponsored</a></div>

    </div>

        <script> window.uet && uet('be', 'searchSafeFrame:LEFT', {wb: 1}); </script>
</div>
</div>
                  
                      
                      <div data-uuid="c57afbb9-76a1-4b2a-afcd-e6702a759f02" cel_widget_id="LEFT-SAFE_FRAME-2" class="s-widget-container s-spacing-medium s-widget-container-height-medium s-left-ads-item celwidget slot=LEFT template=SAFE_FRAME widget=loom-desktop-skyscraper_adPlacements:amazon.us.Search.Desktop.auto-left-advertising-2 pf_rd_p=e2524703-dda1-4ff9-9b61-f76b6e245c59 pf_rd_r=BNJYY9EBY54VZZF6X4X6 pd_rd_wg-MBnpm pd_rd_w-Qc97e content-id=amzn1.sym.e2524703-dda1-4ff9-9b61-f76b6e245c59:amzn1.sym.e2524703-dda1-4ff9-9b61-f76b6e245c59 pd_rd_r-12c1c0da-5406-44f9-9360-6d381729e9e2 widgetId=loom-desktop-skyscraper_adPlacements:amazon.us.Search.Desktop.auto-left-advertising-2" data-csa-c-content-id="amzn1.sym.e2524703-dda1-4ff9-9b61-f76b6e245c59:amzn1.sym.e2524703-dda1-4ff9-9b61-f76b6e245c59" data-csa-op-log-render="" data-csa-c-slot-id="LEFT" data-csa-c-type="widget" data-csa-c-id="fjxtl-is0lzd-rwth73-sypun4" data-cel-widget="LEFT-SAFE_FRAME-2">
<div class="amzn-safe-frame-container">
        <script> window.uet && uet('bb', 'searchSafeFrame:LEFT', {wb: 1}); </script>

    <div class="amzn-safe-frame-sizing" style="display: block; margin-top: 679px; width: 160px;">
        <iframe srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;57674be4-a5ae-42c2-a2cd-2de2596fa29a&quot;;</script>
    <script>
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <div id='ape_Search_auto-left-advertising-2_Desktop_wrapper' class='celwidget'  aria-hidden='true' ><div id='ape_Search_auto-left-advertising-2_Desktop_placement' ></div></div><script type=&quot;text/javascript&quot;>SafeFrameClient.on('clientReady', function() {var sendCsmMetric=function(b,d){var a=SafeFrameClient.sendMetrics;if(typeof a===&quot;function&quot;){var c=d?d+&quot;:&quot;:&quot;&quot;;a(b,&quot;adplacements:&quot;+c+&quot;search:auto-left-advertising-2:desktop&quot;);a(b,&quot;adplacements:&quot;+c+&quot;439bcdca-561d-48dd-a4e9-8f3975bf6d38&quot;);}};sendCsmMetric(&quot;bb&quot;);window[&quot;auto-left-advertising-2&quot;]={};window[&quot;auto-left-advertising-2&quot;].adStartTime=(new Date()).getTime();window.hasCaughtWaitOnEvent=false;SafeFrameClient.on(&quot;adaptiveSkyReady&quot;,function(){window.hasCaughtWaitOnEvent=true;});document.addEventListener(&quot;ihjsloaded&quot;,function(){var a={abpStatus:&quot;0&quot;,sfInnerStyle:&quot;&quot;,containerSelector:&quot;#ape_Search_auto-left-advertising-2_Desktop_placement&quot;,sfLogErrors:&quot;false&quot;,onError:SafeFrameClient.collapse,iframeSrc:&quot;https://d1lxz4vuik53pc.cloudfront.net/ii/1664280591753/inner.html&quot;,iframeId:&quot;ad-placements_inner-frame&quot;,scope:&quot;search:auto-left-advertising-2:desktop&quot;,loadAfter:&quot;immediate&quot;,extraDelay:&quot;0&quot;,prerenderLogicEnabled:&quot;false&quot;,adWidth:&quot;160px&quot;,adHeight:&quot;600px&quot;,maxAdWidth:&quot;&quot;,boolFeedback:&quot;true&quot;,encodedHtmlContent:&quot;true&quot;,prefetchEnabled:&quot;false&quot;,src:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=439bcdca-561d-48dd-a4e9-8f3975bf6d38&amp;src=500&amp;slot=auto-left-advertising-2&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,aaxInstrPixelUrl:&quot;&quot;,aaxImpPixelUrl:&quot;&quot;,pageType:&quot;Search&quot;,slotName:&quot;auto-left-advertising-2&quot;,subPageType:&quot;Desktop&quot;,htmlContent:&quot;&quot;,adNetwork:&quot;cs&quot;,enableCreativeBlocking:&quot;false&quot;,waitOnEventName:&quot;adaptiveSkyReady&quot;,invalidFallback:&quot;true&quot;,extras:&quot;{}&quot;};try{window.initInnerHost(a);}catch(b){SafeFrameClient.collapse();}});var scriptElement=document.createElement(&quot;script&quot;);scriptElement.src=&quot;https://d1lxz4vuik53pc.cloudfront.net/ih/1664280594355/inner-host.min.js&quot;;scriptElement.type=&quot;text/javascript&quot;;scriptElement.async=true;sendCsmMetric(&quot;af&quot;);document.body.appendChild(scriptElement);});</script>

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;57674be4-a5ae-42c2-a2cd-2de2596fa29a&quot;;</script>
    <script>
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <div id='ape_Search_auto-left-advertising-2_Desktop_wrapper' class='celwidget'  aria-hidden='true' ><div id='ape_Search_auto-left-advertising-2_Desktop_placement' ></div></div><script type=&quot;text/javascript&quot;>SafeFrameClient.on('clientReady', function() {var sendCsmMetric=function(b,d){var a=SafeFrameClient.sendMetrics;if(typeof a===&quot;function&quot;){var c=d?d+&quot;:&quot;:&quot;&quot;;a(b,&quot;adplacements:&quot;+c+&quot;search:auto-left-advertising-2:desktop&quot;);a(b,&quot;adplacements:&quot;+c+&quot;439bcdca-561d-48dd-a4e9-8f3975bf6d38&quot;);}};sendCsmMetric(&quot;bb&quot;);window[&quot;auto-left-advertising-2&quot;]={};window[&quot;auto-left-advertising-2&quot;].adStartTime=(new Date()).getTime();window.hasCaughtWaitOnEvent=false;SafeFrameClient.on(&quot;adaptiveSkyReady&quot;,function(){window.hasCaughtWaitOnEvent=true;});document.addEventListener(&quot;ihjsloaded&quot;,function(){var a={abpStatus:&quot;0&quot;,sfInnerStyle:&quot;&quot;,containerSelector:&quot;#ape_Search_auto-left-advertising-2_Desktop_placement&quot;,sfLogErrors:&quot;false&quot;,onError:SafeFrameClient.collapse,iframeSrc:&quot;https://d1lxz4vuik53pc.cloudfront.net/ii/1664280591753/inner.html&quot;,iframeId:&quot;ad-placements_inner-frame&quot;,scope:&quot;search:auto-left-advertising-2:desktop&quot;,loadAfter:&quot;immediate&quot;,extraDelay:&quot;0&quot;,prerenderLogicEnabled:&quot;false&quot;,adWidth:&quot;160px&quot;,adHeight:&quot;600px&quot;,maxAdWidth:&quot;&quot;,boolFeedback:&quot;true&quot;,encodedHtmlContent:&quot;true&quot;,prefetchEnabled:&quot;false&quot;,src:&quot;https://aax-us-east-retail-direct.amazon.com/e/xsp/getAd?placementId=439bcdca-561d-48dd-a4e9-8f3975bf6d38&amp;src=500&amp;slot=auto-left-advertising-2&amp;rid=01016f1d8f6a2d3a1d3060ccff845b04f43bf6f6273a28f480a0c027e83995dd4102&amp;rj=%7B%7D&quot;,aaxInstrPixelUrl:&quot;&quot;,aaxImpPixelUrl:&quot;&quot;,pageType:&quot;Search&quot;,slotName:&quot;auto-left-advertising-2&quot;,subPageType:&quot;Desktop&quot;,htmlContent:&quot;&quot;,adNetwork:&quot;cs&quot;,enableCreativeBlocking:&quot;false&quot;,waitOnEventName:&quot;adaptiveSkyReady&quot;,invalidFallback:&quot;true&quot;,extras:&quot;{}&quot;};try{window.initInnerHost(a);}catch(b){SafeFrameClient.collapse();}});var scriptElement=document.createElement(&quot;script&quot;);scriptElement.src=&quot;https://d1lxz4vuik53pc.cloudfront.net/ih/1664280594355/inner-host.min.js&quot;;scriptElement.type=&quot;text/javascript&quot;;scriptElement.async=true;sendCsmMetric(&quot;af&quot;);document.body.appendChild(scriptElement);});</script>

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-use-srcdoc-fallback="true" data-auto-load="true" onload="(function(el, ts){ P.when('amzn-safe-frame-auto-loader').execute(function(fn){ fn(el, ts); }); }(this, +(new Date())));" data-frame-id="57674be4-a5ae-42c2-a2cd-2de2596fa29a" data-frame-attribution="984feefd0a6b1749cf28009cb1ae5f8ee57b52a7" data-additional-attribution="ctiHash: 951d90adaf94afda05197eb644cbaec054f30a27;slotId:LEFT" data-metrics-scope="searchSafeFrame:LEFT" height="600" class="amzn-safe-frame aok-block" frameborder="0" scrolling="no" src="javascript:window.frameElement.getAttribute(&quot;data-srcdoc&quot;);"></iframe>
                <div class="amzn-safe-frame-footer amzn-safe-frame-footer-below"><a class="s-ad-feedback-link" href="#" aria-hidden="false" aria-label="Leave feedback on Sponsored ad">Sponsored</a></div>

    </div>

        <script> window.uet && uet('be', 'searchSafeFrame:LEFT', {wb: 1}); </script>
</div>
</div>
                  
              </span>
          </div>
      </div></div>
</div>


<script>P.declare('sp.load.js', null);</script>

<script>P.declare('s\-aapi\-ajax\-config', {"marketplaceId":"ATVPDKIKX0DER","marketplaceLocale":"en\-US","ajaxEndpoint":"https:\/\/data.amazon.com"});</script>

<script type="a-state" data-a-state="{&quot;key&quot;:&quot;s-url-parameters&quot;}">{"hidden-keywords":"(field-)?hidden-keywords?","lo":"lo|layout","fst":"fst","dm":"dm","pid":"pid","language":"language","fs":"fs","qid":"qid","p_postal_code":"p_postal_code","ds":"ds","suggest_lop_undo":"suggest_undo","wi":"wi","ref":"ref_?","fkey":"fkey","me":"me|merchant","ie":"ie","low-price":"low-price","fskey":"fskey","onc":"onc","subresource":"subresource","af":"af","widgetId":"widgetId","suggest_lop_disabled":"suggest_lop_disabled","i":"i|search-alias|index","k":"k|(field-)?keywords?","adec":"adec","high-price":"high-price","url":"url","n":"n|node","bbn":"bbn","s":"s|sort","srs":"srs","rh":"rh","page":"p|page","dc":"dc"}</script>





<script type="a-state" data-a-state="{&quot;key&quot;:&quot;rush-dispatch&quot;}">{"client-side-metrics-info":{"requestId":"BNJYY9EBY54VZZF6X4X6"}}</script>







<div class="a-popover-preload" id="a-popover-s-safe-modal-singleton">
    <div data-component-type="s-safe-modal" data-component-props="{&quot;contentUnavailableText&quot;:&quot;Sorry, this content is not available.&quot;,&quot;frameId&quot;:&quot;d5514bb4-eeca-4bec-b32e-f847f3624acf&quot;,&quot;html&quot;:&quot;<!--SINGLETON CONTENT-->&quot;,&quot;popoverName&quot;:&quot;s-safe-modal-singleton&quot;}" class="rush-component" data-component-id="74">
        <div class="a-section a-text-center s-safe-modal-spinner aok-hidden">
            <span class="a-spinner a-spinner-medium"></span>
        </div>
        <div class="s-safe-modal-content">
            
<div class="amzn-safe-frame-container">
        <script> window.uet && uet('bb', 'searchSafeFrame:modal:s-safe-modal-singleton', {wb: 1}); </script>

    <div class="amzn-safe-frame-sizing" style="width: 500px;">
        <iframe srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;d5514bb4-eeca-4bec-b32e-f847f3624acf&quot;;</script>
    <link rel=&quot;stylesheet&quot; href=&quot;https://images-na.ssl-images-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,410yLeQZHKL.css,31OSFXVtM5L.css,013z33uKh2L.css,017DsKjNQJL.css,0131vqwP5UL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11fJbvhE5HL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21P6CS3L9LL.css,01oDR3IULNL.css,41Axm2+z87L.css,01XPHJk60-L.css,01S0vRENeAL.css,21IbH+SoKSL.css,11MrAKjcAKL.css,21fecG8pUzL.css,11a5wZbuKrL.css,01CFUgsA-YL.css,31pHA2U5D9L.css,11qour3ND0L.css,116t+WD27UL.css,11gKCCKQV+L.css,11061HxnEvL.css,11oHt2HYxnL.css,01j2JE3j7aL.css,11JQtnL-6eL.css,21KA2rMsZML.css,11jtXRmppwL.css,0114z6bAEoL.css,21uwtfqr5aL.css,11QyqG8yiqL.css,11K24eOJg4L.css,11F2+OBzLyL.css,01890+Vwk8L.css,01g+cOYAZgL.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&amp;VGEEt8I0#us.not-trident.388250-T1.432724-T1.577951-T1.577971-T1.577969-T1.632675-T1.577970-T1&quot; />
<script>
(function(d,g,S,G){function w(a){x&amp;&amp;x.tag&amp;&amp;x.tag(k(&quot;:&quot;,&quot;aui&quot;,a))}function m(a,b){x&amp;&amp;x.count&amp;&amp;x.count(&quot;aui:&quot;+a,0===b?0:b||(x.count(&quot;aui:&quot;+a)||0)+1)}function q(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function r(a){return&quot;function&quot;===typeof a}function z(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)}function k(a,b,c,d){b=b&amp;&amp;c?b+a+c:b||c;return d?k(a,b,d):b}function H(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(u){a[b]=
c}return c}function va(a,b,c){var d=c=a.length,f=function(){d--||(T.push(b),U||(setTimeout(fa,0),U=!0))};for(f();c--;)ha[a[c]]?f():(C[a[c]]=C[a[c]]||[]).push(f)}function wa(a,b,c,d,f){var e=g.createElement(a?&quot;script&quot;:&quot;link&quot;);z(e,&quot;error&quot;,d);f&amp;&amp;z(e,&quot;load&quot;,f);a?(e.type=&quot;text/javascript&quot;,e.async=!0,c&amp;&amp;/AUIClients|images[/]I/.test(b)&amp;&amp;e.setAttribute(&quot;crossorigin&quot;,&quot;anonymous&quot;),e.src=b):(e.rel=&quot;stylesheet&quot;,e.href=b);g.getElementsByTagName(&quot;head&quot;)[0].appendChild(e)}function ia(a,b){return function(c,u){function f(){wa(b,
c,e,function(b){V?m(&quot;resource_unload&quot;):e?(e=!1,m(&quot;resource_retry&quot;),f()):(m(&quot;resource_error&quot;),a.log(&quot;Asset failed to load: &quot;+c));b&amp;&amp;b.stopPropagation?b.stopPropagation():d.event&amp;&amp;(d.event.cancelBubble=!0)},u)}if(ja[c])return!1;ja[c]=!0;m(&quot;resource_count&quot;);var e=!0;return!f()}}function xa(a,b,c){for(var d={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,e,n){b.logError(c,e,n,a)}},f=[],e=0;e<c.length;e++)I.hasOwnProperty(c[e])&amp;&amp;(f[e]=
W.hasOwnProperty(c[e])?W[c[e]](I[c[e]],d):I[c[e]]);return f}function D(a,b,c,u,f){return function(e,g){function m(){var a=null;u?a=g:r(g)&amp;&amp;(X.start=A(),a=g.apply(d,xa(e,n,B)),X.end=A());if(b){I[e]=a;a=e;for(ha[a]=!0;(C[a]||[]).length;)C[a].shift()();delete C[a]}X.done=!0}var n=f||this;r(e)&amp;&amp;(g=e,e=G);b&amp;&amp;(e=e?e.replace(ka,&quot;&quot;):&quot;__NONAME__&quot;,Y.hasOwnProperty(e)&amp;&amp;n.error(k(&quot;, reregistered by &quot;,k(&quot; by &quot;,e+&quot; already registered&quot;,Y[e]),n.attribution),e),Y[e]=n.attribution);for(var B=[],J=0;J<a.length;J++)B[J]=
a[J].replace(ka,&quot;&quot;);var X=E[e||&quot;anon&quot;+ ++ya]={depend:B,registered:A(),namespace:n.namespace};e&amp;&amp;za.hasOwnProperty(e);c?m():va(B,n.guardFatal(e,m),e);return{decorate:function(a){W[e]=n.guardFatal(e,a)}}}}function la(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:D(b,!1,a,!1,this),register:D(b,!0,a,!1,this)}}}function Z(a,b){return function(c,d){d||(d=c,c=G);var f=this.attribution;return function(){y.push(b||{attribution:f,name:c,logLevel:a});var e=d.apply(this,arguments);
y.pop();return e}}}function K(a,b){this.load={js:ia(this,!0),css:ia(this)};H(this,&quot;namespace&quot;,b);H(this,&quot;attribution&quot;,a)}function ma(){g.body?t.trigger(&quot;a-bodyBegin&quot;):setTimeout(ma,20)}function F(a,b){a.className=aa(a,b)+&quot; &quot;+b}function aa(a,b){return(&quot; &quot;+a.className+&quot; &quot;).split(&quot; &quot;+b+&quot; &quot;).join(&quot; &quot;).replace(/^ | $/g,&quot;&quot;)}function na(a){try{return a()}catch(b){return!1}}function L(){if(M){var a={w:d.innerWidth||h.clientWidth,h:d.innerHeight||h.clientHeight};5<Math.abs(a.w-ba.w)||50<a.h-ba.h?(ba=a,N=4,
(a=l.mobile||l.tablet?450<a.w&amp;&amp;a.w>a.h:1250<=a.w)?F(h,&quot;a-ws&quot;):h.className=aa(h,&quot;a-ws&quot;)):0<N&amp;&amp;(N--,oa=setTimeout(L,16))}}function Aa(a){(M=a===G?!M:!!a)&amp;&amp;L()}function Ba(){return M}&quot;use strict&quot;;var O=S.now=S.now||function(){return+new S},A=function(a){return a&amp;&amp;a.now?a.now.bind(a):O}(d.performance),P=A(),za={},v=d.AmazonUIPageJS||d.P;if(v&amp;&amp;v.when&amp;&amp;v.register){P=[];for(var p=g.currentScript;p;p=p.parentElement)p.id&amp;&amp;P.push(p.id);return v.log(&quot;A copy of P has already been loaded on this page.&quot;,&quot;FATAL&quot;,
P.join(&quot; &quot;))}var x=d.ue;w();w(&quot;aui_build_date:3.23.1-2023-04-21&quot;);var T=[],Ca=[],U=!1;var fa=function(){for(var a=setTimeout(fa,0),b=O();Ca.length||T.length;)if(T.shift()(),50<O()-b)return;clearTimeout(a);U=!1};var ha={},C={},ja={},V=!1;z(d,&quot;beforeunload&quot;,function(){V=!0;setTimeout(function(){V=!1},1E4)});var ka=/^prv:/,Y={},I={},W={},E={},ya=0,ca=String.fromCharCode(92),y=[],pa=!0,qa=d.onerror;d.onerror=function(a,b,c,u,f){f&amp;&amp;&quot;object&quot;===typeof f||(f=Error(a,b,c),f.columnNumber=u,f.stack=b||c||u?
k(ca,f.message,&quot;at &quot;+k(&quot;:&quot;,b,c,u)):G);var e=y.pop()||{};f.attribution=k(&quot;:&quot;,f.attribution||e.attribution,e.name);f.logLevel=e.logLevel;f.attribution&amp;&amp;console&amp;&amp;console.log&amp;&amp;console.log([f.logLevel||&quot;ERROR&quot;,a,&quot;thrown by&quot;,f.attribution].join(&quot; &quot;));y=[];qa&amp;&amp;(e=[].slice.call(arguments),e[4]=f,qa.apply(d,e))};K.prototype={logError:function(a,b,c,u){b={message:b,logLevel:c||&quot;ERROR&quot;,attribution:k(&quot;:&quot;,this.attribution,u)};if(d.ueLogError)return d.ueLogError(a||b,a?b:null),!0;console&amp;&amp;console.error&amp;&amp;(console.log(b),
console.error(a));return!1},error:function(a,b,c,d){a=Error(k(&quot;:&quot;,d,a,c));a.attribution=k(&quot;:&quot;,this.attribution,b);throw a;},guardError:Z(),guardFatal:Z(&quot;FATAL&quot;),guardCurrent:function(a){var b=y[y.length-1];return b?Z(b.logLevel,b).call(this,a):a},guardTime:function(a){var b=y[y.length-1],c=b&amp;&amp;b.name;return c&amp;&amp;c in E?function(){var b=A(),d=a.apply(this,arguments);E[c].async=(E[c].async||0)+A()-b;return d}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:D([],!0,!0,!0),register:D([],
!0),execute:D([]),AUI_BUILD_DATE:&quot;3.23.1-2023-04-21&quot;,when:la(),now:la(!0),trigger:function(a,b,c){var g=O();this.declare(a,{data:b,pageElapsedTime:g-(d.aPageStart||NaN),triggerTime:g});c&amp;&amp;c.instrument&amp;&amp;Q.when(&quot;prv:a-logTrigger&quot;).execute(function(b){b(a)})},handleTriggers:function(){this.log(&quot;handleTriggers deprecated&quot;)},attributeErrors:function(a){return new K(a)},_namespace:function(a,b){return new K(a,b)},setPriority:function(a){pa?pa=!1:this.log(&quot;setPriority only accept the first call.&quot;)}};var t=
H(d,&quot;AmazonUIPageJS&quot;,new K);var Q=t._namespace(&quot;PageJS&quot;,&quot;AmazonUI&quot;);Q.declare(&quot;prv:p-debug&quot;,E);t.declare(&quot;p-recorder-events&quot;,[]);t.declare(&quot;p-recorder-stop&quot;,function(){});H(d,&quot;P&quot;,t);ma();if(g.addEventListener){var ra;g.addEventListener(&quot;DOMContentLoaded&quot;,ra=function(){t.trigger(&quot;a-domready&quot;);g.removeEventListener(&quot;DOMContentLoaded&quot;,ra,!1)},!1)}var h=g.documentElement,da=function(){var a=[&quot;O&quot;,&quot;ms&quot;,&quot;Moz&quot;,&quot;Webkit&quot;],b=g.createElement(&quot;div&quot;);return{testGradients:function(){return!0},test:function(c){var d=
c.charAt(0).toUpperCase()+c.substr(1);c=(a.join(d+&quot; &quot;)+d+&quot; &quot;+c).split(&quot; &quot;);for(d=c.length;d--;)if(&quot;&quot;===b.style[c[d]])return!0;return!1},testTransform3d:function(){return!0}}}();v=h.className;var sa=/(^| )a-mobile( |$)/.test(v),ta=/(^| )a-tablet( |$)/.test(v),l={audio:function(){return!!g.createElement(&quot;audio&quot;).canPlayType},video:function(){return!!g.createElement(&quot;video&quot;).canPlayType},canvas:function(){return!!g.createElement(&quot;canvas&quot;).getContext},svg:function(){return!!g.createElementNS&amp;&amp;!!g.createElementNS(&quot;http://www.w3.org/2000/svg&quot;,
&quot;svg&quot;).createSVGRect},offline:function(){return navigator.hasOwnProperty&amp;&amp;navigator.hasOwnProperty(&quot;onLine&quot;)&amp;&amp;navigator.onLine},dragDrop:function(){return&quot;draggable&quot;in g.createElement(&quot;span&quot;)},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!d.history||!d.history.pushState)},webworker:function(){return!!d.Worker},autofocus:function(){return&quot;autofocus&quot;in g.createElement(&quot;input&quot;)},inputPlaceholder:function(){return&quot;placeholder&quot;in g.createElement(&quot;input&quot;)},textareaPlaceholder:function(){return&quot;placeholder&quot;in
g.createElement(&quot;textarea&quot;)},localStorage:function(){return&quot;localStorage&quot;in d&amp;&amp;null!==d.localStorage},orientation:function(){return&quot;orientation&quot;in d},touch:function(){return&quot;ontouchend&quot;in g},gradients:function(){return da.testGradients()},hires:function(){var a=d.devicePixelRatio&amp;&amp;1.5<=d.devicePixelRatio||d.matchMedia&amp;&amp;d.matchMedia(&quot;(min-resolution:144dpi)&quot;).matches;m(&quot;hiRes&quot;+(sa?&quot;Mobile&quot;:ta?&quot;Tablet&quot;:&quot;Desktop&quot;),a?1:0);return a},transform3d:function(){return da.testTransform3d()},touchScrolling:function(){return q(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|SOFTWARE=([5-9]|[1-9][0-9]+)(.[0-9]{1,2})+.*DEVICE=iPhone|Chrome|Silk|Firefox|Trident.+?; Touch/i)},
ios:function(){return q(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&amp;&amp;!q(/trident|Edge/i)},android:function(){return q(/android.([1-9]|[L-Z])/i)&amp;&amp;!q(/trident|Edge/i)},mobile:function(){return sa},tablet:function(){return ta},rtl:function(){return&quot;rtl&quot;===h.dir}};for(p in l)l.hasOwnProperty(p)&amp;&amp;(l[p]=na(l[p]));for(var ea=&quot;textShadow textStroke boxShadow borderRadius borderImage opacity transform transition&quot;.split(&quot; &quot;),R=0;R<ea.length;R++)l[ea[R]]=na(function(){return da.test(ea[R])});var M=!0,oa=0,ba=
{w:0,h:0},N=4;L();z(d,&quot;resize&quot;,function(){clearTimeout(oa);N=4;L()});var ua={getItem:function(a){try{return d.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return d.localStorage.setItem(a,b)}catch(c){}}};h.className=aa(h,&quot;a-no-js&quot;);F(h,&quot;a-js&quot;);!q(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||d.navigator.standalone||q(/safari/i)||F(h,&quot;a-ember&quot;);v=[];for(p in l)l.hasOwnProperty(p)&amp;&amp;l[p]&amp;&amp;v.push(&quot;a-&quot;+p.replace(/([A-Z])/g,function(a){return&quot;-&quot;+a.toLowerCase()}));F(h,v.join(&quot; &quot;));h.setAttribute(&quot;data-aui-build-date&quot;,
&quot;3.23.1-2023-04-21&quot;);t.register(&quot;p-detect&quot;,function(){return{capabilities:l,localStorage:l.localStorage&amp;&amp;ua,toggleResponsiveGrid:Aa,responsiveGridEnabled:Ba}});q(/UCBrowser/i)||l.localStorage&amp;&amp;F(h,ua.getItem(&quot;a-font-class&quot;));t.declare(&quot;a-event-revised-handling&quot;,!1);t.execute(&quot;RetailPageServiceWorker&quot;,function(){function a(a,b){f.controller&amp;&amp;a?(a={feature:&quot;retail_service_worker_messaging&quot;,command:a},b&amp;&amp;(a.data=b),f.controller.postMessage(a)):a&amp;&amp;m(&quot;sw:sw_message_no_ctrl&quot;,1)}function b(a){var b=a.data;
if(b&amp;&amp;&quot;retail_service_worker_messaging&quot;===b.feature&amp;&amp;b.command&amp;&amp;b.data){var c=b.data;a=d.ue;var e=d.ueLogError;switch(b.command){case &quot;log_counter&quot;:a&amp;&amp;r(a.count)&amp;&amp;c.name&amp;&amp;a.count(c.name,0===c.value?0:c.value||1);break;case &quot;log_tag&quot;:a&amp;&amp;r(a.tag)&amp;&amp;c.tag&amp;&amp;(a.tag(c.tag),b=d.uex,a.isl&amp;&amp;r(b)&amp;&amp;b(&quot;at&quot;));break;case &quot;log_error&quot;:e&amp;&amp;r(e)&amp;&amp;c.message&amp;&amp;e({message:c.message,logLevel:c.level||&quot;ERROR&quot;,attribution:c.attribution||&quot;RetailServiceWorker&quot;});break;case &quot;log_weblab_trigger&quot;:if(!c.weblab||!c.treatment)break;
a&amp;&amp;r(a.trigger)?a.trigger(c.weblab,c.treatment):(m(&quot;sw:wt:miss&quot;),m(&quot;sw:wt:miss:&quot;+c.weblab+&quot;:&quot;+c.treatment));break;default:m(&quot;sw:unsupported_message_command&quot;,1)}}}function c(){e.forEach(function(a){w(a)})}function h(a,b,c){if(b){a=q(/Chrome/i)&amp;&amp;!q(/Edge/i)&amp;&amp;!q(/OPR/i)&amp;&amp;!a.capabilities.isAmazonApp&amp;&amp;!q(new RegExp(ca+&quot;bwv&quot;+ca+&quot;b&quot;));var d=&quot;sw:browser:&quot;+c+&quot;:&quot;;b.browser&amp;&amp;a&amp;&amp;(e.push(d+&quot;supported&quot;),b.browser.action(d,c));!a&amp;&amp;b.browser&amp;&amp;e.push(d+&quot;unsupported&quot;)}}try{var f=navigator.serviceWorker}catch(n){w(&quot;sw:nav_err&quot;)}(function(){if(f){var c=
function(){a(&quot;page_loaded&quot;,{rid:d.ue_id,mid:d.ue_mid,pty:d.ue_pty,sid:d.ue_sid,spty:d.ue_spty,furl:d.ue_furl})};z(f,&quot;message&quot;,b);a(&quot;client_messaging_ready&quot;);t.when(&quot;load&quot;).execute(c);z(f,&quot;controllerchange&quot;,function(){a(&quot;client_messaging_ready&quot;);&quot;complete&quot;===g.readyState&amp;&amp;c()})}})();var e=[],l=function(a,b){var c=d.uex,e=d.uet;a=k(&quot;:&quot;,&quot;aui&quot;,&quot;sw&quot;,a);&quot;ld&quot;===b&amp;&amp;r(c)?c(&quot;ld&quot;,a,{wb:1}):r(e)&amp;&amp;e(b,a,{wb:1})},p=function(a,b,c){function e(a){b&amp;&amp;r(b.failure)&amp;&amp;b.failure(a)}function g(){p=setTimeout(function(){w(k(&quot;:&quot;,
&quot;sw:&quot;+n,h.TIMED_OUT));e({ok:!1,statusCode:h.TIMED_OUT,done:!1});l(n,&quot;ld&quot;)},c||4E3)}var h={NO_CONTROLLER:&quot;no_ctrl&quot;,TIMED_OUT:&quot;timed_out&quot;,UNSUPPORTED_BROWSER:&quot;unsupported_browser&quot;,UNEXPECTED_RESPONSE:&quot;unexpected_response&quot;},n=k(&quot;:&quot;,a.feature,a.command),p,q=!0;if(&quot;MessageChannel&quot;in d&amp;&amp;f&amp;&amp;&quot;controller&quot;in f)if(f.controller){var B=new MessageChannel;B.port1.onmessage=function(c){(c=c.data)&amp;&amp;c.feature===a.feature&amp;&amp;c.command===a.command?(q&amp;&amp;(l(n,&quot;cf&quot;),q=!1),l(n,&quot;af&quot;),clearTimeout(p),c.done||g(),c.ok?b&amp;&amp;r(b.success)&amp;&amp;
b.success(c):e(c),c.done&amp;&amp;l(n,&quot;ld&quot;)):m(k(&quot;:&quot;,&quot;sw:&quot;+n,h.UNEXPECTED_RESPONSE),1)};g();l(n,&quot;bb&quot;);f.controller.postMessage(a,[B.port2])}else w(k(&quot;:&quot;,&quot;sw:&quot;+a.feature,h.NO_CONTROLLER)),e({ok:!1,statusCode:h.NO_CONTROLLER,done:!0});else w(k(&quot;:&quot;,&quot;sw:&quot;+a.feature,h.UNSUPPORTED_BROWSER)),e({ok:!1,statusCode:h.UNSUPPORTED_BROWSER,done:!0})};(function(){f?(l(&quot;ctrl_changed&quot;,&quot;bb&quot;),f.addEventListener(&quot;controllerchange&quot;,function(){w(&quot;sw:ctrl_changed&quot;);l(&quot;ctrl_changed&quot;,&quot;ld&quot;)})):m(k(&quot;:&quot;,&quot;sw:ctrl_changed&quot;,&quot;sw_unsupp&quot;),
1)})();(function(){var a=function(){l(b,&quot;ld&quot;);var a=d.uex;p({feature:&quot;page_proxy&quot;,command:&quot;request_feature_tags&quot;},{success:function(b){b=b.data;Array.isArray(b)&amp;&amp;b.forEach(function(a){&quot;string&quot;===typeof a?w(k(&quot;:&quot;,&quot;sw:ppft&quot;,a)):m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;invalid_tag&quot;),1)});m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;success&quot;),1);x&amp;&amp;x.isl&amp;&amp;r(a)&amp;&amp;a(&quot;at&quot;)},failure:function(a){m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;error:&quot;+(a.statusCode||&quot;ppft_error&quot;)),1)}})};if(&quot;requestIdleCallback&quot;in d){var b=k(&quot;:&quot;,&quot;ppft&quot;,&quot;callback_ricb&quot;);d.requestIdleCallback(a,{timeout:1E3})}else b=
k(&quot;:&quot;,&quot;ppft&quot;,&quot;callback_timeout&quot;),setTimeout(a,0);l(b,&quot;bb&quot;)})();(function(a){var b=a.reg,g=a.unreg;f&amp;&amp;f.getRegistrations?(Q.when(&quot;A&quot;).execute(function(a){h(a,g,&quot;unregister&quot;)}),z(d,&quot;load&quot;,function(){Q.when(&quot;A&quot;).execute(function(a){h(a,b,&quot;register&quot;);c()})})):(b&amp;&amp;b.browser&amp;&amp;e.push(&quot;sw:browser:register:unsupported&quot;),g&amp;&amp;g.browser&amp;&amp;e.push(&quot;sw:browser:unregister:unsupported&quot;),c())})({reg:{},unreg:{}})});t.declare(&quot;a-fix-event-off&quot;,!1);m(&quot;pagejs:pkgExecTime&quot;,A()-P)})(window,document,Date);
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61yXDIPmT-L._RC|11Y+5x+kkTL.js,51Am7NcREVL.js,11yKORv-GTL.js,11GgN1+C7hL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,516j7qaWchL.js,11kWu3cNjYL.js,11wr1I7-WYL.js,11OREnu1epL.js,11Wm6BwZ+6L.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31nfKXylf6L.js,01ezj5Rkz1L.js,11bEz2VIYrL.js,31o2NGTXThL.js,01rpauTep4L.js,015tKjxsR2L.js_.js?AUIClients/AmazonUI&amp;MFdCk5El#567364-T1.432724-T1.577970-T1');
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <!--SINGLETON CONTENT-->

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-srcdoc="<!DOCTYPE html>
<html
        lang=&quot;en-us&quot;
>
<head>
    <meta charset=&quot;UTF-8&quot;>
        <script>window.safeFrameId = &quot;d5514bb4-eeca-4bec-b32e-f847f3624acf&quot;;</script>
    <link rel=&quot;stylesheet&quot; href=&quot;https://images-na.ssl-images-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,410yLeQZHKL.css,31OSFXVtM5L.css,013z33uKh2L.css,017DsKjNQJL.css,0131vqwP5UL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11fJbvhE5HL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21P6CS3L9LL.css,01oDR3IULNL.css,41Axm2+z87L.css,01XPHJk60-L.css,01S0vRENeAL.css,21IbH+SoKSL.css,11MrAKjcAKL.css,21fecG8pUzL.css,11a5wZbuKrL.css,01CFUgsA-YL.css,31pHA2U5D9L.css,11qour3ND0L.css,116t+WD27UL.css,11gKCCKQV+L.css,11061HxnEvL.css,11oHt2HYxnL.css,01j2JE3j7aL.css,11JQtnL-6eL.css,21KA2rMsZML.css,11jtXRmppwL.css,0114z6bAEoL.css,21uwtfqr5aL.css,11QyqG8yiqL.css,11K24eOJg4L.css,11F2+OBzLyL.css,01890+Vwk8L.css,01g+cOYAZgL.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&amp;VGEEt8I0#us.not-trident.388250-T1.432724-T1.577951-T1.577971-T1.577969-T1.632675-T1.577970-T1&quot; />
<script>
(function(d,g,S,G){function w(a){x&amp;&amp;x.tag&amp;&amp;x.tag(k(&quot;:&quot;,&quot;aui&quot;,a))}function m(a,b){x&amp;&amp;x.count&amp;&amp;x.count(&quot;aui:&quot;+a,0===b?0:b||(x.count(&quot;aui:&quot;+a)||0)+1)}function q(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function r(a){return&quot;function&quot;===typeof a}function z(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)}function k(a,b,c,d){b=b&amp;&amp;c?b+a+c:b||c;return d?k(a,b,d):b}function H(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(u){a[b]=
c}return c}function va(a,b,c){var d=c=a.length,f=function(){d--||(T.push(b),U||(setTimeout(fa,0),U=!0))};for(f();c--;)ha[a[c]]?f():(C[a[c]]=C[a[c]]||[]).push(f)}function wa(a,b,c,d,f){var e=g.createElement(a?&quot;script&quot;:&quot;link&quot;);z(e,&quot;error&quot;,d);f&amp;&amp;z(e,&quot;load&quot;,f);a?(e.type=&quot;text/javascript&quot;,e.async=!0,c&amp;&amp;/AUIClients|images[/]I/.test(b)&amp;&amp;e.setAttribute(&quot;crossorigin&quot;,&quot;anonymous&quot;),e.src=b):(e.rel=&quot;stylesheet&quot;,e.href=b);g.getElementsByTagName(&quot;head&quot;)[0].appendChild(e)}function ia(a,b){return function(c,u){function f(){wa(b,
c,e,function(b){V?m(&quot;resource_unload&quot;):e?(e=!1,m(&quot;resource_retry&quot;),f()):(m(&quot;resource_error&quot;),a.log(&quot;Asset failed to load: &quot;+c));b&amp;&amp;b.stopPropagation?b.stopPropagation():d.event&amp;&amp;(d.event.cancelBubble=!0)},u)}if(ja[c])return!1;ja[c]=!0;m(&quot;resource_count&quot;);var e=!0;return!f()}}function xa(a,b,c){for(var d={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,e,n){b.logError(c,e,n,a)}},f=[],e=0;e<c.length;e++)I.hasOwnProperty(c[e])&amp;&amp;(f[e]=
W.hasOwnProperty(c[e])?W[c[e]](I[c[e]],d):I[c[e]]);return f}function D(a,b,c,u,f){return function(e,g){function m(){var a=null;u?a=g:r(g)&amp;&amp;(X.start=A(),a=g.apply(d,xa(e,n,B)),X.end=A());if(b){I[e]=a;a=e;for(ha[a]=!0;(C[a]||[]).length;)C[a].shift()();delete C[a]}X.done=!0}var n=f||this;r(e)&amp;&amp;(g=e,e=G);b&amp;&amp;(e=e?e.replace(ka,&quot;&quot;):&quot;__NONAME__&quot;,Y.hasOwnProperty(e)&amp;&amp;n.error(k(&quot;, reregistered by &quot;,k(&quot; by &quot;,e+&quot; already registered&quot;,Y[e]),n.attribution),e),Y[e]=n.attribution);for(var B=[],J=0;J<a.length;J++)B[J]=
a[J].replace(ka,&quot;&quot;);var X=E[e||&quot;anon&quot;+ ++ya]={depend:B,registered:A(),namespace:n.namespace};e&amp;&amp;za.hasOwnProperty(e);c?m():va(B,n.guardFatal(e,m),e);return{decorate:function(a){W[e]=n.guardFatal(e,a)}}}}function la(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:D(b,!1,a,!1,this),register:D(b,!0,a,!1,this)}}}function Z(a,b){return function(c,d){d||(d=c,c=G);var f=this.attribution;return function(){y.push(b||{attribution:f,name:c,logLevel:a});var e=d.apply(this,arguments);
y.pop();return e}}}function K(a,b){this.load={js:ia(this,!0),css:ia(this)};H(this,&quot;namespace&quot;,b);H(this,&quot;attribution&quot;,a)}function ma(){g.body?t.trigger(&quot;a-bodyBegin&quot;):setTimeout(ma,20)}function F(a,b){a.className=aa(a,b)+&quot; &quot;+b}function aa(a,b){return(&quot; &quot;+a.className+&quot; &quot;).split(&quot; &quot;+b+&quot; &quot;).join(&quot; &quot;).replace(/^ | $/g,&quot;&quot;)}function na(a){try{return a()}catch(b){return!1}}function L(){if(M){var a={w:d.innerWidth||h.clientWidth,h:d.innerHeight||h.clientHeight};5<Math.abs(a.w-ba.w)||50<a.h-ba.h?(ba=a,N=4,
(a=l.mobile||l.tablet?450<a.w&amp;&amp;a.w>a.h:1250<=a.w)?F(h,&quot;a-ws&quot;):h.className=aa(h,&quot;a-ws&quot;)):0<N&amp;&amp;(N--,oa=setTimeout(L,16))}}function Aa(a){(M=a===G?!M:!!a)&amp;&amp;L()}function Ba(){return M}&quot;use strict&quot;;var O=S.now=S.now||function(){return+new S},A=function(a){return a&amp;&amp;a.now?a.now.bind(a):O}(d.performance),P=A(),za={},v=d.AmazonUIPageJS||d.P;if(v&amp;&amp;v.when&amp;&amp;v.register){P=[];for(var p=g.currentScript;p;p=p.parentElement)p.id&amp;&amp;P.push(p.id);return v.log(&quot;A copy of P has already been loaded on this page.&quot;,&quot;FATAL&quot;,
P.join(&quot; &quot;))}var x=d.ue;w();w(&quot;aui_build_date:3.23.1-2023-04-21&quot;);var T=[],Ca=[],U=!1;var fa=function(){for(var a=setTimeout(fa,0),b=O();Ca.length||T.length;)if(T.shift()(),50<O()-b)return;clearTimeout(a);U=!1};var ha={},C={},ja={},V=!1;z(d,&quot;beforeunload&quot;,function(){V=!0;setTimeout(function(){V=!1},1E4)});var ka=/^prv:/,Y={},I={},W={},E={},ya=0,ca=String.fromCharCode(92),y=[],pa=!0,qa=d.onerror;d.onerror=function(a,b,c,u,f){f&amp;&amp;&quot;object&quot;===typeof f||(f=Error(a,b,c),f.columnNumber=u,f.stack=b||c||u?
k(ca,f.message,&quot;at &quot;+k(&quot;:&quot;,b,c,u)):G);var e=y.pop()||{};f.attribution=k(&quot;:&quot;,f.attribution||e.attribution,e.name);f.logLevel=e.logLevel;f.attribution&amp;&amp;console&amp;&amp;console.log&amp;&amp;console.log([f.logLevel||&quot;ERROR&quot;,a,&quot;thrown by&quot;,f.attribution].join(&quot; &quot;));y=[];qa&amp;&amp;(e=[].slice.call(arguments),e[4]=f,qa.apply(d,e))};K.prototype={logError:function(a,b,c,u){b={message:b,logLevel:c||&quot;ERROR&quot;,attribution:k(&quot;:&quot;,this.attribution,u)};if(d.ueLogError)return d.ueLogError(a||b,a?b:null),!0;console&amp;&amp;console.error&amp;&amp;(console.log(b),
console.error(a));return!1},error:function(a,b,c,d){a=Error(k(&quot;:&quot;,d,a,c));a.attribution=k(&quot;:&quot;,this.attribution,b);throw a;},guardError:Z(),guardFatal:Z(&quot;FATAL&quot;),guardCurrent:function(a){var b=y[y.length-1];return b?Z(b.logLevel,b).call(this,a):a},guardTime:function(a){var b=y[y.length-1],c=b&amp;&amp;b.name;return c&amp;&amp;c in E?function(){var b=A(),d=a.apply(this,arguments);E[c].async=(E[c].async||0)+A()-b;return d}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:D([],!0,!0,!0),register:D([],
!0),execute:D([]),AUI_BUILD_DATE:&quot;3.23.1-2023-04-21&quot;,when:la(),now:la(!0),trigger:function(a,b,c){var g=O();this.declare(a,{data:b,pageElapsedTime:g-(d.aPageStart||NaN),triggerTime:g});c&amp;&amp;c.instrument&amp;&amp;Q.when(&quot;prv:a-logTrigger&quot;).execute(function(b){b(a)})},handleTriggers:function(){this.log(&quot;handleTriggers deprecated&quot;)},attributeErrors:function(a){return new K(a)},_namespace:function(a,b){return new K(a,b)},setPriority:function(a){pa?pa=!1:this.log(&quot;setPriority only accept the first call.&quot;)}};var t=
H(d,&quot;AmazonUIPageJS&quot;,new K);var Q=t._namespace(&quot;PageJS&quot;,&quot;AmazonUI&quot;);Q.declare(&quot;prv:p-debug&quot;,E);t.declare(&quot;p-recorder-events&quot;,[]);t.declare(&quot;p-recorder-stop&quot;,function(){});H(d,&quot;P&quot;,t);ma();if(g.addEventListener){var ra;g.addEventListener(&quot;DOMContentLoaded&quot;,ra=function(){t.trigger(&quot;a-domready&quot;);g.removeEventListener(&quot;DOMContentLoaded&quot;,ra,!1)},!1)}var h=g.documentElement,da=function(){var a=[&quot;O&quot;,&quot;ms&quot;,&quot;Moz&quot;,&quot;Webkit&quot;],b=g.createElement(&quot;div&quot;);return{testGradients:function(){return!0},test:function(c){var d=
c.charAt(0).toUpperCase()+c.substr(1);c=(a.join(d+&quot; &quot;)+d+&quot; &quot;+c).split(&quot; &quot;);for(d=c.length;d--;)if(&quot;&quot;===b.style[c[d]])return!0;return!1},testTransform3d:function(){return!0}}}();v=h.className;var sa=/(^| )a-mobile( |$)/.test(v),ta=/(^| )a-tablet( |$)/.test(v),l={audio:function(){return!!g.createElement(&quot;audio&quot;).canPlayType},video:function(){return!!g.createElement(&quot;video&quot;).canPlayType},canvas:function(){return!!g.createElement(&quot;canvas&quot;).getContext},svg:function(){return!!g.createElementNS&amp;&amp;!!g.createElementNS(&quot;http://www.w3.org/2000/svg&quot;,
&quot;svg&quot;).createSVGRect},offline:function(){return navigator.hasOwnProperty&amp;&amp;navigator.hasOwnProperty(&quot;onLine&quot;)&amp;&amp;navigator.onLine},dragDrop:function(){return&quot;draggable&quot;in g.createElement(&quot;span&quot;)},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!d.history||!d.history.pushState)},webworker:function(){return!!d.Worker},autofocus:function(){return&quot;autofocus&quot;in g.createElement(&quot;input&quot;)},inputPlaceholder:function(){return&quot;placeholder&quot;in g.createElement(&quot;input&quot;)},textareaPlaceholder:function(){return&quot;placeholder&quot;in
g.createElement(&quot;textarea&quot;)},localStorage:function(){return&quot;localStorage&quot;in d&amp;&amp;null!==d.localStorage},orientation:function(){return&quot;orientation&quot;in d},touch:function(){return&quot;ontouchend&quot;in g},gradients:function(){return da.testGradients()},hires:function(){var a=d.devicePixelRatio&amp;&amp;1.5<=d.devicePixelRatio||d.matchMedia&amp;&amp;d.matchMedia(&quot;(min-resolution:144dpi)&quot;).matches;m(&quot;hiRes&quot;+(sa?&quot;Mobile&quot;:ta?&quot;Tablet&quot;:&quot;Desktop&quot;),a?1:0);return a},transform3d:function(){return da.testTransform3d()},touchScrolling:function(){return q(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|SOFTWARE=([5-9]|[1-9][0-9]+)(.[0-9]{1,2})+.*DEVICE=iPhone|Chrome|Silk|Firefox|Trident.+?; Touch/i)},
ios:function(){return q(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&amp;&amp;!q(/trident|Edge/i)},android:function(){return q(/android.([1-9]|[L-Z])/i)&amp;&amp;!q(/trident|Edge/i)},mobile:function(){return sa},tablet:function(){return ta},rtl:function(){return&quot;rtl&quot;===h.dir}};for(p in l)l.hasOwnProperty(p)&amp;&amp;(l[p]=na(l[p]));for(var ea=&quot;textShadow textStroke boxShadow borderRadius borderImage opacity transform transition&quot;.split(&quot; &quot;),R=0;R<ea.length;R++)l[ea[R]]=na(function(){return da.test(ea[R])});var M=!0,oa=0,ba=
{w:0,h:0},N=4;L();z(d,&quot;resize&quot;,function(){clearTimeout(oa);N=4;L()});var ua={getItem:function(a){try{return d.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return d.localStorage.setItem(a,b)}catch(c){}}};h.className=aa(h,&quot;a-no-js&quot;);F(h,&quot;a-js&quot;);!q(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||d.navigator.standalone||q(/safari/i)||F(h,&quot;a-ember&quot;);v=[];for(p in l)l.hasOwnProperty(p)&amp;&amp;l[p]&amp;&amp;v.push(&quot;a-&quot;+p.replace(/([A-Z])/g,function(a){return&quot;-&quot;+a.toLowerCase()}));F(h,v.join(&quot; &quot;));h.setAttribute(&quot;data-aui-build-date&quot;,
&quot;3.23.1-2023-04-21&quot;);t.register(&quot;p-detect&quot;,function(){return{capabilities:l,localStorage:l.localStorage&amp;&amp;ua,toggleResponsiveGrid:Aa,responsiveGridEnabled:Ba}});q(/UCBrowser/i)||l.localStorage&amp;&amp;F(h,ua.getItem(&quot;a-font-class&quot;));t.declare(&quot;a-event-revised-handling&quot;,!1);t.execute(&quot;RetailPageServiceWorker&quot;,function(){function a(a,b){f.controller&amp;&amp;a?(a={feature:&quot;retail_service_worker_messaging&quot;,command:a},b&amp;&amp;(a.data=b),f.controller.postMessage(a)):a&amp;&amp;m(&quot;sw:sw_message_no_ctrl&quot;,1)}function b(a){var b=a.data;
if(b&amp;&amp;&quot;retail_service_worker_messaging&quot;===b.feature&amp;&amp;b.command&amp;&amp;b.data){var c=b.data;a=d.ue;var e=d.ueLogError;switch(b.command){case &quot;log_counter&quot;:a&amp;&amp;r(a.count)&amp;&amp;c.name&amp;&amp;a.count(c.name,0===c.value?0:c.value||1);break;case &quot;log_tag&quot;:a&amp;&amp;r(a.tag)&amp;&amp;c.tag&amp;&amp;(a.tag(c.tag),b=d.uex,a.isl&amp;&amp;r(b)&amp;&amp;b(&quot;at&quot;));break;case &quot;log_error&quot;:e&amp;&amp;r(e)&amp;&amp;c.message&amp;&amp;e({message:c.message,logLevel:c.level||&quot;ERROR&quot;,attribution:c.attribution||&quot;RetailServiceWorker&quot;});break;case &quot;log_weblab_trigger&quot;:if(!c.weblab||!c.treatment)break;
a&amp;&amp;r(a.trigger)?a.trigger(c.weblab,c.treatment):(m(&quot;sw:wt:miss&quot;),m(&quot;sw:wt:miss:&quot;+c.weblab+&quot;:&quot;+c.treatment));break;default:m(&quot;sw:unsupported_message_command&quot;,1)}}}function c(){e.forEach(function(a){w(a)})}function h(a,b,c){if(b){a=q(/Chrome/i)&amp;&amp;!q(/Edge/i)&amp;&amp;!q(/OPR/i)&amp;&amp;!a.capabilities.isAmazonApp&amp;&amp;!q(new RegExp(ca+&quot;bwv&quot;+ca+&quot;b&quot;));var d=&quot;sw:browser:&quot;+c+&quot;:&quot;;b.browser&amp;&amp;a&amp;&amp;(e.push(d+&quot;supported&quot;),b.browser.action(d,c));!a&amp;&amp;b.browser&amp;&amp;e.push(d+&quot;unsupported&quot;)}}try{var f=navigator.serviceWorker}catch(n){w(&quot;sw:nav_err&quot;)}(function(){if(f){var c=
function(){a(&quot;page_loaded&quot;,{rid:d.ue_id,mid:d.ue_mid,pty:d.ue_pty,sid:d.ue_sid,spty:d.ue_spty,furl:d.ue_furl})};z(f,&quot;message&quot;,b);a(&quot;client_messaging_ready&quot;);t.when(&quot;load&quot;).execute(c);z(f,&quot;controllerchange&quot;,function(){a(&quot;client_messaging_ready&quot;);&quot;complete&quot;===g.readyState&amp;&amp;c()})}})();var e=[],l=function(a,b){var c=d.uex,e=d.uet;a=k(&quot;:&quot;,&quot;aui&quot;,&quot;sw&quot;,a);&quot;ld&quot;===b&amp;&amp;r(c)?c(&quot;ld&quot;,a,{wb:1}):r(e)&amp;&amp;e(b,a,{wb:1})},p=function(a,b,c){function e(a){b&amp;&amp;r(b.failure)&amp;&amp;b.failure(a)}function g(){p=setTimeout(function(){w(k(&quot;:&quot;,
&quot;sw:&quot;+n,h.TIMED_OUT));e({ok:!1,statusCode:h.TIMED_OUT,done:!1});l(n,&quot;ld&quot;)},c||4E3)}var h={NO_CONTROLLER:&quot;no_ctrl&quot;,TIMED_OUT:&quot;timed_out&quot;,UNSUPPORTED_BROWSER:&quot;unsupported_browser&quot;,UNEXPECTED_RESPONSE:&quot;unexpected_response&quot;},n=k(&quot;:&quot;,a.feature,a.command),p,q=!0;if(&quot;MessageChannel&quot;in d&amp;&amp;f&amp;&amp;&quot;controller&quot;in f)if(f.controller){var B=new MessageChannel;B.port1.onmessage=function(c){(c=c.data)&amp;&amp;c.feature===a.feature&amp;&amp;c.command===a.command?(q&amp;&amp;(l(n,&quot;cf&quot;),q=!1),l(n,&quot;af&quot;),clearTimeout(p),c.done||g(),c.ok?b&amp;&amp;r(b.success)&amp;&amp;
b.success(c):e(c),c.done&amp;&amp;l(n,&quot;ld&quot;)):m(k(&quot;:&quot;,&quot;sw:&quot;+n,h.UNEXPECTED_RESPONSE),1)};g();l(n,&quot;bb&quot;);f.controller.postMessage(a,[B.port2])}else w(k(&quot;:&quot;,&quot;sw:&quot;+a.feature,h.NO_CONTROLLER)),e({ok:!1,statusCode:h.NO_CONTROLLER,done:!0});else w(k(&quot;:&quot;,&quot;sw:&quot;+a.feature,h.UNSUPPORTED_BROWSER)),e({ok:!1,statusCode:h.UNSUPPORTED_BROWSER,done:!0})};(function(){f?(l(&quot;ctrl_changed&quot;,&quot;bb&quot;),f.addEventListener(&quot;controllerchange&quot;,function(){w(&quot;sw:ctrl_changed&quot;);l(&quot;ctrl_changed&quot;,&quot;ld&quot;)})):m(k(&quot;:&quot;,&quot;sw:ctrl_changed&quot;,&quot;sw_unsupp&quot;),
1)})();(function(){var a=function(){l(b,&quot;ld&quot;);var a=d.uex;p({feature:&quot;page_proxy&quot;,command:&quot;request_feature_tags&quot;},{success:function(b){b=b.data;Array.isArray(b)&amp;&amp;b.forEach(function(a){&quot;string&quot;===typeof a?w(k(&quot;:&quot;,&quot;sw:ppft&quot;,a)):m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;invalid_tag&quot;),1)});m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;success&quot;),1);x&amp;&amp;x.isl&amp;&amp;r(a)&amp;&amp;a(&quot;at&quot;)},failure:function(a){m(k(&quot;:&quot;,&quot;sw:ppft&quot;,&quot;error:&quot;+(a.statusCode||&quot;ppft_error&quot;)),1)}})};if(&quot;requestIdleCallback&quot;in d){var b=k(&quot;:&quot;,&quot;ppft&quot;,&quot;callback_ricb&quot;);d.requestIdleCallback(a,{timeout:1E3})}else b=
k(&quot;:&quot;,&quot;ppft&quot;,&quot;callback_timeout&quot;),setTimeout(a,0);l(b,&quot;bb&quot;)})();(function(a){var b=a.reg,g=a.unreg;f&amp;&amp;f.getRegistrations?(Q.when(&quot;A&quot;).execute(function(a){h(a,g,&quot;unregister&quot;)}),z(d,&quot;load&quot;,function(){Q.when(&quot;A&quot;).execute(function(a){h(a,b,&quot;register&quot;);c()})})):(b&amp;&amp;b.browser&amp;&amp;e.push(&quot;sw:browser:register:unsupported&quot;),g&amp;&amp;g.browser&amp;&amp;e.push(&quot;sw:browser:unregister:unsupported&quot;),c())})({reg:{},unreg:{}})});t.declare(&quot;a-fix-event-off&quot;,!1);m(&quot;pagejs:pkgExecTime&quot;,A()-P)})(window,document,Date);
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61yXDIPmT-L._RC|11Y+5x+kkTL.js,51Am7NcREVL.js,11yKORv-GTL.js,11GgN1+C7hL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,516j7qaWchL.js,11kWu3cNjYL.js,11wr1I7-WYL.js,11OREnu1epL.js,11Wm6BwZ+6L.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31nfKXylf6L.js,01ezj5Rkz1L.js,11bEz2VIYrL.js,31o2NGTXThL.js,01rpauTep4L.js,015tKjxsR2L.js_.js?AUIClients/AmazonUI&amp;MFdCk5El#567364-T1.432724-T1.577970-T1');
(function(c){function z(b,r,c,l){b.addEventListener?b.addEventListener(r,c,!0===l):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+r,c)}function C(){if(c.safeFrameId)return c.safeFrameId;var b=c.location.href;if((b=b&amp;&amp;b.match(/[&amp;?]safeFrameId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/))&amp;&amp;b[1])return b[1]}function D(){if(c.MutationObserver&amp;&amp;c.getComputedStyle){var b=function(){var b;b=document.body.childNodes;var n=b.length,l=Infinity,p=-Infinity,q=-Infinity,m=Infinity,e,g,h,t;if(0!==n&amp;&amp;c.getComputedStyle){for(;n--;)e=
b[n],e.getBoundingClientRect&amp;&amp;(g=c.getComputedStyle(e),g&amp;&amp;&quot;absolute&quot;===g.position||(g=e.getBoundingClientRect(),h=g.left||0,t=Math.max(g.width||0,e.scrollWidth),e=Math.max(g.height||0,e.scrollHeight),l=Math.min(Math.floor(g.top||0),l),p=Math.max(Math.ceil(h+t),Math.ceil(g.right),p),q=Math.max(Math.ceil(l+e),Math.ceil(g.bottom),q),m=Math.min(Math.floor(h),m)));b={width:p-m,height:q-l}}else b=void 0;b&amp;&amp;b.width&amp;&amp;b.height&amp;&amp;(SafeFrameClient.setWidth(b.width),SafeFrameClient.setHeight(b.height))};b();b=
new MutationObserver(b);b.observe(document.body,{childList:!0,subtree:!0});return b}}function x(){function b(a){a.frameId=A;parent.postMessage(JSON.stringify(a),&quot;*&quot;)}function r(){return k.geom}function n(){var a=k.geom&amp;&amp;k.geom.self&amp;&amp;k.geom.self.iv;return&quot;undefined&quot;!==typeof a?100*a:a}function l(){return k.hasAdBlocker}function p(a,d,w){var c;try{c=JSON.parse(JSON.stringify(d))}catch(e){c={}}b({action:&quot;LOG_ERROR&quot;,message:a,exception:c,logLevel:w})}function q(){m();u=D()}function m(){u&amp;&amp;&quot;function&quot;===
typeof u.disconnect&amp;&amp;u.disconnect();u=void 0}function e(a,d,b,c){a&amp;&amp;v.hasOwnProperty(a)&amp;&amp;((d=v[a]&amp;&amp;v[a][d])&amp;&amp;d.apply&amp;&amp;d.apply(null,b),c&amp;&amp;delete v[a])}function g(a,d){a&amp;&amp;&quot;function&quot;===typeof d&amp;&amp;(!0===B[a]&amp;&amp;y[a]?d(y[a]):(f[a]=f[a]||[],f[a].push(d)))}function h(a,d){var b,c,e;if(f[a]&amp;&amp;0<f[a].length)for(e=[].concat(f[a]),c=e.length,b=0;b<c;b++)e[b](d);!0===B[a]&amp;&amp;(delete f[a],y[a]=d)}function t(a){var b;try{b=JSON.parse(a.data)}catch(c){b={}}var w=E[b.action];a.source===parent&amp;&amp;w&amp;&amp;w(b)}var A=C(),x=document.write,
k={},f={},B={adblockerdetected:!0,atf:!0,cf:!0,clientReady:!0,load:!0},y={},u,v={},E={REGISTERED:function(a){k.geom=a.geom;k.isVisible=a.isVisible;k.hasAdBlocker=a.hasAdBlocker;h(&quot;clientReady&quot;,{});a=a.completedEventData||{};for(var b in a)a.hasOwnProperty(b)&amp;&amp;h(b,a[b]);l()&amp;&amp;h(&quot;adblockerdetected&quot;)},SCROLL:function(a){k.geom=a.geom;h(&quot;scroll&quot;,{})},RESIZE:function(a){k.geom=a.geom;h(&quot;resize&quot;,{})},VISIBILITY_CHANGE:function(a){k.isVisible=a.isVisible;h(&quot;visibilitychange&quot;,{})},TRIGGER:function(a){h(a.eventName,
a.eventData||{})},AD_BLOCKER_DETECTED:function(){k.hasAdBlocker=!0;h(&quot;adblockerdetected&quot;)},LOAD_CONTENTS:function(a){document.body.innerHTML=&quot;&quot;;var b=document.body,c=a.contents;a=document.createElement(&quot;div&quot;);var e=&quot;text&quot;in a?&quot;text&quot;:&quot;textContent&quot;,g,k,h,f;a.innerHTML=&quot;_&quot;+c;a.removeChild(a.firstChild);c=a.getElementsByTagName(&quot;script&quot;);g=0;for(k=c.length;g<k;g++)f=c[g],h=document.createElement(&quot;script&quot;),f.type&amp;&amp;(h.type=f.type),f.src?h.src=f.src:f[e]&amp;&amp;(h[e]=f[e]),f.parentNode.replaceChild(h,f);b.appendChild(a)},
ENABLE_AUTO_RESIZE:function(){q()},DISABLE_AUTO_RESIZE:function(){m()},AJAX_SUCCESS:function(a){e(a.requestId,&quot;success&quot;,[a.response,a.status],!0)},AJAX_ERROR:function(a){e(a.requestId,&quot;error&quot;,[null,a.status,a.error],!0)},AJAX_ABORT:function(a){e(a.requestId,&quot;abort&quot;,[],!0)},AJAX_CHUNK:function(a){e(a.requestId,&quot;chunk&quot;,[a.chunk],!1)}};(function(){document.write=function(){Function.prototype.apply.call(x,document,arguments);z(c,&quot;message&quot;,t,!1)}})();(function(){c.onerror=function(a,b,c,e,f){p([&quot;window.onerror&quot;,
a,b,c,e].join(&quot;;&quot;),f,&quot;ERROR&quot;);return!0}})();z(c,&quot;message&quot;,t,!1);(function(){g(&quot;clientReady&quot;,function(){b({action:&quot;CLIENT_READY&quot;})})})();c.$sf=c.$sf||{ext:{geom:r,inViewPercentage:n}};b({action:&quot;REGISTER&quot;,timestamp:(new Date).getTime()});return{isVisible:function(){return k.isVisible},geom:r,inViewPercentage:n,hasAdBlocker:l,sendMetrics:function(a,d){b({action:&quot;SEND_METRICS&quot;,metric:a,scope:d})},countMetric:function(a,d){b({action:&quot;COUNT_METRIC&quot;,counterName:a,value:d})},incrementMetric:function(a,d){b({action:&quot;INCREMENT_METRIC&quot;,
counterName:a,value:d})},logError:p,setHeight:function(a){b({action:&quot;SET_HEIGHT&quot;,value:a})},setWidth:function(a){b({action:&quot;SET_WIDTH&quot;,value:a})},collapse:function(){b({action:&quot;COLLAPSE&quot;})},showFooter:function(a){b({action:&quot;SHOW_FOOTER&quot;,data:a})},getContents:function(){b({action:&quot;GET_CONTENTS&quot;})},enableAutoResize:q,disableAutoResize:m,ajax:function(a,d){var c=a+Math.random().toString(36);d=d||{};v[c]={success:d.success,error:d.error,abort:d.abort,chunk:d.chunk};b({action:&quot;AJAX&quot;,url:a,requestId:c,
options:{accepts:d.accepts,cache:d.cache,contentType:d.contentType,method:d.method,params:d.params,paramsFormat:d.paramsFormat,timeout:d.timeout}})},on:g,off:function(a,b){var c;if(f[a]&amp;&amp;0<f[a].length)for(c=f[a].length;c--;)if(f[a][c]===b){f[a].splice(c,1);break}},tagRequest:function(a){b({action:&quot;TAG_REQUEST&quot;,frameId:A,tagName:a})}}}c.SafeFrameClient=c.SafeFrameClient||x()})(window);
</script>

</head>
<body style=&quot;margin:0;padding:0;&quot;>
    <!--SINGLETON CONTENT-->

    <script>
        window.SafeFrameClient &amp;&amp; SafeFrameClient.on('clientReady', function(){
            SafeFrameClient.countMetric('clientReady', 1);
        });
    </script>
</body>
</html>
" data-use-srcdoc-fallback="false" data-auto-load="true" onload="(function(el, ts){ P.when('amzn-safe-frame-auto-loader').execute(function(fn){ fn(el, ts); }); }(this, +(new Date())));" data-frame-id="d5514bb4-eeca-4bec-b32e-f847f3624acf" data-frame-attribution="SafeModalView:Unset" data-additional-attribution="" data-metrics-scope="searchSafeFrame:modal:s-safe-modal-singleton" data-capabilities="AUI,AJAX" height="300" class="amzn-safe-frame aok-block" frameborder="0" scrolling="no"></iframe>
                <div class="amzn-safe-frame-footer amzn-safe-frame-footer-below aok-hidden">
    </div>

    </div>

        <script> window.uet && uet('be', 'searchSafeFrame:modal:s-safe-modal-singleton', {wb: 1}); </script>
</div>

        </div>
    </div>
</div>


    


</div>
<!-- sp:end-feature:host-atf -->
<!-- sp:feature:nav-btf -->
<!-- NAVYAAN BTF START -->




  



  <script type="text/javascript">(function ($Nav) {
"use strict";

if (typeof $Nav === 'undefined' || $Nav === null || typeof $Nav.when !== 'function') {
    return;
}

$Nav.when('$', 'data', 'flyout.yourAccount', 'sidepanel.csYourAccount',
          'config')
    .run("BuyitAgain-YourAccount-SidePanel",
    function ($, data, yaFlyout, csYourAccount, config) {
        if (config.disableBuyItAgain) {
            return;
        }
        var render = function (data) {
            if (data.dramResult) {
                var widgetHtml = data.dramResult;
                navbar.sidePanel({
                    flyoutName: 'yourAccount',
                    data: {html: widgetHtml}
                });
            }
        };

        var renderBuyItAgain = function (biaData) {
            if (csYourAccount) {
                csYourAccount.register(render, biaData);
            } else {
                render(biaData);
            }
        };

        var truncateAndRestructureYaFlyout = function() {
            if (window.P) {
                P.when('A', 'a-truncate').execute(function(A, truncate) {
                    var truncateElements = A.$('.a-truncate');
                    A.each(truncateElements, function(element) {
                        truncate.get(element).update();
                    });
                    var recommendationsWidget = document.getElementById('bia-hcb-widget');
                    if (recommendationsWidget) { 
                        var navFlyout = recommendationsWidget.parentElement;
                        var navFlyoutPaddingBottom = parseInt(window.getComputedStyle(navFlyout).getPropertyValue('padding-bottom'));
                        var navFlyoutContentHeight = navFlyout.clientHeight - navFlyoutPaddingBottom;
                        while (recommendationsWidget.offsetHeight > navFlyoutContentHeight && recommendationsWidget.offsetHeight > 0){
                            var recommendations = recommendationsWidget.querySelectorAll('.biaNavFlyoutFaceout');
                            if (recommendations.length <= 1) {
                                break;
                            }
                            var lastRecommendation = recommendations[recommendations.length - 1];
                            lastRecommendation.parentElement.removeChild(lastRecommendation);
                        }
                    }
               });
            }
        };

        yaFlyout.sidePanel.onData(truncateAndRestructureYaFlyout);
        yaFlyout.onShow(truncateAndRestructureYaFlyout);

    yaFlyout.onRender(function() {
            $.ajax({
                url: '/gp/bia/external/bia-hcb-ajax-handler.html',
                data: {"biaHcbRid":"BNJYY9EBY54VZZF6X4X6"},
                dataType: 'json',
                timeout: 4*1000,
                success: renderBuyItAgain,
                error: function (jqXHR, textStatus, errorThrown) {
                }
            });
        });
    });
})(window.$Nav);</script>


<script type="text/javascript">
  window.$Nav && $Nav.when("data").run(function (data) {
    data({
      "accountListContent": { "html": "<div id='nav-al-container'><div id='nav-al-signin'><div id='nav-flyout-ya-signin' class='nav-flyout-content nav-flyout-accessibility'><a href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26dc%3D%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26i%3Dstripbooks%26k%3Dbookstore%2520amazon%26qid%3D1682200770%26ref%3Dsr_nr_p_n_condition-type_1%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-action-signin-button' data-nav-role='signin' data-nav-ref='nav_signin'><span class='nav-action-inner'>Sign in</span></a><div id='nav-flyout-ya-newCust' class='nav_pop_new_cust nav-flyout-content nav-flyout-accessibility'>New customer? <a href='https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26dc%3D%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26i%3Dstripbooks%26k%3Dbookstore%2520amazon%26qid%3D1682200770%26ref%3Dsr_nr_p_n_condition-type_1%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-a'>Start here.</a></div></div></div><div id='nav-al-wishlist' class='nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility'><div class='nav-title' id='nav-al-title'>Your Lists</div><a href='/hz/wishlist/ls?triggerElementID=createList&ref_=nav_ListFlyout_navFlyout_createList_lv_redirect' class='nav-link nav-item'><span class='nav-text'>Create a List</span></a> <a href='/registries?ref_=nav_ListFlyout_find' class='nav-link nav-item'><span class='nav-text'>Find a List or Registry</span></a></div><div id='nav-al-your-account' class='nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility'><div class='nav-title'>Your Account</div><a href='/gp/css/homepage.html?ref_=nav_AccountFlyout_ya' class='nav-link nav-item'><span class='nav-text'>Account</span></a> <a id='nav_prefetch_yourorders' href='/gp/css/order-history?ref_=nav_AccountFlyout_orders' class='nav-link nav-item'><span class='nav-text'>Orders</span></a> <a href='/gp/yourstore?ref_=nav_AccountFlyout_recs' class='nav-link nav-item'><span class='nav-text'>Recommendations</span></a> <a href='/gp/history?ref_=nav_AccountFlyout_browsinghistory' class='nav-link nav-item'><span class='nav-text'>Browsing History</span></a> <a href='/gp/video/watchlist?ref_=nav_AccountFlyout_ywl' class='nav-link nav-item'><span class='nav-text'>Watchlist</span></a> <a href='/gp/video/library?ref_=nav_AccountFlyout_yvl' class='nav-link nav-item'><span class='nav-text'>Video Purchases & Rentals</span></a> <a href='/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku' class='nav-link nav-item'><span class='nav-text'>Kindle Unlimited</span></a> <a href='/hz/mycd/myx?pageType=content&ref_=nav_AccountFlyout_myk' class='nav-link nav-item'><span class='nav-text'>Content & Devices</span></a> <a href='/gp/subscribe-and-save/manager/viewsubscriptions?ref_=nav_AccountFlyout_sns' class='nav-link nav-item'><span class='nav-text'>Subscribe & Save Items</span></a> <a href='/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions' class='nav-link nav-item'><span class='nav-text'>Memberships & Subscriptions</span></a> <a href='https://music.amazon.com?ref=nav_youraccount_cldplyr' class='nav-link nav-item'><span class='nav-text'>Music Library</span></a></div></div>" },
      "signinContent": { "html": "<div id='nav-signin-tooltip'><a href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26dc%3D%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26i%3Dstripbooks%26k%3Dbookstore%2520amazon%26qid%3D1682200770%26ref%3Dsr_nr_p_n_condition-type_1%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-action-signin-button' data-nav-role='signin' data-nav-ref='nav_custrec_signin'><span class='nav-action-inner'>Sign in</span></a><div class='nav-signin-tooltip-footer'>New customer? <a href='https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26dc%3D%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26i%3Dstripbooks%26k%3Dbookstore%2520amazon%26qid%3D1682200770%26ref%3Dsr_nr_p_n_condition-type_1%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-a'>Start here.</a></div></div>" },
      "templates": {"itemList":"<# var hasColumns = (function () {  var checkColumns = function (_items) {    if (!_items) {      return false;    }    for (var i=0; i<_items.length; i++) {      if (_items[i].columnBreak || (_items[i].items && checkColumns(_items[i].items))) {        return true;      }    }    return false;  };  return checkColumns(items);}()); #><# if(hasColumns) { #>  <# if(items[0].image && items[0].image.src) { #>    <div class='nav-column nav-column-first nav-column-image'>  <# } else if (items[0].greeting) { #>    <div class='nav-column nav-column-first nav-column-greeting'>  <# } else { #>    <div class='nav-column nav-column-first'>  <# } #><# } #><# var renderItems = function(items) { #>  <# jQuery.each(items, function (i, item) { #>    <# if(hasColumns && item.columnBreak) { #>      <# if(item.image && item.image.src) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-image'>      <# } else if (item.greeting) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-greeting'>      <# } else { #>        </div><div class='nav-column nav-column-notfirst nav-column-break'>      <# } #>    <# } #>    <# if(item.dividerBefore) { #>      <div class='nav-divider'></div>    <# } #>    <# if(item.text || item.content) { #>      <# if(item.url) { #>        <a href='<#=item.url #>' class='nav-link      <# } else {#>        <span class='      <# } #>      <# if(item.panelKey) { #>        nav-hasPanel      <# } #>      <# if(item.items) { #>        nav-title      <# } #>      <# if(item.decorate == 'carat') { #>        nav-carat      <# } #>      <# if(item.decorate == 'nav-action-button') { #>        nav-action-button      <# } #>      nav-item'      <# if(item.extra) { #>        <#=item.extra #>      <# } #>      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      <# if(item.dataNavRole) { #>        data-nav-role='<#=item.dataNavRole #>'      <# } #>      <# if(item.dataNavRef) { #>        data-nav-ref='<#=item.dataNavRef #>'      <# } #>      <# if(item.panelKey) { #>        data-nav-panelkey='<#=item.panelKey #>'        role='navigation'        aria-label='<#=item.text#>'      <# } #>      <# if(item.subtextKey) { #>        data-nav-subtextkey='<#=item.subtextKey #>'      <# } #>      <# if(item.image && item.image.height > 16) { #>        style='line-height:<#=item.image.height #>px;'      <# } #>      >      <# if(item.decorate == 'carat') { #>        <i class='nav-icon'></i>      <# } #>      <# if(item.image && item.image.src) { #>        <img class='nav-image' src='<#=item.image.src #>' style='height:<#=item.image.height #>px; width:<#=item.image.width #>px;' />      <# } #>      <# if(item.text) { #>        <span class='nav-text<# if(item.classname) { #> <#=item.classname #><# } #>'><#=item.text#><# if(item.badgeText) { #>          <span class='nav-badge'><#=item.badgeText#></span>        <# } #></span>      <# } else if (item.content) { #>        <span class='nav-content'><# jQuery.each(item.content, function (j, cItem) { #><# if(cItem.url && cItem.text) { #><a href='<#=cItem.url #>' class='nav-a'><#=cItem.text #></a><# } else if (cItem.text) { #><#=cItem.text#><# } #><# }); #></span>      <# } #>      <# if(item.subtext) { #>        <span class='nav-subtext'><#=item.subtext #></span>      <# } #>      <# if(item.url) { #>        </a>      <# } else {#>        </span>      <# } #>    <# } #>    <# if(item.image && item.image.src) { #>      <# if(item.url) { #>        <a href='<#=item.url #>'>       <# } #>      <img class='nav-image'      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      src='<#=item.image.src #>' <# if (item.alt) { #> alt='<#= item.alt #>'<# } #>/>      <# if(item.url) { #>        </a>       <# } #>    <# } #>    <# if(item.items) { #>      <div class='nav-panel'> <# renderItems(item.items); #> </div>    <# } #>  <# }); #><# }; #><# renderItems(items); #><# if(hasColumns) { #>  </div><# } #>","subnav":"<# if (obj && obj.type === 'vertical') { #>  <# jQuery.each(obj.rows, function (i, row) { #>    <# if (row.flyoutElement === 'button') { #>      <div class='nav_sv_fo_v_button'        <# if (row.elementStyle) { #>          style='<#= row.elementStyle #>'        <# } #>      >        <a href='<#=row.url #>' class='nav-action-button nav-sprite'>          <#=row.text #>        </a>      </div>    <# } else if (row.flyoutElement === 'list' && row.list) { #>      <# jQuery.each(row.list, function (j, list) { #>        <div class='nav_sv_fo_v_column <#=(j === 0) ? 'nav_sv_fo_v_first' : '' #>'>          <ul class='<#=list.elementClass #>'>          <# jQuery.each(list.linkList, function (k, link) { #>            <# if (k === 0) { link.elementClass += ' nav_sv_fo_v_first'; } #>            <li class='<#=link.elementClass #>'>              <# if (link.url) { #>                <a href='<#=link.url #>' class='nav_a'><#=link.text #></a>              <# } else { #>                <span class='nav_sv_fo_v_span'><#=link.text #></span>              <# } #>            </li>          <# }); #>          </ul>        </div>      <# }); #>    <# } else if (row.flyoutElement === 'link') { #>      <# if (row.topSpacer) { #>        <div class='nav_sv_fo_v_clear'></div>      <# } #>      <div class='<#=row.elementClass #>'>        <a href='<#=row.url #>' class='nav_sv_fo_v_lmargin nav_a'>          <#=row.text #>        </a>      </div>    <# } #>  <# }); #><# } else if (obj) { #>  <div class='nav_sv_fo_scheduled'>    <#= obj #>  </div><# } #>","htmlList":"<# jQuery.each(items, function (i, item) { #>  <div class='nav-item'>    <#=item #>  </div><# }); #>"}
    })
  })
</script>

<script type="text/javascript">
  window.$Nav && $Nav.declare('config.flyoutURL', null);
  window.$Nav && $Nav.declare('btf.lite');
  window.$Nav && $Nav.declare('btf.full');
  window.$Nav && $Nav.declare('btf.exists');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).register('navCF');
</script>


<!-- NAVYAAN BTF END -->
<!-- sp:end-feature:nav-btf -->
<!-- sp:feature:host-btf -->
<!-- sp:end-feature:host-btf -->
<!-- sp:feature:aui-preload -->
<!-- sp:end-feature:aui-preload -->
<!-- sp:feature:nav-footer -->

  <!-- NAVYAAN FOOTER START -->
  <!-- WITH MOZART -->

<div id="rhf" class="copilot-secure-display" style="clear: both;" role="complementary" aria-label="Your recently viewed items and featured recommendations" data-cel-widget="rhf"> <div class="rhf-frame" style="display: none;"> <br> <div id="rhf-container"> <div class="rhf-loading-outer"> <table class="rhf-loading-middle"> <tbody><tr> <td class="rhf-loading-inner"> <img src="https://m.media-amazon.com/images/G/01/personalization/ybh/loading-4x-gray._CB485916920_.gif"> </td> </tr> </tbody></table> </div> <div id="rhf-context"> <script type="application/json"> { "rhfHandlerParams":{"currentPageType":"Search","currentSubPageType":"List","excludeAsin":"","fieldKeywords":"","k":"bookstore%20amazon","keywords":"","search":"","auditEnabled":"","previewCampaigns":"","forceWidgets":"","searchAlias":"stripbooks"} } </script> </div> </div> <noscript> <div class='rhf-border'> <div class='rhf-header'> Your recently viewed items and featured recommendations </div> <div class='rhf-footer'> <div class='rvi-container'> <div class='ybh-edit'> <div class='ybh-edit-arrow'> &#8250; </div> <div class='ybh-edit-link'> <a href='/gp/history'> View or edit your browsing history </a> </div> </div> <span class='no-rvi-message'> After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. </span> </div> </div> </div> </noscript> <div id="rhf-error" style="display: none;"> <div class="rhf-border"> <div class="rhf-header"> Your recently viewed items and featured recommendations </div> <div class="rhf-footer"> <div class="rvi-container"> <div class="ybh-edit"> <div class="ybh-edit-arrow"> › </div> <div class="ybh-edit-link"> <a href="/gp/history"> View or edit your browsing history </a> </div> </div> <span class="no-rvi-message"> After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. </span> </div> </div> </div> </div> <br> </div> </div>
<div class="navLeftFooter nav-sprite-v1" id="navFooter" data-cel-widget="navFooter">
  
<a href="#" id="navBackToTop" aria-label="Back to top" onclick="document.body.scrollTop = 0; document.documentElement.scrollTop = 0; event.preventDefault();">
  <div class="navFooterBackToTop">
  <span class="navFooterBackToTopText">
    Back to top
  </span>
  </div>
</a>

  
<div class="navFooterVerticalColumn navAccessibility" role="presentation">
  <div class="navFooterVerticalRow navAccessibility" style="display: table-row;">
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Get to Know Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://www.amazon.jobs" class="nav_a">Careers</a>
            </li>
            <li>
              <a href="https://blog.aboutamazon.com/?utm_source=gateway&amp;utm_medium=footer" class="nav_a">Blog</a>
            </li>
            <li>
              <a href="https://www.aboutamazon.com/?utm_source=gateway&amp;utm_medium=footer" class="nav_a">About Amazon</a>
            </li>
            <li>
              <a href="https://www.amazon.com/ir" class="nav_a">Investor Relations</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=2102313011&amp;ref_=footer_devices" class="nav_a">Amazon Devices</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.science" class="nav_a">Amazon Science</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Make Money with Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://services.amazon.com/sell.html?ld=AZFSSOA&amp;ref_=footer_soa" class="nav_a">Sell products on Amazon</a>
            </li>
            <li>
              <a href="https://services.amazon.com/amazon-business.html?ld=usb2bunifooter&amp;ref_=footer_b2b" class="nav_a">Sell on Amazon Business</a>
            </li>
            <li>
              <a href="https://developer.amazon.com" class="nav_a">Sell apps on Amazon</a>
            </li>
            <li>
              <a href="https://affiliate-program.amazon.com/" class="nav_a">Become an Affiliate</a>
            </li>
            <li>
              <a href="https://advertising.amazon.com/?ref=ext_amzn_ftr" class="nav_a">Advertise Your Products</a>
            </li>
            <li>
              <a href="/gp/seller-account/mm-summary-page.html?ld=AZFooterSelfPublish&amp;topic=200260520&amp;ref_=footer_publishing" class="nav_a">Self-Publish with Us</a>
            </li>
            <li>
              <a href="https://go.thehub-amazon.com/amazon-hub-locker" class="nav_a">Host an Amazon Hub</a>
            </li>
            <li class="nav_last nav_a_carat">
              <span class="nav_a_carat" aria-hidden="true">›</span><a href="/b/?node=18190131011&amp;ld=AZUSSOA-seemore&amp;ref_=footer_seemore" class="nav_a">See More Make Money with Us</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Amazon Payment Products</div>
        <ul>
            <li class="nav_first">
              <a href="/dp/B07984JN3L?plattr=ACOMFO&amp;ie=UTF-8" class="nav_a">Amazon Business Card</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=16218619011&amp;ref_=footer_swp" class="nav_a">Shop with Points</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=10232440011&amp;ref_=footer_reload_us" class="nav_a">Reload Your Balance</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/browse.html?node=388305011&amp;ref_=footer_tfx" class="nav_a">Amazon Currency Converter</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Let Us Help You</div>
        <ul>
            <li class="nav_first">
              <a href="/gp/help/customer/display.html?nodeId=GDFU3JS5AL6SYHRD&amp;ref_=footer_covid" class="nav_a">Amazon and COVID-19</a>
            </li>
            <li>
              <a href="https://www.amazon.com/gp/css/homepage.html?ref_=footer_ya" class="nav_a">Your Account</a>
            </li>
            <li>
              <a href="https://www.amazon.com/gp/css/order-history?ref_=footer_yo" class="nav_a">Your Orders</a>
            </li>
            <li>
              <a href="/gp/help/customer/display.html?nodeId=468520&amp;ref_=footer_shiprates" class="nav_a">Shipping Rates &amp; Policies</a>
            </li>
            <li>
              <a href="/gp/css/returns/homepage.html?ref_=footer_hy_f_4" class="nav_a">Returns &amp; Replacements</a>
            </li>
            <li>
              <a href="/gp/digital/fiona/manage?ref_=footer_myk" class="nav_a">Manage Your Content and Devices</a>
            </li>
            <li>
              <a href="/gp/BIT/ref=footer_bit_v2_us_A0029?bitCampaignCode=A0029" class="nav_a">Amazon Assistant</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/help/customer/display.html?nodeId=508510&amp;ref_=footer_gw_m_b_he" class="nav_a">Help</a>
            </li>
        </ul>
      </div>
  </div>
</div>
<div class="nav-footer-line"></div>

  <div class="navFooterLine navFooterLinkLine navFooterPadItemLine">
    <span>
      <div class="navFooterLine navFooterLogoLine">
        <a aria-label="Amazon US Home" href="/?ref_=footer_logo">
        <div class="nav-logo-base nav-sprite"></div>
        </a>
      </div>
</span>
    
      <span class="icp-container-desktop"><div class="navFooterLine">
<style type="text/css">
  #icp-touch-link-language { display: none; }
</style>


<a href="/customer-preferences/edit?ie=UTF8&amp;preferencesReturnUrl=%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dsr_nr_p_n_condition-type_1&amp;ref_=footer_lang" aria-label="Choose a language for shopping." class="icp-button" id="icp-touch-link-language">
  <div class="icp-nav-globe-img-2 icp-button-globe-2"></div><span class="icp-color-base">English</span><span class="nav-arrow icp-up-down-arrow"></span>
</a>



<style type="text/css">
  #icp-touch-link-cop { display: none; }
</style>

<a href="/customer-preferences/edit?ie=UTF8&amp;ref_=footer_cop&amp;preferencesReturnUrl=%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dsr_nr_p_n_condition-type_1s" class="icp-button" id="icp-touch-link-cop">
  <span class="icp-currency-symbol">$</span><span class="icp-color-base">USD - U.S. Dollar</span>
</a>

<style type="text/css">
#icp-touch-link-country { display: none; }
</style>
<a href="/customer-preferences/country?ie=UTF8&amp;preferencesReturnUrl=%2Fs%3Fk%3Dbookstore%2Bamazon%26i%3Dstripbooks%26rh%3Dn%253A283155%252Cn%253A17%252Cp_n_condition-type%253A6461716011%26dc%26ds%3Dv1%253A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8%26hvadid%3D623182854892%26hvdev%3Dc%26hvlocint%3D9061323%26hvlocphy%3D1000060%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D6662995798799223789%26hvtargid%3Dkwd-13263126%26hydadcr%3D20698_13296112%26qid%3D1682200770%26rnid%3D6461714011%26tag%3Dgooghydr-20%26ref%3Dsr_nr_p_n_condition-type_1&amp;ref_=footer_icp_cp" aria-label="Choose a country/region for shopping." class="icp-button" id="icp-touch-link-country">
  <span class="icp-flag-3 icp-flag-3-us"></span><span class="icp-color-base">United States</span>
</a>
</div></span>
    
  </div>
  
  
  <div class="navFooterLine navFooterLinkLine navFooterDescLine" role="navigation" aria-label="More on Amazon">
    <table class="navFooterMoreOnAmazon" cellspacing="0" summary="More on Amazon">
      <tbody><tr>
<td class="navFooterDescItem"><a href="https://music.amazon.com?ref=dm_aff_amz_com" class="nav_a">Amazon Music<br><span class="navFooterDescText">Stream millions<br>of songs</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://advertising.amazon.com/?ref=footer_advtsing_amzn_com" class="nav_a">Amazon Advertising<br><span class="navFooterDescText">Find, attract, and<br>engage customers</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.6pm.com" class="nav_a">6pm<br><span class="navFooterDescText">Score deals<br>on fashion brands</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.abebooks.com" class="nav_a">AbeBooks<br><span class="navFooterDescText">Books, art<br>&amp; collectibles</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.acx.com/" class="nav_a">ACX <br><span class="navFooterDescText">Audiobook Publishing<br>Made Easy</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://sell.amazon.com/?ld=AZUSSOA-footer-aff&amp;ref_=footer_sell" class="nav_a">Sell on Amazon<br><span class="navFooterDescText">Start a Selling Account</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="/business?ref_=footer_retail_b2b" class="nav_a">Amazon Business<br><span class="navFooterDescText">Everything For<br>Your Business</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=230659011&amp;ref_=footer_amazonglobal" class="nav_a">AmazonGlobal<br><span class="navFooterDescText">Ship Orders<br>Internationally</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="/services?ref_=footer_services" class="nav_a">Home Services<br><span class="navFooterDescText">Experienced Pros<br>Happiness Guarantee</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://ignite.amazon.com/?ref=amazon_footer_ignite" class="nav_a">Amazon Ignite<br><span class="navFooterDescText">Sell your original<br>Digital Educational<br>Resources</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&amp;sc_campaign=amazonfooter" class="nav_a">Amazon Web Services<br><span class="navFooterDescText">Scalable Cloud<br>Computing Services</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.audible.com" class="nav_a">Audible<br><span class="navFooterDescText">Listen to Books &amp; Original<br>Audio Performances</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.bookdepository.com" class="nav_a">Book Depository<br><span class="navFooterDescText">Books With Free<br>Delivery Worldwide</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.boxofficemojo.com/?ref_=amzn_nav_ftr" class="nav_a">Box Office Mojo<br><span class="navFooterDescText">Find Movie<br>Box Office Data</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://www.comixology.com" class="nav_a">ComiXology<br><span class="navFooterDescText">Thousands of<br>Digital Comics</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.dpreview.com" class="nav_a">DPReview<br><span class="navFooterDescText">Digital<br>Photography</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.fabric.com" class="nav_a">Fabric<br><span class="navFooterDescText">Sewing, Quilting<br>&amp; Knitting</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.goodreads.com" class="nav_a">Goodreads<br><span class="navFooterDescText">Book reviews<br>&amp; recommendations</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.imdb.com" class="nav_a">IMDb<br><span class="navFooterDescText">Movies, TV<br>&amp; Celebrities</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://pro.imdb.com?ref_=amzn_nav_ftr" class="nav_a">IMDbPro<br><span class="navFooterDescText">Get Info Entertainment<br>Professionals Need</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://kdp.amazon.com" class="nav_a">Kindle Direct Publishing<br><span class="navFooterDescText">Indie Digital &amp; Print Publishing<br>Made Easy
</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://videodirect.amazon.com/home/landing" class="nav_a">Prime Video Direct<br><span class="navFooterDescText">Video Distribution<br>Made Easy</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.shopbop.com" class="nav_a">Shopbop<br><span class="navFooterDescText">Designer<br>Fashion Brands</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.woot.com/" class="nav_a">Woot!<br><span class="navFooterDescText">Deals and <br>Shenanigans</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.zappos.com" class="nav_a">Zappos<br><span class="navFooterDescText">Shoes &amp;<br>Clothing</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://ring.com" class="nav_a">Ring<br><span class="navFooterDescText">Smart Home<br>Security Systems
</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://eero.com/" class="nav_a">eero WiFi<br><span class="navFooterDescText">Stream 4K Video<br>in Every Room</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://blinkforhome.com/?ref=nav_footer" class="nav_a">Blink<br><span class="navFooterDescText">Smart Security<br>for Every Home
</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://shop.ring.com/pages/neighbors-app" class="nav_a">Neighbors App <br><span class="navFooterDescText"> Real-Time Crime<br>&amp; Safety Alerts
</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=14498690011&amp;ref_=amzn_nav_ftr_swa" class="nav_a">Amazon Subscription Boxes<br><span class="navFooterDescText">Top subscription boxes – right to your door</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem"><a href="https://www.pillpack.com" class="nav_a">PillPack<br><span class="navFooterDescText">Pharmacy Simplified</span></a></td><td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 3%"></td>
<td class="navFooterDescItem">&nbsp;</td>
</tr>

    </tbody></table>
  </div>

  
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine navFooterCopyright">
  <ul><li class="nav_first"><a href="/gp/help/customer/display.html?nodeId=508088&amp;ref_=footer_cou" class="nav_a">Conditions of Use</a></li><li><a href="/gp/help/customer/display.html?nodeId=468496&amp;ref_=footer_privacy" class="nav_a">Privacy Notice</a></li><li class="nav_last"><a href="/privacyprefs?ref_=footer_iba" class="nav_a">Your Ads Privacy Choices</a></li></ul><span>© 1996-2023, Amazon.com, Inc. or its affiliates</span>
</div>

  
</div>
<div id="sis_pixel_r2" aria-hidden="true" style="height:1px; position: absolute; left: -1000000px; top: -1000000px;"><iframe id="DAsis" src="//s.amazon-adsystem.com/iu3?d=amazon.com&amp;slot=navFooter&amp;a2=01017474feac463bb3c18412d5b3a32049eacc53d5e4bba0a49b8f69da232b2b58b3&amp;old_oo=0&amp;ts=1682200776572&amp;s=AVR3j5rKdrMUkiBDustVqB4HVS9mSieK-WX9If9M_4K-&amp;gdpr_consent=&amp;gdpr_consent_avl=&amp;cb=1682200776572" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" tabindex="-1" sandbox=""></iframe></div><script>(function(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.addEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=document.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="//s.amazon-adsystem.com/iu3?d=amazon.com&slot=navFooter&a2=01017474feac463bb3c18412d5b3a32049eacc53d5e4bba0a49b8f69da232b2b58b3&old_oo=0&ts=1682200776572&s=AVR3j5rKdrMUkiBDustVqB4HVS9mSieK-WX9If9M_4K-&gdpr_consent=&gdpr_consent_avl=&cb=1682200776572" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" tabindex="-1" sandbox></iframe>')},300)});</script>

  <!-- NAVYAAN FOOTER END -->

<!-- sp:end-feature:nav-footer -->
<!-- sp:feature:configured-sitewide-assets -->
<script src="https://m.media-amazon.com/images/I/01LFiHt-uUL.js?AUIClients/TMCJavascriptAssets" crossorigin="anonymous"></script>
<!-- sp:end-feature:configured-sitewide-assets -->
<!-- sp:feature:csm:body-close -->
<div id="be" style="display:none;visibility:hidden;"><form name="ue_backdetect" action="get"><input type="hidden" name="ue_back" value="2"></form>


<script type="text/javascript">
window.ue_ibe = (window.ue_ibe || 0) + 1;
if (window.ue_ibe === 1) {
(function(e,c){function h(b,a){f.push([b,a])}function g(b,a){if(b){var c=e.head||e.getElementsByTagName("head")[0]||e.documentElement,d=e.createElement("script");d.async="async";d.src=b;d.setAttribute("crossorigin","anonymous");a&&a.onerror&&(d.onerror=a.onerror);a&&a.onload&&(d.onload=a.onload);c.insertBefore(d,c.firstChild)}}function k(){ue.uels=g;for(var b=0;b<f.length;b++){var a=f[b];g(a[0],a[1])}ue.deffered=1}var f=[];c.ue&&(ue.uels=h,c.ue.attach&&c.ue.attach("load",k))})(document,window);


if (window.ue && window.ue.uels) {
        var cel_widgets = [ { "c":"celwidget" },{ "s":"#nav-swmslot > div", "id_gen":function(elem, index){ return 'nav_sitewide_msg'; } },{ "c":"s-result-item", "id_gen":function(elem, index){ return 'search_result_' + index ; } },{ "id":"leftNavContainer" },{ "id":"nav-upnav" },{ "id":"navbar" },{ "id":"hows-my-search" },{ "id":"rhf" },{ "id":"navFooter" },{ "s":".rush-component > .a-section.s-border-bottom > .s-widget-background", "id_gen":function(elem, index){ return 'osa_search_signpost'; } } ];

                ue.uels("https://images-na.ssl-images-amazon.com/images/I/31bJewCvY-L.js");
}
var ue_mbl=ue_csm.ue.exec(function(h,a){function s(c){b=c||{};a.AMZNPerformance=b;b.transition=b.transition||{};b.timing=b.timing||{};if(a.csa){var d;b.timing.transitionStart&&(d=b.timing.transitionStart);b.timing.processStart&&(d=b.timing.processStart);d&&(csa("PageTiming")("mark","nativeTransitionStart",d),csa("PageTiming")("mark","transitionStart",d))}h.ue.exec(t,"csm-android-check")()&&b.tags instanceof Array&&(c=-1!=b.tags.indexOf("usesAppStartTime")||b.transition.type?!b.transition.type&&-1<
b.tags.indexOf("usesAppStartTime")?"warm-start":void 0:"view-transition",c&&(b.transition.type=c));n=null;"reload"===e._nt&&h.ue_orct||"intrapage-transition"===e._nt?u(b):"undefined"===typeof e._nt&&f&&f.timing&&f.timing.navigationStart&&a.history&&"function"===typeof a.History&&"object"===typeof a.history&&a.history.length&&1!=a.history.length&&(b.timing.transitionStart=f.timing.navigationStart);p&&e.ssw(q,""+(b.timing.transitionStart||n||""));c=b.transition;d=e._nt?e._nt:void 0;c.subType=d;a.ue&&
a.ue.tag&&a.ue.tag("has-AMZNPerformance");e.isl&&a.uex&&a.uex("at","csm-timing");v()}function w(c){a.ue&&a.ue.count&&a.ue.count("csm-cordova-plugin-failed",1)}function t(){return a.cordova&&a.cordova.platformId&&"android"==a.cordova.platformId}function u(){if(p){var c=e.ssw(q),a=function(){},x=e.count||a,a=e.tag||a,k=b.timing.transitionStart,g=c&&!c.e&&c.val;n=c=g?+c.val:null;k&&g&&k>c?(x("csm.jumpStart.mtsDiff",k-c||0),a("csm-rld-mts-gt")):k&&g?a("csm-rld-mts-leq"):g?k||a("csm-rld-mts-no-new"):a("csm-rld-mts-no-old")}f&&
f.timing&&f.timing.navigationStart?b.timing.transitionStart=f.timing.navigationStart:delete b.timing.transitionStart}function v(){try{a.P.register("AMZNPerformance",function(){return b})}catch(c){}}function r(){if(!b)return"";ue_mbl.cnt=null;var c=b.timing,d=b.transition,d=["mts",l(c.transitionStart),"mps",l(c.processStart),"mtt",d.type,"mtst",d.subType,"mtlt",d.launchType];a.ue&&a.ue.tag&&(c.fr_ovr&&a.ue.tag("fr_ovr"),c.fcp_ovr&&a.ue.tag("fcp_ovr"),d.push("fr_ovr",l(c.fr_ovr),"fcp_ovr",l(c.fcp_ovr)));
for(var c="",e=0;e<d.length;e+=2){var f=d[e],g=d[e+1];"undefined"!==typeof g&&(c+="&"+f+"="+g)}return c}function l(a){if("undefined"!==typeof a&&"undefined"!==typeof m)return a-m}function y(a,d){b&&(m=d,b.timing.transitionStart=a,b.transition.type="view-transition",b.transition.subType="ajax-transition",b.transition.launchType="normal",ue_mbl.cnt=r)}var e=h.ue||{},m=h.ue_t0,q="csm-last-mts",p=1===h.ue_sswmts,n,f=a.performance,b;if(a.P&&a.P.when&&a.P.register)return 1===a.ue_fnt&&(m=a.aPageStart||
h.ue_t0),a.P.when("CSMPlugin").execute(function(a){a.buildAMZNPerformance&&a.buildAMZNPerformance({successCallback:s,failCallback:w})}),{cnt:r,ajax:y}},"mobile-timing")(ue_csm,ue_csm.window);

(function(d){d._uess=function(){var a="";screen&&screen.width&&screen.height&&(a+="&sw="+screen.width+"&sh="+screen.height);var b=function(a){var b=document.documentElement["client"+a];return"CSS1Compat"===document.compatMode&&b||document.body["client"+a]||b},c=b("Width"),b=b("Height");c&&b&&(a+="&vw="+c+"&vh="+b);return a}})(ue_csm);

(function(a){function c(a){d("log",a)}var d=csa("Errors",{producerId:"csa"});a.ue_err.buffer&&d&&(a.ue_err.buffer.forEach(c),a.ue_err.buffer.push=c);var b=document.ue_backdetect;b&&b.ue_back&&a.ue&&(a.ue.bfini=b.ue_back.value);a.uet&&a.uet("be");a.onLdEnd&&(window.addEventListener?window.addEventListener("load",a.onLdEnd,!1):window.attachEvent&&window.attachEvent("onload",a.onLdEnd));a.ueh&&a.ueh(0,window,"load",a.onLd,1);a.ue&&a.ue.tag&&(a.ue_furl?(b=a.ue_furl.replace(/\./g,"-"),a.ue.tag(b)):a.ue.tag("nofls"))})(ue_csm);

(function(g,h){function d(a,d){var b={};if(!e||!f)try{var c=h.sessionStorage;c?a&&("undefined"!==typeof d?c.setItem(a,d):b.val=c.getItem(a)):f=1}catch(g){e=1}e&&(b.e=1);return b}var b=g.ue||{},a="",f,e,c,a=d("csmtid");f?a="NA":a.e?a="ET":(a=a.val,a||(a=b.oid||"NI",d("csmtid",a)),c=d(b.oid),c.e||(c.val=c.val||0,d(b.oid,c.val+1)),b.ssw=d);b.tabid=a})(ue_csm,ue_csm.window);

ue_csm.ue.exec(function(e,f){var a=e.ue||{},b=a._wlo,d;if(a.ssw){d=a.ssw("CSM_previousURL").val;var c=f.location,b=b?b:c&&c.href?c.href.split("#")[0]:void 0;c=(b||"")===a.ssw("CSM_previousURL").val;!c&&b&&a.ssw("CSM_previousURL",b);d=c?"reload":d?"intrapage-transition":"first-view"}else d="unknown";a._nt=d},"NavTypeModule")(ue_csm,window);
ue_csm.ue.exec(function(c,a){function g(a){a.run(function(e){d.tag("csm-feature-"+a.name+":"+e);d.isl&&c.uex("at")})}if(a.addEventListener)for(var d=c.ue||{},f=[{name:"touch-enabled",run:function(b){var e=function(){a.removeEventListener("touchstart",c,!0);a.removeEventListener("mousemove",d,!0)},c=function(){b("true");e()},d=function(){b("false");e()};a.addEventListener("touchstart",c,!0);a.addEventListener("mousemove",d,!0)}}],b=0;b<f.length;b++)g(f[b])},"csm-features")(ue_csm,window);


(function(a,e){function c(a){d("recordCounter",a.c,a.v)}var b=e.images,d=csa("Metrics",{producerId:"csa"});b&&b.length&&a.ue.count("totalImages",b.length);a.ue.cv.buffer&&d&&(a.ue.cv.buffer.forEach(c),a.ue.cv.buffer.push=c)})(ue_csm,document);
(function(b){function c(){var d=[];a.log&&a.log.isStub&&a.log.replay(function(a){e(d,a)});a.clog&&a.clog.isStub&&a.clog.replay(function(a){e(d,a)});d.length&&(a._flhs+=1,n(d),p(d))}function g(){a.log&&a.log.isStub&&(a.onflush&&a.onflush.replay&&a.onflush.replay(function(a){a[0]()}),a.onunload&&a.onunload.replay&&a.onunload.replay(function(a){a[0]()}),c())}function e(d,b){var c=b[1],f=b[0],e={};a._lpn[c]=(a._lpn[c]||0)+1;e[c]=f;d.push(e)}function n(b){q&&(a._lpn.csm=(a._lpn.csm||0)+1,b.push({csm:{k:"chk",
f:a._flhs,l:a._lpn,s:"inln"}}))}function p(a){if(h)a=k(a),b.navigator.sendBeacon(l,a);else{a=k(a);var c=new b[f];c.open("POST",l,!0);c.setRequestHeader&&c.setRequestHeader("Content-type","text/plain");c.send(a)}}function k(a){return JSON.stringify({rid:b.ue_id,sid:b.ue_sid,mid:b.ue_mid,mkt:b.ue_mkt,sn:b.ue_sn,reqs:a})}var f="XMLHttpRequest",q=1===b.ue_ddq,a=b.ue,r=b[f]&&"withCredentials"in new b[f],h=b.navigator&&b.navigator.sendBeacon,l="//"+b.ue_furl+"/1/batch/1/OE/",m=b.ue_fci_ft||5E3;a&&(r||h)&&
(a._flhs=a._flhs||0,a._lpn=a._lpn||{},a.attach&&(a.attach("beforeunload",a.exec(g,"fcli-bfu")),a.attach("pagehide",a.exec(g,"fcli-ph"))),m&&b.setTimeout(a.exec(c,"fcli-t"),m),a._ffci=a.exec(c))})(window);


(function(k,c){function l(a,b){return a.filter(function(a){return a.initiatorType==b})}function f(a,c){if(b.t[a]){var g=b.t[a]-b._t0,e=c.filter(function(a){return 0!==a.responseEnd&&m(a)<g}),f=l(e,"script"),h=l(e,"link"),k=l(e,"img"),n=e.map(function(a){return a.name.split("/")[2]}).filter(function(a,b,c){return a&&c.lastIndexOf(a)==b}),q=e.filter(function(a){return a.duration<p}),s=g-Math.max.apply(null,e.map(m))<r|0;"af"==a&&(b._afjs=f.length);return a+":"+[e[d],f[d],h[d],k[d],n[d],q[d],s].join("-")}}
function m(a){return a.responseEnd-(b._t0-c.timing.navigationStart)}function n(){var a=c[h]("resource"),d=f("cf",a),g=f("af",a),a=f("ld",a);delete b._rt;b._ld=b.t.ld-b._t0;b._art&&b._art();return[d,g,a].join("_")}var p=20,r=50,d="length",b=k.ue,h="getEntriesByType";b._rre=m;b._rt=c&&c.timing&&c[h]&&n})(ue_csm,window.performance);


(function(c,d){var b=c.ue,a=d.navigator;b&&b.tag&&a&&(a=a.connection||a.mozConnection||a.webkitConnection)&&a.type&&b.tag("netInfo:"+a.type)})(ue_csm,window);


(function(c,d){function h(a,b){for(var c=[],d=0;d<a.length;d++){var e=a[d],f=b.encode(e);if(e[k]){var g=b.metaSep,e=e[k],l=b.metaPairSep,h=[],m=void 0;for(m in e)e.hasOwnProperty(m)&&h.push(m+"="+e[m]);e=h.join(l);f+=g+e}c.push(f)}return c.join(b.resourceSep)}function s(a){var b=a[k]=a[k]||{};b[t]||(b[t]=c.ue_mid);b[u]||(b[u]=c.ue_sid);b[f]||(b[f]=c.ue_id);b.csm=1;a="//"+c.ue_furl+"/1/"+a[v]+"/1/OP/"+a[w]+"/"+a[x]+"/"+h([a],y);if(n)try{n.call(d[p],a)}catch(g){c.ue.sbf=1,(new Image).src=a}else(new Image).src=
a}function q(){g&&g.isStub&&g.replay(function(a,b,c){a=a[0];b=a[k]=a[k]||{};b[f]=b[f]||c;s(a)});l.impression=s;g=null}if(!(1<c.ueinit)){var k="metadata",x="impressionType",v="foresterChannel",w="programGroup",t="marketplaceId",u="session",f="requestId",p="navigator",l=c.ue||{},n=d[p]&&d[p].sendBeacon,r=function(a,b,c,d){return{encode:d,resourceSep:a,metaSep:b,metaPairSep:c}},y=r("","?","&",function(a){return h(a.impressionData,z)}),z=r("/",":",",",function(a){return a.featureName+":"+h(a.resources,
A)}),A=r(",","@","|",function(a){return a.id}),g=l.impression;n?q():(l.attach("load",q),l.attach("beforeunload",q));try{d.P&&d.P.register&&d.P.register("impression-client",function(){})}catch(B){c.ueLogError(B,{logLevel:"WARN"})}}})(ue_csm,window);



var ue_pty = "Search";

var ue_spty = "List";



var ue_adb = 4;
var ue_adb_rtla = 1;
ue_csm.ue.exec(function(y,a){function t(){if(d&&f){var a;a:{try{a=d.getItem(g);break a}catch(c){}a=void 0}if(a)return b=a,!0}return!1}function u(){if(a.fetch)fetch(m).then(function(a){if(!a.ok)throw Error(a.statusText);return a.text?a.text():null}).then(function(b){b?(-1<b.indexOf("window.ue_adb_chk = 1")&&(a.ue_adb_chk=1),n()):h()})["catch"](h);else e.uels(m,{onerror:h,onload:n})}function h(){b=k;l();if(f)try{d.setItem(g,b)}catch(a){}}function n(){b=1===a.ue_adb_chk?p:k;l();if(f)try{d.setItem(g,
b)}catch(c){}}function q(){a.ue_adb_rtla&&c&&0<c.ec&&!1===r&&(c.elh=null,ueLogError({m:"Hit Info",fromOnError:1},{logLevel:"INFO",adb:b}),r=!0)}function l(){e.tag(b);e.isl&&a.uex&&uex("at",b);s&&s.updateCsmHit("adb",b);c&&0<c.ec?q():a.ue_adb_rtla&&c&&(c.elh=q)}function v(){return b}if(a.ue_adb){a.ue_fadb=a.ue_fadb||10;var e=a.ue,k="adblk_yes",p="adblk_no",m="https://m.media-amazon.com/images/G/01/csm/showads.v2.js?ad_size=_Ad300x250_&adstype=-sponsored-links-&advertiser=_googleads_",b="adblk_unk",
d;a:{try{d=a.localStorage;break a}catch(z){}d=void 0}var g="csm:adb",c=a.ue_err,s=e.cookie,f=void 0!==a.localStorage,w=Math.random()>1-1/a.ue_fadb,r=!1,x=t();w||!x?u():l();a.ue_isAdb=v;a.ue_isAdb.unk="adblk_unk";a.ue_isAdb.no=p;a.ue_isAdb.yes=k}},"adb")(document,window);




(function(c,l,m){function h(a){if(a)try{if(a.id)return"//*[@id='"+a.id+"']";var b,d=1,e;for(e=a.previousSibling;e;e=e.previousSibling)e.nodeName===a.nodeName&&(d+=1);b=d;var c=a.nodeName;1!==b&&(c+="["+b+"]");a.parentNode&&(c=h(a.parentNode)+"/"+c);return c}catch(f){return"DETACHED"}}function f(a){if(a&&a.getAttribute)return a.getAttribute(k)?a.getAttribute(k):f(a.parentElement)}var k="data-cel-widget",g=!1,d=[];(c.ue||{}).isBF=function(){try{var a=JSON.parse(localStorage["csm-bf"]||"[]"),b=0<=a.indexOf(c.ue_id);
a.unshift(c.ue_id);a=a.slice(0,20);localStorage["csm-bf"]=JSON.stringify(a);return b}catch(d){return!1}}();c.ue_utils={getXPath:h,getFirstAscendingWidget:function(a,b){c.ue_cel&&c.ue_fem?!0===g?b(f(a)):d.push({element:a,callback:b}):b()},notifyWidgetsLabeled:function(){if(!1===g){g=!0;for(var a=f,b=0;b<d.length;b++)if(d[b].hasOwnProperty("callback")&&d[b].hasOwnProperty("element")){var c=d[b].callback,e=d[b].element;"function"===typeof c&&"function"===typeof a&&c(a(e))}d=null}},extractStringValue:function(a){if("string"===
typeof a)return a}}})(ue_csm,window,document);


(function(a){a.ue_cel||(a.ue_cel=function(){function f(a,c){c?c.r=v:c={r:v,c:1};!ue_csm.ue_sclog&&c.clog&&d.clog?d.clog(a,c.ns||q,c):c.glog&&d.glog?d.glog(a,c.ns||q,c):d.log(a,c.ns||q,c)}function m(a,d){"function"===typeof g&&g("log",{schemaId:s+".RdCSI.1",eventType:a,clientData:d},{ent:{page:["requestId"]}})}function c(){var a=n.length;if(0<a){for(var c=[],b=0;b<a;b++){var F=n[b].api;F.ready()?(F.on({ts:d.d,ns:q}),e.push(n[b]),f({k:"mso",n:n[b].name,t:d.d()})):c.push(n[b])}n=c}}function h(){if(!h.executed){for(var a=
0;a<e.length;a++)e[a].api.off&&e[a].api.off({ts:d.d,ns:q});A();f({k:"eod",t0:d.t0,t:d.d()},{c:1,il:1});h.executed=1;for(a=0;a<e.length;a++)n.push(e[a]);e=[];b(t);b(x)}}function A(a){f({k:"hrt",t:d.d()},{c:1,il:1,n:a});l=Math.min(w,r*l);y()}function y(){b(x);x=k(function(){A(!0)},l)}function u(){h.executed||A()}var p=a.window,k=p.setTimeout,b=p.clearTimeout,r=1.5,w=p.ue_cel_max_hrt||3E4,s="robotdetection",n=[],e=[],q=a.ue_cel_ns||"cel",t,x,d=a.ue,E=a.uet,B=a.uex,v=d.rid,C=p.csa,g,l=p.ue_cel_hrt_int||
3E3,z=p.requestAnimationFrame||function(a){a()};!a.ue_cel_lclia&&C&&(g=C("Events",{producerId:s}));if(d.isBF)f({k:"bft",t:d.d()});else{"function"==typeof E&&E("bb","csmCELLSframework",{wb:1});k(c,0);d.onunload(h);if(d.onflush)d.onflush(u);t=k(h,6E5);y();"function"==typeof B&&B("ld","csmCELLSframework",{wb:1});return{registerModule:function(a,b){n.push({name:a,api:b});f({k:"mrg",n:a,t:d.d()});c()},reset:function(a){f({k:"rst",t0:d.t0,t:d.d()});n=n.concat(e);e=[];for(var r=n.length,g=0;g<r;g++)n[g].api.off(),
n[g].api.reset();v=a||d.rid;c();b(t);t=k(h,6E5);h.executed=0},timeout:function(a,d){return k(function(){z(function(){h.executed||a()})},d)},log:f,csaEventLog:m,off:h}}}())})(ue_csm);
(function(a){a.ue_pdm||!a.ue_cel||a.ue.isBF||(a.ue_pdm=function(){function f(){try{var d=b.screen;if(d){var c={w:d.width,aw:d.availWidth,h:d.height,ah:d.availHeight,cd:d.colorDepth,pd:d.pixelDepth};e&&e.w===c.w&&e.h===c.h&&e.aw===c.aw&&e.ah===c.ah&&e.pd===c.pd&&e.cd===c.cd||(e=c,e.t=s(),e.k="sci",E(e),!C&&g&&l("sci",{h:(e.h||"0")+""}))}var k=r.body||{},h=r.documentElement||{},m={w:Math.max(k.scrollWidth||0,k.offsetWidth||0,h.clientWidth||0,h.scrollWidth||0,h.offsetWidth||0),h:Math.max(k.scrollHeight||
0,k.offsetHeight||0,h.clientHeight||0,h.scrollHeight||0,h.offsetHeight||0)};q&&q.w===m.w&&q.h===m.h||(q=m,q.t=s(),q.k="doi",E(q));w=a.ue_cel.timeout(f,n);x+=1}catch(p){b.ueLogError&&ueLogError(p,{attribution:"csm-cel-page-module",logLevel:"WARN"})}}function m(){u("ebl","default",!1)}function c(){u("efo","default",!0)}function h(){u("ebl","app",!1)}function A(){u("efo","app",!0)}function y(){b.setTimeout(function(){r[H]?u("ebl","pageviz",!1):u("efo","pageviz",!0)},0)}function u(a,d,c){t!==c&&(E({k:a,
t:s(),s:d},{ff:!0===c?0:1}),!C&&g&&l(a,{t:(s()||"0")+"",s:d}));t=c}function p(){d.attach&&(z&&d.attach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.addEventListener&&(a.addEventListener("appPause",h),a.addEventListener("appResume",A))}),d.attach("blur",m,b),d.attach("focus",c,b))}function k(){d.detach&&(z&&d.detach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.removeEventListener&&(a.removeEventListener("appPause",h),a.removeEventListener("appResume",A))}),d.detach("blur",m,b),d.detach("focus",
c,b))}var b=a.window,r=a.document,w,s,n,e,q,t=null,x=0,d=a.ue,E=a.ue_cel.log,B=a.uet,v=a.uex,C=a.ue_cel_lclia,g=b.csa,l=a.ue_cel.csaEventLog,z=!!d.pageViz,D=z&&d.pageViz.event,H=z&&d.pageViz.propHid,I=b.P&&b.P.when;"function"==typeof B&&B("bb","csmCELLSpdm",{wb:1});return{on:function(a){n=a.timespan||500;s=a.ts;p();a=b.location;E({k:"pmd",o:a.origin,p:a.pathname,t:s()});f();"function"==typeof v&&v("ld","csmCELLSpdm",{wb:1})},off:function(a){clearTimeout(w);k();d.count&&d.count("cel.PDM.TotalExecutions",
x)},ready:function(){return r.body&&a.ue_cel&&a.ue_cel.log},reset:function(){e=q=null}}}(),a.ue_cel&&a.ue_cel.registerModule("page module",a.ue_pdm))})(ue_csm);
(function(a){a.ue_vpm||!a.ue_cel||a.ue.isBF||(a.ue_vpm=function(){function f(){var a=y(),b={w:k.innerWidth,h:k.innerHeight,x:k.pageXOffset,y:k.pageYOffset};c&&c.w==b.w&&c.h==b.h&&c.x==b.x&&c.y==b.y||(b.t=a,b.k="vpi",c=b,r(c,{clog:1}),!q&&t&&x("vpi",{t:(c.t||"0")+"",h:(c.h||"0")+"",y:(c.y||"0")+"",w:(c.w||"0")+"",x:(c.x||"0")+""}));h=0;u=y()-a;p+=1}function m(){h||(h=a.ue_cel.timeout(f,A))}var c,h,A,y,u=0,p=0,k=a.window,b=a.ue,r=a.ue_cel.log,w=a.uet,s=a.uex,n=b.attach,e=b.detach,q=a.ue_cel_lclia,t=
k.csa,x=a.ue_cel.csaEventLog;"function"==typeof w&&w("bb","csmCELLSvpm",{wb:1});return{on:function(a){y=a.ts;A=a.timespan||100;f();n&&(n("scroll",m),n("resize",m));"function"==typeof s&&s("ld","csmCELLSvpm",{wb:1})},off:function(a){clearTimeout(h);e&&(e("scroll",m),e("resize",m));b.count&&(b.count("cel.VPI.TotalExecutions",p),b.count("cel.VPI.TotalExecutionTime",u),b.count("cel.VPI.AverageExecutionTime",u/p))},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){c=void 0},getVpi:function(){return c}}}(),
a.ue_cel&&a.ue_cel.registerModule("viewport module",a.ue_vpm))})(ue_csm);
(function(a){if(!a.ue_fem&&a.ue_cel&&a.ue_utils){var f=a.ue||{},m=a.window,c=m.document;!f.isBF&&!a.ue_fem&&c.querySelector&&m.getComputedStyle&&[].forEach&&(a.ue_fem=function(){function h(a,d){return a>d?3>a-d:3>d-a}function A(a,d){var c=m.pageXOffset,b=m.pageYOffset,k;a:{try{if(a){var g=a.getBoundingClientRect(),e,r=0===a.offsetWidth&&0===a.offsetHeight;c:{for(var f=a.parentNode,w=g.left||0,n=g.top||0,p=g.width||0,q=g.height||0;f&&f!==document.body;){var l;d:{try{var s=void 0;if(f)var G=f.getBoundingClientRect(),
s={x:G.left||0,y:G.top||0,w:G.width||0,h:G.height||0};else s=void 0;l=s;break d}catch(v){}l=void 0}var t=window.getComputedStyle(f),u="hidden"===t.overflow,y=u||"hidden"===t.overflowX,z=u||"hidden"===t.overflowY,J=n+q-1<l.y+1||n+1>l.y+l.h-1;if((w+p-1<l.x+1||w+1>l.x+l.w-1)&&y||J&&z){e=!0;break c}f=f.parentNode}e=!1}k={x:g.left+c||0,y:g.top+b||0,w:g.width||0,h:g.height||0,d:(r||e)|0}}else k=void 0;break a}catch(A){}k=void 0}if(k&&!a.cel_b)a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,
x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi",cl:a.className},{clog:1});else{if(c=k)c=a.cel_b,b=k,c=b.d===c.d&&1===b.d?!1:!(h(c.x,b.x)&&h(c.y,b.y)&&h(c.w,b.w)&&h(c.h,b.h)&&c.d===b.d);c&&(a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi"},{clog:1}))}}function y(b,g){var h;h=b.c?c.getElementsByClassName(b.c):b.id?[c.getElementById(b.id)]:c.querySelectorAll(b.s);b.w=[];for(var f=0;f<h.length;f++){var e=h[f];if(e){if(!e.getAttribute(x)){var r=e.getAttribute("cel_widget_id")||
(b.id_gen||v)(e,f)||e.id;e.setAttribute(x,r)}b.w.push(e);k(Q,e,g)}}!1===B&&(E++,E===d.length&&(B=!0,a.ue_utils.notifyWidgetsLabeled()))}function u(a,c){g.contains(a)||C({n:a.getAttribute(x),t:c,k:"ewd"},{clog:1})}function p(a){K.length&&ue_cel.timeout(function(){if(q){for(var c=R(),d=!1;R()-c<e&&!d;){for(d=S;0<d--&&0<K.length;){var b=K.shift();T[b.type](b.elem,b.time)}d=0===K.length}U++;p(a)}},0)}function k(a,c,d){K.push({type:a,elem:c,time:d})}function b(a,c){for(var b=0;b<d.length;b++)for(var e=
d[b].w||[],g=0;g<e.length;g++)k(a,e[g],c)}function r(){M||(M=a.ue_cel.timeout(function(){M=null;var c=t();b(W,c);for(var g=0;g<d.length;g++)k(X,d[g],c);0===d.length&&!1===B&&(B=!0,a.ue_utils.notifyWidgetsLabeled());p(c)},n))}function w(){M||N||(N=a.ue_cel.timeout(function(){N=null;var a=t();b(Q,a);p(a)},n))}function s(){return z&&D&&g&&g.contains&&g.getBoundingClientRect&&t}var n=50,e=4.5,q=!1,t,x="data-cel-widget",d=[],E=0,B=!1,v=function(){},C=a.ue_cel.log,g,l,z,D,H=m.MutationObserver||m.WebKitMutationObserver||
m.MozMutationObserver,I=!!H,F,G,O="DOMAttrModified",L="DOMNodeInserted",J="DOMNodeRemoved",N,M,K=[],U=0,S=null,W="removedWidget",X="updateWidgets",Q="processWidget",T,V=m.performance||{},R=V.now&&function(){return V.now()}||function(){return Date.now()};"function"==typeof uet&&uet("bb","csmCELLSfem",{wb:1});return{on:function(b){function e(){if(s()){T={removedWidget:u,updateWidgets:y,processWidget:A};if(I){var a={attributes:!0,subtree:!0};F=new H(w);G=new H(r);F.observe(g,a);G.observe(g,{childList:!0,
subtree:!0});G.observe(l,a)}else z.call(g,O,w),z.call(g,L,r),z.call(g,J,r),z.call(l,L,w),z.call(l,J,w);r()}}g=c.body;l=c.head;z=g.addEventListener;D=g.removeEventListener;t=b.ts;d=a.cel_widgets||[];S=b.bs||5;f.deffered?e():f.attach&&f.attach("load",e);"function"==typeof uex&&uex("ld","csmCELLSfem",{wb:1});q=!0},off:function(){s()&&(G&&(G.disconnect(),G=null),F&&(F.disconnect(),F=null),D.call(g,O,w),D.call(g,L,r),D.call(g,J,r),D.call(l,L,w),D.call(l,J,w));f.count&&f.count("cel.widgets.batchesProcessed",
U);q=!1},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){d=a.cel_widgets||[]}}}(),a.ue_cel&&a.ue_fem&&a.ue_cel.registerModule("features module",a.ue_fem))}})(ue_csm);
(function(a){!a.ue_mcm&&a.ue_cel&&a.ue_utils&&!a.ue.isBF&&(a.ue_mcm=function(){function f(a,b){var h=a.srcElement||a.target||{},f={k:m,w:(b||{}).ow||(A.body||{}).scrollWidth,h:(b||{}).oh||(A.body||{}).scrollHeight,t:(b||{}).ots||c(),x:a.pageX,y:a.pageY,p:p.getXPath(h),n:h.nodeName};y&&"function"===typeof y.now&&a.timeStamp&&(f.dt=(b||{}).odt||y.now()-a.timeStamp,f.dt=parseFloat(f.dt.toFixed(2)));a.button&&(f.b=a.button);h.href&&(f.r=p.extractStringValue(h.href));h.id&&(f.i=h.id);h.className&&h.className.split&&
(f.c=h.className.split(/\s+/));u(f,{c:1})}var m="mcm",c,h=a.window,A=h.document,y=h.performance,u=a.ue_cel.log,p=a.ue_utils;return{on:function(k){c=k.ts;a.ue_cel_stub&&a.ue_cel_stub.replayModule(m,f);h.addEventListener&&h.addEventListener("mousedown",f,!0)},off:function(a){h.addEventListener&&h.removeEventListener("mousedown",f,!0)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){}}}(),a.ue_cel&&a.ue_cel.registerModule("mouse click module",a.ue_mcm))})(ue_csm);
(function(a){a.ue_mmm||!a.ue_cel||a.ue.isBF||(a.ue_mmm=function(f){function m(a,c){var b={x:a.pageX||a.x||0,y:a.pageY||a.y||0,t:p()};!c&&l&&(b.t-l.t<A||b.x==l.x&&b.y==l.y)||(l=b,v.push(b))}function c(){if(v.length){E=F.now();for(var a=0;a<v.length;a++){var c=v[a],b=a;z=v[g];D=c;var e=void 0;if(!(e=2>b)){e=void 0;a:if(v[b].t-v[b-1].t>h)e=0;else{for(e=g+1;e<b;e++){var f=z,k=D,l=v[e];H=(k.x-f.x)*(f.y-l.y)-(f.x-l.x)*(k.y-f.y);if(H*H/((k.x-f.x)*(k.x-f.x)+(k.y-f.y)*(k.y-f.y))>y){e=0;break a}}e=1}e=!e}(I=
e)?g=b-1:C.pop();C.push(c)}B=F.now()-E;q=Math.min(q,B);t=Math.max(t,B);x=(x*d+B)/(d+1);d+=1;n({k:u,e:C,min:Math.floor(1E3*q),max:Math.floor(1E3*t),avg:Math.floor(1E3*x)},{c:1});v=[];C=[];g=0}}var h=100,A=20,y=25,u="mmm1",p,k,b=a.window,r=b.document,w=b.setInterval,s=a.ue,n=a.ue_cel.log,e,q=1E3,t=0,x=0,d=0,E,B,v=[],C=[],g=0,l,z,D,H,I,F=f&&f.now&&f||Date.now&&Date||{now:function(){return(new Date).getTime()}};return{on:function(a){p=a.ts;k=a.ns;s.attach&&s.attach("mousemove",m,r);e=w(c,3E3)},off:function(a){k&&
(l&&m(l,!0),c());clearInterval(e);s.detach&&s.detach("mousemove",m,r)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){v=[];C=[];g=0;l=null}}}(window.performance),a.ue_cel&&a.ue_cel.registerModule("mouse move module",a.ue_mmm))})(ue_csm);



ue_csm.ue.exec(function(b,c){var e=function(){},f=function(){return{send:function(b,d){if(d&&b){var a;if(c.XDomainRequest)a=new XDomainRequest,a.onerror=e,a.ontimeout=e,a.onprogress=e,a.onload=e,a.timeout=0;else if(c.XMLHttpRequest){if(a=new XMLHttpRequest,!("withCredentials"in a))throw"";}else a=void 0;if(!a)throw"";a.open("POST",b,!0);a.setRequestHeader&&a.setRequestHeader("Content-type","text/plain");a.send(d)}},isSupported:!0}}(),g=function(){return{send:function(c,d){if(c&&d)if(navigator.sendBeacon(c,
d))b.ue_sbuimp&&b.ue&&b.ue.ssw&&b.ue.ssw("eelsts","scs");else throw"";},isSupported:!!navigator.sendBeacon&&!(c.cordova&&c.cordova.platformId&&"ios"==c.cordova.platformId)}}();b.ue._ajx=f;b.ue._sBcn=g},"Transportation-clients")(ue_csm,window);
ue_csm.ue.exec(function(b,k){function B(){for(var a=0;a<arguments.length;a++){var c=arguments[a];try{var g;if(c.isSupported){var f=u.buildPayload(l,e);g=c.send(K,f)}else throw dummyException;return g}catch(d){}}a={m:"All supported clients failed",attribution:"CSMSushiClient_TRANSPORTATION_FAIL",f:"sushi-client.js",logLevel:"ERROR"};C(a,k.ue_err_chan||"jserr");b.ue_err.buffer&&b.ue_err.buffer.push(a)}function m(){if(e.length){for(var a=0;a<n.length;a++)n[a]();B(d._sBcn||{},d._ajx||{});e=[];h={};l=
{};v=w=r=x=0}}function L(){var a=new Date,c=function(a){return 10>a?"0"+a:a};return Date.prototype.toISOString?a.toISOString():a.getUTCFullYear()+"-"+c(a.getUTCMonth()+1)+"-"+c(a.getUTCDate())+"T"+c(a.getUTCHours())+":"+c(a.getUTCMinutes())+":"+c(a.getUTCSeconds())+"."+String((a.getUTCMilliseconds()/1E3).toFixed(3)).slice(2,5)+"Z"}function y(a){try{return JSON.stringify(a)}catch(c){}return null}function D(a,c,g,f){var q=!1;f=f||{};s++;if(s==E){var p={m:"Max number of Sushi Logs exceeded",f:"sushi-client.js",
logLevel:"ERROR",attribution:"CSMSushiClient_MAX_CALLS"};C(p,k.ue_err_chan||"jserr");b.ue_err.buffer&&b.ue_err.buffer.push(p)}if(p=!(s>=E))(p=a&&-1<a.constructor.toString().indexOf("Object")&&c&&-1<c.constructor.toString().indexOf("String")&&g&&-1<g.constructor.toString().indexOf("String"))||M++;p&&(d.count&&d.count("Event:"+g,1),a.producerId=a.producerId||c,a.schemaId=a.schemaId||g,a.timestamp=L(),c=Date.now?Date.now():+new Date,g=Math.random().toString().substring(2,12),a.messageId=b.ue_id+"-"+
c+"-"+g,f&&!f.ssd&&(a.sessionId=a.sessionId||b.ue_sid,a.requestId=a.requestId||b.ue_id,a.obfuscatedMarketplaceId=a.obfuscatedMarketplaceId||b.ue_mid),(c=y(a))?(c=c.length,(e.length==N||r+c>O)&&m(),r+=c,a={data:u.compressEvent(a)},e.push(a),(f||{}).n?0===F?m():v||(v=k.setTimeout(m,F)):w||(w=k.setTimeout(m,P)),q=!0):q=!1);!q&&b.ue_int&&console.error("Invalid JS Nexus API call");return q}function G(){if(!H){for(var a=0;a<z.length;a++)z[a]();for(a=0;a<n.length;a++)n[a]();e.length&&(b.ue_sbuimp&&b.ue&&
b.ue.ssw&&(a=y({dct:l,evt:e}),b.ue.ssw("eeldata",a),b.ue.ssw("eelsts","unk")),B(d._sBcn||{}));H=!0}}function I(a){z.push(a)}function J(a){n.push(a)}var E=1E3,N=499,O=524288,t=function(){},d=b.ue||{},C=d.log||t,Q=b.uex||t;(b.uet||t)("bb","ue_sushi_v1",{wb:1});var K=b.ue_surl||"https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.gamma",R=["messageId","timestamp"],A="#",e=[],h={},l={},r=0,x=0,M=0,s=0,z=[],n=[],H=!1,v,w,F=void 0===b.ue_hpsi?1E3:b.ue_hpsi,P=void 0===b.ue_lpsi?1E4:b.ue_lpsi,
u=function(){function a(a){h[a]=A+x++;l[h[a]]=a;return h[a]}function c(b){if(!(b instanceof Function)){if(b instanceof Array){for(var f=[],d=b.length,e=0;e<d;e++)f[e]=c(b[e]);return f}if(b instanceof Object){f={};for(d in b)b.hasOwnProperty(d)&&(f[h[d]?h[d]:a(d)]=-1===R.indexOf(d)?c(b[d]):b[d]);return f}return"string"===typeof b&&(b.length>(A+x).length||b.charAt(0)===A)?h[b]?h[b]:a(b):b}}return{compressEvent:c,buildPayload:function(){return y({cs:{dct:l},events:e})}}}();(function(){if(d.event&&d.event.isStub){if(b.ue_sbuimp&&
b.ue&&b.ue.ssw){var a=b.ue.ssw("eelsts").val;if(a&&"unk"===a&&(a=b.ue.ssw("eeldata").val)){var c;a:{try{c=JSON.parse(a);break a}catch(g){}c=null}c&&c.evt instanceof Array&&c.dct instanceof Object&&(e=c.evt,l=c.dct,e&&l&&(m(),b.ue.ssw("eeldata","{}"),b.ue.ssw("eelsts","scs")))}}d.event.replay(function(a){a[3]=a[3]||{};a[3].n=1;D.apply(this,a)});d.onSushiUnload.replay(function(a){I(a[0])});d.onSushiFlush.replay(function(a){J(a[0])})}})();d.attach("beforeunload",G);d.attach("pagehide",G);d._cmps=u;d.event=
D;d.event.reset=function(){s=0};d.onSushiUnload=I;d.onSushiFlush=J;try{k.P&&k.P.register&&k.P.register("sushi-client",t)}catch(S){b.ueLogError(S,{logLevel:"WARN"})}Q("ld","ue_sushi_v1",{wb:1})},"Nxs-JS-Client")(ue_csm,window);


ue_csm.ue_unrt = 1500;
(function(d,b,t){function u(a,g){var c=a.srcElement||a.target||{},b={k:v,t:g.t,dt:g.dt,x:a.pageX,y:a.pageY,p:e.getXPath(c),n:c.nodeName};a.button&&(b.b=a.button);c.type&&(b.ty=c.type);c.href&&(b.r=e.extractStringValue(c.href));c.id&&(b.i=c.id);c.className&&c.className.split&&(b.c=c.className.split(/\s+/));h+=1;e.getFirstAscendingWidget(c,function(a){b.wd=a;d.ue.log(b,r)})}function w(a){if(!x(a.srcElement||a.target)){m+=1;n=!0;var g=f=d.ue.d(),c;p&&"function"===typeof p.now&&a.timeStamp&&(c=p.now()-
a.timeStamp,c=parseFloat(c.toFixed(2)));s=b.setTimeout(function(){u(a,{t:g,dt:c})},y)}}function z(a){if(a){var b=a.filter(A);a.length!==b.length&&(q=!0,k=d.ue.d(),n&&q&&(k&&f&&d.ue.log({k:B,t:f,m:Math.abs(k-f)},r),l(),q=!1,k=0))}}function A(a){if(!a)return!1;var b="characterData"===a.type?a.target.parentElement:a.target;if(!b||!b.hasAttributes||!b.attributes)return!1;var c={"class":"gw-clock gw-clock-aria s-item-container-height-auto feed-carousel using-mouse kfs-inner-container".split(" "),id:["dealClock",
"deal_expiry_timer","timer"],role:["timer"]},d=!1;Object.keys(c).forEach(function(a){var e=b.attributes[a]?b.attributes[a].value:"";(c[a]||"").forEach(function(a){-1!==e.indexOf(a)&&(d=!0)})});return d}function x(a){if(!a)return!1;var b=(e.extractStringValue(a.nodeName)||"").toLowerCase(),c=(e.extractStringValue(a.type)||"").toLowerCase(),d=(e.extractStringValue(a.href)||"").toLowerCase();a=(e.extractStringValue(a.id)||"").toLowerCase();var f="checkbox color date datetime-local email file month number password radio range reset search tel text time url week".split(" ");
if(-1!==["select","textarea","html"].indexOf(b)||"input"===b&&-1!==f.indexOf(c)||"a"===b&&-1!==d.indexOf("http")||-1!==["sitbreaderrightpageturner","sitbreaderleftpageturner","sitbreaderpagecontainer"].indexOf(a))return!0}function l(){n=!1;f=0;b.clearTimeout(s)}function C(){b.ue.onunload(function(){ue.count("armored-cxguardrails.unresponsive-clicks.violations",h);ue.count("armored-cxguardrails.unresponsive-clicks.violationRate",h/m*100||0)})}if(b.MutationObserver&&b.addEventListener&&Object.keys&&
d&&d.ue&&d.ue.log&&d.ue_unrt&&d.ue_utils){var y=d.ue_unrt,r="cel",v="unr_mcm",B="res_mcm",p=b.performance,e=d.ue_utils,n=!1,f=0,s=0,q=!1,k=0,h=0,m=0;b.addEventListener&&(b.addEventListener("mousedown",w,!0),b.addEventListener("beforeunload",l,!0),b.addEventListener("visibilitychange",l,!0),b.addEventListener("pagehide",l,!0));b.ue&&b.ue.event&&b.ue.onSushiUnload&&b.ue.onunload&&C();(new MutationObserver(z)).observe(t,{childList:!0,attributes:!0,characterData:!0,subtree:!0})}})(ue_csm,window,document);


ue_csm.ue.exec(function(g,e){if(e.ue_err){var f="";e.ue_err.errorHandlers||(e.ue_err.errorHandlers=[]);e.ue_err.errorHandlers.push({name:"fctx",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel)if(f=g.getElementsByTagName("html")[0].innerHTML){var b=f.indexOf("var ue_t0=ue_t0||+new Date();");if(-1!==b){var b=f.substr(0,b).split(String.fromCharCode(10)),d=Math.max(b.length-10-1,0),b=b.slice(d,b.length-1);a.fcsmln=d+b.length+1;a.cinfo=a.cinfo||{};for(var c=0;c<b.length;c++)a.cinfo[d+c+1+""]=
b[c]}b=f.split(String.fromCharCode(10));a.cinfo=a.cinfo||{};if(!(a.f||void 0===a.l||a.l in a.cinfo))for(c=+a.l-1,d=Math.max(c-5,0),c=Math.min(c+5,b.length-1);d<=c;d++)a.cinfo[d+1+""]=b[d]}}})}},"fatals-context")(document,window);


(function(m,a){function c(k){function f(b){b&&"string"===typeof b&&(b=(b=b.match(/^(?:https?:)?\/\/(.*?)(\/|$)/i))&&1<b.length?b[1]:null,b&&b&&("number"===typeof e[b]?e[b]++:e[b]=1))}function d(b){var e=10,d=+new Date;b&&b.timeRemaining?e=b.timeRemaining():b={timeRemaining:function(){return Math.max(0,e-(+new Date-d))}};for(var c=a.performance.getEntries(),k=e;g<c.length&&k>n;)c[g].name&&f(c[g].name),g++,k=b.timeRemaining();g>=c.length?h(!0):l()}function h(b){if(!b){b=m.scripts;var c;if(b)for(var d=
0;d<b.length;d++)(c=b[d].getAttribute("src"))&&"undefined"!==c&&f(c)}0<Object.keys(e).length&&(p&&ue_csm.ue&&ue_csm.ue.event&&ue_csm.ue.event({domains:e,pageType:a.ue_pty||null,subPageType:a.ue_spty||null,pageTypeId:a.ue_pti||null},"csm","csm.CrossOriginDomains.2"),a.ue_ext=e)}function l(){!0===k?d():a.requestIdleCallback?a.requestIdleCallback(d):a.requestAnimationFrame?a.requestAnimationFrame(d):a.setTimeout(d,100)}function c(){if(a.performance&&a.performance.getEntries){var b=a.performance.getEntries();
!b||0>=b.length?h(!1):l()}else h(!1)}var e=a.ue_ext||{};a.ue_ext||c();return e}function q(){setTimeout(c,r)}var s=a.ue_dserr||!1,p=!0,n=1,r=2E3,g=0;a.ue_err&&s&&(a.ue_err.errorHandlers||(a.ue_err.errorHandlers=[]),a.ue_err.errorHandlers.push({name:"ext",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel){var f=c(!0),d=[],h;for(h in f){var f=h,g=f.match(/amazon(\.com?)?\.\w{2,3}$/i);g&&1<g.length||-1!==f.indexOf("amazon-adsystem.com")||-1!==f.indexOf("amazonpay.com")||-1!==f.indexOf("cloudfront-labs.amazonaws.com")||
d.push(h)}a.ext=d}}}));a.ue&&a.ue.isl?c():a.ue&&ue.attach&&ue.attach("load",q)})(document,window);





var ue_wtc_c = 3;
ue_csm.ue.exec(function(b,e){function l(){for(var a=0;a<f.length;a++)a:for(var d=s.replace(A,f[a])+g[f[a]]+t,c=arguments,b=0;b<c.length;b++)try{c[b].send(d);break a}catch(e){}g={};f=[];n=0;k=p}function u(){B?l(q):l(C,q)}function v(a,m,c){r++;if(r>w)d.count&&1==r-w&&(d.count("WeblabTriggerThresholdReached",1),b.ue_int&&console.error("Number of max call reached. Data will no longer be send"));else{var h=c||{};h&&-1<h.constructor.toString().indexOf(D)&&a&&-1<a.constructor.toString().indexOf(x)&&m&&-1<
m.constructor.toString().indexOf(x)?(h=b.ue_id,c&&c.rid&&(h=c.rid),c=h,a=encodeURIComponent(",wl="+a+"/"+m),2E3>a.length+p?(2E3<k+a.length&&u(),void 0===g[c]&&(g[c]="",f.push(c)),g[c]+=a,k+=a.length,n||(n=e.setTimeout(u,E))):b.ue_int&&console.error("Invalid API call. The input provided is over 2000 chars.")):d.count&&(d.count("WeblabTriggerImproperAPICall",1),b.ue_int&&console.error("Invalid API call. The input provided does not match the API protocol i.e ue.trigger(String, String, Object)."))}}function F(){d.trigger&&
d.trigger.isStub&&d.trigger.replay(function(a){v.apply(this,a)})}function y(){z||(f.length&&l(q),z=!0)}var t=":1234",s="//"+b.ue_furl+"/1/remote-weblab-triggers/1/OE/"+b.ue_mid+":"+b.ue_sid+":PLCHLDR_RID$s:wl-client-id%3DCSMTriger",A="PLCHLDR_RID",E=b.wtt||1E4,p=s.length+t.length,w=b.mwtc||2E3,G=1===e.ue_wtc_c,B=3===e.ue_wtc_c,H=e.XMLHttpRequest&&"withCredentials"in new e.XMLHttpRequest,x="String",D="Object",d=b.ue,g={},f=[],k=p,n,z=!1,r=0,C=function(){return{send:function(a){if(H){var b=new e.XMLHttpRequest;
b.open("GET",a,!0);G&&(b.withCredentials=!0);b.send()}else throw"";}}}(),q=function(){return{send:function(a){(new Image).src=a}}}();e.encodeURIComponent&&(d.attach&&(d.attach("beforeunload",y),d.attach("pagehide",y)),F(),d.trigger=v)},"client-wbl-trg")(ue_csm,window);


(function(k,d,h){function f(a,c,b){a&&a.indexOf&&0===a.indexOf("http")&&0!==a.indexOf("https")&&l(s,c,a,b)}function g(a,c,b){a&&a.indexOf&&(location.href.split("#")[0]!=a&&null!==a&&"undefined"!==typeof a||l(t,c,a,b))}function l(a,c,b,e){m[b]||(e=u&&e?n(e):"N/A",d.ueLogError&&d.ueLogError({message:a+c+" : "+b,logLevel:v,stack:"N/A"},{attribution:e}),m[b]=1,p++)}function e(a,c){if(a&&c)for(var b=0;b<a.length;b++)try{c(a[b])}catch(d){}}function q(){return d.performance&&d.performance.getEntriesByType?
d.performance.getEntriesByType("resource"):[]}function n(a){if(a.id)return"//*[@id='"+a.id+"']";var c;c=1;var b;for(b=a.previousSibling;b;b=b.previousSibling)b.nodeName==a.nodeName&&(c+=1);b=a.nodeName;1!=c&&(b+="["+c+"]");a.parentNode&&(b=n(a.parentNode)+"/"+b);return b}function w(){var a=h.images;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"img",a);g(b,"img",a)})}function x(){var a=h.scripts;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"script",a);g(b,"script",a)})}
function y(){var a=h.styleSheets;a&&a.length&&e(a,function(a){if(a=a.ownerNode){var b=a.getAttribute("href");f(b,"style",a);g(b,"style",a)}})}function z(){if(A){var a=q();e(a,function(a){f(a.name,a.initiatorType)})}}function B(){e(q(),function(a){g(a.name,a.initiatorType)})}function r(){var a;a=d.location&&d.location.protocol?d.location.protocol:void 0;"https:"==a&&(z(),w(),x(),y(),B(),p<C&&setTimeout(r,D))}var s="[CSM] Insecure content detected ",t="[CSM] Ajax request to same page detected ",v="WARN",
m={},p=0,D=k.ue_nsip||1E3,C=5,A=1==k.ue_urt,u=!0;ue_csm.ue_disableNonSecure||(d.performance&&d.performance.setResourceTimingBufferSize&&d.performance.setResourceTimingBufferSize(300),r())})(ue_csm,window,document);


var ue_aa_a = "T1";
if (ue.trigger && (ue_aa_a === "C" || ue_aa_a === "T1")) {
    ue.trigger("UEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249", ue_aa_a);
}
(function(f,b){function g(){try{b.PerformanceObserver&&"function"===typeof b.PerformanceObserver&&(a=new b.PerformanceObserver(function(b){c(b.getEntries())}),a.observe(d))}catch(h){k()}}function m(){for(var h=d.entryTypes,a=0;a<h.length;a++)c(b.performance.getEntriesByType(h[a]))}function c(a){if(a&&Array.isArray(a)){for(var c=0,e=0;e<a.length;e++){var d=l.indexOf(a[e].name);if(-1!==d){var g=Math.round(b.performance.timing.navigationStart+a[e].startTime);f.uet(n[d],void 0,void 0,g);c++}}l.length===
c&&k()}}function k(){a&&a.disconnect&&"function"===typeof a.disconnect&&a.disconnect()}if("function"===typeof f.uet&&b.performance&&"object"===typeof b.performance&&b.performance.getEntriesByType&&"function"===typeof b.performance.getEntriesByType&&b.performance.timing&&"object"===typeof b.performance.timing&&"number"===typeof b.performance.timing.navigationStart){var d={entryTypes:["paint"]},l=["first-paint","first-contentful-paint"],n=["fp","fcp"],a;try{m(),g()}catch(p){f.ueLogError(p,{logLevel:"ERROR",
attribution:"performanceMetrics"})}}})(ue_csm,window);


if (window.csa) {
    csa("Events")("setEntity", {
        page:{pageType: "Search", subPageType: "List", pageTypeId: ""}
    });
}
csa.plugin(function(c){var m="transitionStart",n="pageVisible",e="PageTiming",t="visibilitychange",s="$latency.visible",i=c.global,r=(i.performance||{}).timing,a=["navigationStart","unloadEventStart","unloadEventEnd","redirectStart","redirectEnd","fetchStart","domainLookupStart","domainLookupEnd","connectStart","connectEnd","secureConnectionStart","requestStart","responseStart","responseEnd","domLoading","domInteractive","domContentLoadedEventStart","domContentLoadedEventEnd","domComplete","loadEventStart","loadEventEnd"],o=i.Math,u=o.max,l=o.floor,d=i.document||{},g=(r||{}).navigationStart,f=g,v=0,p=null;if(i.Object.keys&&[].forEach&&!c.config["KillSwitch."+e]){if(!r||null===g||g<=0||void 0===g)return c.error("Invalid navigation timing data: "+g);p=new S({schemaId:"<ns>.PageLatency.5",producerId:"csa"}),"boolean"!=typeof d.hidden&&"string"!=typeof d.visibilityState||!d.removeEventListener?c.emit(s):h()?(c.emit(s),E(n,g)):c.on(d,t,function e(){h()&&(f=c.time(),d.removeEventListener(t,e),E(m,f),E(n,f),c.emit(s))}),c.once("$unload",I),c.once("$load",I),c.on("$pageTransition",function(){f=c.time()}),c.register(e,{mark:E,instance:function(e){return new S(e)}})}function S(e){var i,r=null,a=e.ent||{page:["pageType","subPageType","requestId"]},o=e.logger||c("Events",{producerId:e.producerId});if(!e||!e.producerId||!e.schemaId)return c.error("The producer id and schema Id must be defined for PageLatencyInstance.");function d(){return i||f}function n(){r=c.UUID()}this.mark=function(n,t){if(null!=n)return t=t||c.time(),n===m&&(i=t),c.once(s,function(){o("log",{messageId:r,__merge:function(e){e.markers[n]=function(e,n){return u(0,n-(e||f))}(d(),t),e.markerTimestamps[n]=l(t)},markers:{},markerTimestamps:{},navigationStartTimestamp:d()?new Date(d()).toISOString():null,schemaId:e.schemaId},{ent:a})}),t},n(),c.on("$beforePageTransition",n)}function E(e,n){e===m&&(f=n);var t=p.mark(e,n);c.emit("$timing:"+e,t)}function I(){if(!v){for(var e=0;e<a.length;e++)r[a[e]]&&E(a[e],r[a[e]]);v=1}}function h(){return!d.hidden||"visible"===d.visibilityState}});csa.plugin(function(f){var u,c,l="length",a="parentElement",t="target",i="getEntriesByName",e="perf",n=null,r="_csa_flt",o="_csa_llt",s="previousSibling",d="_osrc",g="_elt",h="_eid",m=10,p=5,v=15,y=100,E=f.global,S=f.timeout,b=E.Math,x=b.max,L=b.floor,O=b.ceil,_=E.document,w=E.performance||{},T=(w.timing||{}).navigationStart,I=Date.now,N=Object.values||(f.types||{}).ovl,k=f("PageTiming"),B=f("SpeedIndexBuffers"),Y=[],C=[],F=[],H=[],M=[],R=[],V=.1,W=.1,$=0,P=0,X=!0,D=0,J=0,j=1==f.config["SpeedIndex.ForceReplay"],q=0,Q=1,U=0,z={},A=[],G=0,K={buffered:1};function Z(e){f.global.ue_csa_ss_tag||f.emit("$csmTag:"+e,0,K)}function ee(){for(var e=I(),n=0;u;){if(0!==u[l]){if(!1!==u.h(u[0])&&u.shift(),n++,!j&&n%m==0&&I()-e>p)break}else u=u.n}$=0,u&&($||(!0===_.hidden?(j=1,ee()):f.timeout(ee,0)))}function ne(e,n,t,i,r){U=L(e),Y=n,C=t,F=i,R=r;var o=_.createTreeWalker(_.body,NodeFilter.SHOW_TEXT,null,null),a={w:E.innerWidth,h:E.innerHeight,x:E.pageXOffset,y:E.pageYOffset};_.body[g]=e,H.push({w:o,vp:a}),M.push({img:_.images,iter:0}),Y.h=te,(Y.n=C).h=ie,(C.n=F).h=re,(F.n=H).h=oe,(H.n=M).h=ae,(M.n=R).h=fe,u=Y,ee()}function te(e){e.m.forEach(function(e){for(var n=e;n&&(e===n||!n[r]||!n[o]);)n[r]||(n[r]=e[r]),n[o]||(n[o]=e[o]),n[g]=n[r]-T,n=n[s]})}function ie(e){e.m.forEach(function(e){var n=e[t];d in n||(n[d]=e.oldValue)})}function re(n){n.m.forEach(function(e){e[t][g]=n.t-T})}function oe(e){for(var n,t=e.vp,i=e.w,r=m;(n=i.nextNode())&&0<r;){r-=1;var o=(n[a]||{}).nodeName;"SCRIPT"!==o&&"STYLE"!==o&&"NOSCRIPT"!==o&&"BODY"!==o&&0!==(n.nodeValue||"").trim()[l]&&de(n[a],ue(n),t)}return!n}function ae(e){for(var n={w:E.innerWidth,h:E.innerHeight,x:E.pageXOffset,y:E.pageYOffset},t=m;e.iter<e.img[l]&&0<t;){var i,r=e.img[e.iter],o=se(r),a=o&&ue(o)||ue(r);o?(o[g]=a,i=le(o.querySelector('[aria-posinset="1"] img')||r)||a,r=o):i=le(r)||a,J&&c<i&&(i=a),de(r,i,n),e.iter+=1,t-=1}return e.img[l]<=e.iter}function fe(e){var n=[],i=0,r=0,o=P,t=L(e.y/y),a=O((e.y+E.innerHeight)/y);A.slice(t,a).forEach(function(e){(e.elems||[]).forEach(function(e){e.lt in n||(n[e.lt]={}),e.id in n[e.lt]||(i+=(n[e.lt][e.id]=e).a)})}),Z("startVL"),N(n).forEach(function(e){N(e).forEach(function(e){var n=1-r/i,t=x(e.lt,o);G+=n*(t-o),o=t,function(e,n){var t;for(;V<=1&&V-.01<=e;)ge("visuallyLoaded"+(t=(100*V).toFixed(0)),n.lt),"50"!==t&&"90"!==t||f("Content",{target:n.e})("mark","visuallyLoaded"+t,T+O(n.lt||0)),V+=W}((r+=e.a)/i,e)})}),Z("endVL"),P=e.t-T,R[l]<=1&&(ge("speedIndex",G),ge("visuallyLoaded0",U)),X&&(X=!1,ge("atfSpeedIndex",G))}function ue(e){for(var n=e[a],t=v;n&&0<t;){if(n[g]||0===n[g])return x(n[g],U);n=n.parentElement,t-=1}}function ce(e,n){if(e){if(!e.indexOf("data:"))return ue(n);var t=w[i](e)||[];if(0<t[l])return x(O(t[0].responseEnd||0),U)}}function le(e){return ce(e[d],e)||ce(e.currentSrc,e)||ce(e.src,e)}function se(e){for(var n=10,t=e.parentElement;t&&0<n;){if(t.classList&&t.classList.contains("a-carousel-viewport"))return t;t=t.parentElement,n-=1}return null}function de(e,n,t){if((n||0===n)&&!e[h]){var i=e.getBoundingClientRect(),r=i.width*i.height,o=i.width/2,a=Q++;if(0!=r&&!(o<i.right-t.w||i.right<o)){for(var f={e:e,lt:n,a:r,id:a},u=L((i.top+t.y)/y),c=O((i.top+t.y+i.height)/y),l=u;l<=c;l++)l in A||(A[l]={elems:[],lt:0}),A[l].elems.push(f);e[h]=a}}}function ge(e,n){k("mark",e,T+O((z[e]=n)||0))}function he(e){q||(Z("browserQuite"+e),B("getBuffers",ne),q=1)}T&&N&&w[i]?(Z(e+"Yes"),B("registerListener",function(){J&&(clearTimeout(D),D=S(he.bind(n,"Mut"),2500))}),f.once("$unload",function(){j=1,he("Ud")}),f.once("$load",function(){J=1,c=I()-T,D=S(he.bind(n,"Ld"),2500)}),f.once("$timing:functional",he.bind(n,"Fn")),B("replayModuleIsLive"),f.register("SpeedIndex",{getMarkers:function(e){e&&e(JSON.parse(JSON.stringify(z)))}})):Z(e+"No")});csa.plugin(function(e){var m=!!e.config["LCP.elementDedup"],t=!1,n=e("PageTiming"),r=e.global.PerformanceObserver,a=e.global.performance;function i(){return a.timing.navigationStart}function o(){t||function(o){var l=new r(function(e){var t=e.getEntries();if(0!==t.length){var n=t[t.length-1];if(m&&""!==n.id&&n.element&&"IMG"===n.element.tagName){for(var r={},a=t[0],i=0;i<t.length;i++)t[i].id in r||(""!==t[i].id&&(r[t[i].id]=!0),a.startTime<t[i].startTime&&(a=t[i]));n=a}l.disconnect(),o({startTime:n.startTime,renderTime:n.renderTime,loadTime:n.loadTime})}});try{l.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}}(function(e){e&&(t=!0,n("mark","largestContentfulPaint",Math.floor(e.startTime+i())),e.renderTime&&n("mark","largestContentfulPaint.render",Math.floor(e.renderTime+i())),e.loadTime&&n("mark","largestContentfulPaint.load",Math.floor(e.loadTime+i())))})}r&&a&&a.timing&&(e.once("$unload",o),e.once("$load",o),e.register("LargestContentfulPaint",{}))});csa.plugin(function(r){var e=r("Metrics",{producerId:"csa"}),n=r.global.PerformanceObserver;n&&(n=new n(function(r){var t=r.getEntries();if(0===t.length||!t[0].processingStart||!t[0].startTime)return;!function(r){r=r||0,n.disconnect(),0<=r?e("recordMetric","firstInputDelay",r):e("recordMetric","firstInputDelay.invalid",1)}(t[0].processingStart-t[0].startTime)}),function(){try{n.observe({type:"first-input",buffered:!0})}catch(r){}}())});csa.plugin(function(d){var e="Metrics",g=0;function r(i){var c,t,e=i.producerId,r=i.logger,s=r||d("Events",{producerId:e}),o=(i||{}).dimensions||{},u={},n=-1;if(!e&&!r)return d.error("Either a producer id or custom logger must be defined");function a(){n!==g&&(c=d.UUID(),t=d.UUID(),u={},n=g)}this.recordMetric=function(r,n){var e=i.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};e.debugMetric=i.debugMetric,a(),s("log",{messageId:c,schemaId:i.schemaId||"<ns>.Metric.3",metrics:{},dimensions:o,__merge:function(e){e.metrics[r]=n}},e)},this.recordCounter=function(r,e){var n=i.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};if("string"!=typeof r||"number"!=typeof e||!isFinite(e))return d.error("Invalid type given for counter name or counter value: "+r+"/"+e);a(),r in u||(u[r]={});var c=u[r];"f"in c||(c.f=e),c.c=(c.c||0)+1,c.s=(c.s||0)+e,c.l=e,s("log",{messageId:t,schemaId:i.schemaId||"<ns>.InternalCounters.2",c:{},__merge:function(e){r in e.c||(e.c[r]={}),c.fs||(c.fs=1,e.c[r].f=c.f),1<c.c&&(e.c[r].s=c.s,e.c[r].l=c.l,e.c[r].c=c.c)}},n)}}d.config["KillSwitch."+e]||(new r({producerId:"csa"}).recordMetric("baselineMetricEvent",1),d.on("$beforePageTransition",function(){g++}),d.register(e,{instance:function(e){return new r(e||{})}}))});csa.plugin(function(t){var a,r=(t.global.performance||{}).timing,s=(r||{}).navigationStart||t.time();function e(){a=t.UUID()}function n(i){var r=(i=i||{}).producerId,e=i.logger,o=e||t("Events",{producerId:r});if(!r&&!e)return t.error("Either a producer id or custom logger must be defined");this.mark=function(e,r){var n=(void 0===r?t.time():r)-s;o("log",{messageId:a,schemaId:i.schemaId||"<ns>.Timer.1",markers:{},__merge:function(r){r.markers[e]=n}},i.logOptions)}}r&&(e(),t.on("$beforePageTransition",e),t.register("Timers",{instance:function(r){return new n(r||{})}}))});csa.plugin(function(t){var e="takeRecords",i="disconnect",n="function",o=t("Metrics",{producerId:"csa"}),c=t("PageTiming"),a=t.global,u=t.timeout,r=t.on,f=a.PerformanceObserver,m=0,l=!1,s=0,d=a.performance,h=a.document,v=null,y=!1,g=t.blank;function p(){l||(l=!0,clearTimeout(v),typeof f[e]===n&&f[e](),typeof f[i]===n&&f[i](),o("recordMetric","documentCumulativeLayoutShift",m),c("mark","cumulativeLayoutShiftLastTimestamp",Math.floor(s+d.timing.navigationStart)))}f&&d&&d.timing&&h&&(f=new f(function(t){v&&clearTimeout(v);t.getEntries().forEach(function(t){t.hadRecentInput||(m+=t.value,s<t.startTime&&(s=t.startTime))}),v=u(p,5e3)}),function(){try{f.observe({type:"layout-shift",buffered:!0}),v=u(p,5e3)}catch(t){}}(),g=r(h,"click",function(t){y||(y=!0,o("recordMetric","documentCumulativeLayoutShiftToFirstInput",m),g())}),r(h,"visibilitychange",function(){"hidden"===h.visibilityState&&p()}),t.once("$unload",p))});csa.plugin(function(e){var t,n=e.global,r=n.PerformanceObserver,c=e("Metrics",{producerId:"csa"}),o=0,i=0,a=-1,l=n.Math,f=l.max,u=l.ceil;if(r){t=new r(function(e){e.getEntries().forEach(function(e){var t=e.duration;o+=t,i+=t,a=f(t,a)})});try{t.observe({type:"longtask",buffered:!0})}catch(e){}t=new r(function(e){0<e.getEntries().length&&(i=0,a=-1)});try{t.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}e.on("$unload",g),e.on("$beforePageTransition",g)}function g(){c("recordMetric","totalBlockingTime",u(i||0)),c("recordMetric","totalBlockingTimeInclLCP",u(o||0)),c("recordMetric","maxBlockingTime",u(a||0)),i=o=0,a=-1}});csa.plugin(function(r){var e="CacheDetection",o="csa-ctoken-",n=r.store,t=r.deleteStored,c=r.config,a=c[e+".RequestID"],i=c[e+".Callback"],s=r.global,u=s.document||{},d=s.Date,f=r("Events"),l=r("Events",{producerId:"csa"});function p(e){try{var n=u.cookie.match(RegExp("(^| )"+e+"=([^;]+)"));return n&&n[2].trim()}catch(e){}}!function(){var e=function(){var e=p("cdn-rid");if(e)return{r:e,s:"cdn"}}()||function(){if(r.store(o+a))return{r:r.UUID().toUpperCase().replace(/-/g,"").slice(0,20),s:"device"}}()||{},n=e.r,c=e.s;if(!!n){var t=p("session-id");!function(e,n,c,t){f("setEntity",{page:{pageSource:"cache",requestId:e,cacheRequestId:a,cacheSource:t},session:{id:c}})}(n,0,t,c),"device"===c&&l("log",{schemaId:"<ns>.CacheImpression.1"},{ent:"all"}),i&&i(n,t,c)}}(),n(o+a,d.now()+36e5),r.once("$load",function(){var c=d.now();t(function(e,n){return 0==e.indexOf(o)&&parseInt(n)<c})})});csa.plugin(function(u){var i,t="Content",e="MutationObserver",n="addedNodes",a="querySelectorAll",f="matches",o="getAttributeNames",r="getAttribute",s="dataset",c="widget",l="producerId",d="slotId",h="iSlotId",g={ent:{element:1,page:["pageType","subPageType","requestId"]}},p=5,m=u.config[t+".BubbleUp.SearchDepth"]||35,y=u.config[t+".SearchPage"]||0,v="csaC",b=v+"Id",E="logRender",w={},I=u.config,O=I[t+".Selectors"]||[],C=I[t+".WhitelistedAttributes"]||{href:1,class:1},N=I[t+".EnableContentEntities"],S=I["KillSwitch.ContentRendered"],k=u.global,A=k.document||{},U=A.documentElement,L=k.HTMLElement,R={},_=[],j=function(t,e,n,i){var r=this,o=u("Events",{producerId:t||"csa"});e.type=e.type||c,r.id=e.id,r.l=o,r.e=e,r.el=n,r.rt=i,r.dlo=g,r.op=W(n,"csaOp"),r.log=function(t,e){o("log",t,e||g)},e.id&&o("setEntity",{element:e})},x=j.prototype;function D(t){var e=(t=t||{}).element,n=t.target;return e?function(t,e){var n;n=t instanceof L?K(t)||Y(e[l],t,z,u.time()):R[t.id]||H(e[l],0,t,u.time());return n}(e,t):n?M(n):u.error("No element or target argument provided.")}function M(t){var e=function(t){var e=null,n=0;for(;t&&n<m;){if(n++,P(t,b)){e=t;break}t=t.parentElement}return e}(t);return e?K(e):new j("csa",{id:null},null,u.time())}function P(t,e){if(t&&t.dataset)return t.dataset[e]}function T(t,e,n){_.push({n:n,e:t,t:e}),B()}function q(){for(var t=u.time(),e=0;0<_.length;){var n=_.shift();if(w[n.n](n.e,n.t),++e%10==0&&u.time()-t>p)break}i=0,_.length&&B()}function B(){i=i||u.raf(q)}function X(t,e,n){return{n:t,e:e,t:n}}function Y(t,e,n,i){var r=u.UUID(),o={id:r},c=M(e);return e[s][b]=r,n(o,e),c&&c.id&&(o.parentId=c.id),H(t,e,o,i)}function $(t){return isNaN(t)?null:Math.round(t)}function H(t,e,n,i){N&&(n.schemaId="<ns>.ContentEntity.2"),n.id=n.id||u.UUID();var r=new j(t,n,e,i);return function(t){return!S&&((t.op||{}).hasOwnProperty(E)||y)}(r)&&function(t,e){var n={},i=u.exec($);t.el&&(n=t.el.getBoundingClientRect()),t.log({schemaId:"<ns>.ContentRender.2",timestamp:e,width:i(n.width),height:i(n.height),positionX:i(n.left+k.pageXOffset),positionY:i(n.top+k.pageYOffset)})}(r,i),u.emit("$content.register",r),R[n.id]=r}function K(t){return R[(t[s]||{})[b]]}function W(n,i){var r={};return o in(n=n||{})&&Object.keys(n[s]).forEach(function(t){if(!t.indexOf(i)&&i.length<t.length){var e=function(t){return(t[0]||"").toLowerCase()+t.slice(1)}(t.slice(i.length));r[e]=n[s][t]}}),r}function z(t,e){o in e&&(function(t,e){var n=W(t,v);Object.keys(n).forEach(function(t){e[t]=n[t]})}(e,t),d in t&&(t[h]=t[d]),function(e,n){(e[o]()||[]).forEach(function(t){t in C&&(n[t]=e[r](t))})}(e,t))}U&&A[a]&&k[e]&&(O.push({selector:"*[data-csa-c-type]",entity:z}),O.push({selector:".celwidget",entity:function(t,e){z(t,e),t[d]=t[d]||e[r]("cel_widget_id")||e.id,t.legacyId=e[r]("cel_widget_id")||e.id,t.type=t.type||c}}),w[1]=function(t,e){t.forEach(function(t){t[n]&&t[n].constructor&&"NodeList"===t[n].constructor.name&&Array.prototype.forEach.call(t[n],function(t){_.unshift(X(2,t,e))})})},w[2]=function(o,c){a in o&&f in o&&O.forEach(function(t){for(var e=t.selector,n=o[f](e),i=o[a](e),r=i.length-1;0<=r;r--)_.unshift(X(3,{e:i[r],s:t},c));n&&_.unshift(X(3,{e:o,s:t},c))})},w[3]=function(t,e){var n=t.e;K(n)||Y("csa",n,t.s.entity,e)},w[4]=function(){u.register(t,{instance:D})},new k[e](function(t){T(t,u.time(),1)}).observe(U,{childList:!0,subtree:!0}),T(U,u.time(),2),T(null,u.time(),4),u.on("$content.export",function(e){Object.keys(e).forEach(function(t){x[t]=e[t]})}))});csa.plugin(function(o){var i,t="ContentImpressions",e="KillSwitch.",n="IntersectionObserver",r="getAttribute",s="dataset",c="intersectionRatio",a="csaCId",m=1e3,l=o.global,f=o.config,u=f[e+t],v=f[e+t+".ContentViews"],g=((l.performance||{}).timing||{}).navigationStart||o.time(),d={};function h(t){t&&(t.v=1,function(t){t.vt=o.time(),t.el.log({schemaId:"<ns>.ContentView.3",timeToViewed:t.vt-t.el.rt,pageFirstPaintToElementViewed:t.vt-g})}(t))}function I(t){t&&!t.it&&(t.i=o.time()-t.is>m,function(t){t.it=o.time(),t.el.log({schemaId:"<ns>.ContentImpressed.2",timeToImpressed:t.it-t.el.rt,pageFirstPaintToElementImpressed:t.it-g})}(t))}!u&&l[n]&&(i=new l[n](function(t){var n=o.time();t.forEach(function(t){var e=function(t){if(t&&t[r])return d[t[s][a]]}(t.target);if(e){o.emit("$content.intersection",{meta:e.el,t:n,e:t});var i=t.intersectionRect;t.isIntersecting&&0<i.width&&0<i.height&&(v||e.v||h(e),.5<=t[c]&&!e.is&&(e.is=n,e.timer=o.timeout(function(){I(e)},m))),t[c]<.5&&!e.it&&e.timer&&(l.clearTimeout(e.timer),e.is=0,e.timer=0)}})},{threshold:[0,.5,.99]}),o.on("$content.register",function(t){var e=t.el;e&&(d[t.id]={el:t,v:0,i:0,is:0,vt:0,it:0},i.observe(e))}))});csa.plugin(function(e){e.config["KillSwitch.ContentLatency"]||e.emit("$content.export",{mark:function(t,n){var o=this;o.t||(o.t=e("Timers",{logger:o.l,schemaId:"<ns>.ContentLatency.1",logOptions:o.dlo})),o.t("mark",t,n)}})});csa.plugin(function(t){function n(i,e,o){var c={};function r(t,n,e){t in c&&o<=n-c[t].s&&(function(n,e,i){if(!p)return;S(function(t){T(n,t),t.w[n][e]=a((t.w[n][e]||0)+i)})}(t,i,n-c[t].d),c[t].d=n),e||delete c[t]}this.update=function(t,n){n.isIntersecting&&e<=n.intersectionRatio?function(t,n){t in c||(c[t]={s:n,d:n})}(t,u()):r(t,u())},this.stopAll=function(t){var n=u();for(var e in c)r(e,n,t)},this.reset=function(){var t=u();for(var n in c)c[n].s=t,c[n].d=t}}var e=t.config,u=t.time,i="ContentInteractionsSummary",o=e[i+".FlushInterval"]||5e3,c=e[i+".FlushBackoff"]||1.5,r=t.global,s=t.on,a=Math.floor,f=(r.document||{}).documentElement||{},l=((r.performance||{}).timing||{}).responseStart||t.time(),d=o,m=0,p=!0,v=t.UUID(),g=t("Events",{producerId:"csa"}),I=new n("it0",0,0),w=new n("it50",.5,1e3),h=new n("it100",.99,0),A={},b={};function $(){I.stopAll(!0),w.stopAll(!0),h.stopAll(!0),U()}function C(){I.reset(),w.reset(),h.reset(),U()}function U(){d&&(clearTimeout(m),m=t.timeout($,d),d*=c)}function E(n){S(function(t){T(n,t),t.w[n].mc=(t.w[n].mc||0)+1})}function S(t){g("log",{messageId:v,schemaId:"<ns>.ContentInteractionsSummary.1",w:{},__merge:t},{ent:{page:["requestId"]}})}function T(t,n){t in n.w||(n.w[t]={})}s("$content.intersection",function(t){if(t&&t.meta&&t.e){var n=t.meta.id;if(n in A){var e=t.e.boundingClientRect||{};e.width<5||e.height<5||(I.update(n,t.e),w.update(n,t.e),h.update(n,t.e),!t.e.isIntersecting||n in b||(b[n]=1,function(n,e){S(function(t){T(n,t),t.w[n].ttfv=a(e)})}(n,u()-l)))}}}),s("$content.register",function(t){(t.e||{}).slotId&&(A[t.id]={},function(e){S(function(t){var n=e.id;T(n,t),t.w[n].sid=(e.e||{}).slotId,t.w[n].cid=(e.e||{}).contentId})}(t))}),s("$beforePageTransition",function(){$(),C(),v=t.UUID(),U()}),s("$beforeunload",function(){I.stopAll(),w.stopAll(),h.stopAll(),d=null}),s("$visible",function(t){t?C():($(),clearTimeout(m)),p=t},{buffered:1}),s(f,"click",function(t){for(var n=t.target,e=25;n&&0<e;){var i=(n.dataset||{}).csaCId;i&&E(i),n=n.parentElement,e-=1}},{capture:!0,passive:!0}),U()});csa.plugin(function(o){var t,n,i="normal",s="reload",e="history",d="new-tab",a="ajax",r=1,c=2,u="lastActive",l="lastInteraction",f="used",p="csa-tabbed-browsing",g="visibilityState",v={"back-memory-cache":1,"tab-switch":1,"history-navigation-page-cache":1},b="<ns>.TabbedBrowsing.2",m="visible",y=o.global,I=o("Events",{producerId:"csa"}),h=y.location||{},T=y.document,w=y.JSON,z=((y.performance||{}).navigation||{}).type,P=o.store,S=o.on,k=o.storageSupport(),x=!1,A={},C={},O={},$={},j=!1,q=!1,B=!1;function E(i){try{return w.parse(P(p,void 0,{session:i})||"{}")||{}}catch(i){o.error('Could not parse storage value for key "'+p+'": '+i)}return{}}function J(i,t){P(p,w.stringify(t||{}),{session:i})}function N(i){var t=C.tid||i.id,n=A[u]||{};n.tid===t&&(n.pid=i.id),$={pid:i.id,tid:t,lastInteraction:C[l]||{},initialized:!0},O={lastActive:n,lastInteraction:A[l]||{},time:o.time()}}function D(i){var t=i===d,n=T.referrer,e=!(n&&n.length)||!~n.indexOf(h.origin||""),a=t&&e,r={type:i,toTabId:$.tid,toPageId:$.pid,transitTime:o.time()-A.time||null};a||function(i,t,n){var e=i===s,a=t?A[u]||{}:C,r=A[l]||{},o=C[l]||{},d=t?r:o;n.fromTabId=a.tid,n.fromPageId=a.pid,e||!d.id||d[f]||(n.interactionId=d.id||null,r.id===d.id&&(r[f]=!0),o.id===d.id&&(o[f]=!0))}(i,t,r),I("log",{navigation:r,schemaId:b},{ent:{page:["pageType","subPageType","requestId"]}})}function F(i){B=function(i){return i&&i in v}(i.transitionType),function(){A=E(!1),C=E(!0);var i=A[l],t=C[l],n=!1,e=!1;i&&t&&i.id===t.id&&i[f]!==t[f]&&(n=!i[f],e=!t[f],t[f]=i[f]=!0,n&&J(!1,A),e&&J(!0,C))}(),N(i),j=!0,function(i){var t,n;t=H(),n=K(),(t||n)&&N(i)}(i)}function G(){x&&!B?D(a):(x=!0,D(z===c||B?e:z===r?C.initialized?s:d:C.initialized?i:d))}function H(){return!(!j||!t)&&(C[l]={id:t.messageId,used:!(A[l]={id:t.messageId,used:!1})},!(t=null))}function K(){var i=!1;if(q=T[g]===m,j){var t=A[u]||{};i=function(i,t,n){var e=!1,a=i[u];return q?a&&a.tid===$.tid&&a[m]&&a.pid===n||(i[u]={visible:!0,pid:n,tid:t},e=!0):a&&a.tid===$.tid&&a[m]&&(e=!(a[m]=!1)),e}(A,C.tid||t.tid||$.tid,C.pid||t.pid||$.pid)}return i}k.local&&k.session&&w&&T&&g in T&&(n=function(){try{return y.self!==y.top}catch(i){return!0}}(),S("$pageChange",function(i){n||(F(i),G(),J(!1,O),J(!0,$),C=$,A=O)},{buffered:1}),S("$content.interaction",function(i){t=i,H()&&(J(!1,A),J(!0,C))}),S(T,"visibilitychange",function(){!n&&K()&&J(!1,A)},{capture:!1,passive:!0}))});csa.plugin(function(c){var e=c("Metrics",{producerId:"csa"});c.on(c.global,"pageshow",function(c){c&&c.persisted&&e("recordMetric","bfCache",1)})});csa.plugin(function(n){var e,t,i,o,r,a,c,u,f,s,l,d,m,p,g,v,h="hasFocus",b="$app.",y="avail",S="client",T="document",$="inner",I="offset",P="screen",w="scroll",D="Width",E="Height",F=y+D,O=y+E,q=S+D,x=S+E,z=$+D,C=$+E,H=I+D,K=I+E,M=w+D,W=w+E,X=n.config["KillSwitch.PageInteractionsSummary"],Y=n("Events",{producerId:"csa"}),j=1,k=n.global||{},A=n.time,B=n.on,G=n.once,J=k[T]||{},L=k[P]||{},N=k.Math||{},Q=N.abs,R=N.max,U=N.ceil,V=((k.performance||{}).timing||{}).responseStart,Z=function(){return J[h]()},_=1,nn=100,en={},tn=1;function on(){c=t=o=r=e,i=0,a=u=f=s=0,cn(),an()}function rn(){V&&!o&&(c=U((o=l)-V),tn=1)}function an(){u=U(R(u,m+v)),d&&(f=U(R(f,d+g))),tn=1}function cn(){l=A(),d=Q(k.pageXOffset||0),m=Q(k.pageYOffset||0),p=0<d||0<m,g=k[z]||0,v=k[C]||0}function un(){cn(),rn(),function(){var n=m-i;t&&!(t&&t<=l)||(n&&(++a,tn=1),i=m,n),t=l+nn}(),an()}function fn(){if(r){var n=U(A()-r);s+=n,r=e,tn=0<n}}function sn(){r=r||A()}function ln(n,e,t,i){e[n+D]=U(t||0),e[n+E]=U(i||0)}function dn(n){var e=n===en,t=Z();if(t||tn){if(!e){if(!j)return;j=0,t&&fn()}var i=function(){var n={},e=J.documentElement||{},t=J.body||{};return ln("availableScreen",n,L[F],L[O]),ln(T,n,R(t[M]||0,t[H]||0,e[q]||0,e[M]||0,e[H]||0),R(t[W]||0,t[K]||0,e[x]||0,e[W]||0,e[K]||0)),ln(P,n,L.width,L.height),ln("viewport",n,k[z],k[C]),n}(),o=function(){var n={scrollCounts:a,reachedDepth:u,horizontalScrollDistance:f,dwellTime:s};return"number"==typeof c&&(n.clientTimeToFirstScroll=c),n}();e?tn=0:(on(),V=A(),t&&(r=V)),Y("log",{activity:o,dimensions:i,schemaId:"<ns>.PageInteractionsSummary.1"},{ent:{page:["pageType","subPageType","requestId"]}})}}function mn(){fn(),dn(en)}function pn(n,e){return function(){_=e,n()}}function gn(){Z=function(){return _},_&&!r&&(r=A())}"function"!=typeof J[h]||X||(on(),p&&rn(),B(k,w,un,{passive:!0}),B(k,"blur",mn),B(k,"focus",pn(sn,1)),G(b+"android",gn),G(b+"ios",gn),B(b+"pause",pn(mn,0)),B(b+"resume",pn(sn,1)),B(b+"resign",pn(mn,0)),B(b+"active",pn(sn,1)),Z()&&(r=V||A()),G("$beforeunload",dn),B("$beforeunload",dn),B("$document.hidden",mn),B("$beforePageTransition",dn),B("$afterPageTransition",function(){tn=j=1}))});csa.plugin(function(e){var o,n,r="<ns>.Navigator.4",a=e.global,i=a.navigator||{},d=i.connection||{},c=a.Math.round,t=e("Events",{producerId:"csa"});function l(){o={network:{downlink:void 0,downlinkMax:void 0,rtt:void 0,type:void 0,effectiveType:void 0,saveData:void 0},language:void 0,doNotTrack:void 0,hardwareConcurrency:void 0,deviceMemory:void 0,cookieEnabled:void 0,webdriver:void 0},v(),o.language=i.language||null,o.doNotTrack=function(){switch(i.doNotTrack){case"1":return"enabled";case"0":return"disabled";case"unspecified":return i.doNotTrack;default:return null}}(),o.hardwareConcurrency="hardwareConcurrency"in i?c(i.hardwareConcurrency||0):null,o.deviceMemory="deviceMemory"in i?c(i.deviceMemory||0):null,o.cookieEnabled="cookieEnabled"in i?i.cookieEnabled:null,o.webdriver="webdriver"in i?i.webdriver:null}function u(){t("log",{network:(n={},Object.keys(o.network).forEach(function(e){n[e]=o.network[e]+""}),n),language:o.language,doNotTrack:o.doNotTrack,hardwareConcurrency:o.hardwareConcurrency,deviceMemory:o.deviceMemory,cookieEnabled:o.cookieEnabled,webdriver:o.webdriver,schemaId:r},{ent:{page:["pageType","subPageType","requestId"]}})}function v(){!function(n){Object.keys(o.network).forEach(function(e){o.network[e]=n[e]})}({downlink:"downlink"in d?c(d.downlink||0):null,downlinkMax:"downlinkMax"in d?c(d.downlinkMax||0):null,rtt:"rtt"in d?(d.rtt||0).toFixed():null,type:d.type||null,effectiveType:d.effectiveType||null,saveData:"saveData"in d?d.saveData:null})}function k(){v(),u()}function w(){l(),u()}l(),u(),e.on("$afterPageTransition",w),e.on(d,"change",k)});
(function(t,z,C){var u=function(){var a,c=function(){return null!=a?a:a=function(){var a=[],c="unknown",b={trident:0,gecko:0,presto:0,webkit:0,unknown:-1},d,e={},c=document.createElement("nadu");for(d in c.style)if(c=(/^([A-Za-z][a-z]*)[A-Z]/.exec(d)||[])[1])c=c.toLowerCase(),c in e?e[c]++:e[c]=1;for(var n in e)a.push([n,e[n]]);a=a.sort(function(a,c){return c[1]-a[1]}).slice(0,10);for(d=0;d<a.length;d++)switch(a[d][0]){case "moz":b.gecko+=5;break;case "ms":b.trident+=5;break;case "get":b.webkit++;
break;case "webkit":b.webkit+=5;break;case "o":b.presto+=2;break;case "xv":b.presto+=2}"onhelp"in window&&b.trident++;"maxConnectionsPerServer"in window&&b.trident++;try{void 0!==window.ActiveXObject.toString&&(b.trident+=5)}catch(r){}void 0!==function(){}.toSource&&(b.gecko+=5);var a="unknown",q;for(q in b)b[q]>b[a]&&(a=q);return a}()},b=function(){return!!window.opera||!!window.opr&&!!window.opr.addons},d=function(){return!!document.documentMode},e=function(){return!d()&&"undefined"!==typeof CSS&&
CSS.supports("(-ms-ime-align:auto)")},n=function(){return"webkit"==c()},r=function(){return void 0!==z.chrome&&"Opera Software ASA"!=navigator.vendor&&void 0===navigator.msLaunchUri&&n()};return{isOpera:b,isIE:d,isEdge:e,isFirefox:function(){return"undefined"!==typeof InstallTrigger},isWebkit:n,isChrome:r,isSafari:function(){return!r()&&!e()&&!b()&&"WebkitAppearance"in document.documentElement.style}}}(),q=function(a,c,b,d){a.addEventListener?a.addEventListener(c,b,d):a.attachEvent&&a.attachEvent("on"+
c,b)},r=function(a,c,b,d){document.removeEventListener?a.removeEventListener(c,b,d||!1):document.detachEvent&&a.detachEvent("on"+c,b)},H=function(a){var c;a=a.document;"undefined"!==typeof a.hidden?c="visibilitychange":"undefined"!==typeof a.mozHidden?c="mozvisibilitychange":"undefined"!==typeof a.msHidden?c="msvisibilitychange":"undefined"!==typeof a.webkitHidden&&(c="webkitvisibilitychange");return c},T=function(a,c){var b=H(a),d=a.document;b&&q(d,b,c,!1)},U=function(a){var c=window.addEventListener?
"addEventListener":"attachEvent";(0,window[c])("attachEvent"==c?"onmessage":"message",function(c){a(c[c.message?"message":"data"])},!1)},V=function(a,c){"function"===typeof a&&Math.random()<c/100&&a.call(this)},v=function(a){try{for(var c=Array.prototype.slice.call(arguments,1),b=0;b<c.length;b++){if(!a)return!0;var d=a[c[b]];if(null===d||void 0===d)return!0;a=d}return!1}catch(e){return!0}},A=function(a){try{if(!a)return a;for(var c=Array.prototype.slice.call(arguments,1),b,d=0;d<c.length;d++){b=
a[c[d]];if(!b)break;a=b}return b}catch(e){return null}},W=function(a,c){try{if(!a)return!1;for(var b=Array.prototype.slice.call(arguments,2),d=0;d<b.length;d++){var e=a[b[d]];if(null===e||void 0===e)return d===b.length-1?typeof e===c:!1;a=e}return typeof e===c}catch(n){return!1}},I=function(a){a&&document.body&&a.parentNode===document.body&&document.body.removeChild(a)},J=function(a,c,b){var d=window.document.createElement("IFRAME");d.id=c;d.height="5px";d.width="5px";d.src=b?b:"javascript:'1'";d.style.position=
"absolute";d.style.top="-10000px";d.style.left="-10000px";d.style.visibility="hidden";d.style.opacity=0;window.document.body.appendChild(d);try{var e=d.contentDocument;if(e&&(e.open(),e.writeln("<!DOCTYPE html><html><head><title></title></head><body></body></html>"),e.close(),a)){var r=e.createElement("script");r&&(r.type="text/javascript",r.text=a,e.body.appendChild(r))}}catch(q){n(q,"JS exception while injecting iframe")}return d},n=function(a,c){t.ueLogError(a,{logLevel:"ERROR",attribution:"A9TQForensics",
message:c})},X=function(a,c,b){a={vfrd:1===c?"8":"4",dbg:a};"object"===typeof b?a.info=JSON.stringify(b):"string"===typeof b&&(a.info=b);return{server:window.location.hostname,fmp:a}};(function(a){function c(a,c,b){var d="chrm msie ffox sfri opra phnt slnm othr extr xpcm invs poev njs cjs rhn clik1 rfs uam clik stln mua nfo hlpx clkh mmh chrm1 chrm2 wgl srvr zdim nomime chrm3 otch ivm.tst ivm.clk mmh2 clkh2 achf nopl spfp4 uam1 lsph nmim1 slnm2 crtt spfp misp spfp1 spfp2 clik2 clik3 spfp3 estr".split(" ");
F=a<d.length?d[a]:"othr";t.ue&&t.ue.event&&t.ue.event(X(F,c,b),"a9_tq","a9_tq.FraudMetrics.3")}function b(){var c=!1,m="",b=6,d=function(a,c){var f,m,b=!1;for(f in a)b=b||-1<c.indexOf(f);if("function"===typeof Object.getOwnPropertyNames)for(f=Object.getOwnPropertyNames(a),m=0;m<f.length;m++)b=b||-1<c.indexOf(f[m]);if("function"===typeof Object.keys)for(f=Object.keys(a),m=0;m<f.length;m++)b=b||-1<c.indexOf(f[m]);return b},k=function(a){try{return!!a.toString().match(/\{\s*\[native code\]\s*\}$/m)}catch(c){return!1}},
l=0;"undefined"!==typeof _evaluate&&-1<_evaluate.toString().indexOf("browser.runScript")&&l++;"undefined"!==typeof ArrayBuffer&&"undefined"!==typeof print&&k(ArrayBuffer)&&!k(print)&&l++;"undefined"!==typeof ABORT_ERR&&l++;try{"undefined"!==typeof browser&&"undefined"!==typeof browser._windowInScope&&"undefined"!==typeof browser._windowInScope._response&&l++}catch(Z){}3<=l&&(c=!0);k=[function(){if(!0===d(C,"__webdriver_evaluate __selenium_evaluate __fxdriver_evaluate __driver_evaluate __webdriver_unwrapped __selenium_unwrapped __fxdriver_unwrapped __driver_unwrapped __webdriver_script_function __webdriver_script_func __webdriver_script_fn webdriver _Selenium_IDE_Recorder _selenium calledSelenium $cdc_asdjflasutopfhvcZLmcfl_ $chrome_asyncScriptInfo __$webdriverAsyncExecutor".split(" ")))return!0;
var c=function(c){return c.match(/\$[a-z]dc_/)&&a.document[c]&&a.document[c].cache_},f;for(f in C)if(c(f))return m=f,!0;if("function"===typeof Object.getOwnPropertyNames)for(var b=Object.getOwnPropertyNames(C),l=0;l<b.length;l++)if(c(b[l]))return m=f,!0;return!1},function(){return d(a,"_phantom __nightmare _selenium callPhantom callSelenium _Selenium_IDE_Recorder webdriver __webdriverFunc domAutomation domAutomationController __lastWatirAlert __lastWatirConfirm __lastWatirPrompt _WEBDRIVER_ELEM_CACHE".split(" "))||
"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Promise||"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Array||"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Symbol?!0:!1},function(){return a.webdriver||a.document.webdriver||a.document.documentElement.hasAttribute("webdriver")||a.document.documentElement.hasAttribute("selenium")||a.document.documentElement.hasAttribute("driver")||navigator.webdriver||A(p,"navigator","webdriver")||"object"===typeof a.$cdc_asdjflasutopfhvcZLmcfl_||"object"===typeof a.document.$cdc_asdjflasutopfhvcZLmcfl_||
null!=a.name&&-1<a.name.indexOf("driver")?(m=null!=a.name?a.name:"",!0):!1},function(){return a.external&&"function"===typeof a.external.toString&&a.external.toString()&&-1!=a.external.toString().indexOf("Sequentum")?(m=a.external.toString(),!0):!1},function(){for(var c in a){var f;a:{if((f=c)&&33<=f.length&&"function"===typeof a[f]){var b=a[f];if(/\.*_Array$/.test(f)||/\.*_Promise$/.test(f)||/\.*_Symbol$/.test(f)||34===f.length&&"resolve"in b&&"reject"in b&&"prototype"in b||33===f.length&&"isConcatSpreadable"in
b&&"unscopables"in b&&"toStringTag"in b&&"match"in b){f=!0;break a}}f=!1}if(f)return m=c,!0}return!1},function(){var a=!1;if(!u.isFirefox())return!1;var c;c=navigator.userAgent.match(/(firefox(?=\/))\/?\s*(\d+)/i)||[];c=3<=c.length?c[2]:null;if(!c)return!1;60<=c&&void 0===navigator.webdriver?a=!0:60>c&&"webdriver"in navigator&&(a=!0);return a?(b=43,m=c.toString(),!0):!1}];for(l=0;l<k.length;l++)if(k[l].call()){c=!0;break}return{isSel:c,isTest:!1,info:m,headlessCode:b}}function d(a){var b=new Date;
!v(a,"Function","prototype","toString")&&W(b,"function","toLocaleString")&&(a=a.Function.prototype.toString.call(b.toLocaleString))&&100<a.length&&0<=a.indexOf("this.getTime")&&c(41)}function e(){var a="AddChannel AddDesktopComponent AddFavorite AddSearchProvider AddService AddToFavoritesBar AutoCompleteSaveForm AutoScan bubbleEvent ContentDiscoveryReset ImportExportFavorites InPrivateFilteringEnabled IsSearchProviderInstalled IsServiceInstalled IsSubscribed msActiveXFilteringEnabled msAddSiteMode msAddTrackingProtectionList msClearTile msEnableTileNotificationQueue msEnableTileNotificationQueueForSquare150x150 msEnableTileNotificationQueueForSquare310x310 msEnableTileNotificationQueueForWide310x150 msIsSiteMode msIsSiteModeFirstRun msPinnedSiteState msProvisionNetworks msRemoveScheduledTileNotification msReportSafeUrl msScheduledTileNotification msSiteModeActivate msSiteModeAddButtonStyle msSiteModeAddJumpListItem msSiteModeAddThumbBarButton msSiteModeClearBadge msSiteModeClearIconOverlay msSiteModeClearJumpList msSiteModeCreateJumpList msSiteModeRefreshBadge msSiteModeSetIconOverlay msSiteModeShowButtonStyle msSiteModeShowJumpList msSiteModeShowThumbBar msSiteModeUpdateThumbBarButton msStartPeriodicBadgeUpdate msStartPeriodicTileUpdate msStartPeriodicTileUpdateBatch msStopPeriodicBadgeUpdate msStopPeriodicTileUpdate msTrackingProtectionEnabled NavigateAndFind raiseEvent setContextMenu ShowBrowserUI menuArguments onvisibilitychange scrollbar selectableContent version visibility mssitepinned AddUrlAuthentication CloseRegPopup FeatureEnabled GetJsonWebData GetRegValue Log LogShellErrorsOnly OpenPopup ReadFile RunGutsScript SaveRegInfo SetAppMaximizeTimeToRestart SetAppMinimizeTimeToRestart SetAutoStart SetAutoStartMinimized SetMaxMemory ShareEventFromBrowser ShowPopup ShowRadar WriteFile WriteRegValue summonWalrus".split(" "),
b=-1,d,h;"Microsoft Internet Explorer"===navigator.appName?(d=navigator.userAgent,h=/MSIE ([0-9]{1,}[\.0-9]{0,})/,null!==h.exec(d)&&(b=parseFloat(RegExp.$1))):"Netscape"===navigator.appName&&(d=navigator.userAgent,h=/Trident\/.*rv:([0-9]{1,}[\.0-9]{0,})/,null!==h.exec(d)&&(b=parseFloat(RegExp.$1)));if(-1===b&&null===navigator.userAgent.match(/Windows Phone/)&&window.external){for(d=b=0;d<a.length;d++)if("unknown"===typeof window.external[a[d]]){b++;break}0<b&&c(17)}}function z(){var f=a.navigator.userAgent;
if(f&&!/8.0 Safari|iPhone|iPad/.test(f)){var b={clearInterval:42,clearTimeout:41,eval:33,alert:34,prompt:35,scroll:35},d={clearInterval:46,clearTimeout:45,eval:37,alert:38,prompt:39,scroll:39},h=0;if(/Chrome/.test(f))d=b;else if(b=/Firefox/.test(f),f=/Safari/.test(f),!b&&!f)return;if(Function.prototype&&Function.prototype.toString)for(var k in d)"function"===typeof window[k]&&(f=Function.prototype.toString.call(window[k]))&&f.length!==d[k]&&(h+=1);3<=h&&(6<=h?c(40,0,h.toString()):c(40,1,h.toString()))}}
function S(){var a=Math.random().toString(36).substr(2),b=null;U(function(d){try{var h=d.split(" ");if(null!==b&&h[0]===a&&0<h[1].length){var k=JSON.parse(h[1]);for(d=0;d<k.length;d++)1==d&&"R29vZ2xlIFN3aWZ0U2hhZGVy"==k[d]&&c(27)}}catch(l){}});b=J('(function fg45s() {                     var payload = [];                     var canvas = document.createElement("canvas");                     var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl") || canvas.getContext("moz-webgl");                     if (gl != null) {                         var debugInfo = gl.getExtension("WEBGL_debug_renderer_info");                         if (debugInfo != null) {                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL)));                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL)));                             parent.postMessage(window.frameElement.id + " " + JSON.stringify(payload), parent.location.origin);                         }                     }                 }             )();',
a);window.setTimeout(function(){try{b&&document.body&&b.parentNode===document.body&&document.body.removeChild(b),b=null}catch(a){n(a,"JS exception while removing iframe")}},5E3)}function L(){function b(){r(a,"mousemove",e);r(a,"click",d)}function d(){try{c(23),b(),r(a.document,l,h)}catch(m){n(m,"JS exception - detectClickDuringTabInactive")}}function e(){try{k||(k=!0,c(24),b(),r(a.document,l,h))}catch(d){n(d,"JS exception - detectMouseMovementsDuringTabInactive")}}function h(){try{var c;"undefined"!==
typeof document.hidden?c="hidden":"undefined"!==typeof document.mozHidden?c="mozHidden":"undefined"!==typeof document.msHidden?c="msHidden":"undefined"!==typeof document.webkitHidden&&(c="webkitHidden");!0!==document[c]===!1?(q(a,"mousemove",e,!1),q(a,"click",d,!1)):b()}catch(l){n(l,"JS exception - handleVisibilityChangeDuringTabInactive")}}var k=!1,l=H(a);T(a,h)}var M=function(){var a=window.navigator,c=a.vendor,b="undefined"!==typeof window.opr,d=-1<a.userAgent.indexOf("Edg"),a=/Chrome/.test(a.userAgent);
return/Google Inc\./.test(c)&&a&&!b&&!d},F=null,N=function(a){var b=[],d=(new Date).getTime(),h=!1,k=!1,l,e,D=function(){r(a,"mousemove",s);r(a,"click",g)},s=function(a){try{var f=(new Date).getTime();if(!(100>f-d)){b.push({x:a.clientX,y:a.clientY});if(50<b.length&&(b.shift(),!(50>b.length))){var l=b[0].x,g=b[49].x,k=b[0].y,h=b[49].y;a=h-k;for(var e=l-g,l=k*g-l*h,g=a/e*-1,s=b[49].ts-b[0].ts,k=!0,h=0;h<b.length;h++)if(0!=a*b[h].x+e*b[h].y+l){k=!1;break}!0==k&&(s={grdt:g,tmsp:s},D(),c(19,0,s))}d=f}}catch(B){n(B,
"JS exception - recordHoverPosition")}},g=function(a){try{var d=a.clientX,f=a.clientY,l={hcc:b.length,cx:d,cy:f};if(0===b.length)D(),c(18,0,l);else if(null!=d&&null!=f){var g;l.hpos=b;var k=b[b.length-1];g=Math.sqrt(Math.pow(d-k.x,2)+Math.pow(f-k.y,2));100<g&&(l.hcc=b.length,l.cx=d,l.cy=f,l.dhp=g,D(),c(15,0,l))}}catch(h){n(h,"JS exception - checkClick")}},B=function(c){try{l=c.clientX,e=c.clientY,h=!0,r(a,"mouseup",B)}catch(b){n(b,"JS exception - checkMouseUp")}},p=function(){try{k=!0,r(a,"mousedown",
p)}catch(c){n(c,"JS exception - checkMouseDown")}},t=function(b){try{h||k||c(49);var d=b.clientX-l,g=b.clientY-e;0<d&&1>d&&0<g&&1>g&&c(50,0,{xDiff:d,yDiff:g});r(a,"click",t)}catch(m){n(m,"JS exception - checkFirstClick")}};q(a,"mousemove",s,!1);q(a,"mouseup",B,!1);q(a,"mousedown",p,!1);q(a,"click",t,!1);q(a,"click",g,!1)},O=function(){if(u.isFirefox()){var a=0;void 0!==window.onstorage&&a++;var b=document.createElement("div");b.style.wordSpacing="22%";"22%"===b.style.wordSpacing&&a++;"function"===
typeof b.getAttributeNames&&a++;2<a&&(void 0===window.onabsolutedeviceorientation||void 0===navigator.permissions)&&c(37,0,a)}},w=function(){return null===navigator.userAgent.match(/(iPad|iPhone|iPod|android|webOS)/i)},G=function(a,b){var d=a&&a.navigator;!d||!w()||d.mimeTypes&&0!=d.mimeTypes.length||(x?c(b,0,"chrm"):u.isFirefox()&&c(b,0,"ff"))},R=function(){var a=function(a,c){for(var b,d="",f={},e={},s=0,g=0;g<c.length;g++)e[c[g]]=String.fromCharCode(126-g);var s=0,m;for(m in a)-1<c.indexOf(m)&&
(f[m]=1,s++);d=d+s+"!";if("function"===typeof Object.getOwnPropertyNames){b=Object.getOwnPropertyNames(a);for(g=s=0;g<b.length;g++)-1<c.indexOf(b[g])&&(f[b[g]]=1,s++);d=d+s+"!"}if("function"===typeof Object.keys){b=Object.keys(a);for(g=s=0;g<b.length;g++)-1<c.indexOf(b[g])&&(f[b[g]]=1,s++);d=d+s+"!"}if("prototype"in Object&&"hasOwnProperty"in Object.prototype)for(m in f)Object.prototype.hasOwnProperty.call(f,m)&&(d+=e[m]);else for(m in f)d+=e[m];return encodeURIComponent(d)},c=document.createElement("nadu"),
a={w:a(window,"SVGFESpotLightElement XMLHttpRequestEventTarget onratechange StereoPannerNode dolphinInfo VTTCue globalStorage WebKitCSSRegionRule MozSmsFilter MediaController mozInnerScreenX onwebkitwillrevealleft DOMMatrix GeckoActiveXObject MediaQueryListEvent PhoneNumberService ServiceWorkerContainer yandex vc2hxtaq9c NavigatorDeviceStorage HTMLHtmlElement ScreenOrientation MSGesture mozCancelRequestAnimationFrame GetSVGDocument MediaSource webkitMediaStream DeviceMotionEvent webkitPostMessage doNotTrack WebKitMediaKeyError HTMLCollection InstallTrigger StorageObsolete CustomEvent orientation XMLHttpRequest Worker showModelessDialog EventSource onmouseleave SVGAnimatedPathData TouchList TextTrackCue onanimationend HTMLBodyElement fluid MSFrameUITab Generator SecurityPolicyViolationEvent ClientRectList SmartCardEvent CSSSupportsRule mmbrowser".split(" ")),
c:a(c.style,"XvPhonemes MozTextAlignLast webkitFilter MozPerspective msTextSizeAdjust OAnimationFillMode borderImageSource MozOSXFontSmoothing border-inline-start-color MozOsxFontSmoothing columns touchAction scroll-snap-coordinate webkitAnimationFillMode webkitLineSnap webkitGridAutoColumns animationDuration isolation overflowWrap offsetRotation webkitShapeOutside MozOpacity position justifySelf borderRight webkitMatchNearestMailBlockquoteColor msImeAlign parentRule MozColumnFill cssText borderRightStyle textOverflow webkitGridRow webkitBackgroundComposite length -moz-column-fill enableBackground flex-basis".split(" "))};
t.ue&&t.ue.event&&(a={vfrd:"0",info:JSON.stringify(a)},t.ue.event({server:window.location.hostname,fmp:a},"a9_tq","a9_tq.FraudMetrics.3"))},P=function(){var b=function(a){try{return"function"!==typeof a||v(p,"Function","prototype","toString")?null:p.Function.prototype.toString.call(a)}catch(b){return null}},d=function(a,c){try{if("function"!==typeof Object.getOwnPropertyDescriptor)return null;var d=Object.getPrototypeOf(a);if(!d)return null;var e=Object.getOwnPropertyDescriptor(d,c);return e?b(e.get):
null}catch(g){return null}},e=function(a){var b=[28,161,141];!v(a,"getDetails","a")&&"s"===a.getDetails.a&&0<=b.indexOf(a.getDetails.l)&&c(45,0,k)},h=function(){(function(){if("function"===typeof Object.getOwnPropertyNames&&w()){var a=Object.getOwnPropertyNames(navigator);a&&1<a.length&&c(47,0,a.length.toString())}})();0<navigator.hardwareConcurrency&&!v(p,"navigator","hardwareConcurrency")&&p.navigator.hardwareConcurrency!==navigator.hardwareConcurrency&&c(48,0,p.navigator.hardwareConcurrency.toString());
(function(){var b=[];if(!v(p,"navigator")){p===a&&(b.push("iwin"),c(51,0,b));for(var d="platform vendor maxTouchPoints userAgent deviceMemory webdriver hardwareConcurrency appVersion mimeTypes plugins languages".split(" "),f=0;f<d.length;f++){var e=d[f],g;if("object"===typeof navigator[e]){g=navigator[e];var h=p.navigator[e],k=!1;g||h?(g&&h?g.length!==h.length?k=!0:0<g.length&&0<h.length&&"string"===typeof g[0]&&g[0]!==h[0]&&(k=!0):k=!0,g=k):g=!1}else g=navigator[e],h=p.navigator[e],g=g||h?g!==h?
!0:!1:!1;g&&b.push(e)}0<b.length&&(0<=b.indexOf("webdriver")?c(51,0,b):c(39,1,b))}})()},k=function(a){if(!a)return null;for(var c={},e=0,h=0,g=0;g<a.length;g++)for(var k=a[g].obj,n=a[g].props,r=0;r<n.length;r++){var p=n[r];c[p]={};var q=A(k,n[r]);if(null===q||void 0===q)h+=1,c[p].a="m",c[p].l=0;else if(q="function"===typeof q?b(q):d(k,p))q&&!/\[native code\]/.test(q)?(c[p].a="s",e+=1):c[p].a="p",c[p].l=q.length}return{sig:c,sCount:e,mCount:h}}([{obj:A(a,"chrome","app"),props:["getDetails","getIsInstalled",
"runningState"]},{obj:a.chrome,props:["csi","loadTimes","runtime"]},{obj:navigator,props:"platform vendor userAgent mimeTypes plugins webdriver languages".split(" ")}]);k&&(e(k.sig),x&&w()&&3<=k.mCount&&(6<=k.mCount?c(46,0,k):c(46,1,k)),h())},Q=function(){var b=a.Document&&a.Document.prototype.evaluate;b&&(a.Document.prototype.evaluate=function(){try{var d=Error("test error"),e=d.stack&&d.stack.toString();e&&e.match(/(puppeteer|phantomjs|apply.xpath)/)&&c(52,0,e);a.Document.prototype.evaluate=b;return b.apply(this,
arguments)}catch(h){return n(h,"JS exception while overidding evaluate"),a.Document.prototype.evaluate=b,b.apply(this,arguments)}})};try{v(navigator,"userAgent")&&c(20);var x=M(),y,p;(a.callPhantom||a._phantom||a.PhantomEmitter||a.__phantomas||/PhantomJS/.test(navigator.userAgent))&&c(5);a.Buffer&&c(12);a.emit&&c(13);a.spawn&&c(14);(null!=a.domAutomation||null!=a.domAutomationController||null!=a._WEBDRIVER_ELEM_CACHE||/HeadlessChrome/.test(navigator.userAgent)||""===navigator.languages)&&c(0);if(u.isChrome()&&
a.webkitRequestFileSystem)a.webkitRequestFileSystem(a.TEMPORARY,1,function(){},function(){c(0)});else if(u.isSafari()&&a.localStorage){try{a.localStorage.setItem("__nadu","")}catch($){c(3)}a.localStorage.removeItem("__nadu")}G(a,30);u.isWebkit()&&x&&w()&&(void 0===a.chrome&&c(0),a.chrome&&a.chrome.app&&!1!==a.chrome.app.isInstalled&&void 0!==navigator.languages&&c(31));a.external&&"function"===typeof a.external.toString&&a.external.toString()&&-1<a.external.toString().indexOf("RuntimeObject")&&c(8);
a.FirefoxInterfaces&&"function"===typeof a.FirefoxInterfaces&&a.FirefoxInterfaces("wdICoordinate","wdIMouse","wdIStatus")&&c(2);a.XPCOMUtils&&c(9);(a.Components&&(a.Components.interfaces&&a.Components.interfaces.nsICommandProcessor||a.Components.wdICoordinate||a.Components.wdIMouse||a.Components.wdIStatus||a.Components.classes)||a.netscape&&a.netscape.security&&a.netscape.security.privilegemanager)&&c(8);a.isExternalUrlSafeForNavigation&&c(1);!a.opera||null===a.opera._browserjsran||0!==a.opera._browserjsran&&
!1!==a.opera._browserjsran||c(4);a.screen&&(1>=a.screen.availHeight||1>=a.screen.availWidth||1>=a.screen.height||1>=a.screen.width||0>=a.screen.devicePixelRatio)&&c(10);var E=window.setInterval(function(){try{var a=b();a.isSel&&(c(a.headlessCode,!0===a.isTest?1:0,a.info),window.clearInterval(E),I(y))}catch(d){window.clearInterval(E),n(d,"JS exception - detectSelenium")}},1E3);window.setTimeout(function(){try{window.clearInterval(E),I(y)}catch(a){n(a,"JS exception - clearInterval for detectSelenium")}},
1E4);var K=a.PointerEvent;a.PointerEvent=function(){c(11);if(void 0!==K){var a=Array.prototype.slice.call(arguments);return new K(a)}return null};e();N(a);L();S();0!==a.outerHeight&&0!==a.outerWidth||c(29);O();!w()||navigator.plugins&&0!=navigator.plugins.length||(x?c(38,0,"chrm"):u.isFirefox()&&c(38,0,"ff"));V(R,10);x&&w()&&a.chrome&&!a.chrome.csi&&!a.chrome.loadTimes&&c(25);z();y=J(null,Math.random().toString(36).substr(2));p=v(y,"contentWindow")?a:y.contentWindow;d(p);G(p,42);0===A(navigator,"connection",
"rtt")&&c(44);P();Q()}catch(Y){n(Y,"JS exception - ")}})(z)})(ue_csm,window,document);



ue.exec(function(d,c){function g(e,c){e&&ue.tag(e+c);return!!e}function n(){for(var e=RegExp("^https://(.*\.(images|ssl-images|media)-amazon\.com|"+c.location.hostname+")/images/","i"),d={},h=0,k=c.performance.getEntriesByType("resource"),l=!1,b,a,m,f=0;f<k.length;f++)if(a=k[f],0<a.transferSize&&a.transferSize>=a.encodedBodySize&&(b=e.exec(String(a.name)))&&3===b.length){a:{b=a.serverTiming||[];for(a=0;a<b.length;a++)if("provider"===b[a].name){b=b[a].description;break a}b=void 0}b&&(l||(l=g(b,"_cdn_fr")),
a=d[b]=(d[b]||0)+1,a>h&&(m=b,h=a))}g(m,"_cdn_mp")}d.ue&&"function"===typeof d.ue.tag&&c.performance&&c.location&&n()},"cdnTagging")(ue_csm,window);


}
/* ◬ */
</script>

</div>

<noscript>
    <img height="1" width="1" style='display:none;visibility:hidden;' src='//fls-na.amazon.com/1/batch/1/OP/ATVPDKIKX0DER:139-5329492-5095613:BNJYY9EBY54VZZF6X4X6$uedata=s:%2Frd%2Fuedata%3Fnoscript%26id%3DBNJYY9EBY54VZZF6X4X6:0' alt=""/>
</noscript>

<script>window.ue && ue.count && ue.count('CSMLibrarySize', 85399)</script>
<!-- sp:end-feature:csm:body-close -->
</div>


<div class="brand-follow-tooltip-root"></div><input type="hidden" id="lists-createlist-createAndAddAsin"><div id="a-popover-root" style="z-index:-1;position:absolute;"></div></body></html>"""

class ScraperError(Exception):
    pass


class Scraper:

    """
    Webscraping program for gathering data on different genres from the Book Depository website
    """

    def __init__(self, keyword: str, number_of_items: int, availability: str, sortBy: str, format: str) -> None:
        """
        Initialises the object instance
        Args:
           keyword (str): The genre of book to scrape
           number_of_items (int): Number of pages to scrape
           availability (str): "1" for in-stock, "2" for pre-order, nothing for both
           sortBy (str): "popularity", ...others
           format (str): "1" for paperback, ...others (see on webpage), nothing for everything

        Returns:
            None
        """

        self.__headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
        self.keyword = keyword
        self.availability = availability
        self.sortBy = sortBy
        self.format = format
        self.number_of_items = number_of_items
       
    def get_url(self) -> list:
        """
        Fetches the urls of the pages to be scraped

        Returns:
            urls (list): Urls of the pages to be scraped
            
        """

        #TODO - add variables
        #base_url= f"https://www.bookdepository.com/search?searchTerm={self.keyword}&format={self.format}&availability={self.availability}&searchSortBy={self.sortBy}"
        base_url= f"https://www.amazon.com/s?k=bookstore+amazon&i=stripbooks&rh=n%3A283155%2Cn%3A17%2Cp_n_condition-type%3A6461716011&dc&ds=v1%3A0DnYcXYEkDrwoSuEn1zkiz12phKKtb1L855OLVhOjk8&hvadid=623182854892&hvdev=c&hvlocint=9061323&hvlocphy=1000060&hvnetw=g&hvqmt=b&hvrand=6662995798799223789&hvtargid=kwd-13263126&hydadcr=20698_13296112&qid=1682200770&rnid=6461714011&tag=googhydr-20&ref=sr_nr_p_n_condition-type_1"
        urls= []
        urls.append(base_url)
        return urls

    def request_page(self, url: str):
        """
        Makes a request to the webpage to be scraped
        Args:
            url (str): Url of the page to be scraped

        Returns:
            page (requests.Response): Object containing the server's response to the HTTP request    
                
        """ 

        client = ScrapingAntClient(token='234575b095fc498f86b3a5a498c3c277')
        # Scrape the example.com site.
        result = client.general_request(url)

        if result.status_code != 200:
            print("Error processing request")
        return result.content

    def create_soup(self, content):
        """
        Parses the html
        Args:
            content (str): string containing the server's response to the HTTP request 

        Returns:
            soup: bs4.BeautifulSoup object
            
        """
        soup= BeautifulSoup(content, 'html.parser')
        return soup

    def get_book_title(self, soup) -> str:
        """
        Extracts the title of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            title (str): title of the book
            
        """
        title = None
        try:
            title= soup.find('meta', {'itemprop': "name"})['content']  
        except ScraperError:
            raise ScraperError
        finally:
            return title
        
    def get_book_image(self, soup) -> str:
        """
        Extracts the title of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            title (str): title of the book
            
        """
        title = None
        try:
            title= soup.find('img')['src']
        except ScraperError:
            raise ScraperError
        except KeyError:
            title = soup.find('img')['data-lazy']
        finally:
            return title
        
    def get_book_author(self, soup) -> str:
        """
        Extracts the author of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            price (float): Price of the book
            
        """
        author = None
        try:
            author = soup.find('span', {'itemprop': "name"}).text
        except ScraperError:
            raise ScraperError     
        finally:
            return author

    def get_book_format(self, soup) -> str:
        """
        Extracts the format of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            format (str): Edition of the book
            
        """
        format = None
        try:
            format= soup.find('p', {'class': "format"}).text  
        except ScraperError:
            raise ScraperError     
        finally:
            return format

    def get_publication_date(self, soup)-> str:
        """
        Extracts the publication date of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            date_published (str): publication date of the book
            
        """
        date_published = None
        try:
            date_published = soup.find('p', {'class': "published"}).text
        except ScraperError:
            raise ScraperError     
        finally:
            return date_published
            
    def get_book_ISBN(self, soup) -> str: 
        """
        Extracts the ISBN of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            ISBN (str): ISBN of the book
            
        """
        isbn = None
        try:
            isbn = soup.find("meta", {"itemprop": "isbn"})['content']     
        except ScraperError:
            raise ScraperError     
        finally:
            return isbn

    def get_book_rating(self, soup) -> str:
        """
        Extracts the rating of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            rating (str): rating of the book
            
        """
        rating = None
        try:
            rating= str(len(soup.find_all('span', {'class': "star full-star"}))) + '/5'
        except ScraperError:
            raise ScraperError
        
        finally:
            return rating

    def get_book_price(self, soup) -> str:
        """
        Extracts the price of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            price (str): Price of the book
            
        """
        price = None
        try:
            price = soup.find('strong', attrs={'style': "font-size: 1.5em;"}).find('span').text
        except ScraperError:
            raise ScraperError     
        finally:
            return price

    def get_book_model(self, soup) -> str:
        """
        Extracts the book's JSON model

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            model (obj): JSON of the book's model
            
        """
        model = None
        try:
            model = json.loads(soup.find('script', type='application/ld+json').string)
        except ScraperError:
            raise ScraperError     
        finally:
            return model
           
    def create_dataframe(self, data_list: list, columns:list) -> pd.DataFrame:
        """
        Creates a dataframe from a list

        Args:
            data_list (list): list of values
            columns (list): column labels to use for the resulting dataframe

        Returns:
            data (pd.DataFrame): a dataframe of the list of values 
        """
        data= pd.DataFrame(data_list, columns= columns)
        return data


    def create_csv(self, data: pd.DataFrame, file_title: str) -> None:
        """
        Converts a dataframe to a csv

        Args:
            data (pd.DataFrame): the dataframe to be converted to csv
            file_title (str): title of the output file

        Returns:
            None   
        """
        data.to_csv(f'{file_title}.csv', index= False)

    def scrape_data_lite (self) -> pd.DataFrame:
        """
        Scrapes the Book Depository website and returns a dataframe of the specific genre.

        Returns:
            data: A dataframe of all the books scraped
        """
        #page=requests.get("https://www.bookfinder.com/search/?isbn=9781594634024&mode=isbn&st=sr&ac=qr", headers=self.__headers)
        #print(page.text)
        data_list= [] 
        urls= self.get_url()
        for url in urls:
            content= self.request_page(url)
            print(content)
            #content= html_str
            soup= self.create_soup(content)
            books= soup.find_all('div', {'class': "search-column"})
            num_book= 0
            for book in books:
                book_model= self.get_book_model(book)
                title= book_model['name']
                # title= self.get_book_title(book)
                author= book_model['author']
                # author= self.get_book_author(book)
                format= book_model['bookFormat']
                # format= self.get_book_format(book)
                image= book_model['image']
                # image= self.get_book_image(book)
                #TODO - Fix date
                date_published= "12/04/2020"
                isbn= book_model['isbn']
                # isbn= self.get_book_ISBN(book)
                #TODO - Fix rating
                rating= "5/5"
                # rating= self.get_book_rating(book)
                price= self.get_book_price(book)
                data_list.append([self.keyword, title, author, format, image,
                                    date_published, isbn,
                                    rating, price
                                    ])
                num_book+= 1
                print (f'{num_book} book(s) has been scraped and appended')
        data= self.create_dataframe(data_list, columns= ["genre", "title", "author", "format", "image",
                                "date_published", "ISBN",
                                "rating", "price"
                                ])
        
        return data
