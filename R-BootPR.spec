%global packname  BootPR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.58
Release:          1%{?dist}
Summary:          Bootstrap Prediction Intervals and Bias-Corrected Forecasting

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-zoo R-combinat 

BuildRequires:    R-devel tex(latex) R-zoo R-combinat 

%description
Bias-Corrected Forecasting and Bootstrap Prediction Intervals for
Autoregressive Time Series

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.58-1
- initial package for Fedora