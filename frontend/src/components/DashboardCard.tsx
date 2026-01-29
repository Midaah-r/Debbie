
const DashboardCard = () => {
  return (
    // Before: bg-white shadow-[...] 
// After:
<div className="w-full max-w-md p-10 rounded-2xl transition-all duration-500
                bg-white dark:bg-dark-card 
                border border-transparent dark:border-dark-border
                shadow-sm dark:shadow-none">
  
  <h2 className="text-2xl font-semibold mb-3 text-warm-text dark:text-dark-text">
    Welcome back
  </h2>
  
  <p className="leading-relaxed mb-8 text-warm-muted dark:text-warm-faint">
    Your workspace is ready.
  </p>

  {/* The separator line */}
  <div className="h-px w-full mb-8 bg-cream-dark dark:bg-dark-border" />

  <button className="w-full py-3 px-6 rounded-xl font-medium transition-colors
                     bg-warm-text text-cream-light 
                     dark:bg-dark-border dark:text-dark-text">
    Enter Dashboard
  </button>
</div>
  );
};

export default DashboardCard;