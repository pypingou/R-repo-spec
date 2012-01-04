%global packname  languageR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Data sets and functions with "Analyzing Linguistic Data: A practical introduction to statistics".

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lme4 
Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods R-lme4
BuildRequires:    R-methods 


%description
Data sets exemplifying statistical methods, and some facilitatory utility
functions used in "Analyzing Linguistic Data: A practical introduction to
statistics using R", Cambridge University Press, 2008.

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
%doc %{rlibdir}/languageR/DESCRIPTION
%doc %{rlibdir}/languageR/html
%{rlibdir}/languageR/Meta
%{rlibdir}/languageR/help
%{rlibdir}/languageR/data
%{rlibdir}/languageR/R
%{rlibdir}/languageR/INDEX
%{rlibdir}/languageR/scripts
%{rlibdir}/languageR/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora