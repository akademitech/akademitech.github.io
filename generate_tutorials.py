import os

template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AkademiTech | {title}</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet">
</head>
<body class="tutorial-page">

    <nav class="navbar scrolled" id="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">
                <i class='bx bxs-graduation'></i> Akademi<span>Tech</span>
            </a>
            <ul class="nav-links">
                <li><a href="index.html#home">Home</a></li>
                <li><a href="index.html#courses">Program</a></li>
            </ul>
        </div>
    </nav>

    <div class="tutorial-layout container">
        <aside class="sidebar glass-panel">
            <h3>Daftar Materi</h3>
            <ul class="sidebar-links">
                <li><a href="pengenalan-dasar.html">1. Pengenalan Dasar HTML</a></li>
                <li><a href="tag-elemen-atribut.html">2. Tag, Elemen, Atribut</a></li>
                <li><a href="teks-paragraf.html">3. Membuat Paragraf</a></li>
                <li><a href="heading-formatting.html">4. Heading & Formatting</a></li>
                <li><a href="membuat-link.html">5. Membuat Link</a></li>
                <li><a href="gambar-tabel.html">6. Gambar dan Tabel</a></li>
                <li><a href="membuat-list.html">7. Membuat List</a></li>
                <li><a href="membuat-form.html">9. Membuat Form</a></li>
                <li><a href="elemen-semantik.html">10. Elemen Semantik</a></li>
                <li><a href="menampilkan-video.html">11. Video pada HTML</a></li>
                <li><a href="menambahkan-audio.html">12. Audio pada HTML</a></li>
                <li><a href="pengenalan-css.html">13. Dasar CSS</a></li>
                <li><a href="selektor-css.html">14. 5 Macam Selektor</a></li>
                <li><a href="project-web.html">15. Project Web</a></li>
            </ul>
        </aside>

        <main class="tutorial-content">
            <section class="tutorial-section glass-panel">
                <h2>{title}</h2>
                {content}
                
                <div style="margin-top: 40px; display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;">
                    <a href="{prev_link}" class="btn btn-secondary" style="{prev_display}">Materi Sebelumnya</a>
                    <a href="{next_link}" class="btn btn-primary" style="{next_display}">Materi Selanjutnya</a>
                </div>
            </section>
        </main>
    </div>
    
    <footer class="footer">
        <div class="container"><div class="footer-bottom"><p>&copy; 2026 AkademiTech Tutorials.</p></div></div>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="js/script.js"></script>
</body>
</html>"""

tutorials = [
    {
        "filename": "pengenalan-dasar.html",
        "title": "Pengenalan Dasar HTML",
        "content": """
        <p>HTML (HyperText Markup Language) adalah fondasi paling dasar dari setiap halaman web. HTML bukan bahasa pemrograman yang memiliki logika seperti if-else atau perulangan, melainkan sebuah <strong>bahasa markup</strong> yang bertugas memberitahu *web browser* (seperti Google Chrome atau Firefox) bagaimana cara menyusun dan menampilkan teks, gambar, dan konten lainnya ke layar.</p>
        
        <h3>Sejarah Singkat HTML</h3>
        <p>HTML pertama kali diciptakan oleh Tim Berners-Lee pada tahun 1991. Sejak saat itu, HTML terus berkembang pesat seiring dengan perkembangan internet. Versi terbaru saat ini adalah HTML5, yang dirilis pada tahun 2014. HTML5 membawa revolusi besar karena mendukung berbagai fitur multimedia modern seperti pemutaran video dan audio tanpa memerlukan *plugin* tambahan seperti Flash Player.</p>

        <h3>Struktur Dasar Dokumen HTML</h3>
        <p>Untuk membuat file HTML, Anda harus menyimpannya dengan ekstensi <code>.html</code> (misalnya <code>index.html</code>). Di dalam file tersebut, Anda harus menuliskan kerangka dasar yang menjadi standar wajib agar website dapat dibaca dengan benar oleh browser.</p>
        
        <div class='code-block'>
            <div class="code-header"><span>index.html</span></div>
            <pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="id"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Halaman Pertamaku&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Halo, Selamat Datang di Dunia Web!&lt;/h1&gt;
    &lt;p&gt;Ini adalah kalimat pertama yang saya tampilkan di web.&lt;/p&gt;
    &lt;p&gt;Saya sedang belajar membuat website dari nol.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </div>
        
        <h3>Penjelasan Anatomi Kode:</h3>
        <ul class="custom-list">
            <li><strong><code>&lt;!DOCTYPE html&gt;</code>:</strong> Ini adalah deklarasi tipe dokumen. Tag ini sangat penting untuk memberi tahu browser bahwa kita menggunakan spesifikasi HTML5 terbaru.</li>
            <li><strong><code>&lt;html lang="id"&gt;</code>:</strong> Merupakan elemen akar (root). Semua kode HTML dibungkus di sini. Atribut <code>lang="id"</code> menandakan bahwa bahasa utama website ini adalah bahasa Indonesia, yang sangat membantu Mesin Pencari (Google) dan aplikasi pembaca layar.</li>
            <li><strong><code>&lt;head&gt;</code>:</strong> Bagian kepala ini berisi informasi *meta-data*. Apapun yang ditulis di dalam head (kecuali title) <strong>tidak akan tampil di layar browser</strong>. Di sinilah kita meletakkan deskripsi web, memanggil file CSS, dan file Javascript.</li>
            <li><strong><code>&lt;meta charset="UTF-8"&gt;</code>:</strong> Menentukan jenis karakter (encoding) yang digunakan, UTF-8 mencakup hampir semua karakter dan simbol di dunia.</li>
            <li><strong><code>&lt;meta name="viewport"&gt;</code>:</strong> Memastikan website terlihat baik (*responsive*) saat dibuka di perangkat *mobile* (smartphone).</li>
            <li><strong><code>&lt;title&gt;</code>:</strong> Judul halaman yang akan muncul di tab (jendela) atas browser Anda, sekaligus menjadi judul yang tampil di hasil pencarian Google.</li>
            <li><strong><code>&lt;body&gt;</code>:</strong> Bagian tubuh (*body*) inilah yang merupakan kanvas utama Anda. Semua teks, gambar, tabel, dan video yang ingin dilihat oleh pengunjung web harus dimasukkan ke dalam area ini.</li>
        </ul>
        
        <div class='info-box'>
            <i class='bx bx-check-shield'></i>
            <p><strong>Tips Praktis:</strong> Jika Anda menggunakan kode editor *Visual Studio Code*, Anda bisa langsung mengetikkan tanda seru <code>!</code> lalu menekan tombol <strong>Tab</strong> atau <strong>Enter</strong> untuk menghasilkan kerangka dasar HTML5 ini secara otomatis tanpa harus mengetiknya satu per satu.</p>
        </div>
        """
    },
    {
        "filename": "tag-elemen-atribut.html",
        "title": "Tag, Elemen, dan Atribut dalam HTML",
        "content": """
        <p>Sebelum kita mulai membuat komponen-komponen website, kita harus memahami tata bahasa (sintaks) dasar dari HTML. Secara keseluruhan, HTML dibangun di atas tiga konsep utama: Tag, Elemen, dan Atribut.</p>
        
        <h3>1. Apa itu Tag HTML?</h3>
        <p>Tag adalah penanda yang memberi instruksi kepada browser bagaimana cara menampilkan sebuah teks atau media. Tag selalu dibungkus dengan tanda kurung siku (kurung sudut) <code>&lt; &gt;</code>. Umumnya, tag hadir secara berpasangan, yakni <strong>tag pembuka</strong> dan <strong>tag penutup</strong> (yang ditandai dengan tambahan garis miring <code>/</code>).</p>
        
        <div class='code-block'>
            <pre><code>&lt;p&gt;Ini adalah teks di dalam tag pembuka dan penutup.&lt;/p&gt;
&lt;h1&gt;Ini adalah judul&lt;/h1&gt;</code></pre>
        </div>
        
        <p>Beberapa tag khusus tidak memerlukan penutup dan disebut sebagai <strong>Self-closing tags</strong> (Tag mandiri) atau <strong>Empty Elements</strong>. Contohnya adalah <code>&lt;img&gt;</code> untuk gambar, <code>&lt;br&gt;</code> untuk enter baris, dan <code>&lt;hr&gt;</code> untuk garis horizontal.</p>

        <h3>2. Apa itu Elemen HTML?</h3>
        <p>Banyak pemula yang tertukar antara Tag dan Elemen. <strong>Elemen</strong> adalah keseluruhan satu kesatuan objek HTML dari awal hingga akhir, yang mencakup: Tag Pembuka + Isi Konten + Tag Penutup.</p>
        
        <p>Sebagai contoh, perhatikan kode berikut: <code>&lt;h1&gt;Selamat Datang&lt;/h1&gt;</code>.</p>
        <ul class="custom-list">
            <li><code>&lt;h1&gt;</code> adalah Tag Pembuka.</li>
            <li>"Selamat Datang" adalah Konten.</li>
            <li><code>&lt;/h1&gt;</code> adalah Tag Penutup.</li>
            <li><strong>Keseluruhan baris tersebut</strong> disebut sebagai satu Elemen Heading.</li>
        </ul>
        
        <h4>Elemen Bersarang (Nested Elements)</h4>
        <p>Elemen HTML bisa (dan akan selalu) berisi elemen HTML lainnya di dalamnya. Ini disebut *Nested Elements*. Contohnya, kita menaruh elemen <code>&lt;b&gt;</code> (bold) di dalam elemen <code>&lt;p&gt;</code> (paragraf).</p>
        
        <div class='code-block'>
            <pre><code>&lt;p&gt;Kalimat ini memiliki kata &lt;b&gt;yang ditebalkan&lt;/b&gt; di tengahnya.&lt;/p&gt;</code></pre>
        </div>

        <h3>3. Apa itu Atribut HTML?</h3>
        <p>Atribut adalah semacam "bumbu tambahan" yang disematkan ke dalam elemen untuk memberikan <strong>informasi, karakteristik, atau pengaturan tambahan</strong>. Aturan penulisan atribut adalah:</p>
        <ol class="custom-list numbered">
            <li>Atribut <strong>hanya</strong> ditulis di dalam <strong>tag pembuka</strong>, tidak pernah di tag penutup.</li>
            <li>Atribut umumnya berpasangan antara <code>nama</code> dan <code>nilai</code> yang dipisahkan sama dengan.</li>
            <li>Nilai atribut wajib diapit oleh tanda kutip ganda <code>" "</code> atau kutip tunggal <code>' '</code>.</li>
        </ol>
        
        <div class='code-block'>
            <pre><code>&lt;!-- href adalah atribut, URL adalah nilainya --&gt;
&lt;a href="https://google.com"&gt;Pergi ke Google&lt;/a&gt;

&lt;!-- id dan class adalah atribut. width dan height mengatur ukuran --&gt;
&lt;img src="foto.jpg" alt="Foto Kucing" width="300" height="200" class="foto-bulat" id="foto1"&gt;</code></pre>
        </div>
        
        <div class='info-box'>
            <i class='bx bx-info-circle'></i>
            <p><strong>Core Attributes:</strong> Ada atribut tertentu yang bisa digunakan di hampir semua tag HTML, yang paling populer adalah <code>class</code>, <code>id</code>, <code>style</code>, dan <code>title</code>.</p>
        </div>
        """
    },
    {
        "filename": "teks-paragraf.html",
        "title": "Membuat Teks dan Paragraf di HTML",
        "content": """
        <p>Lebih dari 80% isi dari website modern adalah teks. Memahami cara mengelola dan menampilkan teks yang baik di HTML adalah langkah krusial untuk membuat website yang informatif.</p>
        
        <h3>Membuat Paragraf dengan Tag <code>&lt;p&gt;</code></h3>
        <p>Paragraf didefinisikan dengan menggunakan tag <code>&lt;p&gt;</code>. Browser akan otomatis membuatkan sedikit jarak vertikal (*margin bottom & top*) antara satu paragraf dengan paragraf lainnya agar mudah dibaca.</p>

        <div class='code-block'>
            <pre><code>&lt;p&gt;Ini adalah paragraf pertama. Membahas tentang pengantar web programming.&lt;/p&gt;
&lt;p&gt;Ini adalah paragraf kedua. Berisi materi lanjutan dari modul sebelumnya.&lt;/p&gt;</code></pre>
        </div>
        
        <p><strong>Penting:</strong> Di dalam HTML, Anda tidak bisa sekadar menekan tombol 'Enter' atau spasi panjang di kode editor Anda untuk mengubah tampilan. Browser HTML akan <strong>mengabaikan</strong> semua spasi ganda dan *enter* berturut-turut, dan menjadikannya hanya satu spasi saja.</p>

        <h3>Membuat Baris Baru dengan <code>&lt;br&gt;</code></h3>
        <p>Lalu bagaimana jika kita menulis alamat atau puisi, di mana kita butuh baris baru (*line break*) tetapi tidak ingin membuat paragraf yang baru (karena jarak paragraf terlalu lebar)? Solusinya adalah menggunakan tag <code>&lt;br&gt;</code> (Break).</p>
        
        <div class='code-block'>
            <pre><code>&lt;p&gt;
    PT. AkademiTech Digital Nusantara&lt;br&gt;
    Gedung Cyber, Lantai 5&lt;br&gt;
    Jalan Kuningan Barat, Jakarta Selatan
&lt;/p&gt;</code></pre>
        </div>
        
        <p>Perhatikan bahwa <code>&lt;br&gt;</code> adalah *empty tag*, sehingga ia tidak memerlukan tag penutup seperti <code>&lt;/br&gt;</code>.</p>

        <h3>Menjaga Format Teks Asli dengan <code>&lt;pre&gt;</code></h3>
        <p>Ada kalanya kita benar-benar ingin browser menghormati setiap tombol Enter dan Spasi yang kita ketikkan di kode. Biasanya ini digunakan saat menampilkan kode program komputer di website. Kita menggunakan tag <code>&lt;pre&gt;</code> (Preformatted Text).</p>
        
        <div class='code-block'>
            <pre><code>&lt;pre&gt;
function sapa(nama) {
    console.log("Halo, " + nama);
}

sapa("Budi");
&lt;/pre&gt;</code></pre>
        </div>
        
        <p>Teks di dalam <code>&lt;pre&gt;</code> umumnya akan ditampilkan menggunakan jenis font *monospace* (ukuran huruf sama lebarnya) seperti Courier New.</p>
        
        <h3>Memisahkan Konten dengan <code>&lt;hr&gt;</code></h3>
        <p>Tag <code>&lt;hr&gt;</code> (Horizontal Rule) digunakan untuk membuat garis lurus mendatar yang memisahkan bagian-bagian tertentu di halaman Anda. Ini juga merupakan *empty tag*.</p>
        """
    },
    {
        "filename": "heading-formatting.html",
        "title": "Heading, Komentar, dan Text Formatting",
        "content": """
        <h3>Menggunakan Heading (Judul)</h3>
        <p>Sama seperti saat membaca koran, sebuah website membutuhkan hirarki Judul dan Sub-judul agar mudah dipindai oleh mata pembaca. HTML menyediakan 6 tingkatan heading, mulai dari <code>&lt;h1&gt;</code> hingga <code>&lt;h6&gt;</code>.</p>

        <div class='code-block'>
            <pre><code>&lt;h1&gt;Judul Artikel Paling Utama (h1)&lt;/h1&gt;
&lt;h2&gt;Sub-judul Level 2 (h2)&lt;/h2&gt;
&lt;h3&gt;Sub-judul Level 3 (h3)&lt;/h3&gt;
&lt;h4&gt;Level 4 (h4)&lt;/h4&gt;
&lt;h5&gt;Level 5 (h5)&lt;/h5&gt;
&lt;h6&gt;Level 6 (Terkecil)&lt;/h6&gt;</code></pre>
        </div>
        
        <div class='info-box'>
            <i class='bx bx-search-alt-2'></i>
            <p><strong>Praktek SEO yang Baik:</strong> Google (Mesin Pencari) sangat memperhatikan tag Heading. Pastikan halaman web Anda <strong>hanya memiliki satu buah <code>&lt;h1&gt;</code></strong> yang menjelaskan secara menyeluruh tentang isi halaman tersebut. Sisanya, gunakan h2, h3, dan seterusnya secara terstruktur layaknya daftar isi buku.</p>
        </div>

        <h3>Memberikan Komentar (Comment) di HTML</h3>
        <p>Komentar adalah baris kode yang hanya bisa dilihat oleh *programmer* (di kode sumber), tetapi <strong>sama sekali tidak akan ditampilkan di layar browser</strong> pengguna. Komentar sangat berguna untuk mendokumentasikan kode atau "mematikan" blok kode sementara waktu saat proses pengujian.</p>
        
        <div class='code-block'>
            <pre><code>&lt;!-- Ini adalah area komentar HTML --&gt;
&lt;!-- Bagian di bawah ini adalah Menu Header --&gt;
&lt;div class="header"&gt;
    &lt;h1&gt;Logo Saya&lt;/h1&gt;
&lt;/div&gt;

&lt;!-- &lt;p&gt;Paragraf ini tidak akan dirender oleh browser&lt;/p&gt; --&gt;</code></pre>
        </div>

        <h3>Text Formatting (Memformat Teks)</h3>
        <p>Bosan dengan teks biasa? HTML menyediakan banyak tag (disebut tag pemformatan) untuk mengubah gaya teks, sama seperti fitur *Bold* atau *Italic* di Microsoft Word.</p>
        
        <ul class='custom-list'>
            <li><code>&lt;b&gt;</code> dan <code>&lt;strong&gt;</code>: Keduanya menghasilkan <strong>Teks Tebal (Bold)</strong>. Namun, <code>&lt;strong&gt;</code> memberikan makna *semantik* bahwa teks tersebut sangat penting (Berguna untuk *screen reader* penyandang tunanetra).</li>
            <li><code>&lt;i&gt;</code> dan <code>&lt;em&gt;</code>: Menghasilkan <em>Teks Miring (Italic)</em>. Tag <code>&lt;em&gt;</code> memberikan makna penekanan intonasi suara.</li>
            <li><code>&lt;u&gt;</code>: Memberikan <u>Garis Bawah (Underline)</u>.</li>
            <li><code>&lt;mark&gt;</code>: Memberikan warna latar belakang seperti distabilo <mark>Highlight text</mark>.</li>
            <li><code>&lt;del&gt;</code>: Menandai teks yang dihapus atau tidak berlaku lagi. Browser menampilkannya dengan coretan: <del>Harga Lama Rp 100.000</del>.</li>
            <li><code>&lt;ins&gt;</code>: Teks yang baru saja ditambahkan, biasanya berpasangan dengan del: <ins>Harga Baru Rp 50.000</ins>.</li>
            <li><code>&lt;sup&gt;</code>: Superscript. Membuat teks menjadi kecil di atas. Sangat cocok untuk bilangan pangkat: X<sup>2</sup> + Y<sup>2</sup> = Z<sup>2</sup>.</li>
            <li><code>&lt;sub&gt;</code>: Subscript. Membuat teks menjadi kecil di bawah. Cocok untuk rumus kimia: H<sub>2</sub>O.</li>
        </ul>
        """
    },
    {
        "filename": "membuat-link.html",
        "title": "Membuat Link (Tautan) pada HTML",
        "content": """
        <p>World Wide Web (Jaring Laba-Laba Seluruh Dunia) tidak akan pernah ada tanpa yang namanya <strong>Hyperlink</strong>. Link adalah komponen revolusioner yang memungkinkan kita melompat dari satu halaman ke halaman lainnya hanya dengan satu klik.</p>
        
        <h3>Dasar Penggunaan Tag Anchor <code>&lt;a&gt;</code></h3>
        <p>Untuk membuat link, kita menggunakan tag <code>&lt;a&gt;</code> (kependekan dari *anchor* atau jangkar). Syarat mutlak menggunakan tag ini adalah menambahkan atribut <code>href</code> (Hypertext Reference) yang berisi alamat URL tujuan.</p>

        <div class='code-block'>
            <pre><code>&lt;p&gt;Silakan kunjungi &lt;a href="https://google.com"&gt;Mesin Pencari Google&lt;/a&gt; untuk mencari materi.&lt;/p&gt;</code></pre>
        </div>

        <h3>Mengatur Target Link</h3>
        <p>Secara default (bawaan), ketika Anda mengklik link, browser akan memuat halaman tujuan di tab/jendela yang sama, menggantikan halaman saat ini. Seringkali, saat menautkan ke website orang lain, kita ingin link tersebut terbuka di <strong>tab baru</strong> agar pengunjung tidak pergi dari website kita. Gunakan atribut <code>target="_blank"</code>.</p>
        
        <div class='code-block'>
            <pre><code>&lt;a href="https://wikipedia.org" target="_blank"&gt;Buka Wikipedia di Tab Baru&lt;/a&gt;</code></pre>
        </div>

        <h3>Berbagai Macam URL Tujuan (Jenis Link)</h3>
        <p>Atribut <code>href</code> tidak hanya diisi dengan link website utuh. Berikut adalah beberapa variasinya:</p>
        
        <ul class="custom-list">
            <li><strong>Link Absolut (Absolute URL):</strong> Tautan lengkap menuju website di domain lain. Harus dimulai dengan `http://` atau `https://`.<br><code>href="https://facebook.com"</code></li>
            <li><strong>Link Relatif (Relative URL):</strong> Tautan menuju file lain di dalam folder website Anda sendiri. Tidak perlu awalan https.<br><code>href="tentang-kami.html"</code> atau <code>href="pages/kontak.html"</code></li>
            <li><strong>Link Email (Mailto):</strong> Akan otomatis memanggil aplikasi pengirim email (seperti Outlook/Gmail) di komputer/HP pengguna lengkap dengan alamat tujuan.<br><code>href="mailto:admin@website.com"</code></li>
            <li><strong>Link Telepon / Whatsapp:</strong> Memanggil aplikasi panggilan telepon (di HP).<br><code>href="tel:+62812345678"</code></li>
            <li><strong>Link Bookmark (In-Page Link):</strong> Tautan yang tidak pindah halaman, tetapi membuat browser *scroll* melompat ke bagian tertentu di halaman yang sama. Syaratnya, elemen tujuan harus diberi atribut <code>id</code>, lalu link memanggil ID tersebut menggunakan simbol tagar <code>#</code>.<br><code>&lt;a href="#bagian-footer"&gt;Scroll ke Bawah&lt;/a&gt;</code></li>
        </ul>
        """
    },
    {
        "filename": "gambar-tabel.html",
        "title": "Gambar dan Tabel di HTML",
        "content": """
        <h3>1. Menyisipkan Gambar di Halaman Web</h3>
        <p>Halaman web yang hanya berisi teks akan sangat membosankan. Kita membutuhkan elemen visual. Gambar dapat ditambahkan menggunakan tag <code>&lt;img&gt;</code> (Image). Tag ini adalah tag kosong (*empty element*), ia tidak memiliki penutup <code>&lt;/img&gt;</code>.</p>
        
        <p>Tag img membutuhkan dua atribut yang sangat krusial:</p>
        <ul class="custom-list">
            <li><strong><code>src</code> (Source):</strong> Alamat letak file gambar. Bisa berupa link dari internet atau link relatif dari komputer lokal (misal: <code>folder_gambar/foto1.jpg</code>).</li>
            <li><strong><code>alt</code> (Alternative Text):</strong> Teks pengganti yang akan muncul jika gambar gagal dimuat (misal karena koneksi lambat atau file terhapus). Teks alt juga dibaca oleh aplikasi pembaca layar tunanetra dan sangat penting untuk SEO.</li>
        </ul>
        
        <div class='code-block'>
            <pre><code>&lt;!-- Gambar dari lokal --&gt;
&lt;img src="images/foto-profil.jpg" alt="Foto Profil Saya" width="200" height="200"&gt;

&lt;!-- Gambar dari internet --&gt;
&lt;img src="https://source.unsplash.com/random/400x300" alt="Gambar Acak dari Unsplash"&gt;</code></pre>
        </div>
        
        <p><strong>Catatan:</strong> Atribut <code>width</code> (lebar) dan <code>height</code> (tinggi) menentukan ukuran gambar dalam satuan pixel. Meskipun bisa diatur lewat HTML, cara modern yang disarankan adalah menggunakan CSS untuk mengatur ukuran gambar agar lebih responsif.</p>

        <h3>2. Membuat Struktur Tabel yang Rapi</h3>
        <p>Tabel sangat ideal untuk merepresentasikan data dua dimensi (baris dan kolom), seperti jadwal pelajaran, daftar harga, atau laporan nilai. Membuat tabel di HTML gampang-gampang susah karena membutuhkan rangkaian bersarang (*nested*) dari beberapa tag.</p>
        
        <p>Komponen dasar tabel:</p>
        <ul class="custom-list">
            <li><code>&lt;table&gt;</code>: Pembungkus induk keseluruhan tabel.</li>
            <li><code>&lt;tr&gt;</code> (Table Row): Berfungsi untuk membuat <strong>Baris</strong> secara mendatar.</li>
            <li><code>&lt;th&gt;</code> (Table Header): Sel khusus untuk judul kolom. Teks di dalamnya otomatis tebal dan rata tengah.</li>
            <li><code>&lt;td&gt;</code> (Table Data): Sel biasa untuk menampilkan isi data.</li>
        </ul>

        <div class='code-block'>
            <pre><code>&lt;table border="1" cellpadding="10" cellspacing="0" width="100%"&gt;
    &lt;!-- Baris Judul --&gt;
    &lt;tr&gt;
        &lt;th&gt;No&lt;/th&gt;
        &lt;th&gt;Nama Siswa&lt;/th&gt;
        &lt;th&gt;Nilai Ujian&lt;/th&gt;
    &lt;/tr&gt;
    
    &lt;!-- Baris Data 1 --&gt;
    &lt;tr&gt;
        &lt;td&gt;1&lt;/td&gt;
        &lt;td&gt;Andi Syahputra&lt;/td&gt;
        &lt;td&gt;95&lt;/td&gt;
    &lt;/tr&gt;
    
    &lt;!-- Baris Data 2 --&gt;
    &lt;tr&gt;
        &lt;td&gt;2&lt;/td&gt;
        &lt;td&gt;Budi Santoso&lt;/td&gt;
        &lt;td&gt;88&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;</code></pre>
        </div>
        
        <h4>Menggabungkan Sel (Merge Cells)</h4>
        <p>Mirip fitur Merge di Microsoft Excel, kita bisa menggabungkan kolom ke samping dengan atribut <code>colspan="jumlah"</code> dan menggabungkan baris ke bawah dengan <code>rowspan="jumlah"</code> pada elemen <code>&lt;td&gt;</code>.</p>
        """
    },
    {
        "filename": "membuat-list.html",
        "title": "Membuat List (Daftar) di HTML",
        "content": """
        <p>List (daftar) adalah format penyajian data yang sangat umum. Mulai dari daftar bahan makanan, langkah-langkah membuat kue, hingga menu navigasi di bagian atas website, semuanya dibuat menggunakan tag List di HTML.</p>

        <h3>1. Unordered List (Daftar Tidak Berurutan)</h3>
        <p>Digunakan saat urutan (ranking/prioritas) dari daftar tidak memiliki arti penting. Unordered list akan menghasilkan daftar dengan simbol bulat (*bullet point*). Dibungkus dengan tag <code>&lt;ul&gt;</code> dan isi per-itemnya diisi dengan <code>&lt;li&gt;</code> (List Item).</p>
        
        <div class='code-block'>
            <pre><code>&lt;h3&gt;Daftar Belanja Pasar:&lt;/h3&gt;
&lt;ul&gt;
    &lt;li&gt;Sayur Bayam&lt;/li&gt;
    &lt;li&gt;Minyak Goreng 2 Liter&lt;/li&gt;
    &lt;li&gt;Garam Dapur&lt;/li&gt;
    &lt;li&gt;Telur Ayam&lt;/li&gt;
&lt;/ul&gt;</code></pre>
        </div>

        <h3>2. Ordered List (Daftar Berurutan)</h3>
        <p>Digunakan saat urutan daftar adalah sebuah keharusan, misalnya untuk kronologi, ranking juara, atau langkah-langkah panduan (Step-by-step). Browser secara otomatis akan memberikannya penomoran berurut (1, 2, 3). Dibungkus menggunakan tag <code>&lt;ol&gt;</code>.</p>
        
        <div class='code-block'>
            <pre><code>&lt;h3&gt;Cara Membuat Kopi:&lt;/h3&gt;
&lt;ol&gt;
    &lt;li&gt;Siapkan cangkir dan bubuk kopi.&lt;/li&gt;
    &lt;li&gt;Tuang 2 sendok teh kopi ke dalam cangkir.&lt;/li&gt;
    &lt;li&gt;Tuang air panas yang baru mendidih.&lt;/li&gt;
    &lt;li&gt;Aduk merata lalu kopi siap dinikmati.&lt;/li&gt;
&lt;/ol&gt;</code></pre>
        </div>
        
        <p>Anda bisa mengganti penomoran dengan angka romawi atau abjad dengan menambahkan atribut <code>type</code> pada <code>&lt;ol&gt;</code> (Misal: <code>type="A"</code>, <code>type="I"</code>, atau <code>type="a"</code>).</p>

        <h3>3. Description List (Daftar Deskripsi)</h3>
        <p>List jenis ini agak jarang dipakai, namun sangat tepat untuk format tipe Kamus (Dictionary) atau Tanya-Jawab (FAQ). Ia mendaftar sebuah istilah (Term) dan diikuti oleh penjelasan deskripsinya.</p>
        
        <ul class="custom-list">
            <li><code>&lt;dl&gt;</code> (Description List): Membungkus seluruh daftar.</li>
            <li><code>&lt;dt&gt;</code> (Description Term): Istilah/Kata yang ingin dijelaskan.</li>
            <li><code>&lt;dd&gt;</code> (Description Detail): Penjelasan detail dari istilah tersebut. Menjorok ke kanan.</li>
        </ul>
        
        <div class='code-block'>
            <pre><code>&lt;h3&gt;Glosarium Web:&lt;/h3&gt;
&lt;dl&gt;
    &lt;dt&gt;&lt;strong&gt;HTML&lt;/strong&gt;&lt;/dt&gt;
    &lt;dd&gt;Bahasa standar untuk mendefinisikan struktur dan konten website.&lt;/dd&gt;
    
    &lt;dt&gt;&lt;strong&gt;CSS&lt;/strong&gt;&lt;/dt&gt;
    &lt;dd&gt;Bahasa *stylesheet* untuk mengatur warna, jarak, dan layout desain visual HTML.&lt;/dd&gt;
    
    &lt;dt&gt;&lt;strong&gt;JavaScript&lt;/strong&gt;&lt;/dt&gt;
    &lt;dd&gt;Bahasa pemrograman yang membuat website menjadi interaktif dan dinamis.&lt;/dd&gt;
&lt;/dl&gt;</code></pre>
        </div>
        """
    },
    {
        "filename": "membuat-form.html",
        "title": "Membuat Form Lengkap pada HTML",
        "content": """
        <p>Form (Formulir) adalah komponen paling penting untuk mendapatkan masukan data dari pengguna (Input). Mulai dari halaman Login, Registrasi akun, Kolom Pencarian (Search), hingga Checkout belanja di Tokopedia, semuanya dibangun menggunakan Form HTML.</p>

        <h3>Kerangka Utama: <code>&lt;form&gt;</code></h3>
        <p>Setiap kotak input harus dibungkus oleh tag <code>&lt;form&gt;</code>. Tag ini mengontrol kemana data input akan dilempar ke server setelah tombol Submit ditekan.</p>
        <ul class="custom-list">
            <li><strong>Atribut <code>action</code>:</strong> Menentukan lokasi URL/Script yang akan memproses form (contoh: <code>action="proses_login.php"</code>).</li>
            <li><strong>Atribut <code>method</code>:</strong> Metode pengiriman data. <strong>GET</strong> akan melampirkan data ke URL (cocok untuk pencarian), <strong>POST</strong> akan menyembunyikan data (wajib digunakan untuk input rahasia seperti Password).</li>
        </ul>
        
        <h3>Elemen-elemen Input Dasar</h3>
        <p>Sebagian besar interaksi pengguna ditangkap melalui tag <code>&lt;input&gt;</code>. Bentuk kotak input ini bisa berubah drastis hanya dengan mengganti nilai atribut <code>type</code>.</p>
        
        <div class='code-block'>
            <pre><code>&lt;form action="registrasi.php" method="POST"&gt;
    
    &lt;!-- 1. Text (Input Biasa) --&gt;
    &lt;label for="nama_lengkap"&gt;Nama Lengkap:&lt;/label&gt;
    &lt;input type="text" id="nama_lengkap" name="nama" placeholder="Masukkan nama Anda..." required&gt;
    
    &lt;br&gt;&lt;br&gt;

    &lt;!-- 2. Email (Khusus Email, divalidasi otomatis oleh HTML5) --&gt;
    &lt;label for="alamat_email"&gt;Email:&lt;/label&gt;
    &lt;input type="email" id="alamat_email" name="email" required&gt;
    
    &lt;br&gt;&lt;br&gt;

    &lt;!-- 3. Password (Karakter akan disensor menjadi bintang/titik) --&gt;
    &lt;label for="sandi"&gt;Kata Sandi:&lt;/label&gt;
    &lt;input type="password" id="sandi" name="password" minlength="8" required&gt;
    
    &lt;br&gt;&lt;br&gt;

    &lt;!-- 4. Radio Button (Hanya bisa pilih SATU opsi, pastikan atribut 'name' bernilai sama) --&gt;
    &lt;label&gt;Jenis Kelamin:&lt;/label&gt;&lt;br&gt;
    &lt;input type="radio" id="pria" name="gender" value="L"&gt;
    &lt;label for="pria"&gt;Laki-laki&lt;/label&gt;
    &lt;input type="radio" id="wanita" name="gender" value="P"&gt;
    &lt;label for="wanita"&gt;Perempuan&lt;/label&gt;
    
    &lt;br&gt;&lt;br&gt;

    &lt;!-- 5. Checkbox (Bisa memilih BANYAK opsi / Centang) --&gt;
    &lt;label&gt;Hobi:&lt;/label&gt;&lt;br&gt;
    &lt;input type="checkbox" name="hobi1" value="membaca"&gt; Membaca
    &lt;input type="checkbox" name="hobi2" value="olahraga"&gt; Olahraga
    &lt;input type="checkbox" name="hobi3" value="coding" checked&gt; Coding
    
    &lt;br&gt;&lt;br&gt;
    
    &lt;!-- 6. Select (Dropdown pilihan) --&gt;
    &lt;label for="kota"&gt;Kota Asal:&lt;/label&gt;
    &lt;select id="kota" name="kota"&gt;
        &lt;option value=""&gt;-- Pilih Kota --&lt;/option&gt;
        &lt;option value="jakarta"&gt;Jakarta&lt;/option&gt;
        &lt;option value="bandung"&gt;Bandung&lt;/option&gt;
        &lt;option value="surabaya"&gt;Surabaya&lt;/option&gt;
    &lt;/select&gt;

    &lt;br&gt;&lt;br&gt;

    &lt;!-- 7. Textarea (Kolom teks panjang multi-baris) --&gt;
    &lt;label for="alamat"&gt;Alamat Domisili:&lt;/label&gt;&lt;br&gt;
    &lt;textarea id="alamat" name="alamat" rows="4" cols="40" placeholder="Jalan Raya No.1..."&gt;&lt;/textarea&gt;

    &lt;br&gt;&lt;br&gt;

    &lt;!-- 8. Tombol Submit (Memicu pengiriman form) --&gt;
    &lt;button type="submit"&gt;Daftar Sekarang&lt;/button&gt;
    
&lt;/form&gt;</code></pre>
        </div>

        <h3>Membedah Atribut-Atribut Penting di Input:</h3>
        <ul class="custom-list">
            <li><code>name="..."</code>: Atribut PALING PENTING. Variabel pengenal yang digunakan oleh *Server/Backend* untuk mengambil nilai yang diketik *user*.</li>
            <li><code>placeholder="..."</code>: Teks abu-abu sementara (petunjuk) di dalam kotak input yang menghilang saat diketik.</li>
            <li><code>required</code>: Atribut *boolean* (tanpa nilai). Jika disematkan, form tidak akan bisa dikirim sebelum *user* mengisi kolom tersebut.</li>
            <li><code>value="..."</code>: Nilai bawaan (*default*) yang sudah ada di kotak, atau nilai yang diwakili oleh opsi Radio/Checkbox tersebut saat terpilih.</li>
            <li><code>id="..."</code>: Digunakan untuk menghubungkan input dengan labelnya (melalui atribut <code>for</code> pada elemen <code>&lt;label&gt;</code>). Jika label diklik, input akan otomatis mendapat fokus kursor.</li>
        </ul>
        """
    },
    {
        "filename": "elemen-semantik.html",
        "title": "Elemen Semantik HTML5",
        "content": """
        <p>Sebelum lahirnya HTML5, cara programmer mendesain layout (*struktur*) website sangat berantakan. Kita membagi header, kolom isi, dan footer hanya menggunakan satu tag: <code>&lt;div&gt;</code> (Division). Kita membedakannya dengan menambahkan class, misalnya <code>&lt;div class="header"&gt;</code>, <code>&lt;div class="sidebar"&gt;</code>, <code>&lt;div class="footer"&gt;</code>.</p>
        
        <p>Masalahnya, komputer (Google Search Bot dan aplikasi pembaca layar) tidak mengerti apa isi dari <code>&lt;div&gt;</code> tersebut. Bagi mereka, itu hanya sebuah "kotak" biasa tanpa arti.</p>
        
        <h3>Masuklah Konsep Semantik HTML5</h3>
        <p>HTML5 memperkenal elemen <strong>Semantik</strong>. Semantik berarti "memiliki makna". Tag-tag ini tidak hanya berfungsi sebagai kotak layout, tetapi juga <strong>mengomunikasikan makna</strong> dari blok konten tersebut kepada *browser* dan mesin pencari.</p>

        <h3>Daftar Tag Semantik Utama</h3>
        <ul class="custom-list">
            <li><strong><code>&lt;header&gt;</code></strong> : Area kepala. Digunakan untuk membungkus judul situs web, logo, dan menu navigasi.</li>
            <li><strong><code>&lt;nav&gt;</code></strong> : Navigasi utama. Digunakan untuk membungkus kelompok link menu (seperti Home, About, Contact).</li>
            <li><strong><code>&lt;main&gt;</code></strong> : Merupakan penanda konten pokok/utama dari halaman. Hanya boleh ada satu <code>&lt;main&gt;</code> per halaman web.</li>
            <li><strong><code>&lt;section&gt;</code></strong> : Merupakan bagian tematik spesifik dari halaman, biasanya diawali dengan heading (h2/h3). (Misal: Section Tentang Kami, Section Layanan).</li>
            <li><strong><code>&lt;article&gt;</code></strong> : Digunakan untuk membungkus konten independen yang bisa berdiri sendiri (Jika dicabut dari web tersebut dan ditaruh di tempat lain, ia tetap bermakna utuh). Contoh: Postingan Blog, Komentar, Berita.</li>
            <li><strong><code>&lt;aside&gt;</code></strong> : Konten sampingan (Sidebar) yang berkaitan, namun tidak menjadi fokus utama dari halaman. Contoh: Daftar artikel terpopuler, iklan banner.</li>
            <li><strong><code>&lt;footer&gt;</code></strong> : Area kaki halaman. Tempat menaruh informasi Hak Cipta, tautan sosial media, dan informasi kontak.</li>
        </ul>

        <h3>Contoh Implementasi Layout Semantik Lengkap:</h3>
        <div class='code-block'>
            <pre><code>&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;Portal Berita Terkini&lt;/h1&gt;
        &lt;nav&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Politik&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Olahraga&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Teknologi&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/nav&gt;
    &lt;/header&gt;
    
    &lt;main&gt;
        &lt;section id="berita-utama"&gt;
            &lt;h2&gt;Berita Hari Ini&lt;/h2&gt;
            
            &lt;article&gt;
                &lt;h3&gt;Apple Merilis iPhone 20 Pro&lt;/h3&gt;
                &lt;p&gt;Apple kembali membuat kejutan dengan meluncurkan...&lt;/p&gt;
            &lt;/article&gt;
            
            &lt;article&gt;
                &lt;h3&gt;Timnas Menang Telak!&lt;/h3&gt;
                &lt;p&gt;Pertandingan mendebarkan semalam berakhir dengan...&lt;/p&gt;
            &lt;/article&gt;
        &lt;/section&gt;
        
        &lt;aside&gt;
            &lt;h3&gt;Artikel Terpopuler&lt;/h3&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Cara Cepat Belajar HTML&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/aside&gt;
    &lt;/main&gt;
    
    &lt;footer&gt;
        &lt;p&gt;&amp;copy; 2026 Portal Berita. All rights reserved.&lt;/p&gt;
        &lt;a href="privasi.html"&gt;Kebijakan Privasi&lt;/a&gt;
    &lt;/footer&gt;
&lt;/body&gt;</code></pre>
        </div>
        
        <div class='info-box'>
            <i class='bx bx-trophy'></i>
            <p><strong>Keuntungan:</strong> Dengan menggunakan tag semantik, Google (SEO) akan memberikan peringkat yang jauh lebih baik kepada website Anda karena bot mereka dapat merayapi dan memahami struktur konten Anda dengan akurat. Selain itu kode HTML Anda menjadi sangat rapi dan *readable* bagi manusia.</p>
        </div>
        """
    },
    {
        "filename": "menampilkan-video.html",
        "title": "Menampilkan Video pada HTML",
        "content": """
        <p>Sebelum HTML5 lahir, memutar video di browser adalah mimpi buruk. *Developer* harus memaksa pengguna menginstal ekstensi pihak ketiga yang berat dan rentan virus, seperti Adobe Flash Player atau Silverlight. Saat ini, HTML5 menyediakan solusi asli (*native*) lewat elemen <code>&lt;video&gt;</code>.</p>

        <h3>1. Menggunakan Tag <code>&lt;video&gt;</code> Bawaan</h3>
        <p>Anda cukup menyediakan file berformat `.mp4`, `.webm`, atau `.ogg`. Sangat disarankan berformat MP4 karena format inilah yang paling didukung oleh seluruh tipe browser modern.</p>

        <div class='code-block'>
            <pre><code>&lt;video width="600" height="400" controls poster="images/thumbnail-video.jpg"&gt;
    &lt;source src="media/video-pembelajaran-html.mp4" type="video/mp4"&gt;
    &lt;source src="media/video-pembelajaran-html.webm" type="video/webm"&gt;
    &lt;!-- Teks fallback jika browser terlalu jadul --&gt;
    Maaf, browser Anda sudah usang dan tidak mendukung pemutar video HTML5. Silakan perbarui browser Anda.
&lt;/video&gt;</code></pre>
        </div>

        <h4>Membedah Atribut-Atribut Video:</h4>
        <ul class="custom-list">
            <li><strong><code>controls</code></strong>: Atribut wajib. Akan memunculkan panel kendali di video, seperti tombol *Play/Pause*, pengaturan Volume, *Timeline* durasi, dan fitur *Fullscreen*.</li>
            <li><strong><code>autoplay</code></strong>: Akan otomatis memulai pemutaran saat halaman selesai di-*load*. <em>Peringatan: Karena aturan anti-spam, kebanyakan browser memblokir fitur autoplay KECUALI jika video juga diberi atribut <code>muted</code> (bisu/tanpa suara).</em></li>
            <li><strong><code>muted</code></strong>: Membuat volume video diset ke 0 (bisu) secara bawaan.</li>
            <li><strong><code>loop</code></strong>: Ketika video selesai (sampai detik terakhir), akan memutar kembali secara otomatis dari awal terus-menerus.</li>
            <li><strong><code>poster="gambar.jpg"</code></strong>: Ibarat *Thumbnail* YouTube. Ini adalah gambar diam yang ditampilkan *sebelum* video mulai diputar atau saat sedang di-*buffering*.</li>
        </ul>

        <h3>2. Menanamkan Video YouTube (Embedding)</h3>
        <p>Bagi website berskala kecil, menyimpan file MP4 (yang berukuran puluhan hingga ratusan Megabyte) secara langsung di server akan membuat server jebol (kehabisan ruang dan *bandwidth* internet cepat habis).</p>
        
        <p>Solusi profesional yang paling sering digunakan adalah: Unggah video Anda ke **YouTube** atau **Vimeo**, lalu gunakan fitur <em>Embed</em> menggunakan tag <code>&lt;iframe&gt;</code>.</p>
        
        <div class='code-block'>
            <pre><code>&lt;h3&gt;Tonton Tutorial di Bawah Ini:&lt;/h3&gt;
&lt;!-- Kode Iframe ini dapat di-copy secara instan dengan menekan tombol 'Share' -> 'Embed' di video YouTube --&gt;
&lt;iframe width="560" height="315" 
        src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=0&amp;rel=0" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen&gt;
&lt;/iframe&gt;</code></pre>
        </div>
        """
    },
    {
        "filename": "menambahkan-audio.html",
        "title": "Menambahkan Audio pada HTML",
        "content": """
        <p>Sama persis seperti elemen video, HTML5 membawa anugerah besar bagi para pecinta musik dan podcaster melalui pengenalan tag <code>&lt;audio&gt;</code>. Format file suara yang paling stabil dan umum didukung adalah <strong>MP3</strong> (.mp3), diikuti oleh WAV dan OGG.</p>

        <h3>Cara Dasar Menggunakan Tag <code>&lt;audio&gt;</code></h3>
        <p>Penerapannya sangat identik dengan tag video, hanya saja tidak ada atribut untuk lebar (width) atau tinggi (height), karena komponen audio hanya berupa bilah (bar) suara.</p>

        <div class='code-block'>
            <pre><code>&lt;h3&gt;Dengarkan Episode Podcast Terbaru Kami:&lt;/h3&gt;
&lt;audio controls&gt;
  &lt;source src="media/podcast-episode-01.mp3" type="audio/mpeg"&gt;
  &lt;source src="media/podcast-episode-01.ogg" type="audio/ogg"&gt;
  Teks ini akan muncul jika browser pengguna tidak mendukung HTML5 Audio.
&lt;/audio&gt;</code></pre>
        </div>

        <h4>Atribut yang Didukung:</h4>
        <ul class="custom-list">
            <li><strong><code>controls</code>:</strong> Menampilkan tombol Play, durasi, dan ikon pengatur volume suara. Jika Anda tidak menulis atribut ini, file audio <strong>sama sekali tidak akan terlihat</strong> di layar browser (seolah-olah elemen tersebut tidak ada).</li>
            <li><strong><code>autoplay</code>:</strong> Memutar audio sesaat halaman di-*load*. Sama dengan video, Google Chrome dan Firefox modern sangat ketat melarang website memutar suara secara tiba-tiba tanpa klik/interaksi pengguna terlebih dahulu.</li>
            <li><strong><code>loop</code>:</strong> Musik diulang-ulang.</li>
            <li><strong><code>muted</code>:</strong> Suara langsung disunyikan secara otomatis.</li>
        </ul>

        <h3>Studi Kasus: Membuat Musik Latar Belakang (BGM - Background Music)</h3>
        <p>Di era awal web, banyak website (seperti blog pribadi atau website undangan pernikahan digital saat ini) yang menggunakan musik yang terus berputar di latar belakang tanpa henti.</p>
        
        <p>Anda bisa membuatnya dengan menyembunyikan kontrol (menghapus atribut <code>controls</code>) dan memberinya <code>autoplay loop</code>.</p>
        
        <div class='code-block'>
            <pre><code>&lt;!-- Musik akan tersembunyi (karena tidak ada 'controls') dan terus berputar otomatis --&gt;
&lt;audio autoplay loop&gt;
  &lt;source src="lagu-romantis-pernikahan.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>
        </div>
        
        <div class='info-box'>
            <i class='bx bx-check-shield'></i>
            <p><strong>Praktik Modern (Undangan Digital):</strong> Karena aturan keamanan browser yang akan membungkam fitur <em>autoplay</em> pada musik yang tersembunyi, web undangan digital modern selalu memberikan sebuah tombol besar "Buka Undangan" di halaman pertama. Tombol itulah yang di-*setting* menggunakan JavaScript untuk memicu dimulainya lagu sekaligus membuka konten website.</p>
        </div>
        """
    },
    {
        "filename": "pengenalan-css.html",
        "title": "Pengenalan Dasar CSS (Cascading Style Sheets)",
        "content": """
        <p>Jika HTML diibaratkan sebagai kerangka tulang atau pondasi batu bata pada sebuah rumah, maka <strong>CSS</strong> adalah tukang cat, desainer interior, dan arsitek fasadnya. CSS yang memberi warna dinding, menentukan besar jendela, dan mengatur jarak antar perabotan.</p>

        <p>CSS (Cascading Style Sheets) bertugas penuh untuk mengatur gaya visual (*styling*), layout, tata letak spasial, dan animasi elemen-elemen HTML di dalam *browser*.</p>

        <h3>Tiga Metode Menyisipkan CSS ke dalam HTML</h3>
        <p>Terdapat tiga cara untuk mengawinkan kode CSS dengan kerangka HTML Anda. Ketiganya valid, namun penggunaannya disesuaikan dengan kebutuhan dan skala project.</p>
        
        <h4>1. Inline CSS (Gaya Baris)</h4>
        <p>CSS ditulis langsung di dalam tag HTML menggunakan atribut bernama <code>style</code>. Cara ini <strong>sangat tidak direkomendasikan</strong> untuk dipakai membuat desain menyeluruh karena membuat kode HTML Anda menjadi bengkak, berantakan, dan sulit di-*maintenance*.</p>
        <div class='code-block'>
            <pre><code>&lt;!-- Ini adalah Inline CSS --&gt;
&lt;h1 style="color: blue; font-family: Arial; text-align: center;"&gt;
    Judul Berwarna Biru di Tengah
&lt;/h1&gt;
&lt;p style="color: red; font-size: 18px;"&gt;Teks paragraf ini berwarna merah.&lt;/p&gt;</code></pre>
        </div>

        <h4>2. Internal / Embedded CSS</h4>
        <p>CSS dikumpulkan pada satu lokasi di dalam dokumen HTML itu sendiri. Penulisannya dibungkus dalam tag <code>&lt;style&gt;</code> yang biasanya diletakkan pada bagian <code>&lt;head&gt;</code>. Cocok digunakan jika Anda hanya membuat web satu halaman saja (Single Page).</p>
        <div class='code-block'>
            <div class="code-header"><span>index.html</span></div>
            <pre><code>&lt;head&gt;
    &lt;title&gt;Contoh Internal CSS&lt;/title&gt;
    &lt;style&gt;
        /* Ini adalah blok CSS */
        body { 
            background-color: #f4f4f4; 
        }
        h1 { 
            color: darkblue; 
            text-align: center; 
        }
        p {
            font-size: 16px;
            color: #333333;
        }
    &lt;/style&gt;
&lt;/head&gt;</code></pre>
        </div>

        <h4>3. External CSS (Cara Paling Profesional dan Wajib)</h4>
        <p>Memisahkan secara total antara kerangka data (HTML) dan gaya visual desain (CSS) ke dalam <strong>dua file yang terpisah secara fisik</strong>. File desain disimpan dalam ekstensi <code>.css</code> (contoh: <code>style.css</code>), kemudian dipanggil atau dikaitkan ke dalam file HTML menggunakan tag <code>&lt;link&gt;</code> di dalam <code>&lt;head&gt;</code>.</p>
        
        <p>Keuntungannya luar biasa besar: Satu file <code>style.css</code> dapat dipakai secara serentak untuk mengubah desain 100 file HTML secara bersamaan! Jika Anda ingin mengubah warna latar belakang 100 halaman tersebut, Anda cukup mengubah SATU baris di <code>style.css</code>.</p>
        
        <div class='code-block'>
            <div class="code-header"><span>index.html</span></div>
            <pre><code>&lt;head&gt;
    &lt;!-- Menautkan file style.css eksternal --&gt;
    &lt;link rel="stylesheet" href="css/style.css"&gt;
&lt;/head&gt;</code></pre>
        </div>
        
        <div class='code-block'>
            <div class="code-header"><span>css/style.css</span></div>
            <pre><code class="language-css">/* Semua kode murni CSS ada di sini, tanpa campur aduk tag HTML sedikitpun */
body {
    background-color: #1e293b;
    color: white;
    font-family: 'Outfit', sans-serif;
}

button {
    background-color: blue;
    padding: 10px 20px;
    border-radius: 5px;
}</code></pre>
        </div>
        """
    },
    {
        "filename": "selektor-css.html",
        "title": "Memahami 5 Macam Selektor pada CSS",
        "content": """
        <p>Ketika Anda menulis kode CSS Eksternal (di dalam file <code>.css</code> terpisah), pertanyaan terbesarnya adalah: <em>"Bagaimana cara kode CSS tahu elemen HTML yang mana yang ingin ia ubah warnanya?"</em></p>
        
        <p>Jawabannya adalah <strong>Selektor (Selector)</strong>. Sesuai namanya, Selektor berfungsi untuk "membidik" dan menyeleksi elemen HTML spesifik sebelum gaya desain diterapkan. Terdapat 5 macam selektor dasar yang wajib dikuasai.</p>
        
        <h3>1. Tag / Element Selector</h3>
        <p>Selektor paling sederhana. Memilih (membidik) elemen hanya dengan menyebut nama tag HTML-nya. Semua tag yang disebutkan akan terkena dampaknya secara global.</p>
        <div class='code-block'>
            <pre><code class="language-css">/* Mengubah semua teks di dalam tag &lt;p&gt; se-antero halaman menjadi biru */
p {
    color: blue;
    font-size: 16px;
}

/* Mengubah latar semua tag &lt;button&gt; menjadi merah */
button {
    background-color: red;
}</code></pre>
        </div>

        <h3>2. ID Selector</h3>
        <p>Memilih elemen secara SANGAT spesifik. ID ibarat Nomor KTP bagi sebuah elemen HTML, sifatnya <strong>unik dan tidak boleh ada dua elemen yang memiliki nama ID sama</strong> dalam satu halaman.</p>
        <p>Di HTML, elemen diberi atribut <code>id="nama_unik"</code>. Di CSS, Anda membidiknya dengan menggunakan simbol <strong>tagar (#)</strong>.</p>
        <div class='code-block'>
            <pre><code class="language-css">/* Hanya menghias satu elemen yang memiliki id="header-utama" */
#header-utama {
    background-color: black;
    height: 100px;
    text-align: center;
}</code></pre>
        </div>

        <h3>3. Class Selector (Selektor Kelas)</h3>
        <p>Ini adalah selektor yang <strong>paling sering digunakan</strong> oleh *developer* profesional (seperti di framework Bootstrap atau Tailwind). Class ibarat seragam kelompok. Berbeda dengan ID, nama Class <strong>boleh dipakai berulang kali</strong> pada sebanyak mungkin elemen yang Anda inginkan.</p>
        <p>Di HTML, elemen diberi atribut <code>class="nama_kelas"</code>. Di CSS, Anda membidiknya dengan simbol <strong>titik (.)</strong>.</p>
        <div class='code-block'>
            <pre><code class="language-css">/* Semua elemen dengan class="tombol-sukses" akan berwarna hijau */
.tombol-sukses {
    background-color: green;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
}</code></pre>
        </div>

        <h3>4. Universal Selector</h3>
        <p>Selektor sapu jagat. Membidik <strong>seluruh elemen tanpa terkecuali</strong> (mulai dari tag html, body, div, p, h1, img) di halaman tersebut secara serentak. Disimbolkan dengan tanda <strong>bintang (*)</strong>.</p>
        <p>Umumnya digunakan oleh *programmer* di baris paling atas CSS untuk me-reset bawaan *margin* browser (CSS Reset).</p>
        <div class='code-block'>
            <pre><code class="language-css">* {
    /* Menghilangkan semua jarak bawaan browser */
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}</code></pre>
        </div>

        <h3>5. Grouping Selector (Selektor Pengelompokan)</h3>
        <p>Terkadang, Anda ingin memberi gaya yang sama persis (misal: warna font yang sama) kepada beberapa elemen berbeda, misal `h1`, `h2`, dan `p`. Daripada menulis ulang kode berulang kali, Anda bisa mengelompokkannya dan memisahkannya dengan tanda <strong>koma (,)</strong>.</p>
        <div class='code-block'>
            <pre><code class="language-css">/* Menyatukan h1, h2, dan class .teks-kuning agar sama-sama berwarna kuning */
h1, h2, .teks-kuning {
    color: yellow;
    font-family: 'Arial', sans-serif;
    letter-spacing: 2px;
}</code></pre>
        </div>
        """
    },
    {
        "filename": "project-web.html",
        "title": "Project Web Pribadi - Sintesis Akhir",
        "content": """
        <p>Selamat! Anda telah mempelajari seluruh dasar pembentukan tulang kerangka website menggunakan HTML. Mulai dari teks dasar, merangkai tabel, menata form, hingga menyisipkan video.</p>
        
        <h3>Tugas Akhir Web Statis</h3>
        <p>Untuk menguji kompetensi Anda, saatnya memadukan seluruh pecahan materi dari Pertemuan 1 hingga 12 tersebut menjadi satu kesatuan <strong>Web Portofolio Pribadi (Personal Web)</strong> yang fungsional.</p>
        
        <h4>Struktur Halaman yang Diwajibkan:</h4>
        <ol class="custom-list numbered">
            <li><strong>Semantik Layout:</strong> Pastikan Anda menggunakan tag semantik seperti <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;section&gt;</code>, dan <code>&lt;footer&gt;</code> untuk membagi zona website.</li>
            <li><strong>In-Page Navigation:</strong> Buat menu di navigasi Anda (Home, Profil, Keahlian, Kontak) yang menggunakan tautan ber-ID (<code>&lt;a href="#profil"&gt;</code>) sehingga saat diklik, halaman hanya bergeser ke bawah.</li>
            <li><strong>Media Identitas:</strong> Sisipkan Foto Profil Anda (<code>&lt;img&gt;</code>) dan lengkapi atribut pendukungnya. Tambahkan juga elemen pemformatan teks (*bold, italic, list*) untuk menceritakan latar belakang Anda.</li>
            <li><strong>Data Terstruktur (Tabel):</strong> Buatlah tabel riwayat pendidikan atau daftar nilai IPK Anda yang rapi dengan penggabungan sel (colspan/rowspan) jika diperlukan.</li>
            <li><strong>Area Form (Interaksi):</strong> Di section paling bawah, buat formulir "Hubungi Saya". Masukkan jenis input text, email, pesan (textarea), serta minimal satu opsi radio button/select untuk menanyakan "Dari mana Anda tahu website saya?". Jangan lupa tombol Submit.</li>
            <li><strong>Video/Audio Portofolio (Opsional namun disarankan):</strong> Sisipkan video presentasi atau embed video karya unggulan dari akun YouTube Anda.</li>
        </ol>

        <div class='info-box' style='margin-bottom: 40px;'>
            <i class='bx bx-code-alt'></i>
            <p><strong>Kenapa Website Saya Terlihat Jelek (Putih Hitam)?</strong> Sangat wajar! Project Web Pribadi Anda di titik ini hanya terdiri dari HTML Murni. Tampilannya ibarat rumah batu bata yang belum di-plester dan dicat. Di titik inilah Anda menyadari batasan HTML dan bersiap melompat ke dunia desain visual: <strong>CSS (Cascading Style Sheets)</strong>.</p>
        </div>
        
        <!-- Certificate Generation Section -->
        <div class="certificate-section glass-panel hover-glow" style="margin-top: 50px; padding: 40px 30px; text-align: center; border: 1px solid #10b981; background: rgba(16, 185, 129, 0.05);">
            <h3 style="color: #10b981; margin-bottom: 15px; font-size: 1.8rem;"><i class='bx bx-certification'></i> Klaim Sertifikat Kelulusan</h3>
            <p style="margin-bottom: 25px; color: #cbd5e1;">Telah berhasil merancang halaman web pribadi Anda? Masukkan nama lengkap Anda di bawah ini untuk mencetak dan mengunduh e-Sertifikat resmi dari AkademiTech.</p>
            
            <div style="display: flex; gap: 15px; justify-content: center; max-width: 500px; margin: 0 auto 30px; flex-wrap: wrap;">
                <input type="text" id="certNameInput" placeholder="Masukkan Nama Lengkap Anda..." style="flex: 1; min-width: 200px; padding: 15px; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.5); background: rgba(0,0,0,0.5); color: white; font-size: 16px;">
                <button id="btnGenerateCert" class="btn btn-primary" style="background: linear-gradient(135deg, #10b981, #059669); box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);">Generate Sertifikat</button>
            </div>
            
            <!-- Canvas container (hidden by default) -->
            <div id="certPreviewContainer" style="display: none; flex-direction: column; align-items: center; gap: 20px; margin-top: 30px;">
                <p style="color: #34d399; font-weight: 600;"><i class='bx bx-check-circle'></i> Sertifikat Berhasil Dibuat!</p>
                <!-- HTML5 Canvas for drawing the certificate -->
                <canvas id="certCanvas" width="800" height="560" style="max-width: 100%; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.6);"></canvas>
                <button id="btnDownloadCert" class="btn btn-outline" style="border-color: #10b981; color: #10b981;"><i class='bx bxs-download'></i> Unduh File (PDF)</button>
            </div>
        </div>
        """
    },
]

# Generate Next and Prev Links
for i, tut in enumerate(tutorials):
    prev_link = tutorials[i-1]["filename"] if i > 0 else "#"
    prev_display = "display: inline-block;" if i > 0 else "display: none;"
    
    next_link = tutorials[i+1]["filename"] if i < len(tutorials)-1 else "#"
    next_display = "display: inline-block;" if i < len(tutorials)-1 else "display: none;"
    
    html = template.replace("{title}", tut["title"])
    html = html.replace("{content}", tut["content"])
    html = html.replace("{prev_link}", prev_link).replace("{prev_display}", prev_display)
    html = html.replace("{next_link}", next_link).replace("{next_display}", next_display)
    
    with open(tut["filename"], "w", encoding="utf-8") as f:
        f.write(html)
        
print("Tutorials generated successfully with comprehensive content!")

