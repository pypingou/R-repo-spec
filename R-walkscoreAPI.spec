%global packname  walkscoreAPI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{dist}
Summary:          Walk Score and Transit Score API

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions to perform the Application Programming Interface
(API) calls associated with the Walk Score website (www.walkscore.com)
within the R environment. These functions can be used to query the Walk
Score and Tranist Score database for a wide variety of information using R
scripts. This package includes the simple Walk Score and Transit Score AI
calls, which return the scores associated with an input location, as well
as calls which return some data used to calculate the scores. These
functions are especially useful for mass data collection and gathering
Walk Score and Transit Score values for large lists of locations.

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
%doc %{rlibdir}/walkscoreAPI/html
%doc %{rlibdir}/walkscoreAPI/DESCRIPTION
%{rlibdir}/walkscoreAPI/NAMESPACE
%{rlibdir}/walkscoreAPI/help
%{rlibdir}/walkscoreAPI/Meta
%{rlibdir}/walkscoreAPI/INDEX
%{rlibdir}/walkscoreAPI/R

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- Update to version 1.2

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora