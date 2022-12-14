def validate(function):
    INPUTS = [
        ("aaabbc", "cbabaa"),
        ("aaabbcd", "ecbabaa"),
        ("3Ofri7zTyUFOucos", "fO7OUT3zoysrFiuc"),
        ("hzDaY8NsbUtzEGd9mjieZWTE0ZthOLnC", "iabe08dthTOZ9CEsmYZULtWGnNzzEjDh"),
        ("ylmSLYxmqQf4edzkCHrIlFe41DXWfBdQX3rnU6TjCc9wKBuht4tzQoWEAnY6Jbzk", "Qlmz6hQXjBoxfCwmXUzWQ4cI4LdHztyTfkuSdnWqKABCYrelekDE3J1br469tfnY"),
        ("uv7AXnIIh4chVnTHfUDWmoxhG3qL6dIyqgUJyYEDjOSlMOI4tacEKDNk8Pg4ViiNXAkiRcaPSo5wZ37g7LgU24hAjxVWjZOlKqcRIf9ptFekkFTyZJFOPo18xaVvGidZ", "O3h6cFxIUnToyLlSAVagFkfmVePZRxchcVovgIOEiJZXYuTSiJyk4lwGhPj3DcNWgZ7D8O2Lakk7qIOfiI4dZtURjdpN6Wv7xEIgnHGqi81hA4DVPaMKjXFyU9AtKq4o"),
        ("knKlj5Lfmm2V57GpmABeidJx8DkEwsGQywt3d8fcTa18QkOb8xpMw2T54KMs623ZfwJRUL4rbvUXUOZivZI2w4EcIRJXQKDlgCrE5COYxrKyIVEX3znYpH1EnOeflbhw", "wprs3p8XYG5Jswntyg2Q5AI8wL3zkmEixyCrlK8drepV18jBMMkDfJnEvi6bwQE42fclLdRwKQZx4ZOU2OXZxnUe1VEKhGlTwf45EKXaT7YCmD2IRU5bJmf3bcvH00kI"),
        ("Possession her thoroughly remarkably terminated man continuing. Removed greater to do ability. You shy shall while but wrote marry. Call why sake has sing pure. Gay six set polite nature worthy. So matter be me we wisdom should basket moment merely. Me burst ample wrong which would mr he could. Visit arise my point timed drawn no. Can friendly laughter goodness man him appetite carriage. Any widen see gay forth alone fruit bed.", "aol laosstrhdtynll domrrod ytd..  eh sgrhe k o arm.eoa  t CrnnlwyusdrsiiPaAheoaca iitbt nimwdrrnoyl en o.r wylbteborudhndg eoxReiwwahtfesgwue.ldgnYl  tayesymatrroesh myeeohstmrnevd  rMi tiie  eaarrae  d rhytrmlhaneewpit .top knrS r ip uw elahee.egsuyhn nl  mrnitathk m      ioet mGaiieo  nheipgohtnmeoysc shli  Vitri dt u u.stgoagaae mrtbecnsaosabru igi aubnou so neu u n e els.eomaefl.rl symaCip tpia owt ydfewosememes tbl m ec  w"),
        ("Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity cheerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. Taken now you him trees tears any. Her object giving end sister except oppose.", "egtaeeCy cotntyaew ixg ltsor r   er  i s  ee ct dn pnd tltyrmpPy.i rogirh c fdeanrmod aa  a  enesai strurie h  ienkaaemw wvr mi irusnlriuhnnr rwnlceieonurynrgtunaiyddnrt wiSpeue ifourpsscsupaye L  nsm saestnol nbi.Ceeds i ugdrsi fgcmdpoorr zstrail eg.nrhle hruhe t ttpoygvotr keseseooedemavxy cotdin  yPntndsidepdsnejocuiod oteese oetyoieucicmlaetcsoi   n.i ieecm hraien sTe   iiscvnreeGlsiyrfidml.Haonae.dsiiaeeg w. ye.eeoen n iugnptrrbsveomnrhectr odmocn y. ecspetluiaa"),
        ("On then sake home is am leaf. Of suspicion do departure at extremely he believing. Do know said mind do rent they oh hope of. General enquire picture letters garrets on offices of no on. Say one hearing between excited evening all inhabit thought you. Style begin mr heard by in music tried do. To unreserved projection no introduced invitation.", "o rat o   itutraetdqe i iht  oyif u gonOfrtednt trii ielppeatbatiG nnpnbyaS tn ee  avtgunthsse. wbeiehhrleln .jru c eevoree tpelgdaioaiin n .neert  biie ssfdne niaa bdhcn ioy irne sdegoeor ogeodiiodexkdceg.unveetchmtfupxsfnsmr  aafseo.einyDnenemtm.yilrhem ncason wver  nohrki .t  So eeoedcrel on theTha mheuions o  ye  tuOudl  ooenci lr oor  rd"),
    ]
    EXP_OUTPUTS = [
        True, 
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(*test_input)
        assert isinstance(func_output, bool), "Function did not return a bool"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')