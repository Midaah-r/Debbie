import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import DashboardCard from "./DashboardCard";
import Sidebar from "./Sidebar";

const Layout: React.FC = () => {
  return (
    <div className="flex min-h-screen bg-cream-light dark:bg-dark-bg transition-colors duration-500">
        <Sidebar/>
        <div className="flex flex-col flex-1 pl-16">
            <Header/>
            <main className="flex-grow flex items-center justify-center p-6">
                <DashboardCard/>
            </main>
            <Footer/>
        </div>
    </div>
  )
}

export default Layout