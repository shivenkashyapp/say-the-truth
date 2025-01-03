import React from 'react';

const LLM: React.FC = () => {
    return (
        <div className="flex flex-col justify-between">
            <h2>LLM</h2>
            <div className="overflow-y-scroll">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Similique dignissimos quidem deserunt expedita vitae,
                    blanditiis distinctio dolore amet aspernatur corporis,
                    consequatur nostrum ipsum voluptatem neque rerum error
                    laboriosam molestias aperiam.
                </p>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Similique dignissimos quidem deserunt expedita vitae,
                    blanditiis distinctio dolore amet aspernatur corporis,
                    consequatur nostrum ipsum voluptatem neque rerum error
                    laboriosam molestias aperiam.
                </p>
            </div>
            <form>
                <label htmlFor="prompt"></label>
                <input
                    type="text"
                    name="prompt"
                    placeholder="What possible implications does this misinformation hold ?"
                    className="w-full rounded-md bg-[#949494] placeholder:text-gray-300 outline-none border-none p-2"
                />
            </form>
        </div>
    );
};

export default LLM;
