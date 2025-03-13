# Website PPribadi

Website pribadi untuk menampilkan profil profesional, proyek-proyek AI/ML, pengembangan web, dan tulisan tentang berbagai topik termasuk sains, filsafat, AI, dan sastra.

## Gambaran Proyek

Proyek ini terdiri dari dua komponen utama:

1. **Backend API**: API berbasis Django REST Framework yang menyediakan data untuk bagian portofolio, profil, dan blog.
2. **Frontend**: Antarmuka HTML, CSS (Bootstrap), dan JavaScript yang mengkonsumsi API.

## Teknologi yang Digunakan

### Backend
- **Framework**: Django + Django REST Framework
- **Bahasa**: Python
- **Database**: PostgreSQL
- **Kontainerisasi**: Docker

### Frontend
- **HTML/CSS/JS**: Teknologi web dasar
- **Framework CSS**: Bootstrap
- **JavaScript**: Vanilla JS dengan jQuery untuk konsumsi API

## Fitur

- **Profil/CV**: Latar belakang profesional, pendidikan, keahlian, dan pengalaman
- **Portofolio**: 
  - Proyek AI dan Machine Learning
  - Pengembangan web
  - Penelitian dan publikasi
- **Blog**: 
  - Artikel tentang berbagai topik (Sains, Filsafat, AI, Sastra)
  - Sistem kategori dan tag

## Struktur Proyek

```
personal-portfolio/
├── backend/                # Django REST API
├── frontend/               # Frontend HTML/CSS/JS
└── docker/                 # Konfigurasi Docker
```

## Memulai

### Prasyarat
- Python 3.10+
- PostgreSQL
- Node.js dan npm (opsional, untuk alat pengembangan frontend)
- Docker dan Docker Compose (opsional, untuk deployment kontainer)

### Setup Backend

```bash
# Clone repository
git clone https://github.com/username-anda/personal-portfolio.git
cd personal-portfolio/backend

# Buat dan aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate

# Install dependensi
pip install -r requirements.txt

# Siapkan variabel lingkungan
cp .env.example .env
# Edit file .env dengan kredensial database Anda

# Jalankan migrasi
python manage.py migrate

# Buat superuser
python manage.py createsuperuser

# Jalankan server pengembangan
python manage.py runserver
```

### Setup Frontend

```bash
cd personal-portfolio/frontend

# Jika menggunakan npm untuk alat apa pun
npm install

# Buka index.html di browser Anda atau gunakan server lokal
```

### Setup Docker (Opsional)

```bash
cd personal-portfolio

# Build dan jalankan container
docker-compose up -d
```

## Endpoint API

- `/api/profile/` - Informasi profil dan CV
- `/api/portfolio/projects/` - Proyek portofolio
- `/api/portfolio/publications/` - Publikasi
- `/api/blog/posts/` - Postingan blog
- `/api/blog/categories/` - Kategori blog

## Deployment

### Backend
API backend di-deploy di [Railway/Render] dengan database PostgreSQL.

### Frontend
Frontend di-deploy di [Netlify].

## Roadmap Pengembangan

- [x] Struktur proyek awal
- [ ] Pengembangan API Backend
- [ ] Pengembangan antarmuka Frontend
- [ ] Kontainerisasi Docker
- [ ] Setup pipeline CI/CD
- [ ] Deployment produksi

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detailnya.

## Kontak

Nama Anda - [email.anda@example.com](mailto:email.anda@example.com)

Link Proyek: [https://github.com/username-anda/personal-portfolio](https://github.com/username-anda/personal-portfolio)
