import json
from scrapy import Selector
from lxml import etree

# def clean_html(response):
#     title = response.xpath('//h1[contains(@id, "firstHeading")]').get()
#     content = response.xpath('//div[contains(@class, "mw-parser-output")]')
    
#     # Tags are still present, 
#     # use xpath('//<something>/text') and further processing in the spider to turn into actual documents
    
#     print(f'Content: {content}')
    
#     # TODO: filter "Shown below is ...:" text
#     # TODO: filter "External links" 'sections' and correspondingly sectional contents
#     filtered_content = content.xpath(
#         './/*[\
#             not(\
#                 self::p[contains(., "Editor") or \
#                 contains(., "For patient information") or \
#                     contains(., "help WikiDoc")]) \
#                         or self::h2[contains(., "References")] \
#                             or contains(@class, "reference)\
#                                 or self::ol[contains(@class, "references")]\
#                                 or descendant::ol[contains(@class, "references")]\
#                                     or contains(., "Template:")\
#                                         or self::table[contains(@class, "infobox:")]\
#                                         or descendant::table[contains(@class, "infobox:")]\
#                                             or self::*[contains(@id, "toc")]\
#                                                 or self::figure\
#         ]'
#     )
    
#     filtered_content = filtered_content.getall()
#     return {
#         'title': title,
#         'content': filtered_content
#     }
    
example_html = '''
    <!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Sexually transmitted disease - wikidoc</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"5676b4743cf5b442d4fe33d1","wgCSPNonce":false,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Sexually_transmitted_disease","wgTitle":"Sexually transmitted disease","wgCurRevisionId":1677880,"wgRevisionId":1677880,"wgArticleId":5874,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Disease","Urology","Infectious disease","Primary care"],"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Sexually_transmitted_disease","wgRelevantArticleId":5874,"wgIsProbablyEditable":false,"wgRelevantPageIsProbablyEditable":false,"wgRestrictionEdit":[
],"wgRestrictionMove":[],"wgPageFormsTargetName":null,"wgPageFormsAutocompleteValues":[],"wgPageFormsAutocompleteOnAllChars":false,"wgPageFormsFieldProperties":[],"wgPageFormsCargoFields":[],"wgPageFormsDependentFields":[],"wgPageFormsCalendarValues":[],"wgPageFormsCalendarParams":[],"wgPageFormsCalendarHTML":null,"wgPageFormsGridValues":[],"wgPageFormsGridParams":[],"wgPageFormsContLangYes":null,"wgPageFormsContLangNo":null,"wgPageFormsContLangMonths":[],"wgPageFormsHeightForMinimizingInstances":800,"wgPageFormsShowOnSelect":[],"wgPageFormsScriptPath":"/extensions/PageForms","edgValues":null,"wgPageFormsEDSettings":null,"wgAmericanDates":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgVector2022PreviewPages":[],"wgEditSubmitButtonLabelPublish":false};RLSTATE={"site.styles":"ready","user.styles":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","skins.vector.styles.legacy":"ready",
"ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.CookieWarning.styles":"ready","oojs-ui-core.styles":"ready","oojs-ui.styles.indicators":"ready","mediawiki.widgets.styles":"ready","oojs-ui-core.icons":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","site","mediawiki.page.ready","skins.vector.legacy.js","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.CookieWarning"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});});});</script>
<link rel="stylesheet" href="/load.php?lang=en&amp;modules=ext.CookieWarning.styles%7Cext.cite.styles%7Cext.visualEditor.desktopArticleTarget.noscript%7Cmediawiki.widgets.styles%7Coojs-ui-core.icons%2Cstyles%7Coojs-ui.styles.indicators%7Cskins.vector.styles.legacy&amp;only=styles&amp;skin=vector"/>
<script async="" src="/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.40.0"/>
<meta name="robots" content="max-image-preview:standard"/>
<meta name="format-detection" content="telephone=no"/>
<meta name="viewport" content="width=1000"/>
<link rel="icon" href="http://static.wikidoc.org/Wikidoc.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="wikidoc (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="https://www.wikidoc.org/api.php?action=rsd"/>
<link rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="alternate" type="application/atom+xml" title="wikidoc Atom feed" href="/index.php?title=Special:RecentChanges&amp;feed=atom"/>
</head>
<body class="skin-vector-legacy mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Sexually_transmitted_disease rootpage-Sexually_transmitted_disease skin-vector action-view"><div id="mw-page-base" class="noprint"></div>
<div id="mw-head-base" class="noprint"></div>
<div id="content" class="mw-body" role="main">
	<a id="top"></a>
	<div id="siteNotice"></div>
	<div class="mw-indicators">
	</div>
	<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-main">Sexually transmitted disease</span></h1>
	<div id="bodyContent" class="vector-body">
		<div id="siteSub" class="noprint"></div>
		<div id="contentSub"><div id="mw-content-subtitle"></div></div>
		<div id="contentSub2"></div>
		
		<div id="jump-to-nav"></div>
		<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
		<a class="mw-jump-link" href="#searchInput">Jump to search</a>
		<div id="mw-content-text" class="mw-body-content mw-content-ltr" lang="en" dir="ltr"><div class="mw-parser-output"><p><b>For patient information click <a href="/index.php/Sexually_transmitted_disease_(patient_information)" title="Sexually transmitted disease (patient information)">here</a></b>
</p>
<table class="infobox bordered" style="width: 15em; text-align: left; font-size: 90%; background:AliceBlue">

<tbody><tr>
<td colspan="1" style="text-align:center; background:DarkGray">
<p><b>Sexually transmitted disease Microchapters</b>
<b></b>
</p>
</td></tr>
<tr bgcolor="LightGrey">
<th>
</th></tr>
<tr bgcolor="Pink">
<th>
<p><a href="/index.php/Sexually_transmitted_disease_(patient_information)" title="Sexually transmitted disease (patient information)">Patient Information</a>
</p>
</th></tr>
<tr>
<th>
</th></tr>
<tr bgcolor="Pink">
<th>
<p><a class="mw-selflink-fragment" href="#Overview">Overview</a>
</p>
</th></tr>
<tr>
<th>
</th></tr>
<tr bgcolor="Pink">
<th>
<p><a class="mw-selflink-fragment" href="#Classification">Classification</a>
</p>
<dl><dd><a href="/index.php/Chlamydia" class="mw-redirect" title="Chlamydia">Chlamydia</a></dd>
<dd><a href="/index.php/Gonorrhea" title="Gonorrhea">Gonorrhea</a></dd>
<dd><a href="/index.php/HIV_AIDS" title="HIV AIDS">Human Immunodeficiency Virus (HIV)</a></dd>
<dd><a href="/index.php/Human_Papillomavirus" class="mw-redirect" title="Human Papillomavirus">Human papillomavirus (HPV)</a></dd>
<dd><a href="/index.php/Herpes_Simplex" class="mw-redirect" title="Herpes Simplex">Herpes Simplex Virus (HSV)</a></dd>
<dd><a href="/index.php/Mycoplasma_genitalium_infection" title="Mycoplasma genitalium infection">Mycoplasma genitalium</a></dd>
<dd><a href="/index.php/Syphilis" title="Syphilis">Syphilis</a></dd>
<dd><a href="/index.php/Trichomoniasis" title="Trichomoniasis">Trichomonas vaginalis</a></dd>
<dd><a href="/index.php/Zika_virus_infection" title="Zika virus infection">Zika Virus</a></dd>
<dd><a href="/index.php/Hepatitis_B" title="Hepatitis B">Hepatitis B</a></dd>
<dd><a href="/index.php/Hepatitis_C" title="Hepatitis C">Hepatitis C</a></dd>
<dd><a href="/index.php/Bacterial_vaginosis" title="Bacterial vaginosis">Bacterial vaginosis</a></dd>
<dd></dd></dl>
</th></tr>
<tr>
<th>
</th></tr>
<tr bgcolor="Pink">
<th>
<p><a class="mw-selflink-fragment" href="#Differential_Diagnosis">Differential Diagnosis</a>
</p>
</th></tr>
<tr>
<th>
</th></tr>
<tr bgcolor="Pink">
<th>
<p><a class="mw-selflink-fragment" href="#Treatment">Treatment</a>
</p>
</th></tr>
</tbody></table>
<p><b>Editor-In-Chief:</b> <a href="/index.php/User:C_Michael_Gibson" title="User:C Michael Gibson">C. Michael Gibson, M.S., M.D.</a> <a rel="nofollow" class="external autonumber" href="mailto:charlesmichaelgibson@gmail.com">[1]</a><a href="/index.php/User:Carla_Vorsatz" class="mw-redirect" title="User:Carla Vorsatz">Carla Vorsatz, M.D.</a><a rel="nofollow" class="external autonumber" href="mailto:xstz@milarepa.com.br">[2]</a>; <b>Associate Editor(s)-in-Chief: </b> <a href="/index.php/User:Tarek_Nafee" title="User:Tarek Nafee">Tarek Nafee, M.D.</a> <a rel="nofollow" class="external autonumber" href="mailto:tnafee@bidmc.harvard.edu">[3]</a><br />
</p><p><i><b>Synonyms and keywords:</b></i> Sexually transmissible disease; STD; VD; STI; sexually transmitted infection; venereal disease.
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p><a href="/index.php/Sexually_transmitted_diseases" class="mw-redirect" title="Sexually transmitted diseases">Sexually transmitted diseases</a> (or STDs) are <a href="/index.php/Bacterial" class="mw-redirect" title="Bacterial">bacterial</a>, <a href="/index.php/Viral" class="mw-redirect" title="Viral">viral</a>, <a href="/index.php/Fungal" class="mw-redirect" title="Fungal">fungal</a>, or <a href="/index.php/Protozoal" class="mw-redirect" title="Protozoal">protozoal</a> infections that are transmitted via sexual contact. Sexual contact may entail non-penetrative contact of the genitalia, performing or receiving oral sex (cunnilingus, anilingus, or fellatio), and insertive or receptive vaginal or anal <a href="/index.php?title=Sexual_intercourse&amp;action=edit&amp;redlink=1" class="new" title="Sexual intercourse (page does not exist)">sexual intercourse</a>. <a href="/index.php/STD" class="mw-redirect" title="STD">Sexually transmitted infections</a> may have a variety of clinical presentations including dermatological manifestations, generalized symptoms, or urogenital tract symptoms such as <a href="/index.php/Discharge" title="Discharge">discharge</a> and <a href="/index.php/Dysuria" title="Dysuria">dysuria</a>. Some infectious agents may be transmitted primarily through sexual contact while others may less frequently be transmitted sexually. 
</p><p>The CDC reported updated Surveillance data on <a href="/index.php/Sexually_transmitted_diseases" class="mw-redirect" title="Sexually transmitted diseases">sexually transmitted diseases</a> from 2018 in the United States, which included <a href="/index.php/Chlamydia" class="mw-redirect" title="Chlamydia">chlamydia</a>, <a href="/index.php/Gonorrhea" title="Gonorrhea">gonorrhea</a>, and <a href="/index.php/Syphilis" title="Syphilis">syphilis</a>.<sup id="cite_ref-CDCFact_1-0" class="reference"><a href="#cite_note-CDCFact-1">&#91;1&#93;</a></sup> Complications of <a href="/index.php/STDs" class="mw-redirect" title="STDs">STDs</a> depend on the causative pathogen and may range from genital or oral <a href="/index.php/Pruritis" title="Pruritis">pruritis</a> and discomfort to more serious complications such as <a href="/index.php/Pelvic_inflammatory_disease" title="Pelvic inflammatory disease">pelvic inflammatory disease</a>, <a href="/index.php/Primary_CNS_lymphoma" class="mw-redirect" title="Primary CNS lymphoma">primary CNS lymphoma</a>, <a href="/index.php/Cervical_cancer" title="Cervical cancer">cervical cancer</a>, as well as <a href="/index.php/Cardiac" class="mw-redirect" title="Cardiac">cardiac</a> and <a href="/index.php/Neurological" class="mw-redirect" title="Neurological">neurological</a> complications. If left untreated, some <a href="/index.php/STDs" class="mw-redirect" title="STDs">STDs</a> may progress to <a href="/index.php/Septic_shock" class="mw-redirect" title="Septic shock">septic shock</a> and death.
</p><p>Most <a href="/index.php/STDs" class="mw-redirect" title="STDs">STDs</a> have well-established risk factors and preventative measures. If followed appropriately, most <a href="/index.php/STD" class="mw-redirect" title="STD">STD transmissions</a> can be avoided.
</p>
<h2><span class="mw-headline" id="Classification">Classification</span></h2>
<p>Table below provides a concise comparison of various sexually transmitted diseases:<sup id="cite_ref-CDCFact_1-1" class="reference"><a href="#cite_note-CDCFact-1">&#91;1&#93;</a></sup>
</p>
<table style="border: 2; background: none;" align="center" class="wikitable">
<tbody><tr>
<th colspan="1" rowspan="2" style="border: 1; background: 1;">Transmission
</th>
<th colspan="1" rowspan="2">Clinical Presentation
</th>
<th colspan="1" rowspan="2">Disease
</th>
<th colspan="2" rowspan="1">Diagnosis
</th>
<th colspan="2" rowspan="1">Mother to Child Transmission
</th>
<th colspan="1" rowspan="2">Most Serious Complications
</th></tr>
<tr>
<th colspan="1" rowspan="1">Laboratory Studies</th>
<th>Clinical Diagnosis</th>
<th>Vertical Transmission</th>
<th>Trans-vaginal Transmission
</th></tr>
<tr>
<th colspan="1" rowspan="13">Primarily sexually transmitted
</th>
<th colspan="1" rowspan="6"><b>Genital Dermatological Manifestation <br />(e.g., <a href="/index.php/Genital_ulcer" title="Genital ulcer">ulcers</a>, <a href="/index.php/Chancre" title="Chancre">chancre</a>, vesicles, <a href="/index.php/Genital_warts" title="Genital warts">warts</a>, <a href="/index.php/Balanitis" title="Balanitis">balanitis</a> etc.)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/HPV" class="mw-redirect" title="HPV">HPV</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td><a href="/index.php/Cervical_Cancer" class="mw-redirect" title="Cervical Cancer">Cervical Cancer</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Herpes_simplex%27%27&amp;action=edit&amp;redlink=1" class="new" title="&#39;&#39;Herpes simplex&#39;&#39; (page does not exist)">''Herpes simplex''</a> 1 and 2</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort, superinfection
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Syphilis" title="Syphilis">Syphilis</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Neurosyphilis" title="Neurosyphilis">Neurosyphilis</a><br /></li>
<li><a href="/index.php/Cardiosyphilis" class="mw-redirect" title="Cardiosyphilis">Cardiosyphilis</a></li></ul>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Scabies" title="Scabies">Scabies</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Pubic_lice" class="mw-redirect" title="Pubic lice">Pubic lice</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Candidiasis" title="Candidiasis">Candidiasis</a><br />(in males)</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td>Mild to moderate <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<th colspan="1" rowspan="2"><b>Generalized Symptoms<br /> (e.g., constitutional symptoms)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/HIV" class="mw-redirect" title="HIV">HIV</a></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Primary_CNS_Lymphoma" class="mw-redirect" title="Primary CNS Lymphoma">Primary CNS Lymphoma</a><br /></li>
<li><a href="/index.php/Immunosuppression" title="Immunosuppression">Immunosuppression</a> (AIDS)</li></ul>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Syphilis" title="Syphilis">Syphilis</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Neurosyphilis" title="Neurosyphilis">Neurosyphilis<br /></a></li>
<li><a href="/index.php/Syphilis" title="Syphilis">Cardiosyphilis</a></li></ul>
</td></tr>
<tr>
<th colspan="1" rowspan="5"><b>Urogenital infections<br /> (e.g., <a href="/index.php/Vaginitis" title="Vaginitis">Vaginitis</a>, <a href="/index.php/Urethritis" title="Urethritis">Urethritis</a>, <a href="/index.php/Cervicitis" title="Cervicitis">Cervicitis</a>, and <a href="/index.php/PID" title="PID">PID</a>)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/Gonorrhea" title="Gonorrhea">Gonorrhea</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>✔</td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Chlamydia" class="mw-redirect" title="Chlamydia">Chlamydia</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>✔</td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Syphilis" title="Syphilis">Syphilis</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Neurosyphilis" title="Neurosyphilis">Neurosyphilis</a></li>
<li><a href="/index.php/Cardiosyphilis" class="mw-redirect" title="Cardiosyphilis">Cardiosyphilis</a></li></ul>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Mycoplasma_genitalium%27%27_infection&amp;action=edit&amp;redlink=1" class="new" title="&#39;&#39;Mycoplasma genitalium&#39;&#39; infection (page does not exist)"><i>Mycoplasma genitalium</i></a></td>
<td>✔</td>
<td>✔</td>
<td>unknown</td>
<td>unknown</td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Trichomonas_vaginalis%27%27&amp;action=edit&amp;redlink=1" class="new" title="&#39;&#39;Trichomonas vaginalis&#39;&#39; (page does not exist)">''Trichomonas vaginalis''</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<th colspan="1" rowspan="6">Less frequently sexually transmitted
</th>
<th colspan="1" rowspan="3"><b>Generalized Symptoms<br /> (e.g., constitutional symptoms)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/Zika_virus_infection" title="Zika virus infection">Zika Virus</a></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td><a href="/index.php/Vertical_transmission" title="Vertical transmission">Vertical transmission</a> and congenital abnormalities
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Hepatitis_B" title="Hepatitis B">Hepatitis B</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td><a href="/index.php/Hepatocellular_Carcinoma" class="mw-redirect" title="Hepatocellular Carcinoma">Hepatocellular Carcinoma</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Hepatitis_C" title="Hepatitis C">Hepatitis C</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td><a href="/index.php/Liver_cirrhosis" class="mw-redirect" title="Liver cirrhosis">Liver cirrhosis</a>, <a href="/index.php/Hepatocellular_Carcinoma" class="mw-redirect" title="Hepatocellular Carcinoma">Hepatocellular Carcinoma</a>
</td></tr>
<tr>
<th colspan="1" rowspan="3"><b>Urogenital Infections <br /> (e.g., <a href="/index.php/Vaginitis" title="Vaginitis">Vaginitis</a>, <a href="/index.php/Urethritis" title="Urethritis">Urethritis</a>, <a href="/index.php/Cervicitis" title="Cervicitis">Cervicitis</a>, and <a href="/index.php/PID" title="PID">PID</a>)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Gardnerella_vaginalis%27%27&amp;action=edit&amp;redlink=1" class="new" title="&#39;&#39;Gardnerella vaginalis&#39;&#39; (page does not exist)">''Gardnerella vaginalis''</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Candidiasis" title="Candidiasis">Candidiasis</a><br /> (in females)</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Ureaplasma_urealyticum%27%27&amp;action=edit&amp;redlink=1" class="new" title="&#39;&#39;Ureaplasma urealyticum&#39;&#39; (page does not exist)"> <i>Ureaplasma urealyticum</i></a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Differential_Diagnosis">Differential Diagnosis</span></h2>
<p>Table below provides differential diagnosis of sexually transmitted diseases:<sup id="cite_ref-CDCFact_1-2" class="reference"><a href="#cite_note-CDCFact-1">&#91;1&#93;</a></sup>
</p>
<table class="wikitable" style="border: 2; background: none;">

<tbody><tr>
<th rowspan="2">Disease
</th>
<th rowspan="1" colspan="9">Symptoms
</th></tr>
<tr>
<th rowspan="1"><a href="/index.php/Vaginal_discharge" title="Vaginal discharge">Discharge</a></th>
<th><a href="/index.php/Dysuria" title="Dysuria">Dysuria</a></th>
<th>Vaginal odor</th>
<th><a href="/index.php/Dyspareunia" title="Dyspareunia">Dyspareunia</a></th>
<th>Genital skin lesion</th>
<th>Genital pruritis</th>
<th><a href="/index.php/Fever" title="Fever">Fever</a></th>
<th><a href="/index.php/Lymphadenopathy" title="Lymphadenopathy">Lymphadenopathy</a></th>
<th>Other symptoms
</th></tr>
<tr>
<td><a href="/index.php/Chlamydia" class="mw-redirect" title="Chlamydia">Chlamydia</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td><a href="/index.php/Cough" title="Cough">Cough</a>, <a href="/index.php/Shortness_of_breath" class="mw-redirect" title="Shortness of breath">shortness of breath</a>, <a href="/index.php/Red_eye" title="Red eye">red eye</a> with discharge (neonate), <a href="/index.php/Joint_pain" class="mw-redirect" title="Joint pain">joint pain</a>
</td></tr>
<tr>
<td><a href="/index.php/Gonorrhea" title="Gonorrhea">Gonorrhea</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>✔</td>
<td></td>
<td><a href="/index.php/Sore_throat" class="mw-redirect" title="Sore throat">Sore throat</a>, <a href="/index.php/Polyarthralgia" class="mw-redirect" title="Polyarthralgia">polyarthralgia</a>, <a href="/index.php/Tenosynovitis" title="Tenosynovitis">tenosynovitis</a>, <a href="/index.php/Rash" title="Rash">rash</a>, eye discharge (neonates)
</td></tr>
<tr>
<td><a href="/index.php/HIV" class="mw-redirect" title="HIV">HIV</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>✔</td>
<td>✔</td>
<td><a href="/index.php/Fever" title="Fever">Fever</a>, <a href="/index.php/Lymphadenopathy" title="Lymphadenopathy">lymphadenopathy</a>, <a href="/index.php/Rash" title="Rash">rash</a>, <a href="/index.php/Fatigue" title="Fatigue">fatigue</a>, <a href="/index.php/Myalgia" title="Myalgia">myalgia</a>, arthritic pain, <a href="/index.php/Headache" title="Headache">headache</a>
</td></tr>
<tr>
<td><a href="/index.php/Herpes_simplex" title="Herpes simplex">Herpes simplex</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td>✔</td>
<td><a href="/index.php/Fatigue" title="Fatigue">Fatigue</a>, <a href="/index.php/Myalgia" title="Myalgia">myalgia</a>, painful oral ulcers
</td></tr>
<tr>
<td><a href="/index.php/HPV" class="mw-redirect" title="HPV">HPV</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td><a href="/index.php/Weight_loss" title="Weight loss">Weight loss</a>, <a href="/index.php/Hoarseness" class="mw-redirect" title="Hoarseness">hoarseness</a> (adults), altered cry, <a href="/index.php/Stridor" title="Stridor">stridor</a> (infants)
</td></tr>
<tr>
<td><a href="/index.php/Hepatitis_B" title="Hepatitis B">Hepatitis B</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>✔</td>
<td>✔</td>
<td><a href="/index.php/Fever" title="Fever">Fever</a>, <a href="/index.php/Fatigue" title="Fatigue">fatigue</a>, <a href="/index.php/Nausea" class="mw-redirect" title="Nausea">nausea</a>, <a href="/index.php/Vomiting" class="mw-redirect" title="Vomiting">vomiting</a>, <a href="/index.php/Loss_of_appetite" class="mw-redirect" title="Loss of appetite">loss of appetite</a>, <a href="/index.php/Abdominal_pain" title="Abdominal pain">abdominal pain</a>, <a href="/index.php/Dark_urine" class="mw-redirect" title="Dark urine">dark urine</a>, <a href="/index.php/Acholic_stools" title="Acholic stools">clay-colored stools</a>, <a href="/index.php/Joint_pain" class="mw-redirect" title="Joint pain">joint pain</a>, yellowish discoloration of the eyes and skin, <a href="/index.php/Skin_rash" class="mw-redirect" title="Skin rash">skin rash</a>, <a href="/index.php/Muscle_pain" class="mw-redirect" title="Muscle pain">muscle pain</a>
</td></tr>
<tr>
<td><a href="/index.php/Hepatitis_C" title="Hepatitis C">Hepatitis C</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>✔</td>
<td>✔</td>
<td><a href="/index.php/Fever" title="Fever">Fever</a>, <a href="/index.php/Fatigue" title="Fatigue">fatigue</a>, <a href="/index.php/Anorexia" title="Anorexia">anorexia</a>, <a href="/index.php/Arthralgia" title="Arthralgia">arthralgia</a>, <a href="/index.php/Nausea" class="mw-redirect" title="Nausea">nausea</a>, <a href="/index.php/Vomiting" class="mw-redirect" title="Vomiting">vomiting</a>
</td></tr>
<tr>
<td><a href="/index.php/Bacterial_vaginosis" title="Bacterial vaginosis">Bacterial vaginosis</a></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>None
</td></tr>
<tr>
<td><a href="/index.php/Mycoplasma_genitalium" class="mw-redirect" title="Mycoplasma genitalium">Mycoplasma genitalium</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td>None
</td></tr>
<tr>
<td><a href="/index.php/Zika_virus" title="Zika virus">Zika virus</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>✔</td>
<td></td>
<td><a href="/index.php/Conjunctivitis" title="Conjunctivitis">Conjunctivitis</a>, <a href="/index.php/Rash" title="Rash">rash</a>, <a href="/index.php/Joint_pain" class="mw-redirect" title="Joint pain">joint pain</a>, <a href="/index.php/Myalgia" title="Myalgia">myalgia</a>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Treatment">Treatment</span></h2>
<ul><li>To view the treatment of <a href="/index.php/Chlamydia_infection" title="Chlamydia infection">chlamydia infection</a> <a href="/index.php/Chlamydia_infection_medical_therapy" title="Chlamydia infection medical therapy">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Gonorrhea" title="Gonorrhea">gonorrhea</a> <a href="/index.php/Gonorrhea_medical_therapy" title="Gonorrhea medical therapy">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Herpes_simplex" title="Herpes simplex">herpes simplex</a> <a href="/index.php/Herpes_simplex_treatment" title="Herpes simplex treatment">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Mycoplasma_genitalium_infection" title="Mycoplasma genitalium infection">mycoplasma genitalium infection</a> <a href="/index.php/Mycoplasma_genitalium_infection#Medical_Therapy" title="Mycoplasma genitalium infection">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Syphilis" title="Syphilis">syphilis</a> <a href="/index.php/Syphilis_medical_therapy" title="Syphilis medical therapy">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Trichomoniasis" title="Trichomoniasis">trichomoniasis</a> <a href="/index.php/Trichomoniasis_medical_therapy" title="Trichomoniasis medical therapy">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Bacterial_vaginosis" title="Bacterial vaginosis">bacterial vaginosis</a> <a href="/index.php/Bacterial_vaginosis_medical_therapy" title="Bacterial vaginosis medical therapy">click here</a>.</li>
<li>To view the detailed treatment of <a href="/index.php/Human_papillomavirus" title="Human papillomavirus">human papillomavirus</a> <a href="/index.php/Human_papillomavirus_medical_therapy" title="Human papillomavirus medical therapy">click here</a>.</li></ul>
<h2><span class="mw-headline" id="References">References</span></h2>
<div class="reflist columns references-column-width" style="-moz-column-width: 30em; -webkit-column-width: 30em; column-width: 30em; list-style-type: decimal;">
<ol class="references">
<li id="cite_note-CDCFact-1"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-CDCFact_1-0">1.0</a></sup> <sup><a href="#cite_ref-CDCFact_1-1">1.1</a></sup> <sup><a href="#cite_ref-CDCFact_1-2">1.2</a></sup></span> <span class="reference-text"> CDC Sexually Transmitted Disease Surveillance 2018 <a href="/index.php/STDs" class="mw-redirect" title="STDs">STDs</a> in the United States. The Centers for Disease Control and Prevention. <a rel="nofollow" class="external free" href="https://www.cdc.gov/std/stats18/toc.htm">https://www.cdc.gov/std/stats18/toc.htm</a> Accessed on January 25, 2020. </span>
</li>
</ol></div>
<!-- 
NewPP limit report
Cached time: 20240807134837
Cache expiry: 1209600
Reduced expiry: false
Complications: [no‐toc‐conversion]
CPU time usage: 0.043 seconds
Real time usage: 0.075 seconds
Preprocessor visited node count: 295/1000000
Post‐expand include size: 2241/2097152 bytes
Template argument size: 109/2097152 bytes
Highest expansion depth: 8/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 900/5000000 bytes
Lua time usage: 0.010/7 seconds
Lua virtual size: 5062656/52428800 bytes
Lua estimated memory usage: 0 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   48.900      1 -total
 66.17%   32.359      1 Template:Reflist
  8.36%    4.088      1 Template:CMG
  5.27%    2.578      1 Template:Main_other
  4.84%    2.365      1 Template:Sexually_transmitted_disease
  4.28%    2.091      1 Template:Column-width
  4.09%    2.000      1 Template:AE
  4.02%    1.966      1 Template:Cv
  4.00%    1.956      1 Template:SK
  3.94%    1.926      1 Template:TarekNafee
-->

<!-- Saved in parser cache with key wikidb-wd_:pcache:idhash:5874-0!canonical and timestamp 20240807134837 and revision id 1677880. Rendering was triggered because: page-view
 -->
</div>
<div class="printfooter" data-nosnippet="">Retrieved from "<a dir="ltr" href="https://www.wikidoc.org/index.php?title=Sexually_transmitted_disease&amp;oldid=1677880">https://www.wikidoc.org/index.php?title=Sexually_transmitted_disease&amp;oldid=1677880</a>"</div></div>
		<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/index.php/Special:Categories" title="Special:Categories">Categories</a>: <ul><li><a href="/index.php/Category:Disease" title="Category:Disease">Disease</a></li><li><a href="/index.php/Category:Urology" title="Category:Urology">Urology</a></li><li><a href="/index.php/Category:Infectious_disease" title="Category:Infectious disease">Infectious disease</a></li><li><a href="/index.php/Category:Primary_care" title="Category:Primary care">Primary care</a></li></ul></div></div>
	</div>
</div>
<div id='mw-data-after-content'>
	<div class="mw-cookiewarning-container"><div class="mw-cookiewarning-text"><span>Cookies help us deliver our services. By using our services, you agree to our use of cookies.</span></div><form method="POST"><div class='oo-ui-layout oo-ui-horizontalLayout'><span class='oo-ui-widget oo-ui-widget-enabled oo-ui-inputWidget oo-ui-buttonElement oo-ui-buttonElement-framed oo-ui-labelElement oo-ui-flaggedElement-primary oo-ui-flaggedElement-progressive oo-ui-buttonInputWidget'><button type='submit' tabindex='0' name='disablecookiewarning' value='OK' class='oo-ui-inputWidget-input oo-ui-buttonElement-button'><span class='oo-ui-iconElement-icon oo-ui-iconElement-noIcon oo-ui-image-invert'></span><span class='oo-ui-labelElement-label'>OK</span><span class='oo-ui-indicatorElement-indicator oo-ui-indicatorElement-noIndicator oo-ui-image-invert'></span></button></span></div></form></div>
</div>

<div id="mw-navigation">
	<h2>Navigation menu</h2>
	<div id="mw-head">
		
<nav id="p-personal" class="vector-menu mw-portlet mw-portlet-personal vector-user-menu-legacy" aria-labelledby="p-personal-label" role="navigation"  >
	<h3
		id="p-personal-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Personal tools</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="pt-login" class="mw-list-item"><a href="/index.php?title=Special:UserLogin&amp;returnto=Sexually+transmitted+disease" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o"><span>Log in</span></a></li><li id="pt-createaccount" class="mw-list-item"><a href="/index.php/Special:RequestAccount" title="You are encouraged to create an account and log in; however, it is not mandatory"><span>Request account</span></a></li></ul>
		
	</div>
</nav>

		<div id="left-navigation">
			
<nav id="p-namespaces" class="vector-menu mw-portlet mw-portlet-namespaces vector-menu-tabs vector-menu-tabs-legacy" aria-labelledby="p-namespaces-label" role="navigation"  >
	<h3
		id="p-namespaces-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Namespaces</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="ca-Home2" class="mw-list-item"><a href="http://www.wikidoc.org/index.php/Main_Page"><span>Home</span></a></li><li id="ca-nstab-main" class="selected mw-list-item"><a href="/index.php/Sexually_transmitted_disease" title="View the content page [c]" accesskey="c"><span>Page</span></a></li><li id="ca-talk" class="new mw-list-item"><a href="/index.php?title=Talk:Sexually_transmitted_disease&amp;action=edit&amp;redlink=1" rel="discussion" title="Discussion about the content page (page does not exist) [t]" accesskey="t"><span>Discussion</span></a></li></ul>
		
	</div>
</nav>

			
<nav id="p-variants" class="vector-menu mw-portlet mw-portlet-variants emptyPortlet vector-menu-dropdown" aria-labelledby="p-variants-label" role="navigation"  >
	<input type="checkbox"
		id="p-variants-checkbox"
		role="button"
		aria-haspopup="true"
		data-event-name="ui.dropdown-p-variants"
		class="vector-menu-checkbox"
		aria-labelledby="p-variants-label"
	/>
	<label
		id="p-variants-label"
		 aria-label="Change language variant"
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">English</span>
	</label>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"></ul>
		
	</div>
</nav>

		</div>
		<div id="right-navigation">
			
<nav id="p-views" class="vector-menu mw-portlet mw-portlet-views vector-menu-tabs vector-menu-tabs-legacy" aria-labelledby="p-views-label" role="navigation"  >
	<h3
		id="p-views-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Views</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="ca-view" class="selected mw-list-item"><a href="/index.php/Sexually_transmitted_disease"><span>Read</span></a></li><li id="ca-viewsource" class="mw-list-item"><a href="/index.php?title=Sexually_transmitted_disease&amp;action=edit" title="This page is protected.&#10;You can view its source [e]" accesskey="e"><span>View source</span></a></li><li id="ca-history" class="mw-list-item"><a href="/index.php?title=Sexually_transmitted_disease&amp;action=history" title="Past revisions of this page [h]" accesskey="h"><span>View history</span></a></li><li id="ca-Help" class="mw-list-item"><a href="http://www.wikidoc.org/index.php/Category:Help"><span>Help</span></a></li></ul>
		
	</div>
</nav>

			
<nav id="p-cactions" class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-menu-dropdown" aria-labelledby="p-cactions-label" role="navigation"  title="More options" >
	<input type="checkbox"
		id="p-cactions-checkbox"
		role="button"
		aria-haspopup="true"
		data-event-name="ui.dropdown-p-cactions"
		class="vector-menu-checkbox"
		aria-labelledby="p-cactions-label"
	/>
	<label
		id="p-cactions-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">More</span>
	</label>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"></ul>
		
	</div>
</nav>

			
<div id="p-search" role="search" class="vector-search-box-vue  vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box">
	<div>
		<form action="/index.php" id="searchform"
			class="vector-search-box-form">
			<div id="simpleSearch"
				class="vector-search-box-inner"
				 data-search-loc="header-navigation">
				<input class="vector-search-box-input"
					 type="search" name="search" placeholder="Search wikidoc" aria-label="Search wikidoc" autocapitalize="sentences" title="Search wikidoc [f]" accesskey="f" id="searchInput"
				>
				<input type="hidden" name="title" value="Special:Search">
				<input id="mw-searchButton"
					 class="searchButton mw-fallbackSearchButton" type="submit" name="fulltext" title="Search the pages for this text" value="Search">
				<input id="searchButton"
					 class="searchButton" type="submit" name="go" title="Go to a page with this exact name if it exists" value="Go">
			</div>
		</form>
	</div>
</div>

		</div>
	</div>
	
<div id="mw-panel" class="vector-legacy-sidebar">
	<div id="p-logo" role="banner">
		<a class="mw-wiki-logo" href="/index.php/Main_Page"
			title="Visit the main page"></a>
	</div>
	
<nav id="p-tb" class="vector-menu mw-portlet mw-portlet-tb vector-menu-portal portal" aria-labelledby="p-tb-label" role="navigation"  >
	<h3
		id="p-tb-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Tools</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="t-whatlinkshere" class="mw-list-item"><a href="/index.php/Special:WhatLinksHere/Sexually_transmitted_disease" title="A list of all wiki pages that link here [j]" accesskey="j"><span>What links here</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/index.php/Special:RecentChangesLinked/Sexually_transmitted_disease" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k"><span>Related changes</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/index.php/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q"><span>Special pages</span></a></li><li id="t-print" class="mw-list-item"><a href="javascript:print();" rel="alternate" title="Printable version of this page [p]" accesskey="p"><span>Printable version</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/index.php?title=Sexually_transmitted_disease&amp;oldid=1677880" title="Permanent link to this revision of this page"><span>Permanent link</span></a></li><li id="t-info" class="mw-list-item"><a href="/index.php?title=Sexually_transmitted_disease&amp;action=info" title="More information about this page"><span>Page information</span></a></li></ul>
		
	</div>
</nav>

	
	
</div>

</div>

<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-credits">This page was last edited 18:03, 10 December 2020 by <a href="/index.php/User:Sahar_Memar_Montazerin" class="mw-userlink" title="User:Sahar Memar Montazerin"><bdi>Sahar Memar Montazerin</bdi></a>. Based on work by <a href="/index.php/User:Xstz" class="mw-userlink" title="User:Xstz"><bdi>Carla Vorsatz</bdi></a>, <a href="/index.php/User:Mmir" class="mw-userlink" title="User:Mmir"><bdi>mahshid mir</bdi></a>, <a href="/index.php/User:Aditya_Ganti" class="mw-userlink" title="User:Aditya Ganti"><bdi>adityapavankumarganti@gmail.com</bdi></a>, <a href="/index.php/User:Tarek_Nafee" class="mw-userlink" title="User:Tarek Nafee"><bdi>Tarek Nafee</bdi></a>, <a href="/index.php/User:Anthony_Gallo" class="mw-userlink" title="User:Anthony Gallo"><bdi>Anthony Gallo</bdi></a>, <a href="/index.php/User:Charmaine_Patel" class="mw-userlink" title="User:Charmaine Patel"><bdi>Charmaine Patel</bdi></a>, <a href="/index.php/User:Vishnu_Vardhan_Serla" class="mw-userlink" title="User:Vishnu Vardhan Serla"><bdi>Vishnu Vardhan Serla</bdi></a>, <a href="/index.php/User:Prashanthsaddala" class="mw-userlink" title="User:Prashanthsaddala"><bdi>Prashanth Saddala</bdi></a>, <a href="/index.php/User:Lakshmi_Gopalakrishnan" class="mw-userlink" title="User:Lakshmi Gopalakrishnan"><bdi>Lakshmi Gopalakrishnan</bdi></a> and <a href="/index.php/User:Priyamvada_Singh" class="mw-userlink" title="User:Priyamvada Singh"><bdi>Priyamvada</bdi></a> and wikidoc users <a href="/index.php?title=User:WikiBot&amp;action=edit&amp;redlink=1" class="new mw-userlink" title="User:WikiBot (page does not exist)"><bdi>WikiBot</bdi></a>, <a href="/index.php/User:Sabawoon_Mirwais" class="mw-userlink" title="User:Sabawoon Mirwais"><bdi>Sabawoon Mirwais</bdi></a>, <a href="/index.php/User:Maria_Villarreal" class="mw-userlink" title="User:Maria Villarreal"><bdi>Maria Villarreal</bdi></a> and <a href="/index.php/User:Aysha_Aslam" class="mw-userlink" title="User:Aysha Aslam"><bdi>Aysha Aslam</bdi></a>.</li>
	<li id="footer-info-copyright">Content is available under <a class="external" rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution/Share-Alike License</a> unless otherwise noted; All rights reserved on Board Review content.</li>
</ul>

	<ul id="footer-places">
	<li id="footer-places-privacy"><a href="/index.php/wikidoc:Privacy_policy">Privacy policy</a></li>
	<li id="footer-places-about"><a href="/index.php/wikidoc:About">About wikidoc</a></li>
	<li id="footer-places-disclaimers"><a href="/index.php/wikidoc:General_disclaimer">Disclaimers</a></li>
</ul>

	<ul id="footer-icons" class="noprint">
	<li id="footer-copyrightico"><a href="http://creativecommons.org/licenses/by-sa/3.0/"><img src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" alt="Creative Commons Attribution/Share-Alike License" width="88" height="31" loading="lazy"/></a></li>
	<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/resources/assets/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/resources/assets/poweredby_mediawiki_132x47.png 1.5x, /resources/assets/poweredby_mediawiki_176x62.png 2x" width="88" height="31" loading="lazy"/></a></li>
</ul>

</footer>

<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":110,"wgPageParseReport":{"limitreport":{"cputime":"0.043","walltime":"0.075","ppvisitednodes":{"value":295,"limit":1000000},"postexpandincludesize":{"value":2241,"limit":2097152},"templateargumentsize":{"value":109,"limit":2097152},"expansiondepth":{"value":8,"limit":100},"expensivefunctioncount":{"value":0,"limit":100},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":900,"limit":5000000},"timingprofile":["100.00%   48.900      1 -total"," 66.17%   32.359      1 Template:Reflist","  8.36%    4.088      1 Template:CMG","  5.27%    2.578      1 Template:Main_other","  4.84%    2.365      1 Template:Sexually_transmitted_disease","  4.28%    2.091      1 Template:Column-width","  4.09%    2.000      1 Template:AE","  4.02%    1.966      1 Template:Cv","  4.00%    1.956      1 Template:SK","  3.94%    1.926      1 Template:TarekNafee"]},"scribunto":{"limitreport-timeusage":{"value":"0.010","limit":"7"},"limitreport-virtmemusage":{"value":5062656,"limit":52428800},"limitreport-estmemusage":0},"cachereport":{"timestamp":"20240807134837","ttl":1209600,"transientcontent":false}}});});</script>
</body>
</html>
'''

parser = etree.HTMLParser()
tree = etree.fromstring(example_html, parser)


# Apply your XPath expressions
title = tree.xpath('//h1[contains(@id, "firstHeading")]/text()')
content = tree.xpath('//div[contains(@class, "mw-parser-output")]')

print(f'content: {content}')

filtered_content = content[0].xpath(
        './/*[not(self::table[contains(@class, "infobox")])]'
    )

# './/*[\
#             not(self::p[contains(., "Editor") or \
#             contains(., "For patient information") or \
#             contains(., "help WikiDoc")]) and \
#             not(contains(., "References")) and \
#             not(contains(@class, "reference")) and \
#             not(.//@class="references") and \
#             not(contains(., "Template:")) and \
#             not(self::table[contains(@class, "infobox")]) and \
#             not(descendant::table[contains(@class, "infobox")]) and \
#             not(self::*[contains(@id, "toc")]) and \
#             not(self::figure)\
#         ]'

print(f"Title: {title}")
print(f"Filtered Content:")
print(f"{filtered_content}")
# for element in filtered_content:
#     print(etree.tostring(element, pretty_print=True).decode('utf-8'))

# with open("filtered_content.txt", "w", encoding="utf-8") as file:
#     file.write(f"Title: {title[0] if title else 'No Title'}\n")
#     file.write("Filtered Content:\n")
#     for element in filtered_content:
#         text_content = element.xpath('string()')
#         if text_content:  # Only write non-empty lines
#             file.write(text_content + "\n")
            
# with open("filtered_content.txt", "w", encoding="utf-8") as file:
#     file.write(f"Title: {title[0] if title else 'No Title'}\n")
#     file.write("Filtered Content:\n")
    
#     for element in filtered_content:
#         html_content = etree.tostring(element, pretty_print=True, encoding="unicode")
#         if html_content.strip():  # Only write non-empty content
#             file.write(html_content + "\n")