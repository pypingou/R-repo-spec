%global packname  cotrend
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Consistant Cotrend Rank Selection

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xts 


BuildRequires:    R-devel tex(latex) R-xts



%description
Implements cointegration/cotrending rank selection algorithm in Guo and
Shintani(2011). Paper: "Consistant Cotrending rank selection when both
stochastic and nonlinear deterministic trends are present", Preprint, Feb

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
%doc %{rlibdir}/cotrend/html
%doc %{rlibdir}/cotrend/DESCRIPTION
%{rlibdir}/cotrend/R
%{rlibdir}/cotrend/NAMESPACE
%{rlibdir}/cotrend/help
%{rlibdir}/cotrend/INDEX
%{rlibdir}/cotrend/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora