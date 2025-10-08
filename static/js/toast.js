function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');

    if (!toastComponent) return;

    // Reset semua style & icon dulu
    toastComponent.classList.remove(
        'bg-pink-100', 'border-pink-300', 'text-pink-800',
        'bg-green-100', 'border-green-400', 'text-green-800',
        'bg-red-100', 'border-red-400', 'text-red-800'
    );

    // Default warna & icon
    let icon = '💬';
    toastComponent.style.border = '';

    // Gaya per tipe toast
    if (type === 'success') {
        toastComponent.classList.add('bg-green-100', 'border-green-400', 'text-green-800');
        toastComponent.style.border = '1px solid #86efac'; // green pastel
        icon = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-100', 'border-red-400', 'text-red-800');
        toastComponent.style.border = '1px solid #fca5a5'; // soft red
        icon = '❌';
    } else {
        toastComponent.classList.add('bg-pink-100', 'border-pink-300', 'text-pink-800');
        toastComponent.style.border = '1px solid #f9a8d4'; // pink pastel
        icon = '🌸';
    }

    // Set konten toast
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastIcon.textContent = icon;

    // Animasi muncul
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hilang setelah durasi tertentu
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
