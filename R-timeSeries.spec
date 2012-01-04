%global packname  timeSeries
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2130.92
Release:          1%{?dist}
Summary:          Rmetrics - Financial Time Series Objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-grDevices R-methods R-stats R-utils R-timeDate 

BuildRequires:    R-devel tex(latex) R-graphics R-grDevices R-methods R-stats R-utils R-timeDate 

%description
Environment for teaching "Financial Engineering and Computational Finance"

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
%doc %{rlibdir}/timeSeries/html
%doc %{rlibdir}/timeSeries/DESCRIPTION
%doc %{rlibdir}/timeSeries/COPYING
%{rlibdir}/timeSeries/unitTests
%{rlibdir}/timeSeries/COPYRIGHTS
%{rlibdir}/timeSeries/Meta
%{rlibdir}/timeSeries/data
%{rlibdir}/timeSeries/NAMESPACE
%{rlibdir}/timeSeries/R
%{rlibdir}/timeSeries/INDEX
%{rlibdir}/timeSeries/help
%{rlibdir}/timeSeries/THANKS
%{rlibdir}/timeSeries/README

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2130.92-1
- initial package for Fedora