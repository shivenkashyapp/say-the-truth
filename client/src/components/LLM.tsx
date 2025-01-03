import React, { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:5000';

const LLM: React.FC = () => {
    const [input, setInput] = useState('');
    const [responses, setResponses] = useState<any>([]);

    const handleSubmit = async () => {
        try {
            const res = await axios.post(API_URL, { input });
            console.log(res.data);
            setResponses(res.data);
        } catch (error) {
            console.error(error);
        }

        setInput('');
    };

    return (
        <div className="flex flex-col justify-between">
            <h2>LLM</h2>
            <div className="overflow-y-scroll h-48">
                {responses.map((res: any) => (
                    <div key={res.title}>
                        <h3>{res.title}</h3>
                        <a href={res.href}>Link</a>
                        <p>{res.body}</p>
                    </div>
                ))}
            </div>
            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    handleSubmit();
                }}
            >
                <label htmlFor="prompt">Prompt</label>
                <input
                    type="text"
                    name="prompt"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="What possible implications does this misinformation hold ?"
                    className="w-full rounded-md bg-[#949494] placeholder:text-gray-300 outline-none border-none p-2"
                    autoComplete="off"
                />
            </form>
        </div>
    );
};

export default LLM;
