%global packname  qualityTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.49
Release:          1%{?dist}
Summary:          Statistical Methods for Quality Science

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-methods 

BuildRequires:    R-devel tex(latex) R-graphics R-methods 

%description
This Package contains methods associated with the Define, Measure,
Analyze, Improve and Control (i.e. DMAIC) cycle of the Six Sigma Quality
Management methodology.It covers distribution fitting, normal and
non-normal process capability indices, techniques for Measurement Systems
Analysis especially gage capability indices and Gage Repeatability (i.e
Gage RR) and Reproducibility studies, factorial and fractional factorial
designs as well as response surface methods including the use of
desirability functions. Improvement via Six Sigma is project based
strategy that covers 5 phases: Define - Pareto Chart; Measure -
Probability and Quantile-Quantile Plots, Process Capability Indices for
various distributions and Gage RR Analyze i.e. Pareto Chart, Multi-Vari
Chart, Dot Plot; Improve - Full and fractional factorial, response surface
and mixture designs as well as the desirability approach for simultaneous
optimization of more than one response variable. Normal, Pareto and Lenth
Plot of effects as well as Interaction Plots; Control - Quality Control
Charts can be found in the qcc package. The focus is on teaching the
statistical methodology used in the Quality Sciences.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/qualityTools/doc
%doc %{rlibdir}/qualityTools/CITATION
%doc %{rlibdir}/qualityTools/DESCRIPTION
%doc %{rlibdir}/qualityTools/html
%{rlibdir}/qualityTools/NAMESPACE
%{rlibdir}/qualityTools/help
%{rlibdir}/qualityTools/NEWS.Rd
%{rlibdir}/qualityTools/R
%{rlibdir}/qualityTools/INDEX
%{rlibdir}/qualityTools/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.49-1
- initial package for Fedora