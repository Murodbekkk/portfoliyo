# Portfoliyo — Django + HTML/CSS/JS

Shaxsiy portfoliyo sayti. Backend **Django (Python)** da, frontend **HTML, CSS va JavaScript** da yozilgan. Barcha kontent (loyihalar, ko'nikmalar, tajriba, profil ma'lumotlari) admin panel orqali boshqariladi — kodga tegmasdan yangilash mumkin.

## Nimalar bor?

- **Bosh sahifa**: hero (animatsiyali "terminal" bloki), men haqimda, ko'nikmalar, ish tajribasi (timeline), loyihalar galereyasi, bog'lanish formasi.
- **Loyiha sahifasi**: har bir loyiha uchun alohida batafsil sahifa (`/loyiha/<slug>/`).
- **Admin panel** (`/admin/`): profil, ko'nikmalar, loyihalar, tajriba va kelgan xabarlarni boshqarish.
- **Bog'lanish formasi**: yuborilgan xabarlar bazaga saqlanadi, admin panelda ko'rinadi.
- Responsiv dizayn (mobil, planshet, desktop), scroll-animatsiyalar, `prefers-reduced-motion` hurmat qilinadi.

## O'rnatish va ishga tushirish

1. Virtual muhit yarating (tavsiya etiladi):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Kerakli paketlarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```

3. Ma'lumotlar bazasini tayyorlang:
   ```bash
   python manage.py migrate
   ```

4. (Ixtiyoriy, lekin tavsiya etiladi) Namunaviy ma'lumotlar bilan to'ldirish:
   ```bash
   python manage.py seed_demo
   ```
   Bu buyruq profil, ko'nikmalar, loyihalar va tajribani demo ma'lumotlar bilan to'ldiradi — sayt qanday ko'rinishini darhol ko'rasiz. Keyinchalik ularni admin panel orqali o'zingiznikiga almashtirasiz.

5. Admin foydalanuvchi yarating (o'z ma'lumotlaringizni kiritish uchun):
   ```bash
   python manage.py createsuperuser
   ```

6. Serverni ishga tushiring:
   ```bash
   python manage.py runserver
   ```

7. Brauzerda oching:
   - Sayt: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## O'z ma'lumotlaringizni kiritish

Admin panelga kiring (`/admin/`) va quyidagilarni to'ldiring:

- **Profil** — ismingiz, kasbingiz, o'zingiz haqingizda matn, email/telefon, ijtimoiy tarmoq havolalari, rezyume (PDF) va profil rasmi.
- **Ko'nikmalar** — har biri uchun nomi, turkumi (Backend/Frontend/Vositalar) va foiz darajasi.
- **Loyihalar** — sarlavha, qisqa va to'liq tavsif, texnologiyalar (vergul bilan ajratib), rasm, GitHub va jonli havola.
- **Ish tajribasi** — lavozim, tashkilot, sana va tavsif.

Barcha o'zgarishlar saytda darhol aks etadi — kod fayllarini o'zgartirish shart emas.

## Loyihaning tuzilishi

```
portfolio_project/
├── manage.py
├── requirements.txt
├── portfolio_project/       # loyiha sozlamalari (settings, urls)
└── main/                    # asosiy ilova
    ├── models.py            # Profile, Skill, Project, Experience, ContactMessage
    ├── views.py             # bosh sahifa va loyiha sahifasi
    ├── forms.py             # bog'lanish formasi
    ├── admin.py             # admin panel sozlamalari
    ├── templates/main/      # HTML shablonlar
    ├── static/main/css/     # style.css — dizayn tizimi
    ├── static/main/js/      # script.js — animatsiya va interaktivlik
    └── management/commands/seed_demo.py   # demo ma'lumot yuklovchi
```

## Production'ga chiqarishdan oldin

- `portfolio_project/settings.py` faylida `DEBUG = False` qiling va `ALLOWED_HOSTS` ga domeningizni yozing.
- `SECRET_KEY` ni maxfiy saqlang (muhit o'zgaruvchisiga chiqaring).
- Statik fayllarni yig'ish: `python manage.py collectstatic`.
- Haqiqiy email yuborish uchun `EMAIL_BACKEND` ni SMTP xizmatiga sozlang (hozir xabarlar faqat bazaga saqlanadi va admin panelda ko'rinadi).
