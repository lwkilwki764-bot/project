# 🏛️ الدليل البرمجي الاحترافي الرسمي لتجميع ملف APK و AAB لتطبيق مؤسسة الباقيات الصالحات

أهلاً بك! هذا هو الدليل الهندسي المعتمد لدى شركات ومطوري التطبيقات العالمية لاستخراج ملف **APK** و **AAB** (Android App Bundle) أصلية وموقّعة برمجياً.

---

## 🚀 الطريقة الأولى (الأكثر احترافية): التجميع التلقائي عبر خوادم GitHub Actions (CI/CD)

هذه هي الطريقة الرسمية المعتمدة عالمياً لدى فرق المطورين (تتميز بأنها مجانية، وتستخدم خوادم فائقة السرعة معزولة بنظام Linux و Android SDK/NDK):

### الخطوات:
1. قم بإنشاء مستودع (Repository) جديد على حسابك في [GitHub](https://github.com).
2. ارفع كود هذا المشروع كاملاً إلى المستودع.
3. بمجرد رفع الكود، ستبدأ خوادم GitHub تلقائياً بتشغيل ملف خط الإنتاج الذي أنشأناه لك:
   `.github/workflows/build_apk.yml`
4. خلال بضع دقائق، ستنتهي العملية وستجد ملف الـ **`app-release.apk`** جاهزاً في تبويب **Actions** للتنزيل المباشر!

---

## 🛠️ الطريقة الثانية: التجميع عبر أداة Buildozer (Native NDK Pipeline)

تعتمد هذه الطريقة على ملف المواصفات الرسمي `buildozer.spec` الذي قمنا بإنشائه:

1. افتح بيئة **Linux / WSL / Google Colab**.
2. ثبّت الأداة والأذونات:
   ```bash
   pip install buildozer cython
   sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev
   ```
3. شغّل أمر التجميع المباشر:
   ```bash
   buildozer -v android debug
   ```
4. سيتولى المحرك تنزيل **Android NDK** وتجميع ملفات الـ **C++** واستخراج ملف الـ APK داخل مجلد `bin/`.

---

## 🔑 الطريقة الثالثة: التوقيع الرقمي (Release Signing) للنشر في Google Play

لنشر التطبيق رسمياً في متجر Google Play Console:

1. **توليد مفتاح التوقيع الرقمي**:
   ```bash
   keytool -genkey -v -keystore release.keystore -alias baqiyat_key -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **توقيع وتفعيل الحزمة المعتمدة (`.aab`)**:
   ```bash
   jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore release.keystore build/app-release.aab baqiyat_key
   ```

3. **الرفع للمتجر**:
   رفع ملف `.aab` الموقّع إلى حساب المطور الخاص بك في **Google Play Console**.
