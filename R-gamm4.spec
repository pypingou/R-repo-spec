%global packname  gamm4
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Generalized additive mixed models using mgcv and lme4

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-Matrix R-lme4 R-mgcv 


BuildRequires:    R-devel tex(latex) R-methods R-Matrix R-lme4 R-mgcv



%description
Fit generalized additive mixed models via a version of mgcv's gamm
function, using lme4 for estimation via Fabian Scheipl's trick.

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
%doc %{rlibdir}/gamm4/html
%doc %{rlibdir}/gamm4/DESCRIPTION
%{rlibdir}/gamm4/help
%{rlibdir}/gamm4/Meta
%{rlibdir}/gamm4/NAMESPACE
%{rlibdir}/gamm4/INDEX
%{rlibdir}/gamm4/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora