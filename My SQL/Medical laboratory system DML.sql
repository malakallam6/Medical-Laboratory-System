INSERT INTO Laboratorian (Laboratorian_ID, Name, Street, City, Apartment) VALUES
(1,  'James Anderson',   '123 Maple St',     'New York',     'Apt 3'),
(2,  'Emily Johnson',    '456 Oak Ave',       'Los Angeles',  'Apt 7'),
(3,  'Michael Williams', '789 Pine Blvd',     'Chicago',      'Apt 12'),
(4,  'Sarah Davis',      '321 Elm St',        'Houston',      'Apt 5'),
(5,  'Robert Martinez',  '654 Cedar Rd',      'Phoenix',      'Apt 2'),
(6,  'Jessica Wilson',   '987 Birch Lane',    'Philadelphia', 'Apt 9'),
(7,  'David Thompson',   '147 Walnut Dr',     'San Antonio',  'Apt 1'),
(8,  'Ashley Garcia',    '258 Spruce Ave',    'San Diego',    'Apt 6'),
(9,  'Christopher Lee',  '369 Chestnut Blvd', 'Dallas',       'Apt 4'),
(10, 'Amanda White',     '741 Willow Way',    'San Jose',     'Apt 8');

INSERT INTO Lab_Phone (Laboratorian_ID, Lab_phone) VALUES
(1,  '212-555-0101'),
(2,  '310-555-0102'),
(3,  '312-555-0103'),
(4,  '713-555-0104'),
(5,  '602-555-0105'),
(6,  '215-555-0106'),
(7,  '210-555-0107'),
(8,  '619-555-0108'),
(9,  '214-555-0109'),
(10, '408-555-0110'),
(1,  '212-555-0111'),
(3,  '312-555-0112'),
(5,  '602-555-0113');

INSERT INTO COMPONENT (Component_ID, Name_Of_Component, Available_quantity, Minimum_quantity) VALUES
( 1, 'Test Tubes',        20,  100),
( 2, 'Pipettes',          300,  50),
( 3, 'Glucose Reagent',   15,   30),
( 4, 'Blood Agar Plate',  200,  40),
( 5, 'Urine Strips',      10,   80),
( 6, 'Lancets',           600, 120),
( 7, 'Centrifuge Tubes',  250,  50),
( 8, 'Saline Solution',   5,    20),
( 9, 'Microscope Slides', 350,  70),
(10, 'EDTA Tubes',        280,  60);

INSERT INTO MEDICAL_TEST (Test_ID, Name_Of_Medical_Test, Related_components, Price, Laboratorian_ID) VALUES
( 1, 'Blood Glucose',   'Glucose Reagent',    85,  1),
( 2, 'Complete Blood',  'EDTA Tubes',         120,  2),
( 3, 'Urinalysis',      'Urine Strips',        60,  3),
( 4, 'Blood Culture',   'Blood Agar Plate',   200,  4),
( 5, 'Lipid Panel',     'Centrifuge Tubes',   150,  5),
( 6, 'Thyroid TSH',     'Test Tubes',          95,  6),
( 7, 'HIV Screening',   'Lancets',            110,  7),
( 8, 'Kidney Function', 'Saline Solution',    130,  8),
( 9, 'Liver Panel',     'Pipettes',           140,  9),
(10, 'Malaria Test',    'Microscope Slides',   75, 10);

INSERT INTO ASSOCIATION (Component_ID, Test_ID) VALUES
( 3,  1),
(10,  2),
( 1,  2),
( 5,  3),
( 4,  4),
( 6,  4),
( 7,  5),
( 2,  5),
( 1,  6),
( 6,  7),
( 8,  8),
( 9,  9),
( 2,  9),
( 9, 10),
( 6, 10);

INSERT INTO Patient (Patient_ID, Patient_Name, Job, Birth_Date, Apartment, City, Street) VALUES
(12527, 'James Anderson',  'Engineer',     '1985-03-12', 'Apt 5',  'New York',     '5th Ave'),
(12528, 'Emily Johnson',   'Teacher',      '1990-07-24', 'Apt 12', 'Los Angeles',  'Sunset Blvd'),
(12529, 'Michael Smith',   'Doctor',       '1978-11-05', 'Apt 3',  'Chicago',      'Michigan Ave'),
(12530, 'Ashley Brown',    'Pharmacist',   '1995-01-18', 'Apt 7',  'Houston',      'Main St'),
(12531, 'Chris Davis',     'Accountant',   '1982-06-30', 'Apt 9',  'Phoenix',      'Central Ave'),
(12532, 'Jessica Wilson',  'Nurse',        '1993-09-14', 'Apt 2',  'Philadelphia', 'Broad St'),
(12533, 'Daniel Martinez', 'Lawyer',       '1975-04-22', 'Apt 15', 'San Antonio',  'Commerce St'),
(12534, 'Sarah Taylor',    'Architect',    '1988-12-01', 'Apt 6',  'San Diego',    'Harbor Dr'),
(12535, 'Ryan Thomas',     'Software Dev', '1997-08-09', 'Apt 11', 'Dallas',       'Elm St'),
(12536, 'Lauren White',    NULL,           '2000-02-27', 'Apt 1',  'Austin',       'Congress Ave');

INSERT INTO Patient_Phone (Patient_ID, Patient_Phone) VALUES
(12527, '2125550101'),
(12528, '3105550182'),
(12529, '3125550193'),
(12530, '7135550164'),
(12531, '6025550175'),
(12532, '2155550136'),
(12533, '2105550147'),
(12534, '6195550158'),
(12535, '2145550169'),
(12536, '5125550110');

INSERT INTO undergoes (Patient_ID, Test_ID) VALUES
(12527, 1),
(12528, 2),
(12529, 3),
(12530, 4),
(12531, 5),
(12532, 6),
(12533, 7),
(12534, 8),
(12535, 9),
(12536, 10);

INSERT INTO PREFORM (Laboratorian_ID, Test_ID) VALUES
(1,  1),
(2,  2),
(3,  3),
(4,  4),
(5,  5),
(6,  6),
(7,  7),
(8,  8),
(9,  9),
(10, 10);

INSERT INTO TEST_RESULT (Result, Laboratorian_ID, Patient_ID, TS_Date, Test_ID) VALUES
('Negative',     1,  12527, '2025-06-10', 1),
('Positive',     2,  12528, '2025-07-15', 2),
('Normal',       3,  12529, '2025-08-20', 3),
('Abnormal',     4,  12530, '2025-09-05', 4),
('Negative',     5,  12531, '2025-10-10', 5),
('Positive',     6,  12532, '2025-11-18', 6),
('Normal',       7,  12533, '2025-12-01', 7),
('Inconclusive', 8,  12534, '2026-01-12', 8),
('Negative',     9,  12535, '2026-02-20', 9),
('Positive',     10, 12536, '2026-03-02', 10),
('Normal',       1,  12529, '2026-03-10', 3),
('Abnormal',     2,  12531, '2026-04-15', 5),
('Negative',     3,  12533, '2026-04-22', 7);