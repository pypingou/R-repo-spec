%global packname  LoopAnalyst
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          A collection of tools to conduct Levins' Loop Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
Loop analysis makes qualitative predictions of variable change in a system
of causally interdependent variabless, where "qualitative" means sign only
(i.e. increases, decreases, non change, and ambiguous). This
implementation includes output support for graphs in .dot file format for
use with visualization software such as graphviz (graphviz.org). Loop
Analyst provides tools for the construction and output of community
matrices, computation and output of community effect matrices, tables of
correlations, adjoint, absolute feedback, weighted feedback and weighted
prediction matrices, change in life expectancy matrices, and feedback,
path and loop enumeration tools.

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
%doc %{rlibdir}/LoopAnalyst/DESCRIPTION
%doc %{rlibdir}/LoopAnalyst/html
%{rlibdir}/LoopAnalyst/R
%{rlibdir}/LoopAnalyst/Meta
%{rlibdir}/LoopAnalyst/INDEX
%{rlibdir}/LoopAnalyst/data
%{rlibdir}/LoopAnalyst/NAMESPACE
%{rlibdir}/LoopAnalyst/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora