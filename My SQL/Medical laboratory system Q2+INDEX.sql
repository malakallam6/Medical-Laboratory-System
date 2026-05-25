-- Query 2: all tests performed by patient 12527 in the past year
SELECT
    mt.Name_Of_Medical_Test,
    tr.TS_Date,
    l.Name AS Laboratorian_Name
FROM TEST_RESULT tr
JOIN MEDICAL_TEST mt ON tr.Test_ID = mt.Test_ID
JOIN Laboratorian l ON tr.Laboratorian_ID = l.Laboratorian_ID
WHERE tr.Patient_ID = 12527
  AND tr.TS_Date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- Index for low-stock alerts
CREATE INDEX idx_low_stock
ON COMPONENT (Available_quantity, Minimum_quantity);

-- Query 3: low-stock alert
SELECT Component_ID, Name_Of_Component, Available_quantity, Minimum_quantity
FROM COMPONENT
WHERE Available_quantity < Minimum_quantity;