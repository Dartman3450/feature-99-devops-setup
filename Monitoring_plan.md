Rencana Pemantauan & Logging Aplikasi Voting (Produksi)

Tujuan dari rencana ini adalah untuk memastikan observabilitas penuh pada aplikasi voting, yang terdiri dari tiga komponen utama: Vote App (Front/Backend), Redis (Cache/Broker), dan Worker (Processor).

Kami akan menggunakan stack Prometheus & Grafana (P&G) yang merupakan standar industri untuk pemantauan berbasis metrik.

1. Alat Observability Utama

Komponen

Tujuan

Alat yang Digunakan

Metrik (Metrics)

Mengumpulkan data kinerja time-series dari semua komponen.

Prometheus (Pengumpul/Penyimpanan Metrik)

Visualisasi & Alert

Menampilkan metrik dalam bentuk dashboard dan memicu peringatan.

Grafana (Visualisasi)

Logging

Mengumpulkan, menganalisis, dan mencari log dari semua container.

Promtail & Loki (Sistem Aggregasi Log)

2. Metrik Kritis dan Target (Metrics & SLOs)

Kami akan fokus pada 4 Metrik Emas dari SRE (Latency, Traffic, Errors, Saturation) untuk setiap komponen.

A. Vote App (Frontend/Backend)

Ini adalah container yang menerima input dari pengguna.

Metrik

Tujuan (Alerting)

Latency (Layanan)

Waktu respons API.

Traffic (QPS)

Queries Per Second (jumlah vote baru).

Errors (HTTP)

Tingkat kesalahan HTTP (terutama 5xx).

B. Redis (Cache/Database)

Ini adalah komponen vital untuk menyimpan hasil vote sementara.

Metrik

Tujuan (Alerting)

Memory Usage

Persentase memori yang digunakan Redis.

Uptime / Health

Status running Redis.

Hit Ratio

Persentase cache hit vs miss.

C. Worker (Processor)

Worker memproses hasil vote dari Redis ke database utama.

Metrik

Tujuan (Alerting)

Queue Length

Jumlah vote yang menunggu untuk diproses di antrean Redis.

Processing Time

Waktu yang dibutuhkan worker untuk memproses satu vote.

Worker Count

Jumlah instance worker yang berjalan.

3. Contoh Konfigurasi Prometheus dan Grafana

A. Konfigurasi Prometheus (pseudocode prometheus.yml)

Prometheus dikonfigurasi untuk scrape (mengambil) metrik dari setiap komponen.

# Prometheus Configuration (Target Discovery)
scrape_configs:
  # 1. Memantau Prometheus itu sendiri
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # 2. Memantau Vote App (asumsikan terekspos di port 8080)
  - job_name: 'vote_app'
    metrics_path: '/metrics' # Endpoint yang diekspos oleh aplikasi
    static_configs:
      - targets: ['vote-app-instance-1:8080', 'vote-app-instance-2:8080']

  # 3. Memantau Worker (asumsikan terekspos di port 8081)
  - job_name: 'worker'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['worker-instance-1:8081']

  # 4. Memantau Redis (menggunakan exporter)
  - job_name: 'redis'
    static_configs:
      - targets: ['redis-exporter:9121'] # Redis memerlukan node_exporter


B. Grafana Alert (Contoh PromQL)

Berikut adalah contoh query Prometheus Query Language (PromQL) yang akan digunakan dalam Grafana untuk memicu alert jika vote menumpuk:

# ALERT: High Vote Queue Length
# Pemicu jika rata-rata antrean (length) melebihi 1000 item selama 5 menit
ALERTS:
  - alert: CriticalVoteQueueBacklog
    expr: avg_over_time(redis_queue_length[5m]) > 1000
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Antrean voting Redis memiliki > 1000 item selama 5 menit."
      description: "Worker mungkin macet atau tidak berjalan cukup cepat untuk memproses voting."
