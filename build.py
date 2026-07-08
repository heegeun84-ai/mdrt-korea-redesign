#!/usr/bin/env python3
# 한국MDRT협회 리디자인 시안 — 일본 MDRT 톤(밝고 절제된 미니멀)
import os, base64
HERE=os.path.dirname(os.path.abspath(__file__))
def b64(n):
    p=os.path.join(HERE,"assets",n)
    return base64.b64encode(open(p,"rb").read()).decode() if os.path.exists(p) else ""

HTML=r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="세계 최고 보험·재정 전문가가 함께하는 국제 조직, 한국MDRT협회.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="한국MDRT협회">
<meta property="og:title" content="한국MDRT협회 · Million Dollar Round Table Korea">
<meta property="og:description" content="세계 최고 보험·재정 전문가가 함께하는 국제 조직, 한국MDRT협회.">
<meta property="og:image" content="https://mdrt-korea.vercel.app/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://mdrt-korea.vercel.app/">
<meta name="twitter:card" content="summary_large_image">
<title>한국MDRT협회 · Million Dollar Round Table Korea</title>
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="assets/icon-180.png">
<link rel="icon" type="image/png" href="assets/icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="한국MDRT협회">
<meta name="application-name" content="한국MDRT협회">
<meta name="theme-color" content="#1b3a63">
<link rel="stylesheet" href="https://fastly.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{
  --navy:#1b3a63; --blue:#2f5c9e; --blue-soft:#5680bd; --ink:#182234; --body:#4b586b; --muted:#97a1b2;
  --line:#e9edf3; --line2:#dde4ee; --bg:#ffffff; --bg2:#f6f8fb; --bg3:#eef3f9;
  --sh:0 1px 2px rgba(24,45,80,.04),0 10px 34px rgba(24,45,80,.05);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Pretendard,-apple-system,system-ui,sans-serif;color:var(--body);background:var(--bg);
  -webkit-font-smoothing:antialiased;line-height:1.7;letter-spacing:-.01em;font-size:16px}
a{color:inherit;text-decoration:none}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:700;letter-spacing:.2em;color:var(--blue);text-transform:uppercase}
.eyebrow::before{content:"";width:24px;height:1px;background:var(--blue-soft);opacity:.6}
.center .eyebrow::before{display:none}
h2.t{font-size:clamp(25px,3.6vw,37px);font-weight:800;color:var(--ink);letter-spacing:-.035em;line-height:1.25}
.lead{font-size:16px;color:var(--body);max-width:40em;line-height:1.85}
.btn{display:inline-flex;align-items:center;gap:8px;font-size:14.5px;font-weight:700;padding:13px 26px;border-radius:6px;transition:.2s;cursor:pointer;border:1.5px solid transparent}
.btn.primary{background:var(--navy);color:#fff}
.btn.primary:hover{background:#132c4d}
.btn.ghost{border-color:var(--line2);color:var(--ink)}
.btn.ghost:hover{border-color:var(--navy);color:var(--navy)}

/* nav */
nav{position:fixed;top:0;left:0;right:0;z-index:50;transition:.3s;padding:20px 0;border-bottom:1px solid transparent}
nav.scrolled{background:rgba(255,255,255,.92);backdrop-filter:blur(14px);border-color:var(--line);padding:14px 0}
nav .wrap{display:flex;align-items:center;gap:28px}
.logo{display:flex;align-items:center;gap:11px}
.logo img{height:32px}
.logo .lt{font-weight:800;font-size:16px;color:var(--ink);letter-spacing:-.02em;line-height:1.05}
.logo .lt small{display:block;font-size:9.5px;font-weight:600;letter-spacing:.16em;color:var(--muted)}
.navlinks{display:flex;gap:28px;margin-left:auto}
.navlinks a{font-size:14.5px;font-weight:600;color:var(--body);transition:.2s}
.navlinks a:hover{color:var(--navy)}
.navcta{font-size:13.5px;font-weight:700;padding:9px 18px;border-radius:6px;background:var(--navy);color:#fff;transition:.2s}
.navcta:hover{background:#132c4d}
.menu-btn{display:none;margin-left:auto;background:none;border:none;cursor:pointer;flex-direction:column;gap:5px;padding:6px}
.menu-btn span{width:23px;height:2px;background:var(--ink)}

/* banner */
.banner{padding-top:82px}
.bnr{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:1600/558;border:1px solid var(--line);box-shadow:var(--sh);background:#0f2544}
.bnr .slide{position:absolute;inset:0;background:center/cover no-repeat;opacity:0;transition:opacity .8s}
.bnr .slide.on{opacity:1}
.bnr .bcap{position:relative;z-index:2;color:#fff;max-width:66%}
.bnr .bcap .bk{font-size:11.5px;font-weight:800;letter-spacing:.14em;color:var(--blue-soft);text-transform:uppercase}
.bnr .bcap b{display:block;font-size:clamp(19px,3vw,31px);font-weight:800;letter-spacing:-.03em;margin:6px 0 7px;line-height:1.25}
.bnr .bcap span.d{font-size:14px;opacity:.85}
.bnr .dots{position:absolute;bottom:16px;right:20px;z-index:3;display:flex;gap:7px}
.bnr .dots i{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer;transition:.25s}
.bnr .dots i.on{background:#fff;width:22px;border-radius:5px}
.bnr .bhint{position:absolute;top:12px;left:14px;z-index:3;font-size:10px;font-weight:700;color:rgba(255,255,255,.72);letter-spacing:.05em;background:rgba(0,0,0,.22);padding:3px 9px;border-radius:5px}
/* member search */
.msearch{padding:32px 0 4px}
.msbox{text-align:center;padding:40px 24px;background:var(--bg2);border:1px solid var(--line);border-radius:16px}
.msbox h3{font-size:22px;font-weight:800;color:var(--ink);margin:6px 0 18px;letter-spacing:-.02em}
.msinput{display:flex;gap:8px;max-width:540px;margin:0 auto}
.msinput input{flex:1;padding:15px 20px;font-size:16px;border:1.5px solid var(--line2);border-radius:8px;background:#fff}
.msinput input:focus{border-color:var(--navy);outline:none}
.msinput button{padding:15px 26px;font-size:15px;font-weight:700;background:var(--navy);color:#fff;border:none;border-radius:8px;cursor:pointer;white-space:nowrap}
.msinput button:hover{background:#132c4d}
.msbox .soft{font-size:13px;color:var(--muted);margin-top:14px}
@media(max-width:900px){.bnr{aspect-ratio:16/9}.bnr .bcap{max-width:88%}}

/* hero */
#hero{background:linear-gradient(180deg,#fbfcfe,#eef3fa);border-bottom:1px solid var(--line);padding:64px 0 90px;position:relative;overflow:hidden}
#hero .wrap{display:grid;grid-template-columns:1.25fr .75fr;gap:56px;align-items:center;position:relative;z-index:2}
#hero h1{font-size:clamp(32px,4.8vw,52px);font-weight:800;letter-spacing:-.04em;line-height:1.24;color:var(--ink);margin:20px 0 24px}
#hero h1 em{font-style:normal;color:var(--navy)}
#hero p{font-size:clamp(15px,1.7vw,17.5px);color:var(--body);max-width:33em;margin-bottom:34px;line-height:1.85}
#hero .btns{display:flex;gap:12px;flex-wrap:wrap}
.heroemblem{display:grid;place-items:center;position:relative}
.heroemblem img{width:min(260px,72%);opacity:.92}
.heroemblem .ring{position:absolute;inset:0;margin:auto;width:74%;aspect-ratio:1;border:1px solid var(--line2);border-radius:50%}
.heroemblem .ring2{position:absolute;inset:0;margin:auto;width:92%;aspect-ratio:1;border:1px solid var(--line);border-radius:50%}

/* stats */
.stats{border-bottom:1px solid var(--line);background:#fff}
.stats .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.stat{padding:46px 20px;text-align:center;border-right:1px solid var(--line)}
.stat:last-child{border:none}
.stat b{display:block;font-size:clamp(30px,3.8vw,44px);font-weight:800;letter-spacing:-.03em;line-height:1;color:var(--navy)}
.stat b em{font-style:normal;color:var(--blue-soft);font-size:.55em;margin-left:1px}
.stat span{display:block;margin-top:11px;font-size:13px;color:var(--muted);letter-spacing:.01em}

/* sections */
section.blk{padding:clamp(72px,9vw,116px) 0}
.bg2{background:var(--bg2)}
.center{text-align:center}.center .lead{margin:16px auto 0}
.shead{margin-bottom:56px}.shead h2.t{margin-top:14px}

/* about */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.aboutimg{width:100%;border-radius:14px;border:1px solid var(--line);display:block;box-shadow:var(--sh)}
.about-vals{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-top:52px}
.val{padding:28px 26px;background:#fff}
.val .ic{font-size:15px;font-weight:800;color:var(--blue);letter-spacing:.12em;margin-bottom:12px}
.val h4{font-size:16.5px;font-weight:800;color:var(--ink);margin-bottom:6px}
.val p{font-size:13.5px;color:var(--muted);line-height:1.7}

/* events */
.egrid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.ecard{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:.25s;cursor:pointer}
.ecard:hover{border-color:var(--line2);box-shadow:var(--sh);transform:translateY(-3px)}
.ecard .thumb{aspect-ratio:16/9;position:relative;background:var(--bg3) center/cover no-repeat}
.ecard .thumb::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,37,68,.05),rgba(15,37,68,.22))}
.ecard .thumb .tag{position:absolute;top:14px;left:14px;z-index:2;font-size:10.5px;font-weight:800;letter-spacing:.08em;background:#fff;color:var(--navy);padding:5px 11px;border-radius:5px;box-shadow:0 1px 4px rgba(0,0,0,.1)}
.ecard .body{padding:24px}
.ecard .date{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.03em}
.ecard h3{font-size:18px;font-weight:800;color:var(--ink);margin:7px 0 9px;letter-spacing:-.02em;line-height:1.4}
.ecard p{font-size:13.5px;color:var(--muted);line-height:1.7}
.ecard .go{margin-top:16px;font-size:13px;font-weight:700;color:var(--navy)}

/* resources */
.rgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.rcard{padding:34px 26px;background:#fff;transition:.25s}
.rcard:hover{background:var(--bg2)}
.rcard .ic{font-size:26px;margin-bottom:16px;opacity:.85}
.rcard h4{font-size:16.5px;font-weight:800;color:var(--ink);margin-bottom:8px;letter-spacing:-.02em}
.rcard p{font-size:13.5px;color:var(--muted);line-height:1.7}

/* leaders — 인간미(일본 톤) */
.lgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:20px}
/* whole person */
.wpgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.wp{padding:28px 24px;background:#fff;transition:.25s}
.wp:hover{background:var(--bg2)}
.wp .wn{font-size:12px;font-weight:800;color:var(--blue-soft);letter-spacing:.1em}
.wp h4{font-size:16.5px;font-weight:800;color:var(--ink);margin:9px 0 6px}
.wp p{font-size:13px;color:var(--muted);line-height:1.65}
.wp.logo{display:none}
.wp.intro{background:var(--navy);color:#fff;display:flex;flex-direction:column;justify-content:center}
.wp.intro b{font-size:18px;font-weight:800;color:#fff;letter-spacing:-.02em}
.wp.intro span{font-size:12.5px;color:rgba(255,255,255,.72);margin-top:7px;line-height:1.6}
/* join */
.jsteps{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:6px}
.jstep{text-align:center;padding:8px}
.jstep .jn{width:50px;height:50px;border-radius:50%;background:var(--bg3);color:var(--navy);display:grid;place-items:center;font-size:18px;font-weight:800;margin:0 auto 15px;border:1px solid var(--line2)}
.jstep h4{font-size:15.5px;font-weight:800;color:var(--ink);margin-bottom:5px}
.jstep p{font-size:13px;color:var(--muted);line-height:1.6}
.lcard{text-align:center}
.lface{aspect-ratio:1;border-radius:12px;background:linear-gradient(160deg,#eef3fa,#dfe8f4);overflow:hidden;border:1px solid var(--line);margin-bottom:14px;display:grid;place-items:center;font-size:30px;font-weight:800;color:var(--blue-soft)}
.lface img{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(.1)}
.lcard .lrole{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.06em}
.lcard .lname{font-size:17px;font-weight:800;color:var(--ink);margin-top:3px}
.lcard .lname em{font-style:normal;font-size:12px;color:var(--muted);font-weight:600;display:block;margin-top:2px}

/* membership */
.subhead{text-align:center;font-size:12.5px;font-weight:800;letter-spacing:.12em;color:var(--blue);text-transform:uppercase;margin-bottom:24px}
.subhead::before,.subhead::after{content:"";display:inline-block;width:26px;height:1px;background:var(--blue-soft);opacity:.5;vertical-align:middle;margin:0 12px}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:6px}
.tier{background:#fff;border:1px solid var(--line);border-radius:14px;padding:36px 30px;transition:.25s;position:relative}
.tier:hover{border-color:var(--line2);box-shadow:var(--sh)}
.tier.hl{background:var(--navy);border-color:var(--navy);color:#fff}
.tier .lvl{font-size:12px;font-weight:800;letter-spacing:.16em;color:var(--blue)}
.tier.hl .lvl{color:var(--blue-soft)}
.tier h3{font-size:23px;font-weight:800;margin:10px 0 8px;color:var(--ink);letter-spacing:-.02em}
.tier.hl h3{color:#fff}
.tier p{font-size:13.5px;color:var(--muted);line-height:1.7}
.tier.hl p{color:rgba(255,255,255,.72)}
.tier .req{margin-top:18px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--body);font-weight:600}
.tier.hl .req{border-color:rgba(255,255,255,.15);color:rgba(255,255,255,.85)}
.tier .badge{position:absolute;top:20px;right:22px;font-size:10px;font-weight:800;letter-spacing:.08em;color:var(--blue-soft)}

/* ethics */
.ethics-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:start}
.elist{display:grid;gap:2px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.ei{display:flex;gap:16px;align-items:flex-start;padding:22px 24px;background:#fff}
.ei .n{flex:none;width:30px;height:30px;border-radius:50%;border:1.5px solid var(--blue);color:var(--blue);display:grid;place-items:center;font-size:13px;font-weight:800}
.ei b{color:var(--ink);font-size:15.5px;font-weight:700;display:block;margin-bottom:2px}
.ei span{font-size:13.5px;color:var(--muted)}

/* cta */
.ctaband{background:var(--navy);color:#fff;text-align:center;border-radius:0}
.ctaband .eyebrow{color:var(--blue-soft)}.ctaband .eyebrow::before{background:var(--blue-soft)}
.ctaband h2.t{color:#fff;margin-top:14px;margin-bottom:14px}
.ctaband .lead{color:rgba(255,255,255,.78)}
.ctaband .btn.primary{background:#fff;color:var(--navy)}.ctaband .btn.primary:hover{background:#eaf0f8}
.ctaband .btn.ghost{border-color:rgba(255,255,255,.35);color:#fff}.ctaband .btn.ghost:hover{background:rgba(255,255,255,.1);border-color:#fff}
.ctaband .btns{display:flex;gap:12px;justify-content:center;margin-top:30px;flex-wrap:wrap}

/* footer */
footer{background:#0f2544;color:rgba(255,255,255,.7);padding:66px 0 28px;font-size:13.5px}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:44px;padding-bottom:44px;border-bottom:1px solid rgba(255,255,255,.1)}
footer .logo .lt{color:#fff}footer .logo .lt small{color:rgba(255,255,255,.5)}
footer .fcol h5{font-size:13px;font-weight:800;color:#fff;margin-bottom:16px;letter-spacing:.03em}
footer .fcol a{display:block;margin-bottom:10px;color:rgba(255,255,255,.65);transition:.2s}
footer .fcol a:hover{color:#fff}
footer .fdesc{margin-top:16px;max-width:24em;line-height:1.8;color:rgba(255,255,255,.55);font-size:13px}
.fbot{padding-top:26px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:12.5px;color:rgba(255,255,255,.45)}

.reveal{opacity:0;transform:translateY(20px);transition:.7s cubic-bezier(.2,.7,.2,1)}
.reveal.in{opacity:1;transform:none}

.statrow{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-top:52px;background:#fff}
.hlnum{color:var(--blue);font-weight:800}
.tier.hl .hlnum{color:#bcd4f0}
.orgwrap{margin-top:46px}
.orgimg{width:100%;border-radius:14px;border:1px solid var(--line);display:block;box-shadow:var(--sh)}
.mgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:8px}
.mlogo{aspect-ratio:3/2;border:1px solid var(--line);border-radius:12px;display:grid;place-items:center;background:#fff;padding:18px;transition:.25s}
.mlogo:hover{box-shadow:var(--sh);border-color:var(--line2)}
.mlogo img{max-width:100%;max-height:56px;object-fit:contain}
.mlogo span{font-size:clamp(14px,1.7vw,18px);font-weight:800;color:var(--navy);letter-spacing:-.02em;text-align:center;line-height:1.35}
@media(max-width:900px){.mgrid{grid-template-columns:1fr 1fr}}
@media(max-width:900px){
  .about-grid,.ethics-grid{grid-template-columns:1fr;gap:36px}
  .heroemblem{display:none}
  .egrid,.tiers{grid-template-columns:1fr}
  .rgrid,.about-vals,.wpgrid{grid-template-columns:1fr 1fr}
  .wpgrid .intro{grid-column:1/-1}
  .wp.logo{display:grid;place-items:center;background:var(--bg2)}.wp.logo img{width:66px;opacity:.42}
  .lgrid,.fgrid{grid-template-columns:1fr 1fr}
  .statrow{grid-template-columns:1fr 1fr}.statrow .stat:nth-child(2){border-right:none}.statrow .stat{border-bottom:1px solid var(--line)}
  .navlinks,.navcta{display:none}.menu-btn{display:flex}
}
@media(max-width:560px){.bnr .bcap b{font-size:17px}.bnr .bcap .d{font-size:12px}section.blk{padding:58px 0}}
</style>
</head>
<body>

<nav id="nav"><div class="wrap">
  <a href="#top" class="logo"><img src="data:image/png;base64,__EMB_N__" alt="MDRT"><span class="lt">한국MDRT협회<small>MDRT KOREA</small></span></a>
  <div class="navlinks">
    <a href="#wholeperson">전인적 삶</a><a href="#about">MDRT 소개</a><a href="#membership">명예의 전당</a><a href="#events">행사</a><a href="#resources">리소스</a><a href="#leaders">리더</a>
  </div>
  <a href="#membership" class="navcta">명예의 전당</a>
  <button class="menu-btn"><span></span><span></span><span></span></button>
</div></nav>

<section class="banner" id="top"><div class="wrap">
  <div class="bnr" id="bnr">
    <a class="slide on" href="#events" style="background-image:url(assets/bnr1.jpg)"></a>
    <a class="slide" href="#events" style="background-image:url(assets/bnr2.jpg)"></a>
    <div class="dots" id="bdots"></div>
  </div>
</div></section>

<section class="msearch"><div class="wrap">
  <div class="msbox reveal">
    <span class="eyebrow" style="justify-content:center">Member Search</span>
    <h3>회원 검색</h3>
    <div class="msinput"><input id="msq" placeholder="회원 이름을 입력하세요" onkeypress="if(event.key==='Enter')msDo()"><button onclick="msDo()">검색</button></div>
    <p class="soft">한국MDRT협회 <b>공식 회원 검색</b>으로 연결됩니다.</p>
  </div>
</div></section>

<section class="blk bg2" id="wholeperson"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">The Whole Person</span>
    <h2 class="t">균형 잡힌 삶, 전인적 성장</h2>
    <p class="lead">MDRT는 1961년부터 삶의 일곱 영역이 조화를 이루는 '전인적 인간(Whole Person)'을 추구합니다. 성공은 일의 성취를 넘어 삶 전체의 균형에서 완성됩니다.</p>
  </div>
  <div class="wpgrid reveal">
    <div class="wp intro"><b>전인적 인간<br>Whole Person</b><span>1961년 도입된 MDRT의 핵심 철학, 일곱 영역의 조화</span></div>
    <div class="wp"><div class="wn">01</div><h4>관계</h4><p>가족·친구와의 의미 있는 시간, 사랑과 존중의 관계를 소중히 합니다.</p></div>
    <div class="wp"><div class="wn">02</div><h4>건강</h4><p>규칙적 운동과 균형 잡힌 생활로 건강한 몸과 마음을 지킵니다.</p></div>
    <div class="wp"><div class="wn">03</div><h4>교육</h4><p>끊임없는 배움으로 지적 성장을 이어갑니다.</p></div>
    <div class="wp"><div class="wn">04</div><h4>경력</h4><p>전문성과 생산성을 높이고 동료의 성장을 함께 이끕니다.</p></div>
    <div class="wp"><div class="wn">05</div><h4>봉사</h4><p>지역사회에 기여하고 나눔을 실천합니다.</p></div>
    <div class="wp"><div class="wn">06</div><h4>재정</h4><p>분수에 맞는 삶과 지혜로운 자산 관리를 추구합니다.</p></div>
    <div class="wp"><div class="wn">07</div><h4>영성</h4><p>신념에 따라 살며 영적 성장을 지향합니다.</p></div>
    <div class="wp logo"><img src="data:image/png;base64,__EMB_N__" alt="MDRT"></div>
  </div>
</div></section>

<section class="blk bg2" id="about"><div class="wrap">
  <div class="about-grid">
    <div class="reveal">
      <span class="eyebrow">About MDRT</span>
      <h2 class="t" style="margin:14px 0 20px">MDRT란 무엇인가</h2>
      <p class="lead">MDRT(백만달러원탁회의)는 생명보험 및 금융서비스 분야에서 탁월한 성과와 최고 수준의 윤리를 갖춘 전문가만이 가입할 수 있는 국제 협회입니다. 1927년 설립 이래 전 세계 80여 개국·500여 개 회사의 최상위 전문가가 함께하며, 한국MDRT협회는 3,000여 명의 회원과 함께 신뢰받는 재정 전문가 상을 만들어갑니다.</p>
    </div>
    <div class="reveal"><img class="aboutimg" src="assets/about.jpg" alt="MDRT 회원"></div>
  </div>
  <div class="statrow reveal">
    <div class="stat"><b>3,084<em>명</em></b><span>2026 한국협회 회원</span></div>
    <div class="stat"><b>80<em>+</em></b><span>전 세계 참여 국가</span></div>
    <div class="stat"><b>500<em>+</em></b><span>글로벌 참여 회사</span></div>
    <div class="stat"><b>1927</b><span>MDRT 설립 연도</span></div>
  </div>
  <div class="about-vals reveal">
    <div class="val"><div class="ic">01</div><h4>전문성</h4><p>지속적 학습과 검증된 성과로 최고 수준의 역량을 갖춥니다.</p></div>
    <div class="val"><div class="ic">02</div><h4>윤리</h4><p>고객을 최우선에 두는 엄격한 윤리강령을 실천합니다.</p></div>
    <div class="val"><div class="ic">03</div><h4>생산성</h4><p>탁월한 성과로 업계의 기준을 제시합니다.</p></div>
    <div class="val"><div class="ic">04</div><h4>나눔</h4><p>사회공헌과 자선으로 더 나은 세상에 기여합니다.</p></div>
  </div>
</div></section>

<section class="blk" id="membership"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">Hall of Fame</span>
    <h2 class="t">명예의 전당</h2>
    <p class="lead">탁월한 성과와 오랜 헌신으로 MDRT의 역사를 함께 만들어 온 회원들을 기립니다.</p>
  </div>
  <div class="subhead reveal">회원 자격 등급</div>
  <div class="tiers">
    <div class="tier reveal"><div class="lvl">MDRT</div><h3>Round Table</h3><p>MDRT 회원 자격 기준을 달성한 우수 전문가.</p><div class="req">생산성 · 윤리 기준 충족</div></div>
    <div class="tier hl reveal"><span class="badge">COURT</span><div class="lvl">COT</div><h3>Court of the Table</h3><p>MDRT 기준의 <span class="hlnum">3배</span>를 달성한 최상위 전문가.</p><div class="req">MDRT 기준 <span class="hlnum">3배</span> 달성</div></div>
    <div class="tier reveal"><div class="lvl">TOT</div><h3>Top of the Table</h3><p>MDRT 기준의 <span class="hlnum">6배</span>를 달성한 정상급 전문가.</p><div class="req">MDRT 기준 <span class="hlnum">6배</span> 달성</div></div>
  </div>
  <div class="subhead reveal" style="margin-top:60px">명예 회원 등급</div>
  <div class="tiers">
    <div class="tier reveal"><div class="lvl">QUARTER CENTURY</div><h3>쿼터센추리</h3><p><span class="hlnum">25년</span> 이상 MDRT 자격을 달성해 온 회원. 4반세기에 걸친 변함없는 헌신을 기립니다.</p><div class="req"><span class="hlnum">25년</span> 이상 자격 달성</div></div>
    <div class="tier reveal"><div class="lvl">HONOR ROLL</div><h3>아너롤</h3><p><span class="hlnum">15년</span> 이상 MDRT 자격을 달성하며 탁월함을 이어 온 명예 회원에게 부여됩니다.</p><div class="req"><span class="hlnum">15년</span> 이상 자격 달성</div></div>
    <div class="tier reveal"><div class="lvl">LIFE MEMBER</div><h3>종신멤버</h3><p>MDRT 자격을 <span class="hlnum">10년</span> 이상 달성한 회원에게 주어지는 평생의 명예입니다.</p><div class="req"><span class="hlnum">10년</span> 이상 자격 달성</div></div>
  </div>
  <div class="center" style="margin-top:44px"><a href="#" class="btn primary">회원 등록 안내 →</a></div>
  <p class="center" style="font-size:12px;color:var(--muted);margin-top:14px">※ 명예 회원 등급의 정확한 자격 기준은 협회 규정 및 MDRT 본부 기준에 따릅니다.</p>
</div></section>

<section class="blk bg2" id="events"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">Events</span>
    <h2 class="t">행사 스케치</h2>
    <p class="lead">한국 MDRT Day부터 글로벌 컨퍼런스까지, MDRT 대표 행사의 생생한 현장을 소개합니다.</p>
  </div>
  <div class="egrid">
    <div class="ecard reveal"><div class="thumb" style="background-image:url(assets/ev1.jpg)"><span class="tag">MDRT DAY</span></div>
      <div class="body"><div class="date">2025 · 일산</div><h3>2025 한국 MDRT Day</h3><p>일산에서 열린 국내 회원의 축제. 성취를 나누고 시상하는 협회 대표 연례 행사.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb" style="background-image:url(assets/ev2.jpg)"><span class="tag">SPECIAL SESSION</span></div>
      <div class="body"><div class="date">Special Session</div><h3>MDRT 스페셜세션</h3><p>정상급 회원이 자신의 노하우와 인사이트를 나누는 특별 강연 세션.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb" style="background-image:url(assets/ev3.jpg)"><span class="tag">FIRST TIMER</span></div>
      <div class="body"><div class="date">First Timer</div><h3>퍼스트타이머 페스티벌</h3><p>MDRT에 처음 입회한 회원들을 축하하고 환영하는 뜻깊은 축제의 장.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb" style="background-image:url(assets/ev4.jpg)"><span class="tag">ANNUAL MEETING</span></div>
      <div class="body"><div class="date">2026 · Anaheim</div><h3>2026 MDRT 연차총회</h3><p>전 세계 회원이 모이는 최대 규모의 국제 컨퍼런스. 글로벌 인사이트와 네트워킹의 장.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb" style="background-image:url(assets/ev5.jpg)"><span class="tag">GLOBAL</span></div>
      <div class="body"><div class="date">Global Conference</div><h3>MDRT 글로벌컨퍼런스</h3><p>세계 각지에서 열리는 글로벌 컨퍼런스로 국경을 넘어 함께 성장합니다.</p><div class="go">자세히 보기 →</div></div></div>
  </div>
</div></section>

<section class="blk" id="resources"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">Resource Zone</span>
    <h2 class="t">리소스존 · 최고에게서 배우다</h2>
    <p class="lead">세계적 전문가들의 강연과 검증된 세일즈 아이디어를 회원 전용으로 제공합니다.</p>
  </div>
  <div class="rgrid">
    <div class="rcard reveal"><div class="ic">🎬</div><h4>강연 영상</h4><p>연차총회·컨퍼런스의 명강연을 언제든 다시 봅니다.</p></div>
    <div class="rcard reveal"><div class="ic">📖</div><h4>RTT 간행물</h4><p>Round the Table 등 정기 간행물과 전문 콘텐츠.</p></div>
    <div class="rcard reveal"><div class="ic">💡</div><h4>세일즈 아이디어</h4><p>현장에서 검증된 실전 세일즈 인사이트.</p></div>
    <div class="rcard reveal"><div class="ic">✉️</div><h4>E-뉴스레터</h4><p>협회 소식과 최신 트렌드를 정기적으로.</p></div>
  </div>
</div></section>

<section class="blk bg2" id="leaders"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">Leadership · 제24기</span>
    <h2 class="t">협회 리더존</h2>
    <p class="lead">2026.3 ~ 2027.2 제24기 집행위원회. 회원의 성장과 협회의 미래를 함께 만들어갑니다.</p>
  </div>
  <div class="lgrid">
    <div class="lcard reveal"><div class="lface"><img src="assets/ldr1.jpg" alt="남수경 협회장"></div><div class="lrole">협회장</div><div class="lname">남수경<em>메트라이프생명</em></div></div>
    <div class="lcard reveal"><div class="lface"><img src="assets/ldr2.jpg" alt="이종수 제1부회장"></div><div class="lrole">제1부회장</div><div class="lname">이종수<em>KB라이프파트너스</em></div></div>
    <div class="lcard reveal"><div class="lface"><img src="assets/ldr3.jpg" alt="오수현 제2부회장"></div><div class="lrole">제2부회장</div><div class="lname">오수현<em>미래에셋금융서비스</em></div></div>
    <div class="lcard reveal"><div class="lface"><img src="assets/ldr4.jpg" alt="서정훈 사무국장"></div><div class="lrole">사무국장</div><div class="lname">서정훈<em>신한라이프</em></div></div>
    <div class="lcard reveal"><div class="lface"><img src="assets/ldr5.jpg" alt="이승봉 직전협회장"></div><div class="lrole">직전협회장</div><div class="lname">이승봉<em>KB라이프파트너스</em></div></div>
  </div>
  <div class="orgwrap reveal">
    <div class="subhead">제24기 집행위원회 조직도 · 2026.3–2027.2</div>
    <img class="orgimg" src="assets/org-chart.jpg" alt="한국MDRT협회 제24기 조직도 — 집행위원회, 전임협회장단, 감사위원회, 각 분과 위원장 및 지역위원장">
  </div>
</div></section>

<section class="blk" id="ethics"><div class="wrap ethics-grid">
  <div class="reveal">
    <span class="eyebrow">Code of Ethics</span>
    <h2 class="t" style="margin:14px 0 18px">신뢰는 원칙에서<br>시작됩니다</h2>
    <p class="lead">MDRT 회원은 고객의 이익을 최우선으로 하는 엄격한 윤리강령을 준수하며, 이는 전 세계 MDRT가 공유하는 가장 중요한 가치입니다.</p>
  </div>
  <div class="elist reveal">
    <div class="ei"><div class="n">1</div><div><b>고객 최우선</b><span>고객의 이익을 언제나 자신의 이익보다 앞에 둡니다.</span></div></div>
    <div class="ei"><div class="n">2</div><div><b>정직과 투명</b><span>정확하고 정직한 정보로 신뢰를 지킵니다.</span></div></div>
    <div class="ei"><div class="n">3</div><div><b>전문성 유지</b><span>지속적 학습으로 최고의 전문성을 유지합니다.</span></div></div>
    <div class="ei"><div class="n">4</div><div><b>비밀 보장</b><span>고객의 정보를 철저히 보호합니다.</span></div></div>
  </div>
</div></section>

<section class="blk" id="members"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow" style="justify-content:center">Member Companies</span>
    <h2 class="t">함께하는 회원사</h2>
    <p class="lead">한국MDRT협회 회원이 소속된 회원사입니다.</p>
  </div>
  <div class="mgrid reveal">
    <div class="mlogo"><span>신한라이프</span></div>
    <div class="mlogo"><span>메트라이프</span></div>
    <div class="mlogo"><span>교보생명</span></div>
    <div class="mlogo"><span>KB라이프<br>파트너스</span></div>
    <div class="mlogo"><span>AIA프리미어<br>파트너스</span></div>
    <div class="mlogo"><span>KMI에셋</span></div>
    <div class="mlogo"><span>현대홈쇼핑보험</span></div>
  </div>
  <p class="center" style="font-size:12px;color:var(--muted);margin-top:18px">※ 각 회원사 로고 이미지를 주시면 회사명 자리에 동일 크기로 교체합니다.</p>
</div></section>

<footer><div class="wrap">
  <div class="fgrid">
    <div>
      <div class="logo"><img src="data:image/png;base64,__EMB_W__" alt="MDRT" style="height:30px"><span class="lt">한국MDRT협회<small>MDRT KOREA</small></span></div>
      <p class="fdesc">백만달러원탁회의(MDRT) 한국협회. 최고의 전문성과 윤리로 고객과 사회로부터 신뢰받는 재정 전문가의 국제 조직입니다.</p>
    </div>
    <div class="fcol"><h5>협회</h5><a href="#about">협회 소개</a><a href="#ethics">윤리강령</a><a href="#">자선·사회공헌</a><a href="#leaders">임원 소개</a></div>
    <div class="fcol"><h5>멤버십·행사</h5><a href="#membership">회원 등록</a><a href="#">멘토링</a><a href="#events">행사 안내</a><a href="#">상품 주문</a></div>
    <div class="fcol"><h5>리소스</h5><a href="#resources">강연 영상</a><a href="#">간행물</a><a href="#">공지사항</a><a href="#">FAQ</a></div>
  </div>
  <div class="fbot"><span>© 2026 한국MDRT협회 · Million Dollar Round Table Korea</span><span>서울특별시 서초구 · 리디자인 시안(demo)</span></div>
</div></footer>

<script>
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>40));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// 배너 슬라이드
(function(){const s=document.querySelectorAll('#bnr .slide'),dw=document.getElementById('bdots');let i=0;
  s.forEach((_,k)=>{const d=document.createElement('i');if(k===0)d.className='on';d.onclick=()=>go(k);dw.appendChild(d);});
  function go(k){s[i].classList.remove('on');dw.children[i].classList.remove('on');i=k;s[i].classList.add('on');dw.children[i].classList.add('on');}
  setInterval(()=>go((i+1)%s.length),5000);})();
// 회원 검색(시안)
function msDo(){const q=document.getElementById('msq').value.trim();
  if(!q){alert('검색할 회원 이름을 입력하세요');return;}
  window.open('https://mdrtkorea.org/Membership/searchMember?search_type=mem_username&search_value='+encodeURIComponent(q),'_blank');}
</script>
</body>
</html>"""

html=HTML.replace("__EMB_N__",b64("mdrt-navy.png")).replace("__EMB_W__",b64("mdrt-white.png")).replace("__EMB_G__",b64("mdrt-gold.png"))
open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(html)
print("written:",len(html),"bytes")
