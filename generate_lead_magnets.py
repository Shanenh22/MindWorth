#!/usr/bin/env python3
"""
MindWorth AI - Lead Magnet PDF Generator
Creates professional, branded PDF checklists for each service
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
import os

# Brand colors
ELECTRIC_PURPLE = colors.HexColor('#8B5CF6')
NEON_CYAN = colors.HexColor('#06D6A0')
DEEP_SPACE = colors.HexColor('#0F0F23')
PEARL_WHITE = colors.HexColor('#FEFEFE')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.grey)
        self.drawRightString(
            7.5 * inch, 0.5 * inch,
            f"Page {self._pageNumber} of {page_count}"
        )
        # Footer branding
        self.setFillColor(NEON_CYAN)
        self.drawString(1 * inch, 0.5 * inch, "MindWorth AI | mindworth.ai")

def create_header(title, subtitle):
    """Create branded header"""
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=ELECTRIC_PURPLE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=NEON_CYAN,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    elements = []
    elements.append(Paragraph(title, title_style))
    elements.append(Paragraph(subtitle, subtitle_style))
    elements.append(Spacer(1, 0.3 * inch))
    
    return elements

def create_section(section_title, items, styles):
    """Create a section with checklist items"""
    elements = []
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=ELECTRIC_PURPLE,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    item_style = ParagraphStyle(
        'ItemStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=DEEP_SPACE,
        leftIndent=20,
        spaceAfter=8,
        fontName='Helvetica'
    )
    
    elements.append(Paragraph(section_title, section_style))
    
    for item in items:
        checkbox = "☐"
        elements.append(Paragraph(f"{checkbox} {item}", item_style))
    
    elements.append(Spacer(1, 0.2 * inch))
    return elements

# Lead Magnet 1: Email & Admin Automation Checklist
def create_email_automation_checklist():
    filename = "/mnt/user-data/outputs/lead-magnets/email-admin-automation-checklist.pdf"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    # Header
    elements.extend(create_header(
        "10 Admin Tasks You Can Automate Today",
        "Free Checklist from MindWorth AI"
    ))
    
    # Intro
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "Use this checklist to identify which time-consuming tasks in your business can be automated. "
        "Check off each item as you implement automation. Even automating 2-3 of these will save you 5+ hours per week.",
        intro_style
    ))
    
    # Section 1: Email Management
    elements.extend(create_section(
        "1. Email Management (Save 2-4 hours/week)",
        [
            "Auto-sort incoming emails by sender, topic, or priority into folders",
            "Set up automatic forwarding rules for specific email types to team members",
            "Create email templates for common responses (reduce typing by 80%)",
            "Use scheduling tools to send emails at optimal times automatically",
            "Set up vacation/out-of-office auto-responders with smart routing"
        ],
        styles
    ))
    
    # Section 2: Data Entry
    elements.extend(create_section(
        "2. Data Entry & Processing (Save 3-5 hours/week)",
        [
            "Extract data from emails automatically into spreadsheets or CRM",
            "Auto-populate customer information when they fill out forms",
            "Parse invoices and receipts to extract key data (amount, date, vendor)",
            "Automatically update databases when specific triggers occur",
            "Sync data between multiple platforms (CRM, accounting, spreadsheets)"
        ],
        styles
    ))
    
    # Section 3: Scheduling
    elements.extend(create_section(
        "3. Scheduling & Calendar (Save 1-3 hours/week)",
        [
            "Enable self-service booking so customers can schedule without emails",
            "Send automatic meeting reminders 24 hours and 1 hour before appointments",
            "Auto-sync multiple calendars to prevent double-bookings",
            "Block buffer time between meetings automatically",
            "Send follow-up emails after meetings with action items"
        ],
        styles
    ))
    
    # Section 4: Follow-ups
    elements.extend(create_section(
        "4. Follow-Up Communications (Save 2-4 hours/week)",
        [
            "Create drip email campaigns that send automatically over time",
            "Set up lead nurturing sequences for new prospects",
            "Automate customer onboarding emails (welcome series)",
            "Send automatic reminders for pending tasks or overdue items",
            "Create triggered emails based on customer actions (clicked link, viewed page)"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    # Section 5: Social Media
    elements.extend(create_section(
        "5. Social Media Management (Save 2-3 hours/week)",
        [
            "Schedule posts in advance for all platforms simultaneously",
            "Auto-post blog content to social channels when published",
            "Set up automatic responses to common comments or messages",
            "Create content calendars that populate automatically",
            "Monitor mentions and get alerts for important conversations"
        ],
        styles
    ))
    
    # Section 6: Reporting
    elements.extend(create_section(
        "6. Reporting & Analytics (Save 1-2 hours/week)",
        [
            "Generate weekly/monthly reports automatically from your data",
            "Create dashboards that update in real-time",
            "Send automated report emails to stakeholders on schedule",
            "Track key metrics automatically without manual spreadsheet work",
            "Set up alerts when metrics hit certain thresholds"
        ],
        styles
    ))
    
    # Section 7: Document Management
    elements.extend(create_section(
        "7. Document Management (Save 1-2 hours/week)",
        [
            "Auto-file documents to correct folders based on rules",
            "Extract text from PDFs and images automatically (OCR)",
            "Generate contracts or proposals from templates with auto-fill",
            "Create automatic backup systems for important files",
            "Set expiration reminders for contracts or certifications"
        ],
        styles
    ))
    
    # Section 8: Customer Support
    elements.extend(create_section(
        "8. Customer Support (Save 2-4 hours/week)",
        [
            "Set up chatbot for common questions (24/7 availability)",
            "Auto-categorize support tickets by urgency or topic",
            "Send automatic acknowledgment emails when tickets are received",
            "Route tickets to appropriate team members automatically",
            "Create knowledge base articles that answer FAQs automatically"
        ],
        styles
    ))
    
    # Section 9: Financial Tasks
    elements.extend(create_section(
        "9. Financial Tasks (Save 1-3 hours/week)",
        [
            "Auto-generate and send invoices when work is completed",
            "Send payment reminders for overdue invoices automatically",
            "Reconcile bank transactions with accounting software",
            "Track expenses and categorize automatically",
            "Generate financial reports on a schedule"
        ],
        styles
    ))
    
    # Section 10: Team Coordination
    elements.extend(create_section(
        "10. Team Coordination (Save 1-2 hours/week)",
        [
            "Auto-assign tasks based on workload or specialty",
            "Send daily/weekly digest emails with team updates",
            "Create recurring meeting invites automatically",
            "Share project updates to Slack/Teams channels automatically",
            "Track time and generate timesheets without manual entry"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    # CTA
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Ready to Automate Your Business?", cta_style))
    elements.append(Paragraph(
        "Schedule a free 45-minute audit at <b>mindworth.ai</b><br/>"
        "We'll identify your biggest time-wasters and show you exactly what we can automate.",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

# Lead Magnet 2: Customer Insights Guide
def create_customer_insights_guide():
    filename = "/mnt/user-data/outputs/lead-magnets/customer-insights-analysis-guide.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.extend(create_header(
        "Customer Feedback Analysis Framework",
        "Turn Reviews & Feedback into Actionable Insights"
    ))
    
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "This framework helps you systematically analyze customer feedback to uncover patterns, "
        "identify problems, and make data-driven decisions. Use this whether analyzing manually or setting up automation.",
        intro_style
    ))
    
    elements.extend(create_section(
        "Step 1: Collect Feedback from All Sources",
        [
            "Google Reviews, Yelp, Facebook, and industry-specific review sites",
            "Support tickets and email conversations with customers",
            "Survey responses (NPS, CSAT, post-purchase surveys)",
            "Social media mentions and comments",
            "Sales call notes and lost opportunity reasons",
            "Live chat transcripts and chatbot conversations",
            "Product return/refund request reasons"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 2: Categorize by Topic",
        [
            "Product/service quality issues",
            "Pricing and value perception",
            "Customer service experiences",
            "Shipping/delivery problems",
            "Website/app usability",
            "Feature requests and missing functionality",
            "Competitor comparisons"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 3: Score Sentiment",
        [
            "Rate each piece of feedback: Positive (1), Neutral (0), Negative (-1)",
            "Calculate overall sentiment score by category",
            "Track sentiment trends over time (weekly/monthly)",
            "Flag urgent negative feedback requiring immediate response",
            "Identify your biggest fans for testimonials and case studies"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    elements.extend(create_section(
        "Step 4: Identify Patterns & Trends",
        [
            "Count frequency of each topic mention",
            "Look for issues mentioned across multiple channels",
            "Compare this month vs. last month for changes",
            "Segment by customer type (new vs. repeat, small vs. large)",
            "Identify seasonal patterns or campaign-related feedback",
            "Spot emerging problems before they become major issues"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 5: Prioritize Actions",
        [
            "High frequency + negative sentiment = urgent priority",
            "Quick wins: easy fixes with high impact",
            "Long-term improvements: strategic initiatives",
            "Customer requests vs. internal priorities alignment",
            "ROI calculation: cost of fix vs. customer retention value"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 6: Create Feedback Reports",
        [
            "Weekly: Top 3 urgent issues, new patterns emerging",
            "Monthly: Sentiment trends, top topics, feature requests leaderboard",
            "Quarterly: Customer satisfaction changes, major improvements implemented",
            "Share insights with product, marketing, and leadership teams",
            "Track action items and measure impact of changes"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Key Metrics to Track",
        [
            "Overall sentiment score (track monthly)",
            "Net Promoter Score (NPS) if using surveys",
            "Response time to negative reviews",
            "% of feedback actioned vs. ignored",
            "Customer churn rate correlation with feedback themes",
            "Feature request popularity rankings"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Tools You Can Use",
        [
            "Spreadsheets: Free but manual (Google Sheets templates)",
            "Review aggregators: Trustpilot, Podium, Birdeye",
            "Survey platforms: Typeform, SurveyMonkey, Google Forms",
            "AI analysis: ChatGPT, sentiment analysis APIs",
            "Professional automation: Custom dashboards (what we build)"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Want This Automated?", cta_style))
    elements.append(Paragraph(
        "We build custom sentiment analysis dashboards that do all this automatically.<br/>"
        "Schedule a free demo at <b>mindworth.ai</b>",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

# Lead Magnet 3: Smart Scheduling Guide
def create_scheduling_guide():
    filename = "/mnt/user-data/outputs/lead-magnets/smart-scheduling-implementation-guide.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.extend(create_header(
        "Smart Scheduling Implementation Guide",
        "Eliminate Double-Bookings & No-Shows Forever"
    ))
    
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "Follow this step-by-step guide to implement automated scheduling in your business. "
        "Reduce no-shows by 60%, save 5-8 hours weekly, and never miss a booking opportunity again.",
        intro_style
    ))
    
    elements.extend(create_section(
        "Phase 1: Preparation (30 minutes)",
        [
            "List all appointment types you offer (consultations, services, meetings)",
            "Define duration for each appointment type (15min, 30min, 1hr, etc.)",
            "Identify your available hours (M-F 9am-5pm, evenings, weekends)",
            "Determine buffer time needed between appointments (5-15 minutes)",
            "Note any blackout dates or recurring unavailable times",
            "Decide: one calendar for team or individual calendars per person"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Phase 2: Choose Your Tools (1 hour research)",
        [
            "Calendly: Best for simple scheduling, free plan available",
            "Acuity Scheduling: More features, $16+/month, great for service businesses",
            "Cal.com: Open-source alternative, free self-hosted option",
            "Square Appointments: Best if you also take payments",
            "SimplyBook.me: Good for teams, many integrations",
            "Check which integrates with your current calendar (Google/Outlook)"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Phase 3: Basic Setup (2 hours)",
        [
            "Create account and connect to your calendar",
            "Set up each appointment type with correct duration",
            "Configure your weekly availability hours",
            "Set buffer times between appointments",
            "Add your business information and branding",
            "Create custom booking page URL (yourbusiness.calendly.com)",
            "Test by booking a test appointment yourself"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    elements.extend(create_section(
        "Phase 4: Customize Booking Experience (1 hour)",
        [
            "Add intake questions customers answer when booking",
            "Customize confirmation email with your branding",
            "Set up custom booking confirmation page",
            "Add your cancellation/rescheduling policy",
            "Enable timezone detection for remote clients",
            "Configure minimum notice period (e.g., 24 hours in advance)"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Phase 5: Implement Reminders (30 minutes)",
        [
            "Enable email reminders: 24 hours before appointment",
            "Set up second reminder: 1 hour before appointment",
            "Consider SMS reminders for critical appointments (reduce no-shows 30%)",
            "Customize reminder message with location/preparation instructions",
            "Include easy reschedule/cancel links in reminders",
            "Test all reminders by booking another test appointment"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Phase 6: Distribution & Promotion (1 hour)",
        [
            "Add booking button to your website homepage",
            "Include booking link in email signature",
            "Add to social media bios (Instagram, Facebook, LinkedIn)",
            "Create QR code for physical locations/business cards",
            "Update Google Business Profile with booking link",
            "Train team on how to share booking link with customers"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Phase 7: Advanced Features (Optional)",
        [
            "Payment collection: Require deposit or full payment when booking",
            "Team scheduling: Round-robin or priority-based assignment",
            "Waitlist: Auto-fill cancellations from waitlist",
            "Group bookings: Classes or multi-person appointments",
            "Package deals: Series of appointments or bundles",
            "Zapier integration: Connect to CRM, send to Slack, etc."
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Common Mistakes to Avoid",
        [
            "Making booking process too long (keep to 3 steps max)",
            "Asking too many questions during booking (get details later)",
            "Not testing on mobile devices (50%+ of bookings are mobile)",
            "Forgetting to block personal time/vacations",
            "Setting availability too far in future (30-60 days is optimal)",
            "No cancellation policy = lots of last-minute cancellations"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Measure Success: Track These Metrics",
        [
            "% of appointments booked online vs. phone/email",
            "No-show rate before and after reminders",
            "Time saved on scheduling coordination weekly",
            "After-hours bookings captured",
            "Average time from inquiry to scheduled appointment"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Need Help Setting This Up?", cta_style))
    elements.append(Paragraph(
        "We handle the entire implementation for you—from setup to training.<br/>"
        "Schedule a free assessment at <b>mindworth.ai</b>",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

# Generate all PDFs
def generate_all_lead_magnets():
    print("Generating MindWorth AI Lead Magnets...")
    
    pdfs = []
    
    print("1/6 Creating Email & Admin Automation Checklist...")
    pdfs.append(create_email_automation_checklist())
    
    print("2/6 Creating Customer Insights Analysis Guide...")
    pdfs.append(create_customer_insights_guide())
    
    print("3/6 Creating Smart Scheduling Implementation Guide...")
    pdfs.append(create_scheduling_guide())
    
    # Create simple versions for remaining 3 services
    print("4/6 Creating Sales Follow-Up Playbook...")
    pdfs.append(create_sales_followup_playbook())
    
    print("5/6 Creating Document Processing Blueprint...")
    pdfs.append(create_document_processing_blueprint())
    
    print("6/6 Creating AI Content Creation Playbook...")
    pdfs.append(create_content_creation_playbook())
    
    print("\n✅ All lead magnets created successfully!")
    print("\nFiles generated:")
    for pdf in pdfs:
        print(f"  - {pdf}")
    
    return pdfs

# Lead Magnet 4: Sales Follow-Up Playbook
def create_sales_followup_playbook():
    filename = "/mnt/user-data/outputs/lead-magnets/sales-follow-up-playbook.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.extend(create_header(
        "Sales Follow-Up Playbook",
        "Never Lose a Lead Again: 7-Touch Email Sequence Template"
    ))
    
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "80% of sales require 5+ follow-ups, but most businesses stop after 2. "
        "Use this proven 7-email sequence to nurture leads systematically and increase conversion by 20-30%.",
        intro_style
    ))
    
    elements.extend(create_section(
        "Email 1: Immediate Auto-Response (0 minutes after inquiry)",
        [
            "Subject: Thanks for your interest, [Name]",
            "Confirm you received their inquiry",
            "Set expectations for next steps",
            "Provide immediate value (relevant resource or guide)",
            "Include your calendar link to book a call",
            "Keep it short (3-4 sentences max)"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email 2: Case Study/Social Proof (Day 2)",
        [
            "Subject: How [Similar Company] solved [Their Problem]",
            "Share a relevant customer success story",
            "Focus on results, not features",
            "Match their industry or use case if possible",
            "Soft CTA: 'Curious if we can do the same for you?'",
            "No hard sell—just demonstrate capability"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email 3: Value Question (Day 5)",
        [
            "Subject: Quick question about [Their Goal]",
            "Ask about their timeline or specific needs",
            "Reference something from their initial inquiry",
            "Offer to answer any questions",
            "Position yourself as a consultant, not salesperson",
            "Open-ended question to start conversation"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email 4: Educational Content (Day 9)",
        [
            "Subject: [Video] See how it works in 90 seconds",
            "Share demo video, tutorial, or product walkthrough",
            "Explain one key feature or benefit clearly",
            "Make it easy to understand without jargon",
            "CTA: Schedule a personalized demo",
            "Alternative: Share helpful blog post or guide"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    elements.extend(create_section(
        "Email 5: Limited Offer/Urgency (Day 14)",
        [
            "Subject: [Month] only: [Special offer]",
            "Create legitimate urgency (discount, bonus, limited slots)",
            "Highlight the benefit of acting now",
            "Include clear pricing or package details",
            "Strong CTA with deadline",
            "Option: Feature a specific customer pain point you solve"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email 6: Final Value Add (Day 18)",
        [
            "Subject: One more thing that might help...",
            "Share your best resource (checklist, template, tool)",
            "No strings attached—genuinely helpful",
            "Soft reminder you're available to help",
            "CTA: 'Reply if you have questions'",
            "Position as helpful expert, not pushy salesperson"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email 7: Breakup Email (Day 21)",
        [
            "Subject: Should I close your file?",
            "Acknowledge they might not be ready",
            "Give permission to say 'not now'",
            "Offer to check back in 3-6 months",
            "Final CTA: 'Reply if you'd like to stay in touch'",
            "This often triggers a response from fence-sitters"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Pro Tips for Maximum Effectiveness",
        [
            "Personalize with their name, company, and specific pain points",
            "Sequence pauses automatically if they reply",
            "A/B test subject lines to improve open rates",
            "Send emails during business hours (9am-5pm their timezone)",
            "Track opens and clicks to identify hot leads",
            "Move engaged leads to sales call faster",
            "Move unengaged leads to long-term nurture list"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "After the Sequence: Long-Term Nurture",
        [
            "Don't delete non-responders—add to monthly newsletter",
            "Share valuable content once per month",
            "Announce new features, case studies, offers",
            "Re-engage campaign after 3-6 months",
            "Some leads need 6-12 months before they're ready",
            "Stay top-of-mind without being annoying"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Want This Automated?", cta_style))
    elements.append(Paragraph(
        "We write, design, and automate the entire follow-up sequence for you.<br/>"
        "Schedule a free sales audit at <b>mindworth.ai</b>",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

# Lead Magnet 5: Document Processing Blueprint
def create_document_processing_blueprint():
    filename = "/mnt/user-data/outputs/lead-magnets/document-processing-blueprint.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.extend(create_header(
        "Document Automation Blueprint",
        "Stop Manual Data Entry: Implementation Guide + ROI Calculator"
    ))
    
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "Manual data entry from invoices, receipts, and forms wastes 10-20 hours weekly for most businesses. "
        "This guide shows you how to automate document processing with 95%+ accuracy.",
        intro_style
    ))
    
    elements.extend(create_section(
        "Step 1: Audit Your Document Types",
        [
            "List all documents you manually process (invoices, receipts, forms, contracts)",
            "Estimate volume per month for each type",
            "Calculate time spent per document (avg 5-10 minutes)",
            "Identify which data fields you extract (vendor, date, amount, line items)",
            "Note which software you enter data into (QuickBooks, Excel, CRM)",
            "Prioritize by volume × time = biggest time sink first"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 2: Calculate Your ROI",
        [
            "Documents per month: _______",
            "Minutes per document: _______",
            "Total hours monthly: _______ (multiply above)",
            "Hourly cost (salary/rate): $_______",
            "Monthly cost of manual entry: $_______ ",
            "Annual cost: $_______ (monthly × 12)",
            "Automation ROI payback: 2-6 months typically"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 3: Choose Your Processing Method",
        [
            "Basic OCR: Google Cloud Vision, AWS Textract ($1-3 per 1000 docs)",
            "Smart extraction: GPT-4 API for complex documents ($5-10 per 1000)",
            "Pre-built tools: Rossum, Docsumo, Nanonets (subscription-based)",
            "Full automation: Custom solution (what we build) ($3K-6K setup)",
            "Hybrid: Manual review queue for uncertain extractions",
            "Consider volume, accuracy needs, and integration requirements"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    elements.extend(create_section(
        "Step 4: Prepare Your Documents",
        [
            "Scan quality: 300+ DPI for best OCR accuracy",
            "File format: PDF preferred, JPG/PNG acceptable",
            "Organize samples: Collect 20-50 examples of each document type",
            "Note variations: Different layouts, formats, languages",
            "Clean scans: Remove shadows, straighten images, ensure legibility",
            "Consistent naming: invoice_vendor_date.pdf for easy identification"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 5: Set Up Processing Workflow",
        [
            "Upload method: Email forwarding, Dropbox folder, or mobile scan app",
            "Processing trigger: Automatic when document arrives",
            "Extraction: AI reads document and pulls data fields",
            "Validation: Check for completeness and data quality",
            "Human review: Flag uncertain extractions (confidence <90%)",
            "Integration: Push data to destination (QuickBooks, Excel, database)",
            "Archive: Store original document securely"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Step 6: Train & Validate",
        [
            "Test with 50-100 real documents from your business",
            "Measure accuracy: Target 95%+ for standard fields",
            "Identify problem areas: Handwriting, poor quality, unusual formats",
            "Refine extraction rules based on test results",
            "Create validation rules (amounts must be >0, dates logical, etc.)",
            "Set up quality checks and error alerts"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Common Document Types & Accuracy Rates",
        [
            "Invoices (printed): 95-98% accuracy on key fields",
            "Receipts (printed): 90-95% accuracy (varies by format)",
            "Forms (typed): 98%+ accuracy on checkboxes and text",
            "Forms (handwritten): 60-85% depending on legibility",
            "Contracts (PDF): 95%+ for standard clauses and dates",
            "Business cards: 90-95% for contact information",
            "IDs/Licenses: 95%+ when properly scanned"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Data Fields You Can Extract",
        [
            "Invoice: Vendor, invoice #, date, due date, line items, subtotal, tax, total",
            "Receipt: Merchant, date, time, items, amounts, payment method",
            "Form: All text fields, checkboxes, signatures (as images)",
            "Contract: Parties, dates, terms, renewal clauses, payment terms",
            "W-9/Tax Forms: Name, EIN/SSN, address, business type",
            "Purchase Order: PO#, vendor, items, quantities, prices"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Integration Destinations",
        [
            "Accounting: QuickBooks, Xero, FreshBooks, Sage",
            "Spreadsheets: Excel, Google Sheets, Airtable",
            "Databases: MySQL, PostgreSQL, MongoDB",
            "CRM: Salesforce, HubSpot, Pipedrive",
            "ERP: NetSuite, Odoo, SAP",
            "Custom: API connections to proprietary systems"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Ready to Eliminate Data Entry?", cta_style))
    elements.append(Paragraph(
        "Send us your documents and we'll show you exactly what we can extract.<br/>"
        "Schedule a free assessment at <b>mindworth.ai</b>",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

# Lead Magnet 6: Content Creation Playbook
def create_content_creation_playbook():
    filename = "/mnt/user-data/outputs/lead-magnets/content-creation-playbook.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.extend(create_header(
        "AI Content Creation Playbook",
        "50+ Prompts & Templates for Marketing Content"
    ))
    
    intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=11, spaceAfter=20)
    elements.append(Paragraph(
        "Stop staring at blank pages. Use these AI prompts to generate marketing content 10x faster. "
        "Each prompt produces professional first drafts you can edit in minutes instead of writing for hours.",
        intro_style
    ))
    
    elements.extend(create_section(
        "How to Use These Prompts Effectively",
        [
            "Replace [BRACKETS] with your specific information",
            "Add context about your brand voice (professional, casual, technical)",
            "Include examples of your best past content",
            "Request multiple variations (ask for 5 options)",
            "Always edit AI output—treat it as a first draft",
            "Test different prompts to see what works best",
            "Save successful prompts as templates for reuse"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Social Media Post Prompts",
        [
            "LinkedIn thought leadership: 'Write a LinkedIn post about [TOPIC] that positions me as an expert. Include a hook, 3 key points, and a question to drive engagement.'",
            "Problem-solution post: 'Create a social post about how [YOUR SERVICE] solves [CUSTOMER PAIN POINT]. Start with the problem, then introduce the solution.'",
            "Behind-the-scenes: 'Write a casual post showing [BEHIND SCENES MOMENT] that humanizes my brand and connects with audience.'",
            "Carousel content: 'Create an 8-slide carousel about [TOPIC]. Each slide should have a headline and 2-3 bullet points.'",
            "Engagement post: 'Write a short post that asks my audience about [QUESTION]. Make it conversational and encourage comments.'"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Email Marketing Prompts",
        [
            "Newsletter: 'Write a weekly newsletter for [AUDIENCE]. Include: 1) Hook about [TOPIC], 2) Main insight, 3) Practical tip, 4) CTA to [ACTION].'",
            "Promotional campaign: 'Create a 3-email sequence promoting [PRODUCT/SERVICE]. Email 1: Problem awareness, Email 2: Solution benefits, Email 3: Limited offer.'",
            "Subject lines: 'Generate 10 email subject lines for [CONTENT/OFFER]. Focus on curiosity, urgency, and benefit. Keep under 50 characters.'",
            "Re-engagement: 'Write an email to win back inactive subscribers. Acknowledge absence, offer value, give option to unsubscribe gracefully.'",
            "Welcome series: 'Create email #2 of a welcome series. Introduce [KEY BENEFIT], share customer story, guide to getting started.'"
        ],
        styles
    ))
    
    elements.append(PageBreak())
    
    elements.extend(create_section(
        "Blog Post & Long-Form Prompts",
        [
            "Outline first: 'Create a detailed outline for a blog post about [TOPIC]. Include introduction, 5 main sections with subpoints, and conclusion.'",
            "Introduction: 'Write an engaging introduction for a blog post about [TOPIC]. Hook the reader, state the problem, preview the solution.'",
            "Expand sections: 'Write 300 words expanding on this point: [COPY OUTLINE POINT]. Include examples and actionable advice.'",
            "How-to guide: 'Write a step-by-step guide on [PROCESS]. Make it beginner-friendly with clear instructions for each step.'",
            "Listicle: 'Create a list-based article: \"[NUMBER] Ways to [ACHIEVE GOAL]\". Each item should have a headline, description, and example.'"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Ad Copy & Sales Prompts",
        [
            "Google Ads: 'Write 5 Google ad headlines (30 chars max) and 3 descriptions (90 chars max) for [PRODUCT/SERVICE]. Focus on benefits.'",
            "Facebook Ads: 'Create Facebook ad primary text, headline, and description for [OFFER]. Target audience: [DEMOGRAPHIC]. Address their pain point: [PROBLEM].'",
            "Landing page hero: 'Write a compelling headline and subheadline for a landing page selling [PRODUCT]. Focus on the main benefit and outcome.'",
            "Sales email: 'Write a sales email to [TARGET PERSON] introducing [SOLUTION]. Use the AIDA framework: Attention, Interest, Desire, Action.'",
            "Product description: 'Write a product description for [PRODUCT]. Include features, benefits, who it's for, and what problem it solves.'"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Video Script & Multimedia Prompts",
        [
            "YouTube intro: 'Write a 30-second video intro hook for a video about [TOPIC]. Grab attention and explain what viewers will learn.'",
            "Explainer script: 'Create a 90-second explainer video script for [PRODUCT/SERVICE]. Problem → Solution → How It Works → CTA.'",
            "Short-form video: 'Write a 15-second TikTok/Reel script about [TOPIC]. Start with a hook, deliver value quickly, end with engagement question.'",
            "Podcast outline: 'Create an outline for a 30-minute podcast episode about [TOPIC]. Include intro, 3 main segments with talking points, outro.'",
            "Webinar slides: 'Outline 15 slides for a webinar on [TOPIC]. Each slide should have a headline and 3-5 bullet points.'"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Content Repurposing Prompts",
        [
            "Blog to social: 'Take this blog post [PASTE TEXT] and create 5 social media posts highlighting different key points.'",
            "Long to short: 'Summarize this article [PASTE] into a 3-sentence LinkedIn post with a hook.'",
            "Transcript to article: 'Convert this video transcript [PASTE] into a structured blog post with headers and sections.'",
            "Email to thread: 'Turn this email newsletter [PASTE] into a Twitter/X thread with 8-10 tweets.'",
            "Case study to carousel: 'Transform this case study [PASTE] into a 10-slide carousel format for Instagram/LinkedIn.'"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Brand Voice Training Prompt",
        [
            "Use this prompt first to teach AI your voice:",
            "'Here are 3 examples of my best content: [PASTE EXAMPLES]",
            "Analyze the writing style, tone, and voice. Then rewrite the following content to match that same style: [NEW CONTENT]'",
            "This trains the AI on YOUR specific voice patterns",
            "Save this as a custom instruction in ChatGPT",
            "Reference it at start of future content creation sessions"
        ],
        styles
    ))
    
    elements.extend(create_section(
        "Quality Control Checklist",
        [
            "Read AI output carefully—it may include false facts or generic statements",
            "Fact-check any statistics, dates, or specific claims",
            "Remove buzzwords and corporate jargon (leverage, synergy, paradigm)",
            "Add personal anecdotes or specific examples",
            "Ensure brand voice consistency across all content",
            "Check tone matches platform (LinkedIn ≠ TikTok)",
            "Verify CTAs are clear and aligned with business goals",
            "Run through grammar/spell checker before publishing"
        ],
        styles
    ))
    
    elements.append(Spacer(1, 0.3 * inch))
    
    cta_style = ParagraphStyle('CTA', parent=styles['Normal'], fontSize=12, 
                               textColor=ELECTRIC_PURPLE, alignment=TA_CENTER,
                               spaceAfter=10, fontName='Helvetica-Bold')
    
    elements.append(Paragraph("Want Custom Content Templates?", cta_style))
    elements.append(Paragraph(
        "We build custom GPT models trained on YOUR brand voice with personalized templates.<br/>"
        "Schedule a free content audit at <b>mindworth.ai</b>",
        ParagraphStyle('CTAText', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
    ))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    return filename

if __name__ == "__main__":
    generate_all_lead_magnets()