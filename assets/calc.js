(function(){
var $=function(i){return document.getElementById(i)};
function f(n){return '$'+Math.round(n).toLocaleString('en-US')}
function gd(r,plan){if(plan=='basic'){var c=49;for(var i=2;i<=r;i++){c+=(i<=3?50:30)}return c}var b=plan=='pro'?99:149;return b+50*(r-1)}
function po(c){if(c<=20)return[109,'Starter (0\u201320 active customers)'];if(c<=50)return[159,'Growing (21\u201350)'];if(c<=300)return[239,'Professional (51\u2013300)'];if(c<=500)return[275,'Business (301\u2013500)'];return[275+0.16*(c-500),'Enterprise: $275 + $0.16 per customer over 500']}
var JB={core:[[1,{m:49,c:39,a:29}]],connect:[[1,{m:139,c:119,a:99}],[5,{m:199,c:169,a:149}],[10,{m:299,c:259,a:229}],[15,{m:399,c:339,a:299}]],grow:[[1,{m:199,c:169,a:149}],[5,{m:299,c:259,a:229}],[10,{m:399,c:349,a:299}],[15,{m:499,c:429,a:399}]]};
function jb(u,bill,plan){if(plan=='core'){if(u>1)return null;return[JB.core[0][1][bill],'Core, 1 user']}var best=null;JB[plan].forEach(function(t){var inc=t[0],p=t[1][bill];var cost=p+Math.max(0,u-inc)*29;if(!best||cost<best[0])best=[cost,(plan=='grow'?'Grow':'Connect')+' tier with '+inc+' user'+(inc>1?'s':'')+(u>inc?' + '+(u-inc)+' extra at $29':'')]});return best}
function hcp(u,bill){var a=bill=='a';if(u<=1)return[a?59:79,'Basic, 1 user'];if(u<=5)return[a?149:189,'Essentials, 5 users included'];return[(a?299:329)+35*Math.max(0,u-8),'MAX, 8 users included'+(u>8?' + '+(u-8)+' extra at $35':'')]}
var QQ=[[1,29.99,'Essentials'],[2,99.99,'Beginner'],[4,199.99,'Pro'],[10,299.99,'Elite'],[20,699.99,'Max']];
function qiq(u,bill){var best=null;QQ.forEach(function(t){var c=t[1]+Math.max(0,u-t[0])*25;if(!best||c<best[0])best=[c,t[2]+', '+t[0]+' user'+(t[0]>1?'s':'')+' included'+(u>t[0]?' + '+(u-t[0])+' extra at $25':'')]});if(bill=='a'){best=[best[0]*10/12,best[1]+'; yearly = 10 months, shown per month']}return best}
function run(){
 var r=Math.max(1,parseInt($('r').value,10)||1),o=Math.max(0,parseInt($('o').value,10)||0),c=Math.max(0,parseInt($('c').value,10)||0),bill=$('b').value,jp=$('jp').value,gp=$('gp').value;
 var u=r+o,rows=[],na=(bill!='m'?' (no annual price published; monthly shown)':'');
 rows.push(['GorillaDesk',gd(r,gp),(gp=='basic'?'Basic':gp=='pro'?'Pro':'Growth')+', '+r+' route'+(r>1?'s':'')+'; office users free'+na,'https://gorilladesk.com/pricing/']);
 var p=po(c);rows.push(['Pocomos',p[0],p[1]+'; unlimited users'+na,'https://pocomos.com/pricing']);
 var j=jb(u,bill,jp);rows.push(['Jobber',j?j[0]:null,j?j[1]+(bill=='a'?', billed yearly':bill=='c'?', monthly with 1-year commitment':', monthly, no commitment'):'Core is for 1 user only. Pick Connect or Grow.','https://www.getjobber.com/pricing/']);
 var h=hcp(u,bill=='m'?'m':'a');rows.push(['Housecall Pro',h[0],h[1]+(bill=='m'?', monthly':', billed yearly')+(bill=='c'?' (no 1-year monthly option listed)':''),'https://www.housecallpro.com/pricing/']);
 var q=qiq(u,bill=='a'?'a':'m');rows.push(['QuoteIQ',q[0],q[1],'https://myquoteiq.com/pricing/']);
 var pr=rows.filter(function(x){return x[1]!=null}).sort(function(a,b){return a[1]-b[1]});var mx=Math.max.apply(null,pr.map(function(x){return x[1]}));
 var h2=pr.map(function(x,i){return '<div class="row'+(i==0?' best':'')+'"><div><div class="nm">'+x[0]+(i==0?' <span class="pill">Lowest list price</span>':'')+'</div><div class="pl">'+x[2]+' &middot; <a href="'+x[3]+'" target="_blank" rel="nofollow noopener">source</a></div></div><div class="amt">'+f(x[1])+'/mo<small>'+f(x[1]*12)+' per year</small></div><div class="bar"><i style="width:'+Math.max(4,x[1]/mx*100)+'%"></i></div></div>'}).join('');
 rows.filter(function(x){return x[1]==null}).forEach(function(x){h2+='<div class="row qo"><div><div class="nm">'+x[0]+'</div><div class="pl">'+x[2]+'</div></div><div class="amt">n/a</div></div>'});
 ['PestPac (WorkWave)','FieldRoutes','Briostack'].forEach(function(n){h2+='<div class="row qo"><div><div class="nm">'+n+' <span class="pill q">Quote only</span></div><div class="pl">No public price. Ask for a written quote for '+c+' active customers and '+u+' users.</div></div><div class="amt">Ask</div></div>'});
 $('out').innerHTML=h2;$('sum').textContent=r+' route'+(r>1?'s':'')+', '+u+' user'+(u>1?'s':'')+', '+c.toLocaleString('en-US')+' customers';
}
['r','o','c','b','jp','gp'].forEach(function(i){$(i).addEventListener('input',run);$(i).addEventListener('change',run)});run();
})();
