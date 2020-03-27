-- Table: public.meteo

-- DROP TABLE public.meteo;

CREATE TABLE public.meteo
(
    id integer NOT NULL DEFAULT nextval('meteo_id_seq'::regclass),
    date_insert timestamp without time zone DEFAULT now(),
    temperature double precision,
    CONSTRAINT meteo_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.meteo
    OWNER to admin;