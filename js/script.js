/* =================== Menu Icon Toggle =================== */
let menuIcon = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");
let header = document.querySelector(".header");

// Toggle menu visibility
menuIcon.onclick = () => {
  menuIcon.classList.toggle("bx-x");
  navbar.classList.toggle("active");
};

// Close menu when clicking on a link
document.querySelectorAll(".navbar a").forEach((link) => {
  link.addEventListener("click", () => {
    menuIcon.classList.remove("bx-x");
    navbar.classList.remove("active");
  });
});

/* =================== Header Sticky and Active Link =================== */
window.onscroll = () => {
  // Sticky Header
  if (window.scrollY > 100) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }

  // Active Link on Scroll
  let sections = document.querySelectorAll("section");
  let navLinks = document.querySelectorAll(".navbar a");

  let current = "";
  sections.forEach((sec) => {
    const sectionTop = sec.offsetTop;
    const sectionHeight = sec.clientHeight;
    if (scrollY >= sectionTop - 200) {
      current = sec.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href").includes(current)) {
      link.classList.add("active");
    }
  });
};

/* =================== Scroll Reveal Animation =================== */
ScrollReveal({
  distance: "80px",
  duration: 2000,
  delay: 200,
});

ScrollReveal().reveal(".home-content, .heading", { origin: "top" });
ScrollReveal().reveal(
  ".home-img, .home-logo-mobile, .hobbies-container, .project-box, .contact form",
  { origin: "bottom" }
);
ScrollReveal().reveal(".home-content h1, .about-img", { origin: "left" });
ScrollReveal().reveal(".home-content p, .about-content", { origin: "right" });

/* =================== Typed JS (Typing Text Effect) =================== */
new Typed("#element", {
  strings: [
    "A WhatsApp Bot Developer",
    "A Web Developer",
    "A Video Editor",
    "AN App Maker",
  ],
  typeSpeed: 100,
  backSpeed: 100,
  backDelay: 1000,
  loop: true,
});

    
/* Animate the skills items on reveal*/
let skillsAnimation = document.querySelectorAll(".skills-animation");
skillsAnimation.forEach((item) => {
  new Waypoint({
    element: item,
    offset: "80%",
    handler: function (direction) {
      let progress = item.querySelectorAll(".progress .progress-bar");
      progress.forEach((el) => {
        el.style.width = el.getAttribute("aria-valuenow") + "%";
      });
    },
  });
});
