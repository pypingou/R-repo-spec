%global packname  lmmfit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Goodness-of-fit-measures for linear mixed models with one-level-grouping

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme R-MASS 

BuildRequires:    R-devel tex(latex) R-nlme R-MASS 

%description
Package lmmfit contains three functions evaluating some
goodness-of-fit-measures for linear mixed models with one-level-grouping
fitted using lme() from package nlme.

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
%doc %{rlibdir}/lmmfit/DESCRIPTION
%doc %{rlibdir}/lmmfit/html
%{rlibdir}/lmmfit/NAMESPACE
%{rlibdir}/lmmfit/help
%{rlibdir}/lmmfit/Meta
%{rlibdir}/lmmfit/R
%{rlibdir}/lmmfit/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora