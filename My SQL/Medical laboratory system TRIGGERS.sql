-- Trigger
DELIMITER $$

CREATE TRIGGER decrement_component_stock
AFTER INSERT ON TEST_RESULT
FOR EACH ROW
BEGIN
    UPDATE COMPONENT c
    JOIN ASSOCIATION a ON c.Component_ID = a.Component_ID
    SET c.Available_quantity = c.Available_quantity - 1
    WHERE a.Test_ID = NEW.Test_ID;
END$$

DELIMITER ;
