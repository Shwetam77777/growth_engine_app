import streamlit as st
import google.generativeai as genai
import urllib.parse

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Growth Engine AI",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    .reportview-container {
        background: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. API SETUP (SECURE) ---
try:
    # Try fetching from Streamlit Secrets (Works on Cloud & Local if configured)
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')   # Using Flash for speed/cost efficiency
except Exception as e:
    st.error("⚠️ API Key missing! Please set 'GOOGLE_API_KEY' in your .streamlit/secrets.toml file.")
    st.stop()

# --- 3. HELPER FUNCTIONS ---

def generate_content(prompt_text):
    """Wraps the API call with error handling."""
    try:
        with st.spinner("🤖 AI is thinking..."):
            response = model.generate_content(prompt_text)
            return response.text
    except Exception as e:
        st.error(f"API Error: {e}")
        return None

def create_twitter_link(text):
    """Generates a direct 'Post to X' intent link."""
    base_url = "https://twitter.com/intent/tweet?text="
    encoded_text = urllib.parse.quote(text)
    return f"{base_url}{encoded_text}"

def create_linkedin_link(url=""):
    """Generates a LinkedIn share link (LinkedIn APIs are stricter on text pre-fill)."""
    # Note: LinkedIn pre-fill text support is limited in free web intents. 
    # This opens the share window where user pastes the content.
    return "https://www.linkedin.com/feed/"

# --- 4. MAIN INTERFACE ---

st.title("🚀 Personal Branding AI Architect")
st.markdown("Build your audience on **LinkedIn** & **Twitter** without the spam.")

# Create Tabs for different workflows
tab1, tab2, tab3 = st.tabs(["✍️ Viral Post Generator", "🎣 Hook Smith", "🔍 Profile Auditor"])

# === TAB 1: VIRAL POST GENERATOR ===
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input")
        topic = st.text_area("What do you want to post about?", height=150, placeholder="e.g., I learned Python in 30 days...")
        tone = st.selectbox("Select Tone", ["Storytelling (Hero's Journey)", "Contrarian (Hot Take)", "Educational (How-to)", "Professional Update"])
        
        if st.button("Generate Posts", type="primary"):
            if topic:
                # SYSTEM PROMPT: The 'Senior Architect' Secret Sauce
                system_prompt = f"""
                You are a top-tier ghostwriter for Silicon Valley founders.
                Role: Take the user's raw idea and write two distinct posts.
                
                Input Idea: {topic}
                Selected Tone: {tone}

                Requirements:
                1. LINKEDIN POST: Use short paragraphs. Focus on value. No emojis in the first line. 
                2. TWITTER THREAD: Write a hook + 3 body tweets + conclusion. Under 280 chars per tweet.
                
                Output format:
                ### LINKEDIN
                [Content]
                ### TWITTER
                [Content]
                """
                
                generated_text = generate_content(system_prompt)
                if generated_text:
                    st.session_state['generated_result'] = generated_text
            else:
                st.warning("Please enter a topic first.")

    with col2:
        st.subheader("Output")
        if 'generated_result' in st.session_state:
            st.markdown(st.session_state['generated_result'])
            
            # Action Buttons
            st.markdown("---")
            st.markdown("#### 🚀 Ready to Publish?")
            
            # Note: We can't auto-split the AI text perfectly for buttons without regex, 
            # so we give the user a copy-paste friendly view.
            if st.button("Open LinkedIn (Paste text manually)"):
                 st.markdown(f"[Click here to open LinkedIn]({create_linkedin_link()})", unsafe_allow_html=True)
            
            st.info("💡 Pro Tip: Copy the generated text, verify it, then click the link to post.")

# === TAB 2: HOOK SMITH ===
with tab2:
    st.markdown("### The Hook is 80% of the Post")
    boring_hook = st.text_input("Enter your current (boring) opening line:", placeholder="I wrote a new app today.")
    
    if st.button("Rewrite Hooks"):
        if boring_hook:
            hook_prompt = f"""
            Act as a viral marketing expert. Rewrite the following sentence into 5 different 'Hook' styles.
            Input: "{boring_hook}"
            
            Styles:
            1. The Negative Bias ("Why X is a mistake")
            2. The 'How-To' Promise ("How to X in Y steps")
            3. The Insider Secret ("What nobody tells you about X")
            4. The Data/Number ("I saved $50k by...")
            5. The Direct Question ("Are you still doing X?")
            
            Provide only the 5 bullets.
            """
            hooks = generate_content(hook_prompt)
            st.markdown(hooks)

# === TAB 3: PROFILE AUDITOR ===
with tab3:
    st.markdown("### Roast My Bio")
    current_bio = st.text_area("Paste your current LinkedIn/Twitter Bio:", height=100)
    target_audience = st.text_input("Who is your target audience?", placeholder="e.g. Recruiters, Founders, Developers")
    
    if st.button("Audit Profile"):
        if current_bio:
            audit_prompt = f"""
            Act as a Senior Personal Brand Consultant. Analyze this bio.
            
            Bio: "{current_bio}"
            Target Audience: "{target_audience}"
            
            1. Give a score out of 10.
            2. List 3 specific weaknesses (e.g., "Too vague", "Buzzwords").
            3. Write 2 improved versions (one Professional, one Conversational).
            """
            audit = generate_content(audit_prompt)
            st.markdown(audit)

