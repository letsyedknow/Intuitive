CREATE SCHEMA API;

CREATE TABLE API.BIRD_POWER(
POWER_ID SERIAL,
CARD_ASSET_ID INT,
BIRD_NAME VARCHAR(255),
WINGSPAN INTEGER,
HABITAT_TYPE VARCHAR(255),
MAIN_FOOD VARCHAR(255)
);  

INSERT INTO API.BIRD_POWER(CARD_ASSET_ID,BIRD_NAME,WINGSPAN,HABITAT_TYPE,MAIN_FOOD)
SELECT B.CARD_ASSET_ID,B.BIRD_NAME,B.WINGSPAN,H.HABITAT_ID,F.MAIN_FOOD
FROM BIRD B
LEFT JOIN HABITAT H 
ON B.HABITAT_ID=H.HABITAT_ID
LEFT JOIN FOOD F
ON B.FOOD_TOKEN_ID=F.FOOD_TOKEN_ID 

----- Create a specific roll and authenticating
create role web_anon nologin;

grant usage on schema api to web_anon;
grant select on api.bird_power to web_anon;

create role authenticator noinherit login password 'mysecretpassword';
grant web_anon to authenticator;

---
---install open source postgrest
cd /usr/local/opt
# download from https://github.com/PostgREST/postgrest/releases/latest

tar xJf postgrest-v9.0.-macos-x64.tar.xz

./postgrest


--on basic terminal
cd /usr/local/opt
vi tutorial.conf

db-uri = "postgres://authenticator:mysecretpassword@localhost:5432/postgres"
db-schemas = "api"
db-anon-role = "web_anon"

--running the server make sure postgres is up and running 
./postgrest tutorial.conf

----open another terminal 
curl http://localhost:3000/bird_power

--Check the food 
curl http://localhost:3000/bird_power | grep "RODENT"
--result is in doc file

----