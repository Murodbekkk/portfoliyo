// ============================================
// Mobil menyu
// ============================================
const navToggle = document.getElementById("navToggle");
const navLinks = document.querySelector(".nav-links");
if (navToggle) {
  navToggle.addEventListener("click", () => {
    navLinks.classList.toggle("open");
  });
  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => navLinks.classList.remove("open"));
  });
}

// ============================================
// Terminal typewriter — hero signature element
// ============================================
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const terminalBody = document.getElementById("terminalBody");

const script = [
  { type: "cmd", text: "whoami" },
  { type: "out", text: "backend dasturchi // Python & Django" },
  { type: "cmd", text: "cat skills.txt" },
  { type: "out", text: "Django, REST API, PostgreSQL, Docker, JS" },
  { type: "cmd", text: "./deploy.sh --env=production" },
  { type: "out", text: "✓ build tugadi   ✓ testlar o'tdi   ✓ live" },
];

async function typeLine(el, text, speed = 28) {
  for (let i = 0; i < text.length; i++) {
    el.textContent += text[i];
    await new Promise((r) => setTimeout(r, speed));
  }
}

async function runTerminal() {
  if (!terminalBody) return;

  if (reduceMotion) {
    terminalBody.innerHTML = script
      .map((l) =>
        l.type === "cmd"
          ? `<span class="line-cmd">${l.text}</span>\n`
          : `<span class="line-out">${l.text}</span>`
      )
      .join("");
    return;
  }

  for (const line of script) {
    const lineEl = document.createElement("span");
    lineEl.className = line.type === "cmd" ? "line-cmd" : "line-out";
    terminalBody.appendChild(lineEl);

    if (line.type === "cmd") {
      await typeLine(lineEl, line.text, 32);
      terminalBody.appendChild(document.createTextNode("\n"));
      await new Promise((r) => setTimeout(r, 220));
    } else {
      lineEl.textContent = line.text;
      await new Promise((r) => setTimeout(r, 380));
    }
  }

  const cursor = document.createElement("span");
  cursor.className = "cursor";
  terminalBody.appendChild(cursor);
}

// Start terminal once it scrolls into view (or immediately if already visible)
if (terminalBody) {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          runTerminal();
          io.disconnect();
        }
      });
    },
    { threshold: 0.3 }
  );
  io.observe(terminalBody);
}

// ============================================
// Scroll reveal for skill bars + fade-ins
// ============================================
const skillBars = document.querySelectorAll(".skill-bar");
if (skillBars.length) {
  const barObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          barObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.4 }
  );
  skillBars.forEach((bar) => barObserver.observe(bar));
}

const revealTargets = document.querySelectorAll(
  ".project-card, .timeline-item, .skill-card"
);
if (revealTargets.length && !reduceMotion) {
  revealTargets.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(16px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
  });

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );
  revealTargets.forEach((el) => revealObserver.observe(el));
}
