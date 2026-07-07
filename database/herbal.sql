CREATE DATABASE IF NOT EXISTS herbal_system;
USE herbal_system;

CREATE TABLE disease (
    disease_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    emoji VARCHAR(10)
);

CREATE TABLE herb (
    herb_id INT AUTO_INCREMENT PRIMARY KEY,
    herb_name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(150),
    description TEXT,
    taste VARCHAR(100),
    category VARCHAR(50),
    preparation TEXT,
    dosage VARCHAR(200),
    contraindications TEXT
);

CREATE TABLE recommendation (
    rec_id INT AUTO_INCREMENT PRIMARY KEY,
    herb_id INT NOT NULL,
    disease_id INT NOT NULL,
    dosage VARCHAR(200),
    preparation TEXT,
    effectiveness INT,
    FOREIGN KEY (herb_id) REFERENCES herb(herb_id),
    FOREIGN KEY (disease_id) REFERENCES disease(disease_id)
);

CREATE TABLE taste_profile (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,
    herb_id INT NOT NULL,
    sweet INT DEFAULT 0,
    sour INT DEFAULT 0,
    salty INT DEFAULT 0,
    bitter INT DEFAULT 0,
    umami INT DEFAULT 0,
    astringent INT DEFAULT 0,
    FOREIGN KEY (herb_id) REFERENCES herb(herb_id)
);

CREATE TABLE etongue_reading (
    reading_id INT AUTO_INCREMENT PRIMARY KEY,
    sample_name VARCHAR(100),
    sweet INT DEFAULT 0,
    sour INT DEFAULT 0,
    salty INT DEFAULT 0,
    bitter INT DEFAULT 0,
    umami INT DEFAULT 0,
    astringent INT DEFAULT 0,
    matched_herb_id INT,
    match_score INT,
    reading_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (matched_herb_id) REFERENCES herb(herb_id)
);

-- Sample Data: Diseases
INSERT INTO disease (disease_name, category, description, emoji) VALUES
('Arthritis', 'Musculoskeletal', 'Inflammation of joints causing pain and stiffness', '🦴'),
('Diabetes', 'Metabolic', 'Chronic condition affecting blood sugar regulation', '🩸'),
('Anxiety & Stress', 'Mental Health', 'Persistent worry and tension affecting daily life', '🧘'),
('Digestive Disorders', 'Gastrointestinal', 'Conditions affecting digestion and gut health', '🫄'),
('Skin Diseases', 'Dermatological', 'Various skin conditions including eczema and acne', '🧴'),
('Respiratory Infections', 'Respiratory', 'Infections affecting the respiratory tract', '🫁'),
('Insomnia', 'Sleep', 'Difficulty falling or staying asleep', '😴'),
('Low Immunity', 'Immune', 'Weakened immune system leading to frequent infections', '🛡️');

-- Sample Data: Herbs
INSERT INTO herb (herb_name, scientific_name, description, taste, category, preparation, dosage, contraindications) VALUES
('Turmeric', 'Curcuma longa', 'Golden spice with anti-inflammatory properties', 'Bitter, Pungent', 'Rhizome', 'Mix in warm milk with black pepper', '500-1000 mg daily', 'Avoid with blood thinners'),
('Ashwagandha', 'Withania somnifera', 'Powerful adaptogen for stress management', 'Bitter, Sweet', 'Root', 'Powder with warm milk and honey', '300-600 mg daily', 'Avoid during pregnancy'),
('Tulsi', 'Ocimum tenuiflorum', 'Queen of herbs with antimicrobial properties', 'Pungent, Bitter', 'Leaf', 'Steep leaves in hot water for tea', '2-3 cups tea daily', 'May lower blood sugar'),
('Ginger', 'Zingiber officinale', 'Widely used spice for digestion and nausea', 'Pungent, Sweet', 'Rhizome', 'Grate into hot water with lemon', '1-3 g daily', 'May increase bleeding risk'),
('Neem', 'Azadirachta indica', 'Versatile herb with antibacterial properties', 'Bitter', 'Leaf/Bark', 'Leaf juice or powder capsules', '250-500 mg daily', 'Not for pregnant women'),
('Amla', 'Phyllanthus emblica', 'Richest natural source of Vitamin C', 'Sour, Sweet', 'Fruit', 'Fresh juice or powder with honey', '1-2 tsp daily', 'May lower blood sugar'),
('Brahmi', 'Bacopa monnieri', 'Renowned brain tonic for memory enhancement', 'Bitter, Sweet', 'Herb', 'Powder with ghee and honey', '300-450 mg daily', 'May affect thyroid levels'),
('Triphala', 'Emblica + Terminalia spp.', 'Classical Ayurvedic three-fruit formulation', 'Sour, Bitter', 'Formulation', 'Powder in warm water at bedtime', '3-6 g daily', 'Avoid during pregnancy');

-- Sample Data: Recommendations
INSERT INTO recommendation (herb_id, disease_id, dosage, preparation, effectiveness) VALUES
(1, 1, '500 mg curcumin twice daily', 'Turmeric milk with black pepper', 85),
(4, 1, '2 g ginger powder daily', 'Ginger tea with honey', 70),
(5, 2, '250 mg neem powder twice daily', 'Neem leaf capsules', 75),
(6, 2, '1 tsp amla powder daily', 'Amla juice on empty stomach', 80),
(2, 3, '600 mg extract daily', 'Ashwagandha with warm milk', 90),
(3, 3, '2 cups tulsi tea daily', 'Fresh tulsi leaf tea', 80),
(7, 3, '450 mg brahmi daily', 'Brahmi powder with ghee', 85),
(4, 4, '1 g ginger before meals', 'Fresh ginger tea', 85),
(8, 4, '3 g triphala at bedtime', 'Triphala powder in warm water', 90),
(1, 5, 'Turmeric paste topically', 'Turmeric + coconut oil paste', 80),
(5, 5, 'Neem leaf paste', 'Crushed neem leaves topically', 85),
(3, 6, '3 cups tulsi tea daily', 'Tulsi tea with ginger', 85),
(4, 6, '2 g ginger daily', 'Ginger-honey tea', 80),
(2, 7, '600 mg at bedtime', 'Ashwagandha warm milk', 88),
(7, 7, '450 mg brahmi at night', 'Brahmi capsules before sleep', 82),
(6, 8, '2 tsp amla powder daily', 'Amla juice every morning', 90),
(3, 8, 'Daily tulsi tea', 'Tulsi with black pepper tea', 85),
(2, 8, '600 mg ashwagandha daily', 'Ashwagandha with milk', 80);

-- Sample Data: Taste Profiles
INSERT INTO taste_profile (herb_id, sweet, sour, salty, bitter, umami, astringent) VALUES
(1, 10, 5, 5, 70, 5, 30),
(2, 30, 10, 5, 50, 10, 20),
(3, 5, 5, 5, 40, 10, 50),
(4, 15, 10, 5, 20, 10, 15),
(5, 0, 5, 5, 90, 0, 60),
(6, 20, 60, 5, 10, 5, 40),
(7, 15, 5, 5, 55, 5, 25),
(8, 25, 40, 5, 30, 5, 50);
