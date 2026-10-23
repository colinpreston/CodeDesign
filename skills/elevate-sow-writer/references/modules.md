# Elevate SoW: house wording library

Taken from four signed SoWs: Aluvert, Duette EU, Luxaflex Project, Solskjerming NO/SE. Adapt brand, locale names and counts; keep the structure and phrasing. `[ ]` = fill in.

## Feature keys (for `features` / `out_of_scope.in_scope`)

| key | label | key | label |
|---|---|---|---|
| bloomreach | Bloomreach | email_signup | Email sign up |
| taps_sources | Taps and Sources | samples | Samples |
| guid | GUID Site ID | dealer_locator | Dealer / Showroom Locator |
| salsify_pim | Salsify PIM | contact_us | Contact Us form |
| pdp | Product Detail Pages (PDP) | request_appointment | Request an Appointment form |
| pfg | Product Filter Grid (PFG) | request_consultation | Request a Consultation form |
| infinity | Infinity call tracking | request_brochure | Request a Brochure form |
| trustpilot | Trustpilot | request_ebrochure | Request an E-brochure form |
| turnstile | Turnstile | pii_exports | PII Blob storage exports |
| sitespect | Sitespect | blob_storage | Blob storage |
| vis_app | Vis app | live_diary | Live Diary |
| design_tokens | Design token application | discount_codes | Discount codes |
| page_designs | Journey, page designs / wireframes | seo | Any SEO activity |
| image_migration | Image migration | content_migration | Content migrations |

---

## Summary (section 1)
> Code are delighted to present [client] with this statement of work to deliver the [brand / locales] Elevate website build[s] for the following [existing URLs / locales]:

List existing URLs, then "URLs to be used for new site:" if they change (note languages, e.g. "Duette.com/ch – 2 x languages (German and French)").

Add one context sentence: "Following the successful launch of [previous brands], [brand] [is/are] the next [brand/locale] to be added to the Elevate platform. This SoW covers the design and build activities required to deliver [this website / these websites]."

Cost (fixed): "This proposal has been costed at a total of £[X] [as agreed in the Elevate pitch process]. It includes the existing rate card discount resulting in a day rate of £[day rate from the costing sheet]. The work will be delivered on a fixed cost basis meaning that Hunter Douglas will be invoiced against the billing plan included in this document."

POC variant: "…costed at a fixed cost of £[X]… Given this is a POC Code will track actual time and effort against this project to enable refinement of [small brand] build costings in the future."

Close: "If you have any questions on this document, please contact {{contact}}." (the script fills this from the `contact` details the user gives you)

## Project Overview (section 2)
> [Brand/locales] [is/are] the next [brand/locale] to be built on the new Elevate platform, taking in the benefits of using Prismic the SaaS based CMS to enable the Hunter Douglas content editors to manage website content, features and functionality internally.
>
> This removes the reliance on any further intensive development effort once the site is launched. This project will deliver a consistent front-end user experience with consistent features and functionality using existing components from the global component library [design-route clause].

Design-route clauses:
- Reuse: "…and existing [parent brand] design tokens to deliver the brand application across all [n] locales."
- New tokens: "…each with their own set of design tokens to deliver their unique brand look and feel."
- HD-led: "Hunter Douglas has chosen to take responsibility for the design look and feel of the new website but with the agreement that [brand] will use the components which already exist within the global component library."

---

## 3.1.x Design activities
- **Reuse:** "[Parent] design token application will already exist on the Elevate platform so no design token work is needed within the scope of this statement of work. Fonts: [fonts]. It is also anticipated that the [parent] team can support the local teams on which components to use for which pages… Therefore, no design work is required within the scope of this statement of work."
- **New tokens:** "A new set of design tokens will be produced for the brand but these will be in keeping with the already agreed design token governance set up. Fonts to be used are: [heading font] (Headings) + [body font] (body)." Tag `design_tokens`.
- **Mock-ups provided:** "Code have already provided a mock up to show how each of the websites will look in the Elevate components so there's no further work to be done here. Design token application: using only existing design tokens to apply brand guidelines of each of the [n] websites to the existing global component library." Fonts per brand. Tag `design_tokens`.
- Add, when design work is limited: "No design consultancy or production of page designs are included within the scope of this statement of work."

## 3.1.x Prismic Setup & Infrastructure
Bullets (bold label + detail):
- **Prismic pipelines & infrastructure:** Architect and implement dev, test, staging and prod pipelines for [every locale/brand by name] in line with existing streamlined updates and deployments.
- **Prismic repo instance:** Set up a dedicated Prismic repository instance for [brand(s)]. *(Leave this out for a new locale in an existing repo; say "Code will create a new locale added to the existing [brand] repository".)*
- **Pipeline configuration:** Configure CI/CD pipelines to automate deployment and content publishing workflows.
- **Infra configuration:** Provision and configure cloud infrastructure to support the new website[s].
- **Cloudflare configuration work:** Configuration within the existing infrastructure for optimal performance and security.
- **Automation:** Code will work with the HD team to agree what level of automation will be needed for [brand], delivered as part of the build feature tickets. *(Or: "Code will implement P1 and P2 smoke test automation including GTM, cookies, siteID.")*

Traffic split:
- None: "It's assumed that none of the [brand] sites will be launched with any % traffic split so no load balancers are required."
- Split: "It's assumed at the time of writing this SoW [brand] may wish to split traffic at launch initially. Code / HD teams will continue to work collaboratively to facilitate this through the Cloudflare Load Balancer process which has been part of the previous Elevate brand launches."

## 3.1.x Forms, Integrations, and Storage
Opening line: "Forms included on the [brand] site[s] include the following:" followed by a list.

**Postcode lookup:** "Assumption is that we will use Loqate for all postcode lookups in line with [parent]." (or "No postcode lookup is required.")

**Standard Elevate form (Contact Us / Request an Appointment / Consultation)**, one block per form:
- Applied to [all n locales / named locales] within this statement of work scope
- Form look and feel, entry fields, layout, validation messaging and tracking will all be in line with the standard Elevate platform [form name] (currently used on [brand])
- Prismic CMS fields will be in line with the existing Elevate set up
- Entries from each form to be sent to the following email address endpoints: [locale – email] (one line per locale)
- This will be done via a password protected CSV file sent with each submission (not batched up)
- Customer information will be processed via the existing PII infrastructure to ensure security and compliance is not compromised

**Showroom Locator (map view):** Google API to populate addresses as per existing Elevate; dealer types (or "There are no concepts of different 'types of dealers'"); front-end in line with the standard Showroom Locator journey (currently used on Luxaflex); "HD to share dealer database"; the PII sentence. Tag `dealer_locator`.

**Request an Appointment via locator:** Martech: email to dealer with form entries (password-protected CSV) and email to the brand address per locale. Tag `request_appointment`.

**Elevate generic/simple form:** "Now that the Elevate generic form has been delivered, it's assumed that [brand] will use this for any forms to be used on the site." For new field requirements, list each field with its validation rule (see the Aluvert SoW field list: Title, names max 50, email @ rule, phone 5–12 digits + country code, postcode 4–8, address 250, city/province/county/country 100, appointment date/time pickers, message 200, product category options, consent tick boxes, business name 250, yes/no picks). All fields: toggle on/off, optional/mandatory, validation/help text, any language.

**Embedded third-party form (Prismic slice):** "Code will build a new 'component slice' within Prismic which will house the existing JavaScript API forms managed by [team]." CMS fields: Page title, Description, Brand drop-down, Confirmation/thank-you page URL. Assumptions: all behaviour and martech encapsulated in the third-party app (Code only renders); confirmation page content-managed; HD to make sure cookies aren't displayed twice; FE tracking managed by HD. Risk: "As we are embedding unscoped JS and CSS directly into the page there is a risk of JS / CSS clashes, although Code believe this to be a low risk…"

**Email sign up / E-brochure (Prismic components):** "The [brand] teams have agreed to use the existing Prismic email sign up and Request an E-brochure components." Turnstile keys to be provided by HD IT before build. Tag `email_signup`, `request_ebrochure`, `turnstile`.

**Samples:** "Create new samples form for [brand] (based on Hillarys samples form)", plus new fields, removed fields, and "Integration with existing samples fulfilment (Maxlead)". Tag `samples`.

**Turnstile:** "Re-captcha currently exists on [forms]. In line with Elevate this will change to Turnstile." Tag `turnstile`.

**Linked, not rebuilt:** "Request a Brochure: this feature is via the dealer portal – so the form build is out of scope of this statement of work…" Use `linked` in out_of_scope.

## 3.1.x Taps and Sources
"Do not currently exist on the [brand] sites however, for launch the [brand] team would like to replicate this functionality. Taps and sources: implement taps and sources into the existing taps and sources functionality within Prismic. No work for Code to do." Tag `taps_sources`.

## 3.1.x Analytics & Compliance
- **Analytics:** Implement analytics tracking to monitor website usage, user behaviour, and key performance indicators in line with [Duette UK / existing Elevate] implementation. *(For forms-only: "Forms tracking will be applied to match the existing Elevate implementation.")*
- **OneTrust cookie script in Prismic:** Integrate the OneTrust cookie compliance script within the Prismic-managed site to ensure GDPR and privacy regulation compliance. HD to provide the script for each domain (staging & prod). *(GTM variant: "The HD team will load the OneTrust script via GTM, Code will be available to support with the implementation.")*
- **GUID site ID:** Assign and implement a globally unique identifier (GUID) for the site to support analytics and system integrations. Tag `guid`.

## 3.1.x Bloomreach
"Hunter Douglas have confirmed that Bloomreach BE integration is only required for [forms]. Hunter Douglas will need to provide both the FE tracking brief and BE Bloomreach integration briefs as part of the scoping of build tickets on approval of this SoW." Assumption: HD has completed any internal Bloomreach-to-brand integration; Code delivers the website-to-Bloomreach integration only. Tag `bloomreach`.

## 3.1.x Trustpilot
"This component already exists within the global component library so no additional work for Code to do within this SoW, assuming the brands are not expecting dynamic reviews and will use the standard component. If dynamic reviews are to be displayed in the future on the sites then a Trustpilot ID will be required." Tag `trustpilot`.

## 3.1.x PIM integration
Either config only ("[Brand] will take advantage of the [brand] products within the Salsify PIM…") with configuration activities: create brand record, assign locale, product pages in Prismic, filter records, PIM health check, [n] new categories, [n] new filters, [n] new specifications, download data logic.
Or API-ready ("…appetite to use the Salsify PIM but won't be ready to fully integrate… Code will therefore do the API integration work in preparation…").
Assumptions: products exist in Salsify in the data structure Elevate expects; HD to confirm hierarchy and filtering; PDP & PFG templates included. Tag `salsify_pim`, `pdp`, `pfg`.

## 3.1.x New / updated Elevate component
> Within the [brand] sites, [describe current behaviour]. Within the scope of the SoW Code will [build a new Elevate component / make changes to the existing [component] (likely a new variant)] to [outcome]. [Toggle on/off in Prismic; available on all devices.] No other feature changes are expected as part of this change.
>
> Once built and implemented this feature will be available to all HD brands.
>
> Requirements for this update can be found here: [brief link]

## 3.1.x Linked feature (not rebuilt)
> This feature is available on [all n locales] included in this statement of work. We are not rebuilding this feature on the Elevate platform, however [a link to the existing [feature] ([url]) can be added by the HD content editors in the Prismic CMS / we will recommend which component to use as a CTA].

---

## 3.1.x Locales & Languages
Use this whenever there's more than one locale, or any locale with more than one language.
> The following locales and languages are in scope for this statement of work:

| Locale | Existing URL | New URL / path | Language(s) |
|---|---|---|---|
| [locale] | [url] | [url/path] | [language(s)] |

- Multi-language locales ([locale]) will use the existing Elevate language set-up within Prismic, including the language switcher and hreflang tags
- All content and translations for each language will be created and loaded by the HD content editors in Prismic. Code are not providing copywriting, translation or content entry
- Form labels, validation and system messages will be provided in each language by HD [or: will use the existing Elevate translations for (language)]
- Any additional locale or language not listed above is not in scope and would be handled as a change request

## Design token change level (use inside Design activities)
- **None:** "Existing [parent] design tokens will be applied, so no design token work is included."
- **Light:** "Brand application will be limited to colour and font changes within the existing [parent] token set. No changes to spacing, radius, component structure or layout are included."
- **New token set:** "A new set of design tokens will be produced in keeping with the agreed design token governance. This covers colour, typography, [radius / spacing]. It does not include new components or component variants."
- **Variants:** list each component variant as its own module (see *New / updated Elevate component*).
Always add the fonts, and the dependency: "Fonts confirmed and, where applicable, purchased by HD prior to the start of design token work."

## 3.1.x Import & Migration
If migration **is** in scope, quantify it:
> Code will [script / automate / manually load] the import of [n pages / n products / n dealers / n images] from [source] into Prismic [for locales]. The source data will be supplied by HD as [format] by [date]. Code will run [one] import [plus one delta import before launch]. Data cleansing, de-duplication or re-writing of content is not included.

Assumptions: source data is complete and in the format agreed; any volume above [n] or a second full import is a change request.

If it's **not** in scope (the default), tag nothing and the derived Out of Scope will list "Automated / scripted / manual content migrations" and "Image migration". Add to Summary or Overview: "HD content editors will build all pages in Prismic using the global component library."

## 3.1.x Redirects & SEO
> HD will provide a 301 redirect map from existing URLs to new URLs for each locale, in the agreed format, before launch. Code will implement the redirects via the existing Cloudflare configuration. Up to [n] redirects per locale are included.

No SEO activity is included beyond implementing the redirect map. HD can set up and manage SEO metadata in Prismic. If redirects are excluded entirely, add "301 redirect mapping and implementation" to Out of Scope extras.

## 3.1.x Back-end integration (generic)
One block per system:
> **[System name]:** Code will integrate the [form / feature] with [system] so that [data] is [sent to / read from] [system] on [event].
- Integration method: [API / embedded script / file transfer]
- HD will provide the integration specification, endpoints and credentials for each environment (dev, test, staging, prod) as part of the scoping of build tickets
- Code is responsible for the website-to-[system] integration only; onward processing within [system] and its downstream systems is HD's responsibility
- Assumption: [system] is available and stable in all environments during build and test

## Forms: Customer Data Portal & PII
- **CDP backend hook-up:** "Form submissions will be passed to the Customer Data Portal (CDP) using the existing Elevate CDP integration, connecting to the existing martech endpoint ([endpoint system])."
- **CDP support only:** "HD will configure the CDP set-up; Code will support and check that all forms are submitting correctly."
- **CDP to email:** "Submissions will be sent from the CDP to [n] email endpoint(s): [list]."
- **PII storage:** "Code will set up a new PII storage container for [brand] within the existing PII infrastructure."
- Add the forms package's rules and additional-cost scenarios **from the uploaded sheet** as assumptions and change-request triggers.

## Dealer import responsibility
- **Code full import:** "Code will import up to [n] dealers from the dealer spreadsheet supplied by HD." Add the dealer-locator package's data-format and journey rules **from the uploaded sheet**.
- **Support only:** "HD will import the dealer data ([n] dealers); Code will support the import and check the data displays correctly."

## Image migration responsibility
- **Code does it:** "Code will migrate the existing site images into Prismic for [locales]." (Ask about alt text.)
- **Support only:** "HD will migrate the images; Code will provide support. Alt text is HD's responsibility."
- **Neither:** derived Out of Scope lists "Image migration".

## HD responsibilities (zero rows on the brand tab)
Rows on the brand tab costed at zero, with notes saying HD or the CMS does them (often SEO items), are listed as HD's:
> The following will be set up by the HD content editors within Prismic and are not part of Code's scope: [items from the brand tab].

Add any language or other conditions noted against those rows in the sheet.

---

## Timing plan
> A detailed timing plan will be provided on approval of this SoW so the work can be planned in with the Code team. Working assumption based on the current roadmap is [this build / these brands] will be worked on across [month(s) year]. Launch dates will be driven by HD once the detailed build plan has been agreed and finalised.

## Billing
- PO: script writes "No billing plan is required as PO [n] has already been provided and invoiced against."
- Milestones: script writes the standard sentence and the table.
