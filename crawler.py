from ai_agent import analyze_website, improve_website
import requests
import random
from bs4 import BeautifulSoup

def crawl_website(url):
    print(f"\n🔍 Crawling Website: {url}\n")

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract page title
        title = soup.title.string if soup.title else "No Title"

        # Extract headings
        headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]

        # Extract button and link texts (CTA)
        buttons = [btn.get_text(strip=True) for btn in soup.find_all("button")]
        links = [a.get_text(strip=True) for a in soup.find_all("a") if len(a.get_text(strip=True)) > 2]

        # Extract main text
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        # Check for trust elements
        has_privacy = any("privacy" in link.lower() for link in links)
        has_contact = any("contact" in link.lower() for link in links)
        has_testimonials = any("testimonial" in p.lower() for p in paragraphs)

        website_data = {
            "title": title,
            "headings": headings[:10],
            "buttons": buttons[:10],
            "links": links[:10],
            "paragraphs": paragraphs[:10],
            "has_privacy_policy": has_privacy,
            "has_contact_page": has_contact,
            "has_testimonials": has_testimonials
        }

        return website_data

    except Exception as e:
        print("❌ Error while crawling:", e)
        return None
def generate_website_summary(data):
    summary = []

    # Title
    summary.append(f"The website title is '{data['title']}'.")

    # Headings
    if len(data["headings"]) == 0:
        summary.append("The website does not have clear visible headings, which may reduce content clarity.")
    else:
        summary.append(f"The website contains headings such as: {', '.join(data['headings'][:3])}.")

    # CTA Buttons
    if len(data["buttons"]) == 0:
        summary.append("No call-to-action buttons were detected on the homepage.")
    else:
        summary.append(f"The website has the following call-to-action buttons: {', '.join(data['buttons'])}.")

    # Trust elements
    if data["has_privacy_policy"]:
        summary.append("The website includes a privacy policy link, which improves trust.")
    else:
        summary.append("No privacy policy link was found, which may reduce user trust.")

    if data["has_contact_page"]:
        summary.append("A contact page is available for user support.")
    else:
        summary.append("No visible contact page was found, which may reduce user confidence.")

    if data["has_testimonials"]:
        summary.append("The website includes testimonials, which can increase credibility.")
    else:
        summary.append("No testimonials were found, which may affect trust and conversion.")

    return " ".join(summary)



def simulate_users(quality_score, users=1000):
    """
    Simulates user conversions based on website quality.
    quality_score: float between 0 and 1 (higher = better website)
    users: number of simulated visitors
    """
    conversions = 0

    for _ in range(users):
        if random.random() < quality_score:
            conversions += 1

    conversion_rate = (conversions / users) * 100
    return conversions, conversion_rate




if __name__ == "__main__":
    url = input("Enter website URL: ")
    data = crawl_website(url)

    if data:
        print("\n===== WEBSITE DATA (VERSION A: UNIMPROVED) =====\n")
        print("Title:", data["title"])
        print("\nHeadings:", data["headings"])
        print("\nButtons (CTAs):", data["buttons"])
        print("\nLinks:", data["links"])
        print("\nHas Privacy Policy:", data["has_privacy_policy"])
        print("Has Contact Page:", data["has_contact_page"])
        print("Has Testimonials:", data["has_testimonials"])

        print("\n===== AI INPUT SUMMARY =====\n")
        summary = generate_website_summary(data)
        print(summary)

        print("\n===== AI ANALYSIS: CONVERSION ISSUES =====\n")
        ai_result = analyze_website(summary)
        print(ai_result)

        print("\n===== AI-IMPROVED WEBSITE VERSION (VERSION B) =====\n")
        improved_version = improve_website(summary)
        print(improved_version)

        print("\n===== SIMULATED USER CONVERSION TEST =====\n")

        # Assign quality scores (0 to 1)
        original_quality = 0.02   # 2% base conversion
        improved_quality = 0.05   # 5% conversion after AI improvements

        users = 1000

        orig_conv, orig_rate = simulate_users(original_quality, users)
        imp_conv, imp_rate = simulate_users(improved_quality, users)

        print(f"Original Website (Version A):")
        print(f"Users: {users}")
        print(f"Converted: {orig_conv}")
        print(f"Conversion Rate: {orig_rate:.2f}%\n")

        print(f"AI-Improved Website (Version B):")
        print(f"Users: {users}")
        print(f"Converted: {imp_conv}")
        print(f"Conversion Rate: {imp_rate:.2f}%\n")

        improvement = imp_rate - orig_rate
        print(f"📈 Conversion Rate Improvement: {improvement:.2f}%")







