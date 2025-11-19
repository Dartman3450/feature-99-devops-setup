Rencana Pemantauan & Logging Aplikasi Voting (Produksi)

Tujuan dari rencana plan ini adalah untuk bisa memantau 3 komponen penting dalam aplikasi voting yakni Vote,Redis,Worker dengan alat pemantauan / observasi yang biasa digunakan dalam dunia industri.

Pada planning kali ini rencananya akan menggunakan prometheus dan grafana sebagai standard untuk memantau metric metric tiap komponen

Untuk alat utama:
Metrik -> Mengumpulkan data kinerja tiap komponen dalam aplikasi dengan prometheus sebagai penyimpan datanya
Visualisasi -> menampilkan data metrik menggunakan dashboard grafana 
Logging -> mengumpulkan setiap error dan debug dari aplikasi dengan menggunakan sistem agregasi log

Metrik yang digunakan untuk memantau 3 komponen utama yaitu (redis , vote app , dan worker.

Vote app
Response latency -> Memantau seberapa cepat aplikasi merespon pada permintaan voting dari user , penting karena bila aplikasi lemot maka user bisa komplain
Error rate -> Memantau persentase kode atau sistem yang bisa error saat aplikasi sedang berjalan atau beroperasi , penting agar tau dan bisa dihandle langsung jika aplikasi mengalami error
Traffic(QPS) -> Memeriksa jumlah permintaan voting yang masuk dari aplikasi , berguna untuk mendata banyak responden yang melakukan voting

Redis (cache) Semacam tempat penyimpananan sementara berbasis kontainer
Uptime -> mengecek apakah kontainer / tempat penyimpanan berkerja secara optimal
Queue length -> Memonitoring jumlah vote yang mengantri untuk disimpan di redis
Memory usage-> Memonitoring banyaknya ram yang dipakai oleh redis serta berguna untuk mencegah ram kehabisan memory karena dipantau langsung

Worker (processor) yang mengelola vote
Processing time -> Memantau dan mengecek waktu yang diperlukan worker untuk mengelola votingan user 
Worker health ->  Mengecek status worker hidup atau nyala , penting untuk mengetahui jika worker berjalan dengan optimal dalam mengelola votenya

Rencana alerting sederhana untuk bisa menotify bila ada error yang terjadi atau kesalahan dalam sistem app atau komponen utamanya
Conditioning -> Memberikan kondisi dimana bila ditemukan dalam redis terdapat lebih dari 500 item belum dikelola atau diproses oleh worker selama misalnya 5 menit maka dia akan mengirimkan notifikasi kalau ada worker yang mati atau terjadi kesalahan dalam sistem kategori : parah.

pseudo code:
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
