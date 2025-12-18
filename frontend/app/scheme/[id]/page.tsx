'use client';

import { useEffect, useState, FormEvent } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { API_BASE_URL } from '../../utils/api';
import { useLanguage } from '../../context/LanguageContext';
import LanguageSwitch from '../../components/LanguageSwitch';

export default function SchemeDetails() {
    const params = useParams();
    const id = params.id as string;
    const [scheme, setScheme] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const { t } = useLanguage();

    // Chat State
    const [question, setQuestion] = useState('');
    const [chatHistory, setChatHistory] = useState<{ role: 'user' | 'ai', content: string }[]>([]);
    const [chatLoading, setChatLoading] = useState(false);

    useEffect(() => {
        if (id) {
            fetch(`${API_BASE_URL}/citizen/scheme/${id}`)
                .then(res => {
                    if (!res.ok) throw new Error('Scheme not found');
                    return res.json();
                })
                .then(data => setScheme(data))
                .catch(err => setError(err.message))
                .finally(() => setLoading(false));
        }
    }, [id]);

    const handleChat = async (e: FormEvent) => {
        e.preventDefault();
        if (!question.trim()) return;

        const userQs = question;
        setQuestion('');
        setChatHistory(prev => [...prev, { role: 'user', content: userQs }]);
        setChatLoading(true);

        try {
            const res = await fetch(`${API_BASE_URL}/citizen/scheme/${id}/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: userQs })
            });
            const data = await res.json();
            setChatHistory(prev => [...prev, { role: 'ai', content: data.answer }]);
        } catch (err) {
            setChatHistory(prev => [...prev, { role: 'ai', content: "Error contacting AI service." }]);
        } finally {
            setChatLoading(false);
        }
    };

    if (loading) return <div className="min-h-screen bg-gray-900 text-white p-10">Loading scheme details...</div>;
    if (error) return <div className="min-h-screen bg-gray-900 text-white p-10">Error: {error}</div>;
    if (!scheme) return null;

    const meta = scheme.metadata || {};

    return (
        <div className="min-h-screen bg-gray-900 text-white p-4 sm:p-6 lg:p-8">
            <LanguageSwitch />
            <div className="max-w-4xl mx-auto">
                {/* Header / Nav */}
                <div className="mb-6">
                    <Link href="/results?q=home%20loans" className="text-cyan-400 hover:text-cyan-300 transition-colors">
                        ← Back to Search
                    </Link>
                </div>

                {/* Main Content */}
                <div className="bg-gray-800 rounded-2xl p-6 sm:p-8 border border-gray-700 shadow-2xl mb-8">
                    <h1 className="text-2xl sm:text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-400 mb-4 break-words">
                        {meta.title || 'Unknown Scheme'}
                    </h1>

                    <div className="flex flex-wrap gap-2 mb-6">
                        {meta.ministry && <span className="bg-blue-900 text-blue-200 px-3 py-1 rounded-full text-xs sm:text-sm font-semibold">{meta.ministry}</span>}
                        {meta.bank && <span className="bg-blue-900 text-blue-200 px-3 py-1 rounded-full text-xs sm:text-sm font-semibold">{meta.bank}</span>}
                        {meta.category && <span className="bg-purple-900 text-purple-200 px-3 py-1 rounded-full text-xs sm:text-sm font-semibold">{meta.category}</span>}
                    </div>

                    <div className="prose prose-invert max-w-none">
                        <p className="text-base sm:text-lg text-gray-300 leading-relaxed mb-6">{meta.description}</p>

                        {meta.benefits && (
                            <div className="bg-gray-700/50 p-4 rounded-xl mb-4 border-l-4 border-green-500">
                                <h3 className="text-green-400 font-bold mb-1">Key Benefits</h3>
                                <p className="text-sm sm:text-base">{meta.benefits}</p>
                            </div>
                        )}

                        {meta.regulatory_notes && (
                            <div className="bg-gray-700/50 p-4 rounded-xl mb-4 border-l-4 border-yellow-500">
                                <h3 className="text-yellow-400 font-bold mb-1">Regulatory Notes</h3>
                                <p className="text-sm sm:text-base">{meta.regulatory_notes}</p>
                            </div>
                        )}

                        {/* External Link (if any) */}
                        {(meta.link || meta.read_more_link) && (
                            <div className="mt-6">
                                <a
                                    href={meta.link || meta.read_more_link}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="inline-flex items-center gap-2 bg-cyan-600 hover:bg-cyan-500 text-white px-5 py-2.5 rounded-lg font-semibold transition-colors text-sm sm:text-base"
                                >
                                    Visit Official Website ↗
                                </a>
                            </div>
                        )}
                    </div>
                </div>

                {/* AI Chat Section */}
                <div className="bg-gray-800 rounded-2xl p-6 sm:p-8 border border-gray-700 shadow-2xl">
                    <h2 className="text-xl sm:text-2xl font-bold text-white mb-4 flex items-center gap-2 flex-wrap">
                        🤖 Chat with Scheme Assistant
                        <span className="text-xs bg-purple-600 px-2 py-0.5 rounded text-white font-normal uppercase">Beta</span>
                    </h2>
                    <p className="text-gray-400 mb-6 text-sm sm:text-base">Have questions about eligibility, interest rates, or documents? Ask our AI!</p>

                    <div className="space-y-4 mb-6 max-h-[400px] overflow-y-auto custom-scrollbar">
                        {chatHistory.length === 0 && (
                            <div className="text-center text-gray-500 italic py-8 text-sm sm:text-base">
                                No messages yet. Try asking: "Who is eligible for this scheme?"
                            </div>
                        )}
                        {chatHistory.map((msg, i) => (
                            <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                                <div className={`max-w-[85%] sm:max-w-[80%] rounded-2xl px-4 py-2 sm:px-5 sm:py-3 text-sm sm:text-base ${msg.role === 'user'
                                    ? 'bg-cyan-700 text-white rounded-tr-none'
                                    : 'bg-gray-700 text-gray-200 rounded-tl-none'
                                    }`}>
                                    {msg.content}
                                </div>
                            </div>
                        ))}
                        {chatLoading && (
                            <div className="flex justify-start">
                                <div className="bg-gray-700 text-gray-200 rounded-2xl rounded-tl-none px-5 py-3 animate-pulse text-sm sm:text-base">
                                    AI is typing...
                                </div>
                            </div>
                        )}
                    </div>

                    <form onSubmit={handleChat} className="flex flex-col sm:flex-row gap-3">
                        <input
                            type="text"
                            className="flex-1 bg-gray-900 border border-gray-600 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500 transition-colors text-sm sm:text-base"
                            placeholder="Type your question here..."
                            value={question}
                            onChange={(e) => setQuestion(e.target.value)}
                        />
                        <button
                            type="submit"
                            disabled={chatLoading || !question.trim()}
                            className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white px-6 py-3 rounded-xl font-bold disabled:opacity-50 transition-all shadow-lg text-sm sm:text-base whitespace-nowrap"
                        >
                            Send
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}
