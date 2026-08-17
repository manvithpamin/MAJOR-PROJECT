from flask import Flask, render_template, request

app = Flask(__name__)

# =========================================================
# 30 HERBS DATASET
# =========================================================

HERBS = [

    {
        "id": 1,
        "name": "Tulsi",
        "emoji": "🍃",
        "scientific_name": "Ocimum tenuiflorum",
        "description": "A traditional Ayurvedic herb commonly used in herbal preparations.",
        "taste": "Pungent, Bitter",
        "category": "Leaf",
        "properties": ["Traditional respiratory support", "Antioxidant"],
        "uses": ["Fever", "Cold and cough", "Respiratory wellness"],
        "preparation": "Traditionally prepared as herbal tea or decoction.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under appropriate professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 40, "umami": 10, "astringent": 50
        }
    },

    {
        "id": 2,
        "name": "Ashwagandha",
        "emoji": "🌿",
        "scientific_name": "Withania somnifera",
        "description": "Traditional Ayurvedic root used in restorative herbal preparations.",
        "taste": "Bitter, Sweet",
        "category": "Root",
        "properties": ["Traditional restorative use", "Adaptogenic use"],
        "uses": ["Stress", "Fatigue", "General wellness"],
        "preparation": "Traditionally used as powder or in formulated preparations.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 30, "sour": 10, "salty": 5,
            "bitter": 50, "umami": 10, "astringent": 20
        }
    },

    {
        "id": 3,
        "name": "Turmeric",
        "emoji": "🟡",
        "scientific_name": "Curcuma longa",
        "description": "Traditional rhizome widely used in Ayurvedic preparations.",
        "taste": "Bitter, Pungent",
        "category": "Rhizome",
        "properties": ["Antioxidant", "Traditional anti-inflammatory use"],
        "uses": ["Joint wellness", "Digestive wellness", "Skin preparations"],
        "preparation": "Used as powder, decoction or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 5, "salty": 5,
            "bitter": 70, "umami": 5, "astringent": 30
        }
    },

    {
        "id": 4,
        "name": "Ginger",
        "emoji": "🫚",
        "scientific_name": "Zingiber officinale",
        "description": "Traditional rhizome commonly used in digestive and respiratory preparations.",
        "taste": "Pungent",
        "category": "Rhizome",
        "properties": ["Digestive support", "Antioxidant"],
        "uses": ["Indigestion", "Nausea", "Cold and cough"],
        "preparation": "Commonly prepared as tea or decoction.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 15, "sour": 10, "salty": 5,
            "bitter": 20, "umami": 10, "astringent": 15
        }
    },

    {
        "id": 5,
        "name": "Neem",
        "emoji": "🌳",
        "scientific_name": "Azadirachta indica",
        "description": "Traditional medicinal plant commonly used in Ayurvedic preparations.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Traditional antimicrobial use", "Antioxidant"],
        "uses": ["Skin wellness", "Oral care", "Traditional fever preparations"],
        "preparation": "Leaves are traditionally used in decoctions and other preparations.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 0, "sour": 5, "salty": 5,
            "bitter": 90, "umami": 0, "astringent": 60
        }
    },

    {
        "id": 6,
        "name": "Amla",
        "emoji": "🫐",
        "scientific_name": "Phyllanthus emblica",
        "description": "Traditional fruit used extensively in Ayurvedic formulations.",
        "taste": "Sour, Sweet, Astringent",
        "category": "Fruit",
        "properties": ["Antioxidant", "Traditional wellness support"],
        "uses": ["General wellness", "Digestive wellness", "Hair care"],
        "preparation": "Used as fruit, powder, juice or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 20, "sour": 60, "salty": 5,
            "bitter": 10, "umami": 5, "astringent": 40
        }
    },

    {
        "id": 7,
        "name": "Brahmi",
        "emoji": "🧠",
        "scientific_name": "Bacopa monnieri",
        "description": "Traditional Ayurvedic herb associated with cognitive wellness.",
        "taste": "Bitter",
        "category": "Whole plant",
        "properties": ["Traditional cognitive support", "Antioxidant"],
        "uses": ["Memory support", "Concentration", "Stress"],
        "preparation": "Used traditionally as powder or formulated preparation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 15, "sour": 5, "salty": 5,
            "bitter": 55, "umami": 5, "astringent": 25
        }
    },

    {
        "id": 8,
        "name": "Giloy",
        "emoji": "🌿",
        "scientific_name": "Tinospora cordifolia",
        "description": "Traditional Ayurvedic plant used in several herbal preparations.",
        "taste": "Bitter",
        "category": "Stem",
        "properties": ["Traditional immune support", "Antioxidant"],
        "uses": ["Fever-related preparations", "General wellness"],
        "preparation": "Traditionally used as decoction or formulated preparation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 70, "umami": 5, "astringent": 40
        }
    },

    {
        "id": 9,
        "name": "Licorice",
        "emoji": "🌱",
        "scientific_name": "Glycyrrhiza glabra",
        "description": "Traditional root used in many herbal preparations.",
        "taste": "Sweet",
        "category": "Root",
        "properties": ["Traditional throat support", "Soothing"],
        "uses": ["Cough", "Sore throat", "Digestive wellness"],
        "preparation": "Used as powder, infusion or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 80, "sour": 5, "salty": 5,
            "bitter": 10, "umami": 5, "astringent": 10
        }
    },

    {
        "id": 10,
        "name": "Black Pepper",
        "emoji": "🌶️",
        "scientific_name": "Piper nigrum",
        "description": "Traditional spice used in Ayurvedic formulations.",
        "taste": "Pungent",
        "category": "Fruit",
        "properties": ["Digestive support", "Traditional respiratory use"],
        "uses": ["Cold and cough", "Digestive wellness"],
        "preparation": "Used as powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 20, "umami": 5, "astringent": 10
        }
    },

    {
        "id": 11,
        "name": "Cinnamon",
        "emoji": "🪵",
        "scientific_name": "Cinnamomum verum",
        "description": "Traditional aromatic bark used in herbal preparations.",
        "taste": "Sweet, Pungent",
        "category": "Bark",
        "properties": ["Antioxidant", "Traditional digestive use"],
        "uses": ["Digestive wellness", "Cold preparations"],
        "preparation": "Used as infusion, decoction or powder.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 40, "sour": 5, "salty": 5,
            "bitter": 15, "umami": 5, "astringent": 15
        }
    },

    {
        "id": 12,
        "name": "Cardamom",
        "emoji": "🌱",
        "scientific_name": "Elettaria cardamomum",
        "description": "Traditional aromatic spice used in herbal preparations.",
        "taste": "Sweet, Pungent",
        "category": "Seed",
        "properties": ["Digestive support", "Aromatic"],
        "uses": ["Indigestion", "Respiratory preparations"],
        "preparation": "Used as crushed seed or infusion.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 35, "sour": 5, "salty": 5,
            "bitter": 15, "umami": 5, "astringent": 10
        }
    },

    {
        "id": 13,
        "name": "Shatavari",
        "emoji": "🌿",
        "scientific_name": "Asparagus racemosus",
        "description": "Traditional Ayurvedic root used in restorative formulations.",
        "taste": "Sweet, Bitter",
        "category": "Root",
        "properties": ["Traditional restorative use"],
        "uses": ["General wellness", "Women's health preparations"],
        "preparation": "Used as powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 45, "sour": 5, "salty": 5,
            "bitter": 20, "umami": 5, "astringent": 15
        }
    },

    {
        "id": 14,
        "name": "Arjuna",
        "emoji": "🌳",
        "scientific_name": "Terminalia arjuna",
        "description": "Traditional Ayurvedic bark used in herbal formulations.",
        "taste": "Astringent",
        "category": "Bark",
        "properties": ["Traditional cardiovascular wellness use"],
        "uses": ["Heart-health preparations", "General wellness"],
        "preparation": "Traditionally used as bark powder or decoction.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 20, "umami": 5, "astringent": 80
        }
    },

    {
        "id": 15,
        "name": "Haritaki",
        "emoji": "🟤",
        "scientific_name": "Terminalia chebula",
        "description": "Traditional Ayurvedic fruit and major ingredient of Triphala.",
        "taste": "Astringent, Bitter",
        "category": "Fruit",
        "properties": ["Digestive support", "Traditional cleansing use"],
        "uses": ["Constipation", "Digestive wellness"],
        "preparation": "Used as powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 10, "salty": 5,
            "bitter": 30, "umami": 5, "astringent": 70
        }
    },

    {
        "id": 16,
        "name": "Bibhitaki",
        "emoji": "🟤",
        "scientific_name": "Terminalia bellirica",
        "description": "Traditional Ayurvedic fruit used in Triphala.",
        "taste": "Astringent",
        "category": "Fruit",
        "properties": ["Traditional digestive use"],
        "uses": ["Digestive wellness", "Respiratory preparations"],
        "preparation": "Used as powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 5, "salty": 5,
            "bitter": 20, "umami": 5, "astringent": 75
        }
    },

    {
        "id": 17,
        "name": "Bael",
        "emoji": "🍈",
        "scientific_name": "Aegle marmelos",
        "description": "Traditional fruit used particularly in digestive preparations.",
        "taste": "Sweet, Astringent",
        "category": "Fruit",
        "properties": ["Traditional digestive support"],
        "uses": ["Digestive wellness", "Gastrointestinal preparations"],
        "preparation": "Used as fruit pulp, powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 50, "sour": 10, "salty": 5,
            "bitter": 10, "umami": 5, "astringent": 50
        }
    },

    {
        "id": 18,
        "name": "Punarnava",
        "emoji": "🌿",
        "scientific_name": "Boerhaavia diffusa",
        "description": "Traditional Ayurvedic plant used in several herbal formulations.",
        "taste": "Bitter, Astringent",
        "category": "Root/Whole plant",
        "properties": ["Traditional urinary wellness use"],
        "uses": ["Urinary wellness", "General wellness"],
        "preparation": "Used as powder, decoction or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 50, "umami": 5, "astringent": 50
        }
    },

    {
        "id": 19,
        "name": "Kalmegh",
        "emoji": "🌿",
        "scientific_name": "Andrographis paniculata",
        "description": "Traditional bitter herb used in Ayurvedic preparations.",
        "taste": "Very Bitter",
        "category": "Whole plant",
        "properties": ["Traditional immune use", "Digestive support"],
        "uses": ["Fever-related preparations", "Digestive wellness"],
        "preparation": "Used as powder, decoction or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 0, "sour": 5, "salty": 5,
            "bitter": 95, "umami": 0, "astringent": 60
        }
    },

    {
        "id": 20,
        "name": "Shankhpushpi",
        "emoji": "🌸",
        "scientific_name": "Convolvulus pluricaulis",
        "description": "Traditional Ayurvedic herb associated with mental wellness.",
        "taste": "Bitter",
        "category": "Aerial part",
        "properties": ["Traditional cognitive support"],
        "uses": ["Memory support", "Stress", "Mental wellness"],
        "preparation": "Used as powder or formulated preparation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 5, "salty": 5,
            "bitter": 60, "umami": 5, "astringent": 30
        }
    },

    {
        "id": 21,
        "name": "Jatamansi",
        "emoji": "🌿",
        "scientific_name": "Nardostachys jatamansi",
        "description": "Traditional aromatic root used in Ayurvedic formulations.",
        "taste": "Bitter, Pungent",
        "category": "Root",
        "properties": ["Traditional calming use"],
        "uses": ["Stress", "Sleep wellness", "Mental wellness"],
        "preparation": "Used as powder or formulated preparation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 50, "umami": 5, "astringent": 20
        }
    },

    {
        "id": 22,
        "name": "Lemongrass",
        "emoji": "🌱",
        "scientific_name": "Cymbopogon citratus",
        "description": "Aromatic plant commonly used in herbal teas.",
        "taste": "Citrus, Pungent",
        "category": "Leaf",
        "properties": ["Aromatic", "Antioxidant"],
        "uses": ["Digestive wellness", "Relaxation", "Herbal tea"],
        "preparation": "Commonly prepared as herbal infusion.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 20, "sour": 20, "salty": 5,
            "bitter": 15, "umami": 5, "astringent": 20
        }
    },

    {
        "id": 23,
        "name": "Moringa",
        "emoji": "🌿",
        "scientific_name": "Moringa oleifera",
        "description": "Nutrient-rich plant traditionally used in food and herbal preparations.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Antioxidant", "Nutritional support"],
        "uses": ["General wellness", "Nutritional support"],
        "preparation": "Leaves are commonly used as powder or food ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 5, "salty": 5,
            "bitter": 60, "umami": 10, "astringent": 30
        }
    },

    {
        "id": 24,
        "name": "Aloe Vera",
        "emoji": "🌵",
        "scientific_name": "Aloe barbadensis",
        "description": "Traditional plant used in topical and herbal preparations.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Traditional skin use", "Soothing"],
        "uses": ["Skin preparations", "Digestive formulations"],
        "preparation": "Gel is used in appropriate preparations.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 15, "salty": 5,
            "bitter": 60, "umami": 5, "astringent": 30
        }
    },

    {
        "id": 25,
        "name": "Gudmar",
        "emoji": "🌿",
        "scientific_name": "Gymnema sylvestre",
        "description": "Traditional medicinal plant associated with metabolic wellness.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Traditional metabolic support"],
        "uses": ["Metabolic wellness", "General wellness"],
        "preparation": "Used as leaf powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 0, "sour": 5, "salty": 5,
            "bitter": 90, "umami": 0, "astringent": 40
        }
    },

    {
        "id": 26,
        "name": "Ashoka",
        "emoji": "🌳",
        "scientific_name": "Saraca asoca",
        "description": "Traditional Ayurvedic bark used in women's health formulations.",
        "taste": "Astringent",
        "category": "Bark",
        "properties": ["Traditional women's health use"],
        "uses": ["Traditional menstrual health preparations"],
        "preparation": "Traditionally used as bark-based formulation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 20, "umami": 5, "astringent": 80
        }
    },

    {
        "id": 27,
        "name": "Guggul",
        "emoji": "🌿",
        "scientific_name": "Commiphora mukul",
        "description": "Traditional resin used in several Ayurvedic formulations.",
        "taste": "Bitter, Pungent",
        "category": "Gum/Resin",
        "properties": ["Traditional joint wellness use"],
        "uses": ["Joint wellness", "Traditional metabolic preparations"],
        "preparation": "Used after appropriate purification and formulation.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 45, "umami": 5, "astringent": 30
        }
    },

    {
        "id": 28,
        "name": "Vasaka",
        "emoji": "🌿",
        "scientific_name": "Adhatoda vasica",
        "description": "Traditional Ayurvedic leaf used in respiratory preparations.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Traditional respiratory support"],
        "uses": ["Cough", "Respiratory preparations"],
        "preparation": "Used as decoction or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 75, "umami": 5, "astringent": 40
        }
    },

    {
        "id": 29,
        "name": "Centella",
        "emoji": "🌿",
        "scientific_name": "Centella asiatica",
        "description": "Traditional herb used in cognitive and skin-related preparations.",
        "taste": "Bitter",
        "category": "Whole plant",
        "properties": ["Traditional cognitive support", "Skin wellness"],
        "uses": ["Memory support", "Skin preparations", "General wellness"],
        "preparation": "Used as fresh herb, powder or formulation ingredient.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 10, "sour": 5, "salty": 5,
            "bitter": 55, "umami": 5, "astringent": 35
        }
    },

    {
        "id": 30,
        "name": "Senna",
        "emoji": "🌿",
        "scientific_name": "Cassia angustifolia",
        "description": "Traditional medicinal leaf used in preparations for occasional constipation.",
        "taste": "Bitter",
        "category": "Leaf",
        "properties": ["Traditional laxative use"],
        "uses": ["Occasional constipation"],
        "preparation": "Used in standardized herbal preparations.",
        "dosage": "Formulation dependent",
        "contraindications": "Use under professional guidance.",
        "taste_profile": {
            "sweet": 5, "sour": 5, "salty": 5,
            "bitter": 70, "umami": 5, "astringent": 30
        }
    }
]


# =========================================================
# DISEASE / HEALTH ISSUE DATASET
# =========================================================

DISEASES = [

    {
        "id": 1,
        "name": "Fever",
        "emoji": "🌡️",
        "category": "General",
        "description": "Traditional herbal preparations associated with fever and general wellness.",
        "herb_count": 5
    },

    {
        "id": 2,
        "name": "Cold & Cough",
        "emoji": "🤧",
        "category": "Respiratory",
        "description": "Traditional herbal preparations associated with cold, cough and respiratory wellness.",
        "herb_count": 7
    },

    {
        "id": 3,
        "name": "Digestive Problems",
        "emoji": "🫄",
        "category": "Digestive",
        "description": "Traditional preparations associated with digestive wellness.",
        "herb_count": 7
    },

    {
        "id": 4,
        "name": "Stress & Anxiety",
        "emoji": "🧘",
        "category": "Mental Wellness",
        "description": "Traditional herbal preparations associated with relaxation and mental wellness.",
        "herb_count": 6
    },

    {
        "id": 5,
        "name": "Sleep Problems",
        "emoji": "😴",
        "category": "Sleep",
        "description": "Traditional herbal preparations associated with sleep and relaxation.",
        "herb_count": 4
    },

    {
        "id": 6,
        "name": "Joint & Muscle Wellness",
        "emoji": "🦴",
        "category": "Musculoskeletal",
        "description": "Traditional preparations associated with joint and muscle wellness.",
        "herb_count": 5
    },

    {
        "id": 7,
        "name": "Skin Problems",
        "emoji": "🧴",
        "category": "Skin",
        "description": "Traditional herbal preparations associated with skin wellness.",
        "herb_count": 5
    },

    {
        "id": 8,
        "name": "General Immunity & Wellness",
        "emoji": "🛡️",
        "category": "General Wellness",
        "description": "Traditional herbal preparations associated with general wellness.",
        "herb_count": 6
    },

    {
        "id": 9,
        "name": "Metabolic Wellness",
        "emoji": "🩸",
        "category": "Metabolic",
        "description": "Traditional herbal preparations associated with metabolic wellness.",
        "herb_count": 4
    },

    {
        "id": 10,
        "name": "Women's Health",
        "emoji": "🌸",
        "category": "Women's Health",
        "description": "Traditional herbal preparations associated with women's health.",
        "herb_count": 3
    }
]


# =========================================================
# HERB → HEALTH ISSUE RECOMMENDATIONS
# =========================================================

RECOMMENDATIONS = [

    # Fever
    {
        "herb_id": 1,
        "disease_id": 1,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Tulsi herbal tea/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 5,
        "disease_id": 1,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Neem preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 8,
        "disease_id": 1,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Giloy decoction/formulation",
        "effectiveness": 0
    },
    {
        "herb_id": 19,
        "disease_id": 1,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Kalmegh preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 6,
        "disease_id": 1,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Amla preparation",
        "effectiveness": 0
    },

    # Cold & Cough
    {
        "herb_id": 1,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Tulsi herbal tea/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 4,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Ginger herbal tea/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 9,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Licorice herbal preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 10,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Black pepper herbal preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 11,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Cinnamon infusion/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 28,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Vasaka preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 12,
        "disease_id": 2,
        "dosage": "Formulation dependent",
        "preparation": "Cardamom herbal infusion",
        "effectiveness": 0
    },

    # Digestive Problems
    {
        "herb_id": 4,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Ginger tea/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 10,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Black pepper preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 12,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Cardamom infusion",
        "effectiveness": 0
    },
    {
        "herb_id": 15,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Haritaki preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 16,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Bibhitaki preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 17,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Bael preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 30,
        "disease_id": 3,
        "dosage": "Formulation dependent",
        "preparation": "Standardized Senna preparation",
        "effectiveness": 0
    },

    # Stress & Anxiety
    {
        "herb_id": 2,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Ashwagandha preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 7,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Brahmi preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 20,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Shankhpushpi preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 21,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Jatamansi preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 29,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Centella preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 12,
        "disease_id": 4,
        "dosage": "Formulation dependent",
        "preparation": "Cardamom herbal infusion",
        "effectiveness": 0
    },

    # Sleep
    {
        "herb_id": 2,
        "disease_id": 5,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Ashwagandha preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 7,
        "disease_id": 5,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Brahmi preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 20,
        "disease_id": 5,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Shankhpushpi preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 21,
        "disease_id": 5,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Jatamansi preparation",
        "effectiveness": 0
    },

    # Joint & Muscle Wellness
    {
        "herb_id": 3,
        "disease_id": 6,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Turmeric preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 4,
        "disease_id": 6,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Ginger preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 27,
        "disease_id": 6,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Guggul formulation",
        "effectiveness": 0
    },
    {
        "herb_id": 14,
        "disease_id": 6,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Arjuna preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 6,
        "disease_id": 6,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Amla preparation",
        "effectiveness": 0
    },

    # Skin
    {
        "herb_id": 3,
        "disease_id": 7,
        "dosage": "Formulation dependent",
        "preparation": "Traditional turmeric preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 5,
        "disease_id": 7,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Neem preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 24,
        "disease_id": 7,
        "dosage": "Formulation dependent",
        "preparation": "Aloe vera gel-based preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 29,
        "disease_id": 7,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Centella preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 23,
        "disease_id": 7,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Moringa preparation",
        "effectiveness": 0
    },

    # General Immunity & Wellness
    {
        "herb_id": 1,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Tulsi tea/decoction",
        "effectiveness": 0
    },
    {
        "herb_id": 6,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Amla preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 8,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Giloy preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 19,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Kalmegh preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 23,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Moringa preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 3,
        "disease_id": 8,
        "dosage": "Formulation dependent",
        "preparation": "Turmeric preparation",
        "effectiveness": 0
    },

    # Metabolic Wellness
    {
        "herb_id": 25,
        "disease_id": 9,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Gudmar preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 3,
        "disease_id": 9,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Turmeric preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 6,
        "disease_id": 9,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Amla preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 27,
        "disease_id": 9,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Guggul formulation",
        "effectiveness": 0
    },

    # Women's Health
    {
        "herb_id": 13,
        "disease_id": 10,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Shatavari preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 26,
        "disease_id": 10,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Ashoka preparation",
        "effectiveness": 0
    },
    {
        "herb_id": 6,
        "disease_id": 10,
        "dosage": "Formulation dependent",
        "preparation": "Traditional Amla preparation",
        "effectiveness": 0
    }
]


# =========================================================
# TASTE DATA
# =========================================================

TASTES = [
    {"id": "sweet", "name": "Sweet"},
    {"id": "sour", "name": "Sour"},
    {"id": "salty", "name": "Salty"},
    {"id": "bitter", "name": "Bitter"},
    {"id": "umami", "name": "Umami"},
    {"id": "astringent", "name": "Astringent"}
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_herb(herb_id):
    return next(
        (herb for herb in HERBS if herb["id"] == herb_id),
        None
    )


def get_disease(disease_id):
    return next(
        (disease for disease in DISEASES if disease["id"] == disease_id),
        None
    )


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
                "effectiveness": rec["effectiveness"]
            })

    return results


# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        herbs=HERBS,
        diseases=DISEASES
    )


@app.route("/disease")
def disease():

    return render_template(
        "disease.html",
        diseases=DISEASES
    )


@app.route("/recommendation")
def recommendation():

    disease_id = request.args.get(
        "disease",
        type=int
    )

    recs = get_recommendations(disease_id)

    return render_template(
        "recommendation.html",
        diseases=DISEASES,
        recommendations=recs,
        selected_disease=disease_id
    )


@app.route("/herb")
def herb():

    herb_id = request.args.get(
        "herb_id",
        type=int
    )

    herb_data = (
        get_herb(herb_id)
        if herb_id
        else None
    )

    return render_template(
        "herb_details.html",
        herb=herb_data
    )


@app.route("/electronic_tongue")
def electronic_tongue():

    return render_template(
        "electronic_tongue.html",
        herbs=HERBS,
        tastes=TASTES
    )


@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )