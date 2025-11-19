99 Group Role challenge Devops
Michael yuvi - 2702228545 Binus@Bandung

Pada proyek repo yang saya fork dari ketentuan challenge yaitu berasal dari repositori https://github.com/dockersamples/example-voting-app dimana saya akan mendemonstrasikan implementasi CI/CD pipeline basic , containerization , Infrastructure code dengan menggunakan terraform , dan konsep untuk memonitoring appnya agar berjalan dengan optimal dan lancar.

Setup dan deployment
pastikan sudah mendownload perangkat lunak tersebut di laptop/pc anda :
- GIT bash
- Docker dan docker compose
- Terraform

Pertama membuat CI.YML untuk version control dan sebagai basic CI/CD git dan workflows
- Langkah pertama yang saya lakukan adalah membuka repo https://github.com/dockersamples/example-voting-app lalu menfork langsung dan menamainya sebagai feature-99-devops-setup.
- Langkah kedua adalah membuat branch baru dari hasil fork saya di https://github.com/Dartman3450/feature-99-devops-setup yaitu branch untuk melakukan update kode dan perubahan yang akan di lakukan sebelum diteruskan ke main branch saya.
- Langkah ketiga adalah buka git bash lalu ketikkan cd feature-99-devops-setup agar direktori git mengarah ke repositori ini untuk kepentingan push dan commit.
- Langkah keempat adalah membuat file YAML ci.yml CI(Continuous Integration) sebagai penunjuk branch serta sebagai intruksi kapan suatu fungsi berjalan atau ketrigger setiap kali ada PR (Push Request) atau (Pull request) ke branch main selain itu sebagai checkout kode dan instalasi dependensi untuk python , nodejs , dan lain sebagainya.
- Untuk membuat file CI.YAML nya cukup ketik di direktori feature-99-devops-setup "nano .github/workflows/ci.yml" ini akan membuka notepad versi git bash dan tinggal dibuat intruksinya serta simple test command untuk projeknya , sesudah diisi maka tinggal ctrl + 0 untuk write , lalu tekan enter untuk save , dan untuk keluar ctrl + x.
- Setelah file ci.yaml udah dibuat tinggal di commit dan cek action apakah semua sudah centang , bila masih silang bisa jadi antara ada kesalahan syntax atau ada dependensi yang belum di download.
- Setelah ci/cd beres saya langsung lanjutkan ke tahap 2 yaitu containerization dimana saya download dahulu docker dan docker composer langsung dari websitenya yaitu di : https://www.docker.com/ , dimana saya memakai versi AMD64 window karena lebih kompatibel untuk laptop saya.
- Setelah docker di download jangan lupa untuk sign in menggunakan email
- Setelah berhasil download saatnya mengetes dan menjalankan seluruh stack aplikasi voting menggunakan docker.composer.yml
- buka CMD lalu ketikkan "docker login -u (username) anda , setelah enter akan ditanya password , password itu sebenarnya adalah token yang harus kalian generate di website dockernya yaitu ke app.docker -> setting -> PAT Lalu generate tokennya lalu di proyek saya sekarang saya bash docker build -t michaelyuvi1405/example-voting-vote:latest vote/ untuk repository di dockernya lalu docker push michaelyuvi1405/example-voting-vote:latest untuk tempat membuat kontainernya.
- Setelah generate tokennya tinggal copy paste ke CMD , tulisan tidak keliatan karena untuk keamanan pastikan tidak ada typo dan lain lain , setelah login succeed tinggal bash "docker compose up --build -d" dan 
- Setelah berhasil kebuild bisa di cek melalui bash " docker ps" disinilah list semua daftar containernya.
- Ketika composer sudah running lancar tinggal cek file docker.composer.yml untuk localhostnya , dalam proyek ini localhost saya agak mengikuti dari repo asli yaitu "localhost:8081"
- Kalau mau dihentikan tinggal bash "docker composer down"
- Setelah itu saya mencoba terraform , dimana saya mendownloadnya dari website : https://developer.hashicorp.com/terraform/install#windows untuk window
- Setelah terdownload saya buat folder di D dengan nama devtools lalu saya masukkan hasil ekstrak zipnya yaitu terraform.exe ke dalam folder devtools.
- Sebelum inisiasi terraform jangan lupa membuat folder terraform di folder feature-99-devops-setup dan isinya adalah provider.tf dan main.tf cukup buat dari txt document
- Setelah itu saya buka CMD dan change directory ke feature-99-devops-setup di disc C saya lalu bash D:\Devtools\Terraform init
- Terraform akan membaca file main dan provider kita , jika error cek di explorer di atas -> view -> file name extension -> hapus txtnya dan yes in ketika ada notifikasi file tidak akan bekerja.
- Setelah terraform ke inisiasi maka terraform akan membaca file main dan provider lalu menyiapkan semua yang dibutuhkan untuk berinteraksi dengan infrstruktur docker saya
- Disini saya menggunakan provider lokal docker untuk mencoba terraform.
- Setelah itu bash "terraform plan" dimana dia akan mengecek setiap perubahan yang ada dan ringkasan resource yg perlu di add
- Setelah terraform apply --auto approve untuk menyimpan dan menyetujui perubahan yang dilakukan \
- setelah beres jangan lupa bash "docker compose down" untuk menghemat resource serta bash "terraform destroy --auto approve agar redis tidak kehilangan kendali.

Penjelasan mengapa saya menggunakan software ini :
Github -> Saya menggunakan github action karena sebelumnya saya sering menggunakannya untuk push sama commit tugas proyek sama untuk fortofolio jadi saya lumayan agak familiar dengan github action 
Docker -> sudah pasti jadi ketentuan devops jadi saya wajib harus pelajari agar lebih familiar dan tau apa yang harus dilakukan
Terraform -> menurut saya lumayan beginner friendly dan lumayan simpel serta terraform baru pernah saya denger pas nonton youtube jadi saya agak penasaran ingin mencobanya.
Local docker -> Memakai lokal docker untuk mengaktifkan terraform plan karena lebih simpel.

Improvement yang akan saya lakukan :
- Improvement yang akan lebih saya lakukan adalah mempelajari seluk beluk devops , mulai dari teori hingga prakteknya lebih 
- Review cloud dan mempelajari cloud untuk keperluan devops nantinya
- Mempelajari lebih mengenai CI/CD Pipeline
- Mempelajari konsep lebih mendalam mengenai containerization
