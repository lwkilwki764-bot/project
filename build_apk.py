import os
import sys
import subprocess

def print_header(title):
    print("=" * 60)
    print(f"   {title}")
    print("=" * 60)

def main():
    print_header("أداة تحزيم وبناء تطبيق مؤسسة الباقيات الصالحات (APK Builder)")

    print("\n[1/3] فحص البيئة والمكتبات المطلوب...")
    try:
        import flet
        print("✓ مكتبة Flet متوفرة بنجاح.")
    except ImportError:
        print("x مكتبة Flet غير مثبتة. يرجى تثبيتها عبر: pip install flet")
        sys.exit(1)

    print("\n[2/3] فحص كود C++ والمحرك الأصلي...")
    cpp_files = ["src/DatabaseManager.cpp", "src/AuthManager.cpp", "src/SubscriptionEngine.cpp", "src/ServicesManager.cpp"]
    all_exist = all(os.path.exists(f) for f in cpp_files)
    if all_exist:
        print("✓ ملفات المحرك C++ متوفرة بالكامل ومصممة بنجاح.")
    else:
        print("x بعض ملفات C++ مفقودة.")

    print("\n[3/3] تعليمات بناء واستخراج ملف الـ APK للأندرويد:")
    print("---------------------------------------------------------")
    print("يمكنك استخراج ملف الـ APK بنجاح بأحد الطرق التالية:\n")
    print("الطريقة الأولى (الأسهل عبر السطر الإشاري):")
    print("  افتح الموجه الشريطي في مجلد المشروع واكتب:")
    print("  flet build apk --project-name baqiyat_salihat app/main_app.py\n")
    print("الطريقة الثانية (عبر Google Colab مجاناً دون تثبيت أدوات على جهازك):")
    print("  1. ارفع مجلد المشروع على Google Colab.")
    print("  2. نفّذ الأمر التالي في خلية Colab:")
    print("     !pip install flet")
    print("     !flet build apk app/main_app.py")
    print("  3. ستجد ملف app-release.apk جاهز للتحميل والتثبيت على الهاتف والنشر على Google Play!\n")

if __name__ == "__main__":
    main()
