import streamlit as st
import matplotlib.pyplot as plt
from predictor import recommend_careers, get_course_link

st.set_page_config(page_title="AI Career Path Predictor")

st.title("🎯 AI Career Path Predictor")
st.markdown("Enter your **skills**, **interests**, personality traits, or work style:")

user_input = st.text_area(
    "🧠 Describe yourself:",
    height=150,
    placeholder="e.g. I love problem-solving, creativity, and working independently..."
)

if st.button("🔍 Predict Careers"):
    if not user_input.strip():
        st.warning("⚠️ Please describe yourself to get results.")
    else:
        # Only call predictor if input exists
        results = recommend_careers(user_input)

        if results and len(results) > 0:
            st.subheader("🔮 Top Career Matches")

            best_match = results[0][0]  # safest use of best match

            careers = []
            scores = []

            for career, score in results:
                match_percent = round(score * 100, 2)
                careers.append(career)
                scores.append(match_percent)

                # Highlight top match
                if career == best_match:
                    st.markdown(f"🟢 **TOP MATCH: {career} — {match_percent}%**")
                else:
                    st.markdown(f"**{career}** — `{match_percent}% match`")

                st.progress(score)
                st.markdown(f"🎓 [Recommended Course]({get_course_link(career)})")


            # Show chart
            st.subheader("📊 Career Match Comparison")
            fig, ax = plt.subplots()
            ax.barh(careers[::-1], scores[::-1], color="skyblue")
            ax.set_xlabel("Match %")
            ax.set_title("Your Career Compatibility")
            st.pyplot(fig)

        else:
            st.warning("😕 No matching careers found.")

