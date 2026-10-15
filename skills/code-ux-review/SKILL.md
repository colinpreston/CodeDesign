---
name: code-ux-review
description: Run a Code-format UX review of a website or journey using Code's Persuasion Model, with a Core Web Vitals and PageSpeed check and an accessibility check across design, content and screen readers, and always build the result as a Code-branded slide deck. Use when Colin asks for a UX review, UX audit, site review, expert review, CRO audit or "flags" on a site.
---

# Code UX Review

This is how Code reviews a site: walk a real customer journey page by page and judge each page against **Code's Persuasion Model**. Then add the evidence a client can't argue with:
- **Core Web Vitals and PageSpeed**, from real Chrome users and a lab test;
- **an accessibility check** in three parts: design, content and screen readers.

**The deliverable is always a deck.** The review isn't finished until the deck exists, so never stop at a list of findings in chat. The deck follows the shape of Code's past reviews (Direct Line, Bayer CropScience, James Wellbeloved):
- the persuasion model up front;
- an executive summary and a priority list;
- per page, annotated screenshots with (+)/(−) callouts tagged by stage, plus a scores slide;
- a Now / Next / Future summary per stage.

## The foundation: Code's Persuasion Model

To convert, a page has to do four things, in order. Each one gates the next, so a page that fails Usability can't be rescued by great Emotion.

| Stage | The user thinks | The question to ask |
|---|---|---|
| **1. Usability** | "I can do X" | Can the user interact with and navigate the site effectively? Remove physical barriers to taking action. |
| **2. Trust** | "It's OK to do X" | Is the site building enough trust, through brand, UI, content and third-party proof, for the user to go ahead? |
| **3. Emotion** | "I want to do X" | Does the site make the user *want* to complete the task? Do imagery and copy work together and stay consistent? |
| **4. Trigger** | "I will do X" | Is the user nudged at the right moment? Is the call to action clear, well placed and not competing with other elements? |

Older Code decks label stage 4 "Persuasion" or "Persuasion trigger". Use **Trigger** and say it means the same thing.

Every finding is tagged to one stage. Performance and accessibility findings are **Usability** findings unless they clearly hit trust, for example a broken layout that looks unprofessional. The full model, with its techniques (contrast, serial position, limited choice, affect heuristic, story, social proof), is in `code-design-playbook` module 8. Read it if it isn't already loaded.

**Explain the psychology first.** Whenever a finding or recommendation leans on a bias or effect, state what the effect means in plain words before saying what to do about it.

## Step 1: Scope it

Ask only what you can't infer, one question at a time:
- **Site and journey.** Which URL, and which journey? Write it as a scenario in Code's format: *"As a [user] who wants to [goal], I want to [task], so that [outcome]."* Never review pages in isolation; each page is judged by its role in the journey.
- **Pages.** 5–10 pages along that journey is typical. Bayer covered 12 page types; Direct Line covered a quote journey end to end.
- **Audience.** Who uses the site, especially older users, disabled users, or people under stress. This sets how hard the accessibility check bites.
- **Where it's going.** An internal flag list, a pitch deck, or a full client review. A pitch gets fewer, sharper findings; a full review gets every page.
- **Analytics.** Is there access? If not, say plainly that findings show *where* the journey breaks, not *how many* people it loses.

If a company brain exists for the client (`design-studio-team-setup`), read the Project Brain and the Research Repository first, and log what you produce back into them.

## Step 2: Walk the journey (the persuasion review)

Use the browser (Claude in Chrome or the built-in browser), one page at a time, desktop first, then mobile.

For each page:
1. **Screenshot it.** Take the full page in viewport-height sections, saved to disk; these become the annotated slides.
2. **Find 4–8 findings.** Each one is:
   - **(+) or (−)**: good things matter; the client needs to know what to keep.
   - **the stage** it belongs to;
   - **one or two sentences**: what you saw, why it matters to the user, and the fix.

   Write it like the house examples:
   - *"(−) Usability / Background and foreground colours do not have a sufficient contrast ratio for accessibility."*
   - *"(+) Trust / Third-party trust badges show potential customers that the business is credible."*
   - *"(−) Trigger / Missed opportunity to end the page with a call to action to download the app."*
3. **Record where each callout points.** In the same scroll position as the screenshot, read the element's centre so the deck can draw a line to it exactly. Run `(()=>{const r=document.querySelector('<selector>').getBoundingClientRect();return [Math.round(r.x+r.width/2),Math.round(r.y+r.height/2),innerWidth,innerHeight]})()`, or use `find` and read the element's position from a screenshot. Store the point with the screenshot's file name and pixel size.
4. **Count and measure, don't estimate.** Read the DOM for:
   - call-to-action counts;
   - form fields (type, required, labels, autocomplete);
   - link labels and repeated terms.

   A number you counted beats an adjective.
5. **Never submit forms or create accounts.** Stop at the point of commitment and say what you couldn't see after it, such as the confirmation page or follow-up emails.

**Mobile.** Claude in Chrome often won't resize below about 1,390px wide. If it won't go narrower, use the PageSpeed mobile screenshots and filmstrip for layout evidence, and mark mobile layout as "not hands-on tested" rather than guessing.

## Step 3: Core Web Vitals and PageSpeed

**How to run it.**
- Open `https://pagespeed.web.dev/analysis?url=<encoded URL>&form_factor=mobile` in the browser and wait about 40 seconds for the report. Repeat with `form_factor=desktop`.
- The keyless API (`googleapis.com/pagespeedonline/v5`) is often over Google's shared daily quota, and the cloud shell and web fetcher can't reach it. Use the website.
- Test the journey's key pages, at least the landing page, a product page and the form.

**Extract the numbers.** `get_page_text` returns mostly CSS. Run this in the report tab instead:

```js
const vis=e=>e&&e.offsetParent!==null, T=e=>(e?.textContent||'').trim().replace(/\s+/g,' ');
const body=document.body.innerText, i=body.indexOf('Core Web Vitals Assessment');
const rep=[...document.querySelectorAll('.lh-report,.lh-root')].find(vis)||document;
const bad=c=>{const x=rep.querySelector('.lh-category#'+c);return x?[...new Set([...x.querySelectorAll('.lh-audit--fail,.lh-audit--average')].map(a=>T(a.querySelector('.lh-audit__title'))+(T(a.querySelector('.lh-audit__display-text'))?' — '+T(a.querySelector('.lh-audit__display-text')):'')))]:[]};
JSON.stringify({field:i>=0?body.slice(i,i+600).replace(/\n+/g,' | '):'no field data',
 scores:[...rep.querySelectorAll('.lh-scores-header .lh-gauge__wrapper')].filter(vis).map(g=>T(g.querySelector('.lh-gauge__label'))+': '+T(g.querySelector('.lh-gauge__percentage'))),
 lab:[...rep.querySelectorAll('.lh-metric')].filter(vis).map(m=>T(m.querySelector('.lh-metric__title'))+' = '+T(m.querySelector('.lh-metric__value'))),
 perf:bad('performance').slice(0,12), a11y:bad('accessibility'), bp:bad('best-practices'), seo:bad('seo')})
```

**Record two kinds of data, and never mix them up.**
- **Field data (Core Web Vitals)** comes from real Chrome users over the last 28 days, at the 75th percentile, which means 3 in 4 visits were at least this good. Record pass or fail and each metric against Google's thresholds:

  | Metric | Good | Poor |
  |---|---|---|
  | **LCP** (main content appears) | ≤ 2.5s | > 4s |
  | **INP** (page responds to taps) | ≤ 200ms | > 500ms |
  | **CLS** (layout jumps around) | ≤ 0.1 | > 0.25 |

  Also note FCP and TTFB, and whether the data is for **this URL** or falls back to the **whole site (origin)**. No field data means a low-traffic page; say so.
- **Lab data (Lighthouse)** is one simulated mobile visit on a throttled connection. Record the four category scores (Performance, Accessibility, Best Practices, SEO), the lab metrics (FCP, LCP, TBT, CLS, Speed Index) and the top opportunities with their estimated savings. Lab scores vary from run to run; date-stamp them and treat them as indicative.

**Explain it in plain English and tie it to the user**, for example:
- *"On phones, the page jumps around as it loads (CLS 0.26, poor). That's a Usability problem: people tap the wrong thing."*
- *"The page takes 5.5 seconds to look complete on a mid-range phone."*

Name the likely cause from the opportunities, such as images without set sizes, unused JavaScript or oversized video. Hand the fix to the Engineering Principal desk if one exists.

## Step 4: Accessibility, in three lenses

**An automated score is not a pass.** Lighthouse's accessibility score runs a subset of automated rules. It can't judge text on gradients or images, reading level, alt-text quality, focus order or how a page sounds in a screen reader. On one site reviewed in October 2026, for example, Lighthouse scored accessibility 100 while white text on the main gold gradient button measured 2.1–3.5:1, against a 4.5:1 minimum. Always run all three lenses below. Measure against **WCAG 2.2 AA** and cite criterion numbers.

### Design lens
- **Contrast:** text at 4.5:1; large text (24px+, or 18.66px+ bold) and interface parts at 3:1 (1.4.3, 1.4.11). Check text over gradients and images by hand, at the lightest point.
- **Target size:** at least 24×24px (2.5.8); 44×44px is the comfortable target for older or less steady hands.
- **Colour alone** never carries meaning, for example errors, required fields or sale prices (1.4.1).
- **Focus** is visible on every control (2.4.7) and not hidden under sticky headers (2.4.11).
- **Text and zoom:** 200% zoom and 320px reflow without loss (1.4.4, 1.4.10); body text size and line spacing.
- **Motion:** autoplaying video or carousels can be paused (2.2.2), and `prefers-reduced-motion` is respected.

### Content lens
- **Reading level:** aim for a reading age of about 9–11 (Flesch Reading Ease 60+) for a general public audience, lower for vulnerable users. Flag long sentences, jargon and walls of text.
- **Link and button text** says where it goes or what it does. Flag "Find out more", "Click here" and "Read more" (2.4.4).
- **Headings** describe their section, and **one name per thing**: the same service shouldn't be called four different names.
- **Alt text** says what the image is *for*, and decorative images use `alt=""` (1.1.1).
- **Errors and instructions** say what went wrong and how to fix it (3.3.1, 3.3.3). Required fields are marked in text, not just with a colour or an asterisk.

### Screen reader lens
Use `read_page` (the browser's real accessibility tree) as the stand-in for what a screen reader announces, then check:
- the **page title** and `lang`;
- **landmarks**: header, nav, main and footer;
- the **heading outline**: one H1 and no skipped levels;
- **names** on every link, button and icon;
- **form labels**, required state and error announcements;
- **image alternatives**;
- **reading order** matching the visual order;
- **dynamic changes**, such as added errors or basket updates, being announced (`aria-live`).

Then tab through the key journey: Is there a skip link? Is the focus order logical? Are there any keyboard traps?

Say plainly that this approximates a screen reader. A real test with NVDA and VoiceOver, ideally with disabled users, is needed before anyone claims compliance.

**Quick page scan.** Run this on each page for the numbers; it complements `read_page` and doesn't replace it:

```js
(()=>{const T=e=>(e?.textContent||'').trim().replace(/\s+/g,' '),shown=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
const nm=e=>(e.getAttribute('aria-label')||'').trim()||T(e)||(e.querySelector('img[alt]')?.alt||'').trim()||(e.getAttribute('title')||'').trim();
const rgb=s=>(s.match(/[\d.]+/g)||[]).map(Number),lum=c=>c.slice(0,3).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4}).reduce((a,v,i)=>a+v*[0.2126,0.7152,0.0722][i],0),ratio=(a,b)=>{const x=lum(a),y=lum(b);return(Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)};
// gradient: sample the visible colour at 0/25/50/75/100% of the box, honouring stop positions (stops past 100% never show)
const gs=s=>{const m=s.match(/(?:repeating-)?(?:linear|radial|conic)-gradient\((.*)\)/);if(!m)return null;let d=0,cur='',parts=[];for(const ch of m[1]){if(ch==='(')d++;if(ch===')')d--;if(ch===','&&d===0){parts.push(cur.trim());cur=''}else cur+=ch}parts.push(cur.trim());
const st=parts.map(p=>{const c=p.match(/rgba?\([^)]+\)/);if(!c)return null;const v=c[0].match(/[\d.]+/g).map(Number),pc=p.replace(c[0],'').match(/(-?[\d.]+)%/);return{c:v,p:pc?+pc[1]/100:null}}).filter(x=>x&&(x.c[3]===undefined||x.c[3]>0.5));
if(!st.length)return null;st.forEach((x,i)=>{if(x.p===null)x.p=st.length===1?0:i/(st.length-1)});
const at=t=>{if(t<=st[0].p)return st[0].c;for(let i=1;i<st.length;i++){if(t<=st[i].p){const a=st[i-1],b=st[i],k=(t-a.p)/((b.p-a.p)||1);return a.c.slice(0,3).map((v,j)=>v+(b.c[j]-v)*k)}}return st[st.length-1].c};return[0,.25,.5,.75,1].map(at)};
const split=v=>{let d=0,cur='',out=[];for(const ch of v){if(ch==='(')d++;if(ch===')')d--;if(ch===','&&d===0){out.push(cur.trim());cur=''}else cur+=ch}out.push(cur.trim());return out};
// skip thin layers (underline/border tricks): a layer only counts as background if it covers at least half the element's height
const bg=e=>{for(let n=e;n;n=n.parentElement){const s=getComputedStyle(n);if(s.backgroundImage!=='none'){const L=split(s.backgroundImage),S=split(s.backgroundSize),h=n.getBoundingClientRect().height;let img=0;for(let i=0;i<L.length;i++){const z=(S[i%S.length]||'auto').split(/\s+/),hv=z[1]||z[0];if(/px$/.test(hv)&&parseFloat(hv)<h*0.5)continue;if(/%$/.test(hv)&&parseFloat(hv)<50)continue;if(/url\(/.test(L[i])){img=1;break}const g=gs(L[i]);if(g)return{grad:1,c:g}}if(img)return{grad:0,c:[]}}const c=rgb(s.backgroundColor);if(c.length&&(c[3]===undefined||c[3]>0.5))return{grad:0,c:[c]}}return{grad:0,c:[[255,255,255]]}};
const ctl=[...document.querySelectorAll('a[href],button,[role=button]')].filter(shown),fail=[],partly=[],onImage=[];
for(const e of [...document.querySelectorAll('a,button,p,h1,h2,h3,li,span,label')].filter(shown)){if(!T(e)||[...e.children].some(c=>T(c)===T(e)))continue;const cs=getComputedStyle(e),fs=parseFloat(cs.fontSize),need=(fs>=24||(fs>=18.66&&+cs.fontWeight>=700))?3:4.5,b=bg(e),t=T(e).slice(0,30);if(!b.c.length){onImage.push(t);continue}
const r=b.c.map(c=>ratio(rgb(cs.color),c)),lo=Math.min(...r),hi=Math.max(...r),lab=t+' '+(b.grad?lo.toFixed(1)+'–'+hi.toFixed(1):lo.toFixed(1))+':1 (needs '+need+')'+(b.grad?' gradient':'');if(hi<need)fail.push(lab);else if(lo<need)partly.push(lab)}
const prose=(document.querySelector('main')||document.body).innerText.split(/\n+/).map(t=>t.trim()).filter(t=>t.split(/\s+/).length>=8&&/[a-z]/.test(t)),words=prose.join(' ').split(/\s+/).filter(Boolean),sents=Math.max(1,prose.reduce((a,t)=>a+Math.max(1,(t.match(/[.!?]+(\s|$)/g)||[]).length),0)),syl=words.reduce((a,w)=>a+Math.max(1,(w.toLowerCase().replace(/[^a-z]/g,'').match(/[aeiouy]+/g)||[]).length),0);
return JSON.stringify({title:document.title,lang:document.documentElement.lang||'MISSING',landmarks:['header','nav','main','footer'].map(s=>s+':'+document.querySelectorAll(s+',[role='+({header:'banner',nav:'navigation',main:'main',footer:'contentinfo'})[s]+']').length).join(' '),
headings:[...document.querySelectorAll('h1,h2,h3,h4')].filter(shown).map(h=>h.tagName+' '+T(h).slice(0,50)),unnamed:ctl.filter(e=>!nm(e)).length,
vagueLinks:[...new Set(ctl.map(nm).filter(n=>/^(read more|more|click here|here|find out more|learn more|see more|view)$/i.test(n)))],imgsNoAlt:[...document.querySelectorAll('img')].filter(i=>shown(i)&&!i.hasAttribute('alt')).length,
smallTargets:ctl.filter(e=>{const r=e.getBoundingClientRect();return r.width<24||r.height<24}).length,contrastFail:[...new Set(fail)].slice(0,15),contrastPartlyLow:[...new Set(partly)].slice(0,10),textOnImageCheckByEye:[...new Set(onImage)].slice(0,10),
fleschEase:words.length?Math.round(206.835-1.015*(words.length/sents)-84.6*(syl/words.length)):'no prose',proseWords:words.length,autoplayVideo:document.querySelectorAll('video[autoplay]').length})})()
```

How to read the scan's output:
- **`contrastFail`** means the text fails across its whole background: solid colour, or every visible part of a gradient.
- **`contrastPartlyLow`** means the text fails over part of a gradient. Zoom into the screenshot to see whether the text actually sits over the weak part.
- **`textOnImageCheckByEye`** lists text sitting on photos, which no script can measure. Check each one by eye.
- **`fleschEase`** scores only prose lines of 8 words or more, so treat it as a rough guide on English text: 60+ is plain English, 30–50 is hard going.

## Step 5: Synthesise

- **Executive summary:** 3–5 short paragraphs, biggest issue first, in plain language a client director would read.
- **Priority of recommendations:** a numbered list, ordered by impact on the journey's goal and how early in the model each one fails (a Usability blocker outranks an Emotion polish).
- **Now / Next / Future per stage:** Usability, Trust, Emotion, Trigger, each with what to do now (quick wins), next (needs design or dev), and future (bigger change or research).
- **Make it testable.** For the top recommendations, write Code's test hypothesis: *"Because we have observed (finding), we believe that (change) will result in (effect), confirmed when (measure)."*
- **Name the gaps:** no analytics, mobile untested, forms not submitted, screen reader approximated. These become the research and next steps slide.
- **No dark patterns.** Persuasion recommendations must serve the user, not trick them: no fake urgency, pre-ticked consent or hidden costs.

## Step 6: Build the deck (always)

**Every run ends in a deck.** If time is short, cut pages, not the deck.
- **Default:** a **Slides** artifact. Run Artifact `quickstart` with intent `slides`, or create from the Slides type when its link is known. Follow the type's own instructions for files and publishing.
- **PowerPoint:** only when Colin asks for a .pptx. Then use the pptx skill and the same structure and recipes.
- **Never invent content to fill the deck.** Missing facts become bracketed placeholders, listed in your reply.

**Brand.** Use `code-brand-style`, and pick one colour per stage so callouts read at a glance. Every colour below passes contrast on white:

| Token | Hex |
|---|---|
| Navy (text, dark backgrounds) | `#000050` |
| Body text | `#2A2F6E` |
| Page | `#FBFBFE` |
| Card | `#E8EBFF` |
| Lime (accent fill) | `#B0F467` |
| Cornflower (eyebrows) | `#3F4FE0` |
| Font | **Poppins**, as the stand-in for WPP's own face |
| **Usability** | `#2F6B00` |
| **Trust** | `#000050` |
| **Emotion** | `#3F4FE0` |
| **Trigger** | `#00707D` |
| Good | `#188038` |
| Needs work | `#B85C00` |
| Poor | `#B3261E` |

Every slide gets the footer band: page number and source on the left, "Code Computerlove" on the right, 24px, pinned at `bottom:64px`, with the slide padded `128px 128px 160px`.

**Upload first.** Upload every screenshot as an asset before writing slides, and use the `/_blob/…` URL it returns.

**Deck order:**
1. Cover
2. Approach
3. Persuasion Model
4. Executive summary
5. Priority list
6. Scores at a glance
7. For each page: a divider, 1–2 annotated slides and a scores slide
8. Accessibility: design, content and screen reader
9. Summary for each stage: Now / Next / Future
10. Next steps and research

**These recipes are tested in the Slides format.** Reuse their markup and change only the content and numbers.

**Persuasion Model slide.** Draw four stacked, narrowing bars as a funnel standing in for the triangle. Put the "I can / It's OK / I want / I will" rows beside them.
```html
<div style="width:760px;display:flex;flex-direction:column;align-items:center;gap:14px">
<div style="width:720px;background:#B0F467;border-radius:14px;padding:34px 24px"><p style="font-size:36px;font-weight:700;text-align:center;color:#000050">1. Usability</p></div>
<div style="width:580px;background:#000050;border-radius:14px;padding:34px 24px"><p style="font-size:36px;font-weight:700;text-align:center;color:#FBFBFE">2. Trust</p></div>
<div style="width:440px;background:#3F4FE0;border-radius:14px;padding:34px 24px"><p style="font-size:36px;font-weight:700;text-align:center;color:#FBFBFE">3. Emotion</p></div>
<div style="width:300px;background:#00DBEE;border-radius:14px;padding:34px 24px"><p style="font-size:36px;font-weight:700;text-align:center;color:#000050">4. Trigger</p></div>
</div>
```

**Annotated screenshot slide.** This is the heart of the deck.
- **Layout:** title pinned at top 72; screenshot pinned in the centre; up to 3 callouts on each side; one connector from each callout to its element.
- **Screenshot:** a 1440×757 shot fits at `left:548px;top:260px;width:824px;height:433px;object-fit:contain`, which is a scale of 0.5722.
- **Callout tops:** 190, 440 and 690.
  - Left column: `left:128px;width:340px`.
  - Right column: `left:1412px;width:340px`.
- **Callout length:** 18 words or fewer, so three fit one column.
```html
<div style="position:absolute;left:128px;top:190px;width:340px;display:flex;flex-direction:column;gap:6px;background:#FFFFFF;border:3px solid #2F6B00;border-radius:14px;padding:18px 20px">
<p style="font-size:24px;font-weight:700;color:#2F6B00">(−) Usability</p>
<p style="font-size:24px;line-height:1.3;color:#000050">White on gold measures 2.1–3.5:1, under the 4.5:1 minimum (WCAG 1.4.3).</p>
</div>
<x-connector x1="520" y1="230" x2="700" y2="558" head="end" style="color:#2F6B00;border-width:3px"></x-connector>
```

**Connector maths.**
- Start each line at the callout's inner edge, 40px below the callout's top:
  - left callouts start at `x1=520`;
  - right callouts start at `x1=1404`.
- End it on the element. For a point `(X, Y)` on a screenshot of width `W`, height `H`, placed in a box at `(L, T)` sized `BW×BH` with `contain`:
  - `s = min(BW/W, BH/H)`
  - `x2 = L + (BW − W·s)/2 + X·s`
  - `y2 = T + (BH − H·s)/2 + Y·s`
- Put all connectors after the callouts, as direct children of the section, and keep within 24 pinned children per slide.
- The stage colour carries the meaning, so the (+)/(−) and stage name must also be written in the callout. Never rely on colour alone.

**Score ring** (Lighthouse category, 0–100).
- Circumference at `r=76` is 477.5, so the dash is `score/100 × 477.5`.
- Colour by band: 0–49 Poor `#B3261E`, 50–89 Needs work `#B85C00`, 90–100 Good `#188038`.
- Always write the band word underneath, and the number on top as a `<p>`, never as SVG text.
```html
<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:200px">
<div style="position:relative;width:180px;height:180px">
<svg aria-label="Performance score 61 out of 100" width="180" height="180" viewBox="0 0 180 180"><circle cx="90" cy="90" r="76" fill="none" stroke="#E8EBFF" stroke-width="16"/><circle cx="90" cy="90" r="76" fill="none" stroke="#B85C00" stroke-width="16" stroke-linecap="round" stroke-dasharray="291.3 477.5" transform="rotate(-90 90 90)"/></svg>
<p style="position:absolute;left:0px;top:54px;width:180px;text-align:center;font-size:56px;font-weight:700;color:#B85C00">61</p>
</div>
<p style="font-size:26px;font-weight:600;text-align:center">Performance</p>
<p style="font-size:24px;text-align:center;color:#B85C00">Needs work</p>
</div>
```

**Scores slide.**
- **Top row:** a navy Core Web Vitals verdict card ("Passed" or "Failed", "real Chrome users, last 28 days"), then one card each for LCP, INP and CLS. Each shows the value, then "Good", "Needs work" or "Poor (target …)", tinted `#FCE8E6` when poor.
- **Bottom row:** four rings, then a card headed "What's slowing it down" with the top 3 opportunities in plain English.
- **Speaker notes:** the lab metrics, and that lab scores vary between runs.

**Accessibility slide.** Use three equal cards: Design, Content and Screen reader. Start every line with a word: **Fail:**, **Check:**, **Check by eye:**, **Pass:** or **Not yet tested:**. Cite the WCAG number where there is one. The title says it plainly, for example "An automated 100 isn't a pass".

**Stage summary slide.** Put a lime pill with the stage name and the "I can do X" line above the title, then three cards:
- **Now:** navy card with a lime heading, for quick wins.
- **Next:** pale card, for work that needs design or development.
- **Future:** pale card, for bigger change or research.

Make one summary slide per stage.

**Speaker notes on every slide** give the method, date, device and anything not covered.

**After publishing, give Colin:**
- the deck;
- one line on the headline finding;
- the placeholders to fill;
- what wasn't tested.

Don't render or screenshot the deck to check it unless he asks.

## Step 7: Log it and hand it over

- If a company brain exists:
  - log the full findings in the relevant desk's log (UX Designer, CRO, Accessibility or Engineering);
  - add a summary entry to the Research Repository;
  - correct any earlier entry the review disproves.
- Save the raw numbers (PageSpeed extracts, scan results) with the date, so a re-run can show change over time.
- Give Colin the deck with one line on the headline finding and one line on what still needs checking.

## Fences

- **Everything is an internal draft until Colin sends it.** That includes anything going to a client or to another agency.
- **Never submit forms, sign up, buy anything or enter personal data** on the site being reviewed.
- **Never invent a number.** No analytics means no conversion figures; say so.
- **Accessibility findings are observations against WCAG, not legal advice.** Don't call a site "compliant" or "non-compliant" in law.
- **Date-stamp every score.** PageSpeed and Lighthouse change run to run and month to month.
