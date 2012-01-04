%global packname  features
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.8.2
Release:          1%{?dist}
Summary:          Feature Extraction for Discretely-Sampled Functional Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.8-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lokern 

BuildRequires:    R-devel tex(latex) R-lokern 

%description
Discretely-sampled function is first smoothed.  Features of the smoothed
function are then extracted.  Some of the key features include mean value,
first and second derivatives, critical points (i.e. local maxima and
minima), curvature of cunction at critical points, wiggliness of the
function, noise in data, and outliers in data.

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
%doc %{rlibdir}/features/DESCRIPTION
%doc %{rlibdir}/features/html
%doc %{rlibdir}/features/NEWS
%{rlibdir}/features/NAMESPACE
%{rlibdir}/features/demo
%{rlibdir}/features/help
%{rlibdir}/features/INDEX
%{rlibdir}/features/Meta
%{rlibdir}/features/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.8.2-1
- initial package for Fedora