--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: assignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assignments (
    id integer NOT NULL,
    title text NOT NULL,
    max_grade numeric DEFAULT 10
);


ALTER TABLE public.assignments OWNER TO postgres;

--
-- Name: assignments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.assignments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.assignments_id_seq OWNER TO postgres;

--
-- Name: assignments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.assignments_id_seq OWNED BY public.assignments.id;


--
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    period integer NOT NULL,
    subject text NOT NULL,
    assignment_id integer,
    teacher_id integer
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- Name: grades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grades (
    id integer NOT NULL,
    received_grade numeric,
    student_id integer,
    assignment_id integer
);


ALTER TABLE public.grades OWNER TO postgres;

--
-- Name: grades_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.grades_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.grades_id_seq OWNER TO postgres;

--
-- Name: grades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.grades_id_seq OWNED BY public.grades.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL
);


ALTER TABLE public.students OWNER TO postgres;

--
-- Name: students_assignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students_assignments (
    student_id integer NOT NULL,
    assignment_id integer NOT NULL
);


ALTER TABLE public.students_assignments OWNER TO postgres;

--
-- Name: students_courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students_courses (
    student_id integer NOT NULL,
    course_id integer NOT NULL
);


ALTER TABLE public.students_courses OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: students_teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students_teachers (
    student_id integer NOT NULL,
    teacher_id integer NOT NULL
);


ALTER TABLE public.students_teachers OWNER TO postgres;

--
-- Name: teachaccts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachaccts (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL
);


ALTER TABLE public.teachaccts OWNER TO postgres;

--
-- Name: teachaccts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teachaccts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachaccts_id_seq OWNER TO postgres;

--
-- Name: teachaccts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teachaccts_id_seq OWNED BY public.teachaccts.id;


--
-- Name: teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachers (
    id integer NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    teachacct_id integer
);


ALTER TABLE public.teachers OWNER TO postgres;

--
-- Name: teachers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teachers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachers_id_seq OWNER TO postgres;

--
-- Name: teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teachers_id_seq OWNED BY public.teachers.id;


--
-- Name: assignments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignments ALTER COLUMN id SET DEFAULT nextval('public.assignments_id_seq'::regclass);


--
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- Name: grades id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades ALTER COLUMN id SET DEFAULT nextval('public.grades_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Name: teachaccts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachaccts ALTER COLUMN id SET DEFAULT nextval('public.teachaccts_id_seq'::regclass);


--
-- Name: teachers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers ALTER COLUMN id SET DEFAULT nextval('public.teachers_id_seq'::regclass);


--
-- Data for Name: assignments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assignments (id, title, max_grade) FROM stdin;
1	Density lab	10
2	Mineral identification lab	10
3	Python intro classwork	5
4	About me project	20
5	Python intro	10
\.


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, period, subject, assignment_id, teacher_id) FROM stdin;
7	1	ES-sec1	\N	\N
8	3	CS-sec1	\N	\N
9	6	CS-sec2	\N	\N
10	7	ES-sec2	\N	\N
11	8	ES-sec3	\N	\N
\.


--
-- Data for Name: grades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.grades (id, received_grade, student_id, assignment_id) FROM stdin;
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (id, first_name, last_name) FROM stdin;
1	Aaron	K
2	Beth	M
3	Chris	L
4	Doris	G
\.


--
-- Data for Name: students_assignments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students_assignments (student_id, assignment_id) FROM stdin;
\.


--
-- Data for Name: students_courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students_courses (student_id, course_id) FROM stdin;
\.


--
-- Data for Name: students_teachers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students_teachers (student_id, teacher_id) FROM stdin;
\.


--
-- Data for Name: teachaccts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teachaccts (id, username, password) FROM stdin;
1	spak	Pak12345
\.


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teachers (id, first_name, last_name, teachacct_id) FROM stdin;
1	Sangmin	Pak	\N
\.


--
-- Name: assignments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.assignments_id_seq', 5, true);


--
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 11, true);


--
-- Name: grades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.grades_id_seq', 1, false);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 12, true);


--
-- Name: teachaccts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teachaccts_id_seq', 4, true);


--
-- Name: teachers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teachers_id_seq', 5, true);


--
-- Name: assignments assignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignments
    ADD CONSTRAINT assignments_pkey PRIMARY KEY (id);


--
-- Name: assignments assignments_title_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignments
    ADD CONSTRAINT assignments_title_key UNIQUE (title);


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- Name: grades grades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT grades_pkey PRIMARY KEY (id);


--
-- Name: students_assignments students_assignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_assignments
    ADD CONSTRAINT students_assignments_pkey PRIMARY KEY (student_id, assignment_id);


--
-- Name: students_courses students_courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT students_courses_pkey PRIMARY KEY (student_id, course_id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: students_teachers students_teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_teachers
    ADD CONSTRAINT students_teachers_pkey PRIMARY KEY (student_id, teacher_id);


--
-- Name: teachaccts teachaccts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachaccts
    ADD CONSTRAINT teachaccts_pkey PRIMARY KEY (id);


--
-- Name: teachaccts teachaccts_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachaccts
    ADD CONSTRAINT teachaccts_username_key UNIQUE (username);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- Name: teachers teachers_teachacct_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_teachacct_id_key UNIQUE (teachacct_id);


--
-- Name: grades fk_grades_assignments; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT fk_grades_assignments FOREIGN KEY (assignment_id) REFERENCES public.assignments(id);


--
-- Name: grades fk_grades_students; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT fk_grades_students FOREIGN KEY (student_id) REFERENCES public.students(id);


--
-- Name: students_assignments fk_students_assignments_assignments; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_assignments
    ADD CONSTRAINT fk_students_assignments_assignments FOREIGN KEY (assignment_id) REFERENCES public.assignments(id);


--
-- Name: students_assignments fk_students_assignments_students; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_assignments
    ADD CONSTRAINT fk_students_assignments_students FOREIGN KEY (student_id) REFERENCES public.students(id);


--
-- Name: students_courses fk_students_courses_courses; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT fk_students_courses_courses FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- Name: students_courses fk_students_courses_students; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT fk_students_courses_students FOREIGN KEY (student_id) REFERENCES public.students(id);


--
-- Name: students_teachers fk_students_teachers_students; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_teachers
    ADD CONSTRAINT fk_students_teachers_students FOREIGN KEY (student_id) REFERENCES public.courses(id);


--
-- Name: students_teachers fk_students_teachers_teachers; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students_teachers
    ADD CONSTRAINT fk_students_teachers_teachers FOREIGN KEY (teacher_id) REFERENCES public.teachers(id);


--
-- PostgreSQL database dump complete
--

