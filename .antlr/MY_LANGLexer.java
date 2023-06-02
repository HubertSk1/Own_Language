// Generated from c:\Users\Dawid\Desktop\ProjektJFIK\Own_Language\MY_LANG.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MY_LANGLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, PRINT=4, READ=5, TO_DOUBLE=6, TO_FLOAT=7, INT=8, 
		DOUBLE=9, FLOAT=10, MUL=11, DIV=12, ADD=13, SUB=14, SET=15, EOE=16, ID=17, 
		LEFT_P=18, RIGHT_P=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "PRINT", "READ", "TO_DOUBLE", "TO_FLOAT", "INT", 
			"DOUBLE", "FLOAT", "MUL", "DIV", "ADD", "SUB", "SET", "EOE", "ID", "LEFT_P", 
			"RIGHT_P", "WS"
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


	public MY_LANGLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MY_LANG.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u0095\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\5\tQ\n\t\3\t\6\tT\n\t\r\t"+
		"\16\tU\3\n\5\nY\n\n\3\n\6\n\\\n\n\r\n\16\n]\3\n\3\n\7\nb\n\n\f\n\16\n"+
		"e\13\n\3\13\5\13h\n\13\3\13\6\13k\n\13\r\13\16\13l\3\13\3\13\7\13q\n\13"+
		"\f\13\16\13t\13\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\21\3\21\3\22\3\22\7\22\u0086\n\22\f\22\16\22\u0089\13\22\3\23"+
		"\3\23\3\24\3\24\3\25\6\25\u0090\n\25\r\25\16\25\u0091\3\25\3\25\2\2\26"+
		"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20"+
		"\37\21!\22#\23%\24\'\25)\26\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5"+
		"\2\13\f\17\17\"\"\2\u009e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2"+
		"\2\2\5-\3\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\67\3\2\2\2\r<\3\2\2\2\17F\3"+
		"\2\2\2\21P\3\2\2\2\23X\3\2\2\2\25g\3\2\2\2\27w\3\2\2\2\31y\3\2\2\2\33"+
		"{\3\2\2\2\35}\3\2\2\2\37\177\3\2\2\2!\u0081\3\2\2\2#\u0083\3\2\2\2%\u008a"+
		"\3\2\2\2\'\u008c\3\2\2\2)\u008f\3\2\2\2+,\7]\2\2,\4\3\2\2\2-.\7.\2\2."+
		"\6\3\2\2\2/\60\7_\2\2\60\b\3\2\2\2\61\62\7R\2\2\62\63\7T\2\2\63\64\7K"+
		"\2\2\64\65\7P\2\2\65\66\7V\2\2\66\n\3\2\2\2\678\7T\2\289\7G\2\29:\7C\2"+
		"\2:;\7F\2\2;\f\3\2\2\2<=\7V\2\2=>\7Q\2\2>?\7a\2\2?@\7F\2\2@A\7Q\2\2AB"+
		"\7W\2\2BC\7D\2\2CD\7N\2\2DE\7G\2\2E\16\3\2\2\2FG\7V\2\2GH\7Q\2\2HI\7a"+
		"\2\2IJ\7H\2\2JK\7N\2\2KL\7Q\2\2LM\7C\2\2MN\7V\2\2N\20\3\2\2\2OQ\7/\2\2"+
		"PO\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RT\t\2\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2"+
		"UV\3\2\2\2V\22\3\2\2\2WY\7/\2\2XW\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z\\\t\2\2"+
		"\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_c\7\60\2\2`b\t\2"+
		"\2\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\24\3\2\2\2ec\3\2\2\2fh\7"+
		"/\2\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\t\2\2\2ji\3\2\2\2kl\3\2\2\2lj\3"+
		"\2\2\2lm\3\2\2\2mn\3\2\2\2nr\7\60\2\2oq\t\2\2\2po\3\2\2\2qt\3\2\2\2rp"+
		"\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7H\2\2v\26\3\2\2\2wx\7,\2\2x"+
		"\30\3\2\2\2yz\7\61\2\2z\32\3\2\2\2{|\7-\2\2|\34\3\2\2\2}~\7/\2\2~\36\3"+
		"\2\2\2\177\u0080\7?\2\2\u0080 \3\2\2\2\u0081\u0082\7=\2\2\u0082\"\3\2"+
		"\2\2\u0083\u0087\t\3\2\2\u0084\u0086\t\4\2\2\u0085\u0084\3\2\2\2\u0086"+
		"\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088$\3\2\2\2"+
		"\u0089\u0087\3\2\2\2\u008a\u008b\7*\2\2\u008b&\3\2\2\2\u008c\u008d\7+"+
		"\2\2\u008d(\3\2\2\2\u008e\u0090\t\5\2\2\u008f\u008e\3\2\2\2\u0090\u0091"+
		"\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093"+
		"\u0094\b\25\2\2\u0094*\3\2\2\2\r\2PUX]cglr\u0087\u0091\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}