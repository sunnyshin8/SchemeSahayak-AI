'use client';

import { useState } from 'react';

export default function ContactPage() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        subject: '',
        message: ''
    });
    const [submitted, setSubmitted] = useState(false);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Here you would normally send the form data to your backend
        setSubmitted(true);
        setTimeout(() => {
            setSubmitted(false);
            setFormData({ name: '', email: '', subject: '', message: '' });
        }, 3000);
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white">
            <div className="max-w-5xl mx-auto px-4 py-16">
                <div className="text-center mb-12">
                    <h1 className="text-5xl md:text-6xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400">
                        Contact Us
                    </h1>
                    <p className="text-xl text-gray-300">
                        Have questions? We'd love to hear from you. Send us a message and we'll respond as soon as possible.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    {/* Contact Form */}
                    <div className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                        <h2 className="text-2xl font-bold text-cyan-300 mb-6">Send us a Message</h2>

                        {submitted && (
                            <div className="mb-6 p-4 bg-green-500/20 border border-green-500/50 rounded-lg text-green-300">
                                Thank you! Your message has been sent successfully.
                            </div>
                        )}

                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div>
                                <label htmlFor="name" className="block text-sm font-medium text-gray-300 mb-2">
                                    Name
                                </label>
                                <input
                                    type="text"
                                    id="name"
                                    name="name"
                                    value={formData.name}
                                    onChange={handleChange}
                                    required
                                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
                                    placeholder="Your name"
                                />
                            </div>

                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-300 mb-2">
                                    Email
                                </label>
                                <input
                                    type="email"
                                    id="email"
                                    name="email"
                                    value={formData.email}
                                    onChange={handleChange}
                                    required
                                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
                                    placeholder="your.email@example.com"
                                />
                            </div>

                            <div>
                                <label htmlFor="subject" className="block text-sm font-medium text-gray-300 mb-2">
                                    Subject
                                </label>
                                <input
                                    type="text"
                                    id="subject"
                                    name="subject"
                                    value={formData.subject}
                                    onChange={handleChange}
                                    required
                                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
                                    placeholder="What is this about?"
                                />
                            </div>

                            <div>
                                <label htmlFor="message" className="block text-sm font-medium text-gray-300 mb-2">
                                    Message
                                </label>
                                <textarea
                                    id="message"
                                    name="message"
                                    value={formData.message}
                                    onChange={handleChange}
                                    required
                                    rows={5}
                                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent resize-none"
                                    placeholder="Your message here..."
                                />
                            </div>

                            <button
                                type="submit"
                                className="w-full py-3 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-bold rounded-lg transition-all duration-300 shadow-lg hover:shadow-cyan-500/50"
                            >
                                Send Message
                            </button>
                        </form>
                    </div>

                    {/* Contact Information */}
                    <div className="space-y-6">
                        <div className="bg-white/5 backdrop-blur-lg rounded-xl p-8 border border-white/10">
                            <h2 className="text-2xl font-bold text-purple-300 mb-6">Get in Touch</h2>
                            <div className="space-y-4">
                                <div className="flex items-start space-x-4">
                                    <div className="text-2xl">📧</div>
                                    <div>
                                        <h3 className="font-semibold text-white mb-1">Email</h3>
                                        <p className="text-gray-400">support@schemesahayak.ai</p>
                                    </div>
                                </div>

                                <div className="flex items-start space-x-4">
                                    <div className="text-2xl">📱</div>
                                    <div>
                                        <h3 className="font-semibold text-white mb-1">Phone</h3>
                                        <p className="text-gray-400">+91 1800-XXX-XXXX</p>
                                    </div>
                                </div>

                                <div className="flex items-start space-x-4">
                                    <div className="text-2xl">🏢</div>
                                    <div>
                                        <h3 className="font-semibold text-white mb-1">Office</h3>
                                        <p className="text-gray-400">
                                            123 Innovation Street<br />
                                            Tech Hub, Mumbai 400001<br />
                                            India
                                        </p>
                                    </div>
                                </div>

                                <div className="flex items-start space-x-4">
                                    <div className="text-2xl">⏰</div>
                                    <div>
                                        <h3 className="font-semibold text-white mb-1">Business Hours</h3>
                                        <p className="text-gray-400">
                                            Monday - Friday: 9:00 AM - 6:00 PM IST<br />
                                            Saturday: 10:00 AM - 4:00 PM IST<br />
                                            Sunday: Closed
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-gradient-to-r from-cyan-500/10 to-purple-500/10 backdrop-blur-lg rounded-xl p-6 border border-cyan-500/20">
                            <h3 className="text-xl font-bold text-cyan-300 mb-3">Quick Support</h3>
                            <p className="text-gray-300 mb-4">
                                Need immediate assistance? Check our FAQ section or use our AI chat assistant on the home page.
                            </p>
                            <a
                                href="/"
                                className="inline-block px-6 py-2 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-semibold rounded-lg transition-all duration-300"
                            >
                                Go to Home
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
