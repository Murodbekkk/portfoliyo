from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("tools", "Vositalar"),
    ]

    name = models.CharField("Nomi", max_length=60)
    category = models.CharField("Turkum", max_length=20, choices=CATEGORY_CHOICES, default="backend")
    level = models.PositiveSmallIntegerField("Daraja (0-100)", default=80)
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField("Sarlavha", max_length=120)
    slug = models.SlugField("Slug", max_length=140, unique=True)
    summary = models.CharField("Qisqacha tavsif", max_length=220)
    description = models.TextField("To'liq tavsif", blank=True)
    tech_stack = models.CharField("Texnologiyalar (vergul bilan)", max_length=200, help_text="Masalan: Django, PostgreSQL, Vue.js")
    image = models.ImageField("Rasm", upload_to="projects/", blank=True, null=True)
    repo_url = models.URLField("Manba kod (GitHub)", blank=True)
    live_url = models.URLField("Jonli havola", blank=True)
    featured = models.BooleanField("Asosiy loyihami?", default=False)
    order = models.PositiveIntegerField("Tartib", default=0)
    created_at = models.DateField("Yaratilgan sana", auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]


class Experience(models.Model):
    role = models.CharField("Lavozim", max_length=120)
    company = models.CharField("Tashkilot", max_length=120)
    start_date = models.CharField("Boshlanish", max_length=30, help_text="Masalan: 2023-yil yanvar")
    end_date = models.CharField("Tugash", max_length=30, blank=True, help_text="Bo'sh qoldirilsa 'Hozirgacha' deb chiqadi")
    description = models.TextField("Tavsif")
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Tajriba"
        verbose_name_plural = "Ish tajribasi"

    def __str__(self):
        return f"{self.role} — {self.company}"


class Profile(models.Model):
    full_name = models.CharField("F.I.Sh", max_length=120, default="Ismingiz Familiyangiz")
    title = models.CharField("Kasbiy unvon", max_length=160, default="Backend dasturchi")
    tagline = models.CharField("Qisqa shior", max_length=200, blank=True)
    about = models.TextField("O'zim haqimda")
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Telefon", max_length=30, blank=True)
    location = models.CharField("Manzil", max_length=100, blank=True)
    github = models.URLField("GitHub", blank=True)
    linkedin = models.URLField("LinkedIn", blank=True)
    telegram = models.URLField("Telegram", blank=True)
    resume = models.FileField("Rezyume (PDF)", upload_to="resume/", blank=True, null=True)
    avatar = models.ImageField("Profil rasmi", upload_to="profile/", blank=True, null=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactMessage(models.Model):
    name = models.CharField("Ism", max_length=100)
    email = models.EmailField("Email")
    subject = models.CharField("Mavzu", max_length=150, blank=True)
    message = models.TextField("Xabar")
    created_at = models.DateTimeField("Yuborilgan sana", auto_now_add=True)
    is_read = models.BooleanField("O'qilganmi", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.name} — {self.subject or 'Mavzusiz'}"
