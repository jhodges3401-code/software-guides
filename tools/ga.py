"""GA4 tag for every page served on orvianmarketplace.com (added 2026-10-17 9:30 PM ET).
Usage as module: from ga import add_ga; html = add_ga(html)
Usage as CLI:    python3 ga.py FILE_OR_DIR ...   (idempotent; skips files that already have the ID)
Do NOT add to buyer templates or the open-source *-lite repos (forks would carry our ID)."""
import sys, os, re
GA_ID = "G-F3QH6E9QR7"
# Gumroad slug -> product name for the buy_click event
NAMES = {"answerloft":"Answerloft","bcmhvk":"Okayline","bjkyj":"Thumbtally","ekunvc":"Proposeroo Team",
 "ijsmuq":"PeelPixel Pro","kzjcwp":"Proposeroo Pro","lyrgdx":"Rate Calculator Spreadsheet","pckinc":"Rate-Raise Email Rewrite",
 "kudoshelf":"Kudoshelf","proposeroo-desk":"Proposeroo Desk","proposeroo-desk-team":"Proposeroo Desk Team",
 "ctitql":"Freelance Rate Pack","jtocar":"Client OS","vwxgu":"Prompt Pack","oellyq":"Budget Template",
 "bffum":"Rate Mini (free)","mceana":"Freelancer Toolkit Bundle","nqpwfg":"Raise Emails (free)"}
_map = ",".join(f'"{k}":"{v}"' for k, v in NAMES.items())
SNIPPET = (
 '<!-- Google tag (gtag.js) -->\n'
 f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
 '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
 f"gtag('js',new Date());gtag('config','{GA_ID}');\n"
 "document.addEventListener('click',function(e){var a=e.target&&e.target.closest?e.target.closest('a[href*=\"gumroad.com\"]'):null;if(!a)return;"
 "var m=a.href.match(/\\/l\\/([^\\/?#]+)/),s=m?m[1]:'';var N={" + _map + "};"
 "gtag('event','buy_click',{product_name:a.getAttribute('data-product')||N[s]||s||'gumroad',product_slug:s,link_url:a.href,link_text:(a.textContent||'').trim().slice(0,80),transport_type:'beacon'});},true);</script>\n")

def add_ga(html):
    if GA_ID in html:
        return html
    m = re.search(r'<head[^>]*>', html, re.I)
    if not m:
        return html
    # place right after <meta charset> if it directly follows <head>, else right after <head>
    c = re.match(r'\s*<meta charset=[^>]*>', html[m.end():], re.I)
    pos = m.end() + (c.end() if c else 0)
    return html[:pos] + "\n" + SNIPPET + html[pos:].lstrip("\n")

def run(paths, skip=("google0eb8f0c0b48344a8.html",)):
    n = 0
    for p in paths:
        files = [p] if os.path.isfile(p) else [os.path.join(d, f) for d, _, fs in os.walk(p) if "/.git" not in d and "node_modules" not in d for f in fs if f.endswith(".html")]
        for f in files:
            if os.path.basename(f) in skip: continue
            s = open(f, encoding="utf-8").read(); t = add_ga(s)
            if t != s:
                open(f, "w", encoding="utf-8").write(t); n += 1; print("tagged", f)
    return n

if __name__ == "__main__":
    print(run(sys.argv[1:]), "files tagged")
