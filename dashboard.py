import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="نظام اليقظة التربوية — مدرسة 18 نونبر",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #f4f2ff !important;
    border-left: 1px solid #ddd8fb !important;
}
[data-testid="stSidebar"] * {
    color: #3c3489 !important;
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 16px !important;
    padding: 6px 0 !important;
}

/* ── MAIN BG ── */
.stApp { background: #f9f8ff; }

/* ── METRIC CARDS ── */
[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #ddd8fb;
    border-radius: 14px;
    padding: 1.1rem 1.25rem !important;
    text-align: right !important;
    direction: rtl !important;
}
[data-testid="stMetricLabel"] {
    font-size: 13px !important;
    color: #7f77dd !important;
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl !important;
    text-align: right !important;
}
[data-testid="stMetricValue"] {
    font-size: 36px !important;
    font-weight: 900 !important;
    font-family: 'Tajawal', sans-serif !important;
    color: #26215c !important;
}
[data-testid="stMetricDelta"] { font-size: 12px !important; }

/* ── PAGE TITLES ── */
h1 { color: #26215c !important; font-weight: 900 !important; font-size: 30px !important; font-family: 'Tajawal', sans-serif !important; direction: rtl !important; text-align: right !important; }
h2 { color: #534ab7 !important; font-weight: 700 !important; font-size: 20px !important; font-family: 'Tajawal', sans-serif !important; direction: rtl !important; text-align: right !important; }
h3 { color: #3c3489 !important; font-weight: 500 !important; font-size: 16px !important; font-family: 'Tajawal', sans-serif !important; direction: rtl !important; text-align: right !important; }
p, label, span, li { font-family: 'Tajawal', sans-serif !important; direction: rtl !important; text-align: right !important; color: #444441; }

/* ── BUTTONS ── */
.stButton > button {
    background: #534ab7 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: .7rem 2rem !important;
    width: 100% !important;
}
.stButton > button:hover { background: #3c3489 !important; }

/* ── SELECT / RADIO ── */
.stSelectbox, .stRadio { direction: rtl !important; text-align: right !important; }

/* ── INFO / WARNING / ERROR ── */
.stAlert { direction: rtl !important; font-family: 'Tajawal', sans-serif !important; font-size: 15px !important; }

/* ── DIVIDER ── */
hr { border-color: #ddd8fb !important; }

/* ── HTML ELEMENTS ── */
.banner {
    background: rgba(226,75,74,.08);
    border: 1px solid rgba(226,75,74,.3);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 1rem;
    direction: rtl;
    text-align: right;
}
.banner-num { font-size: 52px; font-weight: 900; color: #a32d2d; line-height: 1; display: block; }
.banner-text { font-size: 15px; color: #791f1f; line-height: 1.6; }

.human-wrap {
    display: flex; flex-wrap: wrap; gap: 7px;
    background: #ffffff; border-radius: 14px;
    padding: 1.25rem; border: 1px solid #ddd8fb;
    justify-content: flex-start;
}
.hu { font-size: 26px; line-height: 1; cursor: default; }

.leg-row { display: flex; gap: 16px; margin-top: .75rem; flex-wrap: wrap; }
.leg-item { display: flex; align-items: center; gap: 5px; font-size: 13px; color: #5f5e5a; font-family: 'Tajawal', sans-serif; }

.qcard {
    background: #f4f2ff;
    border-right: 4px solid #534ab7;
    border-radius: 0 10px 10px 0;
    padding: .875rem 1rem;
    margin-bottom: .75rem;
    direction: rtl; text-align: right;
}
.qcard-text { font-size: 17px; font-weight: 700; color: #26215c; font-style: italic; margin-bottom: .4rem; font-family: 'Tajawal', sans-serif; }
.qcard-meta { font-size: 12px; color: #7f77dd; font-family: 'Tajawal', sans-serif; }

.reco-card {
    background: #ffffff;
    border: 1px solid #ddd8fb;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: .75rem;
    direction: rtl; text-align: right;
    display: flex; gap: .75rem; align-items: flex-start;
}
.reco-num {
    background: rgba(83,74,183,.1);
    color: #534ab7;
    border-radius: 8px;
    padding: 4px 10px;
    font-size: 12px; font-weight: 900;
    flex-shrink: 0;
    font-family: 'Tajawal', sans-serif;
}
.reco-body { font-size: 13px; color: #444441; line-height: 1.6; font-family: 'Tajawal', sans-serif; }
.reco-title { font-size: 15px; font-weight: 700; color: #26215c; margin-bottom: 4px; }

.section-label {
    font-size: 10px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: #b4b2a9;
    border-bottom: 1px solid #ddd8fb;
    padding-bottom: .4rem; margin-bottom: .875rem;
    direction: rtl; text-align: right;
    font-family: 'DM Sans', 'Tajawal', sans-serif;
}

.risk-score-box {
    background: #ffffff; border: 1px solid #ddd8fb;
    border-radius: 16px; padding: 2rem; text-align: center;
    direction: rtl;
}
.risk-big { font-size: 72px; font-weight: 900; line-height: 1; font-family: 'Tajawal', sans-serif; }
.risk-label { font-size: 18px; color: #7f77dd; margin-top: .5rem; font-family: 'Tajawal', sans-serif; }
</style>
""", unsafe_allow_html=True)

# ── DATA ──
@st.cache_data
def load():
    df = pd.read_csv('cleaned_data.csv')
    df.columns = df.columns.str.strip()
    df['عدد أيام الغياب'] = pd.to_numeric(df['عدد أيام الغياب'], errors='coerce').fillna(0)
    df['سهولة الفهم'] = pd.to_numeric(df['سهولة الفهم'], errors='coerce').fillna(0)
    df['الجنس'] = df['الجنس'].astype(str).str.strip().str.replace('"','').str.replace("'","")
    return df

df = load()
N = len(df)
HIGH = int((df['عدد أيام الغياب'] >= 3).sum())
MED  = int(((df['عدد أيام الغياب'] > 0) & (df['عدد أيام الغياب'] < 3)).sum())
SAFE = int((df['عدد أيام الغياب'] == 0).sum())

CHART_THEME = dict(
    plot_bgcolor='#ffffff', paper_bgcolor='#ffffff',
    font=dict(family='Tajawal', color='#5f5e5a', size=13),
    margin=dict(l=10, r=10, t=30, b=10),
)

def theme(**overrides):
    base = dict(CHART_THEME)
    if 'xaxis' not in overrides:
        overrides['xaxis'] = dict(gridcolor='#e8e6f0', zerolinecolor='#e8e6f0')
    if 'yaxis' not in overrides:
        overrides['yaxis'] = dict(gridcolor='#e8e6f0', zerolinecolor='#e8e6f0')
    base.update(overrides)
    return base

# ── SIDEBAR ──
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("""<div style='text-align:center;padding:.5rem 0 1rem'>
<div style='font-size:26px;font-weight:900;color:#26215c;font-family:Tajawal,sans-serif'>🛡️ نظام اليقظة</div>
<div style='font-size:12px;color:#7f77dd;margin-top:3px;font-family:Tajawal,sans-serif'>مدرسة 18 نونبر · فاس</div>
</div>""", unsafe_allow_html=True)

page = st.sidebar.radio("", [
    "📊  نظرة عامة",
    "🔍  تحليل عمقي",
    "💬  صوت التلاميذ",
    "💡  خطة التدخل",
    "🤖  نظام الإنذار المبكر"
], label_visibility="collapsed")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown(f"""<div style='font-size:12px;color:#7f77dd;text-align:center;font-family:Tajawal,sans-serif'>
31 استبيان · أبريل 2026<br>بيانات حقيقية من التلاميذ
</div>""", unsafe_allow_html=True)

# ════════════════════════════════════════
# PAGE 1: نظرة عامة
# ════════════════════════════════════════
if page == "📊  نظرة عامة":
    st.markdown("<h1>التقرير الإحصائي الاستراتيجي — مدرسة 18 نونبر</h1>", unsafe_allow_html=True)

    st.markdown(f"""<div class='banner'>
        <span class='banner-num'>71%</span>
        <span class='banner-text'>من تلاميذ مدرسة 18 نونبر يغيبون 3 أيام أو أكثر كل شهر — 22 تلميذاً من أصل 31.
        هذه أرقام حقيقية، من أطفال جلسوا وملؤوا هذا الاستبيان بأيديهم.</span>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔴 غياب حرج (3+ أيام)", "71%", "22 تلميذاً")
    c2.metric("🏠 مشاكل أسرية", "45%", "السبب الأول")
    c3.metric("👥 عدوى اجتماعية", "87%", "أصدقاؤهم يغيبون")
    c4.metric("😟 انعدام الأمان", "23%", "7 تلاميذ خائفون")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>كل شخصية = تلميذ حقيقي من مدرستنا</div>", unsafe_allow_html=True)
    icons_html = "<div class='human-wrap'>"
    for i, row in df.iterrows():
        a = row['عدد أيام الغياب']
        g = str(row['الجنس'])
        icon = '👧' if 'بنت' in g or g == '0' else '🧒'
        flt = 'hue-rotate(310deg) saturate(5) brightness(.9)' if a>=3 else ('sepia(1) hue-rotate(4deg) saturate(5)' if a>0 else 'hue-rotate(120deg) saturate(5)')
        icons_html += f"<span class='hu' style='filter:{flt}' title='غياب: {a} أيام'>{icon}</span>"
    icons_html += "</div>"
    st.markdown(icons_html, unsafe_allow_html=True)
    st.markdown("""<div class='leg-row'>
        <div class='leg-item'><span style='font-size:18px;filter:hue-rotate(4deg) saturate(2)'>🟢</span> لا غياب (5 تلاميذ)</div>
        <div class='leg-item'><span style='font-size:18px;filter:sepia(1) hue-rotate(10deg) saturate(4)'>🟡</span> 1–2 يوم (4 تلاميذ)</div>
        <div class='leg-item'><span style='font-size:18px;filter:hue-rotate(10deg) saturate(2)'>🔴</span> 3+ أيام (22 تلميذاً)</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1.2, 1])

    with col_a:
        st.markdown("<div class='section-label'>أسباب الغياب المُصرَّح بها</div>", unsafe_allow_html=True)
        reasons_df = pd.DataFrame({
            'السبب': ['مشكل أسري', 'المرض', 'صعوبة الفهم', 'التعب', 'الخوف', 'مشكل النقل'],
            'عدد التلاميذ': [14, 13, 10, 7, 2, 2],
            'النسبة': [45, 42, 32, 23, 6, 6]
        })
        fig_r = px.bar(reasons_df, x='عدد التلاميذ', y='السبب', orientation='h',
                       color='النسبة', color_continuous_scale=[[0,'#afa9ec'],[0.5,'#ef9f27'],[1,'#e24b4a']],
                       text='النسبة', labels={'عدد التلاميذ':'عدد التلاميذ','السبب':''})
        fig_r.update_traces(texttemplate='%{text}%', textposition='outside', textfont_color='#444441')
        fig_r.update_layout(**theme(
            height=280, showlegend=False, coloraxis_showscale=False,
            yaxis=dict(autorange='reversed', gridcolor='#e8e6f0'),
            xaxis=dict(range=[0,18], gridcolor='#e8e6f0')
        ))
        st.plotly_chart(fig_r, use_container_width=True)

    with col_b:
        st.markdown("<div class='section-label'>مستوى الفهم داخل الفصل</div>", unsafe_allow_html=True)
        fig_u = go.Figure(go.Pie(
            labels=['يفهم دائماً', 'يفهم أحياناً', 'لا يفهم'],
            values=[11, 12, 8],
            hole=.65,
            marker_colors=['#3b6d11', '#ba7517', '#a32d2d'],
            textfont_size=13,
            textfont_color='#ffffff',
        ))
        fig_u.update_layout(**theme(
            height=280, showlegend=True,
            legend=dict(font=dict(color='#5f5e5a', size=12), orientation='h', y=-0.15),
            annotations=[dict(text='<b>65%</b><br>مشكلة', x=.5, y=.5, showarrow=False,
                              font=dict(size=15, color='#ba7517'))]
        ))
        st.plotly_chart(fig_u, use_container_width=True)

    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("<div class='section-label'>توزيع الغياب حسب المستوى الدراسي</div>", unsafe_allow_html=True)
        level_data = []
        for lv in range(1,7):
            lvdf = df[df['المستوى الدراسي']==lv]
            level_data.append({
                'المستوى': f'المستوى {lv}',
                'حرج 3+': int((lvdf['عدد أيام الغياب']>=3).sum()),
                'متوسط 1-2': int(((lvdf['عدد أيام الغياب']>0)&(lvdf['عدد أيام الغياب']<3)).sum()),
                'لا غياب': int((lvdf['عدد أيام الغياب']==0).sum()),
            })
        ldf = pd.DataFrame(level_data)
        fig_lv = go.Figure()
        fig_lv.add_bar(name='غياب 3+ أيام', x=ldf['المستوى'], y=ldf['حرج 3+'], marker_color='#e24b4a')
        fig_lv.add_bar(name='غياب 1-2 أيام', x=ldf['المستوى'], y=ldf['متوسط 1-2'], marker_color='#ef9f27')
        fig_lv.add_bar(name='لا غياب', x=ldf['المستوى'], y=ldf['لا غياب'], marker_color='#639922')
        fig_lv.update_layout(**theme(
            barmode='stack', height=260,
            legend=dict(font=dict(color='#5f5e5a',size=11), orientation='h', y=-0.25)
        ))
        st.plotly_chart(fig_lv, use_container_width=True)

    with col_d:
        st.markdown("<div class='section-label'>نسبة الغياب الإجمالية</div>", unsafe_allow_html=True)
        fig_abs = go.Figure(go.Pie(
            labels=['غياب حرج (3+ أيام)', 'غياب متوسط (1-2)', 'لا غياب'],
            values=[22, 4, 5],
            hole=.6,
            marker_colors=['#e24b4a', '#ef9f27', '#639922'],
            textfont_size=12, textfont_color='#ffffff',
        ))
        fig_abs.update_layout(**theme(
            height=260, showlegend=True,
            legend=dict(font=dict(color='#5f5e5a', size=11), orientation='h', y=-0.2),
            annotations=[dict(text='<b>71%</b><br>خطر', x=.5, y=.5, showarrow=False,
                              font=dict(size=16, color='#a32d2d'))]
        ))
        st.plotly_chart(fig_abs, use_container_width=True)

# ════════════════════════════════════════
# PAGE 2: تحليل عمقي
# ════════════════════════════════════════
elif page == "🔍  تحليل عمقي":
    st.markdown("<h1>تحليل الترابطات الإحصائية والميول</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-label'>ارتباط المشاكل الأسرية بالغياب</div>", unsafe_allow_html=True)
        fig_fam = px.scatter(df, x='مشكل فالعائلة', y='عدد أيام الغياب',
            trendline='ols',
            color_discrete_sequence=['#e24b4a'],
            labels={'مشكل فالعائلة':'مشكل أسري (1=نعم)', 'عدد أيام الغياب':'أيام الغياب'},
            size_max=12)
        fig_fam.update_traces(marker=dict(size=11, opacity=.75), selector=dict(mode='markers'))
        fig_fam.update_layout(**theme(
            height=300,
            xaxis=dict(tickvals=[0,1], ticktext=['لا','نعم'], gridcolor='#e8e6f0'),
            yaxis=dict(gridcolor='#e8e6f0')
        ))
        st.plotly_chart(fig_fam, use_container_width=True)
        st.markdown("<div class='qcard'><div class='qcard-text' style='font-size:14px'>64% من ذوي المشاكل الأسرية يغيبون 3+ أيام</div><div class='qcard-meta'>الأسرة هي البيئة الأولى — إذا اهتزت، اهتز الحضور</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-label'>ارتباط صعوبة الفهم بالغياب</div>", unsafe_allow_html=True)
        fig_und = px.scatter(df, x='سهولة الفهم', y='عدد أيام الغياب',
            trendline='ols',
            color_discrete_sequence=['#534ab7'],
            labels={'سهولة الفهم':'سهولة الفهم (1=جيد)', 'عدد أيام الغياب':'أيام الغياب'})
        fig_und.update_traces(marker=dict(size=11, opacity=.75), selector=dict(mode='markers'))
        fig_und.update_layout(**theme(
            height=300,
            xaxis=dict(tickvals=[0,0.5,1], ticktext=['لا يفهم','أحياناً','يفهم'], gridcolor='#e8e6f0'),
            yaxis=dict(gridcolor='#e8e6f0')
        ))
        st.plotly_chart(fig_und, use_container_width=True)
        st.markdown("<div class='qcard' style='border-right-color:#534ab7'><div class='qcard-text' style='font-size:14px'>انحدار سالب واضح: كلما صعب الفهم، ارتفع الغياب</div><div class='qcard-meta'>من يتأخر يكره — ومن يكره يغيب</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>أقراص التأثير المباشر — كل رقم مستخرج من بيانات مدرستنا</div>", unsafe_allow_html=True)
    d1, d2, d3, d4 = st.columns(4)
    disks = [
        ('الضغط الأسري', 45, 55, '#e24b4a'),
        ('التنمر وانعدام الأمان', 23, 77, '#a32d2d'),
        ('النوم المضطرب', 29, 71, '#ef9f27'),
        ('العدوى الاجتماعية', 87, 13, '#534ab7'),
    ]
    for col, (title, pct, rest, color) in zip([d1,d2,d3,d4], disks):
        fig_d = go.Figure(go.Pie(
            labels=['متأثر','مستقر'], values=[pct, rest], hole=.72,
            marker_colors=[color, '#e8e6f0'], textinfo='none'
        ))
        fig_d.update_layout(**theme(
            height=180, showlegend=False,
            annotations=[dict(text=f'<b>{pct}%</b>', x=.5, y=.55, showarrow=False,
                              font=dict(size=26, color=color, family='Tajawal')),
                         dict(text=title, x=.5, y=.35, showarrow=False,
                              font=dict(size=10, color='#7f77dd', family='Tajawal'))],
            margin=dict(l=5,r=5,t=5,b=5)
        ))
        col.plotly_chart(fig_d, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>البصمة المقارنة — التلاميذ في خطر مقابل المستقرين</div>", unsafe_allow_html=True)
    high_df = df[df['عدد أيام الغياب']>=3]
    low_df  = df[df['عدد أيام الغياب']==0]
    cats = ['مشكل أسري','مريض','لا يفهم','خائف','نوم سيء','أقران يغيبون']
    cols = ['مشكل فالعائلة','مريض','ماكنفهمش الدروس','خايف','جودة النوم','غياب الأقران']
    def safe_mean(df2, c):
        if c=='جودة النوم': return round((df2[c]==0).mean()*100) if len(df2)>0 else 0
        return round(df2[c].mean()*100) if len(df2)>0 else 0

    high_vals = [safe_mean(high_df,c) for c in cols]
    low_vals  = [safe_mean(low_df, c) for c in cols]
    fig_rad = go.Figure()
    fig_rad.add_trace(go.Scatterpolar(r=high_vals+[high_vals[0]], theta=cats+[cats[0]],
        fill='toself', name='غياب حرج (3+)', line_color='#e24b4a', fillcolor='rgba(226,75,74,.12)'))
    fig_rad.add_trace(go.Scatterpolar(r=low_vals+[low_vals[0]], theta=cats+[cats[0]],
        fill='toself', name='لا غياب', line_color='#639922', fillcolor='rgba(99,153,34,.1)'))
    fig_rad.update_layout(**theme(
        height=360,
        polar=dict(
            bgcolor='#f9f8ff',
            radialaxis=dict(visible=True, range=[0,100], tickfont=dict(color='#b4b2a9',size=10), gridcolor='#ddd8fb'),
            angularaxis=dict(tickfont=dict(color='#3c3489', size=12, family='Tajawal'), gridcolor='#ddd8fb')
        ),
        legend=dict(font=dict(color='#5f5e5a', size=12))
    ))
    st.plotly_chart(fig_rad, use_container_width=True)

# ════════════════════════════════════════
# PAGE 3: صوت التلاميذ
# ════════════════════════════════════════
elif page == "💬  صوت التلاميذ":
    st.markdown("<h1>صوت التلاميذ — كلامهم الحقيقي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7f77dd;font-size:15px'>هذه ليست أمثلة مختلقة — كل جملة كتبها تلميذ حقيقي من مدرسة 18 نونبر بيده</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    quotes = [
        ("بغيت نقرا وما كنقدرش", "👦 المستوى 3 · غياب 3+ أيام · مشكل أسري + صعوبة فهم", "#a32d2d", "يريد التعلم لكن الظروف تمنعه — هذا ليس رفضاً للمدرسة"),
        ("أنا أحبك يا المدرستي", "👧 المستوى 5 · غياب 3+ أيام", "#ba7517", "تحب المدرسة رغم كل الغيابات — الغياب ليس كراهية للتعلم"),
        ("كنغيب بدون قصد، المرض كيجيني على غفلة", "👧 المستوى 3 · غياب 3+ أيام · نوم سيء", "#ba7517", "أجسام هشة في بيئة صعبة — الصحة والنوم عاملا خطر مخفيان"),
        ("بغيت مدرسة فموزار", "👦 المستوى 3 · غياب 3+ أيام", "#a32d2d", "يتمنى مدرسة في حي آخر — شعور بالدونية تجاه بيئته المدرسية"),
        ("كنتمنى نكون غني", "👦 المستوى 4 · غياب 3+ أيام · مشكل أسري", "#534ab7", "الوعي بالهشاشة الاقتصادية في سن مبكرة — يؤثر على الشعور بالانتماء"),
        ("كنتمان متبقاش نغيب — امين", "👧 المستوى 4 · غياب 1-2 أيام", "#3b6d11", "لديها الإرادة للتغيير — هذه هي الحالات الأكثر قابلية للتدخل"),
        ("كنغيب من اجل الكرة", "👦 المستوى 6 · غياب 3+ أيام · لا يشعر بالأمان", "#ba7517", "غياب انتهازي وليس عجزاً — قابل للحل بجاذبية الجمعة"),
        ("كنغيب بزاف", "👧 المستوى 3 · غياب 3+ أيام · مشكل نقل", "#a32d2d", "تعترف بمشكلتها — التواصل المفتوح ممكن"),
    ]
    for q, meta, color, insight in quotes:
        st.markdown(f"""<div class='qcard' style='border-right-color:{color};margin-bottom:1rem'>
            <div class='qcard-text'>"{q}"</div>
            <div class='qcard-meta' style='margin-bottom:.35rem'>{meta}</div>
            <div style='font-size:12px;color:{color};font-family:Tajawal,sans-serif'>💡 {insight}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>تحليل المشاعر — ماذا كشفت الرسائل الحرة؟</div>", unsafe_allow_html=True)
    col_e1, col_e2, col_e3 = st.columns(3)
    col_e1.metric("يريدون التعلم لكن يعجزون", "4 تلاميذ", "من 8 رسائل حقيقية")
    col_e2.metric("يحبون المدرسة رغم الغياب", "3 تلاميذ", "الغياب ≠ كراهية")
    col_e3.metric("يتمنون التغيير صراحة", "2 تلميذ", "أعلى قابلية للتدخل")

# ════════════════════════════════════════
# PAGE 4: خطة التدخل
# ════════════════════════════════════════
elif page == "💡  خطة التدخل":
    st.markdown("<h1>خطة التدخل الميداني — مبنية على البيانات</h1>", unsafe_allow_html=True)

    col_p, col_q = st.columns([1,1])
    with col_p:
        st.markdown("<div class='section-label'>الأولويات حسب تأثير التدخل</div>", unsafe_allow_html=True)
        impact_df = pd.DataFrame({
            'الإجراء': ['خلية الإنذار المبكر','جلسات الدعم الأسري','مبادرة الجمعة','برنامج الأقران','دعم الفهم البيداغوجي','زاوية الأمان'],
            'الأثر المتوقع': [85, 70, 55, 65, 60, 50],
            'سرعة التنفيذ': [90, 40, 80, 70, 60, 85],
            'الفئة المستهدفة': ['المستويات 3 و6','الأسر','الكل','الأقران','داخل الفصل','الخائفون']
        })
        fig_imp = px.scatter(impact_df, x='سرعة التنفيذ', y='الأثر المتوقع',
            text='الإجراء', color='الأثر المتوقع',
            color_continuous_scale=[[0,'#afa9ec'],[1,'#639922']],
            size=[80,70,60,65,60,50], size_max=30)
        fig_imp.update_traces(textposition='top center', textfont=dict(color='#444441', size=10, family='Tajawal'))
        fig_imp.update_layout(**theme(
            height=320, showlegend=False, coloraxis_showscale=False,
            xaxis=dict(title='سرعة التنفيذ (%)', gridcolor='#e8e6f0', range=[30,100]),
            yaxis=dict(title='الأثر المتوقع (%)', gridcolor='#e8e6f0', range=[40,95])
        ))
        st.plotly_chart(fig_imp, use_container_width=True)

    with col_q:
        st.markdown("<div class='section-label'>الجدول الزمني للتنفيذ</div>", unsafe_allow_html=True)
        timeline = pd.DataFrame({
            'الإجراء': ['خلية الإنذار','زاوية الأمان','مبادرة الجمعة','دعم الأقران','جلسات الأسرة','دعم بيداغوجي'],
            'البداية': [0,0,1,2,3,4],
            'المدة': [12,12,8,10,8,8],
            'الأولوية': ['عاجل','عاجل','مهم','مهم','إستراتيجي','إستراتيجي']
        })
        colors = {'عاجل':'#e24b4a','مهم':'#ef9f27','إستراتيجي':'#534ab7'}
        fig_tl = go.Figure()
        for _, r in timeline.iterrows():
            fig_tl.add_trace(go.Bar(
                x=[r['المدة']], y=[r['الإجراء']], base=[r['البداية']],
                orientation='h', marker_color=colors[r['الأولوية']],
                name=r['الأولوية'], showlegend=False,
                hovertemplate=f"{r['الإجراء']}: أسبوع {r['البداية']+1}–{r['البداية']+r['المدة']}<extra></extra>"
            ))
        fig_tl.update_layout(**theme(
            height=320,
            xaxis=dict(title='الأسابيع', gridcolor='#e8e6f0', tickvals=list(range(0,14,2))),
            yaxis=dict(autorange='reversed', gridcolor='#e8e6f0'),
            barmode='overlay'
        ))
        st.plotly_chart(fig_tl, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>توصيات التدخل التفصيلية</div>", unsafe_allow_html=True)

    recos = [
        ("01", "🚨 خلية الإنذار المبكر — المستويان 3 و6",
         "كل تلميذ يغيب 3 أيام متتالية يتلقى تواصلاً فورياً من الرائدة خلال 24 ساعة. المستوى 3: 88% في خطر. المستوى 6: 75%. هذان المستويان أولوية قصوى."),
        ("02", "🏠 جلسات 'أسرة مدرستي' مع الرائدة",
         "45% من الغيابات مرتبطة بأزمات أسرية. لقاءات شهرية بين الرائدة والأسر، مع ربط الحالات الحرجة بالخدمات الاجتماعية في فاس."),
        ("03", "⚽ مبادرة 'الجمعة مليحة'",
         "6 تلاميذ يختارون الجمعة تحديداً للغياب. نشاط جذاب كل جمعة (رياضة، رسم، ورشة) يجعل الحضور أكثر جاذبية من الغياب."),
        ("04", "👥 سفراء الحضور — كسر العدوى الاجتماعية",
         "87% يغيبون في مجموعات. تكليف تلاميذ منتظمين كـ'سفراء' لمرافقة أصدقائهم المترددين. الضغط الاجتماعي الإيجابي أداة قوية."),
        ("05", "📚 حصص 'نقرأ معاً' بعد الدوام",
         "32% لا يفهمون الدروس — وهذا يُغذّي الغياب. دعم جماعي ثلاث مرات أسبوعياً لتقليص الفجوة التعليمية مرتبطة بخطر التسرب."),
        ("06", "🛡️ زاوية الأمان مع الرائدة",
         "23% لا يشعرون بالأمان داخل المدرسة. مكان هادئ وآمن، صندوق بلاغ مجهول، وبروتوكول تدخل واضح خلال 48 ساعة من كل إبلاغ."),
    ]
    for num, title, desc in recos:
        st.markdown(f"""<div class='reco-card'>
            <div class='reco-num'>{num}</div>
            <div class='reco-body'><div class='reco-title'>{title}</div>{desc}</div>
        </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════
# PAGE 5: الروبوت الذكي
# ════════════════════════════════════════
elif page == "🤖  نظام الإنذار المبكر":
    st.markdown("<h1>🤖 نظام الإنذار المبكر — تحليل ملف التلميذ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7f77dd;font-size:14px'>الأوزان مبنية بالكامل على نتائج دراستنا الميدانية في مدرسة 18 نونبر</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1,1])
    with col_a:
        st.markdown("<h2>بيانات التلميذ</h2>", unsafe_allow_html=True)
        lvl    = st.selectbox("المستوى الدراسي", [1,2,3,4,5,6],
                    help="المستويات 3 و6 الأكثر خطراً في بياناتنا")
        fam    = st.radio("توجد مشاكل أسرية؟", ["لا","نعم"], horizontal=True)
        und    = st.radio("صعوبة في فهم الدروس؟", ["لا","أحياناً","نعم"])
        peers  = st.radio("أصدقاؤه المقربون يغيبون؟", ["لا","نعم"], horizontal=True)
        safe_s = st.radio("يشعر بعدم الأمان أو التنمر؟", ["لا","نعم"], horizontal=True)
        sleep  = st.radio("اضطراب في النوم؟", ["لا","نعم"], horizontal=True)
        health = st.radio("تعب أو وعكات صحية متكررة؟", ["لا","نعم"], horizontal=True)

    with col_b:
        st.markdown("<h2>نتيجة التحليل</h2>", unsafe_allow_html=True)
        if st.button("تحليل ملف التلميذ ←"):
            score = 0
            details = []
            if fam   =="نعم": score+=30; details.append(("مشكل أسري","30","#e24b4a","السبب الأول للغياب — 45% من حالاتنا"))
            if und   =="نعم": score+=20; details.append(("لا يفهم الدروس","20","#ef9f27","32% من التلاميذ — يُغذّي الغياب المزمن"))
            elif und =="أحياناً": score+=10; details.append(("أحياناً يفهم","10","#ef9f27","39% من التلاميذ — فجوة تعليمية ناشئة"))
            if peers =="نعم": score+=15; details.append(("أقران يغيبون","15","#534ab7","87% من حالاتنا — عدوى اجتماعية خطيرة"))
            if safe_s=="نعم": score+=15; details.append(("انعدام الأمان","15","#a32d2d","57% من الخائفين يغيبون 3+ أيام"))
            if health=="نعم": score+=10; details.append(("تعب/وعكات","10","#185fa5","23% من التلاميذ — شائع في الأوساط الهشة"))
            if sleep =="نعم": score+=10; details.append(("نوم مضطرب","10","#185fa5","50% من سيئي النوم يغيبون كثيراً"))
            if lvl in [3,6]: score+=5; details.append(("مستوى حرج","5","#534ab7","المستويان 3 و6 الأعلى خطراً في دراستنا"))
            score = min(score, 100)

            if score >= 70:
                sc_color="#a32d2d"; risk_txt="خطر مرتفع"; risk_icon="🚨"
                advice="تدخل فوري مطلوب: تواصل مع الرائدة والأسرة خلال 24 ساعة."
            elif score >= 40:
                sc_color="#ba7517"; risk_txt="خطر متوسط"; risk_icon="⚠️"
                advice="متابعة أسبوعية مع الرائدة — لا تترك الوضع يتطور."
            else:
                sc_color="#3b6d11"; risk_txt="حالة مستقرة"; risk_icon="✅"
                advice="مراقبة عادية — أي تغيير يستوجب إعادة التقييم."

            st.markdown(f"""<div class='risk-score-box'>
                <div class='risk-big' style='color:{sc_color}'>{risk_icon} {score}%</div>
                <div class='risk-label'>{risk_txt}</div>
            </div>""", unsafe_allow_html=True)

            if score >= 70:
                st.error(f"🚨 {advice}")
            elif score >= 40:
                st.warning(f"⚠️ {advice}")
            else:
                st.success(f"✅ {advice}")

            if details:
                st.markdown("<br><div class='section-label'>تفاصيل عوامل الخطر المكتشفة</div>", unsafe_allow_html=True)
                for lbl, pts, color, note in details:
                    st.markdown(f"""<div style='display:flex;align-items:center;gap:.75rem;background:#f4f2ff;
                        border-radius:8px;padding:.625rem .875rem;margin-bottom:.5rem;direction:rtl'>
                        <div style='font-size:15px;font-weight:700;color:{color};min-width:40px;text-align:center'>+{pts}</div>
                        <div>
                            <div style='font-size:14px;font-weight:700;color:#26215c;font-family:Tajawal,sans-serif'>{lbl}</div>
                            <div style='font-size:11px;color:#7f77dd;font-family:Tajawal,sans-serif'>{note}</div>
                        </div>
                    </div>""", unsafe_allow_html=True)

            fig_g = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                domain={'x':[0,1],'y':[0,1]},
                number={'suffix':'%','font':{'size':36,'color':sc_color,'family':'Tajawal'}},
                gauge=dict(
                    axis=dict(range=[0,100], tickcolor='#b4b2a9', tickfont=dict(color='#5f5e5a')),
                    bar=dict(color=sc_color, thickness=.25),
                    bgcolor='#e8e6f0',
                    steps=[
                        {'range':[0,40],'color':'#eaf3de'},
                        {'range':[40,70],'color':'#faeeda'},
                        {'range':[70,100],'color':'#fcebeb'},
                    ],
                    threshold=dict(line=dict(color=sc_color,width=3), thickness=.8, value=score)
                )
            ))
            fig_g.update_layout(**theme(height=220, margin=dict(l=20,r=20,t=10,b=10)))
            st.plotly_chart(fig_g, use_container_width=True)
        else:
            st.markdown("""<div style='background:#f4f2ff;border-radius:12px;padding:2rem;text-align:center;color:#7f77dd;font-family:Tajawal,sans-serif;font-size:15px'>
            أدخل بيانات التلميذ في اليسار ثم اضغط "تحليل ملف التلميذ"
            </div>""", unsafe_allow_html=True)