#!/usr/bin/env python3
"""
Comprehensive KPI Framework Demo for Managed Service Cloud Operations
Based on the comprehensive framework document
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Managed Service Cloud Operations KPI Framework",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Atos Cloud Services Brand Style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600;700&display=swap');

.stApp {
    font-family: 'Source Sans Pro', sans-serif;
    background-color: #FFFFFF;
}

.atos-card {
    background: #FFFFFF;
    border: 1px solid #E1E5E9;
    padding: 2rem;
    border-radius: 4px;
    margin: 1rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.atos-metric {
    background: #FFFFFF;
    border: 1px solid #E1E5E9;
    padding: 2rem;
    border-radius: 4px;
    margin: 0.5rem 0;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

.atos-primary {
    background: #0052CC;
    color: white;
    padding: 1.5rem;
    border-radius: 4px;
    margin: 1rem 0;
}

.atos-secondary {
    background: #F4F5F7;
    border: 1px solid #E1E5E9;
    padding: 2rem;
    border-radius: 4px;
    margin: 1rem 0;
}

.atos-accent {
    background: #FF6900;
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 4px;
    font-weight: 600;
}

h1 {
    color: #0052CC;
    font-weight: 700;
    font-size: 2.5rem;
}

h2 {
    color: #0052CC;
    font-weight: 600;
    font-size: 1.8rem;
}

h3 {
    color: #2C3E50;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

class FrameworkSimulator:
    def __init__(self):
        self.base_time = datetime.now()
        
    def get_kpi_performance(self):
        """Simulate KPI performance based on framework targets"""
        return {
            # Cost Optimization & Financial Management
            'tco_reduction': np.random.uniform(10, 15),
            'cloud_optimization': np.random.uniform(85, 95),
            'vendor_savings': np.random.uniform(5, 10),
            
            # Operational Efficiency & Automation
            'automation_coverage': np.random.uniform(80, 95),
            'mttr_hours': np.random.uniform(2, 4),
            'service_availability': np.random.uniform(99.9, 99.99),
            'change_success_rate': np.random.uniform(95, 99),
            
            # Security & Compliance
            'security_compliance': np.random.uniform(95, 99),
            'vulnerability_patching': np.random.uniform(24, 72),
            'incident_response': np.random.uniform(0.5, 1),
            
            # Service Delivery & Customer Experience
            'customer_satisfaction': np.random.uniform(4.5, 5.0),
            'sla_compliance': np.random.uniform(99, 100),
            'first_contact_resolution': np.random.uniform(75, 90),
            'time_to_market': np.random.uniform(20, 35),
            
            # Innovation & Technology Integration
            'ai_integration_score': np.random.uniform(60, 80),
            'data_analytics_utilization': np.random.uniform(80, 95),
            'innovation_velocity': np.random.uniform(2, 4),
            'tech_modernization': np.random.uniform(70, 85),
            
            # Continuous Improvement & Analytics
            'predictive_accuracy': np.random.uniform(85, 95),
            'root_cause_resolution': np.random.uniform(90, 98),
            'event_correlation': np.random.uniform(60, 80),
            'process_improvements': np.random.uniform(5, 8)
        }
    
    def calculate_revenue_impact(self, kpis):
        """Calculate revenue impact based on framework analysis"""
        return {
            'cost_reduction_impact': kpis['tco_reduction'] * 2.5 + kpis['cloud_optimization'] * 0.3,
            'delivery_efficiency': kpis['automation_coverage'] * 0.4 + kpis['change_success_rate'] * 0.2,
            'customer_retention': (kpis['customer_satisfaction'] - 4.0) * 25 + kpis['sla_compliance'] * 0.5,
            'innovation_premium': kpis['ai_integration_score'] * 0.5 + kpis['innovation_velocity'] * 8,
            'operational_excellence': kpis['service_availability'] * 0.8 + kpis['predictive_accuracy'] * 0.3
        }

def create_outcome_overview():
    """Create overview of 5 key outcomes"""
    outcomes = [
        {
            "title": "Cost Reduction & Vendor Management",
            "description": "Drive 10-15% TCO reduction through standardisation and automation",
            "kpis": ["TCO Reduction %", "Cloud Spend Optimization", "Vendor Cost Savings"],
            "target": "$25-40M annual savings"
        },
        {
            "title": "Security, Compliance & Risk Management", 
            "description": "Implement CI controls for data security and regulatory compliance",
            "kpis": ["Security Compliance Score", "Vulnerability Patching", "Incident Response"],
            "target": ">95% compliance rate"
        },
        {
            "title": "Strategic Alignment & Service Delivery",
            "description": "Ensure infrastructure delivery aligns with strategic objectives",
            "kpis": ["Customer Satisfaction", "SLA Compliance", "Time to Market"],
            "target": ">90% customer satisfaction"
        },
        {
            "title": "Cloud/Data/AI Synergies & Innovation",
            "description": "Realise synergies between Cloud, Data, and AI for competitive advantage",
            "kpis": ["AI Integration Score", "Data Analytics Utilization", "Innovation Velocity"],
            "target": "25-40% revenue premium"
        },
        {
            "title": "Continuous Improvement & Analytics",
            "description": "Drive improvement through predictive analytics and automation",
            "kpis": ["Predictive Analytics Accuracy", "Root Cause Resolution", "Event Correlation"],
            "target": "20-50% efficiency gains"
        }
    ]
    
    return outcomes

def create_maturity_comparison():
    """Create visually striking traditional vs modern KPI comparison"""
    # Create side-by-side comparison cards instead of charts
    return None  # Will be handled in main function with custom HTML

def create_ai_impact_analysis():
    """Create AI impact visualization"""
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Positive AI Impact (Successful Implementations)', 'Negative AI Impact (Poor Implementations)'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    # Positive impacts
    positive_metrics = ['Sales Forecasting', 'Customer Acquisition', 'Operational Efficiency', 'Decision Speed']
    positive_values = [50, 25, 22, 60]
    
    fig.add_trace(
        go.Bar(x=positive_metrics, y=positive_values, name='Improvement %', 
               marker_color='lightgreen'),
        row=1, col=1
    )
    
    # Negative impacts
    negative_metrics = ['Project Failures', 'Zero ROI Rate', 'Quality Issues', 'Cost Overruns']
    negative_values = [85, 42, 60, 70]
    
    fig.add_trace(
        go.Bar(x=negative_metrics, y=negative_values, name='Failure Rate %',
               marker_color='lightcoral'),
        row=1, col=2
    )
    
    fig.update_layout(height=400, showlegend=False)
    return fig

def main():
    simulator = FrameworkSimulator()
    
    # Sidebar navigation
    st.sidebar.title("☁️ Managed Service Cloud Operations KPI Framework")
    page = st.sidebar.selectbox("Navigate", [
        "Executive Summary", 
        "5 Key Outcomes",
        "KPI Performance Dashboard", 
        "Revenue Lifecycle Integration",
        "Traditional vs Modern KPIs",
        "AI Impact Analysis",
        "Implementation Roadmap"
    ])
    
    if page == "Executive Summary":
        st.title("📊 Comprehensive KPI Framework for Managed Service Cloud Operations")
        st.markdown("*From Strategy to Revenue Impact*")
        
        # Key findings
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="atos-metric">
                <h3 style="color: #0066CC; margin: 0 0 0.5rem 0;">28 Strategic KPIs</h3>
                <p style="color: #6B7280; margin: 0;">Across 7 categories driving 5 key outcomes</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="atos-metric">
                <h3 style="color: #0066CC; margin: 0 0 0.5rem 0;">10-50% Revenue Impact</h3>
                <p style="color: #6B7280; margin: 0;">Improvement in key financial metrics</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="atos-metric">
                <h3 style="color: #0066CC; margin: 0 0 0.5rem 0;">20-50% AI Enhancement</h3>
                <p style="color: #6B7280; margin: 0;">When properly governed and implemented</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="atos-metric">
                <h3 style="color: #0066CC; margin: 0 0 0.5rem 0;">$70-105M Impact</h3>
                <p style="color: #6B7280; margin: 0;">Cumulative revenue lifecycle value</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Interactive Framework Structure
        st.subheader("🎯 Interactive Framework Structure")
        st.markdown("*Click on any category to explore its KPIs*")
        
        # KPI data from the framework document
        kpi_categories = {
            "Cost Optimization & Financial Management": {
                "kpis": [
                    {"name": "Total Cost of Ownership (TCO) Reduction %", "target": "10-15% annual reduction", "impact": "Primary metric for cost reduction success"},
                    {"name": "Cost per Service/Application", "target": "Downward trend month-over-month", "impact": "Enables granular cost tracking"},
                    {"name": "Cloud Spend Optimization Rate", "target": ">85% of resources optimized", "impact": "10-20% service margin improvement"},
                    {"name": "Vendor Cost Savings", "target": "5-10% savings on renewals", "impact": "Direct margin improvement"}
                ],
                "maturity": "High", "impact": "Very High", "color": "#e74c3c"
            },
            "Operational Efficiency & Automation": {
                "kpis": [
                    {"name": "Automation Coverage %", "target": ">80% of routine processes", "impact": "15-25% delivery cost reduction"},
                    {"name": "Mean Time to Recovery (MTTR)", "target": "<4 hours for critical services", "impact": "Prevents SLA penalties"},
                    {"name": "Service Availability/Uptime %", "target": "99.9% for critical services", "impact": "Maintains 100% contractual revenue"},
                    {"name": "Change Success Rate", "target": ">95% success rate", "impact": "Prevents cost overruns"}
                ],
                "maturity": "High", "impact": "High", "color": "#3498db"
            },
            "Security & Compliance": {
                "kpis": [
                    {"name": "Security Compliance Score", "target": ">95% compliance", "impact": "Prevents compliance penalties"},
                    {"name": "Vulnerability Patching Time", "target": "<72 hours for critical", "impact": "Maintains customer trust"},
                    {"name": "Security Incident Response Time", "target": "<1 hour for high-severity", "impact": "Prevents service disruptions"},
                    {"name": "Policy Violation Rate", "target": "<2% violation rate", "impact": "Avoids penalty costs"}
                ],
                "maturity": "High", "impact": "Medium", "color": "#9b59b6"
            },
            "Service Delivery & Customer Experience": {
                "kpis": [
                    {"name": "Customer Satisfaction Score (CSAT)", "target": ">4.5/5.0 or >90%", "impact": "85%+ renewal rate correlation"},
                    {"name": "Service Level Agreement (SLA) Compliance", "target": ">99% compliance", "impact": "15-25% account growth opportunities"},
                    {"name": "First Contact Resolution Rate", "target": ">75% first contact", "impact": "20-30% support cost reduction"},
                    {"name": "Time to Market for New Services", "target": "30% reduction year-over-year", "impact": "15-30% sales velocity improvement"}
                ],
                "maturity": "Medium", "impact": "Very High", "color": "#2ecc71"
            },
            "Innovation & Technology Integration": {
                "kpis": [
                    {"name": "Cloud, Data & AI Integration Score", "target": ">60% of services integrated", "impact": "25-40% higher revenue per customer"},
                    {"name": "Data Analytics Utilization Rate", "target": ">80% of operational decisions", "impact": "Enables predictive capabilities"},
                    {"name": "Innovation Pipeline Velocity", "target": "2-3 major initiatives per quarter", "impact": "10-25% premium pricing"},
                    {"name": "Technology Modernization Index", "target": ">70% modern technology adoption", "impact": "Cost reduction and capability enhancement"}
                ],
                "maturity": "Low", "impact": "Very High", "color": "#f39c12"
            },
            "Continuous Improvement & Analytics": {
                "kpis": [
                    {"name": "Predictive Analytics Accuracy", "target": ">85% prediction accuracy", "impact": "10-15% reduction in unplanned costs"},
                    {"name": "Root Cause Analysis Resolution Rate", "target": ">90% of major incidents", "impact": "Prevents recurring customer issues"},
                    {"name": "Process Improvement Implementation Rate", "target": "5+ improvements per quarter", "impact": "Cumulative efficiency gains"},
                    {"name": "Event Correlation Effectiveness", "target": ">60% event correlation", "impact": "15-20% operational overhead reduction"}
                ],
                "maturity": "Low", "impact": "Medium", "color": "#e67e22"
            },
            "Resource & Performance Management": {
                "kpis": [
                    {"name": "Resource Utilization Rate", "target": "70-85% optimal utilization", "impact": "10-20% revenue per consultant increase"},
                    {"name": "Multi-Cloud Management Efficiency", "target": "Industry benchmark +10%", "impact": "20-30% working capital reduction"},
                    {"name": "Deployment Frequency", "target": "Daily for non-critical, weekly for critical", "impact": "30-45 day cash collection improvement"},
                    {"name": "Infrastructure Standardization Rate", "target": ">90% standardization", "impact": "Reduces costs while improving reliability"}
                ],
                "maturity": "Medium", "impact": "High", "color": "#1abc9c"
            }
        }
        
        # Initialize session state
        if 'selected_category' not in st.session_state:
            st.session_state.selected_category = list(kpi_categories.keys())[0]
        
        # Display category cards in proper grid layout
        category_list = list(kpi_categories.items())
        
        # First row: 4 categories
        cols1 = st.columns(4)
        for i in range(min(4, len(category_list))):
            cat_name, cat_data = category_list[i]
            with cols1[i]:
                if st.button(f"{cat_name.split(' &')[0]}", key=f"btn_{i}", use_container_width=True):
                    st.session_state.selected_category = cat_name
                    st.rerun()
                
                is_selected = cat_name == st.session_state.selected_category
                border_style = "border: 3px solid #FFD700;" if is_selected else ""
                color = cat_data['color']
                
                card_class = "atos-card" + (" selected" if is_selected else "")
                st.markdown(f"""
                <div class="{card_class}" style="{border_style}">
                    <h3 style="color: #0052CC; margin: 0 0 1rem 0; text-align: center; font-size: 1.1em;">{cat_name.split(' &')[0]}</h3>
                    <div style="text-align: center; margin: 1.5rem 0;">
                        <div style="background: #0052CC; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; font-size: 1.8em; font-weight: bold;">{len(cat_data['kpis'])}</div>
                        <p style="margin: 0; color: #6B7280; font-size: 0.9em;">Strategic KPIs</p>
                    </div>
                    <div style="display: flex; justify-content: space-between; padding-top: 1rem; border-top: 1px solid #E1E5E9; font-size: 0.8em; color: #6B7280;">
                        <span>Maturity: <strong>{cat_data['maturity']}</strong></span>
                        <span>Impact: <strong>{cat_data['impact']}</strong></span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Second row: remaining categories (centered)
        if len(category_list) > 4:
            st.markdown("<br>", unsafe_allow_html=True)
            remaining = len(category_list) - 4
            cols2 = st.columns([1] + [2]*remaining + [1])  # Center the remaining cards
            
            for i in range(4, len(category_list)):
                cat_name, cat_data = category_list[i]
                with cols2[i-3]:  # Offset by 1 for centering
                    if st.button(f"{cat_name.split(' &')[0]}", key=f"btn_{i}", use_container_width=True):
                        st.session_state.selected_category = cat_name
                        st.rerun()
                    
                    is_selected = cat_name == st.session_state.selected_category
                    border_style = "border: 3px solid #FFD700;" if is_selected else ""
                    color = cat_data['color']
                    
                    card_class = "atos-card" + (" selected" if is_selected else "")
                    st.markdown(f"""
                    <div class="{card_class}" style="{border_style}">
                        <h3 style="color: #0052CC; margin: 0 0 1rem 0; text-align: center; font-size: 1.1em;">{cat_name.split(' &')[0]}</h3>
                        <div style="text-align: center; margin: 1.5rem 0;">
                            <div style="background: #0052CC; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; font-size: 1.8em; font-weight: bold;">{len(cat_data['kpis'])}</div>
                            <p style="margin: 0; color: #6B7280; font-size: 0.9em;">Strategic KPIs</p>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding-top: 1rem; border-top: 1px solid #E1E5E9; font-size: 0.8em; color: #6B7280;">
                            <span>Maturity: <strong>{cat_data['maturity']}</strong></span>
                            <span>Impact: <strong>{cat_data['impact']}</strong></span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        # Display selected category details
        cat_data = kpi_categories[st.session_state.selected_category]
        
        st.markdown(f"### 📊 {st.session_state.selected_category} - Detailed KPIs")
        
        for i, kpi in enumerate(cat_data['kpis']):
            with st.expander(f"KPI {i+1}: {kpi['name']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Target:** {kpi['target']}")
                with col2:
                    st.markdown(f"**Business Impact:** {kpi['impact']}")
    
    elif page == "5 Key Outcomes":
        st.title("🎯 Five Key Business Outcomes")
        st.markdown("*Strategic objectives driving the Managed Service Cloud Operations role*")
        
        outcomes = create_outcome_overview()
        
        # Display outcomes in Atos brand style
        for i, outcome in enumerate(outcomes):
            st.markdown(f"""
            <div class="atos-secondary">
                <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                    <div style="background: #0052CC; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem;">{i+1}</div>
                    <h2 style="margin: 0; color: #0052CC; font-size: 1.5em;">{outcome['title']}</h2>
                </div>
                <p style="color: #2C3E50; font-size: 1.1em; line-height: 1.6; margin-bottom: 2rem;">{outcome['description']}</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                    <div>
                        <h4 style="color: #0052CC; margin-bottom: 1rem;">Key Performance Indicators</h4>
                        <ul style="color: #2C3E50; margin: 0; padding-left: 1.5rem;">
                            {''.join([f'<li style="margin-bottom: 0.5rem;">{kpi}</li>' for kpi in outcome['kpis']])}
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #0052CC; margin-bottom: 1rem;">Target Impact</h4>
                        <div class="atos-accent" style="text-align: center;">
                            <span style="font-size: 1.3em; font-weight: bold;">{outcome['target']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    elif page == "KPI Performance Dashboard":
        st.title("📈 Live KPI Performance Dashboard")
        st.markdown("*Real-time monitoring of 28 strategic KPIs*")
        
        kpis = simulator.get_kpi_performance()
        revenue_impact = simulator.calculate_revenue_impact(kpis)
        
        # Top-level metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("TCO Reduction", f"{kpis['tco_reduction']:.1f}%", 
                     delta=f"{kpis['tco_reduction']-12.5:.1f}% vs target")
        
        with col2:
            st.metric("Service Availability", f"{kpis['service_availability']:.2f}%",
                     delta=f"{kpis['service_availability']-99.9:.2f}%")
        
        with col3:
            st.metric("Customer Satisfaction", f"{kpis['customer_satisfaction']:.1f}/5.0",
                     delta=f"{kpis['customer_satisfaction']-4.5:.1f} vs target")
        
        with col4:
            st.metric("AI Integration", f"{kpis['ai_integration_score']:.0f}%",
                     delta=f"{kpis['ai_integration_score']-60:.0f}% vs target")
        
        with col5:
            st.metric("Automation Coverage", f"{kpis['automation_coverage']:.0f}%",
                     delta=f"{kpis['automation_coverage']-80:.0f}% vs target")
        
        # Category performance
        st.subheader("📊 Performance by Category")
        
        categories = {
            'Cost Optimization': [kpis['tco_reduction'], kpis['cloud_optimization'], kpis['vendor_savings']],
            'Operational Efficiency': [kpis['automation_coverage'], 100-kpis['mttr_hours']*25, kpis['service_availability']],
            'Security & Compliance': [kpis['security_compliance'], 100-kpis['vulnerability_patching'], 100-kpis['incident_response']*100],
            'Service Delivery': [kpis['customer_satisfaction']*20, kpis['sla_compliance'], kpis['first_contact_resolution']],
            'Innovation & Tech': [kpis['ai_integration_score'], kpis['data_analytics_utilization'], kpis['tech_modernization']],
            'Continuous Improvement': [kpis['predictive_accuracy'], kpis['root_cause_resolution'], kpis['event_correlation']]
        }
        
        category_scores = {cat: np.mean(vals) for cat, vals in categories.items()}
        
        fig = go.Figure(data=[
            go.Bar(x=list(category_scores.keys()), y=list(category_scores.values()),
                   marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3'])
        ])
        
        fig.update_layout(
            title="KPI Category Performance Scores",
            yaxis_title="Performance Score (%)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Revenue impact summary
        st.subheader("💰 Revenue Impact Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            impact_data = pd.DataFrame({
                'Impact Area': list(revenue_impact.keys()),
                'Value ($M)': list(revenue_impact.values())
            })
            
            fig = px.pie(impact_data, values='Value ($M)', names='Impact Area',
                        title="Revenue Impact Distribution")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            total_impact = sum(revenue_impact.values())
            st.markdown(f"""
            ### 🎯 Total Revenue Impact
            **${total_impact:.1f}M Annual Value**
            
            **Breakdown:**
            - Cost Reduction: ${revenue_impact['cost_reduction_impact']:.1f}M
            - Delivery Efficiency: ${revenue_impact['delivery_efficiency']:.1f}M  
            - Customer Retention: ${revenue_impact['customer_retention']:.1f}M
            - Innovation Premium: ${revenue_impact['innovation_premium']:.1f}M
            - Operational Excellence: ${revenue_impact['operational_excellence']:.1f}M
            """)
    
    elif page == "Revenue Lifecycle Integration":
        st.title("🔄 Revenue Lifecycle Integration")
        st.markdown("*How KPIs drive value across the customer journey*")
        
        # Revenue stages with KPI mapping
        stages = [
            {
                "name": "Order Entry & Sales",
                "kpis": ["Time to Market", "Innovation Velocity", "Customer Satisfaction"],
                "impact": "15-30% sales velocity improvement",
                "mechanism": "Faster service development creates competitive advantage"
            },
            {
                "name": "Project Delivery", 
                "kpis": ["Automation Coverage", "Resource Utilization", "Change Success Rate"],
                "impact": "15-25% cost reduction, 20-30% faster delivery",
                "mechanism": "Operational excellence improves margins and timing"
            },
            {
                "name": "Service Operations",
                "kpis": ["Service Availability", "First Contact Resolution", "Cloud Optimization"],
                "impact": "Maintains 100% contracted revenue",
                "mechanism": "Reliability protects recurring revenue streams"
            },
            {
                "name": "Customer Expansion",
                "kpis": ["Customer Satisfaction", "AI Integration", "SLA Compliance"], 
                "impact": "85%+ renewal rates, 25-40% revenue premium",
                "mechanism": "Excellence drives retention and growth"
            }
        ]
        
        for i, stage in enumerate(stages):
            st.markdown(f"""
            <div class="atos-secondary">
                <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                    <div style="background: #0052CC; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem;">{i+1}</div>
                    <h3 style="margin: 0; color: #0052CC;">Stage {i+1}: {stage['name']}</h3>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 1.5rem 0;">
                    <div>
                        <h4 style="color: #0052CC; margin-bottom: 1rem;">Key KPIs</h4>
                        <p style="color: #2C3E50;">{', '.join(stage['kpis'])}</p>
                    </div>
                    <div>
                        <h4 style="color: #0052CC; margin-bottom: 1rem;">Revenue Impact</h4>
                        <div class="atos-accent" style="padding: 0.75rem; font-size: 0.9em;">{stage['impact']}</div>
                    </div>
                    <div>
                        <h4 style="color: #0052CC; margin-bottom: 1rem;">Mechanism</h4>
                        <p style="color: #2C3E50;">{stage['mechanism']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Cascade effects
        st.subheader("📈 Cascade Effects Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### ✅ Positive Cascade (Excellence Path)
            1. **Strong Sales KPIs** → High-quality project pipeline
            2. **Excellent Delivery** → Operational excellence foundation  
            3. **Superior Operations** → Customer expansion opportunities
            4. **Cumulative Impact:** 50-100% increase in customer lifetime value
            """)
        
        with col2:
            st.markdown("""
            ### ❌ Negative Cascade (Poor Performance Path)
            1. **Poor Sales KPIs** → Reduced deal flow and quality
            2. **Delivery Struggles** → Operational challenges
            3. **Service Issues** → Limited expansion and churn risk
            4. **Cumulative Impact:** 40-60% reduction in customer lifetime value
            """)
    
    elif page == "Traditional vs Modern KPIs":
        st.title("⚖️ Traditional vs Modern KPI Analysis")
        st.markdown("*Understanding maturity levels and adoption barriers*")
        
        # Visual maturity comparison cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="atos-primary">
                <h2 style="text-align: center; margin-bottom: 2rem; color: white;">📊 TRADITIONAL KPIs</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.15); border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: white;">90%</h1>
                        <p style="margin: 0.5rem 0; color: white;">Adoption Rate</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.15); border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: white;">70%</h1>
                        <p style="margin: 0.5rem 0; color: white;">Business Impact</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.15); border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: white;">30%</h1>
                        <p style="margin: 0.5rem 0; color: white;">Complexity</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.15); border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: white;">85%</h1>
                        <p style="margin: 0.5rem 0; color: white;">ROI Speed</p>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 4px;">
                    <h3 style="color: white;">✅ ESTABLISHED & RELIABLE</h3>
                    <p style="color: white;">Industry standard, regulatory compliance, proven ROI</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="atos-secondary">
                <h2 style="text-align: center; margin-bottom: 2rem; color: #0052CC;">🚀 MODERN KPIs</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                    <div style="text-align: center; padding: 1rem; background: #FFFFFF; border: 1px solid #E1E5E9; border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: #0052CC;">20%</h1>
                        <p style="margin: 0.5rem 0; color: #2C3E50;">Adoption Rate</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: #FFFFFF; border: 1px solid #E1E5E9; border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: #0052CC;">95%</h1>
                        <p style="margin: 0.5rem 0; color: #2C3E50;">Business Impact</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: #FFFFFF; border: 1px solid #E1E5E9; border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: #0052CC;">90%</h1>
                        <p style="margin: 0.5rem 0; color: #2C3E50;">Complexity</p>
                    </div>
                    <div style="text-align: center; padding: 1rem; background: #FFFFFF; border: 1px solid #E1E5E9; border-radius: 4px;">
                        <h1 style="margin: 0; font-size: 3em; color: #0052CC;">60%</h1>
                        <p style="margin: 0.5rem 0; color: #2C3E50;">ROI Speed</p>
                    </div>
                </div>
                <div class="atos-accent" style="text-align: center; margin-top: 2rem; padding: 1rem;">
                    <h3 style="color: white;">⚡ COMPETITIVE ADVANTAGE</h3>
                    <p style="color: white;">AI-driven, predictive, high-impact differentiation</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Traditional KPIs (90%+ Adoption)")
            traditional_kpis = [
                "Mean Time to Recovery (MTTR)",
                "Service Availability/Uptime %", 
                "Customer Satisfaction Score",
                "First Contact Resolution Rate",
                "SLA Compliance",
                "Change Success Rate",
                "Total Cost of Ownership (TCO)",
                "Security Compliance Score"
            ]
            
            for kpi in traditional_kpis:
                st.markdown(f"✅ {kpi}")
            
            st.markdown("""
            **Why These Exist:**
            - Regulatory and compliance requirements
            - Industry standard practices (ITIL/ITSM)
            - Contractual obligations
            - Basic operational management needs
            """)
        
        with col2:
            st.subheader("🚀 Modern KPIs (<20% Adoption)")
            modern_kpis = [
                "Predictive Analytics Accuracy",
                "Event Correlation Effectiveness", 
                "Cloud, Data & AI Integration Score",
                "Technology Modernization Index",
                "Data Analytics Utilization Rate",
                "Deployment Frequency",
                "Cloud Spend Optimization Rate",
                "Multi-Cloud Management Efficiency"
            ]
            
            for kpi in modern_kpis:
                st.markdown(f"🔄 {kpi}")
            
            st.markdown("""
            **Adoption Barriers:**
            - High technical complexity
            - Significant technology investment
            - Cultural transformation needs
            - Lack of industry standards
            - Integration complexity
            """)
    
    elif page == "AI Impact Analysis":
        st.title("🤖 AI Impact on KPI Performance")
        st.markdown("*The 58% vs 42% divide in AI implementation success*")
        
        # Enhanced AI impact with battle-style visualization
        st.markdown("""
        <div class="atos-secondary">
            <h2 style="text-align: center; margin-bottom: 3rem; color: #0052CC;">⚔️ AI IMPLEMENTATION SUCCESS ANALYSIS</h2>
            <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 2rem; align-items: center;">
                <div style="text-align: center;">
                    <div class="atos-primary" style="padding: 2rem; margin-bottom: 1rem;">
                        <h1 style="margin: 0; font-size: 4em; color: white;">58%</h1>
                        <h3 style="margin: 0.5rem 0; color: white;">SUCCESS RATE</h3>
                    </div>
                    <h3 style="color: #0052CC;">✅ SUCCESS FACTORS</h3>
                    <ul style="text-align: left; margin: 1rem 0; color: #2C3E50;">
                        <li>50% Sales Forecasting Improvement</li>
                        <li>25% Customer Acquisition Cost Reduction</li>
                        <li>60% Decision Speed Increase</li>
                        <li>Business-First Approach</li>
                    </ul>
                </div>
                <div style="text-align: center; font-size: 3em; color: #FF6900;">
                    ⚡VS⚡
                </div>
                <div style="text-align: center;">
                    <div class="atos-accent" style="padding: 2rem; margin-bottom: 1rem;">
                        <h1 style="margin: 0; font-size: 4em; color: white;">42%</h1>
                        <h3 style="margin: 0.5rem 0; color: white;">FAILURE RATE</h3>
                    </div>
                    <h3 style="color: #FF6900;">❌ FAILURE PATTERNS</h3>
                    <ul style="text-align: left; margin: 1rem 0; color: #2C3E50;">
                        <li>85% Projects Never Reach Production</li>
                        <li>42% See Zero ROI</li>
                        <li>Quality & Bias Issues</li>
                        <li>Technology-First Mistakes</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Success vs failure factors
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### ✅ Success Factors (58% of implementations)
            
            **Positive AI Impact:**
            - Sales Forecasting: Up to 50% accuracy improvement
            - Customer Acquisition: 20-30% cost reduction
            - Operational Efficiency: 20-25% productivity gains
            - Decision Speed: 50-70% faster cycles
            
            **Key Success Patterns:**
            - Business-centric approach focusing on outcomes
            - External partnerships with AI specialists
            - Comprehensive governance with multiple metrics
            - Gradual implementation with continuous monitoring
            """)
        
        with col2:
            st.markdown("""
            ### ❌ Failure Patterns (42% of implementations)
            
            **Negative AI Impact:**
            - Project Failures: 80-95% never reach production
            - Zero ROI: 42% of enterprises see no return
            - Quality Issues: Increased errors and bias
            - Cost Overruns: Significant unexpected expenses
            
            **Common Failure Causes:**
            - Technology-first mindset without business alignment
            - Internal development without sufficient expertise
            - Single metric optimization (Goodhart's Law)
            - Poor change management and preparation
            """)
        
        # Strategic recommendations
        st.subheader("🎯 Strategic AI Recommendations for Managed Service Cloud")
        
        recommendations = {
            "Immediate Priorities (High Success)": [
                "Customer Service Automation - 30-50% FCR improvements",
                "Predictive Analytics for Operations - 40-60% accuracy improvements", 
                "Cloud Cost Optimization - 10-20% spend optimization"
            ],
            "Medium-Term Opportunities (Moderate Risk)": [
                "Sales Process Enhancement - 15-35% conversion improvements",
                "Resource Utilization Optimization - 15-25% efficiency gains",
                "Automated Incident Response - 60-80% response time reductions"
            ],
            "High-Risk Areas (Proceed with Caution)": [
                "Complex Decision Automation - High bias and accuracy risks",
                "Custom AI Development - 67% failure rate vs vendor solutions",
                "Broad Organizational Transformation - 80-95% failure rates"
            ]
        }
        
        for category, items in recommendations.items():
            st.markdown(f"**{category}:**")
            for item in items:
                st.markdown(f"- {item}")
    
    elif page == "Implementation Roadmap":
        st.title("🗺️ Implementation Roadmap")
        st.markdown("*Phased approach to KPI framework deployment*")
        
        phases = [
            {
                "name": "Phase 1: Foundation",
                "duration": "0-6 months",
                "objectives": "Establish comprehensive KPI measurement capability",
                "priority_kpis": ["Customer Satisfaction Score", "Service Availability", "Resource Utilization Rate", "Security Compliance Score"],
                "success_criteria": "100% KPI data availability and accuracy"
            },
            {
                "name": "Phase 2: Optimization", 
                "duration": "6-18 months",
                "objectives": "Achieve industry-leading performance on traditional KPIs",
                "priority_kpis": ["Automation Coverage", "Cloud Spend Optimization", "Deployment Frequency", "Predictive Analytics Accuracy"],
                "success_criteria": "Traditional KPIs at industry benchmark +10%"
            },
            {
                "name": "Phase 3: Advanced Capabilities",
                "duration": "18+ months", 
                "objectives": "Achieve competitive differentiation through advanced KPIs",
                "priority_kpis": ["Cloud/Data/AI Integration Score", "Innovation Pipeline Velocity", "Technology Modernization Index", "Event Correlation Effectiveness"],
                "success_criteria": "All modern KPIs performing at target levels"
            },
            {
                "name": "Phase 4: Continuous Evolution",
                "duration": "Ongoing",
                "objectives": "Maintain competitive advantage through continuous improvement",
                "priority_kpis": ["Emerging Technology KPIs", "Market Leadership Metrics", "Global Scaling Indicators"],
                "success_criteria": "Sustained superior performance across all categories"
            }
        ]
        
        for i, phase in enumerate(phases):
            st.markdown(f"""
            <div class="atos-secondary">
                <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                    <div style="background: #0052CC; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem;">{i+1}</div>
                    <h3 style="margin: 0; color: #0052CC;">{phase['name']} ({phase['duration']})</h3>
                </div>
                <div style="margin-bottom: 1rem;">
                    <h4 style="color: #0052CC; margin-bottom: 0.5rem;">Objectives</h4>
                    <p style="color: #2C3E50; margin: 0;">{phase['objectives']}</p>
                </div>
                <div style="margin-bottom: 1rem;">
                    <h4 style="color: #0052CC; margin-bottom: 0.5rem;">Priority KPIs</h4>
                    <p style="color: #2C3E50; margin: 0;">{', '.join(phase['priority_kpis'])}</p>
                </div>
                <div>
                    <h4 style="color: #0052CC; margin-bottom: 0.5rem;">Success Criteria</h4>
                    <div class="atos-accent" style="padding: 0.75rem; font-size: 0.9em;">{phase['success_criteria']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Enhanced investment priorities with interactive elements
        st.subheader("💰 Investment Priorities by ROI Timeline")
        
        # Create investment priority matrix
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 20px; color: white; margin: 2rem 0;">
            <h3 style="text-align: center; margin-bottom: 2rem;">🎯 STRATEGIC INVESTMENT MATRIX</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 10px; text-align: center;">
                    <h4 style="color: #2ecc71;">🚀 IMMEDIATE (0-6M)</h4>
                    <p><strong>25% ROI</strong></p>
                    <p>Automation Coverage<br>Resource Utilization<br>Cloud Optimization</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 10px; text-align: center;">
                    <h4 style="color: #f39c12;">⚡ MEDIUM (6-18M)</h4>
                    <p><strong>50% ROI</strong></p>
                    <p>Predictive Analytics<br>Service Management<br>Innovation Pipeline</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 10px; text-align: center;">
                    <h4 style="color: #e74c3c;">🎖️ ADVANCED (18M+)</h4>
                    <p><strong>70% ROI</strong></p>
                    <p>AI Decision Support<br>Technology Integration<br>Process Automation</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Skip the chart for now - focus on the visual matrix above
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### 📋 Framework Summary
    - **28 Strategic KPIs** across 7 categories
    - **5 Key Business Outcomes** alignment
    - **$70-105M** revenue lifecycle impact
    - **4-Phase** implementation roadmap
    """)

if __name__ == "__main__":
    main()