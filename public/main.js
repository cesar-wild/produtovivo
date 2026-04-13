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
