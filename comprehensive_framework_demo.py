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

# Custom CSS - Atos Brand Style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600;700&display=swap');

.stApp {
    font-family: 'Source Sans Pro', sans-serif;
    background-color: #FFFFFF;
}

.atos-card {
    background: #FFFFFF;
    border: 1px solid #E5E5E5;
    padding: 2rem;
    border-radius: 0;
    margin: 1rem 0;
    box-shadow: none;
}

.atos-metric {
    background: #FFFFFF;
    border: 1px solid #E5E5E5;
    padding: 2rem;
    border-radius: 0;
    margin: 0.5rem 0;
    text-align: center;
    box-shadow: none;
}

.atos-primary {
    background: #0066CC;
    color: white;
    padding: 2rem;
    border-radius: 0;
    margin: 1rem 0;
}

.atos-secondary {
    background: #F8F9FA;
    border: 1px solid #E5E5E5;
    padding: 2rem;
    border-radius: 0;
    margin: 1rem 0;
}

.atos-accent {
    background: #FF6900;
    color: white;
    padding: 1.5rem 2rem;
    border-radius: 0;
    font-weight: 600;
}

.atos-dark {
    background: #2C3E50;
    color: white;
    padding: 2rem;
    border-radius: 0;
    margin: 1rem 0;
}

h1 {
    color: #0066CC;
    font-weight: 700;
    font-size: 2.5rem;
}

h2 {
    color: #0066CC;
    font-weight: 600;
    font-size: 1.8rem;
}

h3 {
    color: #2C3E50;
    font-weight: 600;
}

.metric-box {
    background: #FFFFFF;
    border: 1px solid #E5E5E5;
    padding: 1.5rem;
    margin: 0.5rem 0;
    text-align: center;
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
        "KPI Framework", 
        "Revenue Lifecycle Integration",
        "5 Key Outcomes",
        "AI Impact Analysis",
        "KPI Performance Dashboard", 
        "Traditional vs Modern KPIs",
        "Implementation Roadmap",
        "Strategic Story"
    ])
    
    if page == "KPI Framework":
        st.title("📊 KPI Framework for Managed Service Cloud Operations")
        st.markdown("*28 Strategic KPIs across 7 categories driving 5 key outcomes*")
        
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
                    <h3 style="color: #1A1A1A; margin: 0 0 1rem 0; text-align: center; font-size: 1.1em;">{cat_name.split(' &')[0]}</h3>
                    <div style="text-align: center; margin: 1.5rem 0;">
                        <div style="background: #0070F3; color: white; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; font-size: 1.8em; font-weight: bold;">{len(cat_data['kpis'])}</div>
                        <p style="margin: 0; color: #666666; font-size: 0.9em;">Strategic KPIs</p>
                    </div>
                    <div style="display: flex; justify-content: space-between; padding-top: 1rem; border-top: 1px solid #E5E5E5; font-size: 0.8em; color: #666666;">
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
    
    elif page == "Strategic Story":
        st.title("📖 The Strategic Transformation Story")
        st.markdown("*From Managed Service Cloud Operations KPI Metrics to Business Excellence: An Interactive Journey*")
        
        # Initialize story progress
        if 'story_step' not in st.session_state:
            st.session_state.story_step = 0
        
        # Story progress indicator
        story_steps = ["🎯 KPI Foundation", "🔄 Lifecycle Impact", "🏆 Business Outcomes", "🤖 AI Enhancement"]
        
        # Progress bar
        progress_cols = st.columns(4)
        for i, step in enumerate(story_steps):
            with progress_cols[i]:
                if i <= st.session_state.story_step:
                    st.markdown(f"<div class='atos-primary' style='text-align: center; margin: 0.5rem 0;'><strong style='color: white;'>{step}</strong></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='atos-secondary' style='text-align: center; margin: 0.5rem 0; color: #666666;'>{step}</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Story Step 0: KPI Foundation
        if st.session_state.story_step >= 0:
            st.markdown("## 🎯 The Foundation - Strategic KPI Framework")
            st.markdown("*Our journey begins with 28 strategic KPIs that form the backbone of operational excellence...*")
            
            # All 7 KPI categories with complete data
            kpi_story_data = {
                "Cost Optimization": {"kpis": 4, "impact": "10-15% efficiency gains", "color": "#FF6B6B", "details": ["TCO Reduction %", "Cost per Service", "Cloud Spend Optimization", "Vendor Cost Savings"]},
                "Operational Excellence": {"kpis": 4, "impact": "99.9% reliability targets", "color": "#4ECDC4", "details": ["Automation Coverage %", "Mean Time to Recovery", "Service Availability", "Change Success Rate"]},
                "Security & Compliance": {"kpis": 4, "impact": ">95% compliance achievement", "color": "#45B7D1", "details": ["Security Compliance Score", "Vulnerability Patching Time", "Incident Response Time", "Policy Violation Rate"]},
                "Service Delivery": {"kpis": 4, "impact": ">90% customer satisfaction", "color": "#96CEB4", "details": ["Customer Satisfaction Score", "SLA Compliance", "First Contact Resolution", "Time to Market"]},
                "Innovation & Technology": {"kpis": 4, "impact": "25-40% capability enhancement", "color": "#FECA57", "details": ["AI Integration Score", "Data Analytics Utilization", "Innovation Pipeline Velocity", "Technology Modernization"]},
                "Continuous Improvement": {"kpis": 4, "impact": "20-50% process optimization", "color": "#FF9FF3", "details": ["Predictive Analytics Accuracy", "Root Cause Resolution", "Process Improvement Rate", "Event Correlation"]},
                "Resource Management": {"kpis": 4, "impact": "70-85% utilization efficiency", "color": "#1ABC9C", "details": ["Resource Utilization Rate", "Multi-Cloud Management", "Deployment Frequency", "Infrastructure Standardization"]}
            }
            
            # Display all 7 categories in grid
            kpi_cols1 = st.columns(4)
            kpi_cols2 = st.columns(3)
            
            for i, (category, data) in enumerate(kpi_story_data.items()):
                col = kpi_cols1[i] if i < 4 else kpi_cols2[i-4]
                with col:
                    with st.expander(f"{category} ({data['kpis']} KPIs)"):
                        st.markdown(f"**Impact:** {data['impact']}")
                        st.markdown("**KPIs:**")
                        for kpi in data['details']:
                            st.markdown(f"• {kpi}")
            
            if st.session_state.story_step == 0:
                if st.button("▶️ Continue Story: See How These KPIs Drive Lifecycle Improvements", use_container_width=True):
                    st.session_state.story_step = 1
                    st.rerun()
        
        # Story Step 1: Lifecycle Impact
        if st.session_state.story_step >= 1:
            st.markdown("## 🔄 The Journey - Revenue Lifecycle Transformation")
            st.markdown("*These KPIs now drive measurable improvements across every stage of our customer journey...*")
            
            # Interactive lifecycle flow with detailed KPI mappings
            lifecycle_stages = [
                {
                    "name": "Order Entry & Sales", "icon": "🎯", "improvement": "30% faster time-to-market", "color": "#FF6B6B",
                    "kpis": ["Time to Market for New Services: 30% reduction", "Innovation Pipeline Velocity: 2-3 initiatives/quarter", "Customer Satisfaction: >4.5/5.0"],
                    "mechanism": "Faster service development creates competitive advantage, reduces time to first payment by 30-60 days"
                },
                {
                    "name": "Project Delivery", "icon": "⚡", "improvement": "25% efficiency gains", "color": "#4ECDC4",
                    "kpis": ["Automation Coverage: >80% processes", "Resource Utilization: 70-85% optimal", "Change Success Rate: >95% success"],
                    "mechanism": "Operational excellence translates to higher margins, faster cash collection, improved customer satisfaction"
                },
                {
                    "name": "Service Operations", "icon": "🛡️", "improvement": "99.9% reliability", "color": "#45B7D1",
                    "kpis": ["Service Availability: 99.9% uptime", "First Contact Resolution: >75% first contact", "Cloud Optimization: >85% optimized"],
                    "mechanism": "Operational excellence maintains revenue base while reducing costs, creating sustainable competitive advantages"
                },
                {
                    "name": "Customer Expansion", "icon": "📈", "improvement": "85% retention rates", "color": "#FECA57",
                    "kpis": ["Customer Satisfaction: >4.5/5.0", "AI Integration Score: >60% integrated", "SLA Compliance: >99% compliance"],
                    "mechanism": "Satisfied customers become sources of predictable growth, reducing acquisition costs while increasing lifetime value"
                }
            ]
            
            lifecycle_cols = st.columns(4)
            for i, stage in enumerate(lifecycle_stages):
                with lifecycle_cols[i]:
                    with st.expander(f"{stage['icon']} {stage['name']}"):
                        st.markdown(f"**Improvement:** {stage['improvement']}")
                        st.markdown("**Key KPIs:**")
                        for kpi in stage['kpis']:
                            st.markdown(f"• {kpi}")
                        st.markdown(f"**Revenue Mechanism:** {stage['mechanism']}")
            
            if st.session_state.story_step == 1:
                if st.button("▶️ Continue Story: Discover the Business Outcomes", use_container_width=True):
                    st.session_state.story_step = 2
                    st.rerun()
        
        # Story Step 2: Business Outcomes
        if st.session_state.story_step >= 2:
            st.markdown("## 🏆 The Results - Five Key Business Outcomes")
            st.markdown("*These lifecycle improvements culminate in five transformational business outcomes...*")
            
            outcomes_data = [
                {"title": "Cost Reduction & Vendor Management", "target": "10-15% TCO reduction", "color": "#E74C3C", "kpis": ["TCO Reduction %", "Cloud Spend Optimization", "Vendor Cost Savings"]},
                {"title": "Security & Compliance Excellence", "target": ">95% compliance rate", "color": "#9B59B6", "kpis": ["Security Compliance Score", "Vulnerability Patching", "Incident Response"]},
                {"title": "Strategic Service Delivery", "target": ">90% customer satisfaction", "color": "#2ECC71", "kpis": ["Customer Satisfaction", "SLA Compliance", "Time to Market"]},
                {"title": "Innovation & AI Synergies", "target": "25-40% capability premium", "color": "#F39C12", "kpis": ["AI Integration Score", "Data Analytics Utilization", "Innovation Velocity"]},
                {"title": "Continuous Improvement", "target": "20-50% efficiency gains", "color": "#E67E22", "kpis": ["Predictive Analytics Accuracy", "Root Cause Resolution", "Event Correlation"]}
            ]
            
            # Display all 5 outcomes
            outcome_cols1 = st.columns(3)
            outcome_cols2 = st.columns(2)
            
            for i, outcome in enumerate(outcomes_data):
                col = outcome_cols1[i] if i < 3 else outcome_cols2[i-3]
                with col:
                    with st.expander(f"{outcome['title']}"):
                        st.markdown(f"**Target:** {outcome['target']}")
                        st.markdown("**Key KPIs:**")
                        for kpi in outcome['kpis']:
                            st.markdown(f"• {kpi}")
            
            if st.session_state.story_step == 2:
                if st.button("▶️ Continue Story: See How AI Amplifies Everything", use_container_width=True):
                    st.session_state.story_step = 3
                    st.rerun()
        
        # Story Step 3: AI Enhancement
        if st.session_state.story_step >= 3:
            st.markdown("## 🤖 The Amplifier - AI Impact on Performance")
            st.markdown("*Finally, AI acts as a force multiplier, amplifying every aspect of our framework...*")
            
            # Interactive AI impact sections
            ai_cols = st.columns(2)
            
            with ai_cols[0]:
                with st.expander("✅ SUCCESS FACTORS (58% Implementation Rate)"):
                    st.markdown("**Positive AI Impact:**")
                    st.markdown("• Sales Forecasting: Up to 50% accuracy improvement")
                    st.markdown("• Customer Acquisition: 20-30% cost reduction")
                    st.markdown("• Operational Efficiency: 20-25% productivity gains")
                    st.markdown("• Decision Speed: 50-70% faster cycles")
                    st.markdown("**Success Patterns:**")
                    st.markdown("• Business-centric approach focusing on outcomes")
                    st.markdown("• External partnerships with AI specialists")
                    st.markdown("• Comprehensive governance with multiple metrics")
            
            with ai_cols[1]:
                with st.expander("⚠️ RISK FACTORS (42% Failure Rate)"):
                    st.markdown("**Negative AI Impact:**")
                    st.markdown("• Project Failures: 80-95% never reach production")
                    st.markdown("• Zero ROI: 42% of enterprises see no return")
                    st.markdown("• Quality Issues: Increased errors and bias")
                    st.markdown("• Cost Overruns: Significant unexpected expenses")
                    st.markdown("**Common Failure Causes:**")
                    st.markdown("• Technology-first mindset without business alignment")
                    st.markdown("• Internal development without sufficient expertise")
                    st.markdown("• Single metric optimization (Goodhart's Law)")
            
            # Story conclusion
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 3rem; border-radius: 20px; text-align: center; margin: 2rem 0;">
                <h2 style="margin: 0 0 1rem 0; color: white;">🎯 The Complete Story</h2>
                <p style="margin: 0; font-size: 1.2em; line-height: 1.6;">28 Strategic KPIs → Drive Revenue Lifecycle Excellence → Achieve Business Outcomes → Amplified by AI, modernisation, and continuous integration</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Reset story button
            if st.button("🔄 Restart Story Journey", use_container_width=True):
                st.session_state.story_step = 0
                st.rerun()
    
    elif page == "5 Key Outcomes":
        st.title("🎯 Five Key Business Outcomes")
        st.markdown("*Strategic objectives driving the Managed Service Cloud Operations framework*")
        
        outcomes = create_outcome_overview()
        
        # Display outcomes in Atos brand style
        for i, outcome in enumerate(outcomes):
            st.markdown(f"""
            <div class="atos-secondary">
                <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                    <div style="background: #0070F3; color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem;">{i+1}</div>
                    <h2 style="margin: 0; color: #1A1A1A; font-size: 1.5em;">{outcome['title']}</h2>
                </div>
                <p style="color: #666666; font-size: 1.1em; line-height: 1.6; margin-bottom: 2rem;">{outcome['description']}</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                    <div>
                        <h4 style="color: #1A1A1A; margin-bottom: 1rem;">Key Performance Indicators</h4>
                        <ul style="color: #666666; margin: 0; padding-left: 1.5rem;">
                            {''.join([f'<li style="margin-bottom: 0.5rem;">{kpi}</li>' for kpi in outcome['kpis']])}
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #1A1A1A; margin-bottom: 1rem;">Target Impact</h4>
                        <div class="atos-accent" style="text-align: center;">
                            <span style="font-size: 1.3em; font-weight: bold;">{outcome['target']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    elif page == "KPI Performance Dashboard":
        st.title("📈 KPI Performance Dashboard")
        st.markdown("*Real-time monitoring of 28 strategic KPIs for Managed Service Cloud Operations*")
        
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
        st.markdown("*How Managed Service Cloud Operations KPIs create measurable business value across the customer journey*")
        
        # Header with Atos theme
        st.markdown("""
        <div class="atos-primary">
            <h2 style="margin: 0 0 1rem 0; font-size: 2.5em; color: white; text-align: center;">💰 REVENUE FLOW VISUALIZATION</h2>
            <p style="margin: 0; font-size: 1.3em; color: white; text-align: center;">Watch KPIs Drive Revenue Across the Customer Journey</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive revenue flow diagram using Streamlit columns
        st.markdown("""
        <div class="atos-secondary">
            <h3 style="text-align: center; color: #0066CC; margin-bottom: 2rem;">Revenue Lifecycle Flow</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create the flow using Streamlit columns
        flow_cols = st.columns([2, 1, 2, 1, 2, 1, 2])
        
        with flow_cols[0]:
            st.markdown("""
            <div style="text-align: center;">
                <div style="background: #0066CC; width: 120px; height: 120px; border-radius: 0; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; color: white; font-weight: bold; font-size: 1.1em;">
                    🎯<br>SALES
                </div>
                <h4 style="color: #0066CC; margin: 0; text-align: center;">Order Entry</h4>
            </div>
            """, unsafe_allow_html=True)
        
        with flow_cols[1]:
            st.markdown("<div style='text-align: center; font-size: 2em; color: #0066CC; padding-top: 3rem;'>→</div>", unsafe_allow_html=True)
        
        with flow_cols[2]:
            st.markdown("""
            <div style="text-align: center;">
                <div style="background: #0066CC; width: 120px; height: 120px; border-radius: 0; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; color: white; font-weight: bold; font-size: 1.1em;">
                    ⚡<br>DELIVERY
                </div>
                <h4 style="color: #0066CC; margin: 0; text-align: center;">Project Delivery</h4>
            </div>
            """, unsafe_allow_html=True)
        
        with flow_cols[3]:
            st.markdown("<div style='text-align: center; font-size: 2em; color: #0066CC; padding-top: 3rem;'>→</div>", unsafe_allow_html=True)
        
        with flow_cols[4]:
            st.markdown("""
            <div style="text-align: center;">
                <div style="background: #2C3E50; width: 120px; height: 120px; border-radius: 0; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; color: white; font-weight: bold; font-size: 1.1em;">
                    🛡️<br>OPERATIONS
                </div>
                <h4 style="color: #2C3E50; margin: 0; text-align: center;">Service Operations</h4>
            </div>
            """, unsafe_allow_html=True)
        
        with flow_cols[5]:
            st.markdown("<div style='text-align: center; font-size: 2em; color: #0066CC; padding-top: 3rem;'>→</div>", unsafe_allow_html=True)
        
        with flow_cols[6]:
            st.markdown("""
            <div style="text-align: center;">
                <div style="background: #FF6900; width: 120px; height: 120px; border-radius: 0; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; color: white; font-weight: bold; font-size: 1.1em;">
                    📈<br>GROWTH
                </div>
                <h4 style="color: #FF6900; margin: 0; text-align: center;">Customer Expansion</h4>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interactive stage selector
        st.markdown("### 🎮 Interactive Stage Explorer")
        st.markdown("*Click on any stage below to see detailed KPI performance metrics*")
        
        # Stage data with enhanced visuals
        stages = [
            {
                "stage": "🎯 Order Entry & Sales",
                "icon": "🎯",
                "color": "#0066CC",
                "objective": "Accelerate customer acquisition through operational excellence",
                "kpis": [
                    {"name": "Time to Market", "target": "30% reduction", "current": "85%", "impact": "15-30% sales velocity boost"},
                    {"name": "Innovation Velocity", "target": "2-3 initiatives/quarter", "current": "92%", "impact": "10-25% premium pricing"},
                    {"name": "Customer Satisfaction", "target": ">4.5/5.0", "current": "88%", "impact": "3-6 month cycle reduction"}
                ],
                "revenue_flow": "Faster service development → Competitive advantage → 30-60 day payment acceleration"
            },
            {
                "stage": "⚡ Project Delivery",
                "icon": "⚡",
                "color": "#2C3E50",
                "objective": "Optimize project profitability through operational efficiency",
                "kpis": [
                    {"name": "Automation Coverage", "target": ">80% processes", "current": "91%", "impact": "15-25% cost reduction"},
                    {"name": "Resource Utilization", "target": "70-85% optimal", "current": "78%", "impact": "10-20% revenue per consultant"},
                    {"name": "Change Success Rate", "target": ">95% success", "current": "96%", "impact": "5-10% margin improvement"}
                ],
                "revenue_flow": "Operational excellence → Higher margins → Faster cash collection → Customer satisfaction"
            },
            {
                "stage": "🛡️ Service Operations",
                "icon": "🛡️",
                "color": "#6B7280",
                "objective": "Protect recurring revenue streams through reliability",
                "kpis": [
                    {"name": "Service Availability", "target": "99.9% uptime", "current": "99.95%", "impact": "100% contracted revenue"},
                    {"name": "First Contact Resolution", "target": ">75% first contact", "current": "82%", "impact": "20-30% support cost reduction"},
                    {"name": "Cloud Optimization", "target": ">85% optimized", "current": "89%", "impact": "10-20% margin improvement"}
                ],
                "revenue_flow": "Operational excellence → Revenue protection → Cost reduction → Competitive advantage"
            },
            {
                "stage": "📈 Customer Expansion",
                "icon": "📈",
                "color": "#FF6900",
                "objective": "Drive account growth through service excellence",
                "kpis": [
                    {"name": "Customer Satisfaction", "target": ">4.5/5.0", "current": "4.7", "impact": "85%+ renewal correlation"},
                    {"name": "AI Integration Score", "target": ">60% integrated", "current": "72%", "impact": "25-40% higher revenue"},
                    {"name": "SLA Compliance", "target": ">99% compliance", "current": "99.2%", "impact": "15-25% expansion enablement"}
                ],
                "revenue_flow": "Service excellence → Customer satisfaction → Predictable growth → Reduced acquisition costs"
            }
        ]
        
        # Initialize session state for stage selection
        if 'selected_stage' not in st.session_state:
            st.session_state.selected_stage = 0
        
        # Stage selector buttons
        cols = st.columns(4)
        for i, stage in enumerate(stages):
            with cols[i]:
                if st.button(f"{stage['icon']} {stage['stage'].split(' ', 1)[1]}", key=f"stage_{i}", use_container_width=True):
                    st.session_state.selected_stage = i
                    st.rerun()
        
        # Display selected stage with enhanced visuals
        selected = stages[st.session_state.selected_stage]
        
        st.markdown(f"""
        <div class="atos-primary" style="text-align: center;">
            <div style="font-size: 4em; margin-bottom: 1rem;">{selected['icon']}</div>
            <h2 style="margin: 0 0 1rem 0; font-size: 2.2em; color: white;">{selected['stage']}</h2>
            <p style="margin: 0; font-size: 1.2em; color: white;">{selected['objective']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # KPI Performance Cards
        st.markdown("### 📊 Live KPI Performance Metrics")
        
        kpi_cols = st.columns(3)
        for i, kpi in enumerate(selected['kpis']):
            with kpi_cols[i]:
                # Simulate performance percentage
                performance = float(kpi['current'].rstrip('%')) if '%' in kpi['current'] else float(kpi['current']) * 20
                
                # Use Streamlit metric instead of complex HTML
                st.metric(
                    label=kpi['name'],
                    value=kpi['current'],
                    delta=f"Target: {kpi['target']}"
                )
                
                # Simple progress bar using Streamlit
                st.progress(min(performance/100, 1.0))
                
                # Impact description
                st.info(kpi['impact'])
        
        # Revenue Flow Mechanism
        st.markdown("### 💰 Revenue Flow Mechanism")
        st.markdown(f"""
        <div class="atos-dark" style="text-align: center;">
            <h3 style="margin: 0 0 1rem 0; font-size: 1.5em; color: white;">🔄 How This Stage Creates Revenue</h3>
            <p style="margin: 0; font-size: 1.2em; line-height: 1.6; color: white;">{selected['revenue_flow']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Overall Impact Dashboard
        st.markdown("### 🎯 Cumulative Revenue Impact")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="atos-primary" style="text-align: center;">
                <h3 style="margin: 0 0 1.5rem 0; color: white;">⚡ PERFORMANCE GAINS</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div class="atos-metric">
                        <h2 style="margin: 0; font-size: 2.5em; color: #0066CC;">30%</h2>
                        <p style="margin: 0.5rem 0 0 0; color: #2C3E50;">Sales Velocity</p>
                    </div>
                    <div class="atos-metric">
                        <h2 style="margin: 0; font-size: 2.5em; color: #0066CC;">25%</h2>
                        <p style="margin: 0.5rem 0 0 0; color: #2C3E50;">Delivery Speed</p>
                    </div>
                    <div class="atos-metric">
                        <h2 style="margin: 0; font-size: 2.5em; color: #0066CC;">99.9%</h2>
                        <p style="margin: 0.5rem 0 0 0; color: #2C3E50;">Reliability</p>
                    </div>
                    <div class="atos-metric">
                        <h2 style="margin: 0; font-size: 2.5em; color: #0066CC;">85%</h2>
                        <p style="margin: 0.5rem 0 0 0; color: #2C3E50;">Retention Rate</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="atos-dark" style="text-align: center;">
                <h3 style="margin: 0 0 1.5rem 0; color: white;">💰 REVENUE MECHANISMS</h3>
                <div style="text-align: left;">
                    <div class="atos-card" style="margin-bottom: 1rem; border-left: 4px solid #0066CC;">
                        <strong style="color: #0066CC;">Revenue Protection:</strong><br>
                        <span style="color: #2C3E50;">99.9% uptime maintains contracted revenue</span>
                    </div>
                    <div class="atos-card" style="margin-bottom: 1rem; border-left: 4px solid #0066CC;">
                        <strong style="color: #0066CC;">Revenue Acceleration:</strong><br>
                        <span style="color: #2C3E50;">30% faster time-to-market</span>
                    </div>
                    <div class="atos-card" style="margin-bottom: 1rem; border-left: 4px solid #0066CC;">
                        <strong style="color: #0066CC;">Revenue Expansion:</strong><br>
                        <span style="color: #2C3E50;">60%+ AI integration premium</span>
                    </div>
                    <div class="atos-card" style="border-left: 4px solid #0066CC;">
                        <strong style="color: #0066CC;">Cost Optimization:</strong><br>
                        <span style="color: #2C3E50;">80%+ automation coverage</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    elif page == "Traditional vs Modern KPIs":
        st.title("⚖️ Traditional vs Modern KPI Analysis")
        st.markdown("*Understanding maturity levels and adoption barriers in Managed Service Cloud Operations*")
        
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
        st.markdown("*The 58% vs 42% divide in AI implementation success for Managed Service Cloud Operations*")
        
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
        st.markdown("*Phased approach to Managed Service Cloud Operations KPI framework deployment*")
        
        # Investment priorities moved to top
        st.subheader("💰 Investment Priorities by ROI Timeline")
        
        st.markdown("""
        <div class="atos-dark" style="text-align: center;">
            <h3 style="margin-bottom: 2rem; color: white;">🎯 STRATEGIC INVESTMENT MATRIX</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
                <div class="atos-secondary" style="padding: 1.5rem; text-align: center;">
                    <h4 style="color: #0066CC;">🚀 IMMEDIATE</h4>
                    <p style="color: #2C3E50;"><strong>25% ROI</strong></p>
                    <p style="color: #6B7280;">Automation Coverage<br>Resource Utilization<br>Cloud Optimization</p>
                </div>
                <div class="atos-secondary" style="padding: 1.5rem; text-align: center;">
                    <h4 style="color: #FF6900;">⚡ MEDIUM</h4>
                    <p style="color: #2C3E50;"><strong>50% ROI</strong></p>
                    <p style="color: #6B7280;">Predictive Analytics<br>Service Management<br>Innovation Pipeline</p>
                </div>
                <div class="atos-secondary" style="padding: 1.5rem; text-align: center;">
                    <h4 style="color: #2C3E50;">🎖️ ADVANCED</h4>
                    <p style="color: #2C3E50;"><strong>70% ROI</strong></p>
                    <p style="color: #6B7280;">AI Decision Support<br>Technology Integration<br>Process Automation</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive phases without timeframes
        st.subheader("📋 Implementation Phases")
        
        phases = [
            {
                "name": "Foundation",
                "objectives": "Establish comprehensive KPI measurement capability",
                "priority_kpis": ["Customer Satisfaction Score", "Service Availability", "Resource Utilization Rate", "Security Compliance Score"],
                "success_criteria": "100% KPI data availability and accuracy"
            },
            {
                "name": "Optimization", 
                "objectives": "Achieve industry-leading performance on traditional KPIs",
                "priority_kpis": ["Automation Coverage", "Cloud Spend Optimization", "Deployment Frequency", "Predictive Analytics Accuracy"],
                "success_criteria": "Traditional KPIs at industry benchmark +10%"
            },
            {
                "name": "Advanced Capabilities", 
                "objectives": "Achieve competitive differentiation through advanced KPIs",
                "priority_kpis": ["Cloud/Data/AI Integration Score", "Innovation Pipeline Velocity", "Technology Modernization Index", "Event Correlation Effectiveness"],
                "success_criteria": "All modern KPIs performing at target levels"
            },
            {
                "name": "Continuous Evolution",
                "objectives": "Maintain competitive advantage through continuous improvement",
                "priority_kpis": ["Emerging Technology KPIs", "Market Leadership Metrics", "Global Scaling Indicators"],
                "success_criteria": "Sustained superior performance across all categories"
            }
        ]
        
        phase_cols = st.columns(2)
        for i, phase in enumerate(phases):
            col = phase_cols[i % 2]
            with col:
                with st.expander(f"Phase {i+1}: {phase['name']}"):
                    st.markdown(f"**Objectives:** {phase['objectives']}")
                    st.markdown("**Priority KPIs:**")
                    for kpi in phase['priority_kpis']:
                        st.markdown(f"• {kpi}")
                    st.markdown(f"**Success Criteria:** {phase['success_criteria']}")
    
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