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
		INT_TYPE=1, REAL_TYPE=2, DEF=3, BEGIN=4, RETURN=5, PRINT=6, READ=7, INT=8, 
		REAL=9, MUL=10, DIV=11, ADD=12, SUB=13, SET=14, EOE=15, COMA=16, ID=17, 
		LEFT_P=18, RIGHT_P=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"INT_TYPE", "REAL_TYPE", "DEF", "BEGIN", "RETURN", "PRINT", "READ", "INT", 
			"REAL", "MUL", "DIV", "ADD", "SUB", "SET", "EOE", "COMA", "ID", "LEFT_P", 
			"RIGHT_P", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u008a\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3"+
		"\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\5\tU\n\t"+
		"\3\t\6\tX\n\t\r\t\16\tY\3\n\5\n]\n\n\3\n\6\n`\n\n\r\n\16\na\3\n\3\n\7"+
		"\nf\n\n\f\n\16\ni\13\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3"+
		"\20\3\20\3\21\3\21\3\22\3\22\7\22{\n\22\f\22\16\22~\13\22\3\23\3\23\3"+
		"\24\3\24\3\25\6\25\u0085\n\25\r\25\16\25\u0086\3\25\3\25\2\2\26\3\3\5"+
		"\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21"+
		"!\22#\23%\24\'\25)\26\3\2\6\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17"+
		"\17\"\"\2\u0090\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5/\3\2"+
		"\2\2\7\64\3\2\2\2\t;\3\2\2\2\13A\3\2\2\2\rH\3\2\2\2\17N\3\2\2\2\21T\3"+
		"\2\2\2\23\\\3\2\2\2\25j\3\2\2\2\27l\3\2\2\2\31n\3\2\2\2\33p\3\2\2\2\35"+
		"r\3\2\2\2\37t\3\2\2\2!v\3\2\2\2#x\3\2\2\2%\177\3\2\2\2\'\u0081\3\2\2\2"+
		")\u0084\3\2\2\2+,\7K\2\2,-\7P\2\2-.\7V\2\2.\4\3\2\2\2/\60\7T\2\2\60\61"+
		"\7G\2\2\61\62\7C\2\2\62\63\7N\2\2\63\6\3\2\2\2\64\65\7F\2\2\65\66\7G\2"+
		"\2\66\67\7H\2\2\678\7K\2\289\7P\2\29:\7G\2\2:\b\3\2\2\2;<\7D\2\2<=\7G"+
		"\2\2=>\7I\2\2>?\7K\2\2?@\7P\2\2@\n\3\2\2\2AB\7T\2\2BC\7G\2\2CD\7V\2\2"+
		"DE\7W\2\2EF\7T\2\2FG\7P\2\2G\f\3\2\2\2HI\7R\2\2IJ\7T\2\2JK\7K\2\2KL\7"+
		"P\2\2LM\7V\2\2M\16\3\2\2\2NO\7T\2\2OP\7G\2\2PQ\7C\2\2QR\7F\2\2R\20\3\2"+
		"\2\2SU\7/\2\2TS\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\t\2\2\2WV\3\2\2\2XY\3\2"+
		"\2\2YW\3\2\2\2YZ\3\2\2\2Z\22\3\2\2\2[]\7/\2\2\\[\3\2\2\2\\]\3\2\2\2]_"+
		"\3\2\2\2^`\t\2\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2\2c"+
		"g\7\60\2\2df\t\2\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\24\3\2\2"+
		"\2ig\3\2\2\2jk\7,\2\2k\26\3\2\2\2lm\7\61\2\2m\30\3\2\2\2no\7-\2\2o\32"+
		"\3\2\2\2pq\7/\2\2q\34\3\2\2\2rs\7?\2\2s\36\3\2\2\2tu\7=\2\2u \3\2\2\2"+
		"vw\7.\2\2w\"\3\2\2\2x|\t\3\2\2y{\t\4\2\2zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2"+
		"|}\3\2\2\2}$\3\2\2\2~|\3\2\2\2\177\u0080\7*\2\2\u0080&\3\2\2\2\u0081\u0082"+
		"\7+\2\2\u0082(\3\2\2\2\u0083\u0085\t\5\2\2\u0084\u0083\3\2\2\2\u0085\u0086"+
		"\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088"+
		"\u0089\b\25\2\2\u0089*\3\2\2\2\n\2TY\\ag|\u0086\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}