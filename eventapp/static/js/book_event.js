document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Create animated message
    const message = document.createElement("div");
    message.textContent = "🎉 Booking Confirmed! 🎉";
    message.style.position = "fixed";
    message.style.top = "30%";
    message.style.left = "50%";
    message.style.transform = "translate(-50%, -50%)";
    message.style.background = "#ffffffdd";
    message.style.padding = "20px 40px";
    message.style.borderRadius = "15px";
    message.style.boxShadow = "0 0 15px rgba(0,0,0,0.3)";
    message.style.fontSize = "24px";
    message.style.color = "#ff5e7e";
    message.style.zIndex = "9999";
    document.body.appendChild(message);

    // Confetti animation using canvas
    launchConfetti();

    // Optionally submit the form after 1.5s
    setTimeout(() => {
      form.submit();
    }, 1500);
  });

  function launchConfetti() {
    const canvas = document.createElement("canvas");
    document.body.appendChild(canvas);
    canvas.style.position = "fixed";
    canvas.style.top = 0;
    canvas.style.left = 0;
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const ctx = canvas.getContext("2d");

    const confetti = [];
    for (let i = 0; i < 100; i++) {
      confetti.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height - canvas.height,
        r: Math.random() * 6 + 4,
        d: Math.random() * 40 + 10,
        color: `hsl(${Math.random() * 360}, 100%, 70%)`,
        tilt: Math.random() * 10 - 10,
        tiltAngle: 0,
      });
    }

    function drawConfetti() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      confetti.forEach(c => {
        ctx.beginPath();
        ctx.fillStyle = c.color;
        ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
        ctx.fill();
      });
      updateConfetti();
      requestAnimationFrame(drawConfetti);
    }

    function updateConfetti() {
      confetti.forEach(c => {
        c.y += Math.cos(c.d) + 1 + c.r / 2;
        c.x += Math.sin(c.d);
        if (c.y > canvas.height) {
          c.y = -10;
          c.x = Math.random() * canvas.width;
        }
      });
    }

    drawConfetti();

    setTimeout(() => {
      canvas.remove();
    }, 3000); // Remove canvas after 3s
  }
});
