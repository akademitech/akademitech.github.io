// Add sticky navbar behavior and smooth scrolling
document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.getElementById('navbar');
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    // Sticky Navbar
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile Menu Toggle
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            
            // Toggle Icon
            const icon = hamburger.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.replace('bx-menu', 'bx-x');
            } else {
                icon.classList.replace('bx-x', 'bx-menu');
            }
        });
    }

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Close mobile menu if open
                navLinks.classList.remove('active');
                if (hamburger) {
                    const icon = hamburger.querySelector('i');
                    icon.classList.replace('bx-x', 'bx-menu');
                }

                // Scroll with offset for navbar
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Form Validation (Simple Interactive Feedback)
    
    // --- Live Code Preview Generator ---
    const codeBlocks = document.querySelectorAll('.tutorial-content .code-block');
    codeBlocks.forEach(block => {
        const codeElement = block.querySelector('code');
        if (codeElement) {
            let codeText = codeElement.textContent;
            
            // Only generate preview for HTML code, not CSS or full documents
            if (!codeElement.className.includes('language-css') && !codeText.includes('<!DOCTYPE')) {
                
                // Replace local image paths with placeholders so the preview looks good
                codeText = codeText.replace(/src=["'](?:images\/|foto)[^"']*["']/gi, 'src="https://images.unsplash.com/photo-1579403124614-197f69d8187b?w=200&h=200&fit=crop"');
                
                const previewDiv = document.createElement('div');
                previewDiv.className = 'live-preview-box';
                previewDiv.style.marginBottom = '30px';
                
                const header = document.createElement('div');
                header.innerHTML = `<i class='bx bx-show' style='color: #10b981;'></i> <strong style='color: #10b981;'>Hasil Output (Visual):</strong>`;
                header.style.padding = '10px 0';
                
                const content = document.createElement('div');
                content.style.padding = '20px';
                content.style.border = '2px dashed #6366f1';
                content.style.borderRadius = '8px';
                content.style.background = 'rgba(255,255,255,0.95)'; // White bg to see true HTML colors
                content.style.color = '#000'; // Black text to see default HTML text
                content.style.overflowX = 'auto';
                
                content.innerHTML = codeText;
                
                previewDiv.appendChild(header);
                previewDiv.appendChild(content);
                
                // Insert the preview div right after the code block
                block.parentNode.insertBefore(previewDiv, block.nextSibling);
            }
        }
    });

    const form = document.getElementById('registrationForm');
    const formMessage = document.getElementById('formMessage');

    if (form) {
        form.addEventListener('submit', (e) => {
            // Basic validation
            const password = document.getElementById('password').value;
            if (password.length < 6) {
                e.preventDefault(); // Prevent submit ONLY if invalid
                formMessage.textContent = 'Kata sandi minimal 6 karakter!';
                formMessage.className = 'form-message error';
                return;
            }

            // Let the form submit naturally to FormSubmit.co
            const btn = form.querySelector('.submit-btn');
            btn.textContent = 'Mengirim...';
        });
    }

    // Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    };
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    revealElements.forEach(el => revealObserver.observe(el));
});

    // --- Certificate Generator Logic ---
    const btnGenerateCert = document.getElementById('btnGenerateCert');
    const certNameInput = document.getElementById('certNameInput');
    const certPreviewContainer = document.getElementById('certPreviewContainer');
    const certCanvas = document.getElementById('certCanvas');
    const btnDownloadCert = document.getElementById('btnDownloadCert');

    if (btnGenerateCert && certCanvas) {
        btnGenerateCert.addEventListener('click', () => {
            const name = certNameInput.value.trim();
            if (!name) {
                alert('Tolong masukkan nama lengkap Anda terlebih dahulu!');
                return;
            }

            // Draw Certificate on Canvas
            const ctx = certCanvas.getContext('2d');
            const cw = certCanvas.width;
            const ch = certCanvas.height;

            // 1. Background
            ctx.fillStyle = '#0f172a'; // Dark slate
            ctx.fillRect(0, 0, cw, ch);

            // 2. Borders
            ctx.strokeStyle = '#10b981'; // Emerald Green
            ctx.lineWidth = 15;
            ctx.strokeRect(20, 20, cw - 40, ch - 40);
            
            ctx.strokeStyle = 'rgba(255,255,255,0.2)';
            ctx.lineWidth = 2;
            ctx.strokeRect(30, 30, cw - 60, ch - 60);

            // 3. Texts
            ctx.textAlign = 'center';
            
            // Header
            ctx.fillStyle = '#10b981';
            ctx.font = 'bold 45px "Space Grotesk", sans-serif';
            ctx.fillText('SERTIFIKAT KELULUSAN', cw / 2, 120);
            
            // Subheader
            ctx.fillStyle = '#94a3b8';
            ctx.font = '20px "Outfit", sans-serif';
            ctx.fillText('Dengan bangga diberikan kepada:', cw / 2, 200);

            // Name
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 50px "Outfit", sans-serif';
            ctx.fillText(name.toUpperCase(), cw / 2, 280);

            // Line under name
            ctx.beginPath();
            ctx.moveTo(cw / 2 - 250, 300);
            ctx.lineTo(cw / 2 + 250, 300);
            ctx.strokeStyle = '#6366f1'; // Indigo
            ctx.lineWidth = 3;
            ctx.stroke();

            // Description
            ctx.fillStyle = '#94a3b8';
            ctx.font = '18px "Outfit", sans-serif';
            ctx.fillText('Atas dedikasi dan pencapaiannya dalam menyelesaikan kurikulum:', cw / 2, 350);
            
            ctx.fillStyle = '#34d399';
            ctx.font = 'bold 25px "Space Grotesk", sans-serif';
            ctx.fillText('PEMROGRAMAN WEB 1 (HTML & CSS)', cw / 2, 390);
            
            ctx.fillStyle = '#94a3b8';
            ctx.font = '16px "Outfit", sans-serif';
            ctx.fillText('Serta berhasil membangun Proyek Web Portofolio Pribadi.', cw / 2, 430);

            // Date & Signatures
            const today = new Date().toLocaleDateString('id-ID', { year: 'numeric', month: 'long', day: 'numeric' });
            
            ctx.fillStyle = '#ffffff';
            ctx.font = '15px "Outfit", sans-serif';
            ctx.fillText('Jakarta, ' + today, 120, 490);
            ctx.fillText('Faisal Fadilah', 320, 490);
            ctx.fillText('Hari Yanto', 500, 490);
            ctx.fillText('Desi Ova R.', 680, 490);
            
            ctx.fillStyle = '#6366f1';
            ctx.font = '13px "Outfit", sans-serif';
            ctx.fillText('Tanggal Diterbitkan', 120, 515);
            ctx.fillText('Instruktur', 320, 515);
            ctx.fillText('Mentor', 500, 515);
            ctx.fillText('Pemateri', 680, 515);

            // Show Container
            certPreviewContainer.style.display = 'flex';
        });

        // Download logic
        btnDownloadCert.addEventListener('click', () => {
            const dataURL = certCanvas.toDataURL('image/png');
            const name = certNameInput.value.trim().replace(/\s+/g, '_');
            
            // Periksa ketersediaan jsPDF (dimuat dari CDN)
            if (window.jspdf && window.jspdf.jsPDF) {
                const { jsPDF } = window.jspdf;
                // Buat dokumen PDF landscape berukuran sama dengan canvas (800x560)
                const pdf = new jsPDF({
                    orientation: 'landscape',
                    unit: 'px',
                    format: [800, 560]
                });
                
                // Masukkan gambar canvas ke dalam PDF
                pdf.addImage(dataURL, 'PNG', 0, 0, 800, 560);
                pdf.save('Sertifikat_AkademiTech_' + (name || 'Lulus') + '.pdf');
            } else {
                // Fallback jika library jsPDF gagal dimuat (tetap download PNG)
                const a = document.createElement('a');
                a.href = dataURL;
                a.download = 'Sertifikat_AkademiTech_' + (name || 'Lulus') + '.png';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }
        });
    }
