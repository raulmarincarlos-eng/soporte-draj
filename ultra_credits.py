import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

# Locate the start of the old block
start_marker = "<!-- Floating Credits Button -->"
end_marker = "</body>"

if start_marker in base_content:
    # Everything before the start marker
    before_block = base_content.split(start_marker)[0]
    
    new_ultra_credits = """
    <!-- Ultra-Minimalist Trigger -->
    <div class="webflow-credits-trigger no-print" id="btnCredits">
        <span>C.M. &copy; 2026</span>
    </div>

    <!-- Webflow-style Slide-Up Glass Drawer -->
    <div id="creditsModal" class="webflow-credits-drawer d-none no-print">
        <div class="webflow-drawer-backdrop" id="closeCreditsBackdrop"></div>
        <div class="webflow-drawer-content">
            <button id="closeCreditsBtn" class="webflow-close-btn">&times;</button>
            
            <div class="webflow-drawer-inner">
                <p class="webflow-subtitle">DESIGN & ENGINEERING</p>
                <h2 class="webflow-title">Carlos Marin</h2>
                <div class="webflow-divider"></div>
                <div class="webflow-roles">
                    <span>System Architecture</span>
                    <span class="dot">•</span>
                    <span>UI/UX Design</span>
                    <span class="dot">•</span>
                    <span>Backend Development</span>
                </div>
                
                <p class="webflow-description">
                    Este sistema fue concebido bajo los más altos estándares de desarrollo de software, 
                    fusionando una estética vanguardista con un rendimiento excepcional para la DRAJ.
                </p>
                
                <div class="webflow-footer">
                    <span>Versión 1.0.1</span>
                    <span>Fabricado en 2026</span>
                </div>
            </div>
        </div>
    </div>

    <style>
        /* Webflow-style Ultra Minimalist Trigger */
        .webflow-credits-trigger {
            position: fixed;
            bottom: 10px;
            right: 15px;
            font-size: 0.65rem;
            letter-spacing: 2px;
            font-weight: 500;
            color: rgba(0, 0, 0, 0.2);
            cursor: pointer;
            z-index: 9000;
            transition: all 0.4s ease;
            text-transform: uppercase;
        }
        body.dark-mode .webflow-credits-trigger {
            color: rgba(255, 255, 255, 0.15);
        }
        .webflow-credits-trigger:hover {
            color: rgba(0, 0, 0, 0.8);
            transform: translateY(-2px);
        }
        body.dark-mode .webflow-credits-trigger:hover {
            color: rgba(255, 255, 255, 0.9);
        }

        /* Drawer Backdrop */
        .webflow-drawer-backdrop {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            z-index: 9998;
            opacity: 0;
            transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        /* Drawer Content (Slide Up) */
        .webflow-drawer-content {
            position: fixed;
            bottom: 0; left: 0; width: 100vw;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(30px) saturate(200%);
            -webkit-backdrop-filter: blur(30px) saturate(200%);
            border-top: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 -20px 40px rgba(0,0,0,0.08);
            z-index: 9999;
            transform: translateY(100%);
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            padding: 60px 20px 40px;
            display: flex;
            justify-content: center;
        }
        body.dark-mode .webflow-drawer-content {
            background: rgba(15, 15, 15, 0.85);
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            box-shadow: 0 -20px 60px rgba(0,0,0,0.5);
            color: #f1f1f1;
        }

        /* Activation Classes */
        .webflow-credits-drawer.show .webflow-drawer-backdrop { opacity: 1; }
        .webflow-credits-drawer.show .webflow-drawer-content { transform: translateY(0); }

        /* Inner Layout */
        .webflow-drawer-inner {
            max-width: 800px;
            width: 100%;
            text-align: center;
            position: relative;
        }

        /* Typography */
        .webflow-subtitle {
            font-size: 0.7rem;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #888;
            margin-bottom: 15px;
            font-weight: 600;
        }
        .webflow-title {
            font-size: 4rem;
            font-weight: 300;
            letter-spacing: -1px;
            margin-bottom: 30px;
            color: #111;
            font-family: "Inter", -apple-system, sans-serif;
        }
        body.dark-mode .webflow-title { color: #fff; }
        
        .webflow-divider {
            height: 1px;
            width: 60px;
            background: #ccc;
            margin: 0 auto 30px;
        }
        body.dark-mode .webflow-divider { background: #333; }

        .webflow-roles {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            font-size: 0.85rem;
            color: #555;
            margin-bottom: 30px;
            font-weight: 500;
            letter-spacing: 1px;
        }
        body.dark-mode .webflow-roles { color: #aaa; }
        .webflow-roles .dot { color: #ccc; font-size: 0.5rem; }

        .webflow-description {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #666;
            max-width: 600px;
            margin: 0 auto 50px;
            font-weight: 300;
        }
        body.dark-mode .webflow-description { color: #999; }

        .webflow-footer {
            display: flex;
            justify-content: space-between;
            font-size: 0.7rem;
            color: #aaa;
            letter-spacing: 2px;
            text-transform: uppercase;
            border-top: 1px solid rgba(0,0,0,0.05);
            padding-top: 20px;
        }
        body.dark-mode .webflow-footer { border-top-color: rgba(255,255,255,0.05); color: #666; }

        /* Close Button */
        .webflow-close-btn {
            position: absolute;
            top: 20px;
            right: 30px;
            background: none;
            border: none;
            font-size: 2.5rem;
            font-weight: 200;
            color: #999;
            cursor: pointer;
            transition: transform 0.4s ease, color 0.4s ease;
            line-height: 1;
        }
        .webflow-close-btn:hover {
            color: #111;
            transform: rotate(90deg);
        }
        body.dark-mode .webflow-close-btn:hover { color: #fff; }

        /* Responsive */
        @media (max-width: 768px) {
            .webflow-title { font-size: 2.5rem; }
            .webflow-roles { flex-direction: column; gap: 5px; }
            .webflow-roles .dot { display: none; }
            .webflow-drawer-content { padding: 50px 20px 30px; }
        }
    </style>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btnCredits = document.getElementById('btnCredits');
            const creditsModal = document.getElementById('creditsModal');
            const closeBtn = document.getElementById('closeCreditsBtn');
            const backdrop = document.getElementById('closeCreditsBackdrop');
            
            if(btnCredits && creditsModal && closeBtn && backdrop) {
                btnCredits.addEventListener('click', () => {
                    creditsModal.classList.remove('d-none');
                    // Force reflow
                    void creditsModal.offsetWidth;
                    creditsModal.classList.add('show');
                });
                
                const closeModal = () => {
                    creditsModal.classList.remove('show');
                    setTimeout(() => { creditsModal.classList.add('d-none'); }, 800); // Matches CSS transition duration
                };
                
                closeBtn.addEventListener('click', closeModal);
                backdrop.addEventListener('click', closeModal);
            }
        });
    </script>
"""
    
    new_content = before_block + new_ultra_credits + "\n</body>\n</html>"
    with open('templates/base.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Ultra-elegant credits injected.")
else:
    print("Could not find start marker.")
