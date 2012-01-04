%global packname  KMsurv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Data sets from Klein and Moeschberger (1997), Survival Analysis

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Data sets and functions for Klein and Moeschberger (1997), "Survival
Analysis, Techniques for Censored and Truncated Data", Springer.

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
%doc %{rlibdir}/KMsurv/html
%doc %{rlibdir}/KMsurv/DESCRIPTION
%{rlibdir}/KMsurv/help
%{rlibdir}/KMsurv/Meta
%{rlibdir}/KMsurv/data
%{rlibdir}/KMsurv/NAMESPACE
%{rlibdir}/KMsurv/INDEX
%{rlibdir}/KMsurv/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora