import sys
sys.path.append('../src')
from HtmlTableTransformer.parser import HtmlTableTransformer

html = '''
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
<th colspan="1" rowspan="6"><b>Genital Dermatological Manifestation <br>(e.g., <a href="/index.php/Genital_ulcer" title="Genital ulcer">ulcers</a>, <a href="/index.php/Chancre" title="Chancre">chancre</a>, vesicles, <a href="/index.php/Genital_warts" title="Genital warts">warts</a>, <a href="/index.php/Balanitis" title="Balanitis">balanitis</a> etc.)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/HPV" class="mw-redirect" title="HPV">HPV</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td><a href="/index.php/Cervical_Cancer" class="mw-redirect" title="Cervical Cancer">Cervical Cancer</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Herpes_simplex%27%27&amp;action=edit&amp;redlink=1" class="new" title="''Herpes simplex'' (page does not exist)">''Herpes simplex''</a> 1 and 2</td>
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
<ul><li><a href="/index.php/Neurosyphilis" title="Neurosyphilis">Neurosyphilis</a><br></li>
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
<td colspan="1" rowspan="1"><a href="/index.php/Candidiasis" title="Candidiasis">Candidiasis</a><br>(in males)</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td>Mild to moderate <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<th colspan="1" rowspan="2"><b>Generalized Symptoms<br> (e.g., constitutional symptoms)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php/HIV" class="mw-redirect" title="HIV">HIV</a></td>
<td>✔</td>
<td></td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Primary_CNS_Lymphoma" class="mw-redirect" title="Primary CNS Lymphoma">Primary CNS Lymphoma</a><br></li>
<li><a href="/index.php/Immunosuppression" title="Immunosuppression">Immunosuppression</a> (AIDS)</li></ul>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Syphilis" title="Syphilis">Syphilis</a></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td></td>
<td>
<ul><li><a href="/index.php/Neurosyphilis" title="Neurosyphilis">Neurosyphilis<br></a></li>
<li><a href="/index.php/Syphilis" title="Syphilis">Cardiosyphilis</a></li></ul>
</td></tr>
<tr>
<th colspan="1" rowspan="5"><b>Urogenital infections<br> (e.g., <a href="/index.php/Vaginitis" title="Vaginitis">Vaginitis</a>, <a href="/index.php/Urethritis" title="Urethritis">Urethritis</a>, <a href="/index.php/Cervicitis" title="Cervicitis">Cervicitis</a>, and <a href="/index.php/PID" title="PID">PID</a>)</b>
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
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Mycoplasma_genitalium%27%27_infection&amp;action=edit&amp;redlink=1" class="new" title="''Mycoplasma genitalium'' infection (page does not exist)"><i>Mycoplasma genitalium</i></a></td>
<td>✔</td>
<td>✔</td>
<td>unknown</td>
<td>unknown</td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Trichomonas_vaginalis%27%27&amp;action=edit&amp;redlink=1" class="new" title="''Trichomonas vaginalis'' (page does not exist)">''Trichomonas vaginalis''</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td><a href="/index.php/PID" title="PID">PID</a>
</td></tr>
<tr>
<th colspan="1" rowspan="6">Less frequently sexually transmitted
</th>
<th colspan="1" rowspan="3"><b>Generalized Symptoms<br> (e.g., constitutional symptoms)</b>
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
<th colspan="1" rowspan="3"><b>Urogenital Infections <br> (e.g., <a href="/index.php/Vaginitis" title="Vaginitis">Vaginitis</a>, <a href="/index.php/Urethritis" title="Urethritis">Urethritis</a>, <a href="/index.php/Cervicitis" title="Cervicitis">Cervicitis</a>, and <a href="/index.php/PID" title="PID">PID</a>)</b>
</th>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Gardnerella_vaginalis%27%27&amp;action=edit&amp;redlink=1" class="new" title="''Gardnerella vaginalis'' (page does not exist)">''Gardnerella vaginalis''</a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php/Candidiasis" title="Candidiasis">Candidiasis</a><br> (in females)</td>
<td></td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
<tr>
<td colspan="1" rowspan="1"><a href="/index.php?title=%27%27Ureaplasma_urealyticum%27%27&amp;action=edit&amp;redlink=1" class="new" title="''Ureaplasma urealyticum'' (page does not exist)"> <i>Ureaplasma urealyticum</i></a></td>
<td>✔</td>
<td>✔</td>
<td></td>
<td></td>
<td>Moderate to severe <a href="/index.php/Pruritis" title="Pruritis">pruritis</a>/discomfort
</td></tr>
</tbody></table>'''

html = '''
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
</td></tr></tbody></table>'''

tableParser = HtmlTableTransformer(html)

result = tableParser.toText()

print(result)

# import numpy as np

# array = np.array(result)
# print(array.shape)