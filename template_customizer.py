#!/usr/bin/env python3
"""
Fiverr Template Customization Tool
Automatically personalizes all Fiverr templates with user information
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Any

class FiverrTemplateCustomizer:
    def __init__(self, templates_dir: str, output_dir: str):
        self.templates_dir = Path(templates_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Default template variables that will be replaced
        self.template_vars = {
            'seller_name': 'Michelle Alexander',
            'seller_title': 'Strategic IT Business Advisor | Data Analytics MBA',
            'company_name': 'DataPro Analytics',
            'years_experience': '15+',
            'mba_credential': 'MBA in Data Analytics',
            'fortune_500_companies': 'Bank of America, Charter Communications',
            'portfolio_value': '$147M+',
            'compliance_improvement': '95%',
            'delivery_acceleration': '30%',
            'projects_completed': '500+',
            'satisfaction_rate': '98%',
            'website_domain': 'yourdomain.com',
            'email_address': 'your-email@domain.com',
            'phone_number': '+1-XXX-XXX-XXXX',
            'location': 'Your City, State'
        }
    
    def load_user_config(self, config_file: str) -> Dict[str, Any]:
        """Load user configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file {config_file} not found. Using default values.")
            return {}
    
    def update_template_vars(self, user_config: Dict[str, Any]):
        """Update template variables with user-provided values"""
        for key, value in user_config.items():
            if key in self.template_vars:
                self.template_vars[key] = value
    
    def customize_template(self, template_content: str) -> str:
        """Replace template variables in content"""
        customized_content = template_content
        
        # Replace all template variables
        for var_name, var_value in self.template_vars.items():
            # Replace various formats: {var_name}, [VAR_NAME], {{var_name}}
            patterns = [
                f'{{{var_name}}}',
                f'[{var_name.upper()}]',
                f'{{{{{var_name}}}}}',
                f'[{var_name}]'
            ]
            
            for pattern in patterns:
                customized_content = customized_content.replace(pattern, str(var_value))
        
        # Replace specific known placeholders
        replacements = {
            'Michelle Alexander': self.template_vars['seller_name'],
            'DataPro Analytics': self.template_vars['company_name'],
            'yourdomain.com': self.template_vars['website_domain'],
            'your-email@domain.com': self.template_vars['email_address'],
            '[Client Name]': '[Client Name]',  # Keep this as placeholder
            '[Your Name]': self.template_vars['seller_name']
        }
        
        for old_text, new_text in replacements.items():
            customized_content = customized_content.replace(old_text, new_text)
        
        return customized_content
    
    def process_all_templates(self):
        """Process all template files in the templates directory"""
        processed_files = []
        
        for template_file in self.templates_dir.glob('*.md'):
            try:
                # Read template content
                with open(template_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Customize content
                customized_content = self.customize_template(content)
                
                # Write to output directory
                output_file = self.output_dir / f"customized_{template_file.name}"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(customized_content)
                
                processed_files.append(str(output_file))
                print(f"✅ Processed: {template_file.name} -> {output_file.name}")
                
            except Exception as e:
                print(f"❌ Error processing {template_file.name}: {str(e)}")
        
        return processed_files
    
    def generate_fiverr_gig_files(self):
        """Generate separate files for each Fiverr gig"""
        gig_templates = {
            'market_research_gig.md': {
                'title': 'I will create comprehensive market research reports with competitive analysis and industry insights',
                'category': 'Market Research',
                'base_price': 299
            },
            'bi_dashboard_gig.md': {
                'title': 'I will create interactive business intelligence dashboards with real-time KPI tracking',
                'category': 'Business Intelligence',
                'base_price': 399
            },
            'data_analysis_gig.md': {
                'title': 'I will provide comprehensive data analysis with actionable insights and strategic recommendations',
                'category': 'Data Analysis',
                'base_price': 199
            },
            'strategic_consulting_gig.md': {
                'title': 'I will provide strategic business consulting with data-driven insights and implementation roadmaps',
                'category': 'Strategic Consulting',
                'base_price': 599
            }
        }
        
        for filename, gig_info in gig_templates.items():
            gig_content = self.generate_gig_template(gig_info)
            output_file = self.output_dir / filename
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(gig_content)
            
            print(f"✅ Generated: {filename}")
    
    def generate_gig_template(self, gig_info: Dict[str, Any]) -> str:
        """Generate a complete gig template"""
        return f"""# {gig_info['title']}

## Gig Category: {gig_info['category']}
## Base Price: ${gig_info['base_price']}

## Gig Description
**Transform your business with professional {gig_info['category'].lower()} services!**

Hi! I'm {self.template_vars['seller_name']}, a {self.template_vars['seller_title']} with {self.template_vars['years_experience']} years of experience helping businesses make data-driven decisions.

**My Expertise:**
• {self.template_vars['mba_credential']} with advanced analytics training
• {self.template_vars['years_experience']} years of strategic consulting experience
• Worked with Fortune 500 companies: {self.template_vars['fortune_500_companies']}
• Managed {self.template_vars['portfolio_value']} portfolio with measurable results
• Achieved {self.template_vars['compliance_improvement']} compliance improvement and {self.template_vars['delivery_acceleration']} delivery acceleration

**Why Choose Me:**
✅ {self.template_vars['projects_completed']} successful projects completed
✅ {self.template_vars['satisfaction_rate']} client satisfaction rate
✅ Fast turnaround with quality guaranteed
✅ Clear communication throughout the project
✅ Post-delivery support included

**Ready to transform your business? Let's discuss your project!**

## Package Structure

### Basic Package - ${gig_info['base_price']}
- Core service delivery
- Professional report/analysis
- 3-5 day delivery
- 2 revisions included

### Standard Package - ${gig_info['base_price'] * 2}
- Everything in Basic
- Enhanced analysis and insights
- Additional deliverables
- 5-7 day delivery
- 3 revisions included

### Premium Package - ${gig_info['base_price'] * 3}
- Everything in Standard
- Comprehensive analysis
- Strategic recommendations
- Consultation call included
- 7-10 day delivery
- Unlimited revisions

## Gig Extras
- Rush Delivery (24-48 hours): +$200
- Additional Analysis: +$150
- Follow-up Consultation: +$200
- Monthly Updates: +$300

## FAQ
**Q: What do you need from me to get started?**
A: I'll send you a detailed questionnaire to understand your specific needs and objectives.

**Q: How do you ensure data confidentiality?**
A: I follow strict data security protocols and can sign NDAs. All information is handled with complete confidentiality.

**Q: What if I need revisions?**
A: All packages include revisions, and I work with you until you're 100% satisfied with the results.

---
*Contact me before placing an order to discuss your specific requirements and ensure the best results!*
"""
    
    def generate_quick_responses(self):
        """Generate Fiverr quick response templates"""
        quick_responses = {
            'initial_inquiry.txt': f"""Hi [Buyer Name],

Thank you for your interest in my {'{service_type}'} services! I'm excited to help you achieve your business goals.

With my {self.template_vars['years_experience']} years of experience and {self.template_vars['mba_credential']}, I deliver results that drive real business impact.

To provide the best recommendations, could you please share:
• Your industry and business objectives
• Specific requirements or challenges
• Timeline for completion
• Any existing data or materials

I typically respond within 1-2 hours and would love to discuss your project in detail.

Looking forward to working with you!

Best regards,
{self.template_vars['seller_name']}
{self.template_vars['seller_title']}""",
            
            'project_kickoff.txt': f"""Hi [Buyer Name],

Great! I'm excited to start working on your project. Here's what happens next:

**Next Steps:**
1. I'll send you a detailed questionnaire within 2 hours
2. Once completed, I'll begin the analysis/research
3. I'll provide progress updates every 24-48 hours
4. Final delivery will be on [delivery_date]

**What You Can Expect:**
✅ Professional, comprehensive analysis
✅ Clear, actionable recommendations
✅ Regular communication throughout the project
✅ High-quality deliverables that exceed expectations

If you have any questions or additional requirements, please let me know immediately.

Let's create something amazing together!

Best regards,
{self.template_vars['seller_name']}""",
            
            'delivery_notification.txt': f"""Hi [Buyer Name],

Excellent news! Your project is now complete and ready for delivery.

**What's Included:**
✅ [List specific deliverables]
✅ Executive summary with key findings
✅ Actionable recommendations
✅ Supporting data and analysis

**Next Steps:**
1. Please review all deliverables
2. Let me know if you need any clarifications
3. I'm available for a follow-up call if needed

I'm confident these insights will drive significant value for your business. Please don't hesitate to reach out if you have any questions.

Thank you for choosing my services!

Best regards,
{self.template_vars['seller_name']}
{self.template_vars['seller_title']}"""
        }
        
        responses_dir = self.output_dir / 'quick_responses'
        responses_dir.mkdir(exist_ok=True)
        
        for filename, content in quick_responses.items():
            with open(responses_dir / filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Generated quick response: {filename}")

def main():
    """Main function to run the template customizer"""
    print("🚀 Fiverr Template Customization Tool")
    print("=" * 50)
    
    # Set up paths
    templates_dir = "/home/ubuntu/upload/extracted_files"
    output_dir = "/home/ubuntu/fiverr_automation_system/customized_templates"
    config_file = "/home/ubuntu/fiverr_automation_system/user_config.json"
    
    # Initialize customizer
    customizer = FiverrTemplateCustomizer(templates_dir, output_dir)
    
    # Load user configuration if available
    user_config = customizer.load_user_config(config_file)
    customizer.update_template_vars(user_config)
    
    print(f"📁 Processing templates from: {templates_dir}")
    print(f"📁 Output directory: {output_dir}")
    print()
    
    # Process all templates
    processed_files = customizer.process_all_templates()
    
    # Generate Fiverr-specific files
    print("\n🎯 Generating Fiverr gig templates...")
    customizer.generate_fiverr_gig_files()
    
    print("\n💬 Generating quick response templates...")
    customizer.generate_quick_responses()
    
    print(f"\n✅ Template customization complete!")
    print(f"📊 Processed {len(processed_files)} template files")
    print(f"📁 All customized files saved to: {output_dir}")
    
    # Generate summary report
    summary_file = Path(output_dir) / "customization_summary.md"
    with open(summary_file, 'w') as f:
        f.write(f"""# Template Customization Summary

## Configuration Used:
- Seller Name: {customizer.template_vars['seller_name']}
- Company: {customizer.template_vars['company_name']}
- Experience: {customizer.template_vars['years_experience']} years
- Credentials: {customizer.template_vars['mba_credential']}

## Files Generated:
{chr(10).join([f"- {Path(f).name}" for f in processed_files])}

## Next Steps:
1. Review all customized templates
2. Update user_config.json with your actual information
3. Re-run the script to regenerate with your details
4. Upload gig templates to Fiverr
5. Set up quick responses in Fiverr inbox

## Support:
If you need to modify any templates, edit the source files and re-run this script.
""")
    
    print(f"📋 Summary report saved to: {summary_file}")

if __name__ == "__main__":
    main()

