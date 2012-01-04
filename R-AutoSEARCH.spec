%global packname  AutoSEARCH
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          General-to-Specific (GETs) Model Selection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-zoo 

BuildRequires:    R-devel tex(latex) R-zoo 

%description
Multi-path General-to-Specific (GETS) model selection of the mean and
log-volatility specifications of a power log-ARCH model

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
%doc %{rlibdir}/AutoSEARCH/DESCRIPTION
%doc %{rlibdir}/AutoSEARCH/html
%{rlibdir}/AutoSEARCH/INDEX
%{rlibdir}/AutoSEARCH/help
%{rlibdir}/AutoSEARCH/R
%{rlibdir}/AutoSEARCH/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora