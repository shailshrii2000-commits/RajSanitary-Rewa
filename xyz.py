import requests
url = "https://shailshrii2000-commits.github.io/RajSanitary-Rewa/"  # Replace with the website URL
response = requests.get(url)
from bs4 import BeautifulSoup

html_content = response.text  # Get the HTML from the response
soup = BeautifulSoup(html_content, "html.parser")  # Parse the HTML

print(soup.prettify())

"""<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   Raj Sanitary Rewa | Premium Sanitary &amp; Hardware
  </title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet"/>
  <style>
   *{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:"Segoe UI",sans-serif;
}

body{
  background:#ffffff;
  color:#1f2933;
  scroll-behavior:smooth;
}

header{
  position:sticky;
  top:0;
  z-index:1000;
  background:#ffffff;
  box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.hero{
  text-align:center;
  padding:90px 20px;
  background:linear-gradient(135deg,#c1121f,#e63946);
  color:white;
}

.hero h1{
  font-size:2.8rem;
  margin-bottom:20px;
}

.hero p{
  max-width:800px;
  margin:auto;
  font-size:1.1rem;
  opacity:.95;
}

.btn{
  display:inline-block;
  margin-top:30px;
  padding:14px 36px;
  background:#facc15;
  color:#000;
  font-weight:bold;
  border-radius:30px;
  text-decoration:none;
  transition:.4s;
}

.btn:hover{
  transform:scale(1.08);
  box-shadow:0 0 20px rgba(250,204,21,.7);
}

.section{
  padding:80px 20px;
  text-align:center;
}

.section h2{
  font-size:2.4rem;
  color:#c1121f;
  margin-bottom:50px;
}

.card-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:30px;
  max-width:1200px;
  margin:auto;
}

.card{
  background:#ffffff;
  padding:30px;
  border-radius:18px;
  box-shadow:0 10px 30px rgba(0,0,0,0.08);
  transition:.4s;
}

.card:hover{
  transform:translateY(-12px);
  box-shadow:0 20px 45px rgba(193,18,31,0.3);
}

.highlight{
  background:#f9fafb;
  padding:70px 20px;
  text-align:center;
}

.highlight p{
  max-width:900px;
  margin:auto;
  font-size:1.05rem;
}

.highlight ul{
  max-width:800px;
  margin:30px auto 0;
  list-style:none;
}

.highlight li{
  padding:12px;
  font-size:1.05rem;
}

.cta{
  background:linear-gradient(135deg,#c1121f,#e63946);
  color:white;
  padding:80px 20px;
  text-align:center;
}

/* ===== ABOUT SECTION ENHANCED ===== */
.about-wrap{
  background:linear-gradient(180deg,#fff,#fde8e8,#fff);
  padding:90px 20px;
}

.about-container{
  max-width:1200px;
  margin:auto;
  display:flex;
  align-items:center;
  gap:40px;
  flex-wrap:wrap;
}

.about-text{
  flex:1;
  text-align:center;
}

.about-text p{
  font-size:1.08rem;
  line-height:1.7;
}

.about-img{
  width:260px;
  height:200px;
  border-radius:20px;
  overflow:hidden;
  box-shadow:0 15px 40px rgba(193,18,31,0.3);
  transform:rotate(-6deg);
}

.about-img.right{
  transform:rotate(6deg);
}

.about-img img{
  width:100%;
  height:100%;
  object-fit:cover;
}

.footer{
  background:#1f2933;
  color:#ccc;
  padding:50px 20px 20px;
}

.footer-container{
  max-width:1200px;
  margin:auto;
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:30px;
}

.footer h3{
  color:#facc15;
}

.footer a{
  color:#ccc;
  text-decoration:none;
}

.footer a:hover{
  color:#facc15;
}

.footer-bottom{
  text-align:center;
  margin-top:30px;
  border-top:1px solid #444;
  padding-top:15px;
  font-size:13px;
}

.whatsapp-icon{
  position:fixed;
  bottom:20px;
  right:20px;
  background:#25d366;
  color:white;
  padding:14px;
  border-radius:50%;
  font-size:24px;
  box-shadow:0 0 20px rgba(37,211,102,.7);
}

.scroll-animate{
  opacity:0;
  transform:translateY(50px);
  transition:all .9s ease;
}

.scroll-animate.show{
  opacity:1;
  transform:translateY(0);
}

/* ===== ASTRAL FIRST IMPRESSION ===== */
/* ===== ASTRAL MINI GRID SIZE INCREASE ===== */

/* ===== ASTRAL MINI GRID – 4 IN ONE ROW ===== */

.astral-mini-grid{
  display:grid;
  grid-template-columns:repeat(4, 1fr);   /* 🔥 4 cards in one row */
  gap:30px;
  max-width:1300px;
  margin:80px auto;
  padding:0 20px;
}

/* Tablet */
@media (max-width:1024px){
  .astral-mini-grid{
    grid-template-columns:repeat(2, 1fr);
  }
}

/* Mobile */
@media (max-width:640px){
  .astral-mini-grid{
    grid-template-columns:1fr;
  }
}


.astral-mini-card{
  background:#ffffff;
  border-radius:22px;
  padding:22px;
  box-shadow:0 15px 40px rgba(0,0,0,0.1);
  transition:0.4s;
}

.astral-mini-card:hover{
  transform:translateY(-10px);
  box-shadow:0 25px 55px rgba(193,18,31,0.35);
}

.astral-badge{
  display:inline-flex;
  align-items:center;
  gap:14px;
  background:#fff;
  padding:12px 26px;
  border-radius:40px;
  box-shadow:0 10px 25px rgba(0,0,0,0.12);
  font-weight:700;
  font-size:18px;            /* 🔥 text size increased */
  color:#c1121f;
}

.astral-badge img{
  height:42px;               /* 🔥 logo size increased */
  width:auto;
}

/* Title bigger */
.astral-mini-card h4,
.astral-title{
  font-size:1.25rem;
  font-weight:700;
  text-align:center;
  color:#c1121f;
  margin-bottom:14px;
}

/* Slider container bigger */
.mini-slider{
  width:100%;
  height:220px;   /* 🔥 IMAGE HEIGHT INCREASED */
  border-radius:16px;
  overflow:hidden;
  position:relative;
}

/* Images bigger */
.mini-slider img{
  width:100%;
  height:100%;
  object-fit:cover;
  position:absolute;
  opacity:0;
  transition:opacity 0.8s ease-in-out, transform 0.6s ease;
}

.mini-slider img.active{
  opacity:1;
  transform:scale(1.05);
}
  </style>
  <script src="https://cdn.tailwindcss.com">
  </script>
 </head>
 <body>
  <!-- HEADER -->
  <header class="bg-white shadow sticky top-0 z-50">
   <div class="max-w-7xl mx-auto flex items-center justify-between p-4">
    <div class="flex items-center gap-3">
     <img alt="Raj Sanitary Logo" class="h-16 md:h-20" src="logo.png"/>
     <span class="text-xl font-bold text-red-700">
      RAJ SANITARY
     </span>
    </div>
    <nav class="hidden md:flex gap-6 font-medium">
     <a class="text-red-700" href="index.html">
      Home
     </a>
     <a class="hover:text-red-700" href="products.html">
      Products
     </a>
     <a class="hover:text-red-700" href="contact.html">
      Contact
     </a>
    </nav>
    <a class="bg-yellow-400 px-4 py-2 rounded font-semibold" href="tel:7000903314">
     Call Now
    </a>
   </div>
  </header>
  <!-- HERO -->
  <section class="hero scroll-animate">
   <!-- ASTRAL BADGE -->
   <div class="astral-badge">
    <img alt="Astral Logo" src="astral.logo.jpg"/>
    <span>
     Authorized ASTRAL Dealer
    </span>
   </div>
   <h1>
    Premium Sanitary, Hardware &amp; Paint Solutions
   </h1>
   <p>
    Official ASTRAL agency in Rewa for CPVC Pipes, SWR Ring Fit Pipes,
  Water Tanks, and Premium Bathware.
    <br/>
    <br/>
    We are also a trusted Nerolac Paints dealer, providing high-quality interior and exterior paints,
  primers, and coatings to give your home a fresh, vibrant, and long-lasting finish.
   </p>
   <a class="btn" href="products.html">
    Explore Products
   </a>
   <!-- ASTRAL PRODUCT PREVIEW -->
   <div class="astral-mini-grid">
    <div class="astral-mini-card">
     <h4>
      ASTRAL CPVC Pipes
     </h4>
     <div class="mini-slider cpvc-mini">
      <img class="active" src="cpcv.jpg"/>
      <img src="cpcv1.webp"/>
      <img src="cpvc3.jpg"/>
     </div>
    </div>
    <div class="astral-mini-card">
     <h4>
      ASTRAL SWR Pipes
     </h4>
     <div class="mini-slider swr-mini">
      <img class="active" src="swr.webp"/>
      <img src="swr1.jpg"/>
      <img src="swr3.jpg"/>
     </div>
    </div>
    <div class="astral-mini-card">
     <h4>
      ASTRAL Water Tanks
     </h4>
     <div class="mini-slider tank-mini">
      <img class="active" src="watertank.jpg"/>
      <img src="watertank1.jpg"/>
      <img src="watertank2.jpg"/>
     </div>
    </div>
    <div class="astral-mini-card">
     <h4>
      ASTRAL Bathware
     </h4>
     <div class="mini-slider bath-mini">
      <img class="active" src="abathware.png"/>
      <img src="bathware.jpg"/>
      <img src="bathware.jpg"/>
     </div>
    </div>
   </div>
  </section>
  <!-- CATEGORIES -->
  <section class="section scroll-animate">
   <h2>
    Our Product Categories
   </h2>
   <div class="card-grid">
    <div class="card">
     <h3 class="font-bold text-lg mb-2">
      Sanitaryware
     </h3>
     <p>
      Basins, Western &amp; Indian Toilets, Sinks, Urinals
     </p>
    </div>
    <div class="card">
     <h3 class="font-bold text-lg mb-2">
      Bathroom Fittings
     </h3>
     <p>
      Taps, Showers, Mixer Sets, Angle Valves
     </p>
    </div>
    <div class="card">
     <h3 class="font-bold text-lg mb-2">
      Pipes &amp; Plumbing
     </h3>
     <p>
      PVC, CPVC, UPVC Pipes &amp; Accessories
     </p>
    </div>
   </div>
  </section>
  <!-- ABOUT -->
  <section class="about-wrap scroll-animate">
   <div class="about-container">
    <!-- Left Image -->
    <div class="about-img">
     <img alt="Raj Sanitary Showroom" src="showroom1.jpg"/>
    </div>
    <!-- Text -->
    <div class="about-text">
     <h2 class="text-3xl font-bold text-red-700 mb-4">
      About Raj Sanitary
     </h2>
     <p>
      Raj Sanitary is a trusted and well-established sanitary &amp; hardware store in Rewa,
        known for delivering premium-quality bathroom fittings, sanitaryware, pipes,
        plumbing solutions, and high-quality Nerolac Paints.
      <br/>
      <br/>
      With a strong focus on durability, modern design, and fair pricing,
        we proudly serve homeowners, builders, and contractors with reliable products
        and expert guidance.
     </p>
    </div>
    <!-- Right Image -->
    <div class="about-img right">
     <img alt="Sanitary Products Display" src="showroom3.jpeg"/>
    </div>
   </div>
  </section>
  <!-- WHY CHOOSE US -->
  <section class="highlight scroll-animate">
   <h2 class="text-3xl font-bold text-red-700 mb-4">
    Why Choose Us
   </h2>
   <ul>
    <li>
     ✔ Wide range of premium sanitary &amp; hardware products
    </li>
    <li>
     ✔ Trusted by homeowners and contractors
    </li>
    <li>
     ✔ Honest pricing and quality assurance
    </li>
    <li>
     ✔ Friendly service and expert guidance
    </li>
    <li>
     ✔ High-quality Nerolac Paints for homes and commercial spaces
    </li>
   </ul>
  </section>
  <!-- CTA -->
  <section class="cta scroll-animate">
   <h2>
    Build Your Perfect Bathroom Today
   </h2>
   <a class="btn" href="contact.html">
    Contact Us
   </a>
  </section>
  <!-- WHATSAPP -->
  <a class="whatsapp-icon" href="https://wa.me/917000903314">
   <i class="fab fa-whatsapp">
   </i>
  </a>
  <!-- FOOTER -->
  <footer class="footer">
   <div class="footer-container">
    <div>
     <img alt="Raj Sanitary Logo" class="h-16 mb-3" src="logo.png"/>
     <p>
      Premium Sanitary &amp; Hardware Store in Rewa
     </p>
    </div>
    <div>
     <h3>
      Quick Links
     </h3>
     <a href="index.html">
      Home
     </a>
     <br/>
     <a href="products.html">
      Products
     </a>
     <br/>
     <a href="contact.html">
      Contact
     </a>
    </div>
    <div>
     <h3>
      Contact
     </h3>
     <p>
      📞 7000903314
     </p>
     <p>
      📍 Rewa, Madhya Pradesh
     </p>
    </div>
   </div>
   <div class="footer-bottom">
    ©
    <span id="year">
    </span>
    Raj Sanitary. All Rights Reserved.
   </div>
  </footer>
  <script>
   function miniSlider(cls){
  const imgs=document.querySelectorAll(cls+" img");
  let i=0;
  setInterval(()=>{
    imgs[i].classList.remove("active");
    i=(i+1)%imgs.length;
    imgs[i].classList.add("active");
  },2500);
}

miniSlider(".cpvc-mini");
miniSlider(".swr-mini");
miniSlider(".tank-mini");
miniSlider(".bath-mini");
  </script>
  <script>
   document.getElementById("year").innerText=new Date().getFullYear();

const observer=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){e.target.classList.add("show")}
  })
},{threshold:.15});

document.querySelectorAll(".scroll-animate").forEach(el=>observer.observe(el));
  </script>
 </body>
</html>"""