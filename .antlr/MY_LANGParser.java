// Generated from c:\Users\Dawid\Desktop\ProjektJFIK\Own_Language\MY_LANG.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MY_LANGParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, PRINT=4, READ=5, TO_DOUBLE=6, TO_FLOAT=7, INT=8, 
		DOUBLE=9, FLOAT=10, MUL=11, DIV=12, ADD=13, SUB=14, SET=15, EOE=16, ID=17, 
		LEFT_P=18, RIGHT_P=19, WS=20;
	public static final int
		RULE_prog = 0, RULE_statements = 1, RULE_statement = 2, RULE_assign = 3, 
		RULE_print = 4, RULE_read = 5, RULE_to_double = 6, RULE_to_float = 7, 
		RULE_expr = 8, RULE_matrix = 9, RULE_row = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statements", "statement", "assign", "print", "read", "to_double", 
			"to_float", "expr", "matrix", "row"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'['", "','", "']'", "'PRINT'", "'READ'", "'TO_DOUBLE'", "'TO_FLOAT'", 
			null, null, null, "'*'", "'/'", "'+'", "'-'", "'='", "';'", null, "'('", 
			"')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "PRINT", "READ", "TO_DOUBLE", "TO_FLOAT", "INT", 
			"DOUBLE", "FLOAT", "MUL", "DIV", "ADD", "SUB", "SET", "EOE", "ID", "LEFT_P", 
			"RIGHT_P", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MY_LANG.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MY_LANGParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MY_LANGParser.EOF, 0); }
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			statements();
			setState(23);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementsContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << READ) | (1L << TO_DOUBLE) | (1L << TO_FLOAT) | (1L << ID))) != 0)) {
				{
				{
				setState(25);
				statement();
				}
				}
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public TerminalNode EOE() { return getToken(MY_LANGParser.EOE, 0); }
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public To_doubleContext to_double() {
			return getRuleContext(To_doubleContext.class,0);
		}
		public To_floatContext to_float() {
			return getRuleContext(To_floatContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				{
				setState(31);
				print();
				}
				break;
			case ID:
				{
				setState(32);
				assign();
				}
				break;
			case READ:
				{
				setState(33);
				read();
				}
				break;
			case TO_DOUBLE:
				{
				setState(34);
				to_double();
				}
				break;
			case TO_FLOAT:
				{
				setState(35);
				to_float();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(38);
			match(EOE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode SET() { return getToken(MY_LANGParser.SET, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(ID);
			setState(41);
			match(SET);
			setState(42);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(MY_LANGParser.PRINT, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(PRINT);
			setState(45);
			match(LEFT_P);
			setState(46);
			expr(0);
			setState(47);
			match(RIGHT_P);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(MY_LANGParser.READ, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(READ);
			setState(50);
			match(LEFT_P);
			setState(51);
			match(ID);
			setState(52);
			match(RIGHT_P);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class To_doubleContext extends ParserRuleContext {
		public TerminalNode TO_DOUBLE() { return getToken(MY_LANGParser.TO_DOUBLE, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public To_doubleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_to_double; }
	}

	public final To_doubleContext to_double() throws RecognitionException {
		To_doubleContext _localctx = new To_doubleContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_to_double);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(TO_DOUBLE);
			setState(55);
			match(LEFT_P);
			setState(56);
			match(ID);
			setState(57);
			match(RIGHT_P);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class To_floatContext extends ParserRuleContext {
		public TerminalNode TO_FLOAT() { return getToken(MY_LANGParser.TO_FLOAT, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public To_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_to_float; }
	}

	public final To_floatContext to_float() throws RecognitionException {
		To_floatContext _localctx = new To_floatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_to_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(TO_FLOAT);
			setState(60);
			match(LEFT_P);
			setState(61);
			match(ID);
			setState(62);
			match(RIGHT_P);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MY_LANGParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(MY_LANGParser.DOUBLE, 0); }
		public TerminalNode FLOAT() { return getToken(MY_LANGParser.FLOAT, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public MatrixContext matrix() {
			return getRuleContext(MatrixContext.class,0);
		}
		public TerminalNode MUL() { return getToken(MY_LANGParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(MY_LANGParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(MY_LANGParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(MY_LANGParser.SUB, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(65);
				match(INT);
				}
				break;
			case DOUBLE:
				{
				setState(66);
				match(DOUBLE);
				}
				break;
			case FLOAT:
				{
				setState(67);
				match(FLOAT);
				}
				break;
			case ID:
				{
				setState(68);
				match(ID);
				}
				break;
			case LEFT_P:
				{
				setState(69);
				match(LEFT_P);
				setState(70);
				expr(0);
				setState(71);
				match(RIGHT_P);
				}
				break;
			case T__0:
				{
				setState(73);
				matrix();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(90);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(88);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(76);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(77);
						match(MUL);
						setState(78);
						expr(11);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(79);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(80);
						match(DIV);
						setState(81);
						expr(10);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(82);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(83);
						match(ADD);
						setState(84);
						expr(9);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(85);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(86);
						match(SUB);
						setState(87);
						expr(8);
						}
						break;
					}
					} 
				}
				setState(92);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MatrixContext extends ParserRuleContext {
		public List<RowContext> row() {
			return getRuleContexts(RowContext.class);
		}
		public RowContext row(int i) {
			return getRuleContext(RowContext.class,i);
		}
		public MatrixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matrix; }
	}

	public final MatrixContext matrix() throws RecognitionException {
		MatrixContext _localctx = new MatrixContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_matrix);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(T__0);
			setState(94);
			row();
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(95);
				match(T__1);
				setState(96);
				row();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(102);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RowContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(MY_LANGParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(MY_LANGParser.INT, i);
		}
		public RowContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_row; }
	}

	public final RowContext row() throws RecognitionException {
		RowContext _localctx = new RowContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_row);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(T__0);
			setState(105);
			match(INT);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(106);
				match(T__1);
				setState(107);
				match(INT);
				}
				}
				setState(112);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(113);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26v\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\3\2\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\4\3\4\5"+
		"\4\'\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\5\nM\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\7\n[\n\n\f\n\16\n^\13\n\3\13\3\13\3\13\3\13\7\13d\n\13\f\13\16\13g\13"+
		"\13\3\13\3\13\3\f\3\f\3\f\3\f\7\fo\n\f\f\f\16\fr\13\f\3\f\3\f\3\f\2\3"+
		"\22\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2z\2\30\3\2\2\2\4\36\3\2\2\2\6&\3"+
		"\2\2\2\b*\3\2\2\2\n.\3\2\2\2\f\63\3\2\2\2\168\3\2\2\2\20=\3\2\2\2\22L"+
		"\3\2\2\2\24_\3\2\2\2\26j\3\2\2\2\30\31\5\4\3\2\31\32\7\2\2\3\32\3\3\2"+
		"\2\2\33\35\5\6\4\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2"+
		"\2\37\5\3\2\2\2 \36\3\2\2\2!\'\5\n\6\2\"\'\5\b\5\2#\'\5\f\7\2$\'\5\16"+
		"\b\2%\'\5\20\t\2&!\3\2\2\2&\"\3\2\2\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'"+
		"(\3\2\2\2()\7\22\2\2)\7\3\2\2\2*+\7\23\2\2+,\7\21\2\2,-\5\22\n\2-\t\3"+
		"\2\2\2./\7\6\2\2/\60\7\24\2\2\60\61\5\22\n\2\61\62\7\25\2\2\62\13\3\2"+
		"\2\2\63\64\7\7\2\2\64\65\7\24\2\2\65\66\7\23\2\2\66\67\7\25\2\2\67\r\3"+
		"\2\2\289\7\b\2\29:\7\24\2\2:;\7\23\2\2;<\7\25\2\2<\17\3\2\2\2=>\7\t\2"+
		"\2>?\7\24\2\2?@\7\23\2\2@A\7\25\2\2A\21\3\2\2\2BC\b\n\1\2CM\7\n\2\2DM"+
		"\7\13\2\2EM\7\f\2\2FM\7\23\2\2GH\7\24\2\2HI\5\22\n\2IJ\7\25\2\2JM\3\2"+
		"\2\2KM\5\24\13\2LB\3\2\2\2LD\3\2\2\2LE\3\2\2\2LF\3\2\2\2LG\3\2\2\2LK\3"+
		"\2\2\2M\\\3\2\2\2NO\f\f\2\2OP\7\r\2\2P[\5\22\n\rQR\f\13\2\2RS\7\16\2\2"+
		"S[\5\22\n\fTU\f\n\2\2UV\7\17\2\2V[\5\22\n\13WX\f\t\2\2XY\7\20\2\2Y[\5"+
		"\22\n\nZN\3\2\2\2ZQ\3\2\2\2ZT\3\2\2\2ZW\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\"+
		"]\3\2\2\2]\23\3\2\2\2^\\\3\2\2\2_`\7\3\2\2`e\5\26\f\2ab\7\4\2\2bd\5\26"+
		"\f\2ca\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7\5"+
		"\2\2i\25\3\2\2\2jk\7\3\2\2kp\7\n\2\2lm\7\4\2\2mo\7\n\2\2nl\3\2\2\2or\3"+
		"\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3\2\2\2rp\3\2\2\2st\7\5\2\2t\27\3\2\2\2\t"+
		"\36&LZ\\ep";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}