# PROTOCOL-SAKHA — માસ્ટર જરૂરિયાત અને અંતિમ ઓડિટ ચેકલિસ્ટ

**તારીખ:** 16-10-2026  
**હેતુ:** હાલની કાર્યરત એપ/ડિઝાઇન જાળવીને જરૂરી સુધારાઓ અને પરીક્ષણો માટે એક જ સત્તાવાર યાદી.  
**મહત્વની નોંધ:** આ ZIPમાં સોર્સ કોડ અને નીચે દર્શાવેલા સુધારા છે. વાસ્તવિક Android ફોન પર APK ઇન્સ્ટોલ કરીને અને Windows EXE ચલાવીને પરીક્ષણ કર્યા વગર “બધું 100% પૂર્ણ/ચકાસાયેલ” ગણવું નહીં.

## A. હાલની એપ અને બેકવર્ડ-કમ્પેટિબિલિટી
- [ ] મૂળ ZIP/ફાઇલોનું હેશ અને બેકઅપ રાખવો.
- [ ] હાલની ડિઝાઇન, લોગો, રંગો, નેવિગેશન અને કાર્યરત સુવિધાઓ જાળવવી.
- [ ] કર્મચારી, પોલીસ સ્ટેશન, રૂટ, પોઇન્ટ, ડ્યુટી, રજા, રોટેશન, બેકઅપ/રિસ્ટોર, PDF, શેરિંગ, રિપોર્ટ, Help/Support અને Error Monitoring જેવી હાલની સુવિધાઓની regression test કરવી.
- [ ] જૂના localStorage ડેટાનું migration/restore ચકાસવું; જૂનો ડેટા મિટાવવો નહીં.
- [ ] ZIP ખૂલતી હોય, ફાઇલો સંપૂર્ણ હોય અને APK/EXE build workflow ફાઇલો હાજર હોય તે ચકાસવું.

## B. રૂટ અને પોલીસ સ્ટેશનની હદ
- [ ] કાયમી/સાચવેલા રૂટ પસંદ કરી તેના પોઇન્ટ ફરી ઉપયોગ કરી શકાય.
- [ ] નવો રૂટ બનાવી નામ, દિશા/શરૂઆત-અંત અને સંબંધિત પોલીસ સ્ટેશનની હદ પસંદ કરી શકાય. (ફોર્મમાં રૂટ નામ/શરૂઆત/અંત ઉમેર્યાં; runtime test બાકી.)
- [ ] રૂટમાં પોઇન્ટ ક્રમવાર ટાઇપ/ઉમેરવા, સુધારવા, દૂર કરવા અને ભવિષ્ય માટે સેવ કરવા.
- [ ] એક જ રૂટમાં એકથી વધુ પોલીસ સ્ટેશનની હદ આવતી હોય તો દરેક પોઇન્ટની સાચી હદ અલગ સેટ/દેખાડવી. (પોઇન્ટ માટે jurisdiction selector ઉમેર્યો; અધિકૃત route data અને runtime test બાકી.)
- [ ] રૂટની હદ/પોઇન્ટમાં ફેરફાર થાય ત્યારે જૂની સ્કીમ/ડ્યુટી અનિચ્છિત રીતે overwrite ન થાય.
- [ ] Duplicate route/point સામે ચેતવણી અને deletion પહેલાં snapshot/confirmation.
- [ ] રૂટ અને પોઇન્ટનું નામ/ક્રમ સત્તાવાર સ્કીમ સાથે સરખાવવું.
- [ ] અમદાવાદ તરફના એપની હદ બહારના પોઇન્ટ ઉમેરવા નહીં; ઉદાહરણરૂપ આ એપના બંદોબસ્તનો અંતિમ લાગુ પડતો વિસ્તાર Apollo Bridge સુધી છે, ત્યારપછીના અમદાવાદ-સાઇડ પોઇન્ટ બહાર રાખવા.
- [ ] વાસ્તવિક jurisdiction boundaries/point data અધિકૃત રીતે ચકાસીને જ ભરવા. એપમાં route data manually configure થાય છે; માત્ર route-name પરથી ભૂગોળીય હદની સ્વતંત્ર ખાતરી થતી નથી.

## C. આવવા-જવાના રૂટ અને CM/Governor/દિગ્ગજ કાર્યક્રમ
- [ ] જવાનો અને પરતનો રૂટ/પોઇન્ટ અલગ યાદી તરીકે રાખવા.
- [ ] CM, રાજ્યપાલ અને અન્ય મહાનુભાવ માટે દરેક કાર્યક્રમ/દિવસના વાસ્તવિક માર્ગ પ્રમાણે અલગ event/movement બનાવી શકાય.
- [ ] એક જ દિવસે અનેક સ્થળો/legs હોય તો દરેક leg માટે તારીખ, સમય, શરૂઆત/અંત, સ્થળ, દિશા, રૂટ, પોઇન્ટ અને સ્ટાફ અલગ સચવાય.
- [ ] સામાન્ય રોજિંદી route duty અને ખાસ movement bandobast અલગ રહે; એકબીજાને overwrite ન કરે.
- [ ] સમાન movement group ધરાવતા Going અને Return events માટે પરતના allocation સમયે જવાના eventના ફાળવેલા કર્મચારીઓને એ જ rank-ક્રમમાં જાળવવાનો પ્રયત્ન થાય.
- [ ] કર્મચારી રજા/અનુપલબ્ધ હોય, rank ન મેળ ખાતો હોય અથવા સમય અથડાય તો યોગ્ય વિકલ્પ પસંદ થાય અને substitution નોંધાય.
- [ ] manual substitution પહેલાં કારણ ફરજિયાત લખાવવું; મૂળ નામ, નવું નામ અને કારણ history/audit logમાં રહે.
- [ ] ખાસ કાર્યક્રમનું finalise/lock, unlock, copy, version history અને unassigned staff રિપોર્ટ ચકાસવા.
- [ ] એક જ કર્મચારીની બે ફરજો સમય પ્રમાણે અથડાય તો ચેતવણી; non-overlap હોય તો જ ફરી ફાળવણી વિચારવી.

## D. પોઇન્ટ પર સ્ટાફ સંખ્યા અને રેન્ક
- [ ] દરેક પોઇન્ટ માટે PI/PSI/ASI/HC/PC વગેરે રેન્ક પ્રમાણે જરૂરી સંખ્યા અલગ નક્કી કરી શકાય.
- [ ] એક પોઇન્ટ પર એકથી વધુ કર્મચારી અને જુદા જુદા rank mix (જેમ કે PSI + PC અથવા બે PC) શક્ય.
- [ ] પોઇન્ટના નામ સાથે jurisdiction police station દેખાય.
- [ ] auto allocationમાં કર્મચારીનો વાસ્તવિક rank, availability, leave/training અને સમય-અથડામણ તપાસાય. (leave/unavailability filter source-level સુધાર્યો; runtime scenario test બાકી.)
- [ ] જરૂરી સંખ્યામાં કર્મચારી ન મળે તો મૌનથી ખાલી ન રાખે; unassigned/shortage બતાવે.
- [ ] કર્મચારીની ઓળખ બકલ નંબર/મોબાઇલ/નામને normalize કરીને duplicate identity અટકાવવી.
- [ ] એક જ કર્મચારી એક eventમાં એકથી વધુ પોઇન્ટ પર ફાળવાઈ ન જાય.
- [ ] supervisor/overall road bandobast assignment અલગ દર્શાવવાની જરૂરિયાત વપરાશકર્તા સાથે ચકાસવી.

## E. રોટેશન 🔁
- [ ] દરેક rank/category માટે તમામ પાત્ર કર્મચારીઓમાં ક્રમવાર રોટેશન; માત્ર બે જૂથ વચ્ચે ફેરફાર નહીં.
- [ ] રોટેશન દરેક point/route/assignment માટે શક્ય હોય ત્યાં સ્વતંત્ર રહે.
- [ ] વર્તમાન allocation અને સમગ્ર rotation history ધ્યાનમાં લેવાય; અગાઉના logs કાઢી નાખીને ચક્ર ફરી શરૂ ન થાય.
- [ ] રજા, training, અન્ય duty અને unavailable કર્મચારી rotationમાંથી બહાર રહે.
- [ ] એક જ કર્મચારીની ઓળખ વિવિધ digit/phone/buckle formatsથી duplicate ન ગણાય.
- [ ] દરેક rotation પછી નવા નામ, અગાઉના નામ અને allocation history તપાસી શકાય.

## F. ગુજરાતી લખાણ, ફોન્ટ અને પ્રિન્ટ
- [ ] ગુજરાતી Unicode, માત્રા, અડધા અક્ષર અને જોડાક્ષર યોગ્ય render થાય.
- [ ] ટાઇપ કરેલા શબ્દ અને સેવ થયેલા શબ્દમાં ફેરફાર ન થાય; Unicode normalization તપાસવી.
- [ ] Android WebView, Windows/desktop અને browserમાં ગુજરાતી text input/rendering તપાસવું.
- [ ] PDF, print, download, WhatsApp/share outputમાં એ જ ગુજરાતી લખાણ દેખાય.
- [ ] ફોન્ટ ફાઇલ app packageમાં સામેલ/યોગ્ય રીતે લોડ થાય; external network પર આધાર ન રહે.
- [ ] લાંબી સ્કીમમાં page break, repeated table headings, margins, page number, date/time, signature/remarks જગ્યા તપાસવી.
- [ ] ફોન, બકલ નંબર અને ગુજરાતી/અંગ્રેજી અંકો બંનેનું પરીક્ષણ.

## G. PDF, Export, Sharing અને Reports
- [ ] સત્તાવાર bandobast-style reportમાં event, date/time, VIP, direction, route, point, jurisdiction, rank, name, buckle, phone, police station અને remarks જરૂર મુજબ આવે.
- [ ] PDF export offline સ્થિતિમાં પણ શક્ય હોય અથવા સ્પષ્ટ error બતાવે.
- [ ] Android પર file save/share અને Windows EXE download/export ચકાસવું.
- [ ] Excel-compatible CSV export/importમાં Gujarati, commas, quotes અને newline safe handling તપાસવી.
- [ ] unassigned staff, conflict report, duty-load summary અને allocation version history ચકાસવા.

## H. ડેટા, બેકઅપ અને સુરક્ષા
- [ ] મજબૂત password/PIN login, failed-login temporary lockout અને manual logout.
- [ ] auto-lock તથા background/app switch પર sensitive-screen hiding/blur.
- [ ] local sensitive data/storage અને backup encryption.
- [ ] automatic cloud sync નહીં; analytics/tracking નહીં, જ્યાં સુધી અલગથી મંજૂરી ન હોય.
- [ ] authenticated/verified export અને restore; restore પહેલાં confirmation.
- [ ] clipboard protection અને notificationsમાં sensitive duty details નહીં.
- [ ] source/configuration અને operational data અલગ રાખવા; APK/EXEમાં hard-coded secrets/keys નહીં.
- [ ] security/error logsમાં sensitive program details ન લખાય.
- [ ] delete/reset અને route/point deletion પહેલાં confirmation/snapshot.
- [ ] backupsમાંથી restore, reinstall/migration અને corrupt backup handling ચકાસવું.
- [ ] 100% hack-proof હોવાનો દાવો ન કરવો; security test અને limitation નોંધવી.

## I. Dashboard, શોધ અને વપરાશ સરળતા
- [ ] આજની ડ્યુટી, કાર્યક્રમ, route/point coverage, unassigned અને conflict summary.
- [ ] કર્મચારી, rank, station, route, point, date અને event પ્રમાણે search/filter.
- [ ] સામાન્ય કામ ઓછા પગલાંમાં થાય; mobile screen અને desktop બંનેમાં responsive layout.
- [ ] error message Gujaratiમાં સમજાય અને શક્ય હોય ત્યારે recovery સૂચવે.
- [ ] performance મોટી employee list/long route/long event scheme પર ચકાસવી.

## J. અંતિમ QA અને રિલીઝ
- [ ] JavaScript syntax checks.
- [ ] APK GitHub Actions build અને artifact તપાસ.
- [ ] EXE GitHub Actions build અને artifact તપાસ.
- [ ] actual Android phone પર install/update, login, Gujarati input, route point, rotation, backup, PDF, share અને app restart પછી data persistence ચકાસવું.
- [ ] Windows પર EXE launch, font, route editor, export, backup/restore અને data persistence ચકાસવું.
- [ ] old working features માટે regression checklist પૂર્ણ કરવી.
- [ ] તમામ critical/high issues બંધ થયા પછી જ release-ready ગણવું.

## આ ZIPમાં આ તબક્કે કરેલા કોડ ફેરફારો
1. કાર્યક્રમ ફોર્મમાં movement group field ઉમેર્યું, જેથી Going/Return event ને એક જ movement સાથે જોડવાની સુવિધા મળે.
2. Return event allocate કરતી વખતે સમાન તારીખ, VIP અને movement group ધરાવતા Going eventના allocation ને rank-order પ્રમાણે જાળવવાનો પ્રયત્ન ઉમેર્યો.
3. મૂળ કર્મચારી unavailable/leave/conflict હોય તો વિકલ્પ પસંદ કરવાની હાલની logic સાથે pairing fallback જોડ્યો; pairing ન મળે તો સૂચના આપે.
4. Event Plannerમાં સાચવેલા point dropdown સાથે manually typed point ઉમેરવાની, નવો કાયમી route (નામ/શરૂઆત/અંત) બનાવવાની અને checkboxથી route/point સેવ કરવાની સુવિધા ઉમેરાઈ.
5. દરેક પોઇન્ટ માટે route-owner stationથી અલગ jurisdiction police station પસંદ કરવાની સુવિધા ઉમેરાઈ.
6. Auto-allocationમાં રજા/અનુપલબ્ધ સમયને eligibility ચકાસણીમાં સામેલ કર્યો; પહેલાની duplicate leave-check પણ એક જ helperનો ઉપયોગ કરે છે.
5. Event point માટે route owner અને point jurisdiction અલગ રાખવાનો પ્રયાસ ઉમેર્યો.
6. Event edit માટે existing ID જાળવી, locked event editing અટકાવી, route/time/point ફેરફાર થાય ત્યારે જૂની allocations clear કરીને ફરી allocate કરવાનું કહે છે.
7. Manual substitute માટે કારણ પૂછે અને version/audit logમાં નોંધે.
8. હાલની rotation-cycle, Gujarati font assets, APK/PDF/share workflows અને અન્ય source files જાળવી છે.

## આ સુધારાઓ પછી ચલાવેલા checks
- 19 inline JavaScript blocks તથા main/preload/native shim scripts: Node.js syntax PASS.
- APK/EXE workflow YAML: YAML parse PASS.
- package.json અને capacitor.config.json: JSON parse PASS.
- ZIP structure અને ZIP CRC: PASS (આ આવૃત્તિ પેક કર્યા પછી ફરી ચકાસવાનું).
- Chromium runtime test કરવાનો પ્રયાસ થયો, પરંતુ આ environment એ browser navigation block કર્યું; તેથી UI/runtime behaviorને PASS ગણ્યું નથી.

## બાકીનું વાસ્તવિક પરીક્ષણ / ડેટા-આધારિત કામ
- વાસ્તવિક ફોન પર નવા APKનું installation અને runtime test હજી કરવાનું છે.
- Windows EXEનું actual runtime test હજી કરવાનું છે.
- CM/રાજ્યપાલના વાસ્તવિક રૂટ અને દરેક pointની jurisdiction અધિકૃત રીતે ભરવી/ચકાસવી જરૂરી છે; ZIPમાંથી સાચા point names/route boundaries આપમેળે જાણી શકાતા નથી.
- Going/Return allocation pairing rank-order આધારિત છે; દરેક specific outbound point અને matching return point માટે એક-એક જવાનની જોડી બાંધવી હોય તો real schemes સાથે વધુ field testing કરવી.
- PDF print preview, Gujarati conjuncts, file share, backup/restore અને existing featuresની સંપૂર્ણ regression test કર્યા પછી જ final production release કરવો.

## પોલીસ સ્ટેશન ફાળવણી માટે વધારાની રિગ્રેશન ચકાસણી (2026-10-16)
- [x] PI/PSI/ASI/HC/PC ની માંગણી પ્રમાણે બહુ-કર્મચારી ફાળવણીનો synthetic test.
- [x] અલગ બે સ્ટેશન પર અલગ માંગણી સાથે ફાળવણીનો synthetic test.
- [x] ખાલી/`-` સ્ટેશન ધરાવતા shared pool કર્મચારીઓ માટે eligibility.
- [x] સ્પષ્ટ રીતે બીજા સ્ટેશનને સોંપાયેલા કર્મચારીને અન્ય સ્ટેશનમાં ન વાપરવાની ચકાસણી.
- [x] એક જ કર્મચારીને બે પોઈન્ટ/સ્ટેશનમાં ડુપ્લિકેટ ન કરવાની ચકાસણી.
- [x] સ્ટેશનવાર યાદી અને દૈનિક શેડ્યૂલમાં તમામ multi-person નામ દેખાવાની source logic સુધારેલી.
- [ ] વાસ્તવિક Android APK પર તમામ 11 સ્ટેશન, હાજર/રજા સ્ટાફ, ખાલી જગ્યા અને મોટા ડેટા સાથે પરીક્ષણ.
