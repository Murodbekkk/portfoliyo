from django.core.management.base import BaseCommand
from main.models import Profile, Skill, Project, Experience


class Command(BaseCommand):
    help = "Portfoliyoni namunaviy (demo) ma'lumotlar bilan to'ldiradi"

    def handle(self, *args, **options):
        profile = Profile.load()
        profile.full_name = "Aziz Karimov"
        profile.title = "Python / Django dasturchi"
        profile.tagline = "Ishlaydigan, sinovdan o'tgan va toza kod yozaman — g'oyadan production'gacha."
        profile.about = (
            "Salom! Men 3 yildan beri backend yo'nalishida ishlayman, asosan Python va Django "
            "ekotizimi bilan. REST API'lar qurish, ma'lumotlar bazasini loyihalash va "
            "loyihalarni production muhitiga chiqarish menga qiziq. Yangi texnologiyalarni "
            "o'rganishni va murakkab masalalarni sodda yechimlar bilan hal qilishni yaxshi ko'raman."
        )
        profile.email = "aziz@example.com"
        profile.phone = "+998 90 123 45 67"
        profile.location = "Toshkent, O'zbekiston"
        profile.github = "https://github.com/"
        profile.linkedin = "https://linkedin.com/"
        profile.telegram = "https://t.me/"
        profile.save()

        Skill.objects.all().delete()
        skills = [
            ("Python", "backend", 95),
            ("Django / DRF", "backend", 92),
            ("PostgreSQL", "backend", 85),
            ("Docker", "backend", 78),
            ("HTML / CSS", "frontend", 88),
            ("JavaScript", "frontend", 75),
            ("Vue.js", "frontend", 60),
            ("Git", "tools", 90),
            ("Linux", "tools", 80),
            ("CI/CD", "tools", 70),
        ]
        for i, (name, cat, level) in enumerate(skills):
            Skill.objects.create(name=name, category=cat, level=level, order=i)

        Project.objects.all().delete()
        projects = [
            dict(
                title="TaskFlow — vazifalarni boshqarish",
                slug="taskflow",
                summary="Jamoalar uchun Kanban uslubidagi vazifa boshqaruv tizimi.",
                description="Django REST Framework asosida qurilgan backend va Vue.js frontendga ega, real vaqtda yangilanuvchi vazifa boshqaruv platformasi. JWT autentifikatsiya va WebSocket bildirishnomalari qo'llab-quvvatlanadi.",
                tech_stack="Django, DRF, PostgreSQL, Vue.js, Docker",
                featured=True,
                order=0,
            ),
            dict(
                title="ShopEasy — onlayn do'kon",
                slug="shopeasy",
                summary="To'liq funksional e-commerce platforma, to'lov tizimi integratsiyasi bilan.",
                description="Mahsulotlar katalogi, savat, buyurtma va to'lov (Payme/Click) integratsiyasi. Admin panel orqali mahsulotlarni boshqarish imkoniyati.",
                tech_stack="Django, PostgreSQL, Redis, Celery, JS",
                featured=True,
                order=1,
            ),
            dict(
                title="BlogCraft — shaxsiy blog platformasi",
                slug="blogcraft",
                summary="Markdown qo'llab-quvvatlovchi, tezkor va SEO-optimallashtirilgan blog dvigateli.",
                description="Foydalanuvchilar maqola yozish, teglash va izoh qoldirish imkoniyatiga ega. Sahifalash va qidiruv funksiyalari mavjud.",
                tech_stack="Django, SQLite, HTML, CSS, JS",
                featured=False,
                order=2,
            ),
        ]
        for p in projects:
            Project.objects.create(**p)

        Experience.objects.all().delete()
        experiences = [
            dict(
                role="Backend dasturchi",
                company="TechNova LLC",
                start_date="2024-yil mart",
                end_date="",
                description="Django asosida mikroservislar arxitekturasini loyihalash va qo'llab-quvvatlash, jamoa bilan Agile metodologiyasida ishlash.",
                order=0,
            ),
            dict(
                role="Junior Python dasturchi",
                company="Freelance",
                start_date="2022-yil iyun",
                end_date="2024-yil fevral",
                description="Mijozlar uchun kichik va o'rta hajmdagi veb-ilovalar yaratish, REST API'lar qurish.",
                order=1,
            ),
        ]
        for e in experiences:
            Experience.objects.create(**e)

        self.stdout.write(self.style.SUCCESS("Demo ma'lumotlar muvaffaqiyatli qo'shildi!"))
