# 365WineTrade Business Central QuickStart Guide - HTML Site

This is the HTML website version of the 365WineTrade Business Central QuickStart Guide.

## Contents

This site includes:

- **Home Page** (`index.html`) - Introduction and learning path overview
- **Learning Path Pages**:
  - Round I: Getting Started (`round1-getting-started.html`)
  - Round II: Core Skills (`round2-core-skills.html`)
  - Round III: Foundational Concepts (`round3-foundational.html`)
- **Role-Specific Tracks**:
  - Admin & Leadership (`role-admin.html`) - *To be completed*
  - Finance (`role-finance.html`) - *To be completed*
  - Trade/Sales (`role-trade.html`) - ✅ Complete
  - Warehouse (`role-warehouse.html`) - *To be completed*
  - Power BI (`role-powerbi.html`) - *To be completed*
- **Reference Pages**:
  - Quick Reference (`quick-reference.html`) - ✅ Complete
  - Moving to 365WineTrade (`moving-to-365winetrade.html`) - ✅ Complete
  - Appendix (`appendix.html`) - *To be completed*

## Features

- ✅ **Responsive design** - Works on desktop, tablet, and mobile
- ✅ **Bootstrap 5** framework with custom wine-industry styling
- ✅ **Sidebar navigation** with active page highlighting
- ✅ **Breadcrumb navigation** for context
- ✅ **Previous/Next buttons** for sequential learning
- ✅ **Wine callouts** (🍷) highlighting 365WineTrade-specific features
- ✅ **Module cards** with direct links to Microsoft Learn
- ✅ **Keyboard shortcuts** (Alt+Left/Right for navigation)
- ✅ **Smooth scrolling** and progress indicator
- ✅ **Print-friendly** CSS

## To View the Site

Simply open `index.html` in any modern web browser. The site works entirely with local files - no web server required.

## To Deploy to a Web Server

Upload the entire `html_site` folder to your web server. The site structure is:

```
html_site/
├── index.html
├── round1-getting-started.html
├── round2-core-skills.html
├── round3-foundational.html
├── role-trade.html
├── quick-reference.html
├── moving-to-365winetrade.html
├── assets/
│   ├── css/
│   │   └── custom.css
│   └── js/
│       └── navigation.js
└── README.md
```

## Customization

### Colors

The site uses CSS custom properties (variables) for easy color customization. Edit `assets/css/custom.css`:

```css
:root {
  --wine-primary: #722f37;    /* Main wine red */
  --wine-secondary: #9b4f56;  /* Lighter wine red */
  --wine-light: #f8f3f4;      /* Light background */
  --wine-gold: #d4af37;       /* Gold accent */
}
```

### Logo

To add a logo to the header, edit the `.site-header` section in each HTML file.

### Footer

Update the footer content in each HTML file to change copyright text or add additional links.

## Dependencies

The site uses CDN-hosted libraries:

- **Bootstrap 5.3.2** - CSS framework
- **Bootstrap Icons 1.11.1** - Icon library

These are loaded from CDN, so an internet connection is required for full styling. If you need offline access, download these libraries and reference them locally.

## Browser Compatibility

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome)

## Future Enhancements

Consider adding:

- [ ] Complete remaining role-specific track pages
- [ ] Add Appendix page with detailed reference material
- [ ] Add search functionality across all pages
- [ ] Include screenshots from Business Central
- [ ] Add video embeds for key concepts
- [ ] Create PDF export functionality
- [ ] Add progress tracking (checkboxes that save to localStorage)

## Credits

Created by 365WineTrade and Western Computer for Business Central training.

## Support

For support with the guide content, contact your Western Computer implementation team.

For technical issues with the website, contact your IT department.
