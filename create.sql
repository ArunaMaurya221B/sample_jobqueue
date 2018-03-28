do $$begin

CREATE TABLE %(name)s (
id integer PRIMARY KEY,
name VARCHAR(10),
status VARCHAR(10)
);
end $$language plpgsql;
