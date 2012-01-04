%global packname  pscl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04.1
Release:          1%{?dist}
Summary:          Political Science Computational Laboratory, Stanford University

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-stats R-mvtnorm R-coda R-gam R-vcd 
Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-stats R-mvtnorm R-coda R-gam R-vcd
BuildRequires:    R-lattice 


%description
Bayesian analysis of item-response theory (IRT) models, roll call
analysis; computing highest density regions; maximum likelihood estimation
of zero-inflated and hurdle models for count data; goodness-of-fit
measures for GLMs; data sets used in writing and teaching at the Political
Science Computational Laboratory; seats-votes curves.

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
%doc %{rlibdir}/pscl/html
%doc %{rlibdir}/pscl/doc
%doc %{rlibdir}/pscl/NEWS
%doc %{rlibdir}/pscl/CITATION
%doc %{rlibdir}/pscl/DESCRIPTION
%{rlibdir}/pscl/data
%{rlibdir}/pscl/Meta
%{rlibdir}/pscl/R
%{rlibdir}/pscl/NAMESPACE
RPM build errors:
%{rlibdir}/pscl/help
%{rlibdir}/pscl/INDEX
%{rlibdir}/pscl/libs

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04.1-1
- initial package for Fedora