import sys, io, contextlib
sys.path.insert(0, 'assets')
from python_parser import PythonParser

CASI = {
    "Empty Test": ("tests_estensione/caso_empty.py",
        {("test_metodo_vuoto", 31), ("test_vuoto_pass", 3), ("test_vuoto_ellipsis", 6),
         ("test_vuoto_doc_commento", 9), ("test_pass_commento_inline", 14)}),
    "Redundant Assertion": ("tests_estensione/caso_redundant.py",
        {("test_in_classe", 41), ("test_assert_true", 4), ("test_assert_uno", 7),
         ("test_stesso_valore", 10), ("test_letterali", 13),
         ("test_due_righe_su_tre", 17), ("test_due_righe_su_tre", 19),
         ("test_commento_inline", 33)}),
    "Ignored Test": ("tests_estensione/caso_ignored.py",
        {("test_unittest_skip", 37), ("test_in_classe", 41), ("test_skip", 4),
         ("test_skip_con_motivo", 8), ("test_skipif", 12), ("test_due_decorator", 17)}),
}

tutto_ok = True
for smell, (percorso, atteso) in CASI.items():
    with contextlib.redirect_stdout(io.StringIO()):
        logs = PythonParser(percorso).start()
    trovato = {(l.method_name, l.lines[0]) for l in logs if l.test_smell_type == smell}
    ok = (trovato == atteso)
    tutto_ok = tutto_ok and ok
    print(smell, "->", "OK" if ok else "ERRORE", "(attesi %d, trovati %d)" % (len(atteso), len(trovato)))
    if not ok:
        print("   mancanti:", sorted(atteso - trovato))
        print("   in piu:", sorted(trovato - atteso))
print("TUTTO OK" if tutto_ok else "CI SONO ERRORI")
