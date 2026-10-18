# Generator for orvianmarketplace.com/software-guides/ . Edit here, rebuild, push out/.
import json, html as H, os, re
CHK = "October 17, 2026"; CHK_ISO = "2026-10-17"
BASE = "https://orvianmarketplace.com/software-guides/"
OG = BASE + "assets/og.png"
E = H.escape
NAV = [("index.html","Guides"),("best-pest-control-software.html","Best pest software"),("pest-control-software-pricing-calculator.html","Pricing calculator"),("pesticide-application-records-by-state.html","Records by state"),("best-hood-cleaning-software.html","Hood cleaning"),("hood-cleaning-frequency-requirements.html","Hood schedule"),("about.html","How we compare")]

def page(slug, title, desc, body, ld=None):
    url = BASE + ("" if slug=="index.html" else slug)
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h==slug else ""}>{E(t)}</a>' for h,t in NAV[1:] if h!="about.html")
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
<footer><div class="w"><div class="fg"><a href="index.html">All guides</a><a href="best-pest-control-software.html">Best pest control software</a><a href="pest-control-software-pricing-calculator.html">Pricing calculator</a><a href="pesticide-application-records-by-state.html">Pesticide records by state</a><a href="pest-control-license-requirements-by-state.html">Pest control license by state</a><a href="best-hood-cleaning-software.html">Hood cleaning software</a><a href="hood-cleaning-frequency-requirements.html">Hood cleaning schedule (NFPA 96)</a><a href="how-to-start-a-hood-cleaning-business.html">Start a hood cleaning business</a><a href="about.html">How we compare</a><a href="https://orvianmarketplace.com/privacy.html">Privacy</a><a href="https://orvianmarketplace.com/">Orvian Market</a></div>
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
<section class="sec alt" id="software"><div class="w nw"><h2>Using software instead</h2><p>Pest control apps can fill most of these fields automatically from the job, the product list and the technician&rsquo;s profile. Among tools with published pricing, GorillaDesk lists chemical-use tracking on its $49/mo Basic plan, and Pocomos lists chemical tracking and compliance reporting from $109/mo. General field-service apps like Jobber and Housecall Pro don&rsquo;t list a pest-specific application log, so you&rsquo;d build one from checklists or custom fields. See the <a href="best-pest-control-software.html">full comparison</a> or <a href="pest-control-software-pricing-calculator.html">price your shop</a>. Still getting licensed? See <a href="pest-control-license-requirements-by-state.html">pest control license requirements by state</a>.</p></div></section>
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
<h3>Does the report match your AHJ?</h3><p>Fire marshals may adopt a specific NFPA 96 edition. Ask the vendor which edition its report follows and whether you can add local fields and state license numbers. Our <a href=\"hood-cleaning-frequency-requirements.html\">hood cleaning schedule guide</a> covers the NFPA 96 intervals, tag rules and state licensing examples.</p>
<h3>Reports only, or the whole business?</h3><p>Report apps (HoodCleaningReport, Stampario, HoodStamp) sit alongside whatever you invoice with. All-in-ones (MyHoodClean, Smart Service, HoodOps) replace your scheduling and billing too.</p>
<h3>Report limits</h3><p>HoodCleaningReport caps reports per month by plan and sells packs, and Stampario&rsquo;s free plan stops at 5 reports a month. Count your reports in a busy month before you choose.</p></div></section>
<section class="sec"><div class="w"><h2>How we compared</h2>{METHOD}</div></section>
<section class="sec alt"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Hood cleaning software",slug)])

HF_SRC = {
 "nfpa": ("NFPA 96, 2024 edition, Table 12.4 (as quoted by IKECA)","https://www.ikeca.org/page/IKECAFAQs"),
 "nfpa_toc": ("NFPA 96, 2024 edition, free preview (table of contents)","https://nfpanorm.com/wp-content/preview/96%202024.pdf"),
 "nfpa_depth": ("NFPA 96 first-revision report for the 2026 edition (grease depth text)","https://docinfofiles.nfpa.org/files/AboutTheCodes/96/96_A2026_VEN_AAA_FD_FRReport.2.pdf"),
 "ifc": ("International Fire Code 2021, Section 607.3.3 (UpCodes)","https://up.codes/s/commercial-kitchen-hoods"),
}
HF_ST = [
 ("Massachusetts","Department of Fire Services / State Fire Marshal",
  "Anyone who cleans or inspects commercial cooking exhaust systems needs a State Fire Marshal certificate of competency. Type 1 (unrestricted, for contractors) requires at least 500 hours of experience; Type 2 is only for owners cleaning their own systems. Since January 1, 2018, hood cleaning companies also need a certificate of registration (Form FP-026A, $60, good for 2 years, one per business location). Labels follow 527 CMR 1.00: 50.5.6.13, and a certificate holder who finds an out-of-compliance system must notify the local fire department within 48 hours. Boston adds its own city registration.",
  [("Mass.gov: hood cleaning licenses","https://www.mass.gov/how-to/apply-for-commercial-hood-cleaning-and-inspection-licenses"),("Mass.gov: hood cleaning inspections","https://www.mass.gov/info-details/commercial-cooking-exhaust-system-inspections-hood-cleaning")]),
 ("Utah","Office of the State Fire Marshal",
  "Kitchen exhaust inspection and cleaning companies must be licensed by the State Fire Marshal under Utah Admin. Code R710-7, and each technician needs a certificate of registration (written exam on NFPA 96 and R710-7; $30 exam plus $40 annual certificate). Contractors must give the owner a completion and deficiency report. The service label has a set format: 5.5 by 4.5 inches, any color except red, with the company&rsquo;s license number, the technician&rsquo;s registration number, the service date punched in, and the next service due.",
  [("Utah SFM: kitchen exhaust duct cleaning","https://firemarshal.utah.gov/licensing-and-certification/kitchen-exhaust-duct-cleaning-systems/"),("Utah SFM service label sample (PDF)","https://firemarshal.utah.gov/wp-content/uploads/Hood-Service-Label-w-Instructions.pdf")]),
 ("Nevada","State Fire Marshal Division",
  "Cleaning Type 1 hood and duct systems needs a State Fire Marshal license for the firm (with a stick-on label approved under NAC 477.790) and a certificate of registration for each technician, who must pass an exam with at least 75%. Uncertified employees may help only while a certified person is on site supervising and fills out the certificate. The firm also needs a local business license where it works.",
  [("NAC 477.770","https://www.law.cornell.edu/regulations/nevada/NAC-477-770"),("NAC 477.300","https://www.law.cornell.edu/regulations/nevada/NAC-477-300")]),
 ("Portland, Oregon (city)","Portland Fire &amp; Rescue",
  "Anyone who cleans commercial hood and ventilation systems in Portland, contractor or in-house, needs a Fire Marshal Certificate of Fitness (Title 31, 31.20.110). Policy FIR-8.08 calls for inspection at least every 6 months (infrequent cooking, such as a lodge or church, can be extended to at most 2 years), cleaning to bare metal, and a label in the kitchen showing the date, the company and the technician&rsquo;s certificate number, and any areas not cleaned. The owner keeps reports on site for the Fire Marshal.",
  [("Portland FIR-8.08","https://www.portland.gov/policies/portland-fire-and-rescue/fixed-portable-fire-extinguishing-systems-equipment/fir-808")]),
]
def hood_freq_page():
    slug="hood-cleaning-frequency-requirements.html"
    title="How Often Must a Commercial Kitchen Hood Be Cleaned? NFPA 96 Schedule (2026)"
    desc=f"The NFPA 96 and International Fire Code inspection schedule for kitchen exhaust hoods (monthly, quarterly, semiannual, annual), grease depth limits, tag and record rules, state license examples and a free service record. Checked {CHK}."
    def src(k): n,u=HF_SRC[k]; return f'<a href="{u}" rel="noopener" target="_blank">{n}</a>'
    sched=[("Solid fuel cooking (wood, charcoal)","Monthly","1 month"),
           ("High volume: 24-hour cooking, charbroiling, wok cooking","Quarterly","3 months"),
           ("Moderate volume (most restaurants)","Semiannually","6 months (&ldquo;all other cooking operations&rdquo;)"),
           ("Low volume: churches and places of worship, day camps, seasonal businesses, senior centers","Annually","12 months")]
    srows="".join(f"<tr><td>{a}</td><td><b>{b}</b></td><td>{c}</td></tr>" for a,b,c in sched)
    strows="".join(f'<tr id="{sid(s[0].split(" (")[0].split(",")[0])}"><td>{s[0]}</td><td>{s[1]}</td><td>{s[2]}</td><td class="src">'+"<br>".join(f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' for n,u in s[3])+'</td></tr>' for s in HF_ST)
    flds=["Restaurant / site name and address","Date and time of service","Service type: inspection, cleaning, or both","Company name, address and phone","Technician name and license / certificate number","Cooking type and schedule used (monthly / quarterly / semiannual / annual)","Components inspected: hood, filters, plenum, ducts, access panels, fan","Grease depth readings and where measured","Components cleaned (to bare metal?)","Areas NOT cleaned or inaccessible, and why","Deficiencies found (e.g. missing access panels, fan hinge, damaged filters)","Before / after photos taken (Y/N)","Next service due","Tag / label applied on hood, old tag removed (Y/N)","Owner or manager signature, copy given (Y/N)"]
    form="".join(f"<tr><th>{E(x)}</th><td></td></tr>" for x in flds)
    faq=[("How often does a restaurant hood have to be cleaned?","The codes schedule <b>inspections</b>, and cleaning happens when an inspection finds grease buildup. NFPA 96 (2024 edition, Table 12.4) sets the inspection schedule at monthly for solid fuel cooking, quarterly for high-volume cooking (24-hour, charbroiling, wok), semiannually for moderate volume, and annually for low volume (churches, day camps, seasonal businesses, senior centers). The International Fire Code uses the same intervals. In practice, a busy kitchen ends up cleaned on roughly that schedule."),
         ("How much grease is too much?","NFPA 96 uses a depth gauge comb. Surfaces with 0.078 in. (2,000 &micro;m) of grease, or a fan housing with 0.125 in. (3,175 &micro;m), must be cleaned. That&rsquo;s the wording in NFPA&rsquo;s published revision report for the next edition, linked below."),
         ("Who decides which category my kitchen is in?","Your Authority Having Jurisdiction (AHJ), usually the local fire marshal. The IFC lets the fire code official approve a different interval, and some cities, like Portland, publish their own policy. Ask your fire department if you&rsquo;re unsure."),
         ("What has to go on the hood sticker?","Under IFC 2021 Section 607.3.3.3.1, the tag must show the service provider&rsquo;s name, address, phone number and the date of service, in a conspicuous spot, with older tags covered or removed. Some states prescribe the label in detail. Utah, for example, specifies its size, color and contents."),
         ("Do I need a license to clean hoods?","It depends on where you work. Massachusetts, Utah and Nevada require state licensing, and Portland, Oregon requires a city certificate. Many states have no hood-specific license, and the work is governed by the local fire code instead. Check with your state fire marshal and your city."),
         ("Is this legal advice?",f"No. It&rsquo;s a plain-English summary of NFPA 96, the International Fire Code and the official pages linked here, checked {CHK}. Your jurisdiction may adopt a different edition or add rules, and the official text is what counts.")]
    body = hero("Free guide &middot; kitchen exhaust cleaning","How often must a commercial kitchen hood be cleaned?",
      "The NFPA 96 and International Fire Code inspection schedule in one table, the grease depth that triggers a cleaning, what records and tags the code asks for, and four places that license hood cleaners. Plus a free next-service calculator and a printable service record.",
      [f"Checked {CHK}","Official sources linked","Free calculator + record","Not legal advice"],
      [("schedule","The schedule"),("calc","Next service due"),("grease","When to clean"),("records","Records and tags"),("states","Licensing examples"),("template","Printable record"),("faq","FAQ")])
    body += f'''<section class="sec" id="schedule"><div class="w"><h2>The inspection schedule</h2><p class="sub">Both codes set the minimum interval for <b>inspecting</b> the whole exhaust system for grease buildup. Inspection results decide whether it gets cleaned.</p>
<div class="tw"><table class="t"><thead><tr><th>Type or volume of cooking</th><th>NFPA 96 (2024), Table 12.4</th><th>IFC 2021, Table 607.3.3.1</th></tr></thead><tbody>{srows}</tbody></table></div>
<div class="note"><b>Sources:</b> {src("nfpa")}; {src("ifc")}. NFPA 96 says inspections must be done by a &ldquo;properly trained, qualified, and certified person(s) acceptable to the authority having jurisdiction.&rdquo; The IFC lets the fire code official approve other intervals.</div></div></section>
<section class="sec alt" id="calc"><div class="w"><h2>When is the next service due?</h2><p class="sub">Pick the cooking type and the last service date. This uses the code minimums above; your AHJ or a dirty system can call for sooner.</p>
<div class="calc"><form class="cin" onsubmit="return false" aria-label="Kitchen details">
<label for="ct">Cooking type</label><select id="ct"><option value="1">Solid fuel (wood or charcoal)</option><option value="3">High volume: 24-hour, charbroil, wok</option><option value="6" selected>Moderate volume (most restaurants)</option><option value="12">Low volume: church, day camp, seasonal, senior center</option></select>
<label for="ld">Last inspection or cleaning</label><input id="ld" type="date">
<p class="hint">Leave blank to use today.</p></form>
<div><div class="res" id="hout" aria-live="polite"></div></div></div></div></section>
<script>(function(){{var ct=document.getElementById('ct'),ld=document.getElementById('ld'),o=document.getElementById('hout');var nm={{1:'monthly',3:'quarterly',6:'semiannual',12:'annual'}};function f(d){{return d.toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}})}}function u(){{var m=+ct.value,b=ld.value?new Date(ld.value+'T12:00:00'):new Date();var n=new Date(b);n.setMonth(n.getMonth()+m);var t=new Date();t.setHours(0,0,0,0);var days=Math.round((n-t)/864e5);var st=days<0?'Overdue by '+(-days)+' days':days+' days from today';var h='<div class="row best"><div><div class="nm">Next inspection due</div><div class="pl">'+nm[m]+' schedule, every '+m+' month'+(m>1?'s':'')+'</div></div><div class="amt">'+f(n)+'<small>'+st+'</small></div></div>';var y=[];var c=new Date(b);for(var i=0;i<Math.max(1,Math.round(12/m));i++){{c=new Date(c);c.setMonth(c.getMonth()+m);y.push(f(c))}}h+='<div class="row"><div><div class="nm">Next 12 months</div><div class="pl">'+y.join(' &middot; ')+'</div></div><div class="amt">'+y.length+'<small>visits a year</small></div></div>';o.innerHTML=h}}ct.addEventListener('change',u);ld.addEventListener('input',u);u()}})();</script>
<section class="sec" id="grease"><div class="w nw"><h2>When does a hood have to be cleaned?</h2><p>When the inspection finds grease. Under the IFC, if hoods, grease-removal devices, fans, ducts or other parts have an accumulation of grease, they &ldquo;shall be cleaned in accordance with ANSI/IKECA C10&rdquo; (Section 607.3.3.2). NFPA 96 gives a measurable trigger: place a <b>grease depth gauge comb</b> on the surface, and clean when it reads <b>0.078 in. (2,000 &micro;m)</b> on a surface or <b>0.125 in. (3,175 &micro;m)</b> in a fan housing.</p>
<div class="note w2"><b>Source for the depth limits:</b> {src("nfpa_depth")}, which shows the current text alongside the proposed renumbering. Section titles for the 2024 edition are in the {src("nfpa_toc")}.</div></div></section>
<section class="sec alt" id="records"><div class="w nw"><h2>Records and tags the fire code asks for</h2>
<h3>Records (IFC 2021, 607.3.3.3)</h3><p>After every inspection, record the individual and company that did it, a description of the inspection, and when it happened. After every cleaning, record the individual and company and when it happened. Records must be completed after each visit and kept.</p>
<h3>Tags (IFC 2021, 607.3.3.3.1)</h3><p>When the hood or duct system is inspected, leave a tag in a conspicuous location with the service provider&rsquo;s name, address, phone number and date of service. Cover or remove older tags.</p>
<h3>Reports to the owner</h3><p>Several jurisdictions go further. Utah requires a completion and deficiency report for the owner, and Portland requires the label to list any areas not cleaned and the owner to keep reports on site.</p></div></section>
<section class="sec" id="states"><div class="w"><h2>Licensing examples: four places with their own rules</h2><p class="sub">Not every state licenses hood cleaners. These four publish specific requirements, checked {CHK}. Elsewhere, ask your state fire marshal and the city fire department.</p>
<div class="tw"><table class="t"><thead><tr><th>Where</th><th>Agency</th><th>What it requires (summary)</th><th>Official source</th></tr></thead><tbody>{strows}</tbody></table></div></div></section>
<section class="sec alt" id="template"><div class="w nw"><h2>Free printable hood service record</h2><p class="sub">One sheet per visit. It covers the IFC record and tag fields plus the details owners and fire marshals usually ask for. Add your state&rsquo;s license fields.</p>
<p class="noprint"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button></p>
<div class="form"><h3>Kitchen exhaust inspection / cleaning record</h3><table>{form}</table></div>
<p style="font-size:13px;color:var(--mute)">Template by Orvian Market. Free to copy and use. Not legal advice; your jurisdiction&rsquo;s rules are what count.</p></div></section>
<section class="sec" id="software"><div class="w nw"><h2>Doing this in an app instead</h2><p>Hood cleaning apps fill in the record, take photos, track grease readings and schedule the next visit from the cooking type. Free options exist: Stampario&rsquo;s free plan covers 5 reports a month and HoodStamp lists 3 free certificates a month. Paid all-in-ones such as MyHoodClean ($49.99/mo) also schedule and invoice. See the <a href="best-hood-cleaning-software.html">hood cleaning software comparison</a> for prices and sources.</p></div></section>
<section class="sec alt" id="faq"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Hood cleaning frequency",slug)])

ST_SRC = {
 "ikeca_faq": ("IKECA FAQ (membership, certification, NFPA 96 12.6.1)","https://www.ikeca.org/page/IKECAFAQs"),
 "cect": ("IKECA CECT exam fee","https://www.ikeca.org/store/ListProducts.aspx?catid=918390"),
 "cect_rules": ("IKECA certification: CECT scoring and retakes","https://www.ikeca.org/page/IKECACertification"),
 "cect_app": ("IKECA CECT application","https://www.ikeca.org/page/CECTAPP"),
 "cecs": ("IKECA CECS exam fee","https://www.ikeca.org/store/viewproduct.aspx?id=21076218"),
 "cesi": ("IKECA CESI exam fees","https://www.ikeca.org/store/ListProducts.aspx?catid=906371"),
 "pa_course": ("Phil Ackland kitchen exhaust certification course","https://powerwashacademy.com/kitchen-exhaust-certification-course/"),
 "pa_recert": ("Phil Ackland certification forms (recertification price)","https://philacklandtraining.com/phil-acklands-exhaust-cleaners-certification-forms/"),
 "nh": ("NH DES: Kitchen exhaust hood cleaning guidance (PDF, Dec 2020)","https://www.des.nh.gov/sites/g/files/ehbemt341/files/documents/2020-01/co-17-01.pdf"),
 "corv": ("City of Corvallis, OR: Commercial hood cleaners","https://www.corvallisoregon.gov/publicworks/page/commercial-hood-cleaners"),
 "osha": ("OSHA 29 CFR 1910.28, duty to have fall protection","https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.28"),
 "halo": ("Halo Restoration Services: average hood cleaning cost","https://www.halorestorationservices.com/blog/hood-cleaning-cost/"),
 "esti": ("EstiCube: commercial hood cleaning cost guide","https://esticube.com/guides/commercial-hood-cleaning-cost"),
 "hcr_quote": ("HoodCleaningReport: free hood cleaning quote template","https://hoodcleaningreport.com/tools/hood-cleaning-quote-template/"),
 "qwick": ("Qwick hood cleaning quote page","https://qwicksolutions.com/quote"),
}
def start_page():
    slug="how-to-start-a-hood-cleaning-business.html"
    title="How to Start a Hood Cleaning Business (2026): Licenses, Certification, Insurance and Costs"
    desc=f"A sourced startup guide for kitchen exhaust (hood) cleaning: state license examples, IKECA and Phil Ackland certification costs, insurance, wastewater and roof safety rules, pricing benchmarks and a printable checklist. Checked {CHK}."
    def s(k): n,u=ST_SRC[k]; return f'<a href="{u}" rel="noopener" target="_blank">{n}</a>'
    certs=[("Phil Ackland 5-day kitchen exhaust certification course","Hands-on training plus Phil Ackland&rsquo;s own certification test, NFPA 96 copy and forms","$4,500 per attendee, hotel included; recertification $369 ($747 if lapsed over a year)","New owners and crew leaders who need hands-on training first",["pa_course","pa_recert"]),
           ("IKECA CECT (Certified Exhaust Cleaning Technician)","100 multiple-choice questions, 2 hours, closed book, 70% to pass, English or Spanish","$325 exam (listed price); retakes $80, up to two; study guide $60","Field technicians: IKECA calls it the baseline certification",["cect","cect_rules","cect_app"]),
           ("IKECA CECS (Certified Exhaust Cleaning Specialist)","Online-proctored exam for experienced professionals","$750 exam (listed price)","Seasoned cleaners and business owners",["cecs","ikeca_faq"]),
           ("IKECA CESI (Certified Exhaust System Inspector)","Online-proctored exam for inspection roles","$1,020 exam (listed price); retake $100; study guide $60","Inspection and code-enforcement work",["cesi","ikeca_faq"])]
    crow="".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td class="src">'+"<br>".join(f'<a href="{ST_SRC[k][1]}" rel="noopener" target="_blank">source</a>' for k in ks)+'</td></tr>' for a,b,c,d,ks in certs)
    steps=[("Check your state and city rules","Some states and cities license hood cleaners; most leave it to the local fire marshal.","rules"),
           ("Get hands-on training","IKECA says its certifications don&rsquo;t replace training for people new to the trade.","certs"),
           ("Earn a certification","NFPA 96 asks for a certified person, and some states name the exam.","certs"),
           ("Insure the business","Customers and trade groups ask for a certificate of insurance before you start.","insurance"),
           ("Plan wastewater disposal","Greasy, caustic wash water must never reach a storm or roof drain.","water"),
           ("Set up roof and access safety","Fan cleaning means roof work and fall protection.","roof"),
           ("Price the year, document every visit","Quote per visit and per year, then leave a record and tag every time.","price")]
    stp="".join(f'<li><a href="#{a}"><b>{E(t) if "&" not in t else t}</b></a> {d}</li>' for t,d,a in steps)
    checklist=["Called the state fire marshal and city fire department; written down any license, registration or exam needed","Local business license and registration for each city or county you&rsquo;ll work in","Hands-on training completed (course name and date)","Certification held by at least one person on every crew (number and expiry date)","Certificate of insurance on file; limits match what your target customers ask for","Workers&rsquo; compensation in place before hiring, where your state requires it","Wastewater plan: collection tubs, pH strips, interceptor or licensed hauler, and the local pretreatment contact","Roof plan: ladder or hatch access, fall protection, fan hinge kits on upblast fans","Grease depth gauge, photos before and after, and a service record for every visit","Service tag format that meets your fire code (company name, address, phone, date)","Price sheet: per hood foot, per fan, per duct foot, minimum charge, access and after-hours adders","Reminder system for each customer&rsquo;s next service date"]
    form="".join(f'<tr><td style="width:28px">&#9744;</td><td>{c}</td></tr>' for c in checklist)
    faq=[("Do I need a license to clean commercial kitchen hoods?","It depends on where you work. Massachusetts, Utah and Nevada license or register hood cleaners at the state level, and Portland, Oregon requires a city certificate of fitness. Many other places have no separate license, but NFPA 96 (2024, Section 12.6.1) says contaminated systems must be cleaned by a properly trained, qualified and certified person acceptable to the authority having jurisdiction. Ask your state fire marshal and local fire department."),
         ("Is IKECA certification required?","Not by IKECA itself for individuals, but some fire marshals and customers ask for a recognized certification, and IKECA requires a qualifying credential from North American cleaning companies that want to join as members. IKECA doesn&rsquo;t track local legal requirements."),
         ("How much does hood cleaning certification cost?",f"Listed prices checked {CHK}: IKECA CECT exam $325, CECS $750 and CESI $1,020 (members may see different pricing after signing in), study guides $60. The Phil Ackland 5-day course is $4,500 per attendee with a hotel included."),
         ("Can hood cleaning wash water go down a storm drain?","No. New Hampshire&rsquo;s environmental agency calls it illegal to discharge grease and cleaning chemicals to anything that drains to a stormwater system, including roof drains and parking lots. Collect it and use a licensed hauler or a working grease interceptor, within your local sewer limits."),
         ("What should I charge for a hood cleaning job?","Published industry ranges put hood cleaning at about $10&ndash;$20 per linear foot of hood and $40&ndash;$60 per fan, with typical minimum charges around $400&ndash;$450. Your local market, duct length and roof access change it a lot, so build your price from your own costs.")]
    body = hero("Hood cleaning &middot; startup guide","How to start a hood cleaning business (2026)",
      "What you actually need before your first kitchen exhaust job: the rules where you work, training and certification, insurance, a wastewater plan, roof safety and a price sheet. Every cost here links to its source.",
      [f"Checked {CHK}","Official and vendor sources linked","Printable checklist","Not legal advice"],
      [("rules","License rules"),("certs","Certification costs"),("insurance","Insurance"),("water","Wastewater"),("roof","Roof safety"),("price","Pricing"),("checklist","Checklist"),("faq","FAQ")])
    body += f'''<section class="sec"><div class="w nw"><h2>The seven steps</h2><ol class="steps">{stp}</ol></div></section>
<section class="sec alt" id="rules"><div class="w nw"><h2>1. Check what your state and city require</h2>
<p>There is no single national hood cleaning license in the US. The baseline is NFPA 96, the fire standard most jurisdictions adopt: when an exhaust system is contaminated with grease, it &ldquo;shall be cleaned by a properly trained, qualified, and certified person(s) acceptable to the authority having jurisdiction&rdquo; (2024 edition, Section 12.6.1, quoted in the {s("ikeca_faq")}). The &ldquo;authority having jurisdiction&rdquo; is usually your local fire marshal.</p>
<p>Some places go further and license the company, the technician, or both:</p>
<ul><li><b>Massachusetts:</b> State Fire Marshal certificate of competency for anyone who cleans or inspects these systems, plus a company certificate of registration.</li><li><b>Utah:</b> a State Fire Marshal company license and a registered technician (written exam).</li><li><b>Nevada:</b> a State Fire Marshal firm license plus a certificate of registration for each technician (exam, 75% to pass).</li><li><b>Portland, Oregon:</b> a Fire Marshal certificate of fitness for anyone cleaning hoods in the city.</li></ul>
<p>Details, fees and official links for all four are in our <a href="hood-cleaning-frequency-requirements.html#states">hood cleaning schedule and licensing guide</a>. Even IKECA, the industry association, says it doesn&rsquo;t track local rules and recommends starting with your local regulatory authority. Ask the state fire marshal and the fire department in each city you plan to serve, and get a regular business license there too.</p></div></section>
<section class="sec" id="certs"><div class="w"><h2>2&ndash;3. Training and certification: what it costs</h2><p class="sub">Listed prices on each provider&rsquo;s site, checked {CHK}. IKECA&rsquo;s store says &ldquo;Sign in for your pricing,&rdquo; so members may pay a different amount.</p>
<div class="tw"><table class="t"><thead><tr><th>Program</th><th>Format</th><th>Cost</th><th>Who it&rsquo;s for</th><th>Source</th></tr></thead><tbody>{crow}</tbody></table></div>
<div class="note"><b>Order matters.</b> IKECA says its certifications are knowledge tests and &ldquo;not a substitution&rdquo; for hands-on training for people new to the trade, so plan training first. IKECA certifies individuals, not companies. Company membership is a separate step: $995 a year for Active North American members or $595 for a one-year Introductory membership, and new companies get 90 days to show a qualifying credential and proof of insurance ({s("ikeca_faq")}).</div></div></section>
<section class="sec alt" id="insurance"><div class="w nw"><h2>4. Insurance</h2>
<p>Expect to show a certificate of insurance (COI) before you work on a customer&rsquo;s system. IKECA asks new member companies for proof of insurance, and hood companies advertise their coverage to buyers; one, for example, lists &ldquo;$1M/$2M COI on file&rdquo; on its {s("qwick")}.</p>
<p>We don&rsquo;t sell insurance and can&rsquo;t tell you what limits you need. Ask a commercial insurance broker who covers hood cleaning work which policies your state and your target customers require. That usually means general liability, commercial auto for the work vehicle, and workers&rsquo; compensation once you hire, since most states require it for employees.</p></div></section>
<section class="sec" id="water"><div class="w nw"><h2>5. Wastewater: keep it out of storm drains</h2>
<p>Hood cleaning makes greasy, often caustic wash water. New Hampshire&rsquo;s environmental agency puts it plainly: it is illegal to discharge pollutants &ldquo;directly to, or indirectly into, an area that could drain to a stormwater system,&rdquo; which includes roof drains, storm drains, roads, ditches and parking lots ({s("nh")}).</p>
<ul><li><b>Scrape first.</b> Remove as much grease as possible mechanically before chemicals and rinse water.</li><li><b>Collect the water.</b> Use a licensed hauler where possible, or a drain connected to a working grease interceptor if your local rules allow it.</li><li><b>Test the pH.</b> NH DES says wastewater must typically stay between pH 5.0 and 12.5, and above 12.5 it&rsquo;s hazardous and can&rsquo;t go down any drain. A test strip checks it.</li><li><b>Watch the temperature.</b> Corvallis, Oregon, for example, prohibits discharges over 150&deg;F and tells hood cleaners to let water cool before it goes through an interceptor ({s("corv")}).</li><li><b>Protect the roof drain.</b> Roof drains usually connect to stormwater systems, so contain any runoff from the fan.</li></ul>
<p>Call the local wastewater (pretreatment) office before your first job to learn its limits.</p></div></section>
<section class="sec alt" id="roof"><div class="w nw"><h2>6. Roof and access safety</h2>
<p>A full system clean ends at the exhaust fan on the roof, so plan for roof work. OSHA&rsquo;s general industry rule on walking-working surfaces includes fall protection requirements for work on roofs ({s("osha")}); read the low-slope roof sections and set up guardrails, anchors or a designated area before you send a crew up.</p>
<p>Two equipment points come straight from NFPA 96 via IKECA: upblast fans are required to have hinges (2024 edition, 8.1.2.1), and access panels may be needed to reach and clean the whole duct. Hinge kits and access panels are also extra line items you can quote.</p></div></section>
<section class="sec" id="price"><div class="w nw"><h2>7. Pricing and paperwork</h2>
<p>Published industry ranges give you a starting point, not a price list. One cost guide puts flat-rate hood cleaning at about <b>$10&ndash;$20 per linear foot of hood</b> and <b>$40&ndash;$60 per fan</b>, with typical minimum charges of <b>$400&ndash;$450</b> ({s("halo")}). Another uses $18 per foot of hood, $95 per fan and $9 per foot of duct as national planning numbers, with a $375 minimum ({s("esti")}). Build your own price from labor, chemicals, travel and insurance, then check it against your local market.</p>
<p>Quote the year, not just the visit: a quarterly kitchen is four visits, and that yearly number is what owners compare. Our <a href="hood-cleaning-frequency-requirements.html">NFPA 96 schedule guide</a> has a next-service calculator. For the quote itself, the {s("hcr_quote")} does the math on your own rates for free.</p>
<p>After every visit, the fire code expects a record (who did the work, what was done, when) and a tag in the kitchen. Our schedule guide covers those rules and has a free printable service record. When paper gets old, see the <a href="best-hood-cleaning-software.html">hood cleaning software comparison</a>, which includes free plans.</p></div></section>
<section class="sec alt" id="checklist"><div class="w nw"><h2>Free printable startup checklist</h2><p class="sub">Tick these off before your first paying job.</p>
<p class="noprint"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button></p>
<div class="form"><h3>Hood cleaning business startup checklist</h3><table>{form}</table></div>
<p style="font-size:13px;color:var(--mute)">Checklist by Orvian Market. Free to copy and use. Not legal, tax or insurance advice.</p></div></section>
<section class="sec" id="faq"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Start a hood cleaning business",slug)])

# ---- page 7: pest control license requirements by state (added 2026-10-17 8:20 PM block) ----
LIC = [
 dict(st="Texas", ag="Texas Department of Agriculture, Structural Pest Control Service (SPCS)",
  biz="Commercial business license for each business location, including branch offices. You can&rsquo;t advertise or solicit until it&rsquo;s issued.",
  who="A <b>responsible commercial certified applicator</b> registered with the business, who can&rsquo;t be the responsible applicator for any other business or location.",
  exp="12 months of verifiable pest control experience in the past 24 months plus at least 6 months holding an SPCS technician license; or a qualifying biological-science degree; or 12 of the past 24 months of related industry experience. Technicians first complete 20 classroom hours, 40 on-the-job and 8 classroom hours per category, and a 6-hour approved course.",
  ins="At least $500,000 bodily injury and property damage per occurrence, $1,000,000 aggregate, on TDA form ALS-1101.",
  fees=[("Commercial business license (per location)",300),("Certified applicator license",125)],
  nf="Each apprentice or technician also registers for $125. Exam fees are paid to TDA&rsquo;s testing vendor (Metro) after TDA pre-approves you.",
  src=[("TDA: business license","https://texasagriculture.gov/Regulatory-Programs/Pesticides/Structural-Pest-Control-Service/Structural-Pest-Control-Business"),("TDA: exams and eligibility","https://texasagriculture.gov/Regulatory-Programs/Pesticides/Structural-Pest-Control-Service/Structural-Pest-Control-Exams"),("TDA: technician licensing","https://texasagriculture.gov/Regulatory-Programs/Pesticides/Structural-Pest-Control-Service/Structural-Pest-Control-Licensing/SPCS-Technician-and-Apprentice-Licensing")]),
 dict(st="Florida", ag="Florida Department of Agriculture and Consumer Services (FDACS)",
  biz="A business license for each pest control business location, renewed every year.",
  who="A full-time <b>certified operator in charge</b>, certified in every category the location works in (general household pest and rodent, termite and other WDO, lawn and ornamental, fumigation).",
  exp="Three years as a service employee of a licensee in the category, one of them in Florida immediately before you apply; or a qualifying degree (20 semester hours in entomology, botany, agronomy or horticulture) plus one year. FDACS&rsquo;s exam application also asks you to document at least 45 jobs per category.",
  ins="$250,000 per person and $500,000 per occurrence bodily injury, plus $250,000 per occurrence and $500,000 aggregate property damage, or a $500,000 combined single limit.",
  fees=[("Business license (per location, yearly)",300),("Certified operator exam (per category)",300)],
  nf="Employee ID cards are $10 each, and the operator certificate renews at $150 a year.",
  src=[("FDACS: licensing and certification","https://www.fdacs.gov/Business-Services/Pest-Control/Licensing-and-Certification"),("FDACS: fee schedule","https://www.fdacs.gov/Business-Services/Pest-Control/Pest-Control-FAQ/What-are-the-pest-control-licensing-fees"),("F.S. 482.132","https://www.flsenate.gov/Laws/Statutes/2026/482.132")]),
 dict(st="California", ag="Structural Pest Control Board (SPCB)",
  biz="Company registration with the SPCB, in each branch you work in (Branch 1 fumigation, Branch 2 general pest, Branch 3 wood-destroying organisms).",
  who="A <b>Qualifying Manager</b>: a licensed Operator in the same branch who supervises the company&rsquo;s daily business.",
  exp="For a Branch 2 Operator license: two years of Branch 2 field experience, including one year as a licensed Branch 2 Field Representative (one year = 1,600 hours of field work), plus board-approved pre-operator courses taken within 3 years before the exam. Live Scan fingerprints.",
  ins="$500,000 general liability, a $12,500 surety bond, and workers&rsquo; compensation (or a filed exemption).",
  fees=[("Operator exam",100),("Operator license",150)],
  nf="The company registration fee comes in the SPCB registration packet.",
  src=[("SPCB: become an Operator","https://www.pestboard.ca.gov/howdoi/opr.shtml"),("SPCB: start a company","https://www.pestboard.ca.gov/howdoi/pr.shtml"),("SPCB: examinations","https://www.pestboard.ca.gov/exam/index.shtml")]),
 dict(st="Georgia", ag="Georgia Department of Agriculture, Structural Pest Control",
  biz="A structural pest control <b>company license</b> for anyone doing the work for hire.",
  who="A <b>Designated Certified Operator (DCO)</b> for each category. The owner can be the DCO if certified; otherwise hire one.",
  exp="Two years of verifiable structural pest control experience (one within the last five years), or a degree in entomology, public health or a related subject plus one year of service experience in the last five. Pass the core exam plus a category exam. No reciprocity with other states.",
  ins="Household pest and fumigation: $50,000 bodily injury and $50,000 property damage per occurrence, $200,000 annual aggregate. Wood-destroying organisms: $100,000 / $100,000 / $500,000 plus errors and omissions. Pollution liability for sudden and accidental release.",
  fees=[("Certified operator exam (per category)",45),("Certified operator credential",100)],
  nf="The company license fee and a required UGA urban entomology research fee are listed on the application.",
  src=[("GDA: company license","https://agr.georgia.gov/structural-pest-control-company-license"),("GDA: certified operator license","https://www.agr.georgia.gov/certified-operator-license"),("GDA: insurance form (PDF)","https://agr.georgia.gov/sites/default/files/documents/pest-control/sps-13-06-insurance-form.pdf")]),
 dict(st="North Carolina", ag="NCDA&amp;CS Structural Pest Control and Pesticides Division",
  biz="A <b>structural pest control license</b> (held by a person, by phase: P household pests, W wood-destroying organisms, F fumigation) to work on property you or your employer don&rsquo;t own.",
  who="The licensee must first be an NC <b>Certified Applicator</b> in good standing in that phase.",
  exp="Two years of independently verifiable experience in that phase (employer affidavits, or customer letters if self-employed), then pass the phase exam. FBI background check dated within 6 months. College training can substitute for some experience.",
  ins="Proof of insurance, sent by the insurer to NCDA&amp;CS, before the license is issued. Amounts are set in the rules.",
  fees=[("License, first phase (yearly)",200),("License exam (per attempt, per phase)",50),("Certified applicator ID card",50)],
  nf="Each extra phase adds $75; employee ID cards are $40 each.",
  src=[("NCDA&amp;CS: structural licensing","https://www.ncagr.gov/divisions/structural-pest-control-and-pesticides/structural/licensing-and-certification"),("NCDA&amp;CS: license exams","https://www.ncagr.gov/divisions/structural-pest-control-and-pesticides/structural/licensing-and-certification/exam"),("G.S. 106-65.31 (fees)","https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_106/GS_106-65.31.pdf")]),
 dict(st="Arizona", ag="Arizona Department of Agriculture, Pest Management Division (PMD)",
  biz="A PMD <b>business license</b> for anyone who advertises, inspects, bids on or applies pesticides for structural pest management.",
  who="A <b>Qualifying Party (QP)</b>: a Qualified Applicator registered as responsible for training, equipping and supervising the company&rsquo;s applicators.",
  exp="To be a Qualified Applicator: 24 months as a certified applicator in the category within the last 10 years, or 12 months plus qualifying coursework or a degree, or 24 months of pest management business experience in a state that didn&rsquo;t require a license. Pass core and category exams at 75%. Fingerprint background check.",
  ins="Proof of financial security filed with the business license application.",
  fees=[("Business license",185),("Qualified Applicator application",75),("QP registration (filed with the business license)",0)],
  nf="Certified Applicators (your techs) apply for $55 each.",
  src=[("AZDA PMD: FAQs (requirements and fees)","https://agriculture.az.gov/divisions/environmental-consumer-protection-division/pest-management-division/pest-management-faqs"),("A.A.C. R3-8-103 (fees)","https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R3-8-103")]),
 dict(st="Ohio", ag="Ohio Department of Agriculture",
  biz="A <b>pesticide business license</b>, with each registered location listed, to apply pesticides for hire. The licensing period runs October 1 to September 30.",
  who="Licensed <b>commercial applicators</b> do the work.",
  exp="A commercial applicator license needs a passing score on the exams for each pesticide use category you apply in.",
  ins="Proof of financial responsibility, required before the license is issued and each renewal.",
  fees=[("Pesticide business license (and each added location)",35),("Commercial applicator license",35)],
  nf="Late renewals cost 50% more.",
  src=[("OAC 901:5-11-03 (business license)","https://codes.ohio.gov/ohio-administrative-code/rule-901:5-11-03"),("OAC 901:5-11-04 (commercial applicator)","https://codes.ohio.gov/ohio-administrative-code/rule-901:5-11-04")]),
 dict(st="Pennsylvania", ag="Pennsylvania Department of Agriculture",
  biz="A <b>pesticide application business license</b>, renewed every year.",
  who="At least one <b>certified applicator</b>. Technicians who apply under supervision register with the department.",
  exp="Commercial applicators pass the core exam and a category exam.",
  ins="At least $100,000 bodily injury and $100,000 property damage per occurrence, covering completed operations and pesticide application, with a deductible no higher than $2,500.",
  fees=[("Business license (yearly)",35),("Commercial applicator certificate (yearly)",40),("Core exam",50),("Category exam",10)],
  nf="Commercial technician registration is $30 a year.",
  src=[("PDA: pesticide application businesses","https://www.pa.gov/agencies/pda/plants-land-water/plant-industry/pesticide-programs/pesticide-application-businesses"),("7 Pa. Code &sect;128.3 (fees)","https://www.pacodeandbulletin.gov/secure/pacode/data/007/chapter128/s128.3.html"),("7 Pa. Code &sect;128.34 (insurance)","https://www.pacodeandbulletin.gov/Display/pacode?d=reduce&file=%2Fsecure%2Fpacode%2Fdata%2F007%2Fchapter128%2Fs128.34.html")]),
 dict(st="New York", ag="NYS Department of Environmental Conservation (DEC)",
  biz="A <b>business registration</b> for each business address. It lasts about 3 years, with the expiry date set by DEC region.",
  who="A <b>certified applicator</b> in each category. For the structural subcategories (7a&ndash;7d, 7f, 7g) a technician isn&rsquo;t enough.",
  exp="One year as a certified technician plus 12 hours of category training, or two years as a technician; or three years of full-time apprentice experience within the last five years plus the core and category exams.",
  ins="Commercial general liability of at least $1,000,000 per occurrence, with NYSDEC named as certificate holder.",
  fees=[("Business registration (about 3 years)",900),("Applicator certification, first category",450),("Exams: core + one category ($100 each)",200)],
  nf="Each extra category or subcategory is $150.",
  src=[("NYSDEC: business registration","https://dec.ny.gov/environmental-protection/pesticides/business-agency-information"),("6 NYCRR 325.8 (eligibility)","https://www.law.cornell.edu/regulations/new-york/6-NYCRR-325.8"),("ECL &sect;33-0911 (fees)","https://law.justia.com/codes/new-york/env/article-33/title-9/33-0911/")]),
 dict(st="Illinois", ag="Illinois Department of Public Health (Structural Pest Control)",
  biz="A <b>commercial structural pest control business license</b> for each business location, renewed by December 1 every year.",
  who="At least one <b>certified technician</b> at the business.",
  exp="General-use pesticides: pass the General Standards exam. Restricted-use pesticides: also pass subcategory exams. Certification renews every 3 years.",
  ins="A certificate of insurance on IDPH&rsquo;s own form, sent by your insurer.",
  fees=[("Business license (per location)",250)],
  nf="Technician exam fees are on IDPH&rsquo;s technician application.",
  src=[("IDPH: structural pest control","https://dph.illinois.gov/topics-services/environmental-health-protection/structural-pest-control.html"),("IDPH: business license application (PDF)","https://dph.illinois.gov/content/dam/soi/en/web/idph/files/forms/structural-pest-control-license-application-commercial-business-101817.pdf")]),
 dict(st="Virginia", ag="Virginia Department of Agriculture and Consumer Services (VDACS)",
  biz="A <b>pesticide business license</b> for each location or outlet. It expires March 31 every year.",
  who="A <b>certified commercial applicator</b>. The applicant or an employee also passes the business license exam, unless they&rsquo;re already certified.",
  exp="One year as a Virginia Registered Technician, or one year of pesticide-related education, training or experience. Certificates expire June 30 of the second year after issue.",
  ins="At least $100,000 property damage, $100,000 for injury or death of one person, and $300,000 per occurrence.",
  fees=[("Business license (per location, yearly)",75),("Commercial applicator certificate",25)],
  nf="Reexamination is $25.",
  src=[("VDACS: pesticide business license","https://www.vdacs.virginia.gov/pesticide-business-license.shtml"),("2VAC5-675-50 (business fee)","https://law.lis.virginia.gov/admincode/title02/agency5/chapter675/section50/"),("2VAC5-675-30 (applicator fee)","https://law.lis.virginia.gov/admincode/title02/agency5/chapter675/section30/")]),
 dict(st="Tennessee", ag="Tennessee Department of Agriculture",
  biz="A <b>pesticide charter</b> for each office that does commercial pest control. Charters expire June 30 of odd-numbered years.",
  who="Each charter names the licensed <b>pest control operator(s)</b> who supervise the work, plus a roster of registered solicitors and technicians.",
  exp="The supervising operator must hold a Tennessee license in the categories offered. See the department&rsquo;s certification page for the exam steps.",
  ins="Proof of a bond and liability insurance. If either lapses the charter expires at once, with a 30-day grace period to send new proof.",
  fees=[],
  nf="The charter fee and the per-person technician fee are tiered fees under T.C.A. &sect;43-1-703 and can be prorated in the first term; the current amounts are on the charter application.",
  src=[("Tenn. Comp. R. &amp; Regs. 0080-09-04-.03 (charters)","https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0080-09-04-.03"),("TDA: certification, licensing and charters","https://www.tn.gov/agriculture/businesses/pesticides/certification.html")]),
]
def lic_page():
    slug="pest-control-license-requirements-by-state.html"
    title="Pest Control License Requirements by State (2026): Fees, Experience and Insurance"
    desc=f"What it takes to license a pest control business in TX, FL, CA, GA, NC, AZ, OH, PA, NY, IL, VA and TN: the business license, who must qualify it, experience, insurance minimums and official fees. Checked {CHK}."
    def fee_txt(v):
        f="; ".join(f"{n}: <b>${a:,}</b>" for n,a in v["fees"]) if v["fees"] else "Not stated as a flat amount (see note)"
        return f+(f'. <span style="color:var(--mute);font-size:13px">{v["nf"]}</span>' if v["nf"] else "")
    def lcard(v):
        srcs=" &middot; ".join(f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' for n,u in v["src"])
        return f'<div class="card" id="{sid(v["st"])}"><h3>{v["st"]}</h3><p class="for">{v["ag"]}</p><p class="price"><b>Business license:</b> {v["biz"]}</p><p class="price"><b>Who qualifies it:</b> {v["who"]}</p><p class="price"><b>Experience:</b> {v["exp"]}</p><p class="price"><b>Insurance:</b> {v["ins"]}</p><p class="price"><b>Listed state fees:</b> {fee_txt(v)}</p><p class="watch"><b>Official sources:</b> {srcs}</p></div>'
    rows="".join(lcard(v) for v in LIC)
    jump=" &middot; ".join(f'<a href="#{sid(v["st"])}">{v["st"]}</a>' for v in LIC)
    cdata=json.dumps({v["st"]:{"f":v["fees"],"n":plain(v["nf"]),"i":plain(v["ins"]),"w":plain(v["who"])} for v in LIC})
    opts="".join(f'<option{" selected" if v["st"]=="Texas" else ""}>{v["st"]}</option>' for v in LIC)
    checklist=["Found your state&rsquo;s lead agency and read its licensing page (linked in the table)","Decided who qualifies the business: you, or a certified person you hire","Counted that person&rsquo;s documented experience against the state&rsquo;s minimum (dates, hours, employer letters)","Booked any required pre-exam training or courses","Passed the core exam and each category exam you&rsquo;ll work in","Insurance certificate on the state&rsquo;s own form, at or above its minimums (and a bond, if required)","Business license or registration issued for each location before advertising","Technicians and salespeople registered, where the state requires it","Local business license and registration with your city or county","Application record forms or software ready before the first job (see our <a href=\"pesticide-application-records-by-state.html\">records guide</a>)","Renewal dates and continuing-education hours on the calendar"]
    form="".join(f'<tr><td style="width:28px">&#9744;</td><td>{c}</td></tr>' for c in checklist)
    faq=[("Do I need a license to start a pest control business?","In every state we checked, yes. Each one requires a business license, registration or charter for the company, and a certified or licensed person who qualifies it. Who that person must be, and how much experience they need, is what varies most."),
         ("Can I get a pest control license with no experience?","Usually not to qualify a business on your own. Most of the 12 states require one to three years of documented experience for the person in charge (for example 2 years in California, Georgia and North Carolina, 3 years in Florida), though a related degree can shorten it in several states. A common path is to work as a registered technician first, or to hire a certified operator to qualify your company while you get your own hours."),
         ("How much does a pest control license cost?",f"The state fees themselves are modest. In the table, the business license runs from $35 a year (Ohio, Pennsylvania) to $300 (Texas, Florida) or $900 for a roughly 3-year New York registration, and exams run from $10 to $300 each. Insurance, bonds, training courses and your time cost far more. All figures are listed state fees checked {CHK}."),
         ("Is a pest control license good in other states?","Generally no. Georgia and North Carolina both say they have no reciprocal licensing agreements, and most states make you meet their own exam and experience rules. Arizona lets the director waive exams in whole or in part for someone certified in another state."),
         ("Is this legal advice?",f"No. It&rsquo;s a plain-English summary of each state&rsquo;s official pages and rules, checked {CHK}, with every source linked. Fees and rules change, so confirm with the agency before you apply.")]
    body = hero("Free guide &middot; pest control licensing","Pest control license requirements by state",
      "What it takes to license a pest control company in 12 big pest-control states: the business license, the certified person who has to qualify it, the experience they need, insurance minimums and the state&rsquo;s own fees. Every row links to the official source.",
      [f"Checked {CHK}","Official sources linked","Fee totals by state","Not legal advice"],
      [("how","How it works"),("calc","Fees by state"),("table","State table"),("checklist","Checklist"),("software","After licensing"),("faq","FAQ")])
    body += f'''<section class="sec" id="how"><div class="w nw"><h2>How pest control licensing works</h2>
<p>Almost every state licenses two things separately. The <b>business</b> gets a license, registration or charter for each location. A <b>certified person</b> (called a certified operator, qualifying manager, qualifying party or responsible certified applicator, depending on the state) has to be attached to that business and passes the exams. Technicians who do the spraying usually register under that person.</p>
<p>That&rsquo;s why the experience rule matters most. You can form the company on day one, but in most states it can&rsquo;t work until someone with enough documented field time has passed the exams and is named on the license.</p>
<p>The federal baseline sits underneath: under EPA&rsquo;s certification rule, anyone who uses or supervises restricted-use pesticides must be a certified applicator under a state plan (<a href="https://www.ecfr.gov/current/title-40/chapter-I/subchapter-E/part-171" rel="noopener" target="_blank">40 CFR Part 171</a>). The states below go further and cover general-use structural work too.</p></div></section>
<section class="sec alt" id="calc"><div class="w"><h2>State fees, added up</h2><p class="sub">Pick a state to see its listed government fees for one location and one qualifying person in one category. Insurance, bonds, courses and testing-vendor fees aren&rsquo;t included.</p>
<div class="calc"><form class="cin" onsubmit="return false" aria-label="State"><label for="lst">State</label><select id="lst">{opts}</select><p class="hint">Fees as listed by each agency, checked {CHK}.</p></form>
<div><div class="res" id="lout" aria-live="polite"></div></div></div>
<noscript><p>Fees for each state are listed in the table below.</p></noscript></div></section>
<script>(function(){{var D={cdata};var s=document.getElementById('lst'),o=document.getElementById('lout');function m(n){{return '$'+n.toLocaleString('en-US')}}function e(t){{var d=document.createElement('div');d.textContent=t;return d.innerHTML}}function u(){{var v=D[s.value],t=0,h='';v.f.forEach(function(x){{t+=x[1];h+='<div class="row"><div><div class="nm">'+e(x[0])+'</div></div><div class="amt">'+m(x[1])+'</div></div>'}});h='<div class="row best"><div><div class="nm">Listed state fees for '+e(s.value)+'</div><div class="pl">'+(v.f.length?'Business plus one qualifying person, one category':'No flat amount published on the pages we checked')+'</div></div><div class="amt">'+(v.f.length?m(t):'See note')+'</div></div>'+h;if(v.n)h+='<div class="row"><div><div class="pl">'+e(v.n)+'</div></div></div>';h+='<div class="row"><div><div class="nm">Insurance minimum</div><div class="pl">'+e(v.i)+'</div></div></div>';o.innerHTML=h}}s.addEventListener('change',u);u()}})();</script>
<section class="sec" id="table"><div class="w"><h2>Requirements in 12 states</h2><p class="sub">Structural (household and commercial building) pest control, summarized from each agency&rsquo;s own pages and rules. Jump to: {jump}</p>
<div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr))">{rows}</div>
<div class="note w2"><b>Summary only.</b> Condensed from official pages as of {CHK}. Termite, fumigation, lawn and ornamental, and wildlife work often have their own categories and rules, and cities or counties may want a separate business license. For states not listed, start with the <a href="https://npic.orst.edu/reg/state_agencies.html" rel="noopener" target="_blank">NPIC directory of state pesticide regulatory agencies</a>.</div></div></section>
<section class="sec alt" id="checklist"><div class="w nw"><h2>Free printable licensing checklist</h2><p class="sub">Work through it with your state&rsquo;s row open.</p>
<p class="noprint"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button></p>
<div class="form"><h3>Pest control business licensing checklist</h3><table>{form}</table></div>
<p style="font-size:13px;color:var(--mute)">Checklist by Orvian Market. Free to copy and use. Not legal advice; your state&rsquo;s rules are what count.</p></div></section>
<section class="sec" id="software"><div class="w nw"><h2>After you&rsquo;re licensed: records and software</h2><p>Once you&rsquo;re working, every state on this list also expects application records, usually kept 2 or 3 years. Our <a href="pesticide-application-records-by-state.html">pesticide records guide</a> has each state&rsquo;s retention rule and a free printable log. When paper stops scaling, compare <a href="best-pest-control-software.html">pest control software</a> on published prices, or <a href="pest-control-software-pricing-calculator.html">price your own shop</a>. Among tools that publish prices, GorillaDesk lists chemical-use tracking on its $49/mo Basic plan.</p></div></section>
<section class="sec alt" id="faq"><div class="w nw"><h2>FAQ</h2>{faq_block(faq)}</div></section>'''
    return slug, page(slug,title,desc,body,[art_ld(title,desc,slug),faq_ld(faq),crumbs("Pest control license by state",slug)])

def about_page():
    slug="about.html"; title="How Orvian Market Software Guides Compares Software"; desc="Method, sources and affiliate disclosure for Orvian Market Software Guides."
    body = hero("About these guides","How we compare software","The same plain rules apply to every guide on this site.",[f"Last updated {CHK}"])
    body += f'''<section class="sec"><div class="w nw"><h2>Method</h2>{METHOD}
<h3>What we use</h3><p>Each vendor&rsquo;s own public pricing page, product pages and documentation, plus official government sources for compliance topics. Every claim links to its source. When a vendor doesn&rsquo;t publish a price, we say &ldquo;quote only&rdquo; rather than repeat third-party estimates.</p>
<h3>What we don&rsquo;t do</h3><p>We don&rsquo;t claim hands-on testing we haven&rsquo;t done, publish star ratings or invented scores, or write fake reviews. If we ever test a product hands-on, the page will say what we did and when.</p>
<h3 id="disclosure">Affiliate disclosure</h3><p><b>None of our guides contain affiliate links today.</b> In the future we may join vendors&rsquo; affiliate or partner programs, which pay us a commission if you buy through our link, at no extra cost to you. If we do, every affiliate link will be labeled, this notice will name the programs, and rankings won&rsquo;t depend on commissions. Vendors can&rsquo;t pay to be listed or ranked.</p>
<h3 id="privacy">Privacy</h3><p>We use Google Analytics 4 to count page views and clicks on outbound buy links. It sets first-party cookies. We don&rsquo;t run ads, don&rsquo;t sell personal data, and the pricing calculator runs entirely in your browser. Full details in our <a href="https://orvianmarketplace.com/privacy.html">privacy note</a>.</p>
<h3>Corrections</h3><p>Spotted an outdated price? Every page shows the date we checked, and vendors change prices often, so the vendor&rsquo;s own page is always the final word.</p></div></section>'''
    return slug, page(slug,title,desc,body,[crumbs("How we compare",slug)])

def index_page():
    slug="index.html"; title="Software Guides for Pest Control and Hood Cleaning Businesses | Orvian Market"
    desc=f"Honest, dated software comparisons for small field-service businesses: pest control software, a pricing calculator, state license and pesticide record rules, and hood cleaning guides. Checked {CHK}."
    hubs=[("Pest control","best-pest-control-software.html","Best pest control software for small operators (2026)","GorillaDesk, Pocomos, Jobber, Housecall Pro, QuoteIQ, PestPac, FieldRoutes and Briostack, compared on public pricing."),
          ("Free tool","pest-control-software-pricing-calculator.html","Pest control software pricing calculator","Enter your routes, users and customers to see five vendors&rsquo; list prices side by side."),
          ("Free guide","pesticide-application-records-by-state.html","Pesticide application records by state","Retention periods and required fields for 12 states, with official sources and a printable log."),
          ("Free guide","pest-control-license-requirements-by-state.html","Pest control license requirements by state","Business licenses, who must qualify them, experience, insurance minimums and state fees for 12 states."),
          ("Hood cleaning","best-hood-cleaning-software.html","Best hood cleaning software (2026)","Seven NFPA 96 report and business apps, free plans included."),
          ("Free guide","hood-cleaning-frequency-requirements.html","How often must a kitchen hood be cleaned?","The NFPA 96 and fire code schedule, grease depth limits, tag rules, a next-service calculator and a printable record."),
          ("Startup guide","how-to-start-a-hood-cleaning-business.html","How to start a hood cleaning business","License examples, certification costs, insurance, wastewater and roof rules, pricing benchmarks and a printable checklist.")]
    hb="".join(f'<a class="hub" href="{h}"><span class="k">{k}</span><h3>{E(t)}</h3><p>{d}</p></a>' for k,h,t,d in hubs)
    body = hero("Orvian Market &middot; Software Guides","Software guides for pest control and hood cleaning businesses","Honest, dated comparisons built from vendors&rsquo; public pricing and docs. No sponsored rankings, no fake reviews, and every number links to its source.",[f"Checked {CHK}","Sources on every row","Free tools"])
    body += f'<section class="sec"><div class="w"><h2>Guides</h2><p class="sub">Start with your trade.</p><div class="hubs">{hb}</div></div></section><section class="sec alt"><div class="w"><h2>How we compare</h2>{METHOD}<p style="margin-top:16px"><a href="about.html">Read the full method and disclosure &rarr;</a></p></div></section>'
    return slug, page(slug,title,desc,body,[{"@context":"https://schema.org","@type":"CollectionPage","name":title,"url":BASE,"description":desc}])

pages=[index_page(),best_page(),calc_page(),records_page(),lic_page(),hood_page(),hood_freq_page(),start_page(),about_page()]
# GA4 tag (G-F3QH6E9QR7) + buy_click listener, from ga.py (next to this file in the repo, or /workspace/money-lab/brand/site)
import sys as _sys
_sys.path[:0]=[os.path.dirname(os.path.abspath(__file__)),"/workspace/money-lab/brand/site"]
from ga import add_ga
for s,h in pages: open("out/"+s,"w").write(add_ga(h))
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}{"" if s=="index.html" else s}</loc><lastmod>{CHK_ISO}</lastmod></url>\n' for s,_ in pages)+'</urlset>\n'
open("out/sitemap.xml","w").write(sm)
print("built",[s for s,_ in pages])
