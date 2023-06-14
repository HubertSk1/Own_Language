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
		INT_TYPE=1, REAL_TYPE=2, DEF=3, BEGIN=4, RETURN=5, PRINT=6, READ=7, INT=8, 
		REAL=9, MUL=10, DIV=11, ADD=12, SUB=13, SET=14, EOE=15, COMA=16, ID=17, 
		LEFT_P=18, RIGHT_P=19, WS=20;
	public static final int
		RULE_prog = 0, RULE_statements = 1, RULE_statement = 2, RULE_assign = 3, 
		RULE_print = 4, RULE_read = 5, RULE_arg_list = 6, RULE_function_header = 7, 
		RULE_define = 8, RULE_end_function = 9, RULE_typ = 10, RULE_expr = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statements", "statement", "assign", "print", "read", "arg_list", 
			"function_header", "define", "end_function", "typ", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'INT'", "'REAL'", "'DEFINE'", "'BEGIN'", "'RETURN'", "'PRINT'", 
			"'READ'", null, null, "'*'", "'/'", "'+'", "'-'", "'='", "';'", "','", 
			null, "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INT_TYPE", "REAL_TYPE", "DEF", "BEGIN", "RETURN", "PRINT", "READ", 
			"INT", "REAL", "MUL", "DIV", "ADD", "SUB", "SET", "EOE", "COMA", "ID", 
			"LEFT_P", "RIGHT_P", "WS"
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
			setState(24);
			statements();
			setState(25);
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
		public List<DefineContext> define() {
			return getRuleContexts(DefineContext.class);
		}
		public DefineContext define(int i) {
			return getRuleContext(DefineContext.class,i);
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
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DEF) | (1L << PRINT) | (1L << READ) | (1L << ID))) != 0)) {
				{
				setState(29);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRINT:
				case READ:
				case ID:
					{
					setState(27);
					statement();
					}
					break;
				case DEF:
					{
					setState(28);
					define();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(33);
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
			setState(37);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				{
				setState(34);
				print();
				}
				break;
			case ID:
				{
				setState(35);
				assign();
				}
				break;
			case READ:
				{
				setState(36);
				read();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(39);
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
			setState(41);
			match(ID);
			setState(42);
			match(SET);
			setState(43);
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
			setState(45);
			match(PRINT);
			setState(46);
			match(LEFT_P);
			setState(47);
			expr(0);
			setState(48);
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
			setState(50);
			match(READ);
			setState(51);
			match(LEFT_P);
			setState(52);
			match(ID);
			setState(53);
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

	public static class Arg_listContext extends ParserRuleContext {
		public List<TypContext> typ() {
			return getRuleContexts(TypContext.class);
		}
		public TypContext typ(int i) {
			return getRuleContext(TypContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(MY_LANGParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MY_LANGParser.ID, i);
		}
		public TerminalNode COMA() { return getToken(MY_LANGParser.COMA, 0); }
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_arg_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			typ();
			setState(56);
			match(ID);
			{
			setState(57);
			match(COMA);
			setState(58);
			typ();
			setState(59);
			match(ID);
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

	public static class Function_headerContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(MY_LANGParser.DEF, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
		public Function_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_header; }
	}

	public final Function_headerContext function_header() throws RecognitionException {
		Function_headerContext _localctx = new Function_headerContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function_header);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(DEF);
			setState(62);
			match(ID);
			setState(63);
			match(LEFT_P);
			setState(64);
			arg_list();
			setState(65);
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

	public static class DefineContext extends ParserRuleContext {
		public Function_headerContext function_header() {
			return getRuleContext(Function_headerContext.class,0);
		}
		public TerminalNode BEGIN() { return getToken(MY_LANGParser.BEGIN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public End_functionContext end_function() {
			return getRuleContext(End_functionContext.class,0);
		}
		public DefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define; }
	}

	public final DefineContext define() throws RecognitionException {
		DefineContext _localctx = new DefineContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_define);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			function_header();
			setState(68);
			match(BEGIN);
			setState(69);
			statement();
			setState(70);
			end_function();
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

	public static class End_functionContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(MY_LANGParser.RETURN, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public End_functionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_function; }
	}

	public final End_functionContext end_function() throws RecognitionException {
		End_functionContext _localctx = new End_functionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_end_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(RETURN);
			setState(73);
			match(ID);
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

	public static class TypContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(MY_LANGParser.INT_TYPE, 0); }
		public TerminalNode REAL_TYPE() { return getToken(MY_LANGParser.REAL_TYPE, 0); }
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_typ);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_la = _input.LA(1);
			if ( !(_la==INT_TYPE || _la==REAL_TYPE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MY_LANGParser.INT, 0); }
		public TerminalNode REAL() { return getToken(MY_LANGParser.REAL, 0); }
		public TerminalNode ID() { return getToken(MY_LANGParser.ID, 0); }
		public TerminalNode LEFT_P() { return getToken(MY_LANGParser.LEFT_P, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RIGHT_P() { return getToken(MY_LANGParser.RIGHT_P, 0); }
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
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(78);
				match(INT);
				}
				break;
			case REAL:
				{
				setState(79);
				match(REAL);
				}
				break;
			case ID:
				{
				setState(80);
				match(ID);
				}
				break;
			case LEFT_P:
				{
				setState(81);
				match(LEFT_P);
				setState(82);
				expr(0);
				setState(83);
				match(RIGHT_P);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(101);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(99);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(87);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(88);
						match(MUL);
						setState(89);
						expr(9);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(90);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(91);
						match(DIV);
						setState(92);
						expr(8);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(93);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(94);
						match(ADD);
						setState(95);
						expr(7);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(96);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(97);
						match(SUB);
						setState(98);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(103);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26k\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\3\2\3\2\3\2\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4\3\4"+
		"\5\4(\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\rX\n\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\rf\n\r\f\r\16\ri\13\r\3"+
		"\r\2\3\30\16\2\4\6\b\n\f\16\20\22\24\26\30\2\3\3\2\3\4\2i\2\32\3\2\2\2"+
		"\4!\3\2\2\2\6\'\3\2\2\2\b+\3\2\2\2\n/\3\2\2\2\f\64\3\2\2\2\169\3\2\2\2"+
		"\20?\3\2\2\2\22E\3\2\2\2\24J\3\2\2\2\26M\3\2\2\2\30W\3\2\2\2\32\33\5\4"+
		"\3\2\33\34\7\2\2\3\34\3\3\2\2\2\35 \5\6\4\2\36 \5\22\n\2\37\35\3\2\2\2"+
		"\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\5\3\2\2\2#!\3\2\2\2"+
		"$(\5\n\6\2%(\5\b\5\2&(\5\f\7\2\'$\3\2\2\2\'%\3\2\2\2\'&\3\2\2\2()\3\2"+
		"\2\2)*\7\21\2\2*\7\3\2\2\2+,\7\23\2\2,-\7\20\2\2-.\5\30\r\2.\t\3\2\2\2"+
		"/\60\7\b\2\2\60\61\7\24\2\2\61\62\5\30\r\2\62\63\7\25\2\2\63\13\3\2\2"+
		"\2\64\65\7\t\2\2\65\66\7\24\2\2\66\67\7\23\2\2\678\7\25\2\28\r\3\2\2\2"+
		"9:\5\26\f\2:;\7\23\2\2;<\7\22\2\2<=\5\26\f\2=>\7\23\2\2>\17\3\2\2\2?@"+
		"\7\5\2\2@A\7\23\2\2AB\7\24\2\2BC\5\16\b\2CD\7\25\2\2D\21\3\2\2\2EF\5\20"+
		"\t\2FG\7\6\2\2GH\5\6\4\2HI\5\24\13\2I\23\3\2\2\2JK\7\7\2\2KL\7\23\2\2"+
		"L\25\3\2\2\2MN\t\2\2\2N\27\3\2\2\2OP\b\r\1\2PX\7\n\2\2QX\7\13\2\2RX\7"+
		"\23\2\2ST\7\24\2\2TU\5\30\r\2UV\7\25\2\2VX\3\2\2\2WO\3\2\2\2WQ\3\2\2\2"+
		"WR\3\2\2\2WS\3\2\2\2Xg\3\2\2\2YZ\f\n\2\2Z[\7\f\2\2[f\5\30\r\13\\]\f\t"+
		"\2\2]^\7\r\2\2^f\5\30\r\n_`\f\b\2\2`a\7\16\2\2af\5\30\r\tbc\f\7\2\2cd"+
		"\7\17\2\2df\5\30\r\beY\3\2\2\2e\\\3\2\2\2e_\3\2\2\2eb\3\2\2\2fi\3\2\2"+
		"\2ge\3\2\2\2gh\3\2\2\2h\31\3\2\2\2ig\3\2\2\2\b\37!\'Weg";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}