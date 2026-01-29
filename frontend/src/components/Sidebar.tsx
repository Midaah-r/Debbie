import { useState } from "react"

const Sidebar = () => {
    const[isDark, setIsDark] = useState(false)
    const toggleDarkMode = () => {
    setIsDark(!isDark)
    document.documentElement.classList.toggle('dark')
    }
  return (
    <aside
    className='fixed left-0 top-0 h-full z-50 group flex flex-col w-16 hover:w-64 bg-yellow-50 border-r border-dark transition-all duration-500 ease-[cubic-bezier(0.23,1,0.32,1)]'
    >
    {/* Top Logo / Icon Area */}
    <div className="h-20 flex items-center px-5">
        <div className="w-6 h-6 bg-text rounded-full flex-shrink-0"/>
    <span className="ml-6 font-semibold text-text opacity-0 group-hover:opacity-100 transition-opacity duration-300 whitespace-nowrap">
        Menu
    </span>
    </div>

    {/* Nav Links */}
    
    <nav className="flex-1 px-3 space-y-4 mt-4">
        {['Dashboard', 'Analytics', 'Settings', 'Profile'].map((item) => (
            <div
                key={item}
                className="flex items-center p-3 rounded-xl hover:bg-dark cursor-pointer transition-colors group/item"
            >
                {/* Minimal Icon Placeholder */}
                <div className="w-5 h-5 border-2 rounded-md flex-shrink-0"/>
                <span className="ml-6 text-sm font-medium text-dark opacity-0 group-hover:opacity-100 transition-opacity duration-300 whitespace-nowrap">
                    {item}

                </span>

            </div>
        ))}
    </nav>

    {/* Bottom */}
    <div className="mt-auto p-3 border-t border-cream-dark dark:border-dark-border">
        <button
        onClick={toggleDarkMode}
        className="flex items-center w-full p-3 rounded-xl hover:bg-cream-dark dark:hover:bg-dark-border transition-all"
        >
            <div className="relative w-5 h-5 flex-shrink-0">
                {/* Sun Icon */}
                <div className={`absolute inset-0 transform transition-all duration-500 ${isDark ? 'rotate-90 scale-0 opacity-0' : 'rotate-0 scale-100 opacity-100'}`}>
                    <svg fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="text-warm-text">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
                    </svg>
                </div>
            </div>
            <span className="ml-6 text-sm font-medium text-warm-text dark:text-dark-text opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                {isDark ? 'Light' : 'Dark'}
            </span>
        </button>
    </div>
    </aside>
  )
}

export default Sidebar