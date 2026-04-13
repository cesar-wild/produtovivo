// Countdown timer — launch price expires 2026-05-15
(function() {
  const DEADLINE = new Date('2026-05-15T23:59:59-03:00').getTime();
  function pad(n) { return String(n).padStart(2, '0'); }
  function tick() {
    const now = Date.now();
    const diff = DEADLINE - now;
    if (diff <= 0) return;
    const days  = Math.floor(diff / 86400000);
    const hours = Math.floor((diff % 86400000) / 3600000);
    const mins  = Math.floor((diff % 3600000) / 60000);
    const secs  = Math.floor((diff % 60000) / 1000);
    const d = document.getElementById('cd-days');
    const h = document.getElementById('cd-hours');
    const m = document.getElementById('cd-mins');
    const s = document.getElementById('cd-secs');
    if (d) d.textContent = pad(days);
    if (h) h.textContent = pad(hours);
    if (m) m.textContent = pad(mins);
    if (s) s.textContent = pad(secs);
  }
  tick();
  setInterval(tick, 1000);
})();

document.addEventListener('DOMContentLoaded', () => {
  const buyBtn = document.getElementById('buy-btn');
  if (!buyBtn) return;

  buyBtn.addEventListener('click', async () => {
    buyBtn.disabled = true;
    buyBtn.textContent = 'Aguarde...';

    try {
      const res = await fetch('/checkout/session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!res.ok) throw new Error('Checkout failed');

      const { url } = await res.json();
      window.location.href = url;
    } catch (err) {
      console.error(err);
      buyBtn.disabled = false;
      buyBtn.textContent = 'Comprar agora — R$37';
      alert('Houve um erro. Tente novamente ou entre em contato: suporte@produtovivo.com');
    }
  });
});
