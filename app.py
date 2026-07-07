from flask import Flask, render_template, request

app = Flask(__name__)

# ==========================
# SAMPLE DATA
# ==========================

HERBS = [
    {
        "id": 1, "name": "Turmeric", "emoji": "🟡", "scientific_name": "Curcuma longa",
        "description": "Turmeric is a golden-yellow spice widely used in Ayurvedic medicine. Its active compound curcumin has powerful anti-inflammatory and antioxidant properties.",
        "taste": "Bitter, Pungent", "category": "Rhizome",
        "properties": ["Anti-inflammatory", "Antioxidant", "Antimicrobial", "Hepatoprotective"],
        "uses": ["Joint pain relief", "Digestive health", "Skin conditions", "Wound healing"],
        "preparation": "Mix 1 tsp turmeric powder in warm milk or water. Can also be used as a paste for topical application.",
        "dosage": "500–1000 mg curcumin daily (1–3 tsp powder)",
        "contraindications": "Avoid high doses with blood thinners. Not recommended during pregnancy in large amounts.",
        "taste_profile": {"sweet": 10, "sour": 5, "salty": 5, "bitter": 70, "umami": 5, "astringent": 30},
    },
    {
        "id": 2, "name": "Ashwagandha", "emoji": "🌿", "scientific_name": "Withania somnifera",
        "description": "Known as Indian ginseng, Ashwagandha is a powerful adaptogen that helps the body manage stress and supports overall vitality.",
        "taste": "Bitter, Sweet", "category": "Root",
        "properties": ["Adaptogenic", "Anxiolytic", "Immunomodulatory", "Neuroprotective"],
        "uses": ["Stress and anxiety", "Insomnia", "Fatigue", "Cognitive enhancement"],
        "preparation": "Take as powder mixed with warm milk and honey, or as standardized capsule extract.",
        "dosage": "300–600 mg extract daily, or 3–6 g root powder",
        "contraindications": "Avoid during pregnancy. May interact with thyroid medications and sedatives.",
        "taste_profile": {"sweet": 30, "sour": 10, "salty": 5, "bitter": 50, "umami": 10, "astringent": 20},
    },
    {
        "id": 3, "name": "Tulsi (Holy Basil)", "emoji": "🍃", "scientific_name": "Ocimum tenuiflorum",
        "description": "Tulsi is revered in Ayurveda as the 'Queen of Herbs'. It has antimicrobial, anti-inflammatory, and adaptogenic properties.",
        "taste": "Pungent, Bitter", "category": "Leaf",
        "properties": ["Antimicrobial", "Anti-inflammatory", "Adaptogenic", "Expectorant"],
        "uses": ["Respiratory infections", "Stress relief", "Fever", "Digestive issues"],
        "preparation": "Steep 5–10 fresh leaves or 1 tsp dried leaves in hot water for 5–10 minutes.",
        "dosage": "2–3 cups of tea daily, or 300–600 mg extract",
        "contraindications": "May lower blood sugar. Use cautiously with anticoagulant medications.",
        "taste_profile": {"sweet": 5, "sour": 5, "salty": 5, "bitter": 40, "umami": 10, "astringent": 50},
    },
    {
        "id": 4, "name": "Ginger", "emoji": "🫚", "scientific_name": "Zingiber officinale",
        "description": "Ginger is one of the most widely used medicinal spices, known for its digestive and anti-nausea properties.",
        "taste": "Pungent, Sweet", "category": "Rhizome",
        "properties": ["Anti-nausea", "Anti-inflammatory", "Digestive stimulant", "Antioxidant"],
        "uses": ["Nausea and vomiting", "Indigestion", "Cold and flu", "Joint pain"],
        "preparation": "Grate fresh ginger into hot water with lemon and honey. Can also be used in cooking.",
        "dosage": "1–3 g dried ginger daily, or 2–4 g fresh ginger",
        "contraindications": "May increase bleeding risk. Avoid large doses with gallstones.",
        "taste_profile": {"sweet": 15, "sour": 10, "salty": 5, "bitter": 20, "umami": 10, "astringent": 15},
    },
    {
        "id": 5, "name": "Neem", "emoji": "🌳", "scientific_name": "Azadirachta indica",
        "description": "Neem is a versatile herb known as 'Nature's Pharmacy' with potent antibacterial, antifungal, and blood-purifying properties.",
        "taste": "Bitter", "category": "Leaf/Bark",
        "properties": ["Antibacterial", "Antifungal", "Blood purifier", "Antipyretic"],
        "uses": ["Skin diseases", "Diabetes management", "Dental health", "Malaria fever"],
        "preparation": "Neem leaf juice, powder in capsules, or neem oil for topical use.",
        "dosage": "2–4 neem leaves daily, or 250–500 mg powder",
        "contraindications": "Not for pregnant or breastfeeding women. May affect fertility in high doses.",
        "taste_profile": {"sweet": 0, "sour": 5, "salty": 5, "bitter": 90, "umami": 0, "astringent": 60},
    },
    {
        "id": 6, "name": "Amla", "emoji": "🫐", "scientific_name": "Phyllanthus emblica",
        "description": "Amla (Indian Gooseberry) is one of the richest natural sources of Vitamin C and a key ingredient in Chyawanprash.",
        "taste": "Sour, Sweet, Astringent", "category": "Fruit",
        "properties": ["Antioxidant", "Immunomodulatory", "Hepatoprotective", "Anti-aging"],
        "uses": ["Immunity boost", "Hair health", "Digestive tonic", "Diabetes support"],
        "preparation": "Fresh juice, dried powder with honey, or as part of Triphala formulation.",
        "dosage": "1–2 tsp powder daily, or 20–30 ml fresh juice",
        "contraindications": "May lower blood sugar. Monitor if on diabetes medication.",
        "taste_profile": {"sweet": 20, "sour": 60, "salty": 5, "bitter": 10, "umami": 5, "astringent": 40},
    },
    {
        "id": 7, "name": "Brahmi", "emoji": "🧠", "scientific_name": "Bacopa monnieri",
        "description": "Brahmi is a renowned brain tonic in Ayurveda, used to enhance memory, concentration, and cognitive function.",
        "taste": "Bitter, Sweet", "category": "Herb",
        "properties": ["Nootropic", "Anxiolytic", "Neuroprotective", "Antioxidant"],
        "uses": ["Memory enhancement", "Anxiety", "ADHD support", "Epilepsy adjunct"],
        "preparation": "Powder mixed with ghee and honey, or as standardized extract capsules.",
        "dosage": "300–450 mg extract daily, or 2–3 g powder",
        "contraindications": "May increase thyroid hormone levels. Avoid with sedative medications.",
        "taste_profile": {"sweet": 15, "sour": 5, "salty": 5, "bitter": 55, "umami": 5, "astringent": 25},
    },
    {
        "id": 8, "name": "Triphala", "emoji": "⚗️", "scientific_name": "Emblica + Terminalia spp.",
        "description": "Triphala is a classical Ayurvedic formulation combining three fruits: Amla, Bibhitaki, and Haritaki for digestive health.",
        "taste": "Sour, Sweet, Bitter, Astringent", "category": "Formulation",
        "properties": ["Laxative", "Antioxidant", "Digestive tonic", "Detoxifying"],
        "uses": ["Constipation", "Digestive cleansing", "Eye health", "Weight management"],
        "preparation": "1 tsp powder in warm water before bedtime, or as tablets.",
        "dosage": "3–6 g powder daily, preferably at night",
        "contraindications": "Avoid during pregnancy and acute diarrhea. May interact with blood thinners.",
        "taste_profile": {"sweet": 25, "sour": 40, "salty": 5, "bitter": 30, "umami": 5, "astringent": 50},
    },
]

DISEASES = [
    {"id": 1, "name": "Arthritis", "emoji": "🦴", "category": "Musculoskeletal",
     "description": "Inflammation of joints causing pain, stiffness, and reduced mobility.",
     "herb_count": 2},
    {"id": 2, "name": "Diabetes", "emoji": "🩸", "category": "Metabolic",
     "description": "Chronic condition affecting blood sugar regulation and metabolism.",
     "herb_count": 2},
    {"id": 3, "name": "Anxiety & Stress", "emoji": "🧘", "category": "Mental Health",
     "description": "Persistent worry, tension, and stress affecting daily life and well-being.",
     "herb_count": 3},
    {"id": 4, "name": "Digestive Disorders", "emoji": "🫄", "category": "Gastrointestinal",
     "description": "Conditions affecting digestion including indigestion, bloating, and constipation.",
     "herb_count": 3},
    {"id": 5, "name": "Skin Diseases", "emoji": "🧴", "category": "Dermatological",
     "description": "Various skin conditions including eczema, acne, and fungal infections.",
     "herb_count": 2},
    {"id": 6, "name": "Respiratory Infections", "emoji": "🫁", "category": "Respiratory",
     "description": "Infections affecting the respiratory tract including cold, cough, and bronchitis.",
     "herb_count": 2},
    {"id": 7, "name": "Insomnia", "emoji": "😴", "category": "Sleep",
     "description": "Difficulty falling or staying asleep, leading to fatigue and impaired function.",
     "herb_count": 2},
    {"id": 8, "name": "Low Immunity", "emoji": "🛡️", "category": "Immune",
     "description": "Weakened immune system leading to frequent infections and slow recovery.",
     "herb_count": 3},
]

RECOMMENDATIONS = [
    {"herb_id": 1, "disease_id": 1, "dosage": "500 mg curcumin twice daily", "preparation": "Turmeric milk with black pepper", "effectiveness": 85},
    {"herb_id": 4, "disease_id": 1, "dosage": "2 g ginger powder daily", "preparation": "Ginger tea with honey", "effectiveness": 70},
    {"herb_id": 5, "disease_id": 2, "dosage": "250 mg neem powder twice daily", "preparation": "Neem leaf capsules after meals", "effectiveness": 75},
    {"herb_id": 6, "disease_id": 2, "dosage": "1 tsp amla powder daily", "preparation": "Amla juice on empty stomach", "effectiveness": 80},
    {"herb_id": 2, "disease_id": 3, "dosage": "600 mg extract daily", "preparation": "Ashwagandha with warm milk at night", "effectiveness": 90},
    {"herb_id": 3, "disease_id": 3, "dosage": "2 cups tulsi tea daily", "preparation": "Fresh tulsi leaf tea with honey", "effectiveness": 80},
    {"herb_id": 7, "disease_id": 3, "dosage": "300 mg brahmi extract daily", "preparation": "Brahmi powder with ghee", "effectiveness": 85},
    {"herb_id": 4, "disease_id": 4, "dosage": "1 g ginger before meals", "preparation": "Fresh ginger tea", "effectiveness": 85},
    {"herb_id": 8, "disease_id": 4, "dosage": "3 g triphala at bedtime", "preparation": "Triphala powder in warm water", "effectiveness": 90},
    {"herb_id": 6, "disease_id": 4, "dosage": "1 tsp amla powder daily", "preparation": "Amla with honey after meals", "effectiveness": 75},
    {"herb_id": 1, "disease_id": 5, "dosage": "Turmeric paste topically", "preparation": "Turmeric + coconut oil paste", "effectiveness": 80},
    {"herb_id": 5, "disease_id": 5, "dosage": "Neem leaf paste or oil", "preparation": "Crushed neem leaves applied topically", "effectiveness": 85},
    {"herb_id": 3, "disease_id": 6, "dosage": "3 cups tulsi tea daily", "preparation": "Tulsi tea with ginger and honey", "effectiveness": 85},
    {"herb_id": 4, "disease_id": 6, "dosage": "2 g ginger daily", "preparation": "Ginger-honey tea", "effectiveness": 80},
    {"herb_id": 2, "disease_id": 7, "dosage": "600 mg at bedtime", "preparation": "Ashwagandha warm milk", "effectiveness": 88},
    {"herb_id": 7, "disease_id": 7, "dosage": "450 mg brahmi at night", "preparation": "Brahmi capsules before sleep", "effectiveness": 82},
    {"herb_id": 6, "disease_id": 8, "dosage": "2 tsp amla powder daily", "preparation": "Amla juice every morning", "effectiveness": 90},
    {"herb_id": 3, "disease_id": 8, "dosage": "Daily tulsi tea", "preparation": "Tulsi with black pepper tea", "effectiveness": 85},
    {"herb_id": 2, "disease_id": 8, "dosage": "600 mg ashwagandha daily", "preparation": "Ashwagandha with milk", "effectiveness": 80},
]

TASTES = [
    {"id": "sweet", "name": "Sweet"},
    {"id": "sour", "name": "Sour"},
    {"id": "salty", "name": "Salty"},
    {"id": "bitter", "name": "Bitter"},
    {"id": "umami", "name": "Umami"},
    {"id": "astringent", "name": "Astringent"},
]


def get_herb(herb_id):
    return next((h for h in HERBS if h["id"] == herb_id), None)


def get_disease(disease_id):
    return next((d for d in DISEASES if d["id"] == disease_id), None)


def get_recommendations(disease_id=None):
    results = []
    for rec in RECOMMENDATIONS:
        if disease_id and rec["disease_id"] != disease_id:
            continue
        herb = get_herb(rec["herb_id"])
        disease = get_disease(rec["disease_id"])
        if herb and disease:
            results.append({
                "herb": herb,
                "disease_name": disease["name"],
                "dosage": rec["dosage"],
                "preparation": rec["preparation"],
                "effectiveness": rec["effectiveness"],
            })
    return results


# ==========================
# ROUTES
# ==========================

@app.route("/")
def home():
    return render_template("index.html", herbs=HERBS, diseases=DISEASES)


@app.route("/disease")
def disease():
    return render_template("disease.html", diseases=DISEASES)


@app.route("/recommendation")
def recommendation():
    disease_id = request.args.get("disease", type=int)
    recs = get_recommendations(disease_id)
    return render_template(
        "recommendation.html",
        diseases=DISEASES,
        recommendations=recs,
        selected_disease=disease_id,
    )


@app.route("/herb")
def herb():
    herb_id = request.args.get("herb_id", type=int)
    herb_data = get_herb(herb_id) if herb_id else None
    return render_template("herb_details.html", herb=herb_data)


@app.route("/electronic_tongue")
def electronic_tongue():
    return render_template("electronic_tongue.html", herbs=HERBS, tastes=TASTES)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
