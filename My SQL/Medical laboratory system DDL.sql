drop database PROJECT;
create database PROJECT;
use PROJECT;

create table if not exists COMPONENT (
    Component_ID int,
    Name_Of_Component varchar(20) not null,
    Available_quantity int,
    Minimum_quantity int,
    primary key (Component_ID)
);

create table if not exists MEDICAL_TEST (
    Test_ID int,
    Name_Of_Medical_Test varchar(20) not null,
    Related_components varchar(20),
    Price int,
    Laboratorian_ID int,
    primary key (Test_ID)
);

create table if not exists ASSOCIATION (
    Component_ID int,
    Test_ID int
);

CREATE TABLE IF NOT EXISTS PREFORM (
    Laboratorian_ID int NOT NULL,
    Test_ID int NOT NULL,
    PRIMARY KEY (Laboratorian_ID, Test_ID),
    FOREIGN KEY (Test_ID) REFERENCES MEDICAL_TEST(Test_ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Laboratorian (
    Laboratorian_ID int PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Street varchar(100),
    City varchar(50),
    Apartment varchar(50)
);

CREATE TABLE Lab_Phone (
    Laboratorian_ID int,
    Lab_phone varchar(15),
    PRIMARY KEY (Laboratorian_ID, Lab_phone),
    FOREIGN KEY (Laboratorian_ID) REFERENCES Laboratorian(Laboratorian_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create table if not exists Patient (
    Patient_ID int,
    Patient_Name varchar(40) not null,
    Job varchar(40),
    Birth_Date date,
    Apartment varchar(100),
    City varchar(100),
    Street varchar(100),
    primary key (Patient_ID)
);

create table if not exists Patient_Phone(
    Patient_ID int,
    Patient_Phone varchar(15),
    primary key (Patient_Phone,Patient_ID),
    foreign key (Patient_ID) REFERENCES Patient(Patient_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS TEST_RESULT (
    Test_Result_ID int NOT NULL AUTO_INCREMENT,
    Result varchar(255) NOT NULL,
    Laboratorian_ID int NOT NULL,
    Patient_ID int NOT NULL,
    TS_Date date NOT NULL,
    Test_ID int NOT NULL,
    PRIMARY KEY (Test_Result_ID),
    FOREIGN KEY (Laboratorian_ID) REFERENCES Laboratorian(Laboratorian_ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (Test_ID) REFERENCES MEDICAL_TEST(Test_ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS undergoes (
    Patient_ID int,
    Test_ID int,
    foreign key (Patient_ID) REFERENCES Patient(Patient_ID),
    foreign key (Test_ID) REFERENCES MEDICAL_TEST(Test_ID)
);

ALTER TABLE MEDICAL_TEST
ADD FOREIGN KEY (Laboratorian_ID)
REFERENCES Laboratorian(Laboratorian_ID)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE ASSOCIATION
ADD FOREIGN KEY (Component_ID)
REFERENCES COMPONENT(Component_ID)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE ASSOCIATION
ADD FOREIGN KEY (Test_ID)
REFERENCES MEDICAL_TEST(Test_ID)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE PREFORM
ADD FOREIGN KEY (Laboratorian_ID)
REFERENCES Laboratorian(Laboratorian_ID)
ON DELETE RESTRICT
ON UPDATE CASCADE;