CREATE FUNCTION this()
RETURNS trigger AS
$BODY$
	BEGIN
		NEW.status = 'worked';
		RETURN NEW;
	END
$BODY$
language plpgsql;





