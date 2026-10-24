import os, sys

p = 'android/app/build.gradle'
with open(p, encoding='utf-8') as f:
    s = f.read()
required = ['PDR_KEYSTORE_PASSWORD', 'PDR_KEY_ALIAS', 'PDR_KEY_PASSWORD']
missing = [k for k in required if not os.environ.get(k)]
if missing:
    raise SystemExit('Missing GitHub Actions signing secrets: ' + ', '.join(missing))
if not os.path.exists('protocol-sakha.keystore'):
    raise SystemExit('Signing keystore is missing. Configure PDR_KEYSTORE_BASE64 secret.')
if 'signingConfigs.release' not in s:
    sc = '''    signingConfigs {
        release {
            storeFile file("../../protocol-sakha.keystore")
            storePassword System.getenv("PDR_KEYSTORE_PASSWORD")
            keyAlias System.getenv("PDR_KEY_ALIAS")
            keyPassword System.getenv("PDR_KEY_PASSWORD")
        }
    }
    buildTypes {'''
    if 'buildTypes {' not in s:
        raise SystemExit('Could not locate Android buildTypes block')
    s = s.replace('buildTypes {', sc, 1)
    i = s.index('buildTypes {')
    j = s.index('release {', i) + len('release {')
    s = s[:j] + '\n            signingConfig signingConfigs.release' + s[j:]
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
print('Android release signing configured from environment secrets')
