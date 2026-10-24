# PROTOCOL-SAKHA — આ ZIPની સ્થિતિ

આ ZIP હાલના PROTOCOL-SAKHA source project પર આધારિત છે અને હાલની design/feature set જાળવવાનો પ્રયાસ કરે છે. તેમાં નીચેના source-level updates છે:

- Event Plannerમાં Going/Return માટે movement group field.
- Return allocation દરમિયાન matching Going eventમાંથી rank-order પ્રમાણે એ જ કર્મચારી જાળવવાનો પ્રયત્ન.
- substitute બદલાય તો કારણની નોંધ.
- Event Plannerમાં manual point entry, પસંદ કરેલા કાયમી રૂટમાં point save, અને નવો કાયમી રૂટ નામ/શરૂઆત/અંત સાથે બનાવવાની સુવિધા.
- દરેક point માટે route ownerથી અલગ jurisdiction police station પસંદ કરવાની સુવિધા.
- Auto allocationમાં leave/unavailability eligibility filter અને Gujarati font path fix.
- Android signing configuration હવે GitHub Actions secrets માગે છે; keystore/password જાહેર repositoryમાં ન મૂકવા.
- Event edit ID, lock guard અને route/time/point બદલાય તો stale allocations clear કરવી.
- Gujarati master checklist અને audit status document.

## સત્યાપિત થયેલી બાબતો
- ZIP archive રચનાત્મક રીતે valid છે.
- `www/index.html`ના 19 inline JavaScript blocks તથા main/preload/native shim scripts માટે Node.js syntax checks PASS.
- APK/EXE workflow YAML parse PASS; package/config JSON parse PASS.
- Gujarati font files હાજર છે અને CSS path `www/assets` સાથે સુસંગત છે.

## હજી સત્યાપિત નથી
- Chromium runtime test આ environmentમાં browser navigation block થવાથી પૂર્ણ ન થયો.
- નવી APK build/physical phone test.
- Windows EXE build/physical Windows test.
- actual duty schemes સાથે same-staff outbound/return pairing behavior અને leave/availability test.
- Gujarati PDF/print rendering on device, share/download, and backup/restore regression.
- દરેક police station boundary અને route pointની official correctness.

**આને સંપૂર્ણ runtime-verified release ન ગણવું.** પહેલા master checklistના section J અને સંબંધિત route/Gujarati/rotation tests પૂર્ણ કરવા.

## 2026-10-16 — પોલીસ સ્ટેશન ફાળવણી હેંગ / બીજા સ્ટેશનની ફાળવણી
- `applyPointDistribution()`માં duty station લખતી વખતે કર્મચારીના મૂળ `station` fieldને overwrite કરવાનું બંધ કર્યું.
- Point rotation history હવે દરેક પોઈન્ટ માટે આખું localStorage history ફરીથી scan/parse કરતી નથી; history એકવાર index થાય છે અને allocation save થયા પછી index refresh થાય છે.
- બધા inline JS blocks syntax-check PASS.
- વાસ્તવિક એપમાં અલગ-અલગ પોલીસ સ્ટેશનની ફાળવણી, જૂના ડેટા સાથે migration અને લાંબી history performance હજી device/runtime પર ચકાસવાની બાકી છે.
- અગાઉના versionથી કર્મચારીનું મૂળ station field પહેલેથી બદલાઈ ગયું હોય તો verified backupમાંથી સાચી station assignment પુનઃસ્થાપિત કરવી પડી શકે છે; allocation logમાંથી મૂળ station ખાતરીપૂર્વક જાણી શકાતું નથી.

## 2026-10-16 — પોલીસ સ્ટેશન ફાળવણી અને નામ દેખાવનો સુધારો
- `PI/PSI/ASI/HC/PC` પોઈન્ટ-વાઈઝ માગણી ઉપલબ્ધ કરી; ગુજરાતી હોદ્દા matching સુધાર્યું.
- ખાલી અથવા `-` સ્ટેશન ધરાવતા ઉપલબ્ધ કર્મચારીઓને shared/unassigned pool તરીકે ગણવામાં આવે છે; સ્પષ્ટ રીતે બીજા સ્ટેશનને સોંપાયેલા કર્મચારીને ઉધાર લેવામાં આવતો નથી.
- રોટેશન helper માં employee object બદલે stable employee-key મોકલવાની ખામી સુધારી, જેથી એક જ કર્મચારી બે પોઈન્ટ/સ્ટેશન પર ફરીથી ફાળવાઈ ન જાય.
- સ્ટેશનવાર યાદી અને દૈનિક શેડ્યૂલ હવે દરેક પોઈન્ટની multi-person ફાળવણી વાંચે છે; માત્ર પ્રથમ નામ બતાવવાની જૂની મર્યાદા દૂર કરી.
- કૃત્રિમ regression test: બે અલગ સ્ટેશનની multi-rank ફાળવણી પાસ; duplicate કર્મચારી નહીં; બીજા સ્ટેશનના સ્પષ્ટ માલિકીના સ્ટાફનો ઉપયોગ નહીં.
- મર્યાદા: વાસ્તવિક ફોન પર APK/EXE ચલાવી પરીક્ષણ હજુ બાકી છે.


## 2026-10-16 — સ્ટેશન માંગણી / ઓટો રોટેશન બોર્ડ follow-up
- બોર્ડમાં PI ને rank તરીકે ઉમેર્યો; point-wise માંગણી, ઉપલબ્ધ સ્ટાફ ગણતરી, કાર્ડ ટોટલ અને ફાળવણીમાં PI સમાવાયો.
- OK દબાવતી વખતે point-wise માંગણીમાંથી PI સંખ્યા ગુમ થતી હતી; હવે saved card અને point plan સુધી PI માંગણી જળવાય છે.
- પસંદ કરેલા સ્ટેશન માટે station-aware eligibility લાગુ કરી: સ્પષ્ટ રીતે બીજા સ્ટેશનને સોંપાયેલ કર્મચારી આ સ્ટેશનમાં આપોઆપ લેવામાં નહીં આવે; ખાલી અથવા '-' સ્ટેશનવાળા ઉપલબ્ધ કર્મચારીઓ shared pool તરીકે રહી શકે છે.
- રોટેશન અને manual substitute પસંદગીમાં પણ એ જ eligibility filter વપરાય છે.
- બે સ્ટેશનના synthetic eligibility test, shared-pool test, PI rank-match, ZIP integrity અને JavaScript syntax checks PASS.
- હજી બાકી: વાસ્તવિક ફોનમાં OK પછી નામ દેખાવાની end-to-end ચકાસણી અને નવી APK/EXE build. આ ZIP ને physical-device verified ગણવી નહીં.

## 2026-10-16 — સ્ટેશન માંગણી / ઓટો રોટેશન બોર્ડ follow-up correction
- બોર્ડના મૂળ rank groups PSI, ASI, HC અને PC જ રાખ્યા છે; PI ઉમેરવું આ સુધારાની માંગણી નહોતી.
- અગાઉના follow-up ZIPમાં PI ઉમેરતાં point-plan rendererમાં PI માટેની array બનાવાઈ નહોતી. આ અસંગતતાથી allocation પછી board render કરતી વખતે JavaScript error આવી શકે અને નામ દેખાતા અટકી શકે. આ PI ફેરફાર પાછો હટાવ્યો.
- પસંદ કરેલા સ્ટેશન માટે station-aware eligibility લાગુ છે: સ્પષ્ટ રીતે બીજા સ્ટેશનને સોંપાયેલ કર્મચારી આ સ્ટેશનમાં આપોઆપ લેવામાં નહીં આવે; ખાલી અથવા '-' સ્ટેશનવાળા ઉપલબ્ધ કર્મચારીઓ shared pool તરીકે રહી શકે છે.
- રોટેશન અને manual substitute પસંદગીમાં પણ એ જ eligibility filter વપરાય છે.
- હજી બાકી: syntax/archive ચકાસણી પછી વાસ્તવિક ફોનમાં OK પછી નામ દેખાવાની અને 🔄 દ્વારા બધા પાત્ર કર્મચારીઓ સુધી રોટેશનની end-to-end ચકાસણી. આ ZIP ને physical-device verified ગણવી નહીં.
