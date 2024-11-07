document.querySelector('.scroll-button.left').addEventListener('click', () => {
    document.querySelector('.project-images').scrollBy({
        left: -300, // Scrolls 300px to the left
        behavior: 'smooth'
    });
});

document.querySelector('.scroll-button.right').addEventListener('click', () => {
    document.querySelector('.project-images').scrollBy({
        left: 300, // Scrolls 300px to the right
        behavior: 'smooth'
    });
});
