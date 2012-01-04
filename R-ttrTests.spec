%global packname  ttrTests
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Standard Backtests for Technical Trading Rules in Financial Data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fTrading R-TTR 


BuildRequires:    R-devel tex(latex) R-fTrading R-TTR



%description
Five core functions evaluate the efficacy of a technical trading rule. -
Conditional return statistics - Bootstrap resampling statistics - Reality
Check for data snooping bias among parameter choices - Robustness, or
Persistence, of parameter choices - Parameter Domain Correlation Test

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7-1
- initial package for Fedora