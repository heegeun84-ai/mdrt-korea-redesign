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
<title>한국MDRT협회 · Million Dollar Round Table Korea</title>
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

/* hero */
#hero{background:linear-gradient(180deg,#fbfcfe,#eef3fa);border-bottom:1px solid var(--line);padding:150px 0 100px;position:relative;overflow:hidden}
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
.about-vals{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.val{padding:28px 26px;background:#fff}
.val .ic{font-size:15px;font-weight:800;color:var(--blue);letter-spacing:.12em;margin-bottom:12px}
.val h4{font-size:16.5px;font-weight:800;color:var(--ink);margin-bottom:6px}
.val p{font-size:13.5px;color:var(--muted);line-height:1.7}

/* events */
.egrid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.ecard{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:.25s;cursor:pointer}
.ecard:hover{border-color:var(--line2);box-shadow:var(--sh);transform:translateY(-3px)}
.ecard .thumb{aspect-ratio:16/9;position:relative;display:grid;place-items:center;background:var(--bg3)}
.ecard .thumb .tag{position:absolute;top:14px;left:14px;font-size:10.5px;font-weight:800;letter-spacing:.08em;background:#fff;color:var(--navy);padding:5px 11px;border-radius:5px;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.ecard .thumb .em{font-size:38px;opacity:.5}
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
.lgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.lcard{text-align:center}
.lface{aspect-ratio:1;border-radius:12px;background:linear-gradient(160deg,#eef3fa,#dfe8f4);display:grid;place-items:center;
  font-size:30px;font-weight:800;color:var(--blue-soft);letter-spacing:.04em;border:1px solid var(--line);margin-bottom:14px}
.lcard .lrole{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.06em}
.lcard .lname{font-size:17px;font-weight:800;color:var(--ink);margin-top:3px}
.lcard .lname em{font-style:normal;font-size:12px;color:var(--muted);font-weight:600;display:block;margin-top:2px}

/* membership */
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

@media(max-width:900px){
  #hero .wrap,.about-grid,.ethics-grid{grid-template-columns:1fr;gap:36px}
  .heroemblem{display:none}
  .stats .wrap{grid-template-columns:1fr 1fr}.stat:nth-child(2){border-right:none}.stat{border-bottom:1px solid var(--line)}
  .egrid,.rgrid,.tiers,.lgrid,.about-vals{grid-template-columns:1fr}
  .lgrid{grid-template-columns:1fr 1fr}.fgrid{grid-template-columns:1fr 1fr}
  .navlinks,.navcta{display:none}.menu-btn{display:flex}
}
</style>
</head>
<body>

<nav id="nav"><div class="wrap">
  <a href="#hero" class="logo"><img src="data:image/png;base64,__EMB_N__" alt="MDRT"><span class="lt">한국MDRT협회<small>MDRT KOREA</small></span></a>
  <div class="navlinks">
    <a href="#about">협회 소개</a><a href="#events">행사</a><a href="#resources">리소스</a><a href="#leaders">임원</a><a href="#membership">멤버십</a><a href="#ethics">윤리강령</a>
  </div>
  <a href="#membership" class="navcta">회원 가입</a>
  <button class="menu-btn"><span></span><span></span><span></span></button>
</div></nav>

<section id="hero"><div class="wrap">
  <div>
    <span class="eyebrow">Million Dollar Round Table · Korea</span>
    <h1>세계 최고 <em>보험·재정 전문가</em>가<br>함께하는 원탁</h1>
    <p>1927년 설립된 MDRT는 전 세계 80여 개국, 500여 개 회사의 최상위 전문가가 모이는 국제 조직입니다. 한국MDRT협회는 최고의 전문성과 윤리로 고객의 삶을 지키는 3,000여 명의 회원과 함께합니다.</p>
    <div class="btns">
      <a href="#membership" class="btn primary">회원 가입 안내 →</a>
      <a href="#about" class="btn ghost">협회 소개</a>
    </div>
  </div>
  <div class="heroemblem"><div class="ring2"></div><div class="ring"></div><img src="data:image/png;base64,__EMB_N__" alt="MDRT Emblem"></div>
</div></section>

<div class="stats"><div class="wrap">
  <div class="stat reveal"><b>3,084<em>명</em></b><span>2026 한국협회 회원</span></div>
  <div class="stat reveal"><b>80<em>+</em></b><span>전 세계 참여 국가</span></div>
  <div class="stat reveal"><b>500<em>+</em></b><span>글로벌 참여 회사</span></div>
  <div class="stat reveal"><b>1927</b><span>MDRT 설립 연도</span></div>
</div></div>

<section class="blk" id="about"><div class="wrap about-grid">
  <div class="reveal">
    <span class="eyebrow">About MDRT</span>
    <h2 class="t" style="margin:14px 0 20px">신뢰받는 전문가의<br>기준이 되다</h2>
    <p class="lead">MDRT(백만달러원탁회의)는 생명보험 및 금융서비스 분야에서 탁월한 성과와 최고 수준의 윤리를 갖춘 전문가만이 가입할 수 있는 국제 협회입니다. 한국MDRT협회는 회원의 전문성 향상과 품격 있는 문화를 이끌며, 고객과 사회로부터 신뢰받는 재정 전문가 상을 만들어갑니다.</p>
  </div>
  <div class="about-vals reveal">
    <div class="val"><div class="ic">01</div><h4>전문성</h4><p>지속적 학습과 검증된 성과로 최고 수준의 역량을 갖춥니다.</p></div>
    <div class="val"><div class="ic">02</div><h4>윤리</h4><p>고객을 최우선에 두는 엄격한 윤리강령을 실천합니다.</p></div>
    <div class="val"><div class="ic">03</div><h4>생산성</h4><p>탁월한 성과로 업계의 기준을 제시합니다.</p></div>
    <div class="val"><div class="ic">04</div><h4>나눔</h4><p>사회공헌과 자선으로 더 나은 세상에 기여합니다.</p></div>
  </div>
</div></section>

<section class="blk bg2" id="events"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow">Events</span>
    <h2 class="t">함께 성장하는 무대</h2>
    <p class="lead">연차총회부터 지역 워크숍까지, 회원의 성장을 위한 다양한 행사가 열립니다.</p>
  </div>
  <div class="egrid">
    <div class="ecard reveal"><div class="thumb"><span class="tag">ANNUAL MEETING</span><span class="em">🏛️</span></div>
      <div class="body"><div class="date">2026 · Anaheim, USA</div><h3>2026 MDRT 애너하임 연차총회</h3><p>전 세계 회원이 모이는 최대 규모의 국제 컨퍼런스. 글로벌 인사이트와 네트워킹의 장.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb"><span class="tag">MDRT DAY</span><span class="em">🎖️</span></div>
      <div class="body"><div class="date">2026 · Seoul</div><h3>한국 MDRT Day</h3><p>국내 회원이 한자리에 모여 성취를 나누고 시상하는 협회 대표 연례 행사.</p><div class="go">자세히 보기 →</div></div></div>
    <div class="ecard reveal"><div class="thumb"><span class="tag">CONFERENCE</span><span class="em">🌏</span></div>
      <div class="body"><div class="date">Global · 연중</div><h3>글로벌 컨퍼런스 · 워크숍</h3><p>지역별 스페셜 세션과 실무 워크숍으로 언제 어디서나 성장할 수 있습니다.</p><div class="go">자세히 보기 →</div></div></div>
  </div>
</div></section>

<section class="blk" id="resources"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow">Resource Zone</span>
    <h2 class="t">최고에게서 배우다</h2>
    <p class="lead">세계적 전문가들의 강연과 검증된 세일즈 아이디어를 회원 전용으로 제공합니다.</p>
  </div>
  <div class="rgrid">
    <div class="rcard reveal"><div class="ic">🎬</div><h4>강연 영상</h4><p>연차총회·컨퍼런스의 명강연을 언제든 다시 봅니다.</p></div>
    <div class="rcard reveal"><div class="ic">📖</div><h4>RTT 간행물</h4><p>Round the Table 등 정기 간행물과 전문 콘텐츠.</p></div>
    <div class="rcard reveal"><div class="ic">💡</div><h4>세일즈 아이디어</h4><p>현장에서 검증된 실전 세일즈 인사이트.</p></div>
    <div class="rcard reveal"><div class="ic">✉️</div><h4>E-뉴스레터</h4><p>협회 소식과 최신 트렌드를 정기적으로.</p></div>
  </div>
</section></div>

<section class="blk bg2" id="leaders"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow">Leadership · 2026</span>
    <h2 class="t">협회를 이끄는 사람들</h2>
    <p class="lead">회원의 성장과 협회의 미래를 함께 만들어가는 2026년도 집행부입니다.</p>
  </div>
  <div class="lgrid">
    <div class="lcard reveal"><div class="lface">회장</div><div class="lrole">회 장</div><div class="lname">○○○<em>Chair</em></div></div>
    <div class="lcard reveal"><div class="lface">부회장</div><div class="lrole">부회장</div><div class="lname">○○○<em>Vice Chair</em></div></div>
    <div class="lcard reveal"><div class="lface">총무</div><div class="lrole">총 무</div><div class="lname">○○○<em>Secretary</em></div></div>
    <div class="lcard reveal"><div class="lface">재정</div><div class="lrole">재 정</div><div class="lname">○○○<em>Treasurer</em></div></div>
  </div>
  <p class="center" style="margin-top:20px;font-size:12.5px;color:var(--muted)">※ 임원 사진·명단은 실제 자료로 교체 예정입니다.</p>
</div></section>

<section class="blk" id="membership"><div class="wrap">
  <div class="shead center reveal">
    <span class="eyebrow">Membership</span>
    <h2 class="t">최고의 자리에 합류하세요</h2>
    <p class="lead">성과에 따라 MDRT, COT, TOT 자격으로 인정받으며, 전 세계 전문가 네트워크의 일원이 됩니다.</p>
  </div>
  <div class="tiers">
    <div class="tier reveal"><div class="lvl">MDRT</div><h3>Round Table</h3><p>MDRT 회원 자격 기준을 달성한 우수 전문가.</p><div class="req">생산성 · 윤리 기준 충족</div></div>
    <div class="tier hl reveal"><span class="badge">COURT</span><div class="lvl">COT</div><h3>Court of the Table</h3><p>MDRT 기준의 3배를 달성한 최상위 전문가.</p><div class="req">MDRT 기준 3배 달성</div></div>
    <div class="tier reveal"><div class="lvl">TOT</div><h3>Top of the Table</h3><p>MDRT 기준의 6배를 달성한 정상급 전문가.</p><div class="req">MDRT 기준 6배 달성</div></div>
  </div>
  <div class="center" style="margin-top:40px"><a href="#" class="btn primary">회원 등록 안내 →</a></div>
</div></section>

<section class="blk bg2" id="ethics"><div class="wrap ethics-grid">
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

<section class="blk ctaband"><div class="wrap reveal">
  <span class="eyebrow">Join Us</span>
  <h2 class="t">당신의 다음 도약,<br>한국MDRT협회와 함께</h2>
  <p class="lead center">최고의 전문가들과 함께 성장하고, 고객에게 더 큰 가치를 전하세요.</p>
  <div class="btns">
    <a href="#membership" class="btn primary">회원 가입 안내</a>
    <a href="#events" class="btn ghost">다가오는 행사 보기</a>
  </div>
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
</script>
</body>
</html>"""

html=HTML.replace("__EMB_N__",b64("mdrt-navy.png")).replace("__EMB_W__",b64("mdrt-white.png")).replace("__EMB_G__",b64("mdrt-gold.png"))
open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(html)
print("written:",len(html),"bytes")
