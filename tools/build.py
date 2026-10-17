# Generator for orvianmarketplace.com/software-guides/ . Edit here, rebuild, push out/.
import json, html as H, os, re
CHK = "October 17, 2026"; CHK_ISO = "2026-10-17"
BASE = "https://orvianmarketplace.com/software-guides/"
OG = BASE + "assets/og.png"
E = H.escape
NAV = [("index.html","Guides"),("best-pest-control-software.html","Best pest control software"),("pest-control-software-pricing-calculator.html","Pricing calculator"),("pesticide-application-records-by-state.html","Records by state"),("best-hood-cleaning-software.html","Hood cleaning"),("about.html","How we compare")]

def page(slug, title, desc, body, ld=None):
    url = BASE + ("" if slug=="index.html" else slug)
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h==slug else ""}>{E(t)}</a>' for h,t in NAV[1:])
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in (ld or []))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#0b1220">
<meta property="og:type" content="article"><meta property="og:site_name" content="Orvian Market"><meta property="og:url" content="{url}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Orvian Market Software Guides: honest, dated comparisons from public pricing">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{OG}"><meta property="article:modified_time" content="{CHK_ISO}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230f766e'/%3E%3Ctext x='32' y='44' font-family='Arial' font-weight='800' font-size='34' fill='white' text-anchor='middle'%3EO%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/guides.css">{lds}</head><body>
<header class="nav"><div class="w"><a class="brand" href="index.html"><span class="mk" aria-hidden="true">O</span>Software Guides <small>by Orvian Market</small></a><nav aria-label="Guides">{nav}</nav></div></header>
<div class="disc" role="note"><div class="w"><b>Disclosure:</b> This page has no affiliate links right now. If we add any later, we&rsquo;ll label them and update this notice. No vendor paid to be listed or ranked. <a href="about.html#disclosure">Details</a></div></div>
<main id="main">{body}</main>
<footer><div class="w"><div class="fg"><a href="index.html">All guides</a><a href="best-pest-control-software.html">Best pest control software</a><a href="pest-control-software-pricing-calculator.html">Pricing calculator</a><a href="pesticide-application-records-by-state.html">Pesticide records by state</a><a href="best-hood-cleaning-software.html">Hood cleaning software</a><a href="about.html">How we compare</a><a href="https://orvianmarketplace.com/">Orvian Market</a></div>
<p>&copy; 2026 Orvian Market. Comparisons are built from vendors&rsquo; public pricing pages and documentation, checked {CHK}. We have not tested these products hands-on. Prices change, so confirm on each vendor&rsquo;s site before you buy. Product names and trademarks belong to their owners; Orvian Market isn&rsquo;t affiliated with or endorsed by any vendor named here. Nothing here is legal advice.</p></div></footer>
</body></html>'''

def hero(eb, h1, lead, meta, toc=None):
    m = "".join(f"<span>{E(x)}</span>" for x in meta)
    t = ('<div class="toc">'+"".join(f'<a href="#{a}">{E(b)}</a>' for a,b in toc)+'</div>') if toc else ""
    return f'<section class="hero"><div class="w"><p class="eb">{eb}</p><h1>{E(h1)}</h1><p class="lead">{lead}</p><div class="meta">{m}</div>{t}</div></section>'
def faq_block(faq):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
def plain(s): return H.unescape(re.sub("<[^>]+>","",s))
def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":plain(q),"acceptedAnswer":{"@type":"Answer","text":plain(a)}} for q,a in faq]}
def art_ld(title, desc, slug):
    return {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"dateModified":CHK_ISO,"datePublished":CHK_ISO,"mainEntityOfPage":BASE+slug,"image":OG,"author":{"@type":"Organization","name":"Orvian Market","url":"https://orvianmarketplace.com/"},"publisher":{"@type":"Organization","name":"Orvian Market"}}
def crumbs(name, slug):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Software Guides","item":BASE},{"@type":"ListItem","position":2,"name":name,"item":BASE+slug}]}
METHOD = f'''<div class="method"><div><b>Public sources only</b>Every price and feature comes from the vendor&rsquo;s own pricing page or docs, linked next to it.</div><div><b>Dated</b>Checked {CHK}. Vendors change prices, so re-check before you buy.</div><div><b>Not hands-on</b>We haven&rsquo;t run these products in a live pest or hood business. No star ratings, no made-up test results.</div><div><b>Not paid</b>No vendor paid for placement. No affiliate links on this page today.</div></div>'''
V = [
 dict(k="gd", name="GorillaDesk", url="https://gorilladesk.com/pricing/", for_="Best value for 1&ndash;5 route pest shops that want published prices",
  short="From $49/mo (Basic, 1 route)",
  price="Basic $49/mo, Pro $99/mo, Growth $149/mo for 1 route. Basic adds $50/mo each for routes 2&ndash;3, then $30/mo each from route 4; Pro and Growth add $50/mo per route.",
  model="Per route (technician schedule). Unlimited admin, office and crew users free.",
  trial="Free trial (length not stated on pricing page)", contract="Month-to-month; no setup fee; free data migration",
  pest="Material/chemical use tracking and reporting on Basic; device tracking &amp; barcoding (traps, stations) on Pro",
  good=["Published, route-based pricing: you can work out the bill before a sales call","Chemical-use records are on the cheapest plan","Customer portal, online booking and QuickBooks Online sync on Pro"],
  watch="Basic routing is limited to 25 stops at a time; drive-time routing, subscription billing and QuickBooks sync need Pro. SMS is extra ($5/mo plus credits)."),
 dict(k="po", name="Pocomos", url="https://pocomos.com/pricing", for_="Pest-only shops with several techs that hate per-seat fees",
  short="From $109/mo (0&ndash;20 active customers)",
  price="By active and on-hold customers: $109/mo (0&ndash;20), $159 (21&ndash;50), $239 (51&ndash;300), $275 (301&ndash;500); 501+ is $275 plus $0.16 per customer over 500.",
  model="By active customer count. Unlimited users.", trial="Not stated on pricing page", contract="Not stated on pricing page",
  pest="Chemical tracking and compliance reporting, device and inspection tracking, WDO/WDI and custom forms (per its homepage)",
  good=["Add technicians and office staff without paying per seat","Pest-specific: chemical logs, device tracking, WDO/WDI forms","Published SMS pricing ($4/mo platform fee plus $0.04 per text)"],
  watch="The bill climbs with your customer count, so a solo operator with 200 recurring accounts pays $239/mo where GorillaDesk Basic is $49."),
 dict(k="jb", name="Jobber", url="https://www.getjobber.com/pricing/", for_="Shops where pest control is one of several home services",
  short="From $29/mo billed yearly ($49 monthly), 1 user",
  price="Core $29/mo billed yearly or $49/mo monthly, 1 user. Connect from $99/mo yearly ($139 monthly), Grow from $149/mo yearly ($199 monthly). Extra users $29/mo.",
  model="Per plan with included users (Connect and Grow tiers for 1, 5, 10 and 15 users)", trial="14 days on Grow, no credit card", contract="Monthly, monthly with 1-year commitment, or prepaid annual",
  pest="No pest-specific chemical log listed on its pricing page; checklists (Connect and up) and custom fields can capture application details",
  good=["Polished quoting, invoicing, online booking and client hub","QuickBooks Online and Xero sync, 100+ app integrations","Clear published pricing and a trial with no card"],
  watch="Not built for pest control specifically. Check how you&rsquo;d record EPA registration numbers, rates and target pests before you commit."),
 dict(k="hcp", name="Housecall Pro", url="https://www.housecallpro.com/pricing/", for_="Owner-operators focused on online booking, reviews and marketing",
  short="From $59/mo billed yearly ($79 monthly), 1 user",
  price="Basic $59/mo billed yearly ($79 monthly), 1 user. Essentials $149/mo yearly ($189 monthly), 5 users. MAX $299/mo yearly ($329 monthly), 8 users, plus $35/mo per extra user.",
  model="Per plan with included users", trial="14 days on MAX, no credit card", contract="No long-term contract",
  pest="No pest-specific chemical log listed on its pricing page; checklist automations and photo reports on Essentials",
  good=["Online booking, review management and consumer financing on every plan","Recurring service plans and route optimization on MAX","No long-term contract"],
  watch="Recurring service plans, the core of pest revenue, are listed on MAX ($299+). The pricing page also shows intro promos; we don&rsquo;t count those."),
 dict(k="qiq", name="QuoteIQ", url="https://myquoteiq.com/pricing/", for_="Budget-minded operators who want many AI tools in one app",
  short="From $29.99/mo (1 user)",
  price="Essentials $29.99/mo (1 user), Beginner $99.99 (2), Pro $199.99 (4), Elite $299.99 (10), Max $699.99 (20). Extra users $25/mo. Yearly billing costs 10 months&rsquo; price.",
  model="Per plan with included users, plus monthly AI credits", trial="14 days, credit or debit card required", contract="No contract; price lock while you stay on a plan",
  pest="General field-service app; route optimization and inventory on Elite. Confirm pest record fields during the trial",
  good=["Cheap entry plan with estimates, invoices, scheduling and online payments","Route optimization and inventory on Elite ($299.99)","Yearly billing saves two months"],
  watch="AI features run on monthly credits that don&rsquo;t roll over, and the trial needs a card."),
 dict(k="pp", name="PestPac (WorkWave)", url="https://www.pestpac.com/pricing", for_="Established, multi-branch and commercial-heavy operations",
  short="Not published (quote only)",
  price="Not published. Small Business, Professional and Enterprise packages are quote-only (&ldquo;speak with a consultant&rdquo;).",
  model="Quote-based modules", trial="None listed", contract="Ask in the quote",
  pest="Chemical tracking, termite inspection, custom forms, multi-unit support (per pestpac.com features)",
  good=["Deep pest-specific modules: chemical tracking, termite, commercial and multi-unit","Long history in the pest industry","Built for multiple branches"],
  watch="No public prices or trial, so budget for a sales process. Get the module list, onboarding fees and contract term in writing."),
 dict(k="fr", name="FieldRoutes (ServiceTitan)", url="https://www.fieldroutes.com/pricing", for_="Growing pest and lawn companies scaling routes and sales teams",
  short="Not published (quote only)",
  price="Not published. Growth and Corporate packages; the monthly subscription is &ldquo;based on the number of active customers.&rdquo;",
  model="Quote-based, by active customers", trial="No free trial (stated); free demo", contract="Ask in the quote",
  pest="Route optimization, mobile sales, Sentricon integration, commercial trend reporting (per its pricing page)",
  good=["Pest and lawn focus with route optimization and door-to-door sales tools","Sentricon listed on both packages","Marketing add-on through ServiceTitan"],
  watch="FieldRoutes says it has no free trial because each setup is customized. Price depends on customer count, so ask for the price at 2x your size, not just year one."),
 dict(k="bs", name="Briostack", url="https://www.briostack.com/", for_="Pest and lawn shops that want concurrent-user licensing",
  short="Not published (quote only)",
  price="Not published. Custom pricing by business size, with concurrent licensing by active users. Its add-on price list is public (SMS $0.04 per text, calls $0.04 per minute, plus migration and custom-document fees).",
  model="Quote-based, concurrent user licenses", trial="Demo; no trial listed", contract="Ask in the quote",
  pest="Chemical-usage dashboards and reporting, offline technician app, route optimization (per briostack.com)",
  good=["Founded by a pest control company; pest and lawn in one system","Concurrent licensing can suit seasonal staffing","Public API"],
  watch="Read the public add-on list (briostack.com/additionalpricing) before signing: migrations, custom documents and backups are billed separately."),
]
def vcard(v):
    li = "".join(f"<li>{x}</li>" for x in v["good"])
    return f'<div class="card" id="{v["k"]}"><h3>{v["name"]}</h3><p class="for">{v["for_"]}</p><p class="price"><b>Price:</b> {v["price"]}</p><ul>{li}</ul><p class="watch"><b>Watch for:</b> {v["watch"]}</p><p style="margin:10px 0 0"><a class="vl" href="{v["url"]}" rel="nofollow noopener" target="_blank">Source: {E(v["url"].split("//")[1].rstrip("/"))} &rarr;</a></p></div>'

def best_page():
    slug="best-pest-control-software.html"
    title="Best Pest Control Software for Small Operators (2026): Prices Compared"
    desc=f"GorillaDesk, Pocomos, Jobber, Housecall Pro, QuoteIQ, PestPac, FieldRoutes and Briostack compared on published pricing, pest-specific records and who each fits. Checked {CHK}."
    rows="".join(f'<tr><td>{v["name"]}</td><td>{v["short"]}</td><td>{v["model"]}</td><td>{v["pest"]}</td><td>{v["trial"]}</td><td>{v["contract"]}</td><td class="src"><a href="{v["url"]}" rel="nofollow noopener" target="_blank">pricing page</a></td></tr>' for v in V)
    picks = [("Cheapest published, 1 route","GorillaDesk","Basic is $49/mo for one route and includes chemical-use tracking.","gd"),
             ("Many techs, modest customer list","Pocomos","Unlimited users, priced by active customers, from $109/mo.","po"),
             ("Pest is one of several services","Jobber or Housecall Pro","Strong general field-service tools, but no pest-specific chemical log on their pricing pages.","jb"),
             ("Multi-branch or commercial-heavy","PestPac, FieldRoutes, Briostack","Quote-based, with pest-specific modules. Get three written quotes.","pp")]
    pk="".join(f'<a class="hub" href="#{k}"><span class="k">{a}</span><h3 style="font-size:19px">{b}</h3><p>{c}</p></a>' for a,b,c,k in picks)
    faq=[("What is the cheapest pest control software with chemical tracking?",f"Of the vendors that publish prices, GorillaDesk Basic is $49 a month for one route and lists material (chemical) tracking and reporting on that plan, per its pricing page checked {CHK}. Pocomos starts at $109 a month for up to 20 active customers and also lists chemical tracking."),
         ("Is there free pest control software?","None of the eight vendors here offers a free plan. If you&rsquo;re just starting out, a paper or spreadsheet application log can meet your state&rsquo;s record rules. Our <a href=\"pesticide-application-records-by-state.html\">free state records guide</a> includes a printable log template."),
         ("Does Jobber work for pest control?","It can schedule, quote, invoice and take payments for pest jobs. Its pricing page doesn&rsquo;t list a pest-specific chemical application log, so check that its checklists or custom fields can capture what your state requires: product, EPA registration number, amount, target pest and applicator license."),
         ("How much do PestPac, FieldRoutes and Briostack cost?","None of them publish prices. PestPac and Briostack quote by package or license; FieldRoutes says its subscription is based on your number of active customers. Ask each for a written quote that lists modules, onboarding fees and contract length."),
         ("Did you test these products?","No. This comparison is built from public pricing pages and vendor documentation, linked on every row. We haven&rsquo;t used them in a live pest business, and we don&rsquo;t publish star ratings or test scores we didn&rsquo;t earn."),
         ("How current is this?",f"Prices were checked on {CHK}. Every row links to its source page so you can confirm current prices.")]
    body = hero("Pest control software &middot; 2026","Best pest control software for small operators (2026)",
      "Eight tools compared on what they publicly charge, how they bill (per route, per user or per customer) and whether they handle pesticide application records. Built from public pricing pages, not sponsored rankings.",
      [f"Checked {CHK}","Sources linked on every row","No hands-on testing claimed","No paid placement"],
      [("picks","Quick picks"),("table","Comparison table"),("vendors","Vendor by vendor"),("choose","How to choose"),("faq","FAQ")])
    body += f'<section class="sec" id="picks"><div class="w"><h2>Quick picks</h2><p class="sub">Who each tool fits, based on its published pricing model and pest-specific features. Your routes, team size and customer count decide the real winner, so run your numbers in the <a href="pest-control-software-pricing-calculator.html">pricing calculator</a>.</p><div class="hubs">{pk}</div></div></section>'
    body += f'<section class="sec alt" id="table"><div class="w"><h2>Side-by-side comparison</h2><p class="sub">Starting prices and billing models as published on each vendor&rsquo;s site, checked {CHK}. &ldquo;Not published&rdquo; means quote-only.</p><div class="tw"><table class="t"><thead><tr><th>Software</th><th>Published price</th><th>Billing model</th><th>Pest-specific records (vendor&rsquo;s own pages)</th><th>Trial</th><th>Contract</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div><div class="note">Only GorillaDesk, Pocomos, Jobber, Housecall Pro and QuoteIQ publish prices. Not counted: payment processing, SMS and add-on fees, taxes and intro promotions.</div></div></section>'
    body += f'<section class="sec" id="vendors"><div class="w"><h2>Vendor by vendor</h2><p class="sub">What each one publishes, what stands out, and the catch to check before you sign.</p><div class="cards">{"".join(vcard(v) for v in V)}</div></div></section>'
    body += '''<section class="sec alt" id="choose"><div class="w nw"><h2>How to choose pest control software</h2>
<h3>1. Know what you&rsquo;re billed on</h3><p>GorillaDesk charges per route; Pocomos and FieldRoutes charge by active customers; Jobber, Housecall Pro and QuoteIQ charge by plan, with users included. A 2-truck shop with 400 quarterly customers can get very different bills under each model. The <a href="pest-control-software-pricing-calculator.html">calculator</a> does the math for the five vendors with public prices.</p>
<h3>2. Check the records your state requires</h3><p>Most states want a record for every application: product name, EPA registration number, amount or dilution, target pest, site and the applicator&rsquo;s license number, kept for 2 or 3 years depending on the state. Make sure the software captures every field. Our <a href="pesticide-application-records-by-state.html">state-by-state guide</a> links the official rules.</p>
<h3>3. Price recurring billing and routing</h3><p>Recurring quarterly service is the core of most pest businesses. Check which plan includes subscription billing and real route optimization: on GorillaDesk that&rsquo;s Pro, and on Housecall Pro recurring service plans and route optimization are on MAX.</p>
<h3>4. Ask quote-only vendors the same five questions</h3><p>What&rsquo;s the monthly price at your customer count, and at twice that count? What are the onboarding and migration fees? How long is the contract, and how do you cancel? Which modules cost extra? Get the answers in writing.</p>
<h3>5. Run the trial on a real week</h3><p>Enter a real route, record a real application and send a real invoice. Jobber and Housecall Pro trials need no card; QuoteIQ&rsquo;s does.</p>
<div class="note w2"><b>Free option:</b> if you run one truck and want to stay at $0 for now, a paper or spreadsheet log with your state&rsquo;s required fields works. Our <a href="pesticide-application-records-by-state.html#template">printable log template</a> is free.</div></div></section>'''
    body += f'<section class="sec"><div class="w"><h2>How we compared</h2>{METHOD}</div></section>'
    body += f'<section class="sec alt" id="faq"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Best pest control software",slug)])
def calc_page():
    slug="pest-control-software-pricing-calculator.html"
    title="Pest Control Software Pricing Calculator (2026): GorillaDesk vs Pocomos vs Jobber vs Housecall Pro"
    desc=f"Enter your routes, office users and active customers to compare the monthly and yearly list price of five pest control software tools. Public prices checked {CHK}."
    faq=[("How is the cost calculated?","For each vendor we apply its published list price to your inputs: per route for GorillaDesk, by active-customer tier for Pocomos, and the cheapest plan with enough users (plus published extra-user fees) for Jobber, Housecall Pro and QuoteIQ. Taxes, payment processing, SMS, add-ons and intro promotions aren&rsquo;t included."),
         ("Why does the cheapest line show a different plan for each vendor?","The calculator picks the cheapest plan that fits your headcount, but plans differ in features. Recurring billing and route optimization, for example, are on higher plans at some vendors. Check the plan&rsquo;s features on the vendor&rsquo;s pricing page."),
         ("Why aren&rsquo;t PestPac, FieldRoutes and Briostack calculated?","They don&rsquo;t publish prices. They&rsquo;re listed so you remember to ask for a written quote."),
         ("Who counts as a user?","Everyone who logs in: technicians plus office staff. GorillaDesk only charges for technicians who run their own route, and Pocomos doesn&rsquo;t charge per user.")]
    def ex(r,o,c):
        u=r+o
        g=49+sum(50 if i<=3 else 30 for i in range(2,r+1))
        p=109 if c<=20 else 159 if c<=50 else 239 if c<=300 else 275 if c<=500 else 275+0.16*(c-500)
        j=min(pp+max(0,u-inc)*29 for inc,pp in [(1,139),(5,199),(10,299),(15,399)])
        h=79 if u<=1 else 189 if u<=5 else 329+35*max(0,u-8)
        q=min(pp+max(0,u-inc)*25 for inc,pp in [(1,29.99),(2,99.99),(4,199.99),(10,299.99),(20,699.99)])
        return g,p,j,h,q
    scen=[("Solo: 1 route, no office staff, 150 customers",1,0,150),("Small shop: 3 routes, 1 office user, 400 customers",3,1,400),("Growing: 6 routes, 2 office users, 900 customers",6,2,900)]
    trs="".join(f"<tr><td>{E(n)}</td>"+"".join(f"<td>${x:,.0f}</td>" for x in ex(r,o,c))+"</tr>" for n,r,o,c in scen)
    th="<tr><th>Scenario (monthly billing)</th><th>GorillaDesk Basic</th><th>Pocomos</th><th>Jobber Connect</th><th>Housecall Pro</th><th>QuoteIQ</th></tr>"
    body = hero("Free tool &middot; pest control software","Pest control software pricing calculator",
      "Enter your routes, office staff and active customers to see the monthly and yearly <b>list price</b> of five pest control tools that publish prices, side by side, each linked to its source.",
      [f"Prices checked {CHK}","Runs in your browser","No signup or email","Not sponsored"])
    body += f'''<section class="sec"><div class="w"><div class="calc"><form class="cin" onsubmit="return false" aria-label="Your business">
<label for="r">Technicians with their own route</label><input id="r" type="number" min="1" max="50" value="2" inputmode="numeric"><p class="hint">Crews that ride together count as one route.</p>
<label for="o">Office users (owner, CSR, manager)</label><input id="o" type="number" min="0" max="50" value="1" inputmode="numeric">
<label for="c">Active recurring customers</label><input id="c" type="number" min="0" max="20000" value="250" inputmode="numeric"><p class="hint">Used for Pocomos, which prices by active and on-hold customers.</p>
<label for="b">Billing</label><select id="b"><option value="m">Monthly, no commitment</option><option value="c">Monthly, 1-year commitment</option><option value="a">Billed yearly</option></select>
<label for="gp">GorillaDesk plan</label><select id="gp"><option value="basic">Basic</option><option value="pro">Pro (portal, subscriptions, QuickBooks)</option><option value="growth">Growth (sales suite)</option></select>
<label for="jp">Jobber plan</label><select id="jp"><option value="connect">Connect</option><option value="grow">Grow</option><option value="core">Core (1 user only)</option></select>
</form><div><h2 style="font-size:24px">Monthly list price for <span id="sum">your shop</span></h2><p class="sub" style="margin-bottom:14px">Lowest first. Plans differ in features, so the cheapest line isn&rsquo;t automatically the best fit; see the <a href="best-pest-control-software.html">comparison</a>.</p><div class="res" id="out" aria-live="polite"></div>
<noscript><div class="tw"><table class="t"><thead>{th}</thead><tbody>{trs}</tbody></table></div></noscript></div></div></div></section>
<section class="sec alt"><div class="w"><h2>Three example shops (monthly billing)</h2><p class="sub">Same math as the calculator: GorillaDesk on Basic, Jobber on Connect, and the cheapest plan that fits the headcount for the others.</p><div class="tw"><table class="t"><thead>{th}</thead><tbody>{trs}</tbody></table></div>
<div class="note"><b>Not counted:</b> payment processing (Jobber lists 2.9% + 30&cent; for cards, for example), SMS fees (GorillaDesk $5/mo plus credits; Pocomos $4/mo plus $0.04 per text), add-ons (such as Jobber Receptionist at $29/mo), taxes, onboarding fees and intro promotions. GorillaDesk and Pocomos don&rsquo;t publish annual prices, so their monthly price is shown for yearly billing. Housecall Pro publishes an extra-user fee only for MAX.</div></div></section>
<section class="sec"><div class="w"><h2>Price rules we used</h2><p class="sub">Straight from each vendor&rsquo;s pricing page, checked {CHK}.</p><div class="tw"><table class="t"><thead><tr><th>Vendor</th><th>Rule</th><th>Source</th></tr></thead><tbody>
<tr><td>GorillaDesk</td><td>Basic $49/mo for 1 route; routes 2&ndash;3 add $50/mo each, route 4+ adds $30/mo each. Pro $99 and Growth $149 add $50/mo per route. Unlimited non-route users free.</td><td class="src"><a href="https://gorilladesk.com/pricing/" rel="nofollow noopener" target="_blank">gorilladesk.com/pricing</a></td></tr>
<tr><td>Pocomos</td><td>$109 (0&ndash;20 active customers), $159 (21&ndash;50), $239 (51&ndash;300), $275 (301&ndash;500), then $275 + $0.16 per customer over 500. Unlimited users.</td><td class="src"><a href="https://pocomos.com/pricing" rel="nofollow noopener" target="_blank">pocomos.com/pricing</a></td></tr>
<tr><td>Jobber</td><td>Core $49 / $39 / $29 (monthly / monthly with 1-year commitment / annual), 1 user. Connect tiers for 1/5/10/15 users: $139/$199/$299/$399 monthly, $99/$149/$229/$299 annual. Grow: $199/$299/$399/$499 monthly, $149/$229/$299/$399 annual. Extra users $29/mo.</td><td class="src"><a href="https://www.getjobber.com/pricing/" rel="nofollow noopener" target="_blank">getjobber.com/pricing</a></td></tr>
<tr><td>Housecall Pro</td><td>Basic, 1 user: $79 monthly / $59 yearly. Essentials, 5 users: $189 / $149. MAX, 8 users: $329 / $299, +$35/mo per extra user.</td><td class="src"><a href="https://www.housecallpro.com/pricing/" rel="nofollow noopener" target="_blank">housecallpro.com/pricing</a></td></tr>
<tr><td>QuoteIQ</td><td>Essentials 1 user $29.99, Beginner 2 $99.99, Pro 4 $199.99, Elite 10 $299.99, Max 20 $699.99; +$25/mo per extra user; yearly = 10 months.</td><td class="src"><a href="https://myquoteiq.com/pricing/" rel="nofollow noopener" target="_blank">myquoteiq.com/pricing</a></td></tr>
</tbody></table></div></div></section>
<section class="sec alt"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section><script src="assets/calc.js" defer></script>'''
    ld=[{"@context":"https://schema.org","@type":"WebApplication","name":"Pest control software pricing calculator","applicationCategory":"BusinessApplication","operatingSystem":"Any (web browser)","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"url":BASE+slug},faq_ld(faq),crumbs("Pricing calculator",slug)]
    return slug, page(slug,title,desc,body,ld)
S = [
 ("Texas","Texas Department of Agriculture (Structural Pest Control Service)","2 years","Customer billing name and address; service address; pesticide or device name or EPA registration number; amounts and mixing rate; target pest; date; names and license numbers of the applicator, supervisor and trainee; the business TPCL number. Termite treatments need extra fields.",
  [("4 TAC &sect;7.144","https://www.law.cornell.edu/regulations/texas/4-Tex-Admin-Code-SS-7-144"),("TDA self-audit checklist","https://texasagriculture.gov/Regulatory-Programs/Pesticides/Structural-Pest-Control-Service/Structural-Pest-Control-Business/Structural-Business-Self-Auditing")]),
 ("Florida","Florida Department of Agriculture and Consumer Services (FDACS)","2 years (3 for preconstruction termite treatments)","Pest control records and contracts, kept at the licensed business location. For restricted-use pesticides: product brand names, amounts, uses, dates and places of application. Fumigation logs add the fumigant cylinder ID.",
  [("Rule 5E-14.142","https://flrules.org/gateway/ruleno.asp?id=5E-14.142"),("F.S. Chapter 482","https://flsenate.gov/Laws/Statutes/2025/Chapter482/All")]),
 ("California","Structural Pest Control Board","3 years","For each non-fumigation application: date and time; owner or agent; property address; areas treated; target pests; product name with EPA or CA registration number and amount used; identity and license number of the applicator(s). A Standard Structural Fumigation Log for each fumigation.",
  [("16 CCR &sect;1970","https://www.law.cornell.edu/regulations/california/16-CCR-1970"),("Structural Pest Control Board","https://www.pestboard.ca.gov/")]),
 ("Georgia","Georgia Department of Agriculture (Structural Pest Control)","2 years","A legible pesticide-use record after every structural application: customer; property address; company; applicator; area treated; product and EPA number; amount; concentration; method; target pest; date; precautions; start and end times where applicable.",
  [("Rule 620-3-.02","https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-620-3-.02"),("GDA CAM 1: Pesticide Use Records (PDF)","https://agr.georgia.gov/sites/default/files/documents/pest-control/cam-1-pesticide-use-records.pdf")]),
 ("North Carolina","NCDA&amp;CS Structural Pest Control and Pesticides Division","2 years beyond the last treatment date","Property owner name and address; company name, address and license number; property treated, type of treatment and dates; pests covered; EPA brand name of every pesticide; federal RUP record fields; name of the person who applied it. Keep records at the licensed office.",
  [("02 NCAC 34 .0703","https://www.law.cornell.edu/regulations/north-carolina/02-N-C-Admin-Code-34-0703"),("02 NCAC 34 .0328 (record location)","https://www.law.cornell.edu/regulations/north-carolina/02-N-C-Admin-Code-34-0328")]),
 ("Arizona","Arizona Department of Agriculture, Pest Management Division","3 years (business licensee)","A service record for each service: customer name and address; specific site; date and time; target pest; trade name; EPA registration number of any restricted-use pesticide; amount applied; name and certification number of the applicator or supervisor. Applicators hand records to the business within 5 business days.",
  [("A.A.C. R3-8-501","https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R3-8-501"),("A.A.C. R3-8-503 (retention)","https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R3-8-503")]),
 ("Ohio","Ohio Department of Agriculture","3 years","Recorded on the application date: responsible applicator and trained servicepersons; customer name and address; date; pests; locations and methods; trade name and EPA registration number; concentration and total volume; start and finish times. Termite work also needs a structure drawing. Copies go to the business within 10 days.",
  [("OAC 901:5-11-10","https://codes.ohio.gov/ohio-administrative-code/rule-901:5-11-10")]),
 ("Pennsylvania","Pennsylvania Department of Agriculture","3 years","A record for every application, completed within 24 hours: date and time; customer and site; product brand name and EPA registration number; amount and rate; the applicator&rsquo;s name and certification or registration number.",
  [("7 Pa. Code &sect;128.35","https://www.pacodeandbulletin.gov/secure/pacode/data/007/chapter128/s128.35.html")]),
 ("New York","NYS Department of Environmental Conservation","3 years, plus an annual report","Commercial businesses keep application records and file an annual report under the Pesticide Reporting Law. DEC accepts those records in place of separate ones if they include the application location.",
  [("6 NYCRR 325.25","https://www.law.cornell.edu/regulations/new-york/6-NYCRR-325.25"),("DEC guidance OGC 3","https://dec.ny.gov/regulatory/guidance-and-policy-documents/ogc-3-pesticide-recordkeeping-and-reporting-of-commercial-applicators")]),
 ("Illinois","Illinois Department of Public Health (Structural Pest Control)","2 years","Commercial locations keep records of all pesticide applications. Restricted-use records are kept separately, with customer and site, technician, date and time, target pest, pesticide details, and an amount estimate within 10%. Copies go to the property owner, manager or tenant on request.",
  [("77 Ill. Adm. Code 830.820","https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-77-SS-830.820")]),
 ("Virginia","Virginia Department of Agriculture and Consumer Services (VDACS)","2 years","Licensed businesses record every application, general-use and restricted-use alike: customer name, address and phone; site; applicator name and certification number; date; site treated and pests; area; product name; EPA registration number; concentrate and diluent amounts; equipment.",
  [("2VAC5-680-65","https://law.lis.virginia.gov/admincode/title2/agency5/chapter680/section65/"),("VDACS applicator responsibilities (PDF)","https://www.vdacs.virginia.gov/pdf/responsibilitiescommrt.pdf")]),
 ("Tennessee","Tennessee Department of Agriculture","2 years from the application date","Applicator name and certification number; trade name; address; date; target area and pest; total amount, dilution and rate; property owner or tenant name. Restricted-use pesticides also need the EPA registration number and time. Give the owner or tenant a copy within 48 hours of a request.",
  [("Rule 0080-09-04-.06","https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0080-09-04-.06")]),
]
def sid(n): return n.lower().replace(" ","-")
def records_page():
    slug="pesticide-application-records-by-state.html"
    title="Pesticide Application Record Requirements by State (2026): Free Guide + Log Template"
    desc=f"How long to keep pest control application records, and what to record, in TX, FL, CA, GA, NC, AZ, OH, PA, NY, IL, VA and TN, with links to the official rules and a free printable log. Checked {CHK}."
    rows="".join(f'<tr id="{sid(s[0])}"><td>{s[0]}</td><td><b>{s[2]}</b></td><td>{s[3]}</td><td>{s[1]}</td><td class="src">'+"<br>".join(f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' for n,u in s[4])+'</td></tr>' for s in S)
    jump=" &middot; ".join(f'<a href="#{sid(s[0])}">{s[0]}</a>' for s in S)
    flds=["Date, start time and finish time","Customer name, address and phone","Service address and specific site or area treated","Target pest(s)","Product trade (brand) name","EPA registration number","Amount applied; dilution or % active ingredient; rate","Application method and equipment","Applicator name and license/certification no.","Supervising applicator and license no. (if supervised)","Business license number","Outdoor work: wind direction, speed, temperature","Devices or bait stations installed or checked","Precautions, notes, customer copy given (Y/N)"]
    form="".join(f"<tr><th>{E(x)}</th><td></td></tr>" for x in flds)
    faq=[("How long do I have to keep pest control application records?","In the 12 states we checked it&rsquo;s 2 or 3 years. Texas, Florida, Georgia, Illinois, Virginia and Tennessee require 2 years; North Carolina requires 2 years beyond the last treatment; California, Arizona, Ohio, Pennsylvania and New York require 3. Some record types run longer, such as Florida&rsquo;s preconstruction termite records (3 years). Check your state&rsquo;s rule, linked in the table."),
         ("Is there a federal requirement?","Yes, for restricted-use pesticides (RUPs). EPA&rsquo;s certification rule requires state plans to make certified commercial applicators keep RUP application records for at least 2 years (40 CFR 171.303). Most state rules go further and cover general-use pesticides too."),
         ("Can I keep records electronically?","Most rules care about the content and about handing records over on request, not the format. Florida&rsquo;s rule, for example, says electronic records must be provided to the department on request. Confirm with your state agency."),
         ("Is this legal advice?",f"No. It&rsquo;s a plain-English summary of official rules, checked {CHK}, with a link to each source. Rules change, and the official text is what counts. If you&rsquo;re unsure, call your state&rsquo;s lead agency."),
         ("My state isn&rsquo;t listed. Where do I look?","The National Pesticide Information Center keeps a directory of every state&rsquo;s pesticide regulatory agency. It&rsquo;s linked below the table.")]
    body = hero("Free guide &middot; pest control compliance","Pesticide application record requirements by state",
      "How long to keep application records, and which fields to record, in 12 large pest-control states, with the official rule linked for each. Plus a free printable application log.",
      [f"Rules checked {CHK}","Official sources linked","Free printable log","Not legal advice"],
      [("table","State table"),("federal","Federal baseline"),("template","Printable log"),("software","Using software instead"),("faq","FAQ")])
    body += f'''<section class="sec" id="table"><div class="w"><h2>Record rules in 12 states</h2><p class="sub">Structural and commercial pest control application records, summarized from the official rule text. Jump to: {jump}</p>
<div class="tw"><table class="t"><thead><tr><th>State</th><th>Keep records for</th><th>What to record (summary)</th><th>Lead agency</th><th>Official rule / source</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="note w2"><b>Summary only.</b> These are condensed from the rule text as of {CHK}. Several states have extra rules for termite, fumigation, school or restricted-use work, so read the linked rule before you design your forms. Rule text links go to the Cornell LII mirror of the state code where the state&rsquo;s own site is hard to link. For other states, see the <a href="https://npic.orst.edu/reg/state_agencies.html" rel="noopener" target="_blank">NPIC directory of state pesticide regulatory agencies</a>.</div></div></section>
<section class="sec alt" id="federal"><div class="w nw"><h2>The federal baseline for restricted-use pesticides</h2><p>Under EPA&rsquo;s certification rule, state plans must require certified commercial applicators to keep records of restricted-use pesticide (RUP) applications for at least <b>2 years</b>. The record covers: customer name and address; location; crop or site; date and time; product name and EPA registration number; amount; and the certified applicator&rsquo;s name and certification number. Supervised applications also name the noncertified applicator. Source: <a href="https://www.ecfr.gov/current/title-40/chapter-I/subchapter-E/part-171/subpart-D/section-171.303" rel="noopener" target="_blank">40 CFR 171.303</a>. Most state rules above cover <i>every</i> application, not just RUPs.</p></div></section>
<section class="sec" id="template"><div class="w nw"><h2>Free printable application log</h2><p class="sub">One sheet per application. It combines the most common fields from the rules above, so compare it with your state&rsquo;s list and add anything missing. Print it, or save it as a PDF from your browser.</p>
<p class="noprint"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button></p>
<div class="form"><h3>Pesticide application record</h3><table>{form}</table></div>
<p style="font-size:13px;color:var(--mute)">Template by Orvian Market. Free to copy and use. Not legal advice; your state&rsquo;s rule is what counts.</p></div></section>
<section class="sec alt" id="software"><div class="w nw"><h2>Using software instead</h2><p>Pest control apps can fill most of these fields automatically from the job, the product list and the technician&rsquo;s profile. Among tools with published pricing, GorillaDesk lists chemical-use tracking on its $49/mo Basic plan, and Pocomos lists chemical tracking and compliance reporting from $109/mo. General field-service apps like Jobber and Housecall Pro don&rsquo;t list a pest-specific application log, so you&rsquo;d build one from checklists or custom fields. See the <a href="best-pest-control-software.html">full comparison</a> or <a href="pest-control-software-pricing-calculator.html">price your shop</a>.</p></div></section>
<section class="sec" id="faq"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Pesticide records by state",slug)])
HV=[
 ("MyHoodClean","https://myhoodclean.com/","$49.99/mo, or $419.88/yr ($34.99/mo equivalent)","7-day free trial, no payment details","All-in-one: NFPA 96 reports with grease depth, scheduling by NFPA 96 frequency, invoicing, customer portal, a website, AI assistant, QuickBooks/CSV export, offline mode","Small hood companies that want one app for reports, scheduling and billing"),
 ("HoodCleaningReport","https://hoodcleaningreport.com/pricing","Standard $49/mo (20 reports, 5 seats), Pro $89/mo (50 reports, 10 seats), Business $109/mo (unlimited). Annual saves 20%. Report packs from $25 for 10.","Free trial: 3 reports or 3 days, no card","Reports: AI inspection and post-clean reports, NFPA 96 and ANSI/IKECA C10 fields, certificate and sticker, CompanyCam import, a vault for sharing with AHJs and owners","Companies that schedule and invoice elsewhere but want better reports"),
 ("Stampario","https://stampario.com/for/hood-cleaning-companies","Free for 5 reports/mo; Pro $29/mo (unlimited reports, reminder emails); Team $69/mo (3 techs)","Free plan","Hood cleaning reports finished on screen at the end of the job; free printable report template","Solo operators on a tight budget, or a free first try at digital reports"),
 ("HoodStamp","https://hoodstamp.com/","Free (3 certificates/mo). Starter $49, Pro $99, Business $199/mo listed, with paid plans &ldquo;opening soon&rdquo;","Free plan","NFPA 96 certificates in minutes, per-component checklist, before/after photos, QR stickers that link to a live status page","Trying QR-sticker certificates at no cost"),
 ("QuoteIQ","https://myquoteiq.com/pricing/","Essentials $29.99/mo (1 user) up to Max $699.99/mo (20 users)","14 days, card required","General field-service app (estimates, invoices, scheduling, payments; photo inspection reports from Beginner up), not hood-specific","Multi-service exterior cleaning companies that also do hoods"),
 ("Smart Service","https://www.smartservice.com/pricing","From $129.99 per user/mo, 3-user minimum (cloud or desktop); discount for annual","Demo","Scheduling, dispatch and native QuickBooks integration, with a hood cleaning industry page","Established crews that run on QuickBooks"),
 ("HoodOps","https://www.gethoodops.com/","Not published (priced by accounts serviced, per its site)","Demo","Built by a hood company owner (CESI, CECS): an NFPA 96 report and certificate on every job, grease readings locked at completion, sealed records","Companies that want liability-grade job records"),
]
def hood_page():
    slug="best-hood-cleaning-software.html"
    title="Best Hood Cleaning Software (2026): NFPA 96 Report Apps Compared by Price"
    desc=f"MyHoodClean, HoodCleaningReport, Stampario, HoodStamp, QuoteIQ, Smart Service and HoodOps compared on published pricing, free plans and NFPA 96 reporting. Checked {CHK}."
    rows="".join(f'<tr><td>{a}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td><td class="src"><a href="{u}" rel="nofollow noopener" target="_blank">source</a></td></tr>' for a,u,c,d,e,f in HV)
    faq=[("Is there free hood cleaning report software?",f"Yes. Stampario has a free plan for 5 reports a month, HoodStamp lists a free plan for 3 certificates a month, and HoodCleaningReport has a free trial of 3 reports or 3 days, per their sites checked {CHK}."),
         ("What&rsquo;s the cheapest all-in-one hood cleaning app?","Of the hood-specific apps that publish prices, MyHoodClean is $49.99 a month ($34.99 a month billed yearly) and covers reports, scheduling, invoicing and a website. Stampario Pro is cheaper at $29 a month but focuses on reports."),
         ("Do these reports guarantee NFPA 96 compliance?","No software can. Compliance depends on the work done and on your local Authority Having Jurisdiction (AHJ), which may adopt a specific NFPA 96 edition or add its own requirements. Check with your fire marshal."),
         ("Did you test these apps?","No. This comparison uses each vendor&rsquo;s public pricing and product pages, linked in the table. We haven&rsquo;t used them on real jobs.")]
    body = hero("Hood cleaning software &middot; 2026","Best hood cleaning software (2026), compared by price",
      "Seven tools for kitchen exhaust cleaning companies, covering NFPA 96 reports, certificates, scheduling and invoicing. Compared on what they publicly charge and what each is built for, free options included.",
      [f"Checked {CHK}","Free options included","Sources linked","No paid placement"])
    body += f'''<section class="sec"><div class="w"><h2>Side-by-side comparison</h2><p class="sub">Published prices and positioning from each vendor&rsquo;s own site, checked {CHK}.</p><div class="tw"><table class="t"><thead><tr><th>Software</th><th>Published price</th><th>Free plan / trial</th><th>What it does</th><th>Best for</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="note"><b>Quick take:</b> to try digital NFPA 96 reports for free, start with Stampario&rsquo;s or HoodStamp&rsquo;s free plan. For one app that also schedules and invoices, MyHoodClean has the lowest published all-in-one price. If you mainly want better reports and already invoice in QuickBooks or Jobber, look at HoodCleaningReport.</div></div></section>
<section class="sec alt"><div class="w nw"><h2>What to check before you choose</h2>
<h3>Does the report match your AHJ?</h3><p>Fire marshals may adopt a specific NFPA 96 edition. Ask the vendor which edition its report follows and whether you can add local fields and state license numbers.</p>
<h3>Reports only, or the whole business?</h3><p>Report apps (HoodCleaningReport, Stampario, HoodStamp) sit alongside whatever you invoice with. All-in-ones (MyHoodClean, Smart Service, HoodOps) replace your scheduling and billing too.</p>
<h3>Report limits</h3><p>HoodCleaningReport caps reports per month by plan and sells packs, and Stampario&rsquo;s free plan stops at 5 reports a month. Count your reports in a busy month before you choose.</p></div></section>
<section class="sec"><div class="w"><h2>How we compared</h2>{METHOD}</div></section>
<section class="sec alt"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Hood cleaning software",slug)])

def about_page():
    slug="about.html"; title="How Orvian Market Software Guides Compares Software"; desc="Method, sources and affiliate disclosure for Orvian Market Software Guides."
    body = hero("About these guides","How we compare software","The same plain rules apply to every guide on this site.",[f"Last updated {CHK}"])
    body += f'''<section class="sec"><div class="w nw"><h2>Method</h2>{METHOD}
<h3>What we use</h3><p>Each vendor&rsquo;s own public pricing page, product pages and documentation, plus official government sources for compliance topics. Every claim links to its source. When a vendor doesn&rsquo;t publish a price, we say &ldquo;quote only&rdquo; rather than repeat third-party estimates.</p>
<h3>What we don&rsquo;t do</h3><p>We don&rsquo;t claim hands-on testing we haven&rsquo;t done, publish star ratings or invented scores, or write fake reviews. If we ever test a product hands-on, the page will say what we did and when.</p>
<h3 id="disclosure">Affiliate disclosure</h3><p><b>None of our guides contain affiliate links today.</b> In the future we may join vendors&rsquo; affiliate or partner programs, which pay us a commission if you buy through our link, at no extra cost to you. If we do, every affiliate link will be labeled, this notice will name the programs, and rankings won&rsquo;t depend on commissions. Vendors can&rsquo;t pay to be listed or ranked.</p>
<h3>Corrections</h3><p>Spotted an outdated price? Every page shows the date we checked, and vendors change prices often, so the vendor&rsquo;s own page is always the final word.</p></div></section>'''
    return slug, page(slug,title,desc,body,[crumbs("How we compare",slug)])

def index_page():
    slug="index.html"; title="Software Guides for Pest Control and Hood Cleaning Businesses | Orvian Market"
    desc=f"Honest, dated software comparisons for small field-service businesses: pest control software, a pricing calculator, state pesticide record rules and hood cleaning apps. Checked {CHK}."
    hubs=[("Pest control","best-pest-control-software.html","Best pest control software for small operators (2026)","GorillaDesk, Pocomos, Jobber, Housecall Pro, QuoteIQ, PestPac, FieldRoutes and Briostack, compared on public pricing."),
          ("Free tool","pest-control-software-pricing-calculator.html","Pest control software pricing calculator","Enter your routes, users and customers to see five vendors&rsquo; list prices side by side."),
          ("Free guide","pesticide-application-records-by-state.html","Pesticide application records by state","Retention periods and required fields for 12 states, with official sources and a printable log."),
          ("Hood cleaning","best-hood-cleaning-software.html","Best hood cleaning software (2026)","Seven NFPA 96 report and business apps, free plans included.")]
    hb="".join(f'<a class="hub" href="{h}"><span class="k">{k}</span><h3>{E(t)}</h3><p>{d}</p></a>' for k,h,t,d in hubs)
    body = hero("Orvian Market &middot; Software Guides","Software guides for pest control and hood cleaning businesses","Honest, dated comparisons built from vendors&rsquo; public pricing and docs. No sponsored rankings, no fake reviews, and every number links to its source.",[f"Checked {CHK}","Sources on every row","Free tools"])
    body += f'<section class="sec"><div class="w"><h2>Guides</h2><p class="sub">Start with your trade.</p><div class="hubs">{hb}</div></div></section><section class="sec alt"><div class="w"><h2>How we compare</h2>{METHOD}<p style="margin-top:16px"><a href="about.html">Read the full method and disclosure &rarr;</a></p></div></section>'
    return slug, page(slug,title,desc,body,[{"@context":"https://schema.org","@type":"CollectionPage","name":title,"url":BASE,"description":desc}])

pages=[index_page(),best_page(),calc_page(),records_page(),hood_page(),about_page()]
for s,h in pages: open("out/"+s,"w").write(h)
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}{"" if s=="index.html" else s}</loc><lastmod>{CHK_ISO}</lastmod></url>\n' for s,_ in pages)+'</urlset>\n'
open("out/sitemap.xml","w").write(sm)
print("built",[s for s,_ in pages])
