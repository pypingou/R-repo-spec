%global packname  PCIT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04.3
Release:          1%{?dist}
Summary:          PCIT algorithm - Partial Correlation Coefficient with Information Theory

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.04-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides the necessary functions for performing the Partial
Correlation coefficient with Information Theory (PCIT) algorithm developed
by Reverter and Chan (2008). The PCIT algorithm identifies meaningful
correlations to define edges in a weighted network. The algorithm can be
applied to any correlation-based network including but not limited to gene
co-expression networks.

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
%doc %{rlibdir}/PCIT/CITATION
%doc %{rlibdir}/PCIT/DESCRIPTION
%doc %{rlibdir}/PCIT/html
%{rlibdir}/PCIT/INDEX
%{rlibdir}/PCIT/data
%{rlibdir}/PCIT/R
%{rlibdir}/PCIT/NAMESPACE
%{rlibdir}/PCIT/libs
%{rlibdir}/PCIT/Meta
%{rlibdir}/PCIT/demo
%{rlibdir}/PCIT/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04.3-1
- initial package for Fedora