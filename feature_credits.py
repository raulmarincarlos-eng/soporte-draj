import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

# 1. HTML and CSS for the Credits Modal and Floating Button
credits_html = """
    <!-- Floating Credits Button -->
    <div id="btnCredits" class="credits-btn no-print" title="Créditos del Sistema">
        <i class="fas fa-fingerprint me-2"></i><span>© Carlos</span>
    </div>

    <!-- Elegant Glassmorphism Credits Modal -->
    <div id="creditsModal" class="credits-overlay d-none no-print">
        <div class="credits-glass-card">
            <button id="closeCredits" class="credits-close"><i class="fas fa-times"></i></button>
            <div class="credits-header">
                <div class="credits-avatar">
                    <i class="fas fa-code"></i>
                </div>
                <div class="credits-pulse-ring"></div>
            </div>
            <div class="credits-body mt-4 text-center">
                <h3 class="fw-bold mb-1" style="background: linear-gradient(90deg, #0d6efd, #198754); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Ing. Carlos Marin</h3>
                <p class="text-muted fw-bold mb-3" style="letter-spacing: 2px; font-size: 0.8rem; text-transform: uppercase;">Lead Developer / UI Architect</p>
                <div class="d-flex justify-content-center gap-3 mb-4">
                    <span class="badge bg-primary bg-opacity-10 text-primary border border-primary border-opacity-25 rounded-pill px-3 py-2"><i class="fab fa-python me-1"></i> Python Backend</span>
                    <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 rounded-pill px-3 py-2"><i class="fab fa-js me-1"></i> UI/UX Design</span>
                </div>
                <p class="small text-secondary px-3" style="line-height: 1.6;">
                    Sistema integral de soporte tecnológico diseñado y programado desde cero para optimizar la gestión de incidencias de la DRAJ. 
                    <br><br><strong>Versión 1.0.1 (Premium Edition)</strong>
                </p>
            </div>
        </div>
    </div>

    <style>
        /* Credits Button */
        .credits-btn {
            position: fixed;
            bottom: 30px;
            left: 30px;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 0, 0, 0.1);
            color: #333;
            padding: 8px 16px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 0.85rem;
            cursor: pointer;
            z-index: 9998;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            display: flex;
            align-items: center;
        }
        .credits-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            background: #fff;
            color: #0d6efd;
        }
        body.dark-mode .credits-btn {
            background: rgba(30, 30, 30, 0.8);
            border-color: rgba(255, 255, 255, 0.1);
            color: #ccc;
        }
        body.dark-mode .credits-btn:hover { background: #333; color: #fff; }

        /* Credits Overlay */
        .credits-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            z-index: 10000;
            display: flex; justify-content: center; align-items: center;
            opacity: 0; transition: opacity 0.4s ease;
        }
        .credits-overlay.show { opacity: 1; }

        /* Glass Card */
        .credits-glass-card {
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 30px 60px rgba(0,0,0,0.15);
            border-radius: 24px;
            width: 100%; max-width: 450px;
            padding: 40px 30px;
            position: relative;
            transform: translateY(50px) scale(0.95);
            transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        }
        .credits-overlay.show .credits-glass-card {
            transform: translateY(0) scale(1);
        }
        body.dark-mode .credits-glass-card {
            background: rgba(25, 25, 25, 0.85);
            border-color: rgba(255, 255, 255, 0.08);
            box-shadow: 0 30px 60px rgba(0,0,0,0.5);
        }
        body.dark-mode .credits-glass-card .text-secondary { color: #aaa !important; }

        /* Close Button */
        .credits-close {
            position: absolute; top: 20px; right: 20px;
            background: none; border: none;
            color: #999; font-size: 1.2rem; cursor: pointer;
            transition: color 0.3s;
        }
        .credits-close:hover { color: #dc3545; }

        /* Avatar Animation */
        .credits-header {
            position: relative; width: 90px; height: 90px; margin: 0 auto;
        }
        .credits-avatar {
            width: 100%; height: 100%;
            background: linear-gradient(135deg, #0d6efd, #198754);
            border-radius: 50%;
            display: flex; justify-content: center; align-items: center;
            color: white; font-size: 2rem;
            position: relative; z-index: 2;
            box-shadow: 0 10px 20px rgba(13, 110, 253, 0.3);
        }
        .credits-pulse-ring {
            position: absolute; top: -10px; left: -10px; right: -10px; bottom: -10px;
            border: 2px solid rgba(13, 110, 253, 0.5);
            border-radius: 50%; z-index: 1;
            animation: pulse-ring 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.8); opacity: 1; }
            100% { transform: scale(1.3); opacity: 0; }
        }
    </style>

    <script>
        // Credits Logic
        document.addEventListener('DOMContentLoaded', () => {
            const btnCredits = document.getElementById('btnCredits');
            const creditsModal = document.getElementById('creditsModal');
            const closeCredits = document.getElementById('closeCredits');
            
            if(btnCredits && creditsModal && closeCredits) {
                btnCredits.addEventListener('click', () => {
                    creditsModal.classList.remove('d-none');
                    // Trigger reflow for animation
                    void creditsModal.offsetWidth;
                    creditsModal.classList.add('show');
                });
                
                const closeModal = () => {
                    creditsModal.classList.remove('show');
                    setTimeout(() => { creditsModal.classList.add('d-none'); }, 400); // Wait for transition
                };
                
                closeCredits.addEventListener('click', closeModal);
                creditsModal.addEventListener('click', (e) => {
                    if(e.target === creditsModal) closeModal();
                });
            }
        });
    </script>
"""
if "btnCredits" not in base_content:
    base_content = base_content.replace("</body>", credits_html + "\n</body>")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_content)

print("Credits UI logic injected in base.html")
