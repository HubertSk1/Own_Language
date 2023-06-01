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
		T__0=1, T__1=2, T__2=3, PRINT=4, READ=5, INT=6, DOUBLE=7, FLOAT=8, MUL=9, 
		DIV=10, ADD=11, SUB=12, SET=13, EOE=14, ID=15, LEFT_P=16, RIGHT_P=17, 
		WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "PRINT", "READ", "INT", "DOUBLE", "FLOAT", "MUL", 
			"DIV", "ADD", "SUB", "SET", "EOE", "ID", "LEFT_P", "RIGHT_P", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'['", "','", "']'", "'PRINT'", "'READ'", null, null, null, "'*'", 
			"'/'", "'+'", "'-'", "'='", "';'", null, "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "PRINT", "READ", "INT", "DOUBLE", "FLOAT", "MUL", 
			"DIV", "ADD", "SUB", "SET", "EOE", "ID", "LEFT_P", "RIGHT_P", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24u\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6"+
		"\3\6\3\6\3\7\6\7:\n\7\r\7\16\7;\3\b\6\b?\n\b\r\b\16\b@\3\b\3\b\7\bE\n"+
		"\b\f\b\16\bH\13\b\3\t\6\tK\n\t\r\t\16\tL\3\t\3\t\7\tQ\n\t\f\t\16\tT\13"+
		"\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\7\20f\n\20\f\20\16\20i\13\20\3\21\3\21\3\22\3\22\3\23\6\23p\n\23"+
		"\r\23\16\23q\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13"+
		"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\6\3\2\62;\5\2C\\aa"+
		"c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2{\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3"+
		"\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2"+
		"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)"+
		"\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13\63\3\2\2\2\r9\3\2\2\2\17>\3\2\2\2\21"+
		"J\3\2\2\2\23W\3\2\2\2\25Y\3\2\2\2\27[\3\2\2\2\31]\3\2\2\2\33_\3\2\2\2"+
		"\35a\3\2\2\2\37c\3\2\2\2!j\3\2\2\2#l\3\2\2\2%o\3\2\2\2\'(\7]\2\2(\4\3"+
		"\2\2\2)*\7.\2\2*\6\3\2\2\2+,\7_\2\2,\b\3\2\2\2-.\7R\2\2./\7T\2\2/\60\7"+
		"K\2\2\60\61\7P\2\2\61\62\7V\2\2\62\n\3\2\2\2\63\64\7T\2\2\64\65\7G\2\2"+
		"\65\66\7C\2\2\66\67\7F\2\2\67\f\3\2\2\28:\t\2\2\298\3\2\2\2:;\3\2\2\2"+
		";9\3\2\2\2;<\3\2\2\2<\16\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2"+
		"\2@A\3\2\2\2AB\3\2\2\2BF\7\60\2\2CE\t\2\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2"+
		"\2\2FG\3\2\2\2G\20\3\2\2\2HF\3\2\2\2IK\t\2\2\2JI\3\2\2\2KL\3\2\2\2LJ\3"+
		"\2\2\2LM\3\2\2\2MN\3\2\2\2NR\7\60\2\2OQ\t\2\2\2PO\3\2\2\2QT\3\2\2\2RP"+
		"\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7H\2\2V\22\3\2\2\2WX\7,\2\2X"+
		"\24\3\2\2\2YZ\7\61\2\2Z\26\3\2\2\2[\\\7-\2\2\\\30\3\2\2\2]^\7/\2\2^\32"+
		"\3\2\2\2_`\7?\2\2`\34\3\2\2\2ab\7=\2\2b\36\3\2\2\2cg\t\3\2\2df\t\4\2\2"+
		"ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h \3\2\2\2ig\3\2\2\2jk\7*\2\2"+
		"k\"\3\2\2\2lm\7+\2\2m$\3\2\2\2np\t\5\2\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2"+
		"qr\3\2\2\2rs\3\2\2\2st\b\23\2\2t&\3\2\2\2\n\2;@FLRgq\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}