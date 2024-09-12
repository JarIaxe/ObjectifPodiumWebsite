INSERT INTO public.song_session(
	id_song, id_session, found, isoral)
		select so.ID, se.ID, cast(0 as bit), cast(0 as bit)
		from public.song so
		cross join public.session se