document.addEventListener('DOMContentLoaded', () => {
    initMobileNav();
    initDiseaseSearch();
    initContactForm();
    initTasteSliders();
    initTasteAnalyzer();
});

function initMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if (!toggle || !links) return;

    toggle.addEventListener('click', () => {
        links.classList.toggle('open');
    });

    links.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => links.classList.remove('open'));
    });
}

function initDiseaseSearch() {
    const searchInput = document.getElementById('disease-search');
    const grid = document.getElementById('disease-grid');
    if (!searchInput || !grid) return;

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.toLowerCase();
        grid.querySelectorAll('.disease-card').forEach(card => {
            const name = card.dataset.name || '';
            card.style.display = name.includes(query) ? '' : 'none';
        });
    });
}

function initContactForm() {
    const form = document.getElementById('contact-form');
    const success = document.getElementById('form-success');
    if (!form || !success) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        form.style.display = 'none';
        success.classList.remove('hidden');
    });
}

function initTasteSliders() {
    document.querySelectorAll('.taste-slider').forEach(slider => {
        const valueEl = document.getElementById('val-' + slider.dataset.taste);
        if (!valueEl) return;

        slider.addEventListener('input', () => {
            valueEl.textContent = slider.value + '%';
        });
    });
}

function initTasteAnalyzer() {
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultsContent = document.getElementById('results-content');
    if (!analyzeBtn || !resultsContent || typeof herbProfiles === 'undefined') return;

    analyzeBtn.addEventListener('click', () => {
        const profile = {};
        document.querySelectorAll('.taste-slider').forEach(slider => {
            profile[slider.dataset.taste] = parseInt(slider.value, 10);
        });

        const total = Object.values(profile).reduce((a, b) => a + b, 0);
        if (total === 0) {
            resultsContent.innerHTML = '<p class="results-placeholder">Please adjust at least one taste slider before analyzing.</p>';
            return;
        }

        const matches = herbProfiles.map(herb => {
            let diff = 0;
            for (const [taste, value] of Object.entries(profile)) {
                diff += Math.abs(value - (herb.taste_profile[taste] || 0));
            }
            const maxDiff = 600;
            const score = Math.max(0, Math.round((1 - diff / maxDiff) * 100));
            return { herb, score };
        }).sort((a, b) => b.score - a.score).slice(0, 5);

        let html = '<div class="match-results">';
        matches.forEach(({ herb, score }) => {
            html += `
                <div class="match-result">
                    <span class="herb-emoji">${herb.emoji}</span>
                    <div style="flex:1">
                        <strong>${herb.name}</strong>
                        <div class="progress-bar" style="margin-top:4px">
                            <div class="progress-fill" style="width:${score}%"></div>
                        </div>
                    </div>
                    <span class="match-score">${score}%</span>
                </div>`;
        });
        html += '</div>';
        resultsContent.innerHTML = html;
    });
}
