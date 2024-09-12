INSERT INTO public.session_participant(
	id_session, id_participant)
	select se.ID, pa.ID
	from public.session se
	cross join public.participant pa