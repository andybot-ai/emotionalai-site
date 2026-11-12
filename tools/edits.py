import re
LI='https://www.linkedin.com/company/emotionalai'
# contact
p='content/pages/contact.md'; s=open(p).read()
s=re.sub(r'For all enquiries.*', f'For all enquiries please contact Prof. Andrew McStay at [mcstay@bangor.ac.uk](mailto:mcstay@bangor.ac.uk).\n\nFor news from the Lab, follow us on [LinkedIn]({LI}).', s)
open(p,'w').write(s)
# companies page
p='content/pages/useful-links.md'; s=open(p).read()
s=re.sub(r'Please suggest more by tweeting to \[@EmotionalAI\]\([^)]*\)', f'Please suggest more via [LinkedIn]({LI})', s)
open(p,'w').write(s)
# personal data stores -> governing
p='content/projects/personal-data-stores.md'; s=open(p).read()
s=s.replace('group: "sensing"','group: "governing"').replace('weight: 3','weight: 4'); open(p,'w').write(s)
# funders
p='data/home.yaml'; s=open(p).read()
s=re.sub(r'# Confirmed from the existing site\..*\n','',s)
s=s.replace('"JST", "HDI Network"]','"JST", "HDI Network", "Office of the Privacy Commissioner of Canada"]')
open(p,'w').write(s)
# homepage team: centred, link below and larger
p='layouts/index.html'; s=open(p).read()
s=s.replace('<div class="sec-head"><h2>Team</h2><a class="mono" href="/team">Team and collaborators →</a></div>\n  <div class="team">','<div class="sec-head"><h2>Team</h2></div>\n  <div class="team">')
s=s.replace('''{{ end }}
  </div>
</div></section>

<section class="funders">''','''{{ end }}
  </div>
  <p class="team-more"><a href="/team">Team and collaborators →</a></p>
</div></section>

<section class="funders">''')
open(p,'w').write(s)
# footer: LinkedIn
p='layouts/partials/footer.html'; s=open(p).read()
if 'linkedin' not in s: s=s.replace('<a href="/news/index.xml">RSS</a>',f'<a href="{LI}">LinkedIn</a><a href="/news/index.xml">RSS</a>')
open(p,'w').write(s)
# css
p='static/css/site.css'; s=open(p).read()
s=s.replace('.team{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px}','.team{display:flex;flex-wrap:wrap;justify-content:center;gap:48px 80px}\n.team .person{align-items:center;text-align:center;width:180px}\n.team .av{width:150px}\n.team-more{text-align:center;margin:44px 0 0;font-size:21px;font-weight:600}\n.team-more a{text-decoration:none;border-bottom:2px solid var(--ink);padding-bottom:4px}')
open(p,'w').write(s)
print('done')
