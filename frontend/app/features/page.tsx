export default function FeaturesPage() {
    const features = [
        {
            title: 'AI-Powered Search',
            description: 'Natural language understanding that comprehends your needs and finds relevant schemes instantly.',
            icon: '🤖',
            color: 'from-cyan-400 to-blue-400'
        },
        {
            title: 'Multi-Language Support',
            description: 'Access information in your preferred language - English, Hindi, and more regional languages.',
            icon: '🌍',
            color: 'from-purple-400 to-pink-400'
        },
        {
            title: 'Smart Recommendations',
            description: 'Get personalized suggestions based on your profile, location, and specific circumstances.',
            icon: '✨',
            color: 'from-green-400 to-cyan-400'
        },
        {
            title: 'Government & Banking Schemes',
            description: 'Discover both government welfare programs and linked banking products in one platform.',
            icon: '🏛️',
            color: 'from-orange-400 to-red-400'
        },
        {
            title: 'Real-Time Updates',
            description: 'Stay informed about new schemes, policy changes, and application deadlines.',
            icon: '⚡',
            color: 'from-yellow-400 to-orange-400'
        },
        {
            title: 'Privacy Protected',
            description: 'Your personal information is secure. We prioritize data privacy and user confidentiality.',
            icon: '🔒',
            color: 'from-indigo-400 to-purple-400'
        },
        {
            title: 'Interactive Chat',
            description: 'Ask questions and get detailed information about schemes through our AI assistant.',
            icon: '💬',
            color: 'from-pink-400 to-rose-400'
        },
        {
            title: 'Eligibility Checker',
            description: 'Quickly determine if you qualify for specific schemes before applying.',
            icon: '✅',
            color: 'from-teal-400 to-green-400'
        },
        {
            title: 'Application Guidance',
            description: 'Step-by-step assistance to help you complete applications successfully.',
            icon: '📝',
            color: 'from-blue-400 to-indigo-400'
        }
    ];

    return (
        <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white">
            <div className="max-w-7xl mx-auto px-4 py-16">
                <div className="text-center mb-16">
                    <h1 className="text-5xl md:text-6xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400">
                        Platform Features
                    </h1>
                    <p className="text-xl text-gray-300 max-w-3xl mx-auto">
                        Discover how SchemeSahayak empowers you to find and access government schemes with cutting-edge AI technology
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {features.map((feature, index) => (
                        <div
                            key={index}
                            className="bg-white/5 backdrop-blur-lg rounded-xl p-6 border border-white/10 hover:bg-white/10 transition-all duration-300 hover:scale-105 hover:shadow-2xl"
                        >
                            <div className="text-5xl mb-4">{feature.icon}</div>
                            <h3 className={`text-2xl font-bold mb-3 bg-clip-text text-transparent bg-gradient-to-r ${feature.color}`}>
                                {feature.title}
                            </h3>
                            <p className="text-gray-400 leading-relaxed">
                                {feature.description}
                            </p>
                        </div>
                    ))}
                </div>

                <div className="mt-16 bg-gradient-to-r from-cyan-500/10 to-purple-500/10 backdrop-blur-lg rounded-xl p-8 border border-cyan-500/20">
                    <h2 className="text-3xl font-bold text-center mb-4 text-cyan-300">
                        Ready to Get Started?
                    </h2>
                    <p className="text-center text-gray-300 text-lg mb-6">
                        Experience the power of AI-driven scheme discovery today
                    </p>
                    <div className="text-center">
                        <a
                            href="/"
                            className="inline-block px-8 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-bold rounded-lg transition-all duration-300 shadow-lg hover:shadow-cyan-500/50"
                        >
                            Start Searching
                        </a>
                    </div>
                </div>
            </div>
        </div>
    );
}
