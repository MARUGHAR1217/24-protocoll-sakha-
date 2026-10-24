PROTOCOL SAKHA — APK અને EXE બનાવવાની માર્ગદર્શિકા

1) GitHub પર શક્ય હોય તો Private repository બનાવો. Source files upload કરતાં પહેલાં protocol-sakha.keystore ક્યારેય repositoryમાં upload/commit ન કરો.
2) APK signing માટે repository Settings → Secrets and variables → Actions માં નીચેના secrets ઉમેરો:
   - PDR_KEYSTORE_BASE64: protocol-sakha.keystore ફાઇલનું Base64 લખાણ
   - PDR_KEYSTORE_PASSWORD: keystore નો હાલનો password
   - PDR_KEY_ALIAS: keystore નો હાલનો key alias
   - PDR_KEY_PASSWORD: તે alias નો હાલનો password
   Base64 બનાવવા: Windows PowerShell માં `[Convert]::ToBase64String([IO.File]::ReadAllBytes("protocol-sakha.keystore"))` ચલાવો; આખું output `PDR_KEYSTORE_BASE64` secretમાં મૂકો. Linux/macOS પર `base64 -w 0 protocol-sakha.keystore` વાપરી શકાય.
   Android signing key ગુમાવશો નહીં; એ જ key જૂની APK ઉપર update માટે જરૂરી છે.
3) Actions → “Build PROTOCOL SAKHA APK” → Run workflow. સફળ થયા પછી PROTOCOL-SAKHA-apk artifact ડાઉનલોડ કરો.
4) Actions → “Build PROTOCOL SAKHA EXE” → Run workflow. સફળ થયા પછી PROTOCOL-SAKHA-exe artifact ડાઉનલોડ કરો.
5) APK/EXE install/run કર્યા પછી ગુજરાતી લખાણ, route points, rotation, PDF/share, backup/restore અને જૂના ડેટાનું પરીક્ષણ કરો.

સુરક્ષા નોંધ: keystore, passwords અથવા operational duty data જાહેર repositoryમાં ન મૂકો. APK/EXEનું build સફળ થવું એ physical-device runtime testનું સ્થાન લેતું નથી.
