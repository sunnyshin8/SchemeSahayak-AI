export default function AboutPage() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white">
            <div className="max-w-6xl mx-auto px-4 py-16">
                <h1 className="text-5xl md:text-6xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400">
                    About SchemeSahayak
                </h1>

                <div className="space-y-8 text-gray-300">
                    <section className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                        <h2 className="text-3xl font-bold text-cyan-300 mb-4">Our Mission</h2>
                        <p className="text-lg leading-relaxed">
                            SchemeSahayak is an AI-powered government scheme intelligence platform designed to bridge the gap between citizens and the myriad of government schemes available. Our mission is to make government benefits accessible to everyone through intelligent search and personalized recommendations.
                        </p>
                    </section>

                    <section className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                        <h2 className="text-3xl font-bold text-purple-300 mb-4">What We Do</h2>
                        <p className="text-lg leading-relaxed mb-4">
                            We leverage advanced AI and natural language processing to understand your needs and match you with relevant government schemes and banking products. Whether you're looking for:
                        </p>
                        <ul className="list-disc list-inside space-y-2 text-lg ml-4">
                            <li>Farmer welfare schemes</li>
                            <li>Housing assistance programs</li>
                            <li>Health insurance benefits</li>
                            <li>Education scholarships</li>
                            <li>Banking credit facilities</li>
                        </ul>
                        <p className="text-lg leading-relaxed mt-4">
                            SchemeSahayak helps you discover opportunities you might not have known existed.
                        </p>
                    </section>

                    <section className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                        <h2 className="text-3xl font-bold text-pink-300 mb-4">Our Technology</h2>
                        <p className="text-lg leading-relaxed">
                            Built with cutting-edge AI technology and powered by CyborgDB for vector search, our platform provides accurate, context-aware results in multiple languages. We ensure your data privacy while delivering personalized recommendations that truly matter.
                        </p>
                    </section>

                    <section className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                        <h2 className="text-3xl font-bold text-cyan-300 mb-4">Our Vision</h2>
                        <p className="text-lg leading-relaxed">
                            We envision a future where every citizen can easily access the government benefits they deserve, without navigating complex bureaucracies or missing out due to lack of awareness. SchemeSahayak is your digital companion in this journey.
                        </p>
                    </section>
                </div>
            </div>
        </div>
    );
}
