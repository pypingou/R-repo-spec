%global packname  evdbayes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Bayesian Analysis in Extreme Value Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides functions for the bayesian analysis of extreme value models,
using MCMC methods.

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
%doc %{rlibdir}/evdbayes/html
%doc %{rlibdir}/evdbayes/DESCRIPTION
%doc %{rlibdir}/evdbayes/doc
%{rlibdir}/evdbayes/data
%{rlibdir}/evdbayes/CHANGES
%{rlibdir}/evdbayes/libs
%{rlibdir}/evdbayes/R
%{rlibdir}/evdbayes/Meta
%{rlibdir}/evdbayes/README
%{rlibdir}/evdbayes/NAMESPACE
%{rlibdir}/evdbayes/help
%{rlibdir}/evdbayes/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora