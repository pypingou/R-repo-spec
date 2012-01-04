%global packname  pamm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Power analysis for random effects in mixed models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lme4 R-mvtnorm R-gmodels 


BuildRequires:    R-devel tex(latex) R-lme4 R-mvtnorm R-gmodels



%description
Simulation functions to assess or explore the power of a dataset to
estimates significant random effects (intercept or slope) in a mixed
model. The functions are based on the "lme4" package.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora